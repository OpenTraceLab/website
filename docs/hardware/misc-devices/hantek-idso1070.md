# Hantek Idso1070

| | | |:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------------:| | [![\1](../../assets/hardware/general/\2)](./File:Hantek_iDSO1070A.JPG.html) | | | Status | planned | | Source code | [[1]](http://github.com/OpenTraceLab/?p=OpenTraceCapture.git;a=tree;f=src/hardware/) | | Channels | 2 | | Samplerate | 250MSa/s | | Analog bandwidth | 70MHz | | Vertical resolution | 8bit | | Triggers | none (SW-only) | | Input impedance | 1MΩ‖25pF | | Memory | none | | Display | none | | Connectivity | USB / Wifi | | Website | [hantek.com](http://www.hantek.com/en/productdetail_2_10165.html) | **Hantek iDSO1070** The **Hantek iDSO1070** is a self powered, 2-channel oscilloscope with an analog bandwidth of 70MHz with 250MSa/s sampling rate (125MSa/s each channel). The internal battery let the device to run up to 3-4 hours. See [Hantek iDSO1070/Info](https://OpenTraceLab.org/w/index.php?title=Hantek_iDSO1070/Info&action=edit&redlink=1 "Hantek iDSO1070/Info \(page does not exist\)") for more details (such as **lsusb -v** output) about the device. 
## Contents 
\- [1 Hardware](Hantek_iDSO1070.html#Hardware) \- [2 Photos](Hantek_iDSO1070.html#Photos) \- [3 Protocol](Hantek_iDSO1070.html#Protocol) \- [4 Resources](Hantek_iDSO1070.html#Resources) 
## Hardware \- **Main chip**: [Xilinx Spartan XC3S50A](http://www.xilinx.com/support/documentation/spartan-3an_data_sheets.htm) ([datasheet](http://www.xilinx.com/support/documentation/data_sheets/ds557.pdf)) \- **Main oscillator**: 50MHz 50.000 YX FH ## Photos \- 
[![\1](../../assets/hardware/general/\2)](./File:Hantek_iDSO1070A_inside1_front.JPG.html)
\- 
[![\1](../../assets/hardware/general/\2)](./File:Hantek_iDSO1070A_inside1_back.JPG.html)
\- 
[![\1](../../assets/hardware/general/\2)](./File:Hantek_iDSO1070A_channel_module.JPG.html)
\- 
[![\1](../../assets/hardware/general/\2)](./File:Hantek_iDSO1070A_wifi_module.JPG.html)
\- 
[![\1](../../assets/hardware/general/\2)](./File:Hantek_iDSO1070A_detail_1.JPG.html)
## Protocol See [Reverse Engineered Protocol](https://github.com/hhornbacher/idso1070-protocol/blob/master/lib/README.md). When the "Refresh" button is **not** pressed, the device run in Wifi mode, when "Refresh" button is kept pressed at boot it run in USB mode (USB vendor_id and device_id will change). ## Resources \- [Linux Driver and Software on GitHub](https://github.com/hhornbacher/idso1070-protocol)
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=Hantek_iDSO1070&oldid=13360](https://OpenTraceLab.org/w/index.php?title=Hantek_iDSO1070&oldid=13360)" 
[Categories](specialcategories-specialcategories.md): \- [Device](./Category:Device.html "Category:Device") \- [Oscilloscope](./Category:Oscilloscope.html "Category:Oscilloscope") \- [Planned](./Category:Planned.html "Category:Planned")

## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
