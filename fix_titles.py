#!/usr/bin/env python3
"""
Fix remaining sigrok references in titles while preserving attribution URLs.
"""

import os
import re
from pathlib import Path

def fix_titles_in_file(filepath):
    """Fix titles in a single file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Fix titles (first line starting with #) but not URLs in "Retrieved from" lines
        lines = content.split('\n')
        modified_lines = []
        
        for i, line in enumerate(lines):
            # Skip "Retrieved from" attribution lines
            if line.strip().startswith('Retrieved from'):
                modified_lines.append(line)
                continue
                
            # Fix titles
            if line.startswith('# ') and 'sigrok' in line.lower():
                # Replace sigrok-cli with OpenTraceCLI in titles
                line = re.sub(r'\bsigrok-cli\b', 'OpenTraceCLI', line, flags=re.IGNORECASE)
                line = re.sub(r'\bSigrok Cli\b', 'OpenTraceCLI', line, flags=re.IGNORECASE)
                
            modified_lines.append(line)
        
        new_content = '\n'.join(modified_lines)
        
        if new_content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"✓ Updated title in: {filepath}")
            return True
        
        return False
        
    except Exception as e:
        print(f"✗ Error processing {filepath}: {e}")
        return False

def main():
    """Main function."""
    base_dir = Path('/home/epkcfsm/src/website')
    
    files_to_check = [
        'docs/hardware/misc-devices/managing-sigrok-cli-data-with-python.md',
        'docs/hardware/misc-devices/using-sigrok-cli-with-an-oscilloscope.md'
    ]
    
    modified_count = 0
    
    for file_path in files_to_check:
        full_path = base_dir / file_path
        if full_path.exists():
            if fix_titles_in_file(full_path):
                modified_count += 1
    
    print(f"\nTitle fixes complete! Modified {modified_count} files.")

if __name__ == '__main__':
    main()
