# OpenTraceBroadcaster

OpenTraceBroadcaster is an OBS Studio plugin that displays real-time measurement values from DMM (Digital Multimeter) and LCR (Inductance, Capacitance, Resistance) meters directly in your live streams and recordings.

## Features

- **Real-time measurement overlay** in OBS Studio
- **DMM and LCR meter support** via OpenTraceCapture integration
- **Automatic unit detection** (V, A, Ω, F, H, Hz)
- **Configurable appearance** through OBS properties panel
- **Cross-platform support** (Windows, macOS, Linux)

## Installation

### Prerequisites

- OBS Studio installed
- OpenTraceCapture library
- Compatible DMM/LCR measurement device

### Build from Source

1. **Build OpenTraceCapture:**
   ```bash
   cd OpenTraceCapture
   meson setup builddir
   meson compile -C builddir
   meson install -C builddir
   ```

2. **Build the plugin:**
   ```bash
   cd OpenTraceBroadcaster
   ./build.sh
   ```

3. **Install the plugin:**
   ```bash
   meson install -C builddir
   ```

## Usage

1. **Connect your measurement device** (DMM or LCR meter)
2. **Start OBS Studio**
3. **Add a new Source** → "Measurement Overlay"
4. **Configure the overlay** in Properties:
   - Adjust width and height
   - Set font size and decimal precision
   - Toggle unit display
5. **Position the overlay** in your scene

The plugin automatically detects connected devices and displays measurements in real-time.

## Configuration Options

| Setting | Description | Range |
|---------|-------------|-------|
| Width | Overlay width in pixels | 200-800px |
| Height | Overlay height in pixels | 50-200px |
| Font Size | Text size | 12-48px |
| Decimal Places | Measurement precision | 0-6 places |
| Show Units | Display unit symbols | On/Off |
| Auto Range | Automatic unit scaling | On/Off |

## Supported Devices

Any measurement device supported by OpenTraceCapture, including:

- **Keysight/Agilent** multimeters
- **Fluke** multimeters  
- **Rigol** multimeters
- **LCR meters** with serial/USB interfaces

See the [supported hardware](../hardware/supported-hardware.md) page for a complete list.

## Use Cases

- **Electronics tutorials** - Show live measurements during demonstrations
- **Product reviews** - Display real-time power consumption or specifications
- **Educational content** - Visualize electrical measurements for students
- **Troubleshooting streams** - Share diagnostic measurements with viewers

## Troubleshooting

**Plugin not appearing in OBS:**
- Verify the plugin is installed in the correct OBS plugins directory
- Check OBS log files for loading errors

**No measurement data:**
- Ensure your device is connected and recognized by the system
- Test device detection with `OpenTraceCLI --scan`
- Verify OpenTraceCapture can access the device

**Measurements not updating:**
- Check device connection and power
- Restart OBS Studio
- Verify device compatibility with OpenTraceCapture
