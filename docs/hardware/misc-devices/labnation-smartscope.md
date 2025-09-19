# Labnation Smartscope
| | | |:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------:| | [*Image: \1* | | | Status | planned | | Channels | 8 | | Samplerate | 100MHz | | Samplerate (state) | — | | Triggers | low, high, rising, falling, edge | | Min/max voltage | ? | | Threshold voltage | Fixed: VIL=0.8V, VIH=2.0V | | Memory | 4Msamples (8MByte SDRAM) | | Compression | ? | | Website | [lab-nation.com](https://www.lab-nation.com) | **LabNation SmartScope** The **LabNation SmartScope** is a USB-based mixed-signal oscilloscope (100 MS/s, 45MHz bandwidth), 8-channel logic analyzer (100MHz), arbitrary waveform generator / function generator. See *LabNation SmartScope/Info* for some more details (such as **lsusb -v** output) on the device.
## Contents
\- *1 Hardware* \- *2 Photos* \- *3 Protocol* \- *4 Progress* \- *5 Resources*
## Hardware \- **FPGA (3840 logic cells)**: *Xilinx XC6SXL4* ([datasheet](http://www.xilinx.com/support/documentation/data_sheets/ds160.pdf)) \- **64Mbit SDRAM**: [Alliance Memory AS4C4M16S](http://www.alliancememory.com/datasheets/AS4C4M16S.asp) ([datasheet](http://www.alliancememory.com/pdf/dram/64M-AS4C4M16S.pdf)) \- **Dual-channel, 8-bit, 100Msps ADC**: *Maxim MAX19506* ([datasheet](http://datasheets.maximintegrated.com/en/ds/MAX19506.pdf)) \- **8-bit microcontroller with full-speed USB**: [Microchip PIC18F14K50](http://www.microchip.com/wwwproducts/Devices.aspx?dDocName=en533924) ([datasheet](http://ww1.microchip.com/downloads/en/DeviceDoc/41350E.pdf)) \- **Single-pole normally-closed SOP OptoMOS relay**: [Ixys CPC1125N](http://www.ixysic.com/Products/SSRFormB.htm) ([datasheet](http://www.ixysic.com/home/pdfs.nsf/www/CPC1125N.pdf/$file/CPC1125N.pdf)) \- **250MHz, rail-to-rail I/O, CMOS dual opamp**: [Texas Instruments OPA2354](http://www.ti.com/product/opa2354) ([datasheet](http://www.ti.com/lit/gpn/opa2354)) \- **Quad buffer/line driver with 3-state outputs**: *Diodes Incorporated 74LVC126A* ([datasheet](http://diodes.com/datasheets/74LVC126A.pdf)) \- 0480000 OCP1332 1725 \- 4x CGA4V \- S03A ## Photos \-
[*Image: \1*
Package, top
\-
[*Image: \1*
Package, bottom
\-
[*Image: \1*
Package, contents
\-
[*Image: \1*
Cables and probes
\-
[*Image: \1*
P6060 probe
\-
[*Image: \1*
Device, top
\-
[*Image: \1*
Device, bottom
\-
[*Image: \1*
Probe connector
\-
[*Image: \1*
Misc connectors
\-
[*Image: \1*
PCB, top
\-
[*Image: \1*
PCB, bottom
\-
[*Image: \1*
Analog frontend
\-
[*Image: \1*
Xilinx XC6SLX4
\-
[*Image: \1*
Alliance AS4C4M16S
\-
[*Image: \1*
Maxim MAX19506
\-
[*Image: \1*
Microchip 18LF14K50
\-
[*Image: \1*
Ixys CPC1125N
\-
[*Image: \1*
74LVC126A
\-
[*Image: \1*
TI OPA2354
## Protocol ## Progress Detection and bitstream loading implemented in OpenTraceCapture driver. Scope init and acquisition WIP in python test code. See <https://github.com/karlp/OpenTraceCapture/tree/devel/labnation> ## Resources \- [Vendor software](https://www.lab-nation.com/download)
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=LabNation_SmartScope&oldid=13200](https://OpenTraceLab.org/w/index.php?title=LabNation_SmartScope&oldid=13200)"
: \- *Device* \- *Logic analyzer* \- *Oscilloscope* \- *Mixed-signal oscilloscope* \- *Planned*
## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
