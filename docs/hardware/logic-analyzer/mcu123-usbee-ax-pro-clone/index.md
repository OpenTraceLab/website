---
title: MCU123 USBee AX Pro clone
---

# MCU123 USBee AX Pro clone

<div class="infobox" markdown>

![MCU123 USBee AX Pro clone](./img/Usbee_ax_clone_angle.jpg){ .infobox-image }

### MCU123 USBee AX Pro clone

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
| **Website** | [dx.com](http://dx.com/p/logic-analyzer-w-dupont-lines-and-usb-cable-for-scm-black-148945) |

</div>

The **MCU123 USBee AX Pro clone** is a USB-based, 8-channel logic analyzer with up to 24MHz sampling rate.

It is a clone of the [CWAV USBee AX-Pro](/w/index.php?title=CWAV_USBee_AX-Pro&action=edit&redlink=1), but it doesn't have analog (only 8-channel digital) sampling capabilities. It's also *very* similar to the [MCU123 Saleae Logic clone](https://sigrok.org/wiki/MCU123_Saleae_Logic_clone) minus the different USB vendor/device IDs.

In sigrok, we use the open-source [fx2lafw](https://sigrok.org/wiki/Fx2lafw) firmware for this logic analyzer.

See [MCU123 USBee AX Pro clone/Info](https://sigrok.org/wiki/MCU123_USBee_AX_Pro_clone/Info) for more detailed information on the device.

## Hardware
- **Main chip**: Cypress CY7C68013A-56PVXC (FX2LP)
- **Input buffer**: NXP 74HC245 (markings: "NXP HC245 2A7K508 UnD2 18E")
- **256-byte I2C EEPROM**: Atmel AT24C02 (markings: "ATMEL218 24C02N SU27 D")
- **3.3V low-dropout voltage regulator**: Advanced Monolithic Systems AMS1117-3.3 (markings: "AMS1117 3.3 HT240E")
- **24MHz crystal**: 24.000

## Photos

<div class="photo-grid" markdown>

[![Usbee Ax Clone Angle](./img/Usbee_ax_clone_angle.jpg)](./img/Usbee_ax_clone_angle.jpg "Usbee Ax Clone Angle"){ .glightbox data-gallery="mcu123-usbee-ax-pro-clone" }
<span class="caption">Usbee Ax Clone Angle</span>

[![Usbee Ax Clone Front](./img/Usbee_ax_clone_front.jpg)](./img/Usbee_ax_clone_front.png "Usbee Ax Clone Front"){ .glightbox data-gallery="mcu123-usbee-ax-pro-clone" }
<span class="caption">Usbee Ax Clone Front</span>

[![Usbee Ax Clone Back](./img/Usbee_ax_clone_back.jpg)](./img/Usbee_ax_clone_back.jpg "Usbee Ax Clone Back"){ .glightbox data-gallery="mcu123-usbee-ax-pro-clone" }
<span class="caption">Usbee Ax Clone Back</span>

[![Usbee Ax Clone Opened](./img/Usbee_ax_clone_opened.jpg)](./img/Usbee_ax_clone_opened.jpg "Usbee Ax Clone Opened"){ .glightbox data-gallery="mcu123-usbee-ax-pro-clone" }
<span class="caption">Usbee Ax Clone Opened</span>

[![Usbee Ax Clone Pcb Front](./img/Usbee_ax_clone_pcb_front.jpg)](./img/Usbee_ax_clone_pcb_front.jpg "Usbee Ax Clone Pcb Front"){ .glightbox data-gallery="mcu123-usbee-ax-pro-clone" }
<span class="caption">Usbee Ax Clone Pcb Front</span>

[![Usbee Ax Clone Pcb Back](./img/Usbee_ax_clone_pcb_back.jpg)](./img/Usbee_ax_clone_pcb_back.jpg "Usbee Ax Clone Pcb Back"){ .glightbox data-gallery="mcu123-usbee-ax-pro-clone" }
<span class="caption">Usbee Ax Clone Pcb Back</span>

</div>
## Protocol

Since we use the open-source [fx2lafw](https://sigrok.org/wiki/Fx2lafw) firmware for this device, we don't need to know the protocol.

## Resources
- [DealExtreme online shop](http://dx.com/p/logic-analyzer-w-dupont-lines-and-usb-cable-for-scm-black-148945)

