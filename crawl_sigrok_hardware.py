#!/usr/bin/env python3
"""
Crawl sigrok wiki to generate hardware device pages for OpenTraceLab
"""

import os
import re
import requests
from pathlib import Path
from urllib.parse import urljoin, urlparse
import time

BASE_URL = "https://sigrok.org"
WIKI_URL = f"{BASE_URL}/wiki"
HW_DIR = Path("hw")

# Device type mappings from sigrok categories
DEVICE_TYPES = {
    "Logic analyzer": "logic-analyzer",
    "Multimeter": "multimeter", 
    "Oscilloscope": "oscilloscope",
    "Power supply": "power-supply",
    "Function generator": "function-generator",
    "Thermometer": "thermometer",
    "Sound level meter": "sound-level-meter",
    "LCR meter": "lcr-meter",
    "Frequency counter": "frequency-counter",
    "Spectrum analyzer": "spectrum-analyzer",
    "Programmable load": "programmable-load"
}

def get_all_supported_devices():
    """Get all supported devices from sigrok wiki"""
    print("Fetching supported hardware list...")
    url = f"{WIKI_URL}/Supported_hardware"
    response = requests.get(url)
    content = response.text
    
    devices = []
    current_type = "misc-devices"
    
    # Parse content by sections
    sections = re.split(r'<h[2-6][^>]*>([^<]+)</h[2-6]>', content)
    
    for i in range(1, len(sections), 2):
        section_title = sections[i].strip()
        section_content = sections[i+1] if i+1 < len(sections) else ""
        
        # Map section titles to device types
        if "logic analyzer" in section_title.lower():
            current_type = "logic-analyzer"
        elif "multimeter" in section_title.lower():
            current_type = "multimeter"
        elif "oscilloscope" in section_title.lower():
            current_type = "oscilloscope"
        elif "power suppl" in section_title.lower():
            current_type = "power-supply"
        elif "function generator" in section_title.lower():
            current_type = "function-generator"
        elif "thermometer" in section_title.lower():
            current_type = "thermometer"
        else:
            current_type = "misc-devices"
        
        # Find device links in this section
        section_links = re.findall(r'<a[^>]*href="(/wiki/[^"]*)"[^>]*>([^<]+)</a>', section_content)
        
        for device_url, device_name in section_links:
            # Skip non-device links
            if any(skip in device_url.lower() for skip in ['category:', 'file:', 'template:', 'help:', 'special:']):
                continue
            
            # Only include devices that look like hardware devices
            if len(device_name) > 3 and not device_name.lower() in ['supported', 'planned', 'work in progress']:
                slug = device_name.lower().replace(' ', '-').replace('/', '-').replace('(', '').replace(')', '').replace('&', '').strip('-')
                devices.append({
                    'name': device_name.strip(),
                    'url': urljoin(BASE_URL, device_url),
                    'type': current_type,
                    'slug': slug
                })
    
    # Remove duplicates
    seen = set()
    unique_devices = []
    for device in devices:
        key = (device['name'], device['url'])
        if key not in seen:
            seen.add(key)
            unique_devices.append(device)
    
    print(f"Found {len(unique_devices)} supported devices")
    return unique_devices

