---
title: Velleman DVM4100
---

# Velleman DVM4100

<div class="infobox" markdown>

![Velleman DVM4100](./img/DVM4100.png){ .infobox-image }

### Velleman DVM4100

| | |
|---|---|
| **Status** | supported |
| **Source code** | [serial-dmm](https://github.com/OpenTraceLab/OpenTraceCapture/tree/main/src/hardware/serial-dmm) |
| **Counts** | 6000 |
| **IEC 61010-1** | CAT III (1000V) / CAT IV (600V) |
| **Connectivity** | [USB/serial](https://sigrok.org/wiki/Device_cables#V.26A_VA4000) |
| **Measurements** | voltage, current, resistance, capacitance, frequency, temperature, duty cycle, diode, continuity |
| **Features** | autorange, data hold, relative, min/max, backlight |
| **Website** | [velleman.eu](http://www.velleman.eu/products/view/?id=385116) |

</div>

The **Velleman DVM4100** is a 6000 count CAT III (1000V) / CAT IV (600V) handheld digital multimeter with USB connectivity.

See [Velleman DVM4100/Info](https://sigrok.org/wiki/Velleman_DVM4100/Info) for more details (such as **lsusb -v** output) about the device.

The Velleman DVM4100 model looks identical to the [PeakTech 3415](https://sigrok.org/wiki/PeakTech_3415), except for its labels and blue case color. The DVM4100 also has similarities with the [V&A VA40B](https://sigrok.org/wiki/V%26A_VA40B) but with a different protocol version. This could suggest that those devices share the [Dream Tech International DTM0660](https://sigrok.org/wiki/Multimeter_ICs#Dream_Tech_International_DTM0660) as main IC since it's possible to modify certain protocol characteristics using this IC.

## Hardware

**Multimeter:**

- **Multimeter IC**: [Dream Tech International DTM0660](https://sigrok.org/wiki/Multimeter_ICs#Dream_Tech_International_DTM0660)
- **Fuses**: [F10A/1000V, F0.63A/1000V](http://www.velleman.eu/products/view/?id=387038)

**USB cable:**

- See [Device cables#V.26A_VA4000](https://sigrok.org/wiki/Device_cables#V.26A_VA4000).

## Photos

<div class="photo-grid" markdown>

[![Dvm4100](./img/DVM4100.png)](./img/DVM4100.png "Dvm4100"){ .glightbox data-gallery="velleman-dvm4100" }
<span class="caption">Dvm4100</span>

[![Dvm4100 Ir](./img/DVM4100_IR.jpg)](./img/DVM4100_IR.jpg "Dvm4100 Ir"){ .glightbox data-gallery="velleman-dvm4100" }
<span class="caption">Dvm4100 Ir</span>

[![Dvm4100 Top](./img/DVM4100_top.jpg)](./img/DVM4100_top.jpg "Dvm4100 Top"){ .glightbox data-gallery="velleman-dvm4100" }
<span class="caption">Dvm4100 Top</span>

[![Dvm4100 Bottom](./img/DVM4100_bottom.jpg)](./img/DVM4100_bottom.jpg "Dvm4100 Bottom"){ .glightbox data-gallery="velleman-dvm4100" }
<span class="caption">Dvm4100 Bottom</span>

[![Dvm4100 Case](./img/DVM4100_case.jpg)](./img/DVM4100_case.jpg "Dvm4100 Case"){ .glightbox data-gallery="velleman-dvm4100" }
<span class="caption">Dvm4100 Case</span>

</div>
## Protocol

15-byte LCD segments over USB-to-serial (Prolific chip, 2400 baud, 8n1). The DMM IC used in this multimeter is a [Dream Tech International DTM0660](https://sigrok.org/wiki/Multimeter_ICs#Dream_Tech_International_Ltd_DTM0660).

To enable output to the PC on the multimeter you have to keep the **REL** key pressed while powering on the device. However, it will auto-poweroff (after roughly 1 hour?), even in this mode. To avoid that, press both the **REL** and the **SELECT** key during power-up (see manual).

## Resources
- [Manual](http://www.velleman.eu/downloads/1/dvm4x00a6v03.pdf)

