---
title: Saleae Logic8
---

# Saleae Logic8

<div class="infobox" markdown>

![Saleae Logic8](./img/Saleae_Logic8_case_top.jpg){ .infobox-image }

### Saleae Logic8

| | |
|---|---|
| **Status** | planned |
| **Channels** | 3/6/7/8 |
| **Samplerate** | 100/50/40/25 |
| **Samplerate (state)** | — |
| **Triggers** | none (SW-only) |
| **Min/max voltage** | 1.8V — 5.5V |
| **Threshold voltage** | VIH=1.2V, VIL=0.6V |
| **Memory** | ? |
| **Compression** | yes |
| **Price range** | $349 |
| **Website** | [saleae.com](http://www.saleae.com/) |

</div>

The **Saleae Logic8** is a USB-based, 8-channel logic analyzer with 100/50/40/25MHz sampling rate (at 3/6/7/8 enabled channels).

The case requires a **Torx T7** screwdriver to open.

See [Saleae Logic8/Info](https://sigrok.org/wiki/Saleae_Logic8/Info) for more details (such as lsusb -v output) about the device. 

## Hardware

These are provisional guesses, please correct if you spot errors, they are surely there.

- **FPGA**: [XILINIX Spartan-6](http://www.xilinx.com/products/silicon-devices/fpga/spartan-6.html) XC6SLX9 CSG225BIV1425 [Spartan-6 Family Overview](http://www.xilinx.com/support/documentation/data_sheets/ds160.pdf)
- **USB interface chip**: [Cypress CY7C66013A-56LTXC](http://www.cypress.com/?mpn=CY7C68013A-56LTXC) [datasheet](http://www.cypress.com/?docID=45142)
- [TI SN74LVC245A](http://www.ti.com/product/sn74lvc245a?qgpn=sn74lvc245a) 5.5V tolerant octal bus transceiver
- **Acquisition signal processing**: 6x [Analog Devices ADA4891-4](http://www.analog.com/static/imported-files/data_sheets/ADA4891-1_4891-2_4891-3_4891-4.PDF) quad amplifier
- **ADC**: [Hittite Microwave HMCAD1100](https://www.hittite.com/products/view.html/view/HMCAD1100) ([datasheet](https://www.hittite.com/content/documents/data_sheet/hmcad1100.pdf))
- **Unknown function**: MNAB / F26A
- This list not yet complete (EEPROM? Voltage regulation?)

## Photos

<div class="photo-grid" markdown>

[![Saleae Logic8 Case Top](./img/Saleae_Logic8_case_top.jpg)](./img/Saleae_Logic8_case_top.jpg "Saleae Logic8 Case Top"){ .glightbox data-gallery="saleae-logic8" }
<span class="caption">Saleae Logic8 Case Top</span>

[![Saleae Logic8 Board Bottom Upper Right](./img/Saleae_Logic8_board_bottom_upper_right.jpg)](./img/Saleae_Logic8_board_bottom_upper_right.jpg "Saleae Logic8 Board Bottom Upper Right"){ .glightbox data-gallery="saleae-logic8" }
<span class="caption">Saleae Logic8 Board Bottom Upper Right</span>

[![Saleae Logic8 Case Rear](./img/Saleae_Logic8_case_rear.jpg)](./img/Saleae_Logic8_case_rear.jpg "Saleae Logic8 Case Rear"){ .glightbox data-gallery="saleae-logic8" }
<span class="caption">Saleae Logic8 Case Rear</span>

[![Saleae Logic8 Case Bottom](./img/Saleae_Logic8_case_bottom.jpg)](./img/Saleae_Logic8_case_bottom.jpg "Saleae Logic8 Case Bottom"){ .glightbox data-gallery="saleae-logic8" }
<span class="caption">Saleae Logic8 Case Bottom</span>

[![Saleae Logic8 Board Top Upper](./img/Saleae_Logic8_board_top_upper.jpg)](./img/Saleae_Logic8_board_top_upper.jpg "Saleae Logic8 Board Top Upper"){ .glightbox data-gallery="saleae-logic8" }
<span class="caption">Saleae Logic8 Board Top Upper</span>

[![Saleae Logic8 Board Bottom](./img/Saleae_Logic8_board_bottom.jpg)](./img/Saleae_Logic8_board_bottom.jpg "Saleae Logic8 Board Bottom"){ .glightbox data-gallery="saleae-logic8" }
<span class="caption">Saleae Logic8 Board Bottom</span>

[![Saleae Logic8 Board Top](./img/Saleae_Logic8_board_top.jpg)](./img/Saleae_Logic8_board_top.jpg "Saleae Logic8 Board Top"){ .glightbox data-gallery="saleae-logic8" }
<span class="caption">Saleae Logic8 Board Top</span>

</div>
## Resources
- [Manual / Getting started](http://support.saleae.com/hc/en-us/sections/200114124-get-started-using-the-saleae-logic-analyzer)
- [Vendor software](http://www.saleae.com/downloads)
- [SDKs](http://support.saleae.com/hc/en-us/categories/200077184-sdks-automation-betas)

