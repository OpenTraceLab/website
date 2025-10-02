---
title: MASTECH MS8250B
---

# MASTECH MS8250B

<div class="infobox" markdown>

![MASTECH MS8250B](./img/MASTECH_MS8250B.jpg){ .infobox-image }

### MASTECH MS8250B

| | |
|---|---|
| **Status** | supported |
| **Source code** | [serial-dmm](https://github.com/OpenTraceLab/OpenTraceCapture/tree/main/src/hardware/serial-dmm) |
| **Counts** | 4000 |
| **IEC 61010-1** | CAT IV (600V) |
| **Connectivity** | USB-to-serial |
| **Measurements** | voltage, current, resistance, capacitance, diode, continuity, frequency |
| **Features** | autorange, data hold, backlight, relative |
| **Website** | [p-mastech.com](http://www.p-mastech.com/index.php?page=shop.product_details&amp;flypage=flypage.tpl&amp;product_id=30&amp;category_id=3&amp;option=com_virtuemart&amp;Itemid=29&amp;vmcchk=1&amp;Itemid=29) |

</div>

The **MASTECH MS8250B** is a 4000 counts, CAT IV (600V) handheld digital multimeter with USB connectivity.

## Hardware
- **Main chip**: Fortune Semiconductor FS9721-LP3 (guessed from protocol)

## Photos

<div class="photo-grid" markdown>

[![Mastech Ms8250b](./img/MASTECH_MS8250B.jpg)](./img/MASTECH_MS8250B.jpg "Mastech Ms8250b"){ .glightbox data-gallery="mastech-ms8250b" }
<span class="caption">Mastech Ms8250b</span>

[![Mastech Ms8250b Mugshot](./img/Mastech_ms8250b_mugshot.jpg)](./img/Mastech_ms8250b_mugshot.png "Mastech Ms8250b Mugshot"){ .glightbox data-gallery="mastech-ms8250b" }
<span class="caption">Mastech Ms8250b Mugshot</span>

</div>
## Protocol

The protocol is the same as the one used in the Fortune Semiconductor FS9721 chip (likely because that chip is used in the DMM).

See [Multimeter_ICs#Fortune_Semiconductor_FS9721_LP3](https://sigrok.org/wiki/Multimeter_ICs#Fortune_Semiconductor_FS9721_LP3) for the DMM IC protocol.

## Resources
- [Specs](http://www.p-mastech.com/images/SPEC/ms8250a%20ms8250b%20ms8250d.jpg)
- [Manual](http://www.p-mastech.com/images/Manual/ms8250a%20ms8250b%20english%20manual.pdf)
- [Mastech parser tool](https://github.com/jlhonora/mastech-parser)

