#!/usr/bin/env python3
"""
Migrate hardware device pages from sigrok documentation to OpenTraceLab format
"""

import os
import re
import shutil
from pathlib import Path
import html2text

# Source and destination paths
SIGROK_DOCS = Path("../sigladocs/docs")
DEST_DOCS = Path("docs/hardware")
DEST_MEDIA = Path("docs/assets/hardware")

# Device categories and their mappings
DEVICE_CATEGORIES = {
    "logic-analyzer": {
        "source_dir": "logic-analyzer",
        "dest_dir": "logic-analyzer",
        "title_prefix": "Logic Analyzer: "
    },
    "multimeter": {
        "source_dir": "multimeter", 
        "dest_dir": "multimeter",
        "title_prefix": "Multimeter: "
    },
    "oscilloscope": {
        "source_dir": "oscilloscope",
        "dest_dir": "oscilloscope", 
        "title_prefix": "Oscilloscope: "
    },
    "power-supply": {
        "source_dir": "power-supply",
        "dest_dir": "power-supply",
        "title_prefix": "Power Supply: "
    },
    "function-generator": {
        "source_dir": "function-generator",
        "dest_dir": "function-generator",
        "title_prefix": "Function Generator: "
    },
    "thermometer": {
        "source_dir": "thermometer",
        "dest_dir": "thermometer", 
        "title_prefix": "Thermometer: "
    },
    "sound-level-meter": {
        "source_dir": "sound-level-meter",
        "dest_dir": "sound-level-meter",
        "title_prefix": "Sound Level Meter: "
    },
    "lcr-meter": {
        "source_dir": "lcr-meter",
        "dest_dir": "lcr-meter",
        "title_prefix": "LCR Meter: "
    },
    "frequency-counter": {
        "source_dir": "frequency-counter", 
        "dest_dir": "frequency-counter",
        "title_prefix": "Frequency Counter: "
    },
    "spectrum-analyzer": {
        "source_dir": "spectrum-analyzer",
        "dest_dir": "spectrum-analyzer", 
        "title_prefix": "Spectrum Analyzer: "
    },
    "programmable-load": {
        "source_dir": "programmable-load",
        "dest_dir": "programmable-load",
        "title_prefix": "Programmable Load: "
    },
    "misc-devices": {
        "source_dir": "misc-devices",
        "dest_dir": "misc-devices",
        "title_prefix": "Device: "
    }
}

def clean_html_content(content):
    """Convert HTML to clean markdown"""
    # Initialize html2text converter
    h = html2text.HTML2Text()
    h.ignore_links = False
    h.ignore_images = False
    h.ignore_emphasis = False
    h.body_width = 0  # Don't wrap lines
    
    # Convert HTML to markdown
    markdown = h.handle(content)
    
    # Clean up common issues
    markdown = re.sub(r'\n\n\n+', '\n\n', markdown)  # Remove excessive newlines
    markdown = re.sub(r'^\s*\n', '', markdown, flags=re.MULTILINE)  # Remove leading whitespace lines
    
    return markdown.strip()

def extract_title_from_content(content):
    """Extract device title from HTML content"""
    # Try to find h1 tag
    h1_match = re.search(r'<h1[^>]*>(.*?)</h1>', content, re.IGNORECASE | re.DOTALL)
    if h1_match:
        title = re.sub(r'<[^>]+>', '', h1_match.group(1)).strip()
        return title
    
    # Try to find title in div with id="firstHeading"
    title_match = re.search(r'<div[^>]*id="firstHeading"[^>]*>(.*?)</div>', content, re.IGNORECASE | re.DOTALL)
    if title_match:
        title = re.sub(r'<[^>]+>', '', title_match.group(1)).strip()
        return title
    
    return None

def process_images(content, source_file, dest_dir):
    """Process and copy images, update image paths"""
    media_dir = DEST_MEDIA / dest_dir.name
    media_dir.mkdir(parents=True, exist_ok=True)
    
    # Find all image references
    img_pattern = r'!\[([^\]]*)\]\(([^)]+)\)'
    images = re.findall(img_pattern, content)
    
    for alt_text, img_path in images:
        # Handle relative paths
        if not img_path.startswith('http'):
            # Resolve relative to source file
            source_img = source_file.parent / img_path
            if not source_img.exists():
                # Try in media directory
                source_img = SIGROK_DOCS / "media" / img_path
            
            if source_img.exists():
                # Copy image to destination
                dest_img = media_dir / source_img.name
                shutil.copy2(source_img, dest_img)
                
                # Update path in content
                new_path = f"../../assets/hardware/{dest_dir.name}/{source_img.name}"
                content = content.replace(f"]({img_path})", f"]({new_path})")
    
    return content

