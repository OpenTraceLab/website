# Mastech Ms2115B

| | | |:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------------------:| | [![\1](../../assets/hardware/general/\2)](./File:Mastech_ms2115b_mugshot.png.html) | | | Status | supported | | Source code | [serial-dmm](http://github.com/OpenTraceLab/?p=OpenTraceCapture.git;a=tree;f=src/hardware/serial-dmm) | | Counts | 6000 | | IEC 61010-1 | CAT III (1000V) / CAT IV (600V) | | Connectivity | USB/serial | | Measurements | voltage, current, resistance, capacitance, frequency, duty cycle, diode, continuity | | Features | autorange, true-rms, data hold, min/max, relative, inrush, bargraph, backlight, ncv | | Website | [mastech-group.com](http://www.mastech-group.com/products.php?cate=97) | **MASTECH MS2115B** The **MASTECH MS2115B** is a 6000 counts, CAT III (1000V) / CAT IV (600V) handheld dual display digital AC/DC clamp meter with USB connectivity. See [MASTECH MS2115B/Info](MASTECH_MS2115B/Info.html "MASTECH MS2115B/Info") for more details (such as **lsusb -v** output) about the device. 
## Contents 
\- [1 Hardware](MASTECH_MS2115B.html#Hardware) \- [2 Photos](MASTECH_MS2115B.html#Photos) \- [3 Protocol](MASTECH_MS2115B.html#Protocol) \- [4 Resources](MASTECH_MS2115B.html#Resources) 
## Hardware \- Silicon Labs CP2102 USB to UART bridge controller ([datasheet](https://www.silabs.com/documents/public/data-sheets/CP2102-9.pdf)) \- Cyrustek ES51970 DMM analog front end with inrush ([datasheet](http://www.cyrustek.com.tw/spec/ES51970.pdf)) ## Photos \- 
[![\1](../../assets/hardware/general/\2)](./File:Ms2115b_front.jpg.html)
Device, front
\- 
[![\1](../../assets/hardware/general/\2)](./File:Ms2115b_back.jpg.html)
Device, back
\- 
[![\1](../../assets/hardware/general/\2)](./File:Ms2115b_usb_port.jpg.html)
USB interface
**Another device:** \- 
[![\1](../../assets/hardware/general/\2)](./File:Mastech_ms2115b_package_top.jpg.html)
Package, top
\- 
[![\1](../../assets/hardware/general/\2)](./File:Mastech_ms2115b_package_bottom.jpg.html)
Package, bottom
\- 
[![\1](../../assets/hardware/general/\2)](./File:Mastech_ms2115b_package_contents.jpg.html)
Package, contents
\- 
[![\1](../../assets/hardware/general/\2)](./File:Mastech_ms2115b_device_top.jpg.html)
Device, top
\- 
[![\1](../../assets/hardware/general/\2)](./File:Mastech_ms2115b_device_bottom.jpg.html)
Device, bottom
## Protocol The chip periodically sends 9-byte packets at 1200 baud, 8n1. There is no checksum or CRC in the packet. [ms2115b.c](https://github.com/miek/OpenTraceCapture/blob/master/src/dmm/ms2115b.c) ## Resources \- [YouTube: FLR: Mastech MS2115B review](https://www.youtube.com/watch?v=0wLex6KQO04) \- [YouTube: DIY Tech & Repairs: Mastech MS2115A - Quick look](https://www.youtube.com/watch?v=g3WnYct1h8Q)
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=MASTECH_MS2115B&oldid=16438](https://OpenTraceLab.org/w/index.php?title=MASTECH_MS2115B&oldid=16438)" 
[Categories](specialcategories-specialcategories.md): \- [Device](./Category:Device.html "Category:Device") \- [Multimeter](./Category:Multimeter.html "Category:Multimeter") \- [Supported](./Category:Supported.html "Category:Supported")

## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
