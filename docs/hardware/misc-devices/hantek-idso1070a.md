# Hantek Idso1070A

| | | |:--------------------|----------------------------------------------------------------------------------------------------------------| | Status | planned | | Channels | 2 | | Samplerate | 250MS/s (125 for 2 channels) | | Analog bandwidth | 70MHz | | Vertical resolution | 8bit | | Triggers | CH1, CH2, EXT (all hardware) | | Input impedance | 1MΩ‖25pF | | Memory | ? | | Display | none | | Connectivity | USB / WiFi | | Website | [hantek.com](http://www.hantek.com/en/ProductDetail_2_31.html) | **Hantek iDSO1070A** The **Hantek iDSO1070A** is a USB/WiFi-based, 2-channel oscilloscope with an analog bandwidth of 70MHz and 250MS/s sampling rate. 
## Contents 
\- [1 Hardware](Hantek_iDSO1070A.html#Hardware) \- [2 Photos](Hantek_iDSO1070A.html#Photos) \- [3 Notes](Hantek_iDSO1070A.html#Notes) \- [4 Protocol](Hantek_iDSO1070A.html#Protocol) \- [5 Resources](Hantek_iDSO1070A.html#Resources) 
## Hardware \- **Main chip**: [Xilinx Spartan XC3S50A](http://www.xilinx.com/support/documentation/spartan-3an_data_sheets.htm) ([datasheet](http://www.xilinx.com/support/documentation/data_sheets/ds557.pdf)) \- **Wifi module**: [MxChip EMW3162](http://en.mxchip.com/product/wifi_product/39) ([datasheet](http://en.mxchip.com/download/getFiles/57391c8444837.pdf/Datasheet.pdf))  \- **Main oscillator**: 50MHz 50.000 YX FH ## Photos \- 
[![\1](../../assets/hardware/general/\2)](./File:Hantek_iDSO1070A_inside1_front.JPG.html)
PCB, top
\- 
[![\1](../../assets/hardware/general/\2)](./File:Hantek_iDSO1070A_inside1_back.JPG.html)
PCB, bottom
\- 
[![\1](../../assets/hardware/general/\2)](./File:Hantek_iDSO1070A_channel_module.JPG.html)
Channel module
\- 
[![\1](../../assets/hardware/general/\2)](./File:Hantek_iDSO1070A_wifi_module.JPG.html)
WiFi Module
\- 
[![\1](../../assets/hardware/general/\2)](./File:Hantek_iDSO1070A_detail_1.JPG.html)
Detail
## Notes \- Has been found cross channel interference. To observe this just connect Channel 1 to 5V DC and it is possible to see the shift of Channel 2 zero offset. ## Protocol [Reverse engineered implementation of the protocol](https://github.com/hhornbacher/idso1070-protocol) ## Resources
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=Hantek_iDSO1070A&oldid=13978](https://OpenTraceLab.org/w/index.php?title=Hantek_iDSO1070A&oldid=13978)" 
[Categories](specialcategories-specialcategories.md): \- [Device](./Category:Device.html "Category:Device") \- [Oscilloscope](./Category:Oscilloscope.html "Category:Oscilloscope") \- [Planned](./Category:Planned.html "Category:Planned")

## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
