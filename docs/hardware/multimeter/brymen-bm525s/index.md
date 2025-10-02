---
title: Brymen BM525s
---

# Brymen BM525s

<div class="infobox" markdown>

![Brymen BM525s](./img/Bm525s-manual.jpg){ .infobox-image }

### Brymen BM525s

| | |
|---|---|
| **Status** | supported |
| **Source code** | [serial-dmm](https://github.com/OpenTraceLab/OpenTraceCapture/tree/main/src/hardware/serial-dmm) |
| **Counts** | 10000 |
| **IEC 61010-1** | CAT IV (1000V) |
| **Connectivity** | USB |
| **Measurements** | voltage, current, resistance, capacitance, diode, continuity, conductivity, frequency, duty cycle, temperature |
| **Features** | autorange, data hold, crest, backlight, true-RMS, logging meter |
| **Website** | [brymen.com](http://brymen.com/product-html/PD02BM520s_525s.html) |

</div>

The **Brymen BM525s** is a 10000 counts, dual display, CAT IV (1000V), handheld logging digital multimeter with USB connectivity. See the [ BU-86x adapter](https://sigrok.org/wiki/Device_cables#Brymen_BU-86X).

The DMM can record up to 87000 (single display) or 43500 (dual display) measurements in up to 999 "pages" (recording sessions, limited to one of the meter's functions) at a rate between 20/s and one every 600s.

## Photos

<div class="photo-grid" markdown>

[![Bm525s Manual](./img/Bm525s-manual.jpg)](./img/Bm525s-manual.png "Bm525s Manual"){ .glightbox data-gallery="brymen-bm525s" }
<span class="caption">Bm525s Manual</span>

[![Bm525s Box Front](./img/Bm525s-box-front.jpg)](./img/Bm525s-box-front.png "Bm525s Box Front"){ .glightbox data-gallery="brymen-bm525s" }
<span class="caption">Bm525s Box Front</span>

[![Bm525s Display Segments](./img/Bm525s-display-segments.jpg)](./img/Bm525s-display-segments.png "Bm525s Display Segments"){ .glightbox data-gallery="brymen-bm525s" }
<span class="caption">Bm525s Display Segments</span>

[![Bm525s Mugshot](./img/Bm525s-mugshot.jpg)](./img/Bm525s-mugshot.png "Bm525s Mugshot"){ .glightbox data-gallery="brymen-bm525s" }
<span class="caption">Bm525s Mugshot</span>

</div>
## Protocol

The vendor documents both protocols for live readings (referred to as "real-time download" RTD) as well as recordings (referred to as "memory data sets" xMD).

Live readings require one HID report to request a measurement, and results in three HID reports of response data which carry 24 bytes of information. Payload consists of bitmaps for LCD segments, which naturally fit the serial-dmm implementation. Current mainline fully supports live readings in all the meter's functions.

The protocol for recordings differs. One HID report (different from the RTD request) initiates the transmission of data, two other HID reports either advance to the next data chunk, or repeat the most recently communicated data chunk. These packets are referred to as HEAD, NEXT, and CURR requests, and result in four HID reports of response data, which carry 24 bytes of information, and a checksum. The response data forms an adjacent stream of header information, and all measurements of all recording sessions. There is no means of random access, the retrieval of a single recording session involves the communication of all previously recorded information. Reading out recordings is implemented but has not seen much testing.

## Resources
- vendor's [BM525s product page](http://brymen.com/product-html/PD02BM520s_525s.html) and [family page](http://brymen.com/product-html/Products2-1.html)
- vendor's [BM520s download page](http://brymen.com/product-html/PD02BM520s_protocolDL.html) and [BM520s protocol documentation](http://brymen.com/product-html/images/DownloadList/ProtocolList/BM520-BM520s_List/BM520-BM520s-10000-count-professional-dual-display-mobile-logging-DMMs-protocol.zip)

