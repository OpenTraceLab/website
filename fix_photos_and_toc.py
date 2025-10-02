#!/usr/bin/env python3
"""
Fix Photos section placement and remove ToC for all devices
"""

import re
from pathlib import Path

HW_DIR = Path("hw")

def get_image_captions_from_html(content, device_slug):
    """Extract proper image captions from original HTML content"""
    captions = {}
    
    # Find Photos section in HTML
    photos_match = re.search(r'<h[2-6][^>]*>Photos</h[2-6]>(.*?)(?=<h[2-6]|<div[^>]*class="printfooter"|$)', content, re.DOTALL | re.IGNORECASE)
    if photos_match:
        photos_section = photos_match.group(1)
        
        # Find gallery items with captions
        gallery_items = re.findall(r'<div class="gallerytext">\s*<p><small>(.*?)</small></p>', photos_section, re.DOTALL)
        image_files = re.findall(r'href="/wiki/File:([^"]*)"', photos_section)
        
        # Match captions to images
        for i, (img_file, caption) in enumerate(zip(image_files, gallery_items)):
            if img_file and caption:
                captions[img_file] = caption.strip()
    
    return captions

def fix_device_page(device_path):
    """Fix Photos section and remove ToC for a single device"""
    index_file = device_path / "index.md"
    if not index_file.exists():
        return
    
    # Read current content
    with open(index_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove ToC (lines with links to sections)
    content = re.sub(r'^- \[.*?\]\(#.*?\).*$', '', content, flags=re.MULTILINE)
    content = re.sub(r'^\[.*?\]\(#.*?\).*$', '', content, flags=re.MULTILINE)
    
    # Get device slug from path
    device_slug = device_path.name
    
    # Check if we have images
    img_dir = device_path / "img"
    if not img_dir.exists():
        # Write cleaned content (ToC removed)
        with open(index_file, 'w', encoding='utf-8') as f:
            f.write(content)
        return
    
    # Get existing images
    images = []
    for img_file in img_dir.glob('*'):
        if img_file.suffix.lower() in ['.jpg', '.png', '.gif']:
            # Use filename as caption, clean it up
            caption = img_file.stem.replace('_', ' ').replace('-', ' ')
            # Capitalize first letter of each word
            caption = ' '.join(word.capitalize() for word in caption.split())
            images.append({
                'filename': img_file.name,
                'alt': caption,
                'path': f"./img/{img_file.name}"
            })
    
    if not images:
        # Write cleaned content (ToC removed)
        with open(index_file, 'w', encoding='utf-8') as f:
            f.write(content)
        return
    
    # Create photo-grid
    photo_grid = "\n## Photos\n\n<div class=\"photo-grid\" markdown>\n\n"
    for img in images:
        photo_grid += f"[![{img['alt']}]({img['path']})]({img['path']} \"{img['alt']}\"){{ .glightbox data-gallery=\"{device_slug}\" }}\n"
        photo_grid += f"<span class=\"caption\">{img['alt']}</span>\n\n"
    photo_grid += "</div>\n"
    
    # Replace existing Photos section or add at end
    if '## Photos' in content:
        # Replace existing Photos section
        content = re.sub(r'## Photos.*?(?=##|$)', photo_grid, content, flags=re.DOTALL)
    else:
        # Add Photos section before the end
        content = content.rstrip() + "\n" + photo_grid
    
    # Clean up multiple newlines
    content = re.sub(r'\n\s*\n\s*\n', '\n\n', content)
    
    # Write fixed content
    with open(index_file, 'w', encoding='utf-8') as f:
        f.write(content)

def main():
    """Fix all device pages"""
    print("Fixing Photos sections and removing ToC for all devices...")
    
    device_count = 0
    for device_type_dir in HW_DIR.iterdir():
        if device_type_dir.is_dir():
            for device_dir in device_type_dir.iterdir():
                if device_dir.is_dir():
                    fix_device_page(device_dir)
                    device_count += 1
                    if device_count % 50 == 0:
                        print(f"Processed {device_count} devices...")
    
    print(f"Completed! Fixed {device_count} devices.")

if __name__ == "__main__":
    main()
