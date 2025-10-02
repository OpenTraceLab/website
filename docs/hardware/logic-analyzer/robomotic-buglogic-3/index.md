---
title: Robomotic BugLogic 3
---

# Robomotic BugLogic 3

<div class="infobox" markdown>

![Robomotic BugLogic 3](./img/Robomotic_buglogic3.jpg){ .infobox-image }

### Robomotic BugLogic 3

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
| **Website** | [robomotic.com](http://norduino.robomotic.com/products-page/categories/buglogic3/) |

</div>

The **Robomotic BugLogic 3** is a USB-based, 8-channel logic analyzer with up to 24MHz sampling rate. 

It is a clone of the [Saleae Logic](https://sigrok.org/wiki/Saleae_Logic).

In sigrok, we use the open-source [fx2lafw](https://sigrok.org/wiki/Fx2lafw) firmware for this logic analyzer.

See [Robomotic BugLogic 3/Info](https://sigrok.org/wiki/Robomotic_BugLogic_3/Info) for more details (such as **lsusb -vvv** output) about the device.

## Hardware
- **Main chip:** Cypress CY7C68013A-56LFXC (FX2LP)
- **I2C EEPROM**:&#160;?
- **Octal tristate bus transceiver**: LVC245 (TODO: vendor?)
- **Crystal**: 24MHz

## Photos

<div class="photo-grid" markdown>

[![Robomotic Buglogic3](./img/Robomotic_buglogic3.jpg)](./img/Robomotic_buglogic3.jpg "Robomotic Buglogic3"){ .glightbox data-gallery="robomotic-buglogic-3" }
<span class="caption">Robomotic Buglogic3</span>

[![Robomotic Buglogic3](./img/Robomotic_buglogic3.jpg)](./img/Robomotic_buglogic3.png "Robomotic Buglogic3"){ .glightbox data-gallery="robomotic-buglogic-3" }
<span class="caption">Robomotic Buglogic3</span>

</div>
## Protocol

Since we use the open-source [fx2lafw](https://sigrok.org/wiki/Fx2lafw) firmware for this device, we don't need to know the protocol.

## Resources
- [Buglogic3 wiki page](http://www.norduino.org/index.php?title=BugLogic3_board)
- [robomotic.com: Hardware description](http://norduino.robomotic.com/products-page/categories/buglogic3/)

