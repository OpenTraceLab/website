---
title: Robomotic MiniLogic
---

# Robomotic MiniLogic

<div class="infobox" markdown>

![Robomotic MiniLogic](./img/Robomotic_minilogic_microchip_24lc64i.jpg){ .infobox-image }

### Robomotic MiniLogic

| | |
|---|---|
| **Status** | supported |
| **Source code** | [fx2lafw](https://github.com/OpenTraceLab/OpenTraceCapture/tree/main/src/hardware/fx2lafw) |
| **Channels** | 8 |
| **Samplerate** | 24MHz |
| **Samplerate (state)** | — |
| **Triggers** | none (SW-only) |
| **Min/max voltage** | -0.5V — 5.25V |
| **Threshold voltage** | Fixed: VIH=2.0V—5.25V, VIL=-0.5V—0.8V |
| **Memory** | none |
| **Compression** | none |
| **Website** | [robomotic.com](http://buglogic.robomotic.com) |

</div>

The **Robomotic MiniLogic** is a USB-based, 8-channel logic analyzer with up to 24MHz sampling rate.

It is a clone of the [Saleae Logic](https://sigrok.org/wiki/Saleae_Logic).

In sigrok, we use the open-source [fx2lafw](https://sigrok.org/wiki/Fx2lafw) firmware for this logic analyzer.

See [Robomotic MiniLogic/Info](https://sigrok.org/wiki/Robomotic_MiniLogic/Info) for more details (such as **lsusb -vvv** output) about the device.

## Hardware
- **Main chip:** [Cypress CY7C68013A-56PVXC (FX2LP)](http://www.cypress.com/?rID=38801) ([datasheet](http://www.cypress.com/?docID=34060))
- **Octal 3-state non-inverting buffer/line-driver/line-receiver:** 74HC244A (TODO: vendor?)
- **1A low-dropout voltage regulator (3.3V):** [Advanced Monolithic Systems AMS1117-3.3](http://www.advanced-monolithic.com/products/voltreg.html#1117) ([datasheet](http://www.advanced-monolithic.com/pdf/ds1117.pdf))
- **2K I2C serial EEPROM:** 2x [Microchip 24LC02BI](https://www.microchip.com/wwwproducts/Devices.aspx?dDocName=en010810) ([datasheet](http://ww1.microchip.com/downloads/en/DeviceDoc/21709J.pdf))
- **64K I2C serial EEPROM:** [Microchip 24LC64I](https://www.microchip.com/wwwproducts/Devices.aspx?dDocName=en010831) ([datasheet](http://ww1.microchip.com/downloads/en/DeviceDoc/21189S.pdf))

## Photos

<div class="photo-grid" markdown>

[![Robomotic Minilogic Microchip 24lc64i](./img/Robomotic_minilogic_microchip_24lc64i.jpg)](./img/Robomotic_minilogic_microchip_24lc64i.jpg "Robomotic Minilogic Microchip 24lc64i"){ .glightbox data-gallery="robomotic-minilogic" }
<span class="caption">Robomotic Minilogic Microchip 24lc64i</span>

[![Robomotic Minilogic](./img/Robomotic_minilogic.jpg)](./img/Robomotic_minilogic.jpg "Robomotic Minilogic"){ .glightbox data-gallery="robomotic-minilogic" }
<span class="caption">Robomotic Minilogic</span>

[![Robomotic Minilogic](./img/Robomotic_minilogic.png)](./img/Robomotic_minilogic.png "Robomotic Minilogic"){ .glightbox data-gallery="robomotic-minilogic" }
<span class="caption">Robomotic Minilogic</span>

[![Robomotic Minilogic Back](./img/Robomotic_minilogic_back.jpg)](./img/Robomotic_minilogic_back.jpg "Robomotic Minilogic Back"){ .glightbox data-gallery="robomotic-minilogic" }
<span class="caption">Robomotic Minilogic Back</span>

[![Robomotic Minilogic Ams1117](./img/Robomotic_minilogic_ams1117.jpg)](./img/Robomotic_minilogic_ams1117.jpg "Robomotic Minilogic Ams1117"){ .glightbox data-gallery="robomotic-minilogic" }
<span class="caption">Robomotic Minilogic Ams1117</span>

[![Robomotic Minilogic Pcb Back](./img/Robomotic_minilogic_pcb_back.jpg)](./img/Robomotic_minilogic_pcb_back.jpg "Robomotic Minilogic Pcb Back"){ .glightbox data-gallery="robomotic-minilogic" }
<span class="caption">Robomotic Minilogic Pcb Back</span>

[![Robomotic Minilogic 74hc244a](./img/Robomotic_minilogic_74hc244a.jpg)](./img/Robomotic_minilogic_74hc244a.jpg "Robomotic Minilogic 74hc244a"){ .glightbox data-gallery="robomotic-minilogic" }
<span class="caption">Robomotic Minilogic 74hc244a</span>

[![Robomotic Minilogic Microchip 24lc02bi](./img/Robomotic_minilogic_microchip_24lc02bi.jpg)](./img/Robomotic_minilogic_microchip_24lc02bi.jpg "Robomotic Minilogic Microchip 24lc02bi"){ .glightbox data-gallery="robomotic-minilogic" }
<span class="caption">Robomotic Minilogic Microchip 24lc02bi</span>

[![Robomotic Minilogic Pcb Front](./img/Robomotic_minilogic_pcb_front.jpg)](./img/Robomotic_minilogic_pcb_front.jpg "Robomotic Minilogic Pcb Front"){ .glightbox data-gallery="robomotic-minilogic" }
<span class="caption">Robomotic Minilogic Pcb Front</span>

[![Robomotic Minilogic Cypress Fx2](./img/Robomotic_minilogic_cypress_fx2.jpg)](./img/Robomotic_minilogic_cypress_fx2.jpg "Robomotic Minilogic Cypress Fx2"){ .glightbox data-gallery="robomotic-minilogic" }
<span class="caption">Robomotic Minilogic Cypress Fx2</span>

</div>
## Protocol

Since we use the open-source [fx2lafw](https://sigrok.org/wiki/Fx2lafw) firmware for this device, we don't need to know the protocol.

## Resources

TODO.

