#!/usr/bin/env python3
"""
Fix device naming issues and move remaining devices to proper categories
"""

import shutil
from pathlib import Path

HW_DIR = Path("hw")

# Device renames and moves
DEVICE_FIXES = {
    # HTML entity fixes and moves
    'rohdeamp;schwarz-hmc-8043': ('rohde-schwarz-hmc-8043', 'power-supply'),
    'rohdeamp;schwarz-hmo-3000-series': ('rohde-schwarz-hmo-3000-series', 'mixed-signal-devices'),
    'rohdeamp;schwarz-hmp-4000-series': ('rohde-schwarz-hmp-4000-series', 'power-supply'),
    'rohdeamp;schwarz-rt-series': ('rohde-schwarz-rt-series', 'mixed-signal-devices'),
    'vamp;a-va18b': ('v-a-va18b', 'multimeter'),
    'vamp;a-va40b': ('v-a-va40b', 'multimeter'),
    
    # Underscore/hyphen fixes and moves
    'atorch_j7-c': ('atorch-j7-c', 'energy-meter'),
    'xzl_studio-ax': ('xzl-studio-ax', 'mixed-signal-devices'),
    'xzl_studio-dx': ('xzl-studio-dx', 'mixed-signal-devices'),
    'instrustar_isds205a': ('instrustar-isds205a', 'oscilloscope'),
    'braintechnology-usb-interface-v2.x': ('braintechnology-usb-interface-v2x', 'logic-analyzer'),
    
    # Missing categorizations
    'fluke-187-189': ('fluke-187-189', 'multimeter'),
    'fluke-287-289': ('fluke-287-289', 'multimeter'),
    'fluke-philips-pm2800-series': ('fluke-philips-pm2800-series', 'power-supply'),
}

def fix_device_names():
    """Fix device names and move to proper categories"""
    misc_dir = HW_DIR / "misc-devices"
    
    for old_name, (new_name, category) in DEVICE_FIXES.items():
        old_path = misc_dir / old_name
        if old_path.exists():
            # Create target directory
            target_dir = HW_DIR / category / new_name
            target_dir.parent.mkdir(exist_ok=True)
            
            # Move and rename
            if target_dir.exists():
                shutil.rmtree(target_dir)
            shutil.move(str(old_path), str(target_dir))
            print(f"Fixed: {old_name} -> {category}/{new_name}")
        else:
            print(f"Not found: {old_name}")

def main():
    """Main function"""
    print("Fixing device names and moving to proper categories...")
    fix_device_names()
    print("Device name fixes complete!")

if __name__ == "__main__":
    main()
