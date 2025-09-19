# Brymen Bm525S
| | | |:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------------------:| | [*Image: \1* | | | Status | supported | | Source code | [serial-dmm](http://github.com/OpenTraceLab/?p=OpenTraceCapture.git;a=tree;f=src/hardware/serial-dmm) | | Counts | 10000 | | IEC 61010-1 | CAT IV (1000V) | | Connectivity | USB | | Measurements | voltage, current, resistance, capacitance, diode, continuity, conductivity, frequency, duty cycle, temperature | | Features | autorange, data hold, crest, backlight, true-RMS, logging meter | | Website | *brymen.com* | **Brymen BM525s** The **Brymen BM525s** is a 10000 counts, dual display, CAT IV (1000V), handheld logging digital multimeter with USB connectivity. See the *BU-86x adapter*. The DMM can record up to 87000 (single display) or 43500 (dual display) measurements in up to 999 "pages" (recording sessions, limited to one of the meter's functions) at a rate between 20/s and one every 600s. ## Photos \-
[*Image: \1*
DMM front
\-
[*Image: \1*
Box
\-
[*Image: \1*
Manual
\-
[*Image: \1*
Display segments
**Cable:** See *BU-86x* (USB HID). ## Protocol The vendor documents both protocols for live readings (referred to as "real-time download" RTD) as well as recordings (referred to as "memory data sets" xMD). Live readings require one HID report to request a measurement, and results in three HID reports of response data which carry 24 bytes of information. Payload consists of bitmaps for LCD segments, which naturally fit the serial-dmm implementation. Current mainline fully supports live readings in all the meter's functions. The protocol for recordings differs. One HID report (different from the RTD request) initiates the transmission of data, two other HID reports either advance to the next data chunk, or repeat the most recently communicated data chunk. These packets are referred to as HEAD, NEXT, and CURR requests, and result in four HID reports of response data, which carry 24 bytes of information, and a checksum. The response data forms an adjacent stream of header information, and all measurements of all recording sessions. There is no means of random access, the retrieval of a single recording session involves the communication of all previously recorded information. Reading out recordings is implemented but has not seen much testing. ## Resources \- vendor's *BM525s product page* and *family page* \- vendor's *BM520s download page* and [BM520s protocol documentation](http://brymen.com/product-html/images/DownloadList/ProtocolList/BM520-BM520s_List/BM520-BM520s-10000-count-professional-dual-display-mobile-logging-DMMs-protocol.zip)
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=Brymen_BM525s&oldid=15613](https://OpenTraceLab.org/w/index.php?title=Brymen_BM525s&oldid=15613)"
: \- *Device* \- *Multimeter* \- *Supported*
## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