def convert_sigrok_to_opentracelab(content):
    """Convert OpenTraceLab-specific content to OpenTraceLab format"""
    # Replace OpenTraceLab references with OpenTraceLab
    content = re.sub(r'\bsigrok\b', 'OpenTraceLab', content, flags=re.IGNORECASE)
    content = re.sub(r'\bPulseView\b', 'OpenTraceView', content)
    content = re.sub(r'\bsigrok-cli\b', 'OpenTraceCLI', content)  # Keep CLI name
    
    # Update command examples to use OpenTraceLab context
    content = re.sub(r'OpenTraceCapture', 'OpenTraceCapture', content)
    content = re.sub(r'OpenTraceDecode', 'OpenTraceDecode', content)
    
    return content

def create_device_page(source_file, dest_file, category_info):
    """Convert a single device page"""
    print(f"Processing: {source_file.name} -> {dest_file}")
    
    # Read source file
    with open(source_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract title
    title = extract_title_from_content(content)
    if not title:
        title = source_file.stem.replace('-', ' ').title()
    
    # Extract main content (remove navigation, headers, footers)
    # Look for main content div
    content_match = re.search(r'<div[^>]*class="mw-parser-output"[^>]*>(.*?)</div>\s*</div>\s*</div>', content, re.DOTALL)
    if content_match:
        main_content = content_match.group(1)
    else:
        # Fallback: try to find content between body tags
        body_match = re.search(r'<body[^>]*>(.*?)</body>', content, re.DOTALL)
        if body_match:
            main_content = body_match.group(1)
        else:
            main_content = content
    
    # Convert HTML to markdown
    markdown_content = clean_html_content(main_content)
    
    # Convert OpenTraceLab references to OpenTraceLab
    markdown_content = convert_sigrok_to_opentracelab(markdown_content)
    
    # Process images
    markdown_content = process_images(markdown_content, source_file, dest_file.parent)
    
    # Create final markdown with frontmatter
    final_content = f"""# {title}

{markdown_content}

## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
"""
    
    # Write destination file
    dest_file.parent.mkdir(parents=True, exist_ok=True)
    with open(dest_file, 'w', encoding='utf-8') as f:
        f.write(final_content)

def update_navigation(migrated_devices):
    """Update mkdocs.yml navigation with migrated devices"""
    mkdocs_file = Path("mkdocs.yml")
    
    with open(mkdocs_file, 'r') as f:
        content = f.read()
    
    # Build navigation entries for each category
    nav_entries = {}
    for category, devices in migrated_devices.items():
        if not devices:
            continue
            
        category_title = category.replace('-', ' ').title()
        nav_entries[category] = f"      - {category_title}:\n"
        
        for device_file, device_title in sorted(devices):
            nav_entries[category] += f"          - {device_title}: hardware/{category}/{device_file}\n"
    
    # Find Hardware section and update it
    hardware_pattern = r'(  - Hardware:\s*\n)(.*?)(\n  - [^:]+:|$)'
    
    new_hardware_section = "  - Hardware:\n      - Supported Devices: hardware/supported-hardware.md\n"
    for category in sorted(nav_entries.keys()):
        new_hardware_section += nav_entries[category]
    
    updated_content = re.sub(hardware_pattern, new_hardware_section + r'\3', content, flags=re.DOTALL)
    
    with open(mkdocs_file, 'w') as f:
        f.write(updated_content)

def main():
    """Main migration function"""
    print("Starting hardware device migration...")
    
    # Create destination directories
    DEST_DOCS.mkdir(parents=True, exist_ok=True)
    DEST_MEDIA.mkdir(parents=True, exist_ok=True)
    
    migrated_devices = {}
    
    # Process each device category
    for category, info in DEVICE_CATEGORIES.items():
        source_dir = SIGROK_DOCS / info["source_dir"]
        dest_dir = DEST_DOCS / info["dest_dir"]
        
        if not source_dir.exists():
            print(f"Skipping {category}: source directory not found")
            continue
        
        print(f"\nProcessing category: {category}")
        migrated_devices[category] = []
        
        # Process all .md files in source directory
        for source_file in source_dir.glob("*.md"):
            dest_file = dest_dir / source_file.name
            
            try:
                create_device_page(source_file, dest_file, info)
                
                # Extract device name for navigation
                device_name = source_file.stem.replace('-', ' ').title()
                migrated_devices[category].append((source_file.name, device_name))
                
            except Exception as e:
                print(f"Error processing {source_file}: {e}")
    
    # Copy media files
    print("\nCopying media files...")
    media_source = SIGROK_DOCS / "media"
    if media_source.exists():
        for media_file in media_source.rglob("*"):
            if media_file.is_file():
                # Copy to general media directory
                dest_media_file = DEST_MEDIA / "general" / media_file.name
                dest_media_file.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(media_file, dest_media_file)
    
    # Update navigation
    print("\nUpdating navigation...")
    update_navigation(migrated_devices)
    
    # Print summary
    total_devices = sum(len(devices) for devices in migrated_devices.values())
    print(f"\nMigration completed!")
    print(f"Total devices migrated: {total_devices}")
    for category, devices in migrated_devices.items():
        if devices:
            print(f"  {category}: {len(devices)} devices")

if __name__ == "__main__":
    main()
