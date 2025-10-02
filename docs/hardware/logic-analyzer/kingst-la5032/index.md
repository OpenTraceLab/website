---
title: Kingst LA5032
---

# Kingst LA5032

<div class="infobox" markdown>

![Kingst LA5032](./img/Kingst-la5032-mugshot.jpg){ .infobox-image }

### Kingst LA5032

| | |
|---|---|
| **Status** | supported |
| **Source code** | [kingst-la2016](https://github.com/OpenTraceLab/OpenTraceCapture/tree/main/src/hardware/kingst-la2016) |
| **Channels** | 32 |
| **Samplerate** | 500MHz max. |
| **Samplerate (state)** | — |
| **Triggers** | Level, Edge |
| **Min/max voltage** | -50V — +50V tolerant |
| **Threshold voltage** | -4.0V — +4.0V, min step 0.01V |
| **Memory** | 4Gib RAM (512MiB) |
| **Compression** | Yes |
| **Website** | [qdkingst.com](http://www.qdkingst.com/en) |

</div>

The **Kingst LA5032** is a USB-based, 32-channel logic analyser with 500MHz maximum sampling rate and 512MiB sample memory.
It is part of the [Kingst LA Series](https://sigrok.org/wiki/Kingst_LA_Series) and is supported by the **kingst-la2016** sigrok driver.

The USB identification is shared among Kingst LA devices. See [Kingst LA2016](https://sigrok.org/wiki/Kingst_LA2016), the same VID:PID and the same USB endpoints are used.

## Hardware
- Cypress FX2 MCU (assumed, label has been removed)
- AT24C02 EEPROM
- FPGA below heatsink, assumed to be Cyclone IV FPGA (Altera/Intel)
- U10 authentication device
- 2x 2Gib DRAM chips
- a bunch of regulators
- opamp for input threshold control
- input protection

## Photos

<div class="photo-grid" markdown>

[![Kingst La5032 Mugshot](./img/Kingst-la5032-mugshot.jpg)](./img/Kingst-la5032-mugshot.jpg "Kingst La5032 Mugshot"){ .glightbox data-gallery="kingst-la5032" }
<span class="caption">Kingst La5032 Mugshot</span>

[![Kingst La5032 Pcb Bottom](./img/Kingst-la5032-pcb-bottom.jpg)](./img/Kingst-la5032-pcb-bottom.jpg "Kingst La5032 Pcb Bottom"){ .glightbox data-gallery="kingst-la5032" }
<span class="caption">Kingst La5032 Pcb Bottom</span>

[![Kingst La5032 Pcb Top](./img/Kingst-la5032-pcb-top.jpg)](./img/Kingst-la5032-pcb-top.jpg "Kingst La5032 Pcb Top"){ .glightbox data-gallery="kingst-la5032" }
<span class="caption">Kingst La5032 Pcb Top</span>

</div>
## Protocol

See the [Kingst LA Series](https://sigrok.org/wiki/Kingst_LA_Series) page, all devices communicate to the host in identical ways.

## Firmware

Device firmware must be extracted from vendor software before sigrok use. See [Kingst LA Series](https://sigrok.org/wiki/Kingst_LA_Series) for details.

