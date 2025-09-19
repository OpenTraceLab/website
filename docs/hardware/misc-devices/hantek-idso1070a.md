# Hantek Idso1070A
| | | |:--------------------|----------------------------------------------------------------------------------------------------------------| | Status | planned | | Channels | 2 | | Samplerate | 250MS/s (125 for 2 channels) | | Analog bandwidth | 70MHz | | Vertical resolution | 8bit | | Triggers | CH1, CH2, EXT (all hardware) | | Input impedance | 1MΩ‖25pF | | Memory | ? | | Display | none | | Connectivity | USB / WiFi | | Website | *hantek.com* | **Hantek iDSO1070A** The **Hantek iDSO1070A** is a USB/WiFi-based, 2-channel oscilloscope with an analog bandwidth of 70MHz and 250MS/s sampling rate.
## Contents
\- *1 Hardware* \- *2 Photos* \- *3 Notes* \- *4 Protocol* \- *5 Resources*
## Hardware \- **Main chip**: [Xilinx Spartan XC3S50A](http://www.xilinx.com/support/documentation/spartan-3an_data_sheets.htm) ([datasheet](http://www.xilinx.com/support/documentation/data_sheets/ds557.pdf)) \- **Wifi module**: [MxChip EMW3162](http://en.mxchip.com/product/wifi_product/39) ([datasheet](http://en.mxchip.com/download/getFiles/57391c8444837.pdf/Datasheet.pdf))  \- **Main oscillator**: 50MHz 50.000 YX FH ## Photos \-
[*Image: \1*
PCB, top
\-
[*Image: \1*
PCB, bottom
\-
[*Image: \1*
Channel module
\-
[*Image: \1*
WiFi Module
\-
[*Image: \1*
Detail
## Notes \- Has been found cross channel interference. To observe this just connect Channel 1 to 5V DC and it is possible to see the shift of Channel 2 zero offset. ## Protocol [Reverse engineered implementation of the protocol](https://github.com/hhornbacher/idso1070-protocol) ## Resources
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=Hantek_iDSO1070A&oldid=13978](https://OpenTraceLab.org/w/index.php?title=Hantek_iDSO1070A&oldid=13978)"
: \- *Device* \- *Oscilloscope* \- *Planned*
## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
