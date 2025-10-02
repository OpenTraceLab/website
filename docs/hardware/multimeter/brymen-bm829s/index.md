---
title: Brymen BM829s
---

# Brymen BM829s

<div class="infobox" markdown>

![Brymen BM829s](./img/Bm829s-display-segments.jpg){ .infobox-image }

### Brymen BM829s

| | |
|---|---|
| **Status** | supported |
| **Source code** | [serial-dmm](https://github.com/OpenTraceLab/OpenTraceCapture/tree/main/src/hardware/serial-dmm) |
| **Counts** | 10000 |
| **IEC 61010-1** | CAT IV (1000V) |
| **Connectivity** | USB |
| **Measurements** | voltage, current, resistance, capacitance, diode, continuity, conductivity, frequency, duty cycle, power, temperature |
| **Features** | autorange, data hold, crest, backlight, true-RMS, NCV EF |
| **Website** | [brymen.com](http://brymen.com/product-html/PD02BM820s_829s.html) |

</div>

The **Brymen BM829s** is a 10000 counts, dual display, CAT IV (1000V), handheld digital multimeter with USB connectivity. See the [ BU-86x adapter](https://sigrok.org/wiki/Device_cables#Brymen_BU-86X).

## Photos

<div class="photo-grid" markdown>

[![Bm829s Display Segments](./img/Bm829s-display-segments.jpg)](./img/Bm829s-display-segments.png "Bm829s Display Segments"){ .glightbox data-gallery="brymen-bm829s" }
<span class="caption">Bm829s Display Segments</span>

[![Bm829s Box Front](./img/Bm829s-box-front.jpg)](./img/Bm829s-box-front.png "Bm829s Box Front"){ .glightbox data-gallery="brymen-bm829s" }
<span class="caption">Bm829s Box Front</span>

[![Bm829s Manual](./img/Bm829s-manual.jpg)](./img/Bm829s-manual.png "Bm829s Manual"){ .glightbox data-gallery="brymen-bm829s" }
<span class="caption">Bm829s Manual</span>

[![Bm829s Mugshot](./img/Bm829s-mugshot.jpg)](./img/Bm829s-mugshot.png "Bm829s Mugshot"){ .glightbox data-gallery="brymen-bm829s" }
<span class="caption">Bm829s Mugshot</span>

</div>
## Protocol

One outgoing HID report initiates the transmission of another reading (think serial-dmm packet request). The reading is received in three incoming HID reports. The 24 bytes of payload data carry bitmaps for LCD segments. The vendor provides the protocol description in the download area.

## Resources
- vendor's [BM829s product page](http://brymen.com/product-html/PD02BM820s_829s.html) and [family page](http://brymen.com/product-html/Products2-1.html)
- vendor's [BM820s download page](http://brymen.com/product-html/PD02BM820s_protocolDL.html) and [BM820s protocol documentation](http://brymen.com/product-html/images/DownloadList/ProtocolList/BM820-BM820s_List/BM820-BM820s-10000count-professional-dual-display-DMMs-protocol.pdf)

