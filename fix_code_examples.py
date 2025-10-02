#!/usr/bin/env python3
"""
Fix remaining sigrok references in code examples.
"""

import os
import re
from pathlib import Path

def fix_code_examples(filepath):
    """Fix code examples in a file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Fix include statements and similar code references
        content = re.sub(r'#include <libsigrokcxx/libsigrokcxx\.hpp>', 
                        '#include <libopentracecapturecxx/libopentracecapturecxx.hpp>', content)
        
        # Fix namespace references in code
        content = re.sub(r'OpenTraceLab::Context::create\(\)', 
                        'OpenTraceCapture::Context::create()', content)
        
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✓ Updated code examples in: {filepath}")
            return True
        
        return False
        
    except Exception as e:
        print(f"✗ Error processing {filepath}: {e}")
        return False

def main():
    """Main function."""
    base_dir = Path('/home/epkcfsm/src/website')
    
    # Check the specific file with code examples
    file_path = base_dir / 'docs/opentracecapture/overview.md'
    
    if file_path.exists():
        fix_code_examples(file_path)
    
    print("Code example fixes complete!")

if __name__ == '__main__':
    main()
