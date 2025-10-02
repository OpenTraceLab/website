---
title: MASTECH MS8250D
---

# MASTECH MS8250D

<div class="infobox" markdown>

![MASTECH MS8250D](./img/Mastech_ms8250d_mugshot.png){ .infobox-image }

### MASTECH MS8250D

| | |
|---|---|
| **Status** | supported |
| **Source code** | [serial-dmm](https://github.com/OpenTraceLab/OpenTraceCapture/tree/main/src/hardware/serial-dmm) |
| **Counts** | 6600 |
| **IEC 61010-1** | CAT III (1000V) / CAT IV (600V) |
| **Connectivity** | USB/serial |
| **Measurements** | voltage, current, resistance, capacitance, frequency, duty cycle, diode, continuity |
| **Features** | autorange, true-rms, data hold, min/max, relative, bargraph, backlight, ncv |
| **Website** | [mastech-group.com](http://www.mastech-group.com/products.php?cate=123&amp;PNo=142) |

</div>

The **MASTECH MS8250D** is a 6600 counts, CAT III (1000V) / CAT IV (600V) handheld digital multimeter with USB connectivity.

See [MASTECH MS8250D/Info](https://sigrok.org/wiki/MASTECH_MS8250D/Info) for more details (such as **lsusb -v** output) about the device.

## Hardware
- CP2102 USB to UART bridge controller
- HY11P14 embedded 18-Bit Σ∆ADC 8-Bit RISC-like mixed signal microcontroller ([datasheet](http://www.hycontek.com/wp-content/uploads/HY11P14_EN.pdf))
- DTA0660L multimeter chip
- ATMLH538 EEPROM

## Photos

<div class="photo-grid" markdown>

[![Mastech Ms8250d Mugshot](./img/Mastech_ms8250d_mugshot.png)](./img/Mastech_ms8250d_mugshot.png "Mastech Ms8250d Mugshot"){ .glightbox data-gallery="mastech-ms8250d" }
<span class="caption">Mastech Ms8250d Mugshot</span>

[![P1040388](./img/P1040388.jpg)](./img/P1040388.jpg "P1040388"){ .glightbox data-gallery="mastech-ms8250d" }
<span class="caption">P1040388</span>

[![P1040348](./img/P1040348.jpg)](./img/P1040348.jpg "P1040348"){ .glightbox data-gallery="mastech-ms8250d" }
<span class="caption">P1040348</span>

[![P1040378](./img/P1040378.jpg)](./img/P1040378.jpg "P1040378"){ .glightbox data-gallery="mastech-ms8250d" }
<span class="caption">P1040378</span>

[![P1040343](./img/P1040343.jpg)](./img/P1040343.jpg "P1040343"){ .glightbox data-gallery="mastech-ms8250d" }
<span class="caption">P1040343</span>

</div>
## Protocol

The chip periodically sends 18-byte packets at 2400 baud, 8n1. There is no checksum or CRC in the packet.

The payload is composed of a 1-1 mapping of the LCD segments.

## Resources
- [Manual](http://www.mastech-group.com/download_s.php?id=62)
- [Vendor software](http://www.mastech-group.com/download_s.php?id=210)

