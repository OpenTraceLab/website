# Mastech Ms2115B
| | | |:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------------------:| | [*Image: \1* | | | Status | supported | | Source code | [serial-dmm](http://github.com/OpenTraceLab/?p=OpenTraceCapture.git;a=tree;f=src/hardware/serial-dmm) | | Counts | 6000 | | IEC 61010-1 | CAT III (1000V) / CAT IV (600V) | | Connectivity | USB/serial | | Measurements | voltage, current, resistance, capacitance, frequency, duty cycle, diode, continuity | | Features | autorange, true-rms, data hold, min/max, relative, inrush, bargraph, backlight, ncv | | Website | [mastech-group.com](http://www.mastech-group.com/products.php?cate=97) | **MASTECH MS2115B** The **MASTECH MS2115B** is a 6000 counts, CAT III (1000V) / CAT IV (600V) handheld dual display digital AC/DC clamp meter with USB connectivity. See *MASTECH MS2115B/Info* for more details (such as **lsusb -v** output) about the device.
## Contents
\- *1 Hardware* \- *2 Photos* \- *3 Protocol* \- *4 Resources*
## Hardware \- Silicon Labs CP2102 USB to UART bridge controller ([datasheet](https://www.silabs.com/documents/public/data-sheets/CP2102-9.pdf)) \- Cyrustek ES51970 DMM analog front end with inrush ([datasheet](http://www.cyrustek.com.tw/spec/ES51970.pdf)) ## Photos \-
[*Image: \1*
Device, front
\-
[*Image: \1*
Device, back
\-
[*Image: \1*
USB interface
**Another device:** \-
[*Image: \1*
Package, top
\-
[*Image: \1*
Package, bottom
\-
[*Image: \1*
Package, contents
\-
[*Image: \1*
Device, top
\-
[*Image: \1*
Device, bottom
## Protocol The chip periodically sends 9-byte packets at 1200 baud, 8n1. There is no checksum or CRC in the packet. [ms2115b.c](https://github.com/miek/OpenTraceCapture/blob/master/src/dmm/ms2115b.c) ## Resources \- [YouTube: FLR: Mastech MS2115B review](https://www.youtube.com/watch?v=0wLex6KQO04) \- [YouTube: DIY Tech & Repairs: Mastech MS2115A - Quick look](https://www.youtube.com/watch?v=g3WnYct1h8Q)
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=MASTECH_MS2115B&oldid=16438](https://OpenTraceLab.org/w/index.php?title=MASTECH_MS2115B&oldid=16438)"
: \- *Device* \- *Multimeter* \- *Supported*
## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