def download_image(img_url, dest_path):
    """Download image with highest resolution available"""
    try:
        # For MediaWiki, convert thumbnail URLs to full size
        if '/thumb/' in img_url:
            # Extract original filename from thumbnail path
            # /wiki/images/thumb/a/ab/Filename.jpg/120px-Filename.jpg -> /wiki/images/a/ab/Filename.jpg
            parts = img_url.split('/thumb/')
            if len(parts) == 2:
                base_path = parts[0]
                thumb_path = parts[1]
                # Extract the original path: a/ab/Filename.jpg from a/ab/Filename.jpg/120px-Filename.jpg
                original_path = '/'.join(thumb_path.split('/')[:-1])
                full_url = f"{base_path}/{original_path}"
                img_url = full_url
        
        response = requests.get(img_url, stream=True)
        response.raise_for_status()
        
        with open(dest_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        
        return True
    except Exception as e:
        print(f"Failed to download {img_url}: {e}")
        return False

def extract_infobox_data(content):
    """Extract infobox data from wiki page"""
    infobox = {}
    
    # Find infobox table - look for the device info table
    infobox_match = re.search(r'<table[^>]*class="[^"]*infobox[^"]*"[^>]*>(.*?)</table>', content, re.DOTALL)
    if not infobox_match:
        # Try alternative patterns
        infobox_match = re.search(r'<table[^>]*style="[^"]*float:\s*right[^"]*"[^>]*>(.*?)</table>', content, re.DOTALL)
    
    if not infobox_match:
        return infobox
    
    infobox_content = infobox_match.group(1)
    
    # Extract rows
    rows = re.findall(r'<tr[^>]*>(.*?)</tr>', infobox_content, re.DOTALL)
    for row in rows:
        # Extract key-value pairs from th/td or td/td
        cells = re.findall(r'<t[hd][^>]*>(.*?)</t[hd]>', row, re.DOTALL)
        if len(cells) == 2:
            key = re.sub(r'<[^>]+>', '', cells[0]).strip()
            value_html = cells[1].strip()
            
            # Preserve links in values (especially for Source code)
            if 'href=' in value_html:
                # Convert links to markdown
                value = re.sub(r'<a[^>]*href="([^"]*)"[^>]*>([^<]+)</a>', r'[\2](\1)', value_html)
                value = re.sub(r'<[^>]+>', '', value).strip()
                
                # Convert sigrok links to OpenTraceLab links
                if 'sigrok.org/gitweb' in value and 'libsigrok.git' in value:
                    # Extract the hardware path
                    path_match = re.search(r'f=src/hardware/([^)]+)', value)
                    if path_match:
                        hardware_path = path_match.group(1)
                        new_url = f"https://github.com/OpenTraceLab/OpenTraceCapture/tree/main/src/hardware/{hardware_path}"
                        # Replace the URL in the markdown link
                        value = re.sub(r'\(http://sigrok\.org/gitweb/[^)]+\)', f'({new_url})', value)
            else:
                value = re.sub(r'<[^>]+>', '', value_html).strip()
            
            # Clean up HTML entities
            key = key.replace('&nbsp;', ' ').replace('&#8212;', '—')
            value = value.replace('&nbsp;', ' ').replace('&#8212;', '—')
            if key and value and key.lower() not in ['device', 'picture']:
                infobox[key] = value
    
    return infobox

def process_images(content, device_slug, device_type):
    """Use existing downloaded images"""
    img_dir = HW_DIR / device_type / device_slug / "img"
    images = []
    
    # Use existing images if directory exists
    if img_dir.exists():
        for img_file in img_dir.glob('*'):
            if img_file.suffix.lower() in ['.jpg', '.png', '.gif']:
                clean_alt = img_file.stem.replace('_', ' ').replace('-', ' ')
                images.append({
                    'filename': img_file.name,
                    'alt': clean_alt,
                    'path': f"./img/{img_file.name}"
                })
    
    return images

def html_to_markdown(html_content):
    """Convert HTML content to proper Markdown"""
    # Remove infobox and navigation elements first
    html_content = re.sub(r'<table[^>]*class="[^"]*infobox[^"]*"[^>]*>.*?</table>', '', html_content, flags=re.DOTALL)
    html_content = re.sub(r'<table[^>]*style="[^"]*float:\s*right[^"]*"[^>]*>.*?</table>', '', html_content, flags=re.DOTALL)
    # Remove ToC completely
    html_content = re.sub(r'<div[^>]*class="[^"]*toc[^"]*"[^>]*>.*?</div>', '', html_content, flags=re.DOTALL)
    
    # Convert headers (handle both patterns)
    html_content = re.sub(r'<h([1-6])[^>]*><span[^>]*>(.*?)</span></h\1>', lambda m: '#' * int(m.group(1)) + ' ' + m.group(2), html_content)
    html_content = re.sub(r'<h([1-6])[^>]*>(.*?)</h\1>', lambda m: '#' * int(m.group(1)) + ' ' + m.group(2), html_content)
    
    # Convert bold and italic
    html_content = re.sub(r'<(?:b|strong)[^>]*>(.*?)</(?:b|strong)>', r'**\1**', html_content)
    html_content = re.sub(r'<(?:i|em)[^>]*>(.*?)</(?:i|em)>', r'*\1*', html_content)
    
    # Convert links
    html_content = re.sub(r'<a[^>]*href="([^"]*)"[^>]*>(.*?)</a>', r'[\2](\1)', html_content)
    
    # Convert code
    html_content = re.sub(r'<(?:code|tt)[^>]*>(.*?)</(?:code|tt)>', r'`\1`', html_content)
    html_content = re.sub(r'<pre[^>]*>(.*?)</pre>', r'```\n\1\n```', html_content, flags=re.DOTALL)
    
    # Convert tables
    def convert_table(match):
        table_html = match.group(0)
        rows = re.findall(r'<tr[^>]*>(.*?)</tr>', table_html, re.DOTALL)
        if not rows:
            return ""
        
        md_table = []
        for i, row in enumerate(rows):
            cells = re.findall(r'<t[hd][^>]*>(.*?)</t[hd]>', row, re.DOTALL)
            if cells:
                # Clean cell content
                clean_cells = [re.sub(r'<[^>]+>', '', cell).strip() for cell in cells]
                md_table.append('| ' + ' | '.join(clean_cells) + ' |')
                
                # Add header separator after first row
                if i == 0:
                    md_table.append('|' + '---|' * len(clean_cells))
        
        return '\n'.join(md_table) + '\n'
    
    html_content = re.sub(r'<table[^>]*>.*?</table>', convert_table, html_content, flags=re.DOTALL)
    
    # Convert lists
    html_content = re.sub(r'<li[^>]*>(.*?)</li>', r'- \1', html_content, flags=re.DOTALL)
    html_content = re.sub(r'</?[uo]l[^>]*>', '', html_content)
    
    # Convert line breaks
    html_content = re.sub(r'<br[^>]*/?>', '\n', html_content)
    html_content = re.sub(r'<p[^>]*>', '\n', html_content)
    html_content = re.sub(r'</p>', '\n', html_content)
    
    # Remove remaining HTML tags
    html_content = re.sub(r'<[^>]+>', '', html_content)
    
    # Clean up whitespace and entities
    html_content = re.sub(r'&nbsp;', ' ', html_content)
    html_content = re.sub(r'&#8212;', '—', html_content)
    html_content = re.sub(r'&amp;', '&', html_content)
    html_content = re.sub(r'&lt;', '<', html_content)
    html_content = re.sub(r'&gt;', '>', html_content)
    html_content = re.sub(r'\n\s*\n\s*\n', '\n\n', html_content)
    
    return html_content.strip()

def consolidate_linked_pages(content, base_url):
    """Consolidate linked wiki pages (like /Info pages)"""
    consolidated = content
    
    # Find links to /Info pages
    info_links = re.findall(r'<a[^>]*href="([^"]*/(Info|Protocol))"[^>]*>', content)
    
    for link_path, _ in info_links:
        try:
            info_url = urljoin(base_url, link_path)
            response = requests.get(info_url)
            info_content = response.text
            
            # Extract main content
            main_match = re.search(r'<div[^>]*class="mw-parser-output"[^>]*>(.*?)</div>', info_content, re.DOTALL)
            if main_match:
                info_text = main_match.group(1)
                # Convert to text and append
                info_text = re.sub(r'<[^>]+>', '', info_text)
                info_text = re.sub(r'\s+', ' ', info_text).strip()
                consolidated += f"\n\n## Additional Information\n\n{info_text}"
            
        except Exception as e:
            print(f"Warning: Could not consolidate {link_path}: {e}")
    
    return consolidated

def create_device_page(device, current, total):
    """Create device page with infobox and photo grid"""
    print(f"[{current}/{total}] Processing {device['name']} ({device['type']})...")
    
    try:
        response = requests.get(device['url'])
        response.raise_for_status()
        content = response.text
        
        # Consolidate linked pages
        content = consolidate_linked_pages(content, device['url'])
        
        # Extract infobox data
        infobox = extract_infobox_data(content)
        
        # Process images
        images = process_images(content, device['slug'], device['type'])
        
        # Extract main content - get the COMPLETE mw-parser-output div
        main_match = re.search(r'<div[^>]*class="mw-parser-output"[^>]*>(.*?)</div>\s*</div>\s*</div>', content, re.DOTALL)
        if not main_match:
            # Fallback pattern
            main_match = re.search(r'<div[^>]*class="mw-parser-output"[^>]*>(.*)', content, re.DOTALL)
        
        if main_match:
            full_content = main_match.group(1)
            # Find where the main content ends (before footer/navigation)
            end_match = re.search(r'(.*?)(?:<div[^>]*class="printfooter"|<div[^>]*id="catlinks"|$)', full_content, re.DOTALL)
            if end_match:
                full_content = end_match.group(1)
            
            main_content = html_to_markdown(full_content)
        else:
            main_content = ""
        
        # Create markdown content
        md_content = f"""---
title: {device['name']}
---

# {device['name']}

<div class="infobox" markdown>

"""
        
        # Add main image if available
        if images:
            md_content += f"![{device['name']}]({images[0]['path']}){{ .infobox-image }}\n\n"
        
        md_content += f"### {device['name']}\n\n| | |\n|---|---|\n"
        
        # Add infobox data
        for key, value in infobox.items():
            md_content += f"| **{key}** | {value} |\n"
        
        md_content += "\n</div>\n\n"
        
        # Add main content
        if main_content:
            md_content += main_content + "\n\n"
        
        # Don't add photo grid at end since it's already in main content
        
        # Write file
        device_dir = HW_DIR / device['type'] / device['slug']
        device_dir.mkdir(parents=True, exist_ok=True)
        
        with open(device_dir / "index.md", 'w', encoding='utf-8') as f:
            f.write(md_content)
        
        time.sleep(0.5)  # Be nice to the server
        
    except Exception as e:
        print(f"  ERROR: {e}")
        # Create error page
        device_dir = HW_DIR / device['type'] / device['slug']
        device_dir.mkdir(parents=True, exist_ok=True)
        
        error_content = f"""---
title: {device['name']}
---

# {device['name']}

<!-- Warning: Error processing this device page: {e} -->
<!-- Please manually review and fix this page -->

Source: {device['url']}
"""
        
        with open(device_dir / "index.md", 'w', encoding='utf-8') as f:
            f.write(error_content)

def main():
    """Main function"""
    print("Crawling ALL sigrok supported hardware...")
    
    # Create hw directory
    HW_DIR.mkdir(exist_ok=True)
    
    # Get all supported devices
    devices = get_all_supported_devices()
    
    # Process each device
    for i, device in enumerate(devices, 1):
        create_device_page(device, i, len(devices))
    
    print(f"\nCompleted! Processed {len(devices)} devices.")
    
    # Print summary by category
    categories = {}
    for device in devices:
        categories[device['type']] = categories.get(device['type'], 0) + 1
    
    print("\nDevices by category:")
    for category, count in sorted(categories.items()):
        print(f"  {category}: {count} devices")

if __name__ == "__main__":
    main()
