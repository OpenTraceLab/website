# Frequently Asked Questions

## General Questions

### What is OpenTraceLab?
OpenTraceLab is an open-source ecosystem for logic analysis, consisting of three main components:
- **OpenTraceCapture** - Hardware abstraction and signal acquisition
- **OpenTraceView** - Graphical interface for signal visualization
- **OpenTraceDecode** - Protocol decoders for signal interpretation

### How is OpenTraceLab different from sigrok?
OpenTraceLab is a fork of the sigrok project with modernized architecture, enhanced features, and active development focused on logic analysis applications.

### What hardware does OpenTraceLab support?
OpenTraceLab supports 200+ devices including:
- FX2-based logic analyzers (~$10)
- Saleae Logic series
- Rigol oscilloscopes
- Various multimeters, power supplies, and function generators

## Installation Issues

### "Cannot access USB device" error
**Linux:** Install udev rules and add user to plugdev group:
```bash
sudo cp contrib/60-opentracelab.rules /etc/udev/rules.d/
sudo usermod -a -G plugdev $USER
```

**Windows:** Run OpenTraceView as Administrator or install proper USB drivers.

### "Library not found" errors
```bash
# Linux - update library cache
sudo ldconfig

# Or set library path
export LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH
```

### Python decoder errors
Ensure Python development packages are installed:
```bash
sudo apt install python3-dev python3-setuptools python3-numpy
```

## Usage Questions

### How do I capture my first signal?
1. Connect your logic analyzer via USB
2. Launch OpenTraceView
3. Configure channels and sample rate
4. Connect probes to your circuit
5. Click "Run" to start capture

See our [capture guide](capture-first-trace.md) for details.

### Which logic analyzer should I buy?
For beginners, we recommend:
- **FX2-based analyzers** - Cheap (~$10), 8-16 channels, 24MHz
- **Saleae Logic 8** - Professional quality, excellent software
- **OpenBench LogicSniffer** - Open hardware design

### How do I decode protocols?
1. Capture your signal in OpenTraceView
2. Go to **Decoders** menu
3. Select your protocol (I²C, SPI, UART, etc.)
4. Configure channel mappings
5. View decoded results

### Can I write custom decoders?
Yes! OpenTraceDecode uses Python for protocol decoders. See our [decoder development guide](../opentracedecode/decoder-howto.md).

## Hardware Questions

### What sample rate do I need?
- **I²C/SPI:** 4-10x the clock frequency
- **UART:** 10x the baud rate minimum
- **High-speed protocols:** Use fastest available rate

### How many channels do I need?
- **Basic protocols:** 2-4 channels (I²C, SPI, UART)
- **Parallel buses:** 8-16 channels
- **Complex systems:** 16+ channels recommended

### What about probe quality?
Good probes are essential:
- Use short ground leads (<3cm)
- Quality probe hooks (E-Z-Hook XKM series)
- Proper impedance matching for high-speed signals

## Software Questions

### Can I use OpenTraceLab with other tools?
Yes! OpenTraceLab can:
- Export data to CSV, JSON, VCD formats
- Integrate with scripts via OpenTraceCLI
- Work with collectd for monitoring
- Interface with custom applications via API

### Does OpenTraceLab run on my OS?
OpenTraceLab supports:
- **Linux** - Native packages and AppImage
- **Windows** - Installer and portable versions
- **macOS** - Homebrew and .dmg packages
- **FreeBSD/NetBSD/OpenBSD** - Source builds

### How do I get help?
- **Documentation** - This website and manuals
- **GitHub Issues** - Bug reports and feature requests
- **Community** - Discussions and forums
- **Email** - Direct support for complex issues

## Performance Questions

### OpenTraceView is slow with large captures
- Use "Fast" rendering mode for large datasets
- Reduce visible time range when zoomed out
- Consider using OpenTraceCLI for batch processing
- Increase system RAM for better performance

### My device isn't detected
1. Check USB connection and cables
2. Verify device is supported
3. Install proper drivers/udev rules
4. Try different USB ports
5. Check device power requirements

### Capture keeps stopping
- Check USB cable quality
- Reduce sample rate if bandwidth limited
- Verify trigger settings
- Check available disk space
- Monitor system resources

## Protocol-Specific Questions

### I²C decoding shows errors
- Verify SCL/SDA channel assignments
- Check pull-up resistors on I²C lines
- Ensure adequate sample rate (>4x I²C clock)
- Verify signal voltage levels

### UART data looks garbled
- Confirm baud rate setting
- Check data bits, parity, stop bits
- Verify signal polarity (inverted?)
- Ensure stable clock reference

### SPI decoding is incorrect
- Verify MOSI/MISO/CLK/CS assignments
- Check SPI mode (CPOL/CPHA settings)
- Confirm bit order (MSB/LSB first)
- Verify chip select polarity

## Troubleshooting

### General debugging steps
1. Check all connections
2. Verify power and ground
3. Confirm signal voltage levels
4. Test with known-good signals
5. Try different sample rates
6. Check for electrical noise

### Getting more help
If you can't find answers here:
1. Search existing GitHub issues
2. Create detailed bug report with:
   - OpenTraceLab version
   - Operating system
   - Hardware details
   - Steps to reproduce
   - Sample capture files
3. Use the "Report Issue" button on any documentation page
