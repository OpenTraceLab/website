#!/usr/bin/env python3
"""
Rename files with sigrok in filename and update all links.
"""

import os
import re
from pathlib import Path

# File rename mappings
FILE_RENAMES = {
    'sigrokabout.md': 'opentracelababout.md',
    'sigrokprivacy-policy.md': 'opentracelabprivacy-policy.md', 
    'managing-sigrok-cli-data-with-python.md': 'managing-opentracecli-data-with-python.md',
    'using-sigrok-cli-with-an-oscilloscope.md': 'using-opentracecli-with-an-oscilloscope.md',
    'advertising-sigrok-compatible-products.md': 'advertising-opentracelab-compatible-products.md',
    'feeding-hardware-decoded-packets-into-libsigrok.md': 'feeding-hardware-decoded-packets-into-opentracecapture.md',
    'sigrok-gtk.md': 'opentracelab-gtk.md',
    'sigrok-meter.md': 'opentracelab-meter.md', 
    'sigrokgeneral-disclaimer.md': 'opentracelabgeneral-disclaimer.md'
}

def rename_files():
    """Rename files with sigrok in filename."""
    base_dir = Path('/home/epkcfsm/src/website')
    renamed_files = {}
    
    for old_name, new_name in FILE_RENAMES.items():
        old_path = base_dir / 'docs/hardware/misc-devices' / old_name
        new_path = base_dir / 'docs/hardware/misc-devices' / new_name
        
        if old_path.exists():
            old_path.rename(new_path)
            renamed_files[old_name] = new_name
            print(f"✓ Renamed: {old_name} → {new_name}")
    
    return renamed_files

def update_links_in_file(filepath, renamed_files):
    """Update links in a single file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Update markdown links
        for old_name, new_name in renamed_files.items():
            old_name_no_ext = old_name.replace('.md', '')
            new_name_no_ext = new_name.replace('.md', '')
            
            # Update various link formats
            patterns = [
                (rf'\[([^\]]*)\]\({old_name_no_ext}\)', rf'[\1]({new_name_no_ext})'),
                (rf'\[([^\]]*)\]\({old_name}\)', rf'[\1]({new_name})'),
                (rf'\[([^\]]*)\]\(\.\.\/.*\/{old_name_no_ext}\)', rf'[\1](../misc-devices/{new_name_no_ext})'),
                (rf'{old_name_no_ext}\.md', f'{new_name}'),
                (rf'{old_name_no_ext}/index\.html', f'{new_name_no_ext}/index.html')
            ]
            
            for pattern, replacement in patterns:
                content = re.sub(pattern, replacement, content)
        
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        
        return False
        
    except Exception as e:
        print(f"✗ Error updating {filepath}: {e}")
        return False

def update_all_links(renamed_files):
    """Update links in all files."""
    base_dir = Path('/home/epkcfsm/src/website')
    extensions = {'.md', '.yml', '.yaml', '.html'}
    updated_count = 0
    
    for root, dirs, files in os.walk(base_dir):
        dirs[:] = [d for d in dirs if not d.startswith('.') or d in ['.github']]
        
        for file in files:
            filepath = Path(root) / file
            
            if filepath.suffix in extensions and not str(filepath).endswith('replace_sigrok.py'):
                if update_links_in_file(filepath, renamed_files):
                    updated_count += 1
    
    return updated_count

def main():
    """Main function."""
    print("Renaming files with sigrok in filename...")
    renamed_files = rename_files()
    
    if renamed_files:
        print(f"\nUpdating links in all files...")
        updated_count = update_all_links(renamed_files)
        print(f"✓ Updated links in {updated_count} files")
    
    print(f"\nFile rename complete! Renamed {len(renamed_files)} files.")

if __name__ == '__main__':
    main()
