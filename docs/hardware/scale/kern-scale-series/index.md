---
title: KERN scale series
---

# KERN scale series

<div class="infobox" markdown>

![KERN scale series](./img/Kern_ew-6200-2nm_mugshot.png){ .infobox-image }

### KERN scale series

| | |
|---|---|
| **Status** | supported |
| **Source code** | [kern-scale](https://github.com/OpenTraceLab/OpenTraceCapture/tree/main/src/hardware/kern-scale) |
| **Connectivity** | [RS-232](https://sigrok.org/wiki/Device_cables#KERN_EW_6200-2NM_cable) |
| **Measurements** | mass |
| **Website** | [kern-sohn.com](http://www.kern-sohn.com/shop/en/laboratory-balances/precision-balances/) |

</div>

The **KERN scale** is a series of weighing scales with RS-232 connectivity.

## Devices
| Device | Max. weight | Readout | Protocol | Comments |
|---|---|---|---|---|
| KERN EW 220-3NM | 220 g | 0.001 g | 14/15-byte ASCII |  |
| KERN EW 420-3NM | 420 g | 0.001 g | 14/15-byte ASCII |  |
| KERN EW 620-3NM | 620 g | 0.001 g | 14/15-byte ASCII |  |
| KERN EW 820-2NM | 820 g | 0.01 g | 14/15-byte ASCII |  |
| KERN EW 2200-2NM | 2200 g | 0.01 g | 14/15-byte ASCII |  |
| KERN EW 4200-2NM | 4200 g | 0.01 g | 14/15-byte ASCII |  |
| [KERN EW 6200-2NM](https://sigrok.org/wiki/KERN_EW_6200-2NM) | 6200 g | 0.01 g | 14/15-byte ASCII |  |
| KERN EW 12000-1NM | 12000 g | 0.1 g | 14/15-byte ASCII |  |
| KERN EG 220-3NM | 220 g | 0.001 g | 14/15-byte ASCII |  |
| KERN EG 420-3NM | 420 g | 0.001 g | 14/15-byte ASCII |  |
| KERN EG 620-3NM | 620 g | 0.001 g | 14/15-byte ASCII |  |
| KERN EG 2200-2NM | 2200 g | 0.01 g | 14/15-byte ASCII |  |
| KERN EG 4200-2NM | 4200 g | 0.01 g | 14/15-byte ASCII |  |

## Protocol

The devices use a simple ASCII-based protocol over an [RS-232 cable](https://sigrok.org/wiki/Device_cables#KERN_EW_6200-2NM_cable).

The default settings are (device-dependent), e.g., 1200 8N2, but the devices usually have a menu where the user can change the baud rate, parity settings, and so on.

There are two different packet lengths (also user-configurable via the menu): 14-byte packets and 15-byte packets.

See e.g. the [KERN EW/EG-N/EWB series user manual](http://dok.kern-sohn.com/downloads/de/EW%206200-2NM/file/EW_EG-(N)-EWB-BA-e-1226.pdf) for more protocol details.

## Resources
- [Device list](http://www.kern-sohn.com/shop/en/laboratory-balances/precision-balances/)

## Photos

<div class="photo-grid" markdown>

[![Kern Ew 6200 2nm Mugshot](./img/Kern_ew-6200-2nm_mugshot.png)](./img/Kern_ew-6200-2nm_mugshot.png "Kern Ew 6200 2nm Mugshot"){ .glightbox data-gallery="kern-scale-series" }
<span class="caption">Kern Ew 6200 2nm Mugshot</span>

</div>
