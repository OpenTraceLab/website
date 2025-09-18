# Uni T Ut61D

| | | |:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------------------:| | [![\1](../../assets/hardware/general/\2)](./File:Uni_t_ut61d_device.png.html) | | | Status | supported | | Source code | [uni-t-dmm](http://github.com/OpenTraceLab/?p=OpenTraceCapture.git;a=tree;f=src/hardware/uni-t-dmm) | | Counts | 6000 | | IEC 61010-1 | CAT II (600V) / CAT III (300V) | | Connectivity | [RS232](Device_cables.html#UNI-T_UT-D02 "Device cables") / [USB](Device_cables.html#UNI-T_UT-D04 "Device cables") | | Measurements | voltage, current, resistance, capacitance, frequency, duty cycle, diode, continuity | | Features | autorange, true-rms, data hold, min/max, rel, bargraph, backlight | | Website | [uni-trend.com](http://www.uni-trend.com/UT61D.html) | **UNI-T UT61D** The **UNI-T UT61D** is a 6000 counts, CAT II (600V) / CAT III (300V) handheld digital multimeter with RS232 or USB connectivity. See [UNI-T UT61D/Info](UNI-T_UT61D/Info.html "UNI-T UT61D/Info") for more details (such as **lsusb -v** output) about the device. 
## Contents 
\- [1 Hardware](UNI-T_UT61D.html#Hardware) \- [2 Photos](UNI-T_UT61D.html#Photos) \- [3 Protocol](UNI-T_UT61D.html#Protocol) \- [4 Resources](UNI-T_UT61D.html#Resources) 
## Hardware **Multimeter**: \- **Multimeter IC**: [Fortune Semiconductor FS9922-DMM4](Multimeter_ICs.html#Fortune_Semiconductor_FS9922-DMM4 "Multimeter ICs") ([datasheet](http://www.ic-fortune.com/upload/Download/FS9922-DMM4-DS-11_EN.pdf)) \- **Low-power True RMS-to-DC converter**: [Analog Devices AD737](http://www.analog.com/en/special-linear-functions/rms-to-dc-converters/ad737/products/product.html) ([datasheet](http://www.analog.com/static/imported-files/data_sheets/AD737.pdf)) \- **Crystal**: 4MHz (markings: "ROSON 3.999FSHN") \- **Fuses**: 10A/240V and 1A/240V (HRV fuses) **RS232 cable**: See [Device cables#UNI-T_UT-D02](Device_cables.html#UNI-T_UT-D02 "Device cables"). **USB cable**: See [Device cables#UNI-T_UT-D04](Device_cables.html#UNI-T_UT-D04 "Device cables"). ## Photos **Multimeter**: \- 
[![\1](../../assets/hardware/general/\2)](./File:Uni-t_ut61d_package_contents.jpg.html)
Package contents
\- 
[![\1](../../assets/hardware/general/\2)](./File:Uni_t_ut61d_device.jpg.html)
Device, front
\- 
[![\1](../../assets/hardware/general/\2)](./File:Uni-t_ut61d_device_back.jpg.html)
Device, back
\- 
[![\1](../../assets/hardware/general/\2)](./File:Uni-t_ut61d_battery.jpg.html)
Battery
\- 
[![\1](../../assets/hardware/general/\2)](./File:Uni-t_ut61d_device_open1.jpg.html)
Device open 1
\- 
[![\1](../../assets/hardware/general/\2)](./File:Uni-t_ut61d_device_open2.jpg.html)
Device open 2
\- 
[![\1](../../assets/hardware/general/\2)](./File:Uni-t_ut61d_device_open3.jpg.html)
Device open 3
\- 
[![\1](../../assets/hardware/general/\2)](./File:Uni-t_ut61d_device_open4.jpg.html)
Device open 4
\- 
[![\1](../../assets/hardware/general/\2)](./File:Uni-t_ut61d_pcb_front.jpg.html)
PCB, front
\- 
[![\1](../../assets/hardware/general/\2)](./File:Uni-t_ut61d_pcb_back.jpg.html)
PCB, back
\- 
[![\1](../../assets/hardware/general/\2)](./File:Uni-t_ut61d_pcb_front_top.jpg.html)
PCB front, top
\- 
[![\1](../../assets/hardware/general/\2)](./File:Uni-t_ut61d_pcb_front_middle.jpg.html)
PCB front, middle
\- 
[![\1](../../assets/hardware/general/\2)](./File:Uni-t_ut61d_fs9922-dmm4.jpg.html)
FS9922-DMM4
\- 
[![\1](../../assets/hardware/general/\2)](./File:Uni-t_ut61d_ad737j.jpg.html)
AD737J
\- 
[![\1](../../assets/hardware/general/\2)](./File:Uni-t_ut61d_crystal.jpg.html)
Crystal
\- 
[![\1](../../assets/hardware/general/\2)](./File:Uni-t_ut61d_testadapter1.jpg.html)
Testadapter 1
\- 
[![\1](../../assets/hardware/general/\2)](./File:Uni-t_ut61d_testadapter2.jpg.html)
Testadapter 2
\- 
[![\1](../../assets/hardware/general/\2)](./File:Uni-t_ut61d_testadapter3.jpg.html)
Testadapter 3
\- 
[![\1](../../assets/hardware/general/\2)](./File:Uni-t_ut61d_lcd.jpg.html)
LCD
**RS232 cable**: See [Device cables#UNI-T_UT-D02](Device_cables.html#UNI-T_UT-D02 "Device cables"). **USB cable**: See [Device cables#UNI-T_UT-D04](Device_cables.html#UNI-T_UT-D04 "Device cables"). ## Protocol See [Multimeter_ICs#Fortune_Semiconductor_FS9922-DMM4](Multimeter_ICs.html#Fortune_Semiconductor_FS9922-DMM4 "Multimeter ICs") for the DMM IC protocol. Depending on the cable, additional transport-specific decoding is needed, though. ## Resources \- [Manual](http://www.uni-trend.com/manual2/UT61English.pdf) \- [Vendor software](http://www.uni-trend.com/Web%20site/DMM%20Software/UT61D%20setup.exe) \- [perhof: Uni-T UT61D for Linux](https://perhof.wordpress.com/category/computing/linux/) (also: [ut61d.zip](http://dl.dropbox.com/u/20603229/published/ut61d.zip)) 
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=UNI-T_UT61D&oldid=7949](https://OpenTraceLab.org/w/index.php?title=UNI-T_UT61D&oldid=7949)" 
[Categories](specialcategories-specialcategories.md): \- [Device](./Category:Device.html "Category:Device") \- [Multimeter](./Category:Multimeter.html "Category:Multimeter") \- [Supported](./Category:Supported.html "Category:Supported")

## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
