---
title: CWAV USBee SX
---

# CWAV USBee SX

<div class="infobox" markdown>

![CWAV USBee SX](./img/Cwav_usbee_sx.png){ .infobox-image }

### CWAV USBee SX

| | |
|---|---|
| **Status** | supported |
| **Source code** | [fx2lafw](https://github.com/OpenTraceLab/OpenTraceCapture/tree/main/src/hardware/fx2lafw) |
| **Channels** | 8 |
| **Samplerate** | 24MHz |
| **Samplerate (state)** | — |
| **Triggers** | none (SW-only) |
| **Min/max voltage** | max. 5.5V |
| **Threshold voltage** | Fixed: VIH=1.4V, VIL=0.8V |
| **Memory** | none |
| **Compression** | none |
| **Price range** | $130 |
| **Website** | [usbee.com](http://usbee.com/sx.html) |

</div>

The **USBee SX** is a USB-based, 8-channel logic analyzer (and signal generator) with up to 24MHz sampling rate.

In sigrok, we use the open-source [fx2lafw](https://sigrok.org/wiki/Fx2lafw) firmware for this logic analyzer.

See [CWAV USBee SX/Info](https://sigrok.org/wiki/CWAV_USBee_SX/Info) for some more details (such as **lsusb -vvv** output) on the device.

CWAV, Inc. [has been closed and no longer sells](http://usbee.com/company.htm) the USBee test pods (has chosen to go out of business effective September 10, 2015). But there are a lot of clones, like [MCU123 USBee AX Pro clone](https://sigrok.org/wiki/MCU123_USBee_AX_Pro_clone). Just search for **24mhz 8ch logic analyzer** on [http://ebay.com/](http://ebay.com/) or [http://aliexpress.com/](http://aliexpress.com/) for one (usually under $10).

## Hardware
- **Main chip**: Cypress CY7C68013A-56PVXC (FX2LP)
**Note:** Older versions used the Cypress CY7C68013-56PVC (FX2), which is different in some ways (e.g. less SRAM)
- **3.3V voltage regulator**: ST LD33
- **I2C EEPROM**: Microchip 24LC01B
- **Crystal**: 24MHz

## Photos

<div class="photo-grid" markdown>

[![Cwav Usbee Sx](./img/Cwav_usbee_sx.png)](./img/Cwav_usbee_sx.png "Cwav Usbee Sx"){ .glightbox data-gallery="cwav-usbee-sx" }
<span class="caption">Cwav Usbee Sx</span>

[![Cwav Usbee Sx Device Bottom](./img/Cwav_usbee_sx_device_bottom.jpg)](./img/Cwav_usbee_sx_device_bottom.jpg "Cwav Usbee Sx Device Bottom"){ .glightbox data-gallery="cwav-usbee-sx" }
<span class="caption">Cwav Usbee Sx Device Bottom</span>

[![Cwav Usbee Sx Revision Zx](./img/Cwav_usbee_sx_revision_zx.jpg)](./img/Cwav_usbee_sx_revision_zx.jpg "Cwav Usbee Sx Revision Zx"){ .glightbox data-gallery="cwav-usbee-sx" }
<span class="caption">Cwav Usbee Sx Revision Zx</span>

[![Cwav Usbee Sx Device Top](./img/Cwav_usbee_sx_device_top.jpg)](./img/Cwav_usbee_sx_device_top.jpg "Cwav Usbee Sx Device Top"){ .glightbox data-gallery="cwav-usbee-sx" }
<span class="caption">Cwav Usbee Sx Device Top</span>

[![Usbee Sx Case Back](./img/Usbee_sx_case_back.jpg)](./img/Usbee_sx_case_back.jpg "Usbee Sx Case Back"){ .glightbox data-gallery="cwav-usbee-sx" }
<span class="caption">Usbee Sx Case Back</span>

[![Cwav Usbee Sx](./img/Cwav_usbee_sx.jpg)](./img/Cwav_usbee_sx.jpg "Cwav Usbee Sx"){ .glightbox data-gallery="cwav-usbee-sx" }
<span class="caption">Cwav Usbee Sx</span>

[![Cwav Usbee Sx Pcb Top](./img/Cwav_usbee_sx_pcb_top.jpg)](./img/Cwav_usbee_sx_pcb_top.jpg "Cwav Usbee Sx Pcb Top"){ .glightbox data-gallery="cwav-usbee-sx" }
<span class="caption">Cwav Usbee Sx Pcb Top</span>

[![Usbee Sx Pcb Back](./img/Usbee_sx_pcb_back.jpg)](./img/Usbee_sx_pcb_back.jpg "Usbee Sx Pcb Back"){ .glightbox data-gallery="cwav-usbee-sx" }
<span class="caption">Usbee Sx Pcb Back</span>

[![Cwav Usbee Sx Pcb Bottom](./img/Cwav_usbee_sx_pcb_bottom.jpg)](./img/Cwav_usbee_sx_pcb_bottom.jpg "Cwav Usbee Sx Pcb Bottom"){ .glightbox data-gallery="cwav-usbee-sx" }
<span class="caption">Cwav Usbee Sx Pcb Bottom</span>

[![Usbee Sx Pcb Front](./img/Usbee_sx_pcb_front.jpg)](./img/Usbee_sx_pcb_front.jpg "Usbee Sx Pcb Front"){ .glightbox data-gallery="cwav-usbee-sx" }
<span class="caption">Usbee Sx Pcb Front</span>

[![Usbee Sx Case Open](./img/Usbee_sx_case_open.jpg)](./img/Usbee_sx_case_open.jpg "Usbee Sx Case Open"){ .glightbox data-gallery="cwav-usbee-sx" }
<span class="caption">Usbee Sx Case Open</span>

</div>
## Protocol

Since we use the open-source [fx2lafw](https://sigrok.org/wiki/Fx2lafw) firmware for this device, we don't need to know the protocol.

However, for those interested in this, someone else has already [decoded most of it](https://blog.visucore.com/tags/usbee).

## Resources
- [USBee SX help files](http://usbee.com/software/ZXHelpFiles.zip)
- [USBee Suite manual](http://usbee.com/usbeesuitemanual.pdf)
- [Vendor software](http://usbee.com/usbeesuitesw.zip)
- [Visucore Blog: JTAG using USBee SX](https://blog.visucore.com/2010/5/23/jtag-using-cypress-fx2-usb)
- [Visucore Blog: PWM on the USBee with custom firmware](https://blog.visucore.com/2010/5/28/pwm-on-the-usbee-hardware-using-custom-firmware)

