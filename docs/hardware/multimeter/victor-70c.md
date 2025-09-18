# Victor 70C

| | | |:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------------------------------------:| | [![\1](../../assets/hardware/general/\2)](./File:Victor_70C.png.html) | | | Status | supported | | Source code | [serial-dmm](http://github.com/OpenTraceLab/?p=OpenTraceCapture.git;a=tree;f=src/hardware/serial-dmm) | | Counts | 6000 | | IEC 61010-1 | CAT II | | Connectivity | USB (standard cable) | | Measurements | voltage, current, resistance, continuity, diode, capacitance, frequency, temperature | | Features | max/min, data hold, relative, backlight | | Website | [china-victor.com](http://www.china-victor.com/english/en/product_data.aspx?ClassID=168&ID=121) | **Victor 70C** The **Victor 70C** is a 6000 counts, CAT II handheld digital multimeter with USB connectivity. It is also sold as the [EZA EZ-735](http://github.com/mvneves/victor70c#victor70c-software-for-linux). See [Victor 70C/Info](Victor_70C/Info.html "Victor 70C/Info") for more details (such as **lsusb -v** output) about the device. 
## Contents 
\- [1 Hardware](Victor_70C.html#Hardware) \- [2 Photos](Victor_70C.html#Photos) \- [3 Protocol](Victor_70C.html#Protocol) \- [4 Resources](Victor_70C.html#Resources) 
## Hardware \- [Fortune Semiconductor FS9922-DMM4](http://www.ic-fortune.com/upload/Download/FS9922-DMM4-DS-11_EN.pdf) multimeter chip \- [NXP HEF4066BT](http://datasheet.octopart.com/HEF4066BT-Philips-datasheet-87533.pdf) quadruple bilateral switches \- [Microchip TC7660E](http://datasheet.octopart.com/TC7660EOA-Microchip-datasheet-1009.pdf) charge pump DC-to-DC voltage converter \- [Texas Instruments 27L2C](http://datasheet.octopart.com/TLC27L2CP-Texas-Instruments-datasheet-151061.pdf) precision dual op-amp \- Unknown USB interface chip (HID) Note: the USB/HID chip is *in the multimeter* (not in the USB cable/connector) for this device. The device is connected to the PC using a standard USB cable (without any internal logic/chip). ## Photos \- 
[![\1](../../assets/hardware/general/\2)](./File:Victor_70C.jpg.html)
Device, front
\- 
[![\1](../../assets/hardware/general/\2)](./File:Victor_70C_PCB_top.jpg.html)
PCB, front
\- 
[![\1](../../assets/hardware/general/\2)](./File:Victor_70C_PCB_bottom.jpg.html)
PCB, bottom
\- 
[![\1](../../assets/hardware/general/\2)](./File:Victor_70C_LCD_controller.jpg.html)
DMM/LCD chip
\- 
[![\1](../../assets/hardware/general/\2)](./File:Victor_70C_HEF4066BT.jpg.html)
NXP HEF4066BT
\- 
[![\1](../../assets/hardware/general/\2)](./File:Victor_70C_TC7660E.jpg.html)
Microchip TC7660E
\- 
[![\1](../../assets/hardware/general/\2)](./File:Victor_70C_27L2C.jpg.html)
TI 27L2C
\- 
[![\1](../../assets/hardware/general/\2)](./File:Victor_70C_LCD.jpg.html)
LCD
## Protocol See [Victor protocol](Victor_protocol.html "Victor protocol"). ## Resources \- [RoastLogger: Input Devices](https://web.archive.org/web/20160527152655/http://homepage.ntlworld.com/green_bean/coffee/roastlogger/dmmdetails.html) (Victor Victor 86B/86C support) \- [Dave Ansell Science Communication: Victor 86C multimeter USB encoding for linux](http://www.daveansell.co.uk/?q=node/44) (PHP) \- [victor86b-usb-interface: USB interface for Victor 86B Digital Multimeter using HIDAPI](https://web.archive.org/web/20170104171210/https://code.google.com/archive/p/victor86b-usb-interface/) (see also [here](http://www.codeproject.com/Articles/310547/USB-Digital-Multimeter-Driver-using-HIDAPI)) \- [Github: victor70c](https://github.com/mvneves/victor70c) (HIDAPI) \- [Random review / photos](http://translate.google.com/translate?hl=de&sl=zh-CN&tl=en&u=http%3A%2F%2Fmytes.blog.163.com%2Fblog%2Fstatic%2F24568310201163010029970%2F)
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=Victor_70C&oldid=14306](https://OpenTraceLab.org/w/index.php?title=Victor_70C&oldid=14306)" 
[Categories](specialcategories-specialcategories.md): \- [Device](./Category:Device.html "Category:Device") \- [Multimeter](./Category:Multimeter.html "Category:Multimeter") \- [Supported](./Category:Supported.html "Category:Supported")

## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
