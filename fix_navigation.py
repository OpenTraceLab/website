#!/usr/bin/env python3
"""
Fix navigation configuration and broken links.
"""

import os
import re
from pathlib import Path

def update_mkdocs_nav():
    """Update mkdocs.yml to include all hardware pages."""
    mkdocs_path = Path('/home/epkcfsm/src/website/mkdocs.yml')
    
    with open(mkdocs_path, 'r') as f:
        content = f.read()
    
    # Add comprehensive hardware navigation
    hardware_nav = '''  - Hardware:
      - Supported Devices: hardware/supported-hardware.md
      - Logic Analyzers:
          - Overview: hardware/logic-analyzer/index.md
          - FX2-based Devices: hardware/logic-analyzer/fx2lafw.md
          - Saleae Logic Series: hardware/logic-analyzer/saleae-logic.md
          - Kingst LA Series: hardware/logic-analyzer/kingst-la-series.md
          - OpenBench LogicSniffer: hardware/logic-analyzer/openbench-logic-sniffer.md
      - Multimeters:
          - Overview: hardware/multimeter/index.md
          - UNI-T Series: hardware/multimeter/uni-t.md
          - Voltcraft Series: hardware/multimeter/voltcraft.md
          - Brymen Series: hardware/multimeter/brymen.md
      - Oscilloscopes:
          - Overview: hardware/oscilloscope/index.md
          - Rigol DS Series: hardware/oscilloscope/rigol-ds.md
          - Hantek DSO Series: hardware/oscilloscope/hantek-dso.md
          - Siglent SDS Series: hardware/oscilloscope/siglent-sds.md
      - Power Supplies:
          - Overview: hardware/power-supply/index.md
          - Korad Series: hardware/power-supply/korad.md
          - Rigol DP Series: hardware/power-supply/rigol-dp.md
      - Function Generators:
          - Overview: hardware/function-generator/index.md
      - Thermometers:
          - Overview: hardware/thermometer/index.md'''
    
    # Replace the hardware section
    pattern = r'  - Hardware:.*?(?=  - Community:)'
    content = re.sub(pattern, hardware_nav + '\n', content, flags=re.DOTALL)
    
    with open(mkdocs_path, 'w') as f:
        f.write(content)
    
    print("✓ Updated mkdocs.yml navigation")

def fix_broken_links():
    """Fix broken anchor links."""
    overview_path = Path('/home/epkcfsm/src/website/docs/opentracecapture/overview.md')
    
    with open(overview_path, 'r') as f:
        content = f.read()
    
    # Add missing anchor
    if '## Power Supplies' not in content:
        content += '\n\n## Power Supplies\nOpenTraceCapture supports various programmable power supplies for automated testing and device characterization.\n'
        
        with open(overview_path, 'w') as f:
            f.write(content)
        
        print("✓ Added missing power-supplies anchor")

def main():
    """Main function."""
    print("Fixing navigation and links...")
    update_mkdocs_nav()
    fix_broken_links()
    print("✓ Navigation fixes complete!")

if __name__ == '__main__':
    main()
