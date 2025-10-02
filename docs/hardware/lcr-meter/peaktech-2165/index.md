---
title: Peaktech 2165
---

# Peaktech 2165

<div class="infobox" markdown>

![Peaktech 2165](./img/Vc4080-cable-ir-port.png){ .infobox-image }

### Peaktech 2165

| | |
|---|---|
| **Status** | supported |
| **Source code** | [serial-lcr](https://github.com/OpenTraceLab/OpenTraceCapture/tree/main/src/hardware/serial-lcr) |
| **Counts** | 20000 |
| **IEC 61010-1** | — |
| **Connectivity** | USB, RS232 |
| **Measurements** | resistance, capacitance, inductance |
| **Features** | autorange, relative, auto-poweroff, min-max, tolerance |
| **Website** | [peaktech.de](https://www.peaktech.de/productdetail/kategorie/lcr-messgeraet/produkt/p-2165.html) |

</div>

The **Peaktech 2165** is an LCR meter with USB connectivity. It is a 4.5 digits (20000 count) LCR meter with 0.5% basic accuracy (resistance) that can measure at 120Hz and 1kHz, and comes with USB connectivity (serial protocol). It is a [Voltcraft 4080](https://sigrok.org/wiki/Voltcraft_4080) lookalike.

See [Peaktech_2165/Info](https://sigrok.org/wiki/Peaktech_2165/Info) for USB details.

## Hardware

LCR meter:

- [TI TLC7135C](http://www.ti.com/product/TLC7135) ADC, 4 1/2 digits, 1Ksa/s
- TI MSP430 MCU
- several discrete TI components

USB to IR cable:

- FT232R, regular serial port, bidirectional (RX and TX LED)

## Photos

<div class="photo-grid" markdown>

[![Vc4080 Cable Ir Port](./img/Vc4080-cable-ir-port.png)](./img/Vc4080-cable-ir-port.png "Vc4080 Cable Ir Port"){ .glightbox data-gallery="peaktech-2165" }
<span class="caption">Vc4080 Cable Ir Port</span>

[![Peaktech2165 Front](./img/Peaktech2165-front.png)](./img/Peaktech2165-front.png "Peaktech2165 Front"){ .glightbox data-gallery="peaktech-2165" }
<span class="caption">Peaktech2165 Front</span>

[![Vc4080 Pcb Top](./img/Vc4080-pcb-top.png)](./img/Vc4080-pcb-top.png "Vc4080 Pcb Top"){ .glightbox data-gallery="peaktech-2165" }
<span class="caption">Vc4080 Pcb Top</span>

[![Vc4080 Inside Overview](./img/Vc4080-inside-overview.png)](./img/Vc4080-inside-overview.png "Vc4080 Inside Overview"){ .glightbox data-gallery="peaktech-2165" }
<span class="caption">Vc4080 Inside Overview</span>

[![Vc4080 Pcb Top Zoom Mcu Adc](./img/Vc4080-pcb-top-zoom-mcu-adc.png)](./img/Vc4080-pcb-top-zoom-mcu-adc.png "Vc4080 Pcb Top Zoom Mcu Adc"){ .glightbox data-gallery="peaktech-2165" }
<span class="caption">Vc4080 Pcb Top Zoom Mcu Adc</span>

[![Vc4080 Display All Segments](./img/Vc4080-display-all-segments.png)](./img/Vc4080-display-all-segments.png "Vc4080 Display All Segments"){ .glightbox data-gallery="peaktech-2165" }
<span class="caption">Vc4080 Display All Segments</span>

[![Vc4080 Case Dc Ir](./img/Vc4080-case-dc-ir.png)](./img/Vc4080-case-dc-ir.png "Vc4080 Case Dc Ir"){ .glightbox data-gallery="peaktech-2165" }
<span class="caption">Vc4080 Case Dc Ir</span>

</div>
## Protocol

Serial communication runs at 1200/7e1, uses ASCII characters and is basically human readable.

Serial packets consist of 39 ASCII characters that end in the CR-LF termination, contain a lot of single character flags, as well as multiple multi-character fields for the primary and secondary displays.

The description of the commands you find [at Conrad](http://www.produktinfo.conrad.com/datenblaetter/100000-124999/121064-da-01-en-Schnittstellenbeschr_LCR_4080_Handmessg.pdf). The [PeakTech 2165 user manual](http://peaktech.de/productdetail/kategorie/lcr-messer/produkt/p-2165.html?file=tl_files/downloads/2001%20-%203000/PeakTech_2165_USB.pdf) has another description, represented differently.

See [Voltcraft 4080](https://sigrok.org/wiki/Voltcraft_4080) for a few more details.

### Resources
- [PeakTech 2165 product page](http://peaktech.de/productdetail/kategorie/lcr-messer/produkt/p-2165.html)
- [PeakTech user manual](http://peaktech.de/productdetail/kategorie/lcr-messer/produkt/p-2165.html?file=tl_files/downloads/2001%20-%203000/PeakTech_2165_USB.pdf) bilingual (German/English), see chapter 7 for the protocol

