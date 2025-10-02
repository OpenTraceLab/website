---
title: Saleae Logic
---

# Saleae Logic

<div class="infobox" markdown>

![Saleae Logic](./img/Saleae_Logic.jpg){ .infobox-image }

### Saleae Logic

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
| **Website** | [saleae.com](http://www.saleae.com/logic/) |

</div>

The **Saleae Logic** is a USB-based, 8-channel logic analyzer with up to 24MHz sampling rate.

The unit itself is very small, and has a USB 2.0 port connecting it to a PC (and powering the unit) and a connector for the 8 + 1 probe set. It is built around a Cypress EZ-USB FX2LP microcontroller — an 8051-compatible chip with built-in USB 2.0 controller. It can sample 8 channels up to 24MHz.

In sigrok, we use the open-source [fx2lafw](https://sigrok.org/wiki/Fx2lafw) firmware for this logic analyzer.

See [Saleae Logic/Info](https://sigrok.org/wiki/Saleae_Logic/Info) for more details (such as **lsusb -vvv** output) about the device.

See [Saleae Logic16](https://sigrok.org/wiki/Saleae_Logic16) for the successor product of the Saleae Logic.

## Hardware
- **Main chip:** Cypress CY7C68013A-56PVXC (FX2LP)
- **ESD protection**: ST DVIULC6-4SC6
- **3.3V voltage regulator**: ST LD33C
- **I2C EEPROM**: Microchip 24LC00
- **Crystal**: 24MHz

The case has four **Torx T2** screws you need to remove in order to be able to open it.

## Photos

<div class="photo-grid" markdown>

[![Saleae Logic](./img/Saleae_Logic.jpg)](./img/Saleae_Logic.jpg "Saleae Logic"){ .glightbox data-gallery="saleae-logic" }
<span class="caption">Saleae Logic</span>

[![Saleae Logic](./img/Saleae_logic.jpg)](./img/Saleae_logic.jpg "Saleae Logic"){ .glightbox data-gallery="saleae-logic" }
<span class="caption">Saleae Logic</span>

[![Saleae Logic Collection](./img/Saleae_logic_collection.jpg)](./img/Saleae_logic_collection.jpg "Saleae Logic Collection"){ .glightbox data-gallery="saleae-logic" }
<span class="caption">Saleae Logic Collection</span>

[![Saleae Logic](./img/Saleae_Logic.jpg)](./img/Saleae_Logic.png "Saleae Logic"){ .glightbox data-gallery="saleae-logic" }
<span class="caption">Saleae Logic</span>

[![Saleae Logic Opened](./img/Saleae_logic_opened.jpg)](./img/Saleae_logic_opened.jpg "Saleae Logic Opened"){ .glightbox data-gallery="saleae-logic" }
<span class="caption">Saleae Logic Opened</span>

[![Saleae Logic Pcb Front](./img/Saleae_logic_pcb_front.jpg)](./img/Saleae_logic_pcb_front.jpg "Saleae Logic Pcb Front"){ .glightbox data-gallery="saleae-logic" }
<span class="caption">Saleae Logic Pcb Front</span>

[![Saleae Logic Pcb Back](./img/Saleae_logic_pcb_back.jpg)](./img/Saleae_logic_pcb_back.jpg "Saleae Logic Pcb Back"){ .glightbox data-gallery="saleae-logic" }
<span class="caption">Saleae Logic Pcb Back</span>

</div>
## Protocol

Since we use the open-source [fx2lafw](https://sigrok.org/wiki/Fx2lafw) firmware for this device, we don't need to know the protocol.

However, for those interested in this, see our old [vendor protocol docs](https://sigrok.org/wiki/Saleae_Logic/Info#Vendor_USB_protocol).

## Resources
- [User's guide](http://downloads.saleae.com/Logic+Guide.pdf)
- [Vendor software](http://www.saleae.com/downloads)
- [SDKs](http://community.saleae.com/)

