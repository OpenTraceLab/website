#!/usr/bin/env python3
import yaml
import os
from pathlib import Path

def fix_png_to_jpg():
    yaml_file = Path("docs/data/hardware.yaml")
    
    with open(yaml_file, 'r') as f:
        data = yaml.safe_load(f)
    
    changes = 0
    
    for category in data.get('categories', []):
        for row in category.get('rows', []):
            if 'Image' in row and row['Image']:
                img_path = row['Image']
                if img_path.endswith('.png'):
                    # Convert /website/hardware/... to docs/hardware/...
                    local_path = img_path.replace('/website/', 'docs/')
                    png_file = Path(local_path)
                    jpg_file = png_file.with_suffix('.jpg')
                    
                    # Check if JPG exists (regardless of PNG existence)
                    if jpg_file.exists():
                        row['Image'] = img_path.replace('.png', '.jpg')
                        changes += 1
                        print(f"Fixed: {img_path} -> {row['Image']}")
                    else:
                        print(f"Warning: Neither PNG nor JPG exists for {img_path}")
    
    if changes > 0:
        with open(yaml_file, 'w') as f:
            yaml.dump(data, f, default_flow_style=False, sort_keys=False)
        print(f"Fixed {changes} PNG references to JPG")
    else:
        print("No PNG to JPG fixes needed")

if __name__ == "__main__":
    fix_png_to_jpg()
