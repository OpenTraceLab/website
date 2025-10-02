#!/usr/bin/env python3
import os
from pathlib import Path
import re

def fix_png_references():
    changes = 0
    hardware_dir = Path("docs/hardware")
    
    # Find all index.md files in hardware subdirectories
    for index_file in hardware_dir.rglob("index.md"):
        with open(index_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Find all PNG image references (with various path formats)
        png_matches = re.findall(r'!\[([^\]]*)\]\(([^)]*\.png)\)', content)
        
        for alt_text, png_path in png_matches:
            # Handle different path formats
            if png_path.startswith('./img/'):
                rel_path = png_path[2:]  # Remove './'
                full_png_path = index_file.parent / rel_path
            elif png_path.startswith('img/'):
                full_png_path = index_file.parent / png_path
            else:
                continue  # Skip absolute paths
                
            full_jpg_path = full_png_path.with_suffix('.jpg')
            
            # Check if PNG doesn't exist but JPG does
            if not full_png_path.exists() and full_jpg_path.exists():
                jpg_path = png_path.replace('.png', '.jpg')
                old_ref = f'![{alt_text}]({png_path})'
                new_ref = f'![{alt_text}]({jpg_path})'
                content = content.replace(old_ref, new_ref)
                changes += 1
                print(f"Fixed in {index_file}: {png_path} -> {jpg_path}")
        
        # Write back if changed
        if content != original_content:
            with open(index_file, 'w', encoding='utf-8') as f:
                f.write(content)
    
    print(f"Fixed {changes} PNG references in device pages")

if __name__ == "__main__":
    fix_png_references()
