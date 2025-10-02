---
title: Braintechnology USB Interface V2.x
---

# Braintechnology USB Interface V2.x

<div class="infobox" markdown>

![Braintechnology USB Interface V2.x](./img/Braintechnology_usb_interface_v2x_pdei.jpg){ .infobox-image }

### Braintechnology USB Interface V2.x

| | |
|---|---|
| **Status** | supported |
| **Source code** | [fx2lafw](https://github.com/OpenTraceLab/OpenTraceCapture/tree/main/src/hardware/fx2lafw) |
| **Channels** | 8/16 |
| **Samplerate** | 24MHz |
| **Samplerate (state)** | — |
| **Triggers** | none (SW-only) |
| **Min/max voltage** | -0.5V — 5.25V |
| **Threshold voltage** | Fixed: VIH=2.0V—5.25V, VIL=-0.5V—0.8V |
| **Memory** | none |
| **Compression** | none |
| **Website** | [braintechnology.de](http://www.braintechnology.de/braintechnology/en/usb_fastinterface27.html) |

</div>

The **Braintechnology USB Interface V2.x** is a Cypress FX2 eval board, which can be used as USB-based, 16-channel logic analyzer with up to 24MHz sampling rate.

There are various revisions of the hardware, e.g. [V2.5](http://www.braintechnology.de/braintechnology/en/usb_fastinterface25.html), [V2.6](http://www.braintechnology.de/braintechnology/en/usb_fastinterface26.html), and [V2.7](http://www.braintechnology.de/braintechnology/en/usb_fastinterface27.html).

In sigrok, we use the open-source [fx2lafw](https://sigrok.org/wiki/Fx2lafw) firmware for this logic analyzer.

See [Braintechnology USB Interface V2.x/Info](https://sigrok.org/wiki/Braintechnology_USB_Interface_V2.x/Info) for some more details (such as **lsusb -vvv** output) on the device.

## Hardware
- **Main chip**: Cypress CY7C68013A-56PVXC (FX2LP)
- **64kB I2C EEPROM**: Microchip 24LC641
- **Low-dropout voltage regulator**: ST LD33
- **Crystal**: 24MHz
- **?**: PDEI

## Photos

<div class="photo-grid" markdown>

[![Braintechnology Usb Interface V2x Pdei](./img/Braintechnology_usb_interface_v2x_pdei.jpg)](./img/Braintechnology_usb_interface_v2x_pdei.jpg "Braintechnology Usb Interface V2x Pdei"){ .glightbox data-gallery="braintechnology-usb-interface-v2.x" }
<span class="caption">Braintechnology Usb Interface V2x Pdei</span>

[![Braintechnology Usb Interface V26](./img/Braintechnology_usb_interface_v26.png)](./img/Braintechnology_usb_interface_v26.png "Braintechnology Usb Interface V26"){ .glightbox data-gallery="braintechnology-usb-interface-v2.x" }
<span class="caption">Braintechnology Usb Interface V26</span>

[![Braintechnology Usb Interface V2x Pcb Front](./img/Braintechnology_usb_interface_v2x_pcb_front.jpg)](./img/Braintechnology_usb_interface_v2x_pcb_front.jpg "Braintechnology Usb Interface V2x Pcb Front"){ .glightbox data-gallery="braintechnology-usb-interface-v2.x" }
<span class="caption">Braintechnology Usb Interface V2x Pcb Front</span>

[![Braintechnology Usb Interface V2x Pcb Back](./img/Braintechnology_usb_interface_v2x_pcb_back.jpg)](./img/Braintechnology_usb_interface_v2x_pcb_back.jpg "Braintechnology Usb Interface V2x Pcb Back"){ .glightbox data-gallery="braintechnology-usb-interface-v2.x" }
<span class="caption">Braintechnology Usb Interface V2x Pcb Back</span>

[![Braintechnology Usb Interface V2x Fx2](./img/Braintechnology_usb_interface_v2x_fx2.jpg)](./img/Braintechnology_usb_interface_v2x_fx2.jpg "Braintechnology Usb Interface V2x Fx2"){ .glightbox data-gallery="braintechnology-usb-interface-v2.x" }
<span class="caption">Braintechnology Usb Interface V2x Fx2</span>

[![Braintechnology Usb Interface V2x Eeprom Ldo](./img/Braintechnology_usb_interface_v2x_eeprom_ldo.jpg)](./img/Braintechnology_usb_interface_v2x_eeprom_ldo.jpg "Braintechnology Usb Interface V2x Eeprom Ldo"){ .glightbox data-gallery="braintechnology-usb-interface-v2.x" }
<span class="caption">Braintechnology Usb Interface V2x Eeprom Ldo</span>

</div>
## Protocol

Since we use the open-source [fx2lafw](https://sigrok.org/wiki/Fx2lafw) firmware for this device, we don't need to know the protocol.

## Resources
- [Schematics](http://www.braintechnology.de/downstat18/download.php?file=schematicv27.pdf)
- [Various eval board documentation files](http://www.braintechnology.de/braintechnology/en/usb_fastinterface27.html)

