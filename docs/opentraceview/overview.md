# OpenTraceView

OpenTraceView is the graphical user interface for visualizing and analyzing captured signals in the OpenTraceLab ecosystem.

![OpenTraceView Screenshot](../assets/img/3ea18a7f0fd4ba3e14f54af75737e957b8136042.png)

## Features

- **Fast signal rendering** - O(log N) performance at all zoom levels
- **Protocol decoder support** - 100+ built-in protocol decoders
- **Trace groups** - Organize related signals together
- **Stacked decoders** - Chain decoders for complex analysis
- **Export capabilities** - Save data in multiple formats
- **Cross-platform** - Linux, Windows, macOS support

## Key Capabilities

### Signal Visualization
- Multi-channel digital signal display
- Analog signal support (oscilloscope mode)
- Customizable colors and layouts
- Zoom and pan with smooth navigation

### Protocol Analysis
- Automatic protocol detection
- Real-time decoding during capture
- Hierarchical decoder stacking
- Export decoded data to CSV/JSON

### Hardware Integration
- Direct connection to logic analyzers
- Live capture and analysis
- Trigger configuration
- Sample rate optimization

## Getting Started

1. **[Install OpenTraceView](../get-started/install.md)**
2. **Connect your logic analyzer** - USB connection
3. **Configure channels** - Set up signal names and types
4. **Start capturing** - Click "Run" to begin acquisition
5. **Add decoders** - Select protocols from the Decoders menu

## Supported Protocols

OpenTraceView includes decoders for:

- **Serial**: UART, SPI, I²C, RS232/485
- **Automotive**: CAN, LIN, FlexRay, K-Line
- **Embedded**: ARM ITM/ETM, JTAG, SWD
- **Audio**: I²S, PCM, AC97
- **Wireless**: NRF24L01, CC1101, Bluetooth
- **And 100+ more protocols**

## Advanced Features

### Custom Decoders
Write your own protocol decoders in Python:
```python
import sigrokdecode as srd

class Decoder(srd.Decoder):
    api_version = 3
    id = 'my_protocol'
    name = 'My Protocol'
    # ... decoder implementation
```

### Automation
Integrate with scripts and automation:
```bash
# Export decoded data
opentraceview --input capture.sr --export csv --output data.csv

# Batch processing
for file in *.sr; do
    opentraceview --input "$file" --decode i2c --export json
done
```

## Manual and Documentation

- **[User Manual](https://opentracelab.org/doc/opentraceview/manual.html)** - Complete usage guide
- **[Video Tutorial](https://www.youtube.com/watch?v=dobU-b0_L1I)** - Logic analyzer basics
- **[Architecture Overview](architecture.md)** - Technical details

## Building from Source

```bash
# Requirements
sudo apt install qtbase5-dev qtchooser qt5-qmake qtbase5-dev-tools libqt5svg5-dev

# Build
git clone https://github.com/OpenTraceLab/opentraceview
cd opentraceview
cmake .
make
sudo make install
```

## Contributing

- **Translations** - Help translate the interface
- **Protocol decoders** - Add support for new protocols  
- **Bug reports** - Report issues on GitHub
- **Feature requests** - Suggest improvements

See our [contributing guide](../community/contributing.md) for details.
