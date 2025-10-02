---
title: PeakTech 3415
---

# PeakTech 3415

<div class="infobox" markdown>

![PeakTech 3415](./img/Peaktech3415_top.png){ .infobox-image }

### PeakTech 3415

| | |
|---|---|
| **Status** | supported |
| **Source code** | [serial-dmm](https://github.com/OpenTraceLab/OpenTraceCapture/tree/main/src/hardware/serial-dmm) |
| **Counts** | 6000 |
| **IEC 61010-1** | CAT III (1000V) / CAT IV (600V) |
| **Measurements** | voltage, current, resistance, capacitance, frequency, temperature, duty cycle, diode, continuity |
| **Features** | autorange, data hold, relative, min/max, backlight |
| **Website** | [peaktech.de](https://www.peaktech.de/productdetail/kategorie/digital---handmultimeter/produkt/peaktech-3415-usb.815.html) |

</div>

The **Peaktech** is a handheld digital multimeter with USB connectivity.

The device uses the [Dream Tech International DTM0660](https://sigrok.org/wiki/Multimeter_ICs#Dream_Tech_International_DTM0660) as main IC.

See [PeakTech 3415/Info](https://sigrok.org/wiki/PeakTech_3415/Info) for more details (such as **lsusb -v** output) about the device.

## Hardware

**Multimeter:**

- **Multimeter IC**: [Dream Tech International DTM0660](https://sigrok.org/wiki/Multimeter_ICs#Dream_Tech_International_DTM0660)
- **Fuses**: F10A/1000V 10.3x38, F0.63A/1000V 10.3x38

## Photos

<div class="photo-grid" markdown>

[![Peaktech3415 Top](./img/Peaktech3415_top.png)](./img/Peaktech3415_top.png "Peaktech3415 Top"){ .glightbox data-gallery="peaktech-3415" }
<span class="caption">Peaktech3415 Top</span>

[![Peaktech3415 Cable](./img/Peaktech3415_cable.JPG)](./img/Peaktech3415_cable.JPG "Peaktech3415 Cable"){ .glightbox data-gallery="peaktech-3415" }
<span class="caption">Peaktech3415 Cable</span>

[![Peaktech3415 Operation](./img/Peaktech3415_operation.JPG)](./img/Peaktech3415_operation.JPG "Peaktech3415 Operation"){ .glightbox data-gallery="peaktech-3415" }
<span class="caption">Peaktech3415 Operation</span>

[![Peaktech3415 Pcb](./img/Peaktech3415_pcb.jpg)](./img/Peaktech3415_pcb.jpg "Peaktech3415 Pcb"){ .glightbox data-gallery="peaktech-3415" }
<span class="caption">Peaktech3415 Pcb</span>

</div>
## Protocol

To enable output to the PC on the multimeter you have to long-press the **REL** key. However, it will auto-poweroff even in this mode. To avoid that, press **SELECT** key during power-up (see manual).

## Resources
- [Manual](https://www.peaktech.de/tl_files/downloads/3001%20-%204000/PeakTech_3415%20USB.pdf)
- [Communication protocol](https://www.peaktech.de/tl_files/downloads/Schnittstellenprotokolle/Communication_protocols_all_DMM_2017-12-27.pdf)

