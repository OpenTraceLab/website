#!/usr/bin/env python3
"""
Generate hardware.yaml from categorized devices
"""

import yaml
from pathlib import Path
import re

HW_DIR = Path("hw")
DOCS_DIR = Path("docs")

# Category mappings
CATEGORY_MAPPING = {
    'logic-analyzer': {
        'title': 'Logic Analyzers',
        'columns': ['Image', 'Vendor', 'Model', 'Status']
    },
    'oscilloscope': {
        'title': 'Oscilloscopes', 
        'columns': ['Image', 'Vendor', 'Model', 'Status']
    },
    'mixed-signal-devices': {
        'title': 'Mixed-Signal Devices (MSO)',
        'columns': ['Image', 'Vendor', 'Model', 'Status']
    },
    'multimeter': {
        'title': 'Multimeters',
        'columns': ['Image', 'Vendor', 'Model', 'Status']
    },
    'power-supply': {
        'title': 'Power Supplies',
        'columns': ['Image', 'Vendor', 'Model', 'Status']
    },
    'function-generator': {
        'title': 'Function Generators',
        'columns': ['Image', 'Vendor', 'Model', 'Status']
    }
}

def extract_device_info(device_path):
    """Extract device information from markdown file"""
    index_file = device_path / "index.md"
    if not index_file.exists():
        return None
    
    with open(index_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract title
    title_match = re.search(r'^title:\s*(.+)$', content, re.MULTILINE)
    title = title_match.group(1).strip() if title_match else device_path.name
    
    # Extract infobox data
    info = {}
    infobox_match = re.search(r'<div class="infobox".*?>(.*?)</div>', content, re.DOTALL)
    if infobox_match:
        infobox_content = infobox_match.group(1)
        # Extract table rows
        rows = re.findall(r'\|\s*\*\*([^*]+)\*\*\s*\|\s*([^|]+)\s*\|', infobox_content)
        for key, value in rows:
            info[key.strip()] = value.strip()
    
    # Find first image
    img_dir = device_path / "img"
    image_path = None
    if img_dir.exists():
        for img_file in img_dir.glob('*'):
            if img_file.suffix.lower() in ['.jpg', '.png', '.gif']:
                image_path = f"/website/hardware/{device_path.parent.name}/{device_path.name}/img/{img_file.name}"
                break
    
    # Parse vendor and model from title
    vendor, model = parse_vendor_model(title)
    
    return {
        'title': title,
        'vendor': vendor,
        'model': model,
        'info': info,
        'image': image_path,
        'page': f"{device_path.parent.name}/{device_path.name}/"
    }

def parse_vendor_model(title):
    """Parse vendor and model from device title"""
    # Common patterns
    patterns = [
        r'^([A-Za-z&\-\s]+?)\s+([A-Za-z0-9\-/]+)$',  # "Vendor Model"
        r'^([A-Za-z&\-\s]+?)\s+(.+)$',  # Fallback
    ]
    
    for pattern in patterns:
        match = re.match(pattern, title.strip())
        if match:
            vendor = match.group(1).strip()
            model = match.group(2).strip()
            return vendor, model
    
    # If no pattern matches, use title as model
    return "Unknown", title

def generate_yaml():
    """Generate hardware.yaml from device directories"""
    categories = []
    
    for category_dir in sorted(HW_DIR.iterdir()):
        if not category_dir.is_dir() or category_dir.name == 'misc-devices':
            continue
        
        category_id = category_dir.name
        category_info = CATEGORY_MAPPING.get(category_id, {
            'title': category_id.replace('-', ' ').title(),
            'columns': ['Image', 'Vendor', 'Model', 'Status']
        })
        
        rows = []
        for device_dir in sorted(category_dir.iterdir()):
            if device_dir.is_dir():
                device_info = extract_device_info(device_dir)
                if device_info:
                    row = {
                        'Vendor': device_info['vendor'],
                        'Model': device_info['model'],
                        'Status': device_info['info'].get('Status', device_info['info'].get('status', 'unknown')),
                        'Page': device_info['page']
                    }
                    
                    if device_info['image']:
                        row['Image'] = device_info['image']
                    
                    # Add category-specific fields
                    if category_id == 'logic-analyzer':
                        row['Channels'] = device_info['info'].get('Channels', '')
                        row['Samplerate'] = device_info['info'].get('Samplerate', '')
                    elif category_id == 'oscilloscope':
                        row['Channels'] = device_info['info'].get('Channels', '')
                        row['Bandwidth'] = device_info['info'].get('Bandwidth', '')
                    elif category_id == 'multimeter':
                        row['Digits'] = device_info['info'].get('Digits', '')
                    
                    rows.append(row)
        
        if rows:
            categories.append({
                'id': category_id,
                'title': category_info['title'],
                'columns': category_info['columns'],
                'rows': rows  # Include ALL devices, not just first 10
            })
    
    return {'categories': categories}

def main():
    """Generate and save hardware.yaml"""
    print("Generating hardware.yaml from categorized devices...")
    
    # Create data directory
    data_dir = DOCS_DIR / "data"
    data_dir.mkdir(exist_ok=True)
    
    # Generate YAML data
    hardware_data = generate_yaml()
    
    # Save to file
    yaml_file = data_dir / "hardware.yaml"
    with open(yaml_file, 'w', encoding='utf-8') as f:
        yaml.dump(hardware_data, f, default_flow_style=False, sort_keys=False, allow_unicode=True)
    
    print(f"Generated {yaml_file} with {len(hardware_data['categories'])} categories")
    
    # Print summary
    for cat in hardware_data['categories']:
        print(f"  {cat['title']}: {len(cat['rows'])} devices")

if __name__ == "__main__":
    main()
