# Brymen Bm857

| | | |:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:| | [![\1](../../assets/hardware/general/\2)](./File:Bm_857_mugshot_500000.png.html) | | | Status | supported | | Source code | [serial-dmm](http://github.com/OpenTraceLab/?p=OpenTraceCapture.git;a=tree;f=src/hardware/serial-dmm) | | Counts | 50000, 500000(DCV), 999999(Hz) | | IEC 61010-1 | CAT III (1000V) / CAT IV (600V) | | Connectivity | RS232 | | Measurements | voltage, frequency, diode, resistance, continuity, capacitance, current | | Features | autorange, data hold, crest, backlight, true-rms, dBm (selectable impedance), %4-20mA | | Website | brymen.com [BM857s](http://brymen.com/product-html/PD02BM850s_857s.html) [BM859s](http://brymen.com/product-html/PD02BM850s_859s.html) | **Brymen BM857** The **Brymen BM857** is a 50000 counts (500000 DC V), CAT III (1000V) / CAT IV (600V) handheld digital multimeter with RS232 connectivity. The **BM859s** is also supported, it uses the same protocol. Adapter kits ship with IR to RS232 cables, and include RS232 to USB converters. Higher end models support dual temperature sensors and difference mode, and the reference impedance for dBm measurements can be chosen in a range between 4 and 1200 Ohms. 
## Contents 
\- [1 Hardware](Brymen_BM857.html#Hardware) \- [2 Photos](Brymen_BM857.html#Photos) \- [3 BM850s series](Brymen_BM857.html#BM850s_series) \- [4 Protocol](Brymen_BM857.html#Protocol) \- [5 Resources](Brymen_BM857.html#Resources) 
## Hardware **Multimeter:** \- **Multimeter IC**: TBD \- **Precision +2.5V Voltage reference**: [Analog Devices REF43](http://www.analog.com/en/special-linear-functions/voltage-references/ref43/products/product.html) \- **True RMS-to-DC converter**: [Analog Devices AD737](http://www.analog.com/en/special-linear-functions/rms-to-dc-converters/ad737/products/product.html) \- **EEPROM(?)**: Chip marked S24C0. \- **Unidentified**: Several 062-JRC chips. These appear to be JFET opamps. \- **Unidentified**: Two QFP64 chips. \- TODO **Cable:** \- TODO \- See the [BRUA-85Xa kit](Device_cables.html#Brymen_BRUA-85Xa_kit "Device cables") and the [BC-85Xa adapter](Device_cables.html#Brymen_BC-85Xa "Device cables") \- See [User_talk:Mrnuke#BM857_PC_Interface_cable](./User_talk:Mrnuke.html#BM857_PC_Interface_cable "User talk:Mrnuke") ## Photos **Multimeter:** \- 
[![\1](../../assets/hardware/general/\2)](./File:Bm857_box_left.png.html)
Box
\- 
[![\1](../../assets/hardware/general/\2)](./File:Bm_857_mugshot_500000.png.html)
Mughsot
\- 
[![\1](../../assets/hardware/general/\2)](./File:Bm857_back.jpg.html)
Device, back
\- 
[![\1](../../assets/hardware/general/\2)](./File:Bm857_package_contents.jpg.html)
Package contents
\- 
[![\1](../../assets/hardware/general/\2)](./File:Bm857_cable_clips.jpg.html)
Probe cable storage clips
\- 
[![\1](../../assets/hardware/general/\2)](./File:Bm857_lcd_backlit.jpg.html)
LCD Backlight
\- 
[![\1](../../assets/hardware/general/\2)](./File:Bm857_front_noholster.png.html)
Holster removed, front
\- 
[![\1](../../assets/hardware/general/\2)](./File:Bm857_back_noholster.jpg.html)
Holster removed, back
\- 
[![\1](../../assets/hardware/general/\2)](./File:Bm857_opened.jpg.html)
Case opened
\- 
[![\1](../../assets/hardware/general/\2)](./File:Bm857_inside_backside.jpg.html)
Rear cover
\- 
[![\1](../../assets/hardware/general/\2)](./File:Bm857_cover_front.jpg.html)
Front cover
\- 
[![\1](../../assets/hardware/general/\2)](./File:Bm857_cover_back.jpg.html)
Rear cover, PCB removed
\- 
[![\1](../../assets/hardware/general/\2)](./File:Bm857_upperpcb_top.jpg.html)
Upper PCB, top
\- 
[![\1](../../assets/hardware/general/\2)](./File:Bm857_upperpcb_bottom.jpg.html)
Upper PCB, bottom
\- 
[![\1](../../assets/hardware/general/\2)](./File:Bm857_lowerpcb_top.jpg.html)
Main PCB, top
\- 
[![\1](../../assets/hardware/general/\2)](./File:Bm857_lowerpcb_bottom.jpg.html)
Main PCB, bottom
\- 
[![\1](../../assets/hardware/general/\2)](./File:Bm857_hv_slots.jpg.html)
High voltage isolation slots.
\- 
[![\1](../../assets/hardware/general/\2)](./File:Bm857_hv_walls.jpg.html)
High voltage isolation walls, designed to fit in the isolation slots.
\- 
[![\1](../../assets/hardware/general/\2)](./File:Bm857_input_circuit.jpg.html)
Input circuit near the V jack
\- 
[![\1](../../assets/hardware/general/\2)](./File:Bm857_mcu+lcdc.jpg.html)
Microcontroller (right), and LCD controller (left)
\- 
[![\1](../../assets/hardware/general/\2)](./File:Bm857_mcu+lcdc_2.jpg.html)
Microcontroller (right), and LCD controller (left)
\- 
[![\1](../../assets/hardware/general/\2)](./File:Bm857_lcdc.jpg.html)
LCD controller and connector
\- 
[![\1](../../assets/hardware/general/\2)](./File:Bm857_ICs.jpg.html)
ICs on the main PCB
\- 
[![\1](../../assets/hardware/general/\2)](./File:Bm857_ICs_2.jpg.html)
More ICs
**Cable:** This can use either the BC-85X or the BC-85X-1 cables. See [Device_cables#Brymen_BC-85X(-1)](Device_cables.html#Brymen_BC-85X(-1) "Device cables"). Currently, mrnuke is working on an improvised USB-to-infrared converter cable. See [User_talk:Mrnuke#BM857_PC_interface_cable](./User_talk:Mrnuke.html#BM857_PC_interface_cable "User talk:Mrnuke") for more details. Newer models (BM850a/BM850s) are said to require the BU-85Xa adapter. These different versions of meters and adapters are not compatible to each other.  \- 
[![\1](../../assets/hardware/general/\2)](./File:Brymen_br85x_dmm_hookup_all.jpg.html)
Cable hookup
\- 
[![\1](../../assets/hardware/general/\2)](./File:Brymen_br85x_dmm_hookup_side.jpg.html)
Cable hookup, detail
\- 
[![\1](../../assets/hardware/general/\2)](./File:Brymen_br85x_dmm_hookup_angle.jpg.html)
Cable hookup, closeup
\- 
[![\1](../../assets/hardware/general/\2)](./File:Brymen_br85x_dmm_hookup_top.jpg.html)
Cable hookup, top detail
## BM850s series The BM857s and BM859s meters (the BM850s series) uses the same protocol and works with the [BC-85Xa adapters](Device_cables.html#Brymen_BC-85Xa "Device cables").  \- 
[![\1](../../assets/hardware/general/\2)](./File:Bm859s-front-sleeve.png.html)
BM859s front with sleeve
\- 
[![\1](../../assets/hardware/general/\2)](./File:Bm859s-front.png.html)
BM859s front
\- 
[![\1](../../assets/hardware/general/\2)](./File:Bm859s-manual.png.html)
BM859s manual
\- 
[![\1](../../assets/hardware/general/\2)](./File:Bm859s-box-front.png.html)
BM859s box front
\- 
[![\1](../../assets/hardware/general/\2)](./File:Bm859s-display-segments.png.html)
BM859s display segments
## Protocol Serial communication (genuine COM port), textual presentation of measurement values (floating point, normalized mantissa plus exponent), combined with binary bit fields for current meter's function and thus measured unit, variable length records with control chars in the header/footer (DLE, STX/ETX) around the mode flags and value's text, up to 22 bytes per DMM packet. See resources below for a full description of the protocol.  ## Resources \- vendor's [BM810/BM830/BM850 page](http://brymen.com/product-html/Products2-2.html) which links to individual 857/859 devices \- vendor's [download area](http://brymen.com/product-html/PD02BM850s_protocolDL.html), [BM850 section](http://brymen.com/product-html/PD02BM850s_protocolDL.html), [BM850s protocol details](http://brymen.com/product-html/images/DownloadList/ProtocolList/BM850-BM850a-BM850s_List/BM850-BM850a-BM850s-500000-count-DMM-protocol-BC85X-BC85Xa.zip) (links have changed in the past, might too in the future) \- BM850/BM850a/BM850s protocol documentation [download area](http://brymen.com/product-html/PD02BM850s_protocolDL.html) and [ZIP with PDF](http://brymen.com/product-html/images/DownloadList/ProtocolList/BM850-BM850a-BM850s_List/BM850-BM850a-BM850s-500000-count-DMM-protocol-BC85X-BC85Xa.zip) (worked as of 2019-06-10, vendor may change that) 
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=Brymen_BM857&oldid=15616](https://OpenTraceLab.org/w/index.php?title=Brymen_BM857&oldid=15616)" 
[Categories](specialcategories-specialcategories.md): \- [Device](./Category:Device.html "Category:Device") \- [Multimeter](./Category:Multimeter.html "Category:Multimeter") \- [Supported](./Category:Supported.html "Category:Supported")

## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
