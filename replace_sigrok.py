#!/usr/bin/env python3
"""
Replace OpenTraceLab references with OpenTraceLab equivalents while preserving required attributions.
"""

import os
import re
import sys
from pathlib import Path

# Define replacement mappings
REPLACEMENTS = {
    # Core library replacements
    r'\blibsigrok\b': 'OpenTraceCapture',
    r'\bsigrok-cli\b': 'OpenTraceCLI', 
    r'\bsigrokcli\b': 'OpenTraceCLI',
    r'\bPulseView\b': 'OpenTraceView',
    r'\blibsigrokdecode\b': 'OpenTraceDecode',
    r'\bsigrokdecode\b': 'OpenTraceDecode',
    r'\bsigrok-decode\b': 'OpenTraceDecode',
    
    # General OpenTraceLab references (but preserve in attribution contexts)
    r'(?<!the\s)(?<!original\s)(?<!from\s)(?<!sigrok\s)(?<!\.org/)(?<!://)\bsigrok\b(?!\s+project)(?!\s+community)(?!\s+documentation)(?!\s+wiki)(?!\.org)(?!\s+developers)(?!\s+contributors)': 'OpenTraceLab',
}

# Files and patterns to exclude from replacement
EXCLUDE_PATTERNS = [
    r'\.git/',
    r'\.venv/',
    r'/site/',  # Generated site files
    r'attribution\.md$',  # Attribution file - preserve all sigrok references
    r'LICENSE$',
]

# Context patterns where OpenTraceLab should be preserved (attribution contexts)
PRESERVE_CONTEXTS = [
    r'based on.*sigrok',
    r'derived from.*sigrok', 
    r'fork of.*sigrok',
    r'originally.*sigrok',
    r'sigrok project',
    r'sigrok community',
    r'OpenTraceLab\.org',
    r'https?://.*OpenTraceLab',
    r'original.*sigrok',
    r'attribution.*sigrok',
    r'acknowledge.*sigrok',
    r'credit.*sigrok',
    r'copyright.*sigrok',
    r'license.*sigrok',
    r'authors.*sigrok',
    r'contributors.*sigrok',
    r'website.*sigrok',
    r'source.*sigrok',
]

def should_exclude_file(filepath):
    """Check if file should be excluded from processing."""
    filepath_str = str(filepath)
    return any(re.search(pattern, filepath_str) for pattern in EXCLUDE_PATTERNS)

def should_preserve_line(line):
    """Check if line contains attribution context where sigrok should be preserved."""
    line_lower = line.lower()
    return any(re.search(pattern, line_lower, re.IGNORECASE) for pattern in PRESERVE_CONTEXTS)

def process_file(filepath):
    """Process a single file for OpenTraceLab replacements."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        lines = content.split('\n')
        modified_lines = []
        changes_made = False
        
        for line in lines:
            if should_preserve_line(line):
                # Preserve line as-is if it's in attribution context
                modified_lines.append(line)
            else:
                # Apply replacements
                modified_line = line
                for pattern, replacement in REPLACEMENTS.items():
                    new_line = re.sub(pattern, replacement, modified_line)
                    if new_line != modified_line:
                        changes_made = True
                        modified_line = new_line
                modified_lines.append(modified_line)
        
        if changes_made:
            new_content = '\n'.join(modified_lines)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"✓ Updated: {filepath}")
            return True
        else:
            return False
            
    except Exception as e:
        print(f"✗ Error processing {filepath}: {e}")
        return False

def main():
    """Main function to process all files."""
    base_dir = Path('/home/epkcfsm/src/website')
    
    # File extensions to process
    extensions = {'.md', '.yml', '.yaml', '.py', '.html', '.txt'}
    
    total_files = 0
    modified_files = 0
    
    print("Starting OpenTraceLab → OpenTraceLab replacement...")
    print("Preserving attributions and required references...")
    print()
    
    for root, dirs, files in os.walk(base_dir):
        # Skip certain directories
        dirs[:] = [d for d in dirs if not d.startswith('.') or d in ['.github']]
        
        for file in files:
            filepath = Path(root) / file
            
            # Check file extension
            if filepath.suffix not in extensions:
                continue
                
            # Check if file should be excluded
            if should_exclude_file(filepath):
                continue
                
            total_files += 1
            if process_file(filepath):
                modified_files += 1
    
    print()
    print(f"Processing complete!")
    print(f"Files processed: {total_files}")
    print(f"Files modified: {modified_files}")
    print()
    print("Note: Attribution files and required sigrok references have been preserved.")

if __name__ == '__main__':
    main()
