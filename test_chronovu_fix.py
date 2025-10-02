#!/usr/bin/env python3
"""
Test script to fix ChronoVu LA8 page with proper captions and full content
"""

import os
import re
import requests
from pathlib import Path
from urllib.parse import urljoin

BASE_URL = "https://sigrok.org"
WIKI_URL = f"{BASE_URL}/wiki"
HW_DIR = Path("hw")

def html_to_markdown(html_content):
    """Convert HTML content to proper Markdown"""
    # Remove infobox and navigation elements first
    html_content = re.sub(r'<table[^>]*class="[^"]*infobox[^"]*"[^>]*>.*?</table>', '', html_content, flags=re.DOTALL)
    html_content = re.sub(r'<table[^>]*style="[^"]*float:\s*right[^"]*"[^>]*>.*?</table>', '', html_content, flags=re.DOTALL)
    
    # Remove ToC completely
    html_content = re.sub(r'<div[^>]*class="[^"]*toc[^"]*"[^>]*>.*?</div>', '', html_content, flags=re.DOTALL)
    
    # Remove Photos section completely (we'll replace with photo-grid)
    html_content = re.sub(r'<h2><span[^>]*id="Photos"[^>]*>.*?</span></h2>.*?(?=<h2|<div[^>]*class="printfooter"|$)', '', html_content, flags=re.DOTALL)
    
    # Convert headers
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

def extract_infobox_data(content):
    """Extract infobox data from wiki page"""
    infobox = {}
    
    # Find infobox table
    infobox_match = re.search(r'<table[^>]*class="[^"]*infobox[^"]*"[^>]*>(.*?)</table>', content, re.DOTALL)
    if not infobox_match:
        infobox_match = re.search(r'<table[^>]*style="[^"]*float:\s*right[^"]*"[^>]*>(.*?)</table>', content, re.DOTALL)
    
    if not infobox_match:
        return infobox
    
    infobox_content = infobox_match.group(1)
    
    # Extract rows
    rows = re.findall(r'<tr[^>]*>(.*?)</tr>', infobox_content, re.DOTALL)
    for row in rows:
        cells = re.findall(r'<t[hd][^>]*>(.*?)</t[hd]>', row, re.DOTALL)
        if len(cells) == 2:
            key = re.sub(r'<[^>]+>', '', cells[0]).strip()
            value_html = cells[1].strip()
            
            # Preserve links in values (especially for Source code)
            if 'href=' in value_html:
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
            
            key = key.replace('&nbsp;', ' ').replace('&#8212;', '—')
            value = value.replace('&nbsp;', ' ').replace('&#8212;', '—')
            if key and value and key.lower() not in ['device', 'picture']:
                infobox[key] = value
    
    return infobox

def get_image_captions():
    """Get proper image captions from original page"""
    return {
        'Chronovu_la8_device.jpg': 'Device with probes',
        'Chronovu_la8_front.jpg': 'Device, front', 
        'Chronovu_la8_back.jpg': 'Device, back',
        'Chronovu_la8_usb.jpg': 'USB and LEDs',
        'Chronovu_la8_probes.jpg': 'Probe connector',
        'Chronovu_la8_pcb_front.jpg': 'PCB, front',
        'Chronovu_la8_pcb_back.jpg': 'PCB, back',
        'Chronovu_la8_xilinx.jpg': 'Xilinx CPLD',
        'Chronovu_la8_sdram_mt48lc4m16a2.jpg': 'SDRAM chip',
        'Chronovu_la8_ftdi_ft245rl.jpg': 'FTDI chip',
        'Chronovu_la8_lxh244a.jpg': 'LXH244A',
        'Chronovu_la8_pt70151.jpg': 'PT70151',
        'Chronovu_la8_wires.jpg': 'Custom wire',
        'Chronovu_la8_front.png': 'ChronoVu LA8'
    }

def main():
    print("Fixing ChronoVu LA8 page...")
    
    # Get page content
    url = f"{WIKI_URL}/ChronoVu_LA8"
    response = requests.get(url)
    content = response.text
    
    # Extract infobox and content
    infobox = extract_infobox_data(content)
    
    # Extract main content - find the COMPLETE mw-parser-output div
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
        print("Warning: Could not extract main content")
    
    # Get images with proper captions
    img_dir = HW_DIR / "misc-devices" / "chronovu-la8" / "img"
    captions = get_image_captions()
    images = []
    
    if img_dir.exists():
        for img_file in img_dir.glob('*'):
            if img_file.suffix.lower() in ['.jpg', '.png', '.gif']:
                caption = captions.get(img_file.name, img_file.stem.replace('_', ' '))
                images.append({
                    'filename': img_file.name,
                    'alt': caption,
                    'path': f"./img/{img_file.name}"
                })
    
    # Create markdown content
    md_content = f"""---
title: ChronoVu LA8
---

# ChronoVu LA8

<div class="infobox" markdown>

"""
    
    # Add main image
    if images:
        main_img = next((img for img in images if 'front.png' in img['filename']), images[0])
        md_content += f"![ChronoVu LA8]({main_img['path']}){{ .infobox-image }}\n\n"
    
    md_content += f"### ChronoVu LA8\n\n| | |\n|---|---|\n"
    
    # Add infobox data
    for key, value in infobox.items():
        md_content += f"| **{key}** | {value} |\n"
    
    md_content += "\n</div>\n\n"
    
    # Add main content
    if main_content:
        md_content += main_content + "\n\n"
    
    # Add photo grid
    if len(images) > 1:
        md_content += "## Photos\n\n<div class=\"photo-grid\" markdown>\n\n"
        
        for img in images:
            md_content += f"[![{img['alt']}]({img['path']})]({img['path']} \"{img['alt']}\"){{ .glightbox data-gallery=\"chronovu-la8\" }}\n"
            md_content += f"<span class=\"caption\">{img['alt']}</span>\n\n"
        
        md_content += "</div>\n\n"
    
    # Write file
    device_dir = HW_DIR / "misc-devices" / "chronovu-la8"
    with open(device_dir / "index.md", 'w', encoding='utf-8') as f:
        f.write(md_content)
    
    print("ChronoVu LA8 page fixed!")
    print(f"Content length: {len(main_content)} characters")

if __name__ == "__main__":
    main()
