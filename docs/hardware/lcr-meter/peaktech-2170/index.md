---
title: PeakTech 2170
---

# PeakTech 2170

<div class="infobox" markdown>

![PeakTech 2170](./img/P2170_device_back.png){ .infobox-image }

### PeakTech 2170

| | |
|---|---|
| **Status** | supported |
| **Source code** | [serial-lcr](https://github.com/OpenTraceLab/OpenTraceCapture/tree/main/src/hardware/serial-lcr) |
| **Counts** | 20000 |
| **IEC 61010-1** | — |
| **Connectivity** | USB |
| **Measurements** | resistance, capacitance, inductance, equivalents |
| **Features** | autorange, rel, data-hold, auto-poweroff, self-calibration |
| **Website** | [peaktech.de](http://www.peaktech.de/productdetail/kategorie/lcr-esr-messer/produkt/peaktech-2170.html) |

</div>

The **PeakTech 2170** is a 20000 counts handheld LCR meter with USB connectivity.

Accuracy is 0.3%. LCR measurement frequencies are 100/120/1000/10k/100k Hz.

See [PeakTech 2170/Info](https://sigrok.org/wiki/PeakTech_2170/Info) for more details (such as **lsusb -v** output) about the device.

## Hardware
- Cyrustek ES51919/ES51920 chipset
- Prolific PL2303 USB converter

**USB cable**:

- The LCR meter has USB builtin (onboard PL2303 chip, mini-B connector).

## Photos

<div class="photo-grid" markdown>

[![P2170 Device Back](./img/P2170_device_back.png)](./img/P2170_device_back.png "P2170 Device Back"){ .glightbox data-gallery="peaktech-2170" }
<span class="caption">P2170 Device Back</span>

[![P2170 Pcb Bottom](./img/P2170_pcb_bottom.png)](./img/P2170_pcb_bottom.png "P2170 Pcb Bottom"){ .glightbox data-gallery="peaktech-2170" }
<span class="caption">P2170 Pcb Bottom</span>

[![P2170 Pcb Top](./img/P2170_pcb_top.png)](./img/P2170_pcb_top.png "P2170 Pcb Top"){ .glightbox data-gallery="peaktech-2170" }
<span class="caption">P2170 Pcb Top</span>

[![P2170 Accessories](./img/P2170_accessories.png)](./img/P2170_accessories.png "P2170 Accessories"){ .glightbox data-gallery="peaktech-2170" }
<span class="caption">P2170 Accessories</span>

[![P2170 Lcd Capacitance](./img/P2170_lcd_capacitance.png)](./img/P2170_lcd_capacitance.png "P2170 Lcd Capacitance"){ .glightbox data-gallery="peaktech-2170" }
<span class="caption">P2170 Lcd Capacitance</span>

[![P2170 Pcb Top Lcrchip](./img/P2170_pcb_top_lcrchip.png)](./img/P2170_pcb_top_lcrchip.png "P2170 Pcb Top Lcrchip"){ .glightbox data-gallery="peaktech-2170" }
<span class="caption">P2170 Pcb Top Lcrchip</span>

[![P2170 Device Front](./img/P2170_device_front.png)](./img/P2170_device_front.png "P2170 Device Front"){ .glightbox data-gallery="peaktech-2170" }
<span class="caption">P2170 Device Front</span>

[![P2170 Pcb Top Input](./img/P2170_pcb_top_input.png)](./img/P2170_pcb_top_input.png "P2170 Pcb Top Input"){ .glightbox data-gallery="peaktech-2170" }
<span class="caption">P2170 Pcb Top Input</span>

[![Peaktech 2170 Mugshot](./img/Peaktech_2170_mugshot.png)](./img/Peaktech_2170_mugshot.png "Peaktech 2170 Mugshot"){ .glightbox data-gallery="peaktech-2170" }
<span class="caption">Peaktech 2170 Mugshot</span>

[![P2170 Lcd Resistance](./img/P2170_lcd_resistance.png)](./img/P2170_lcd_resistance.png "P2170 Lcd Resistance"){ .glightbox data-gallery="peaktech-2170" }
<span class="caption">P2170 Lcd Resistance</span>

</div>
## Protocol

ES51919 chip protocol (serial).

## Resources
- [Manual](http://www.peaktech.de/productdetail/kategorie/lcr-esr-messer/produkt/peaktech-2170.html?file=tl_files/downloads/2001%20-%203000/PeakTech_2170.pdf)

