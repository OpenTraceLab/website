---
title: PeakTech 3442
---

# PeakTech 3442

<div class="infobox" markdown>

![PeakTech 3442](./img/Peaktech-3442-bta-4-pcb.png){ .infobox-image }

### PeakTech 3442

| | |
|---|---|
| **Status** | planned |
| **Counts** | 50000 |
| **Connectivity** | BLE |
| **Measurements** | voltage, current, resistance, capacitance, diode, continuity, frequency, duty cycle, period, temperature |
| **Features** | autorange, true-rms, hold, min/max, peak, lowpass, relative, current loop, bargraph, backlight |
| **Website** | [peaktech.de](https://www.peaktech.de/productdetail/kategorie/digital---handmultimeter/produkt/peaktech-3442.html) |

</div>

The **PeakTech 3442** is a 50000 counts handheld digital multimeter with BLE connectivity. It is a rebranded [CEM DT-987BT](https://sigrok.org/wiki/CEM_DT-987BT).

Hold the red **MODE** button to enable BLE communication.

## Hardware

meter

- **HY3131** DMM chipset
- [TI 385B-1.2](https://www.ti.com/lit/ds/symlink/lm385b-1.2.pdf) reference
- TI **MSP430** MCU
- TI **CC2541** BLE communication

dongle

- TI **CC2540** BLE communication

## Photos

<div class="photo-grid" markdown>

[![Peaktech 3442 Bta 4 Pcb](./img/Peaktech-3442-bta-4-pcb.png)](./img/Peaktech-3442-bta-4-pcb.png "Peaktech 3442 Bta 4 Pcb"){ .glightbox data-gallery="peaktech-3442" }
<span class="caption">Peaktech 3442 Bta 4 Pcb</span>

[![Peaktech 3442 Pcb Overview](./img/Peaktech-3442-pcb-overview.png)](./img/Peaktech-3442-pcb-overview.png "Peaktech 3442 Pcb Overview"){ .glightbox data-gallery="peaktech-3442" }
<span class="caption">Peaktech 3442 Pcb Overview</span>

[![Peaktech 3442 Front](./img/Peaktech-3442-front.png)](./img/Peaktech-3442-front.png "Peaktech 3442 Front"){ .glightbox data-gallery="peaktech-3442" }
<span class="caption">Peaktech 3442 Front</span>

[![Peaktech 3442 Pcb Dmm Chip](./img/Peaktech-3442-pcb-dmm-chip.png)](./img/Peaktech-3442-pcb-dmm-chip.png "Peaktech 3442 Pcb Dmm Chip"){ .glightbox data-gallery="peaktech-3442" }
<span class="caption">Peaktech 3442 Pcb Dmm Chip</span>

[![Peaktech 3442 Pcb Mcu Ble](./img/Peaktech-3442-pcb-mcu-ble.png)](./img/Peaktech-3442-pcb-mcu-ble.png "Peaktech 3442 Pcb Mcu Ble"){ .glightbox data-gallery="peaktech-3442" }
<span class="caption">Peaktech 3442 Pcb Mcu Ble</span>

[![Peaktech 3442 Bta 4 Case](./img/Peaktech-3442-bta-4-case.png)](./img/Peaktech-3442-bta-4-case.png "Peaktech 3442 Bta 4 Case"){ .glightbox data-gallery="peaktech-3442" }
<span class="caption">Peaktech 3442 Bta 4 Case</span>

</div>
## Protocol

The Peaktech meter ships with a USB dongle which is labelled "BTA-4", but turns out to be a TI "CC2540 USB Dongle V1.0" with a few parts not fitted (green LED, two push buttons, 2x5 programming header). The USB dongle registers with the PC as a USB ACM serial communication port. Its parameters are yet to get determined (uncertain which bitrate to use, and whether hardware handshake or modem control is involved, whether AT commands need to be sent, etc).

Without the USB dongle, the meter can be used with any other BLE central support in the PC. Communication is unidirektional (RX only on the PC side), data is received by means of BLE notifications.

The meter sends DMM packets of constant length (16(?) bytes each), with a fixed data pattern in some positions for synchronization (an assumption, yet to get verified). Thus this device lends itself to the serial-dmm driver's approach. The specific packet layout is yet to get determined (which fixed/reserved parts to check for reliable communication, which fields to get measurement values and their flags / modifiers from).

TODO

- 16 byte DMM packets, yet to get determined how to parse
## Resources
- TODO

