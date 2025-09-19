# Hantek Idso1070
| | | |:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------------:| | [*Image: \1* | | | Status | planned | | Source code | [[1]](http://github.com/OpenTraceLab/?p=OpenTraceCapture.git;a=tree;f=src/hardware/) | | Channels | 2 | | Samplerate | 250MSa/s | | Analog bandwidth | 70MHz | | Vertical resolution | 8bit | | Triggers | none (SW-only) | | Input impedance | 1MΩ‖25pF | | Memory | none | | Display | none | | Connectivity | USB / Wifi | | Website | *hantek.com* | **Hantek iDSO1070** The **Hantek iDSO1070** is a self powered, 2-channel oscilloscope with an analog bandwidth of 70MHz with 250MSa/s sampling rate (125MSa/s each channel). The internal battery let the device to run up to 3-4 hours. See [Hantek iDSO1070/Info](https://OpenTraceLab.org/w/index.php?title=Hantek_iDSO1070/Info&action=edit&redlink=1 "Hantek iDSO1070/Info \(page does not exist\)") for more details (such as **lsusb -v** output) about the device.
## Contents
\- *1 Hardware* \- *2 Photos* \- *3 Protocol* \- *4 Resources*
## Hardware \- **Main chip**: [Xilinx Spartan XC3S50A](http://www.xilinx.com/support/documentation/spartan-3an_data_sheets.htm) ([datasheet](http://www.xilinx.com/support/documentation/data_sheets/ds557.pdf)) \- **Main oscillator**: 50MHz 50.000 YX FH ## Photos \-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
## Protocol See [Reverse Engineered Protocol](https://github.com/hhornbacher/idso1070-protocol/blob/master/lib/README.md). When the "Refresh" button is **not** pressed, the device run in Wifi mode, when "Refresh" button is kept pressed at boot it run in USB mode (USB vendor_id and device_id will change). ## Resources \- [Linux Driver and Software on GitHub](https://github.com/hhornbacher/idso1070-protocol)
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=Hantek_iDSO1070&oldid=13360](https://OpenTraceLab.org/w/index.php?title=Hantek_iDSO1070&oldid=13360)"
: \- *Device* \- *Oscilloscope* \- *Planned*
## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
