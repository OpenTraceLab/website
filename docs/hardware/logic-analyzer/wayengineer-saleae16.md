# Wayengineer Saleae16

**WayEngineer Saleae16** [![\1](../../assets/hardware/general/\2)](./File:Wayengineer_saleae16.png.html) |   
---|---  
Status | supported  
Source code | [saleae-logic16](http://github.com/OpenTraceLab/?p=OpenTraceCapture.git;a=tree;f=src/hardware/saleae-logic16)  
Channels | 3/6/9/16  
Samplerate | 100/50/32/16MHz  
Samplerate (state) | —  
Triggers | none (SW-only)  
Min/max voltage | -0.9V — 6V  
Threshold voltage | configurable:  
for 1.8V to 3.6V systems: VIH=1.4V, VIL=0.7V  
for 5V systems: VIH=3.6V, VIL=1.4V  
Memory | none  
Compression | yes  
Website | [wayengineer.com](https://web.archive.org/web/20161229025314/http://www.wayengineer.com/index.php?main_page=product_info&products_id=4747)  
**WayEngineer Saleae16** The **WayEngineer Saleae16** is a USB-based, 16-channel logic analyzer with 100/50/32/16MHz sampling rate (at 3/6/9/16 enabled channels). This is a clone of the [Saleae Logic16](Saleae_Logic16.html "Saleae Logic16"). See [WayEngineer Saleae16/Info](WayEngineer_Saleae16/Info.html "WayEngineer Saleae16/Info") for more details (such as **lsusb -v** output) about the device. 
## Contents 
\- [1 Hardware](WayEngineer_Saleae16.html#Hardware) \- [2 Photos](WayEngineer_Saleae16.html#Photos) \- [3 Firmware](WayEngineer_Saleae16.html#Firmware) \- [4 Protocol](WayEngineer_Saleae16.html#Protocol) \- [5 Resources](WayEngineer_Saleae16.html#Resources) 
## Hardware \- **FPGA**: [Xilinx Spartan-3A XC3S200A](http://www.xilinx.com/support/index.html/content/xilinx/en/supportNav/silicon_devices/fpga/spartan-3a.html), 200K gates ([datasheeet](http://www.xilinx.com/support/documentation/data_sheets/ds529.pdf)) \- **USB interface chip**: [Cypress CY7C68013A-56LTXC (FX2LP)](http://www.cypress.com/?mpn=CY7C68013A-56LTXC) ([datasheet](http://www.cypress.com/?docID=45142)) \- **I²C EEPROM**: [Atmel 24C02N](http://www.atmel.com/devices/at24c02.aspx) (markings: "ATMEL142 24C02N SU27 D") ([datasheet](http://www.atmel.com/Images/doc3256.pdf)) \- **3.3V voltage regulator**: [Advanced Monolithic Systems AMS1117-3.3](http://www.advanced-monolithic.com/products/voltreg.html#1117) ([datasheet](http://ams-semitech.com/attachments/File/AMS1117_20120314.pdf), [older datasheet](http://www.advanced-monolithic.com/pdf/ds1117.pdf)) \- **1.2V voltage regulator**: [Advanced Monolithic Systems AMS1117-1.2](http://www.advanced-monolithic.com/products/voltreg.html#1117) ([datasheet](http://ams-semitech.com/attachments/File/AMS1117_20120314.pdf), [older datasheet](http://www.advanced-monolithic.com/pdf/ds1117.pdf)) \- **Crystal:** 24.000 ## Photos \- 
[![\1](../../assets/hardware/general/\2)](./File:Wayengineer_saleae16_package_contents.jpg.html)
Package contents
\- 
[![\1](../../assets/hardware/general/\2)](./File:Wayengineer_saleae16_device_with_cable.jpg.html)
Device with cable
\- 
[![\1](../../assets/hardware/general/\2)](./File:Wayengineer_saleae16_device_top.jpg.html)
Device, top
\- 
[![\1](../../assets/hardware/general/\2)](./File:Wayengineer_saleae16_device_bottom.jpg.html)
Device, bottom
\- 
[![\1](../../assets/hardware/general/\2)](./File:Wayengineer_saleae16_device_usb.jpg.html)
USB connector
\- 
[![\1](../../assets/hardware/general/\2)](./File:Wayengineer_saleae16_device_connector.jpg.html)
LA connector
\- 
[![\1](../../assets/hardware/general/\2)](./File:Wayengineer_saleae16_pcb_top.jpg.html)
PCB, top
\- 
[![\1](../../assets/hardware/general/\2)](./File:Wayengineer_saleae16_pcb_bottom.jpg.html)
PCB, bottom
\- 
[![\1](../../assets/hardware/general/\2)](./File:Wayengineer_saleae16_atmel_24c02n.jpg.html)
Atmel 24C02N
\- 
[![\1](../../assets/hardware/general/\2)](./File:Wayengineer_saleae16_ams1117_33.jpg.html)
AMS117 3.3V
\- 
[![\1](../../assets/hardware/general/\2)](./File:Wayengineer_saleae16_ams1117_12.jpg.html)
AMS117 1.2V
\- 
[![\1](../../assets/hardware/general/\2)](./File:Wayengineer_saleae16_input_stage.jpg.html)
Input stage
**Another device:** \- 
[![\1](../../assets/hardware/general/\2)](./File:WayEngineer16-board-top-2014-09.jpg.html)
PCB, top, without black coating (September 2014)
**Yet another device:** \- 
[![\1](../../assets/hardware/general/\2)](./File:Wayengineer_saleae16_FX2LP.jpg.html)
USB connector (of a Chinese version)
\- 
[![\1](../../assets/hardware/general/\2)](./File:Wayengineer_saleae16_XC3S200A.jpg.html)
FPGA (of a Chinese version)
## Firmware See [Saleae_Logic16#Firmware](Saleae_Logic16.html#Firmware "Saleae Logic16"). ## Protocol See [Saleae_Logic16#Protocol](Saleae_Logic16.html#Protocol "Saleae Logic16"). ## Resources \- [AliExpress entry #1](http://www.aliexpress.com/item/1pcs-lot-Free-shipping-New-Arrival-Saleae-Logic16-saleae16-USB-Logic-Analyzer-100M-16CH-best-quality/667671473.html)
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=WayEngineer_Saleae16&oldid=14191](https://OpenTraceLab.org/w/index.php?title=WayEngineer_Saleae16&oldid=14191)" 
[Categories](specialcategories-specialcategories.md): \- [Device](./Category:Device.html "Category:Device") \- [Logic analyzer](./Category:Logic_analyzer.html "Category:Logic analyzer") \- [Supported](./Category:Supported.html "Category:Supported")

## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
