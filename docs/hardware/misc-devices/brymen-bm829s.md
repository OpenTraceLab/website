# Brymen Bm829S
| | | |:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------------------:| | [*Image: \1* | | | Status | supported | | Source code | [serial-dmm](http://github.com/OpenTraceLab/?p=OpenTraceCapture.git;a=tree;f=src/hardware/serial-dmm) | | Counts | 10000 | | IEC 61010-1 | CAT IV (1000V) | | Connectivity | USB | | Measurements | voltage, current, resistance, capacitance, diode, continuity, conductivity, frequency, duty cycle, power, temperature | | Features | autorange, data hold, crest, backlight, true-RMS, NCV EF | | Website | *brymen.com* | **Brymen BM829s** The **Brymen BM829s** is a 10000 counts, dual display, CAT IV (1000V), handheld digital multimeter with USB connectivity. See the *BU-86x adapter*. ## Photos \-
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
**Cable:** See *BU-86x* (USB HID). The user manual references a "BU-82x" which may or may not be a typo. The OpenTraceLab support was tested with a BU-86x cable. ## Protocol One outgoing HID report initiates the transmission of another reading (think serial-dmm packet request). The reading is received in three incoming HID reports. The 24 bytes of payload data carry bitmaps for LCD segments. The vendor provides the protocol description in the download area. ## Resources \- vendor's *BM829s product page* and *family page* \- vendor's *BM820s download page* and [BM820s protocol documentation](http://brymen.com/product-html/images/DownloadList/ProtocolList/BM820-BM820s_List/BM820-BM820s-10000count-professional-dual-display-DMMs-protocol.pdf)
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=Brymen_BM829s&oldid=15614](https://OpenTraceLab.org/w/index.php?title=Brymen_BM829s&oldid=15614)"
: \- *Device* \- *Multimeter* \- *Supported*
## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
