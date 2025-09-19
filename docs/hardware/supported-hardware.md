# Supported Hardware
OpenTraceLab supports a wide range of measurement devices through the OpenTraceCapture library. This page provides an overview of supported hardware categories and specific devices.
## Device Categories
### Logic Analyzers
Digital signal capture devices for protocol analysis and debugging.
- **FX2-based devices** - Generic Cypress FX2 logic analyzers
- **Saleae Logic series** - Professional USB logic analyzers
- **Kingst LA series** - Affordable logic analyzers
- **Hantek 4032L** - 32-channel logic analyzer
- **OpenBench LogicSniffer** - Open hardware design
[View all logic analyzers →](logic-analyzer/fx2lafw.md)
### Multimeters
Digital multimeters with PC connectivity for automated measurements.
- **UNI-T series** - UT61x, UT32x models
- **Voltcraft series** - VC-820, VC-840 models
- **Brymen series** - BM25x models
[View all multimeters →](multimeter/uni-t.md)
### Oscilloscopes
Digital storage oscilloscopes with PC control capabilities.
- **Rigol DS series** - DS1000Z, DS2000, DS4000 series
- **Hantek DSO series** - DSO-2xxx, DSO-5xxx models
- **Siglent SDS series** - SDS1000 models
[View all oscilloscopes →](oscilloscope/rigol-ds.md)
### Power Supplies
Programmable power supplies with remote control.
- **Korad series** - KA3005P, KD3005P models
- **Rigol DP series** - DP832, DP831A models
[View all power supplies →](power-supply/korad.md)
## Device Status
| Device Type | Supported Models | Status |
|-------------|------------------|---------|
| Logic Analyzers | 40+ models | ✅ Full support |
| Multimeters | 30+ models | ✅ Full support |
| Oscilloscopes | 20+ models | ✅ Full support |
| Power Supplies | 15+ models | ✅ Full support |
| Function Generators | 10+ models | ✅ Full support |
| LCR Meters | 5+ models | ✅ Full support |
## Adding New Hardware
To add support for new hardware:
1. Check if a similar device driver exists
2. Implement the driver following our [hardware driver API](../opentracecapture/overview.md)
3. Submit a pull request with documentation
See our [contributing guide](../community/contributing.md) for details.
