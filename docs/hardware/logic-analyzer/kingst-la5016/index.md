---
title: Kingst LA5016
---

# Kingst LA5016

<div class="infobox" markdown>

![Kingst LA5016](./img/Kingst-la5016-size-compared.jpg){ .infobox-image }

### Kingst LA5016

| | |
|---|---|
| **Status** | supported |
| **Source code** | [kingst-la2016](https://github.com/OpenTraceLab/OpenTraceCapture/tree/main/src/hardware/kingst-la2016) |
| **Channels** | 16 |
| **Samplerate** | 500MHz max. |
| **Samplerate (state)** | — |
| **Triggers** | Level, Edge |
| **Min/max voltage** | -50V — +50V tolerant |
| **Threshold voltage** | -4.0V — +4.0V, min step 0.01V |
| **Memory** | 2Gib RAM (256MiB) |
| **Compression** | Yes |
| **Website** | [qdkingst.com](http://www.qdkingst.com/en) |

</div>

The **Kingst LA5016** is a USB-based, 16-channel logic analyser with 500MHz maximum sampling rate and 256MiB sample memory.
It is part of the [Kingst LA Series](https://sigrok.org/wiki/Kingst_LA_Series) and is supported by the **kingst-la2016** sigrok driver.

The USB identification is shared among Kingst LA devices. See [Kingst LA2016](https://sigrok.org/wiki/Kingst_LA2016), the same VID:PID and the same USB endpoints are used.

## Hardware

TODO Add more details.

- Cypress FX2 MCU
- AT24C02 EEPROM
- Cyclone IV FPGA (Altera/Intel)
- U10 authentication device
- 2Gib DRAM
- a bunch of regulators
- opamp for input threshold control

## Photos

<div class="photo-grid" markdown>

[![Kingst La5016 Size Compared](./img/Kingst-la5016-size-compared.jpg)](./img/Kingst-la5016-size-compared.png "Kingst La5016 Size Compared"){ .glightbox data-gallery="kingst-la5016" }
<span class="caption">Kingst La5016 Size Compared</span>

[![Kingst La5016 Mugshot](./img/Kingst-la5016-mugshot.jpg)](./img/Kingst-la5016-mugshot.png "Kingst La5016 Mugshot"){ .glightbox data-gallery="kingst-la5016" }
<span class="caption">Kingst La5016 Mugshot</span>

[![Kingst La5016 Pcb Top](./img/Kingst-la5016-pcb-top.jpg)](./img/Kingst-la5016-pcb-top.png "Kingst La5016 Pcb Top"){ .glightbox data-gallery="kingst-la5016" }
<span class="caption">Kingst La5016 Pcb Top</span>

[![Kingst La5016 Pcb Bottom](./img/Kingst-la5016-pcb-bottom.jpg)](./img/Kingst-la5016-pcb-bottom.png "Kingst La5016 Pcb Bottom"){ .glightbox data-gallery="kingst-la5016" }
<span class="caption">Kingst La5016 Pcb Bottom</span>

[![Kingst La5016 Case Open](./img/Kingst-la5016-case-open.jpg)](./img/Kingst-la5016-case-open.png "Kingst La5016 Case Open"){ .glightbox data-gallery="kingst-la5016" }
<span class="caption">Kingst La5016 Case Open</span>

[![Kingst La5016 Connectors](./img/Kingst-la5016-connectors.jpg)](./img/Kingst-la5016-connectors.png "Kingst La5016 Connectors"){ .glightbox data-gallery="kingst-la5016" }
<span class="caption">Kingst La5016 Connectors</span>

</div>
## Protocol

See the [Kingst LA Series](https://sigrok.org/wiki/Kingst_LA_Series) page, all devices communicate to the host in identical ways.

## Firmware

Device firmware must be extracted from vendor software before sigrok use. See [Kingst LA Series](https://sigrok.org/wiki/Kingst_LA_Series) for details.

