---
title: Dangerous Prototypes Buspirate
---

# Dangerous Prototypes Buspirate

<div class="infobox" markdown>

![Dangerous Prototypes Buspirate](./img/Buspirate_v3.png){ .infobox-image }

### Dangerous Prototypes Buspirate

| | |
|---|---|
| **Status** | supported |
| **Source code** | [openbench-logic-sniffer](https://github.com/OpenTraceLab/OpenTraceCapture/tree/main/src/hardware/openbench-logic-sniffer) |
| **Channels** | 5 |
| **Samplerate** | 1MHz |
| **Samplerate (state)** | — |
| **Triggers** | ? |
| **Min/max voltage** | ? |
| **Memory** | 4096 samples |
| **Compression** | none |
| **Price range** | $30 - $50 |
| **Website** | [dangerousprototypes.com](http://dangerousprototypes.com/2009/11/03/bus-pirate-logic-analyzer-mode/) |

</div>

The **Dangerous Prototypes Buspirate** supports a logic analyzer mode and can thus be used for sample captures, however only at low speeds. To quote from the announcement: *The Bus Pirate can’t store a lot of samples, it can’t feed live samples very fast, and speeds are in the kHz range*.

See [Dangerous Prototypes Buspirate/Info](https://sigrok.org/wiki/Dangerous_Prototypes_Buspirate/Info) for more details (such as **lsusb -v** output) about the device.

## Hardware
- Microchip PIC24FJ64GA
- FTDI FT232RL
- NXP 74HC4066D

## Photos

<div class="photo-grid" markdown>

[![Buspirate V3](./img/Buspirate_v3.png)](./img/Buspirate_v3.png "Buspirate V3"){ .glightbox data-gallery="dangerous-prototypes-buspirate" }
<span class="caption">Buspirate V3</span>

[![Buspirate V3 Mugshot](./img/Buspirate_v3_mugshot.jpg)](./img/Buspirate_v3_mugshot.jpg "Buspirate V3 Mugshot"){ .glightbox data-gallery="dangerous-prototypes-buspirate" }
<span class="caption">Buspirate V3 Mugshot</span>

[![Buspirate V4 Mugshot](./img/Buspirate_v4_mugshot.jpg)](./img/Buspirate_v4_mugshot.jpg "Buspirate V4 Mugshot"){ .glightbox data-gallery="dangerous-prototypes-buspirate" }
<span class="caption">Buspirate V4 Mugshot</span>

[![Buspirate V3 Back](./img/Buspirate_v3_back.jpg)](./img/Buspirate_v3_back.jpg "Buspirate V3 Back"){ .glightbox data-gallery="dangerous-prototypes-buspirate" }
<span class="caption">Buspirate V3 Back</span>

[![Buspirate V3 Sparkfun Bottom](./img/Buspirate_v3_sparkfun_bottom.jpg)](./img/Buspirate_v3_sparkfun_bottom.jpg "Buspirate V3 Sparkfun Bottom"){ .glightbox data-gallery="dangerous-prototypes-buspirate" }
<span class="caption">Buspirate V3 Sparkfun Bottom</span>

[![Buspirate V3 Sparkfun Top](./img/Buspirate_v3_sparkfun_top.jpg)](./img/Buspirate_v3_sparkfun_top.jpg "Buspirate V3 Sparkfun Top"){ .glightbox data-gallery="dangerous-prototypes-buspirate" }
<span class="caption">Buspirate V3 Sparkfun Top</span>

</div>
## Protocol

The buspirate (in logic analyzer mode) uses a simplified version of the ["extended SUMP" protocol](https://sigrok.org/wiki/Openbench_Logic_Sniffer#Protocol).

## Resources
- [Bus Pirate](http://dangerousprototypes.com/docs/Bus_Pirate) (main wiki page)

