---
title: Braintechnology USB-LPS
---

# Braintechnology USB-LPS

<div class="infobox" markdown>

![Braintechnology USB-LPS](./img/Braintechnology_usb_lps.jpg){ .infobox-image }

### Braintechnology USB-LPS

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
| **Website** | [braintechnology.de](http://www.braintechnology.de/webshop/catalog/product_info.php?&amp;products_id=105) |

</div>

The **Braintechnology USB-LPS** is a Cypress FX2 based 16-channel, 24MHz, USB-based logic analyzer and signal/pattern generator.

In sigrok, the open-source [fx2lafw](https://sigrok.org/wiki/Fx2lafw) firmware and driver is used for this device.

See [Braintechnology USB-LPS/Info](https://sigrok.org/wiki/Braintechnology_USB-LPS/Info) for some more details (such as **lsusb -v** output) on the device.

## Hardware
- **Main chip:** Cypress CY7C68013A-56PVXC (FX2LP)
- **I²C EEPROM**: Atmel ATtiny13-20SU
- **3.3V voltage regulator**: LD33
- **Crystal**: 24MHz

## Photos

<div class="photo-grid" markdown>

[![Braintechnology Usb Lps](./img/Braintechnology_usb_lps.jpg)](./img/Braintechnology_usb_lps.jpg "Braintechnology Usb Lps"){ .glightbox data-gallery="braintechnology-usb-lps" }
<span class="caption">Braintechnology Usb Lps</span>

[![Braintechnology Usb Lps Pcb Front](./img/Braintechnology_usb_lps_pcb_front.jpg)](./img/Braintechnology_usb_lps_pcb_front.jpg "Braintechnology Usb Lps Pcb Front"){ .glightbox data-gallery="braintechnology-usb-lps" }
<span class="caption">Braintechnology Usb Lps Pcb Front</span>

[![Braintechnology Usb Lps](./img/Braintechnology_usb_lps.png)](./img/Braintechnology_usb_lps.png "Braintechnology Usb Lps"){ .glightbox data-gallery="braintechnology-usb-lps" }
<span class="caption">Braintechnology Usb Lps</span>

[![Braintechnology Usb Lps Pcb Back](./img/Braintechnology_usb_lps_pcb_back.jpg)](./img/Braintechnology_usb_lps_pcb_back.jpg "Braintechnology Usb Lps Pcb Back"){ .glightbox data-gallery="braintechnology-usb-lps" }
<span class="caption">Braintechnology Usb Lps Pcb Back</span>

[![Braintechnology Usb Lps Pcb Front Details](./img/Braintechnology_usb_lps_pcb_front_details.jpg)](./img/Braintechnology_usb_lps_pcb_front_details.jpg "Braintechnology Usb Lps Pcb Front Details"){ .glightbox data-gallery="braintechnology-usb-lps" }
<span class="caption">Braintechnology Usb Lps Pcb Front Details</span>

</div>
## Protocol

Since we use the open-source [fx2lafw](https://sigrok.org/wiki/Fx2lafw) firmware for this device, we don't need to know the protocol.

However, for those interested in this, see our old [vendor protocol docs](https://sigrok.org/wiki/Braintechnology_USB-LPS/Info#Vendor_USB_protocol).

## Resources
- [Manual](http://www.braintechnology.de/downstat18/download.php?file=lps_doc.pdf)
- [Vendor software](http://www.braintechnology.de/downstat18/download.php?file=lpssetup10723.exe)
- [Driver](http://www.braintechnology.de/downstat18/download.php?file=lpsdriver_32_64bit.zip)

