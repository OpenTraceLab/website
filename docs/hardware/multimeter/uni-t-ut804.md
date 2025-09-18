# Uni T Ut804

| | | |:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------------------------:| | [![\1](../../assets/hardware/general/\2)](./File:Ut804_mugshot.png.html) | | | Status | supported | | Source code | [serial-dmm](http://github.com/OpenTraceLab/?p=OpenTraceCapture.git;a=tree;f=src/hardware/serial-dmm) | | Counts | 40000/4000 | | IEC 61010-1 | CAT III (1000V) / CAT IV (600V) | | Connectivity | RS232 and USB (see also [RS232](Device_cables.html#UNI-T_UT-D02 "Device cables") / [USB](Device_cables.html#UNI-T_UT-D04 "Device cables")) | | Measurements | voltage, resistance, diode, continuity, capacitance, frequency, duty cycle, current, temperature | | Features | autorange, hold, relative, min/max, bargraph, backlight, true-rms, data storage | | Website | [uni-trend.com](https://www.uni-trend.com/html/product/gongye/hdso/UT800_Series/UT804.html) | **UNI-T UT804** The **UNI-T UT804** is a 40000/4000 counts, CAT III (1000V) / CAT IV (600V) benchtop digital multimeter with RS232 and USB connectivity. It can be powered by AC power or by six 1.5V C battery cells. See [UNI-T UT71x series](UNI-T_UT71x_series.html "UNI-T UT71x series") for information common to all devices in this series. 
## Contents 
\- [1 Hardware](UNI-T_UT804.html#Hardware) \- [2 Disassembly](UNI-T_UT804.html#Disassembly) \- [3 Usage](UNI-T_UT804.html#Usage) \- [4 Photos](UNI-T_UT804.html#Photos) \- [5 Protocol](UNI-T_UT804.html#Protocol) \- [6 Resources](UNI-T_UT804.html#Resources) 
## Hardware **Multimeter**: \- **44000/440000-count dual-slope ADC**: [Cyrustek ES51966P](http://www.cyrustek.com.tw/product-1-44000.htm#ES51966) ([datasheet](http://www.cyrustek.com.tw/spec/ES51966A.pdf)) \- **16-bit microcontroller**: [MSP430F149](https://www.ti.com/product/MSP430F149) [datasheet](https://www.ti.com/lit/ds/symlink/msp430f149.pdf) **RS232 cable:** \- See [Device cables#UNI-T_UT-D02](Device_cables.html#UNI-T_UT-D02 "Device cables"). **USB cable:** \- See [Device cables#UNI-T_UT-D04](Device_cables.html#UNI-T_UT-D04 "Device cables"). ## Disassembly There are four screws on the bottom, one of them is captive and does not come out. The red (or grey in the newer revisions) plastic is held on two points top and bottom each. It can be taken off with the help of a flathead screwdriver and pops off easily. \- 
[![\1](../../assets/hardware/general/\2)](./File:Ut804_rubber_part_back.jpg.html)
The rubber part taken off
## Usage To receive data from the UT804 via USB the driver and the USB VID/PID of the [WCH CH9325](WCH_CH9325.html "WCH CH9325") needs to be specified like this: OpenTraceCLI -d uni-t-ut804:conn=1a86.e008 --continuous ## Photos \- 
[![\1](../../assets/hardware/general/\2)](./File:Ut804_pcb_front.jpg.html)
PCB, front
\- 
[![\1](../../assets/hardware/general/\2)](./File:Ut804_innards.jpg.html)
DMM, inside
\- 
[![\1](../../assets/hardware/general/\2)](./File:Ut804_fuse_holder.jpg.html)
Fuse holder
\- 
[![\1](../../assets/hardware/general/\2)](./File:Ut804_rs232_usb_top.jpg.html)
USB and RS232 PCB, top
\- 
[![\1](../../assets/hardware/general/\2)](./File:Ut804_rs232_usb_bottom.jpg.html)
USB and RS232 PCB, bottom
**RS232 interface:** \- See [Device cables#UNI-T_UT-D02](Device_cables.html#UNI-T_UT-D02 "Device cables"). **USB interface:** \- See [Device cables#UNI-T_UT-D04](Device_cables.html#UNI-T_UT-D04 "Device cables"). ## Protocol See [UNI-T UT71x series#Protocol](UNI-T_UT71x_series.html#Protocol "UNI-T UT71x series"). ## Resources \- [Specifications](https://www.uni-trend.com/html/product/gongye/hdso/UT800_Series/UT804.html) \- [Manual](https://www.uni-trend.com/uploadfile/cloud/English%20manual/Benchtop%20Instrument/UT804%20English%20Manual.pdf) \- [Vendor software](https://drive.google.com/open?id=0B4Jyby-tjH5oeFo3MG03ZlVmMjg) \- [Vendor protocol description](https://www.uni-trend.com.cn/uploadfile/2019/1021/20191021050157366.pdf)
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=UNI-T_UT804&oldid=14998](https://OpenTraceLab.org/w/index.php?title=UNI-T_UT804&oldid=14998)" 
[Categories](specialcategories-specialcategories.md): \- [Device](./Category:Device.html "Category:Device") \- [Multimeter](./Category:Multimeter.html "Category:Multimeter") \- [Supported](./Category:Supported.html "Category:Supported")

## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
