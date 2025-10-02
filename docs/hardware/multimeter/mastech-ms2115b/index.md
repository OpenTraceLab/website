---
title: MASTECH MS2115B
---

# MASTECH MS2115B

<div class="infobox" markdown>

![MASTECH MS2115B](./img/Ms2115b_usb_port.jpg){ .infobox-image }

### MASTECH MS2115B

| | |
|---|---|
| **Status** | supported |
| **Source code** | [serial-dmm](https://github.com/OpenTraceLab/OpenTraceCapture/tree/main/src/hardware/serial-dmm) |
| **Counts** | 6000 |
| **IEC 61010-1** | CAT III (1000V) / CAT IV (600V) |
| **Connectivity** | USB/serial |
| **Measurements** | voltage, current, resistance, capacitance, frequency, duty cycle, diode, continuity |
| **Features** | autorange, true-rms, data hold, min/max, relative, inrush, bargraph, backlight, ncv |
| **Website** | [mastech-group.com](http://www.mastech-group.com/products.php?cate=97) |

</div>

The **MASTECH MS2115B** is a 6000 counts, CAT III (1000V) / CAT IV (600V) handheld dual display digital AC/DC clamp meter with USB connectivity.

See [MASTECH MS2115B/Info](https://sigrok.org/wiki/MASTECH_MS2115B/Info) for more details (such as **lsusb -v** output) about the device.

## Hardware
- Silicon Labs CP2102 USB to UART bridge controller ([datasheet](https://www.silabs.com/documents/public/data-sheets/CP2102-9.pdf))
- Cyrustek ES51970 DMM analog front end with inrush ([datasheet](http://www.cyrustek.com.tw/spec/ES51970.pdf))

## Photos

<div class="photo-grid" markdown>

[![Ms2115b Usb Port](./img/Ms2115b_usb_port.jpg)](./img/Ms2115b_usb_port.jpg "Ms2115b Usb Port"){ .glightbox data-gallery="mastech-ms2115b" }
<span class="caption">Ms2115b Usb Port</span>

[![Mastech Ms2115b Package Bottom](./img/Mastech_ms2115b_package_bottom.jpg)](./img/Mastech_ms2115b_package_bottom.jpg "Mastech Ms2115b Package Bottom"){ .glightbox data-gallery="mastech-ms2115b" }
<span class="caption">Mastech Ms2115b Package Bottom</span>

[![Ms2115b Back](./img/Ms2115b_back.jpg)](./img/Ms2115b_back.jpg "Ms2115b Back"){ .glightbox data-gallery="mastech-ms2115b" }
<span class="caption">Ms2115b Back</span>

[![Mastech Ms2115b Device Bottom](./img/Mastech_ms2115b_device_bottom.jpg)](./img/Mastech_ms2115b_device_bottom.jpg "Mastech Ms2115b Device Bottom"){ .glightbox data-gallery="mastech-ms2115b" }
<span class="caption">Mastech Ms2115b Device Bottom</span>

[![Mastech Ms2115b Package Contents](./img/Mastech_ms2115b_package_contents.jpg)](./img/Mastech_ms2115b_package_contents.jpg "Mastech Ms2115b Package Contents"){ .glightbox data-gallery="mastech-ms2115b" }
<span class="caption">Mastech Ms2115b Package Contents</span>

[![Mastech Ms2115b Package Top](./img/Mastech_ms2115b_package_top.jpg)](./img/Mastech_ms2115b_package_top.jpg "Mastech Ms2115b Package Top"){ .glightbox data-gallery="mastech-ms2115b" }
<span class="caption">Mastech Ms2115b Package Top</span>

[![Mastech Ms2115b Mugshot](./img/Mastech_ms2115b_mugshot.png)](./img/Mastech_ms2115b_mugshot.png "Mastech Ms2115b Mugshot"){ .glightbox data-gallery="mastech-ms2115b" }
<span class="caption">Mastech Ms2115b Mugshot</span>

[![Ms2115b Front](./img/Ms2115b_front.jpg)](./img/Ms2115b_front.jpg "Ms2115b Front"){ .glightbox data-gallery="mastech-ms2115b" }
<span class="caption">Ms2115b Front</span>

[![Mastech Ms2115b Device Top](./img/Mastech_ms2115b_device_top.jpg)](./img/Mastech_ms2115b_device_top.jpg "Mastech Ms2115b Device Top"){ .glightbox data-gallery="mastech-ms2115b" }
<span class="caption">Mastech Ms2115b Device Top</span>

</div>
## Protocol

The chip periodically sends 9-byte packets at 1200 baud, 8n1. There is no checksum or CRC in the packet.
[ms2115b.c](https://github.com/miek/libsigrok/blob/master/src/dmm/ms2115b.c)

## Resources
- [YouTube: FLR: Mastech MS2115B review](https://www.youtube.com/watch?v=0wLex6KQO04)
- [YouTube: DIY Tech & Repairs: Mastech MS2115A - Quick look](https://www.youtube.com/watch?v=g3WnYct1h8Q)

