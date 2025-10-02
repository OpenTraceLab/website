---
title: Hobby Components HCTEST0006
---

# Hobby Components HCTEST0006

<div class="infobox" markdown>

![Hobby Components HCTEST0006](./img/Hobby_components_hctest0006_mugshot.png){ .infobox-image }

### Hobby Components HCTEST0006

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
| **Price range** | $5 - $10 |
| **Website** | [hobbycomponents.com](http://hobbycomponents.com/test/243-hobby-components-usb-8ch-24mhz-8-channel-logic-analyser) |

</div>

The **Hobby Components HCTEST0006** is a USB-based, 8-channel logic analyzer with up to 24MHz sampling rate.

This device ships with the [official sigrok fx2lafw VID/PID](http://sigrok.org/blog/sigrok-firmware-fx2lafw-013-released) in its I²C EEPROM, thus can (only) be used with the fully open-source [fx2lafw](https://sigrok.org/wiki/Fx2lafw) firmware and the sigrok software stack.

## Hardware
- **Main chip**: Cypress CY7C68013A-56LTXI (FX2LP)
- **Input buffer**: NXP 74HC245 (markings: "NXP HC245 ED54008 TXD449E")
- **256-byte I²C EEPROM**: Atmel AT24C02 (markings: "ATMEL450 24C02BN SU27 D")
- **3.3V low-dropout voltage regulator**: Advanced Monolithic Systems AMS1117-3.3 (markings: "AMS1117 3.3 H1418")
- **24MHz crystal**: 24.000

## Photos

<div class="photo-grid" markdown>

[![Hobby Components Hctest0006 Mugshot](./img/Hobby_components_hctest0006_mugshot.png)](./img/Hobby_components_hctest0006_mugshot.png "Hobby Components Hctest0006 Mugshot"){ .glightbox data-gallery="hobby-components-hctest0006" }
<span class="caption">Hobby Components Hctest0006 Mugshot</span>

</div>
## Protocol

This device (only) uses the open-source [fx2lafw](https://sigrok.org/wiki/Fx2lafw) firmware with the corresponding USB protocol.

## Resources
- [Hobby Components store page](http://hobbycomponents.com/test/243-hobby-components-usb-8ch-24mhz-8-channel-logic-analyser)

