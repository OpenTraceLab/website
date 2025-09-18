#!/usr/bin/env python3
"""
Fix navigation and clean up migrated hardware documentation
"""

import os
import re
from pathlib import Path

def update_mkdocs_navigation():
    """Update mkdocs.yml with proper navigation structure"""
    
    # Read current mkdocs.yml
    with open('mkdocs.yml', 'r') as f:
        content = f.read()
    
    # Create new hardware navigation section
    hardware_nav = """  - Hardware:
      - Supported Devices: hardware/supported-hardware.md
      - Logic Analyzers:
          - FX2-based Devices: hardware/logic-analyzer/fx2lafw.md
          - Saleae Logic Series: hardware/logic-analyzer/saleae-logic.md
          - Saleae Logic16: hardware/logic-analyzer/saleae-logic16.md
          - Kingst LA Series: hardware/logic-analyzer/kingst-la-series.md
          - Kingst LA2016: hardware/logic-analyzer/kingst-la2016.md
          - Hantek 4032L: hardware/logic-analyzer/hantek-4032l.md
          - OpenBench LogicSniffer: hardware/logic-analyzer/openbench-logic-sniffer.md
      - Multimeters:
          - UNI-T Series: hardware/multimeter/uni-t.md
          - UNI-T UT61E: hardware/multimeter/uni-t-ut61e.md
          - Voltcraft Series: hardware/multimeter/voltcraft.md
          - Voltcraft VC-820: hardware/multimeter/voltcraft-vc-820.md
          - Brymen Series: hardware/multimeter/brymen.md
      - Oscilloscopes:
          - Rigol DS Series: hardware/oscilloscope/rigol-ds.md
          - Rigol DS1000Z Series: hardware/oscilloscope/rigol-ds1000z-series.md
          - Hantek DSO Series: hardware/oscilloscope/hantek-dso.md
          - Siglent SDS Series: hardware/oscilloscope/siglent-sds.md
      - Power Supplies:
          - Korad Series: hardware/power-supply/korad.md
          - Korad KA3005P: hardware/power-supply/korad-ka3005p.md
          - Rigol DP Series: hardware/power-supply/rigol-dp.md
      - Function Generators:
          - Rigol DG Series: hardware/function-generator/rigol-dg1000z-series.md
          - Siglent SDG Series: hardware/function-generator/siglent-sdg1010.md
      - Thermometers:
          - Voltcraft DL Series: hardware/thermometer/voltcraft-dl-161s.md
          - RDing TEMPer Series: hardware/thermometer/rding-temper.md"""
    
    # Replace the hardware section
    pattern = r'(  - Hardware:.*?)(\n  - [^:]+:|$)'
    replacement = hardware_nav + r'\2'
    
    updated_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    
    # Write updated mkdocs.yml
    with open('mkdocs.yml', 'w') as f:
        f.write(updated_content)
    
    print("Updated mkdocs.yml navigation")

def clean_markdown_files():
    """Clean up migrated markdown files"""
    
    hardware_dir = Path('docs/hardware')
    
    for md_file in hardware_dir.rglob('*.md'):
        if md_file.name == 'supported-hardware.md':
            continue
            
        print(f"Cleaning {md_file}")
        
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Fix image paths - convert old wiki-style links to proper markdown
        content = re.sub(r'!\[([^\]]*)\]\(docs/media/([^)]+)\)', r'![\\1](../../assets/hardware/general/\\2)', content)
        content = re.sub(r'!\[([^\]]*)\]\(\./File:([^)]+)\.html\)', r'![\\1](../../assets/hardware/general/\\2)', content)
        
        # Remove wiki-style table formatting
        content = re.sub(r'\|\s*\n\s*\|---\|---\|\s*\n', '\n\n', content)
        
        # Clean up excessive whitespace
        content = re.sub(r'\n\n\n+', '\n\n', content)
        
        # Fix OpenTraceLab references that might have been over-converted
        content = re.sub(r'OpenTraceLab\.org/gitweb', 'github.com/OpenTraceLab', content)
        
        # Add proper frontmatter if missing
        if not content.startswith('#'):
            title = md_file.stem.replace('-', ' ').title()
            content = f"# {title}\n\n{content}"
        
        with open(md_file, 'w', encoding='utf-8') as f:
            f.write(content)

def create_category_index_pages():
    """Create index pages for each hardware category"""
    
    categories = {
        'logic-analyzer': 'Logic Analyzers',
        'multimeter': 'Multimeters', 
        'oscilloscope': 'Oscilloscopes',
        'power-supply': 'Power Supplies',
        'function-generator': 'Function Generators',
        'thermometer': 'Thermometers'
    }
    
    for category, title in categories.items():
        category_dir = Path(f'docs/hardware/{category}')
        if not category_dir.exists():
            continue
            
        index_file = category_dir / 'index.md'
        
        # Get list of devices in category
        devices = []
        for md_file in category_dir.glob('*.md'):
            if md_file.name != 'index.md':
                device_name = md_file.stem.replace('-', ' ').title()
                devices.append((md_file.name, device_name))
        
        devices.sort(key=lambda x: x[1])
        
        # Create index content
        content = f"""# {title}

This section contains documentation for {title.lower()} supported by OpenTraceLab.

## Supported Devices

"""
        
        for filename, device_name in devices:
            content += f"- [{device_name}]({filename})\n"
        
        content += f"""
## Getting Started

1. **Install OpenTraceLab** - Follow the [installation guide](../../get-started/install.md)
2. **Connect your device** - Use appropriate USB cable or interface
3. **Test connection** - Use `sigrok-cli --scan` to detect your device
4. **Start capturing** - Follow device-specific instructions

## See Also

- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
- [Getting Started Guide](../../get-started/capture-first-trace.md)
"""
        
        with open(index_file, 'w') as f:
            f.write(content)
        
        print(f"Created index for {category}")

def main():
    """Main function"""
    print("Fixing navigation and cleaning up migrated content...")
    
    # Update navigation
    update_mkdocs_navigation()
    
    # Clean markdown files
    clean_markdown_files()
    
    # Create category index pages
    create_category_index_pages()
    
    print("\nCleanup completed!")
    print(f"Total migrated devices: {sum(len(list(Path(f'docs/hardware/{cat}').glob('*.md'))) for cat in ['logic-analyzer', 'multimeter', 'oscilloscope', 'power-supply', 'function-generator', 'thermometer', 'misc-devices'] if Path(f'docs/hardware/{cat}').exists())}")

if __name__ == "__main__":
    main()
