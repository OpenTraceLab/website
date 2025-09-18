# Brymen Bm829S

| | | |:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------------------:| | [![\1](../../assets/hardware/general/\2)](./File:Bm829s-mugshot.png.html) | | | Status | supported | | Source code | [serial-dmm](http://github.com/OpenTraceLab/?p=OpenTraceCapture.git;a=tree;f=src/hardware/serial-dmm) | | Counts | 10000 | | IEC 61010-1 | CAT IV (1000V) | | Connectivity | USB | | Measurements | voltage, current, resistance, capacitance, diode, continuity, conductivity, frequency, duty cycle, power, temperature | | Features | autorange, data hold, crest, backlight, true-RMS, NCV EF | | Website | [brymen.com](http://brymen.com/product-html/PD02BM820s_829s.html) | **Brymen BM829s** The **Brymen BM829s** is a 10000 counts, dual display, CAT IV (1000V), handheld digital multimeter with USB connectivity. See the [BU-86x adapter](Device_cables.html#Brymen_BU-86X "Device cables"). ## Photos \- 
[![\1](../../assets/hardware/general/\2)](./File:Bm829s-mugshot.png.html)
DMM front
\- 
[![\1](../../assets/hardware/general/\2)](./File:Bm829s-box-front.png.html)
Box
\- 
[![\1](../../assets/hardware/general/\2)](./File:Bm829s-manual.png.html)
Manual
\- 
[![\1](../../assets/hardware/general/\2)](./File:Bm829s-display-segments.png.html)
Display segments
**Cable:** See [BU-86x](Device_cables.html#Brymen_BU-86X "Device cables") (USB HID). The user manual references a "BU-82x" which may or may not be a typo. The OpenTraceLab support was tested with a BU-86x cable. ## Protocol One outgoing HID report initiates the transmission of another reading (think serial-dmm packet request). The reading is received in three incoming HID reports. The 24 bytes of payload data carry bitmaps for LCD segments. The vendor provides the protocol description in the download area. ## Resources \- vendor's [BM829s product page](http://brymen.com/product-html/PD02BM820s_829s.html) and [family page](http://brymen.com/product-html/Products2-1.html) \- vendor's [BM820s download page](http://brymen.com/product-html/PD02BM820s_protocolDL.html) and [BM820s protocol documentation](http://brymen.com/product-html/images/DownloadList/ProtocolList/BM820-BM820s_List/BM820-BM820s-10000count-professional-dual-display-DMMs-protocol.pdf)
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=Brymen_BM829s&oldid=15614](https://OpenTraceLab.org/w/index.php?title=Brymen_BM829s&oldid=15614)" 
[Categories](specialcategories-specialcategories.md): \- [Device](./Category:Device.html "Category:Device") \- [Multimeter](./Category:Multimeter.html "Category:Multimeter") \- [Supported](./Category:Supported.html "Category:Supported")

## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
