# Brymen Bm869

| | | |:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------------------:| | [![\1](../../assets/hardware/general/\2)](./File:Bm869_mugshot.png.html) | | | Status | supported | | Source code | [serial-dmm](http://github.com/OpenTraceLab/?p=OpenTraceCapture.git;a=tree;f=src/hardware/serial-dmm) | | Counts | 50000, 500000(DCV), 99999(Hz) | | IEC 61010-1 | CAT IV (1000V) | | Connectivity | Infrared (USB) | | Measurements | voltage, current, frequency, duty cycle, resistance, continuity, conductance, diode, capacitance, temperature | | Features | autorange, data hold, min/max/avg, crest, backlight, true-rms, dBm, %4-20mA, VFD | | Website | [brymen.com](http://brymen.com/product-html/cata860/Bm860s.htm) | **Brymen BM869** The **Brymen BM869** is a 50000 counts (500000 DC), CAT IV (1000V) dual display handheld digital multimeter with USB connectivity. The **BM869s** is also supported, it uses the same cable and protocol. 
## Contents 
\- [1 Hardware](Brymen_BM869.html#Hardware) \- [2 Photos](Brymen_BM869.html#Photos) \- [3 Protocol](Brymen_BM869.html#Protocol) \- [4 Resources](Brymen_BM869.html#Resources) 
## Hardware **Multimeter:** \- **Multimeter IC**: BTC AD-85-4 (hidden under metal shielding) \- **Precision +2.5V Voltage reference**: [Analog Devices REF43](http://www.analog.com/en/special-linear-functions/voltage-references/ref43/products/product.html) \- **True RMS-to-DC converter**: [Analog Devices AD636](http://www.analog.com/en/special-linear-functions/rms-to-dc-converters/ad636/products/product.html) \- **4 Kb EEPROM**: [Seiko S-24CS04A](http://datasheet.octopart.com/S-24CS04AFJ-TB-G-Seiko-datasheet-13119882.pdf). \- **J-FET input op-amp**: Three [NMJ062](http://semicon.njr.co.jp/eng/product/opamp/NJM062.html) chips marked 062-JRC. \- **Rail-to-Rail op-amp**: Two [Microchip MCP6021](http://www.microchip.com/wwwproducts/Devices.aspx?product=MCP6021) probably dedicated to the two temperature sensors. **Cable:** The Brymen BC-86X cable is designed to be used with the Brymen BM867 and BM869. See [Device_cables#Brymen_BU-86X](Device_cables.html#Brymen_BU-86X "Device cables"). ## Photos **Multimeter:** \- 
[![\1](../../assets/hardware/general/\2)](./File:Bm869_01_unboxing.jpeg.html)
Unboxing
\- 
[![\1](../../assets/hardware/general/\2)](./File:Bm869_02_front.jpeg.html)
Mughsot
\- 
[![\1](../../assets/hardware/general/\2)](./File:Bm869_03_back.jpeg.html)
Device back
\- 
[![\1](../../assets/hardware/general/\2)](./File:Bm869_04_front_no_bumper.jpeg.html)
Holster removed, front
\- 
[![\1](../../assets/hardware/general/\2)](./File:Bm869_05_back_no_bumper.jpeg.html)
Holster removed, back
\- 
[![\1](../../assets/hardware/general/\2)](./File:Bm869_06_battery.jpeg.html)
Battery compartment
\- 
[![\1](../../assets/hardware/general/\2)](./File:Bm869_07_front_pcb.jpeg.html)
Opened, PCB top
\- 
[![\1](../../assets/hardware/general/\2)](./File:Bm869_08_back_pcb.jpeg.html)
Opened, PCB bottom
\- 
[![\1](../../assets/hardware/general/\2)](./File:Bm869_09_inside_pcb.jpeg.html)
Separated PCB
\- 
[![\1](../../assets/hardware/general/\2)](./File:Bm869_10_zoom_pcb.jpeg.html)
PCB details
\- 
[![\1](../../assets/hardware/general/\2)](./File:Bm869_11_lcd_segments.jpeg.html)
LCD segments
\- 
[![\1](../../assets/hardware/general/\2)](./File:Bm869_12_backlight.jpeg.html)
LCD Backlight
**Cable:** \- 
[![\1](../../assets/hardware/general/\2)](./File:Bm869_13_plugged.jpeg.html)
Cable hookup
\- 
[![\1](../../assets/hardware/general/\2)](./File:Bm869_14_plugged_details.jpeg.html)
Cable hookup, closeup
## Protocol The Brymen vendor describes the protocol in PDF documents which reside in the product's download section. There are instructions for both the USB (HID) communication as well as the layout of packets whose data bytes communicate measurement results. Individual bits represent LCD segments for digits including signs, and other indicators. Which is a common approach for other multimeter chipsets, too. Several document names were observed over time (500000count-professional-dual-display-DMMs-protocol.pdf, BM860-BM860s-500000-count-dual-display-DMMs-protocol.pdf). Download links kept changing their paths. They either referenced PDF files directly or ZIP files which contained PDF files. Software installations could also contain protocol descriptions, or protocol documentation was available for individual download. It's probably best to just start at the vendor's site and manually navigate the download area. ## Resources \- [Manual](http://www.brymen.com/PD02BM860s_usersmanualDL.html) \- [Brymen protocol description and software](http://www.brymen.com/PD02BM860s_softwareDL.html) (as of 2021-05-17) \- [Brymen raw IR protocol reverse engineering and home made cable](http://www.eevblog.com/forum/testgear/brymen-ir-connection-protocol-anyone-sniffed-it-yet/) (EEVBlog forum) 
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=Brymen_BM869&oldid=16114](https://OpenTraceLab.org/w/index.php?title=Brymen_BM869&oldid=16114)" 
[Categories](specialcategories-specialcategories.md): \- [Device](./Category:Device.html "Category:Device") \- [Multimeter](./Category:Multimeter.html "Category:Multimeter") \- [Supported](./Category:Supported.html "Category:Supported")

## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
