#!/usr/bin/env python3
"""
Optimize images in the repository:
- Resize all images to max 800x600
- Convert PNG to JPG (except logos/icons)
- Update all markdown links
- Reduce repository size
"""

import os
import re
from pathlib import Path
from PIL import Image
import argparse

def should_convert_to_jpg(image_path):
    """Check if image should be converted to JPG (skip logos, icons, etc.)"""
    name = image_path.name.lower()
    # Keep PNG for logos, icons, screenshots with transparency
    skip_patterns = ['logo', 'icon', 'badge', 'button', 'transparent']
    return not any(pattern in name for pattern in skip_patterns)

def optimize_image(image_path, max_width=800, max_height=600, quality=85):
    """Resize and optimize a single image"""
    try:
        with Image.open(image_path) as img:
            # Convert RGBA to RGB for JPG conversion
            if img.mode in ('RGBA', 'LA', 'P'):
                # Create white background for transparency
                background = Image.new('RGB', img.size, (255, 255, 255))
                if img.mode == 'P':
                    img = img.convert('RGBA')
                background.paste(img, mask=img.split()[-1] if img.mode == 'RGBA' else None)
                img = background
            elif img.mode != 'RGB':
                img = img.convert('RGB')
            
            # Resize if larger than max dimensions
            if img.width > max_width or img.height > max_height:
                img.thumbnail((max_width, max_height), Image.Resampling.LANCZOS)
            
            # Determine output format and path
            if image_path.suffix.lower() == '.png' and should_convert_to_jpg(image_path):
                new_path = image_path.with_suffix('.jpg')
                img.save(new_path, 'JPEG', quality=quality, optimize=True)
                
                # Remove original PNG
                image_path.unlink()
                return new_path, True  # Converted
            else:
                # Save as original format but optimized
                if image_path.suffix.lower() in ['.jpg', '.jpeg']:
                    img.save(image_path, 'JPEG', quality=quality, optimize=True)
                else:
                    img.save(image_path, optimize=True)
                return image_path, False  # Not converted
                
    except Exception as e:
        print(f"Error processing {image_path}: {e}")
        return image_path, False

def update_markdown_links(file_path, conversions):
    """Update image links in markdown files"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        updated = False
        for old_path, new_path in conversions.items():
            old_name = old_path.name
            new_name = new_path.name
            
            if old_name != new_name:
                # Update markdown image links
                content = re.sub(
                    rf'!\[([^\]]*)\]\(([^)]*){re.escape(old_name)}\)',
                    rf'![\1](\2{new_name})',
                    content
                )
                # Update HTML img src
                content = re.sub(
                    rf'src="([^"]*){re.escape(old_name)}"',
                    rf'src="\1{new_name}"',
                    content
                )
                updated = True
        
        if updated:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated links in {file_path}")
            
    except Exception as e:
        print(f"Error updating {file_path}: {e}")

def main():
    parser = argparse.ArgumentParser(description='Optimize repository images')
    parser.add_argument('--max-width', type=int, default=800, help='Maximum width')
    parser.add_argument('--max-height', type=int, default=600, help='Maximum height')
    parser.add_argument('--quality', type=int, default=85, help='JPEG quality')
    parser.add_argument('--dry-run', action='store_true', help='Show what would be done')
    args = parser.parse_args()
    
    repo_root = Path(__file__).parent
    conversions = {}
    
    # Find all image files
    image_extensions = {'.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff'}
    image_files = []
    
    for ext in image_extensions:
        image_files.extend(repo_root.rglob(f'*{ext}'))
        image_files.extend(repo_root.rglob(f'*{ext.upper()}'))
    
    print(f"Found {len(image_files)} images to process")
    
    if args.dry_run:
        for img_path in image_files:
            print(f"Would process: {img_path}")
        return
    
    # Process images
    for img_path in image_files:
        print(f"Processing: {img_path}")
        new_path, converted = optimize_image(
            img_path, args.max_width, args.max_height, args.quality
        )
        
        if converted:
            conversions[img_path] = new_path
            print(f"  Converted: {img_path.name} -> {new_path.name}")
    
    # Update markdown files
    if conversions:
        print(f"\nUpdating {len(conversions)} file references...")
        md_files = list(repo_root.rglob('*.md'))
        
        for md_file in md_files:
            update_markdown_links(md_file, conversions)
    
    print(f"\nOptimization complete!")
    print(f"- Processed {len(image_files)} images")
    print(f"- Converted {len(conversions)} PNG files to JPG")

if __name__ == '__main__':
    main()
