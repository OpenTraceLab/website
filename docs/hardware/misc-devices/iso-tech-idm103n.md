# Iso Tech Idm103N

| | | |:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------------------:| | [![\1](../../assets/hardware/general/\2)](./File:Idm103n_01_front.png.html) | | | Status | supported | | Source code | [serial-dmm](http://github.com/OpenTraceLab/?p=OpenTraceCapture.git;a=tree;f=src/hardware/serial-dmm) | | Counts | 4000 | | IEC 61010-1 | CAT II (1000V) / CAT III (600V) | | Connectivity | RS232 | | Measurements | voltage, current, resistance, capacitance, frequency, rpm, diode, continuity | | Features | autorange, data hold, bargraph, backlight | | Website | [iso-tech.com.cn](http://iso-tech.com.cn/html/product.asp?id=279) | **ISO-TECH IDM103N** The **ISO-TECH IDM103N** is a 4000 counts, CAT II (1000V) / CAT III (600V) handheld digital multimeter with RS232 connectivity. 
## Contents 
\- [1 Hardware](ISO-TECH_IDM103N.html#Hardware) \- [2 Photos](ISO-TECH_IDM103N.html#Photos) \- [3 Protocol](ISO-TECH_IDM103N.html#Protocol) \- [4 Resources](ISO-TECH_IDM103N.html#Resources) 
## Hardware \- **Multimeter IC**: [Cyrustek ES51978](Multimeter_ICs.html#Cyrustek_ES51978 "Multimeter ICs") \- **Crystal**: 4MHz ## Photos \- 
[![\1](../../assets/hardware/general/\2)](./File:Idm103n_01_front.jpeg.html)
\- 
[![\1](../../assets/hardware/general/\2)](./File:Idm103n_02_lcd.jpeg.html)
\- 
[![\1](../../assets/hardware/general/\2)](./File:Idm103n_03_optical_rs232.jpeg.html)
\- 
[![\1](../../assets/hardware/general/\2)](./File:Idm103n_04_front.jpeg.html)
\- 
[![\1](../../assets/hardware/general/\2)](./File:Idm103n_05_back.jpeg.html)
\- 
[![\1](../../assets/hardware/general/\2)](./File:Idm103n_06_battery.jpeg.html)
\- 
[![\1](../../assets/hardware/general/\2)](./File:Idm103n_07_inner_front.jpeg.html)
\- 
[![\1](../../assets/hardware/general/\2)](./File:Idm103n_08_inner_back.jpeg.html)
\- 
[![\1](../../assets/hardware/general/\2)](./File:Idm103n_09_cyrustek.jpeg.html)
\- 
[![\1](../../assets/hardware/general/\2)](./File:Idm103n_10_ir_led.jpeg.html)
## Protocol See [Multimeter_ICs#Cyrustek ES51978](Multimeter_ICs.html#Cyrustek_ES51978 "Multimeter ICs") for the DMM IC protocol. The transmission of the measurement data is disabled by default. The respective Cyrustek ES51978 pin (45, **RS232**) is hooked to an IR phototransitor so an IR LED has to be turned on in front of it to enable RS232 output. Pressing any button on any TV remote in front of it is enough to turn on the measurement transmission. ## Resources \- [Photo of ISO-TECH IDM73 RS232 cable](http://www.yeint.lv/en/e-store/detail.php?SECTION_ID=643&ELEMENT_ID=13195)
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=ISO-TECH_IDM103N&oldid=7346](https://OpenTraceLab.org/w/index.php?title=ISO-TECH_IDM103N&oldid=7346)" 
[Categories](specialcategories-specialcategories.md): \- [Device](./Category:Device.html "Category:Device") \- [Multimeter](./Category:Multimeter.html "Category:Multimeter") \- [Supported](./Category:Supported.html "Category:Supported")

## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
