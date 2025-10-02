#!/usr/bin/env python3
"""
Fix MediaWiki links in device pages to use relative image paths
"""

import re
from pathlib import Path

def fix_wiki_links_in_file(file_path):
    """Fix wiki links in a single markdown file"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Fix /wiki/File: links to ./img/ links
    # Pattern: /wiki/File:filename.ext -> ./img/filename.ext
    content = re.sub(r'/wiki/File:([^)\s]+)', r'./img/\1', content)
    
    # Fix any remaining wiki links
    content = re.sub(r'\[([^\]]+)\]\(/wiki/([^)]+)\)', r'[\1](https://sigrok.org/wiki/\2)', content)
    
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def main():
    """Fix all wiki links in hardware documentation"""
    hw_dir = Path("docs/hardware")
    fixed_count = 0
    
    print("Fixing MediaWiki links in hardware documentation...")
    
    for md_file in hw_dir.rglob("*.md"):
        if md_file.name != "supported-hardware.md":  # Skip the main catalog page
            if fix_wiki_links_in_file(md_file):
                print(f"Fixed: {md_file}")
                fixed_count += 1
    
    print(f"Fixed {fixed_count} files with MediaWiki links")

if __name__ == "__main__":
    main()
