#!/usr/bin/env python3
"""
Categorize and move hardware devices from misc-devices to proper categories
"""

import shutil
from pathlib import Path

HW_DIR = Path("hw")

# Device categorization based on sigrok supported hardware page
DEVICE_CATEGORIES = {
    # Logic Analyzers
    'logic-analyzer': [
        '128axc-based-usbee-ax-pro-clone', 'armfly-mini-logic', 'asix-omega', 'asix-sigma',
        'az-delivery-logic-analyzer', 'beaglelogic', 'braintechnology-usb-interface-v2x',
        'braintechnology-usb-lps', 'chronovu-la8', 'chronovu-la16', 'cwav-usbee-sx',
        'dangerous-prototypes-buspirate', 'dangerous-prototypes-usb-ir-toy', 'dreamsourcelab-dslogic',
        'dreamsourcelab-dslogic-basic', 'dreamsourcelab-dslogic-plus', 'dreamsourcelab-dslogic-pro',
        'ee-electronics-esla100', 'ftdi-la', 'grand-idea-studio-jtagulator', 'greatfet-one',
        'hantek-4032l', 'hantek-6022bl', 'hobby-components-hctest0006', 'ikalogic-scanalogic-2',
        'ikalogic-scanaplus', 'kingst-la2016', 'kingst-la5016', 'kingst-la5032',
        'kingst-kqs3506-la16100', 'lcsoft-mini-board', 'lecroy-logicstudio', 'logic-shrimp',
        'mcu123-saleae-logic-clone', 'meilhaus-logian-16l', 'microchip-pickit2', 'mcu123-usbee-ax-pro-clone',
        'mcupro-logic16-clone', 'noname-saleae-logic-clone', 'openbench-logic-sniffer',
        'prist-akip-9101', 'robomotic-buglogic-3', 'robomotic-minilogic', 'saleae-logic',
        'saleae-logic16', 'saanlima-pipistrello-ols', 'sump-compatibles', 'sysclk-lwla1016',
        'sysclk-lwla1034', 'sysclk-sla5032', 'vktech-saleae-clone', 'wayengineer-saleae16',
        'zeroplus-logic-cube-lap-c16032', 'zeroplus-logic-cube-lap-c322000', 'zeroplus-lap-16128u',
        'acute-pkla-1216', 'arduino', 'codethink-interrogizer', 'cola', 'dreamsourcelab-dslogic-u3pro16',
        'hsa-logic', 'ideofy-la-08', 'intronix-logicport-la1034', 'link-instruments-la-5580',
        'minila', 'minila-mockup', 'noname-la16', 'noname-xl-logic16-100m', 'rockylogic-ant8',
        'rockylogic-ant18e', 'sysclk-lwla2034', 'techtools-digiview-dv1-100', 'tektronix-tla520x',
        'xmos-xtag-2', 'zlg-la1032'
    ],
    
    # Mixed-signal devices (MSO)
    'mixed-signal-devices': [
        'armfly-ax-pro', 'sysclk-ax-pro', 'ee-electronics-esla201a', 'ht-usbee-axpro',
        'lecroy-oscilloscope-series', 'noname-lht00su1', 'rigol-ds1000d-series', 'rigol-ds4000-series',
        'rigol-vs5000d-series', 'rohdeschwarz-hmo-3000-series', 'rohdeschwarz-rt-series',
        'saleae-logic-pro-16', 'siglent-sds1000x-series', 'siglent-sds2000x-series',
        'yokogawa-dlm2000-series', 'xzlstudio-ax', 'xzlstudio-dx', 'agilent-mso7104a',
        'bitscope-bs10', 'digilent-analog-discovery', 'hantek-1008c', 'ht-usbee-dxpro',
        'labnation-smartscope', 'link-instruments-mso-19', 'meilhaus-mephisto-scope1',
        'polabs-poscope-basic2', 'quantasylum-qa100', 'rigol-mso5000-series', 'saleae-logic8',
        'saleae-logic-pro-8', 'pico-technology-picoscope-3205d-mso', 'hantek-dso3254a'
    ],
    
    # Oscilloscopes
    'oscilloscope': [
        'agilent-dso1000-series', 'fluke-scopemeter-199b', 'gw-instek-gds-800-series',
        'hameg-hmo-compact-series', 'hantek-6022be', 'hantek-dso-2090', 'hung-chang-dso-2100',
        'rigol-ds1000e-series', 'rigol-ds1000z-series', 'rigol-ds2000-series', 'rigol-vs5000-series',
        'rocktech-bm102', 'sainsmart-dds120', 'yixingdianzi-mdso', 'dreamsourcelab-dscope-c20p',
        'fluke-scopemeter-123', 'focussz-fosc21', 'gw-instek-gds-2000-series', 'hantek-6052be',
        'hantek-6254bd', 'hantek-dso-1200', 'hantek-dso-2100', 'hantek-dso-220', 'hantek-pso2020',
        'hantek-dso-2250', 'hantek-dso-5200a', 'hantek-idso1070', 'hantek-idso1070a',
        'incite-technology-usb-duxfast', 'instrustarisds205a', 'loto-osc802', 'nexus-computing-osciprime',
        'owon-sds-series', 'pico-technology-picoscope-2203', 'pico-technology-picoscope-2204a',
        'pico-technology-picoscope-2205', 'pico-technology-picoscope-3206', 'pico-technology-picoscope-5203',
        'sainsmart-dds140', 'soundcard', 'tektronix-tds2000b-series', 'uni-t-utd2042c',
        'velleman-pcsu1000', 'velleman-wfs210', 'voltcraft-dso-220', 'voltcraft-dso-3062c'
    ],
    
    # Multimeters
    'multimeter': [
        'agilent-34401a', 'agilent-34405a', 'agilent-u12xxx-series', 'bbc-goertz-metrawatt-m2110',
        'brymen-bm257', 'brymen-bm257s', 'brymen-bm525s', 'brymen-bm829s', 'brymen-bm857',
        'brymen-bm859s', 'brymen-bm869', 'digitek-dt4000zc', 'eevblog-121gw', 'fluke-187189',
        'fluke-287289', 'fluke-45', 'gossen-metrawatt-metrahit-14a', 'gossen-metrawatt-metrahit-16i',
        'gossen-metrawatt-metrahit-18s', 'gossen-metrawatt-metrahit-25s', 'gossen-metrawatt-metrahit-29s',
        'gossen-metrawatt-t-com-kmm2002', 'gw-instek-gdm-397', 'gw-instek-gdm-8251a',
        'gw-instek-gdm-8255a', 'gw-instek-gdm-9060', 'gw-instek-gdm-9061', 'hp-3457a', 'hp-3478a',
        'ht-instruments-ht410', 'iso-tech-idm103n', 'keysight-34465a', 'mastech-mas345',
        'mastech-ms2115b', 'mastech-ms8250b', 'mastech-ms8250d', 'meterman-38xr', 'metex-m-3850m',
        'metex-m-4650cr', 'metex-me-21', 'metex-me-31', 'metrix-mx56c', 'mooshim-engineering-mooshimeter',
        'norma-dm950', 'pce-pce-dm32', 'peaktech-3330', 'peaktech-3410', 'peaktech-3415',
        'peaktech-4370', 'peaktech-4390a', 'radioshack-22-168', 'radioshack-22-805', 'radioshack-22-812',
        'siemens-b1026', 'siemens-b1105', 'siglent-sdm3055', 'sparkfun-70c', 'tecpel-dmm-8061',
        'tekpower-tp4000zc', 'tenma-72-7730', 'tenma-72-7732', 'tenma-72-7745', 'tenma-72-7750',
        'tenma-72-9380a', 'uni-t-ut60e', 'uni-t-ut61b', 'uni-t-ut61c', 'uni-t-ut61d', 'uni-t-ut61e',
        'uni-t-ut71c', 'uni-t-ut181a', 'va-va18b', 'va-va40b', 'velleman-dvm4100', 'victor-70c',
        'victor-86c', 'voltcraft-m-3650cr', 'voltcraft-m-3650d', 'voltcraft-m-4650cr', 'voltcraft-me-42',
        'voltcraft-vc-820', 'voltcraft-vc-830', 'voltcraft-vc-840', 'voltcraft-vc-870', 'voltcraft-vc-920',
        'voltcraft-vc-940', 'voltcraft-vc-96', 'appa-107', 'appa-multimeters', 'benning-mm-12',
        'cem-dt-987bt', 'digitek-dt8000', 'digitek-dt80000', 'escort-179', 'gossen-metrawatt-metrahit-28c',
        'gossen-metrawatt-metrahit-28s', 'gossen-metrawatt-metrahit-30m', 'gossen-metrawatt-metrahit-x-tra',
        'hyelec-ms8236', 'mastech-m9803r', 'metrix-mx53', 'owon-xdm2041', 'peaktech-3442',
        'peaktech-4380', 'peaktech-4390', 'protek-6500', 'rigol-dm3068', 'rs-pro-s2', 'tenma-72-1016',
        'uni-t-ut81b', 'voltcraft-m-3850d', 'voltcraft-m-3890dt', 'voltcraft-m-4660a', 'voltcraft-vc-890',
        'voltcraft-vc-950'
    ],
    
    # LCR meters
    'lcr-meter': [
        'der-ee-de-5000', 'mastech-ms5308', 'peaktech-2165', 'peaktech-2170', 'uni-t-ut612', 'voltcraft-4080'
    ],
    
    # Sound level meters
    'sound-level-meter': [
        'agilent-u1732b', 'bk-precision-879b', 'cem-dt-8852', 'colead-sl-5868p', 'kecheng-kc-330b',
        'pce-pce-322a', 'tondaj-sl-814'
    ],
    
    # Thermometers
    'thermometer': [
        'pce-pce-222', 'voltcraft-dl-160s', 'voltcraft-dl-161s', 'appa-55ii', 'lascar-electronics-el-usb-2',
        'mastech-ms6514', 'mic-98581', 'mic-98583', 'uni-t-ut325', 'voltcraft-k204', 'elitech-rc-3',
        'escort-19', 'pax-instruments-t400', 'rding-temper', 'rding-temper-gold', 'rding-temper1',
        'rding-temper1k2', 'voltcraft-dl-120th', 'voltcraft-dl-140th'
    ],
    
    # Hygrometers
    'hygrometer': [
        'silabs-si7005usb-dongle'
    ],
    
    # Light meters
    'light-meter': [
        'mastech-ms6252b', 'lutron-yk-2005lx'
    ],
    
    # Energy meters
    'energy-meter': [
        'atorchj7-c', 'baylibre-acme', 'edf-teleinfo', 'rdtech-tc66c', 'rdtech-um-series'
    ],
    
    # DAQs
    'daq': [
        'ni-usb-6008'
    ],
    
    # Dataloggers
    'datalogger': [
        'lascar-electronics-el-usb-co', 'testo-435-4', 'gsg-indoor-air-monitor', 'maul-studio-i',
        'voltcraft-co-20'
    ],
    
    # Tachometers
    'tachometer': [
        'uni-t-ut372'
    ],
    
    # Scales
    'scale': [
        'kern-scale-series'
    ],
    
    # Digital loads
    'digital-load': [
        'arachnid-labs-reload-pro', 'atorch-dl24mp-150w-purple', 'itech-it8500-series', 'maynuo-m9812',
        'zketech-ebd-usb'
    ],
    
    # Function generators
    'function-generator': [
        'atten-atz9711', 'siglent-sdl10x0', 'joy-it-jds6600', 'rigol-dg800-series', 'rigol-dg900-series',
        'rigol-dg1000z-series', 'agilent-33120a', 'bg7tbl', 'hantek-dds-3x25', 'hp-3325a',
        'mhinstek-udb1xxxs', 'mhinstek-mhs-5200a', 'siglent-sdg1010', 'velleman-pcg10'
    ],
    
    # Frequency counters
    'frequency-counter': [
        'hp-5350b'
    ],
    
    # Spectrum analyzers
    'spectrum-analyzer': [
        'siglent-ssa3000x-series'
    ],
    
    # Power supplies
    'power-supply': [
        'atten-pps3203t-3s', 'chroma-61604', 'conrad-digi-35-cpu', 'envox-eez-h24005',
        'envox-eez-bench-box-3', 'gw-instek-gpd-series', 'hp-66312a', 'hp-6632b',
        'korad-kaxxxxp-series', 'manson-hcs-3xxx-series', 'motech-lps-301', 'owon-p4000-series',
        'flukephilips-pm2800-series', 'rdtech-dps-series', 'rdtech-rd-series', 'rigol-dp800-series',
        'rohdeschwarz-hmc-8043', 'rohdeschwarz-hmp-4000-series', 'delta-elektronika-sm3300-series',
        'etommens-etm-xxxxp-series', 'hanmatek-hm305p', 'rockseed-rs310p', 'siglent-spd3303-series',
        'voltcraft-18220'
    ],
    
    # Multiplexers
    'multiplexer': [
        'dcttech-usbrelay', 'devantech-eth008', 'hp-59306a', 'icstation-usbrelay', 'gembird-silvershield'
    ],
    
    # GPIB interfaces
    'gpib-interface': [
        'agilent-82357a', 'ar488', 'beiming-s82357', 'ics-488-usb', 'gpib-usb-82357b-clone',
        'national-instruments-gpib-enet', 'national-instruments-gpib-usb-hs', 'prologix-gpib-usb',
        'galvant-gpibusb'
    ],
    
    # Misc devices (non-hardware pages)
    'misc-devices': [
        'page', 'read', 'home', 'downloads', 'hardware-support', 'file-formats', 'protocol-decoders',
        'developers', 'privacy-policy', 'about-sigrok', 'disclaimers'
    ]
}

