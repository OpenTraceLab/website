---
title: WayEngineer Saleae16
---

# WayEngineer Saleae16

<div class="infobox" markdown>

![WayEngineer Saleae16](./img/Wayengineer_saleae16_ams1117_33.jpg){ .infobox-image }

### WayEngineer Saleae16

| | |
|---|---|
| **Status** | supported |
| **Source code** | [saleae-logic16](https://github.com/OpenTraceLab/OpenTraceCapture/tree/main/src/hardware/saleae-logic16) |
| **Channels** | 3/6/9/16 |
| **Samplerate** | 100/50/32/16MHz |
| **Samplerate (state)** | — |
| **Triggers** | none (SW-only) |
| **Min/max voltage** | -0.9V — 6V |
| **Threshold voltage** | configurable:for 1.8V to 3.6V systems: VIH=1.4V, VIL=0.7Vfor 5V systems: VIH=3.6V, VIL=1.4V |
| **Memory** | none |
| **Compression** | yes |
| **Website** | [wayengineer.com](https://web.archive.org/web/20161229025314/http://www.wayengineer.com/index.php?main_page=product_info&amp;products_id=4747) |

</div>

The **WayEngineer Saleae16** is a USB-based, 16-channel logic analyzer with 100/50/32/16MHz sampling rate (at 3/6/9/16 enabled channels).

This is a clone of the [Saleae Logic16](https://sigrok.org/wiki/Saleae_Logic16).

See [WayEngineer Saleae16/Info](https://sigrok.org/wiki/WayEngineer_Saleae16/Info) for more details (such as **lsusb -v** output) about the device.

## Hardware
- **FPGA**: [Xilinx Spartan-3A XC3S200A](http://www.xilinx.com/support/index.html/content/xilinx/en/supportNav/silicon_devices/fpga/spartan-3a.html), 200K gates ([datasheeet](http://www.xilinx.com/support/documentation/data_sheets/ds529.pdf))
- **USB interface chip**: [Cypress CY7C68013A-56LTXC (FX2LP)](http://www.cypress.com/?mpn=CY7C68013A-56LTXC) ([datasheet](http://www.cypress.com/?docID=45142))
- **I²C EEPROM**: [Atmel 24C02N](http://www.atmel.com/devices/at24c02.aspx) (markings: "ATMEL142 24C02N SU27 D") ([datasheet](http://www.atmel.com/Images/doc3256.pdf))
- **3.3V voltage regulator**: [Advanced Monolithic Systems AMS1117-3.3](http://www.advanced-monolithic.com/products/voltreg.html#1117) ([datasheet](http://ams-semitech.com/attachments/File/AMS1117_20120314.pdf), [older datasheet](http://www.advanced-monolithic.com/pdf/ds1117.pdf))
- **1.2V voltage regulator**: [Advanced Monolithic Systems AMS1117-1.2](http://www.advanced-monolithic.com/products/voltreg.html#1117) ([datasheet](http://ams-semitech.com/attachments/File/AMS1117_20120314.pdf), [older datasheet](http://www.advanced-monolithic.com/pdf/ds1117.pdf))
- **Crystal:** 24.000

## Photos

<div class="photo-grid" markdown>

[![Wayengineer Saleae16 Ams1117 33](./img/Wayengineer_saleae16_ams1117_33.jpg)](./img/Wayengineer_saleae16_ams1117_33.jpg "Wayengineer Saleae16 Ams1117 33"){ .glightbox data-gallery="wayengineer-saleae16" }
<span class="caption">Wayengineer Saleae16 Ams1117 33</span>

[![Wayengineer Saleae16 Ams1117 12](./img/Wayengineer_saleae16_ams1117_12.jpg)](./img/Wayengineer_saleae16_ams1117_12.jpg "Wayengineer Saleae16 Ams1117 12"){ .glightbox data-gallery="wayengineer-saleae16" }
<span class="caption">Wayengineer Saleae16 Ams1117 12</span>

[![Wayengineer Saleae16 Pcb Top](./img/Wayengineer_saleae16_pcb_top.jpg)](./img/Wayengineer_saleae16_pcb_top.jpg "Wayengineer Saleae16 Pcb Top"){ .glightbox data-gallery="wayengineer-saleae16" }
<span class="caption">Wayengineer Saleae16 Pcb Top</span>

[![Wayengineer Saleae16](./img/Wayengineer_saleae16.jpg)](./img/Wayengineer_saleae16.png "Wayengineer Saleae16"){ .glightbox data-gallery="wayengineer-saleae16" }
<span class="caption">Wayengineer Saleae16</span>

[![Wayengineer Saleae16 Device Usb](./img/Wayengineer_saleae16_device_usb.jpg)](./img/Wayengineer_saleae16_device_usb.jpg "Wayengineer Saleae16 Device Usb"){ .glightbox data-gallery="wayengineer-saleae16" }
<span class="caption">Wayengineer Saleae16 Device Usb</span>

[![Wayengineer16 Board Top 2014 09](./img/WayEngineer16-board-top-2014-09.jpg)](./img/WayEngineer16-board-top-2014-09.jpg "Wayengineer16 Board Top 2014 09"){ .glightbox data-gallery="wayengineer-saleae16" }
<span class="caption">Wayengineer16 Board Top 2014 09</span>

[![Wayengineer Saleae16 Input Stage](./img/Wayengineer_saleae16_input_stage.jpg)](./img/Wayengineer_saleae16_input_stage.jpg "Wayengineer Saleae16 Input Stage"){ .glightbox data-gallery="wayengineer-saleae16" }
<span class="caption">Wayengineer Saleae16 Input Stage</span>

[![Wayengineer Saleae16 Device Bottom](./img/Wayengineer_saleae16_device_bottom.jpg)](./img/Wayengineer_saleae16_device_bottom.jpg "Wayengineer Saleae16 Device Bottom"){ .glightbox data-gallery="wayengineer-saleae16" }
<span class="caption">Wayengineer Saleae16 Device Bottom</span>

[![Wayengineer Saleae16 Device With Cable](./img/Wayengineer_saleae16_device_with_cable.jpg)](./img/Wayengineer_saleae16_device_with_cable.jpg "Wayengineer Saleae16 Device With Cable"){ .glightbox data-gallery="wayengineer-saleae16" }
<span class="caption">Wayengineer Saleae16 Device With Cable</span>

[![Wayengineer Saleae16 Pcb Bottom](./img/Wayengineer_saleae16_pcb_bottom.jpg)](./img/Wayengineer_saleae16_pcb_bottom.jpg "Wayengineer Saleae16 Pcb Bottom"){ .glightbox data-gallery="wayengineer-saleae16" }
<span class="caption">Wayengineer Saleae16 Pcb Bottom</span>

[![Wayengineer Saleae16 Atmel 24c02n](./img/Wayengineer_saleae16_atmel_24c02n.jpg)](./img/Wayengineer_saleae16_atmel_24c02n.jpg "Wayengineer Saleae16 Atmel 24c02n"){ .glightbox data-gallery="wayengineer-saleae16" }
<span class="caption">Wayengineer Saleae16 Atmel 24c02n</span>

[![Wayengineer Saleae16 Fx2lp](./img/Wayengineer_saleae16_FX2LP.jpg)](./img/Wayengineer_saleae16_FX2LP.jpg "Wayengineer Saleae16 Fx2lp"){ .glightbox data-gallery="wayengineer-saleae16" }
<span class="caption">Wayengineer Saleae16 Fx2lp</span>

[![Wayengineer Saleae16 Device Top](./img/Wayengineer_saleae16_device_top.jpg)](./img/Wayengineer_saleae16_device_top.jpg "Wayengineer Saleae16 Device Top"){ .glightbox data-gallery="wayengineer-saleae16" }
<span class="caption">Wayengineer Saleae16 Device Top</span>

[![Wayengineer Saleae16 Package Contents](./img/Wayengineer_saleae16_package_contents.jpg)](./img/Wayengineer_saleae16_package_contents.jpg "Wayengineer Saleae16 Package Contents"){ .glightbox data-gallery="wayengineer-saleae16" }
<span class="caption">Wayengineer Saleae16 Package Contents</span>

[![Wayengineer Saleae16 Device Connector](./img/Wayengineer_saleae16_device_connector.jpg)](./img/Wayengineer_saleae16_device_connector.jpg "Wayengineer Saleae16 Device Connector"){ .glightbox data-gallery="wayengineer-saleae16" }
<span class="caption">Wayengineer Saleae16 Device Connector</span>

[![Wayengineer Saleae16 Xc3s200a](./img/Wayengineer_saleae16_XC3S200A.jpg)](./img/Wayengineer_saleae16_XC3S200A.jpg "Wayengineer Saleae16 Xc3s200a"){ .glightbox data-gallery="wayengineer-saleae16" }
<span class="caption">Wayengineer Saleae16 Xc3s200a</span>

</div>
## Firmware

See [Saleae_Logic16#Firmware](https://sigrok.org/wiki/Saleae_Logic16#Firmware).

## Protocol

See [Saleae_Logic16#Protocol](https://sigrok.org/wiki/Saleae_Logic16#Protocol).

## Resources
- [AliExpress entry #1](http://www.aliexpress.com/item/1pcs-lot-Free-shipping-New-Arrival-Saleae-Logic16-saleae16-USB-Logic-Analyzer-100M-16CH-best-quality/667671473.html)