def create_categories():
    """Create category directories"""
    categories = set(DEVICE_CATEGORIES.keys())
    
    for category in categories:
        category_dir = HW_DIR / category
        category_dir.mkdir(exist_ok=True)
        print(f"Created category: {category}")

def move_devices():
    """Move devices from misc-devices to proper categories"""
    misc_dir = HW_DIR / "misc-devices"
    if not misc_dir.exists():
        print("No misc-devices directory found")
        return
    
    moved_count = 0
    unknown_devices = []
    
    for device_dir in misc_dir.iterdir():
        if device_dir.is_dir():
            device_slug = device_dir.name
            
            # Find which category this device belongs to
            target_category = None
            for category, devices in DEVICE_CATEGORIES.items():
                if device_slug in devices:
                    target_category = category
                    break
            
            if target_category and target_category != 'misc-devices':
                # Move device to proper category
                target_dir = HW_DIR / target_category / device_slug
                if target_dir.exists():
                    shutil.rmtree(target_dir)
                shutil.move(str(device_dir), str(target_dir))
                print(f"Moved {device_slug} -> {target_category}")
                moved_count += 1
            else:
                unknown_devices.append(device_slug)
    
    print(f"\nMoved {moved_count} devices")
    
    if unknown_devices:
        print(f"\nUnknown devices (staying in misc-devices): {len(unknown_devices)}")
        for device in unknown_devices[:10]:  # Show first 10
            print(f"  - {device}")
        if len(unknown_devices) > 10:
            print(f"  ... and {len(unknown_devices) - 10} more")

def main():
    """Main function"""
    print("Creating hardware categories and moving devices...")
    
    create_categories()
    move_devices()
    
    print("\nCategorization complete!")

if __name__ == "__main__":
    main()
