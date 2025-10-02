---
title: mcupro Logic16 clone
---

# mcupro Logic16 clone

<div class="infobox" markdown>

![mcupro Logic16 clone](./img/IMG_0207_v1.JPG){ .infobox-image }

### mcupro Logic16 clone

| | |
|---|---|
| **Status** | supported |
| **Source code** | [saleae-logic16](https://github.com/OpenTraceLab/OpenTraceCapture/tree/main/src/hardware/saleae-logic16) |
| **Channels** | 3/6/9/16 |
| **Samplerate** | 100/50/32/16MHz |
| **Samplerate (state)** | — |
| **Triggers** | none (SW-only) |
| **Min/max voltage** | -0.9V — 6V |
| **Threshold voltage** | 1.5V (operates with 3.3V logic) |
| **Memory** | none |
| **Compression** | yes |
| **Price range** | $30 - $35 |
| **Website** | [aliexpress.com](https://www.aliexpress.com/item/new-USB-Logic-100MHz-16Ch-Logic-Analyzer-for-ARM-FPGA-E4-004/32931358747.html) |

</div>

The **mcupro Logic16 clone** is a USB-based, 16-channel logic analyzer with 100/50/32/16MHz sampling rate (at 3/6/9/16 enabled channels).

This is a clone of the [Saleae Logic16](https://sigrok.org/wiki/Saleae_Logic16).

See [mcupro Logic16 clone/Info](https://sigrok.org/wiki/Mcupro_Logic16_clone/Info) for more details (such as **lsusb -v** output) about the device.

## Hardware (Actel variant)

The PCB is marked "Saleae16 v4.6 By mcupro".

- **FPGA**: [Actel A3P125](https://www.actel.com/documents/PA3_DS.pdf)
- **USB interface chip**: [Cypress CY7C68013A](http://www.cypress.com/?docID=45142)
- **I²C EEPROM**: [Atmel 24C02N](http://www.atmel.com/Images/doc3256.pdf)
- **3.3V voltage regulator**: [Advanced Monolithic Systems AMS1117-3.3](http://ams-semitech.com/attachments/File/AMS1117_20120314.pdf)
- **1.5V voltage regulator**: [Advanced Monolithic Systems AMS1117-1.5](http://ams-semitech.com/attachments/File/AMS1117_20120314.pdf)
- **Crystal**: 24MHz
## Hardware (Cyclone variant)

The PCB doesn't have any identifying markings.

- **FPGA**: [Altera Cyclone EP1C3T100](https://www.altera.com/products/fpga/cyclone-series/cyclone/support.html#Cyclone-Device-Handbook--All-Sections-)
- **USB interface chip**: [Cypress CY7C68013A](http://www.cypress.com/?docID=45142)
- **I²C EEPROM**: [Atmel 24C02N](http://www.atmel.com/Images/doc3256.pdf)
- **3.3V voltage regulator**: [Advanced Monolithic Systems AMS1117-3.3](http://ams-semitech.com/attachments/File/AMS1117_20120314.pdf)
- **1.5V voltage regulator**: [Advanced Monolithic Systems AMS1117-1.5](http://ams-semitech.com/attachments/File/AMS1117_20120314.pdf)
- **Crystal (FX2)**: 24MHz
- **Crystal (FPGA)**: 100MHz
- **FPGA bitstream**: ST M25P10VP, 1Mbit SPI NOR flash ([datasheet](https://cdn.datasheetspdf.com/pdf-down/2/5/P/25P10VP-STMicroelectronics.pdf))
- **Bootstrap controller**: [STCMCU 15F10](http://www.stcmcu.com/datasheet/stc/STC-AD-PDF/STC15.pdf), 8051 compatible
## Hardware (2018 variant)

The PCB is marked "Logic 16 Saleae". This variant also comes in a case identical to the [Noname_XL-LOGIC16-100M](https://sigrok.org/wiki/Noname_XL-LOGIC16-100M).

- **FPGA**: Markings ground off, but pinout indicates an Altera Cyclone EP1C3T144.
- **USB interface chip**: [Cypress CY7C68013A](http://www.cypress.com/?docID=45142)
- **I²C EEPROM**: Markings ground off
- **3.3V voltage regulator**: [TD 6810](http://www.techcodesemi.com/cn/products_info.asp?pid=26) adjustable version + 150k/680k resistors pair
- **1.5V voltage regulator**: [TD 6810](http://www.techcodesemi.com/cn/products_info.asp?pid=26) adjustable version + 160k/240k resistors pair
- **Crystal (FX2)**: 24MHz
- **Crystal (FPGA)**: 32MHz
- **FPGA bitstream**: ST M25P10VP, 1Mbit SPI NOR flash ([datasheet](https://cdn.datasheetspdf.com/pdf-down/2/5/P/25P10VP-STMicroelectronics.pdf))
- **Bootstrap controller**: Not required?
## Hardware (2015-01-08 variant)

The PCB is marked "Saleae Logic 16 By MCUPro 2015-1-8". Readily identifiable by the irregular PCB traces, and switching power supplies. This comes in a different case, identical to the [Noname_XL-LOGIC16-100M](https://sigrok.org/wiki/Noname_XL-LOGIC16-100M).

- **FPGA**: Markings ground off
- **USB interface chip**: [Cypress CY7C68013A](http://www.cypress.com/?docID=45142)
- **I²C EEPROM**: Markings ground off
- **3.3V voltage regulator**: [TD 6810](http://www.techcodesemi.com/cn/products_info.asp?pid=26) adjustable version + 150k/680k resistors pair
- **1.5V voltage regulator**: [TD 6810](http://www.techcodesemi.com/cn/products_info.asp?pid=26) adjustable version + 160k/240k resistors pair
- **Crystal (FX2)**: 24MHz
- **Crystal (FPGA)**: Looks like 32MHz?
- **FPGA bitstream**: ST M25P10VP, 1Mbit SPI NOR flash ([datasheet](https://cdn.datasheetspdf.com/pdf-down/2/5/P/25P10VP-STMicroelectronics.pdf))
- **Bootstrap controller**: Not required?
## Hardware (2014-01-25 variant)

The PCB is marked "Saleae Logic 16 mcupro 2014.1.25".

The bottom two channels are not GND, but SCK (sample clock out) and HCK (half of SCK out).

- **FPGA**: Markings ground off, but pinout and JTAG (IDCODE 0x020810dd) indicate an Altera Cyclone EP1C3T100.
- **USB interface chip**: Markings sometimes ground off? Cypress CY7C68013A
- **Crystal (FX2)**: marked "DKF 24.000"
- **Crystal (FPGA)**: marked "RAK32.00"
- **FPGA bitstream**: ST M25P10VP, 1Mbit SPI NOR flash ([datasheet](https://cdn.datasheetspdf.com/pdf-down/2/5/P/25P10VP-STMicroelectronics.pdf))
- **I²C EEPROM**: None? (CY7C68013A I2C port wired to FPGA pins)
- **Bootstrap controller**: Markings ground off, pinout could indicate a [STCMCU 15F10x](http://www.stcmcu.com/datasheet/stc/STC-AD-PDF/STC15.pdf) 8051-based MCU?
- **3.3V voltage regulator**: unknown switching regulator (marked "IC5CJ"&#160;?) + 150k/680k resistors pair
- **1.5V voltage regulator**: unknown switching regulator (marked "IC5CJ"&#160;?) + 160k/240k resistors pair
- **Channel input buffering**: none, only simple resistor (510R) + TVS diode array protection (possibly [Semtech SRV05](http://www.semtech.com/images/datasheet/srv05-4.pdf))

## Photos

<div class="photo-grid" markdown>

[![Img 0207 V1](./img/IMG_0207_v1.JPG)](./img/IMG_0207_v1.JPG "Img 0207 V1"){ .glightbox data-gallery="mcupro-logic16-clone" }
<span class="caption">Img 0207 V1</span>

[![Mcupro 2014 1 25 Top Overview](./img/Mcupro-2014-1-25-top-overview.jpg)](./img/Mcupro-2014-1-25-top-overview.jpg "Mcupro 2014 1 25 Top Overview"){ .glightbox data-gallery="mcupro-logic16-clone" }
<span class="caption">Mcupro 2014 1 25 Top Overview</span>

[![Mcupro 2015 1 8 Voltage Regulators](./img/Mcupro-2015-1-8-voltage-regulators.jpg)](./img/Mcupro-2015-1-8-voltage-regulators.jpg "Mcupro 2015 1 8 Voltage Regulators"){ .glightbox data-gallery="mcupro-logic16-clone" }
<span class="caption">Mcupro 2015 1 8 Voltage Regulators</span>

[![Mcupro 2018 Back](./img/Mcupro-2018-back.jpg)](./img/Mcupro-2018-back.jpg "Mcupro 2018 Back"){ .glightbox data-gallery="mcupro-logic16-clone" }
<span class="caption">Mcupro 2018 Back</span>

[![Seleae Logic16 Aliexpress Clone](./img/Seleae-logic16-aliexpress-clone.jpg)](./img/Seleae-logic16-aliexpress-clone.jpg "Seleae Logic16 Aliexpress Clone"){ .glightbox data-gallery="mcupro-logic16-clone" }
<span class="caption">Seleae Logic16 Aliexpress Clone</span>

[![Mcupro 2015 1 8 Top Overview](./img/Mcupro-2015-1-8-top-overview.jpg)](./img/Mcupro-2015-1-8-top-overview.jpg "Mcupro 2015 1 8 Top Overview"){ .glightbox data-gallery="mcupro-logic16-clone" }
<span class="caption">Mcupro 2015 1 8 Top Overview</span>

[![Mcupro 2015 1 8 Bottom Overview](./img/Mcupro-2015-1-8-bottom-overview.jpg)](./img/Mcupro-2015-1-8-bottom-overview.jpg "Mcupro 2015 1 8 Bottom Overview"){ .glightbox data-gallery="mcupro-logic16-clone" }
<span class="caption">Mcupro 2015 1 8 Bottom Overview</span>

[![Mcupro 2018 Case](./img/Mcupro-2018-case.jpg)](./img/Mcupro-2018-case.jpg "Mcupro 2018 Case"){ .glightbox data-gallery="mcupro-logic16-clone" }
<span class="caption">Mcupro 2018 Case</span>

[![Mcupro 2015 1 8 Bottom Markings Intact](./img/Mcupro-2015-1-8-bottom-markings-intact.jpg)](./img/Mcupro-2015-1-8-bottom-markings-intact.jpg "Mcupro 2015 1 8 Bottom Markings Intact"){ .glightbox data-gallery="mcupro-logic16-clone" }
<span class="caption">Mcupro 2015 1 8 Bottom Markings Intact</span>

[![Xl Logic16 100m External](./img/Xl-logic16-100m-external.jpg)](./img/Xl-logic16-100m-external.jpg "Xl Logic16 100m External"){ .glightbox data-gallery="mcupro-logic16-clone" }
<span class="caption">Xl Logic16 100m External</span>

[![Mcupro Logic16 Variant2 Top Flash 2buc](./img/Mcupro_Logic16_Variant2_top_flash_2BuC.jpg)](./img/Mcupro_Logic16_Variant2_top_flash_2BuC.jpg "Mcupro Logic16 Variant2 Top Flash 2buc"){ .glightbox data-gallery="mcupro-logic16-clone" }
<span class="caption">Mcupro Logic16 Variant2 Top Flash 2buc</span>

[![Mcupro Logic16 Overview](./img/Mcupro_Logic16_overview.jpg)](./img/Mcupro_Logic16_overview.png "Mcupro Logic16 Overview"){ .glightbox data-gallery="mcupro-logic16-clone" }
<span class="caption">Mcupro Logic16 Overview</span>

[![Mcupro 2014 1 25 Bottom Overview](./img/Mcupro-2014-1-25-bottom-overview.jpg)](./img/Mcupro-2014-1-25-bottom-overview.jpg "Mcupro 2014 1 25 Bottom Overview"){ .glightbox data-gallery="mcupro-logic16-clone" }
<span class="caption">Mcupro 2014 1 25 Bottom Overview</span>

[![Mcupro 2014 1 25 Bottom Ortho](./img/Mcupro-2014-1-25-bottom_ortho.jpg)](./img/Mcupro-2014-1-25-bottom_ortho.jpg "Mcupro 2014 1 25 Bottom Ortho"){ .glightbox data-gallery="mcupro-logic16-clone" }
<span class="caption">Mcupro 2014 1 25 Bottom Ortho</span>

[![Mcupro 2014 1 25 Top Ortho](./img/Mcupro-2014-1-25-top_ortho.jpg)](./img/Mcupro-2014-1-25-top_ortho.jpg "Mcupro 2014 1 25 Top Ortho"){ .glightbox data-gallery="mcupro-logic16-clone" }
<span class="caption">Mcupro 2014 1 25 Top Ortho</span>

[![Mcupro Logic16 Variant2 Top](./img/Mcupro_Logic16_Variant2_top.jpg)](./img/Mcupro_Logic16_Variant2_top.jpg "Mcupro Logic16 Variant2 Top"){ .glightbox data-gallery="mcupro-logic16-clone" }
<span class="caption">Mcupro Logic16 Variant2 Top</span>

[![Mcupro 2018 Front](./img/Mcupro-2018-front.jpg)](./img/Mcupro-2018-front.jpg "Mcupro 2018 Front"){ .glightbox data-gallery="mcupro-logic16-clone" }
<span class="caption">Mcupro 2018 Front</span>

</div>

## Photos

<div class="photo-grid" markdown>

[![Img 0207 V1](./img/IMG_0207_v1.JPG)](./img/IMG_0207_v1.JPG "Img 0207 V1"){ .glightbox data-gallery="mcupro-logic16-clone" }
<span class="caption">Img 0207 V1</span>

[![Mcupro 2014 1 25 Top Overview](./img/Mcupro-2014-1-25-top-overview.jpg)](./img/Mcupro-2014-1-25-top-overview.jpg "Mcupro 2014 1 25 Top Overview"){ .glightbox data-gallery="mcupro-logic16-clone" }
<span class="caption">Mcupro 2014 1 25 Top Overview</span>

[![Mcupro 2015 1 8 Voltage Regulators](./img/Mcupro-2015-1-8-voltage-regulators.jpg)](./img/Mcupro-2015-1-8-voltage-regulators.jpg "Mcupro 2015 1 8 Voltage Regulators"){ .glightbox data-gallery="mcupro-logic16-clone" }
<span class="caption">Mcupro 2015 1 8 Voltage Regulators</span>

[![Mcupro 2018 Back](./img/Mcupro-2018-back.jpg)](./img/Mcupro-2018-back.jpg "Mcupro 2018 Back"){ .glightbox data-gallery="mcupro-logic16-clone" }
<span class="caption">Mcupro 2018 Back</span>

[![Seleae Logic16 Aliexpress Clone](./img/Seleae-logic16-aliexpress-clone.jpg)](./img/Seleae-logic16-aliexpress-clone.jpg "Seleae Logic16 Aliexpress Clone"){ .glightbox data-gallery="mcupro-logic16-clone" }
<span class="caption">Seleae Logic16 Aliexpress Clone</span>

[![Mcupro 2015 1 8 Top Overview](./img/Mcupro-2015-1-8-top-overview.jpg)](./img/Mcupro-2015-1-8-top-overview.jpg "Mcupro 2015 1 8 Top Overview"){ .glightbox data-gallery="mcupro-logic16-clone" }
<span class="caption">Mcupro 2015 1 8 Top Overview</span>

[![Mcupro 2015 1 8 Bottom Overview](./img/Mcupro-2015-1-8-bottom-overview.jpg)](./img/Mcupro-2015-1-8-bottom-overview.jpg "Mcupro 2015 1 8 Bottom Overview"){ .glightbox data-gallery="mcupro-logic16-clone" }
<span class="caption">Mcupro 2015 1 8 Bottom Overview</span>

[![Mcupro 2018 Case](./img/Mcupro-2018-case.jpg)](./img/Mcupro-2018-case.jpg "Mcupro 2018 Case"){ .glightbox data-gallery="mcupro-logic16-clone" }
<span class="caption">Mcupro 2018 Case</span>

[![Mcupro 2015 1 8 Bottom Markings Intact](./img/Mcupro-2015-1-8-bottom-markings-intact.jpg)](./img/Mcupro-2015-1-8-bottom-markings-intact.jpg "Mcupro 2015 1 8 Bottom Markings Intact"){ .glightbox data-gallery="mcupro-logic16-clone" }
<span class="caption">Mcupro 2015 1 8 Bottom Markings Intact</span>

[![Xl Logic16 100m External](./img/Xl-logic16-100m-external.jpg)](./img/Xl-logic16-100m-external.jpg "Xl Logic16 100m External"){ .glightbox data-gallery="mcupro-logic16-clone" }
<span class="caption">Xl Logic16 100m External</span>

[![Mcupro Logic16 Variant2 Top Flash 2buc](./img/Mcupro_Logic16_Variant2_top_flash_2BuC.jpg)](./img/Mcupro_Logic16_Variant2_top_flash_2BuC.jpg "Mcupro Logic16 Variant2 Top Flash 2buc"){ .glightbox data-gallery="mcupro-logic16-clone" }
<span class="caption">Mcupro Logic16 Variant2 Top Flash 2buc</span>

[![Mcupro Logic16 Overview](./img/Mcupro_Logic16_overview.jpg)](./img/Mcupro_Logic16_overview.png "Mcupro Logic16 Overview"){ .glightbox data-gallery="mcupro-logic16-clone" }
<span class="caption">Mcupro Logic16 Overview</span>

[![Mcupro 2014 1 25 Bottom Overview](./img/Mcupro-2014-1-25-bottom-overview.jpg)](./img/Mcupro-2014-1-25-bottom-overview.jpg "Mcupro 2014 1 25 Bottom Overview"){ .glightbox data-gallery="mcupro-logic16-clone" }
<span class="caption">Mcupro 2014 1 25 Bottom Overview</span>

[![Mcupro 2014 1 25 Bottom Ortho](./img/Mcupro-2014-1-25-bottom_ortho.jpg)](./img/Mcupro-2014-1-25-bottom_ortho.jpg "Mcupro 2014 1 25 Bottom Ortho"){ .glightbox data-gallery="mcupro-logic16-clone" }
<span class="caption">Mcupro 2014 1 25 Bottom Ortho</span>

[![Mcupro 2014 1 25 Top Ortho](./img/Mcupro-2014-1-25-top_ortho.jpg)](./img/Mcupro-2014-1-25-top_ortho.jpg "Mcupro 2014 1 25 Top Ortho"){ .glightbox data-gallery="mcupro-logic16-clone" }
<span class="caption">Mcupro 2014 1 25 Top Ortho</span>

[![Mcupro Logic16 Variant2 Top](./img/Mcupro_Logic16_Variant2_top.jpg)](./img/Mcupro_Logic16_Variant2_top.jpg "Mcupro Logic16 Variant2 Top"){ .glightbox data-gallery="mcupro-logic16-clone" }
<span class="caption">Mcupro Logic16 Variant2 Top</span>

[![Mcupro 2018 Front](./img/Mcupro-2018-front.jpg)](./img/Mcupro-2018-front.jpg "Mcupro 2018 Front"){ .glightbox data-gallery="mcupro-logic16-clone" }
<span class="caption">Mcupro 2018 Front</span>

</div>

## Photos

<div class="photo-grid" markdown>

[![Img 0207 V1](./img/IMG_0207_v1.JPG)](./img/IMG_0207_v1.JPG "Img 0207 V1"){ .glightbox data-gallery="mcupro-logic16-clone" }
<span class="caption">Img 0207 V1</span>

[![Mcupro 2014 1 25 Top Overview](./img/Mcupro-2014-1-25-top-overview.jpg)](./img/Mcupro-2014-1-25-top-overview.jpg "Mcupro 2014 1 25 Top Overview"){ .glightbox data-gallery="mcupro-logic16-clone" }
<span class="caption">Mcupro 2014 1 25 Top Overview</span>

[![Mcupro 2015 1 8 Voltage Regulators](./img/Mcupro-2015-1-8-voltage-regulators.jpg)](./img/Mcupro-2015-1-8-voltage-regulators.jpg "Mcupro 2015 1 8 Voltage Regulators"){ .glightbox data-gallery="mcupro-logic16-clone" }
<span class="caption">Mcupro 2015 1 8 Voltage Regulators</span>

[![Mcupro 2018 Back](./img/Mcupro-2018-back.jpg)](./img/Mcupro-2018-back.jpg "Mcupro 2018 Back"){ .glightbox data-gallery="mcupro-logic16-clone" }
<span class="caption">Mcupro 2018 Back</span>

[![Seleae Logic16 Aliexpress Clone](./img/Seleae-logic16-aliexpress-clone.jpg)](./img/Seleae-logic16-aliexpress-clone.jpg "Seleae Logic16 Aliexpress Clone"){ .glightbox data-gallery="mcupro-logic16-clone" }
<span class="caption">Seleae Logic16 Aliexpress Clone</span>

[![Mcupro 2015 1 8 Top Overview](./img/Mcupro-2015-1-8-top-overview.jpg)](./img/Mcupro-2015-1-8-top-overview.jpg "Mcupro 2015 1 8 Top Overview"){ .glightbox data-gallery="mcupro-logic16-clone" }
<span class="caption">Mcupro 2015 1 8 Top Overview</span>

[![Mcupro 2015 1 8 Bottom Overview](./img/Mcupro-2015-1-8-bottom-overview.jpg)](./img/Mcupro-2015-1-8-bottom-overview.jpg "Mcupro 2015 1 8 Bottom Overview"){ .glightbox data-gallery="mcupro-logic16-clone" }
<span class="caption">Mcupro 2015 1 8 Bottom Overview</span>

[![Mcupro 2018 Case](./img/Mcupro-2018-case.jpg)](./img/Mcupro-2018-case.jpg "Mcupro 2018 Case"){ .glightbox data-gallery="mcupro-logic16-clone" }
<span class="caption">Mcupro 2018 Case</span>

[![Mcupro 2015 1 8 Bottom Markings Intact](./img/Mcupro-2015-1-8-bottom-markings-intact.jpg)](./img/Mcupro-2015-1-8-bottom-markings-intact.jpg "Mcupro 2015 1 8 Bottom Markings Intact"){ .glightbox data-gallery="mcupro-logic16-clone" }
<span class="caption">Mcupro 2015 1 8 Bottom Markings Intact</span>

[![Xl Logic16 100m External](./img/Xl-logic16-100m-external.jpg)](./img/Xl-logic16-100m-external.jpg "Xl Logic16 100m External"){ .glightbox data-gallery="mcupro-logic16-clone" }
<span class="caption">Xl Logic16 100m External</span>

[![Mcupro Logic16 Variant2 Top Flash 2buc](./img/Mcupro_Logic16_Variant2_top_flash_2BuC.jpg)](./img/Mcupro_Logic16_Variant2_top_flash_2BuC.jpg "Mcupro Logic16 Variant2 Top Flash 2buc"){ .glightbox data-gallery="mcupro-logic16-clone" }
<span class="caption">Mcupro Logic16 Variant2 Top Flash 2buc</span>

[![Mcupro Logic16 Overview](./img/Mcupro_Logic16_overview.jpg)](./img/Mcupro_Logic16_overview.png "Mcupro Logic16 Overview"){ .glightbox data-gallery="mcupro-logic16-clone" }
<span class="caption">Mcupro Logic16 Overview</span>

[![Mcupro 2014 1 25 Bottom Overview](./img/Mcupro-2014-1-25-bottom-overview.jpg)](./img/Mcupro-2014-1-25-bottom-overview.jpg "Mcupro 2014 1 25 Bottom Overview"){ .glightbox data-gallery="mcupro-logic16-clone" }
<span class="caption">Mcupro 2014 1 25 Bottom Overview</span>

[![Mcupro 2014 1 25 Bottom Ortho](./img/Mcupro-2014-1-25-bottom_ortho.jpg)](./img/Mcupro-2014-1-25-bottom_ortho.jpg "Mcupro 2014 1 25 Bottom Ortho"){ .glightbox data-gallery="mcupro-logic16-clone" }
<span class="caption">Mcupro 2014 1 25 Bottom Ortho</span>

[![Mcupro 2014 1 25 Top Ortho](./img/Mcupro-2014-1-25-top_ortho.jpg)](./img/Mcupro-2014-1-25-top_ortho.jpg "Mcupro 2014 1 25 Top Ortho"){ .glightbox data-gallery="mcupro-logic16-clone" }
<span class="caption">Mcupro 2014 1 25 Top Ortho</span>

[![Mcupro Logic16 Variant2 Top](./img/Mcupro_Logic16_Variant2_top.jpg)](./img/Mcupro_Logic16_Variant2_top.jpg "Mcupro Logic16 Variant2 Top"){ .glightbox data-gallery="mcupro-logic16-clone" }
<span class="caption">Mcupro Logic16 Variant2 Top</span>

[![Mcupro 2018 Front](./img/Mcupro-2018-front.jpg)](./img/Mcupro-2018-front.jpg "Mcupro 2018 Front"){ .glightbox data-gallery="mcupro-logic16-clone" }
<span class="caption">Mcupro 2018 Front</span>

</div>

## Photos

<div class="photo-grid" markdown>

[![Img 0207 V1](./img/IMG_0207_v1.JPG)](./img/IMG_0207_v1.JPG "Img 0207 V1"){ .glightbox data-gallery="mcupro-logic16-clone" }
<span class="caption">Img 0207 V1</span>

[![Mcupro 2014 1 25 Top Overview](./img/Mcupro-2014-1-25-top-overview.jpg)](./img/Mcupro-2014-1-25-top-overview.jpg "Mcupro 2014 1 25 Top Overview"){ .glightbox data-gallery="mcupro-logic16-clone" }
<span class="caption">Mcupro 2014 1 25 Top Overview</span>

[![Mcupro 2015 1 8 Voltage Regulators](./img/Mcupro-2015-1-8-voltage-regulators.jpg)](./img/Mcupro-2015-1-8-voltage-regulators.jpg "Mcupro 2015 1 8 Voltage Regulators"){ .glightbox data-gallery="mcupro-logic16-clone" }
<span class="caption">Mcupro 2015 1 8 Voltage Regulators</span>

[![Mcupro 2018 Back](./img/Mcupro-2018-back.jpg)](./img/Mcupro-2018-back.jpg "Mcupro 2018 Back"){ .glightbox data-gallery="mcupro-logic16-clone" }
<span class="caption">Mcupro 2018 Back</span>

[![Seleae Logic16 Aliexpress Clone](./img/Seleae-logic16-aliexpress-clone.jpg)](./img/Seleae-logic16-aliexpress-clone.jpg "Seleae Logic16 Aliexpress Clone"){ .glightbox data-gallery="mcupro-logic16-clone" }
<span class="caption">Seleae Logic16 Aliexpress Clone</span>

[![Mcupro 2015 1 8 Top Overview](./img/Mcupro-2015-1-8-top-overview.jpg)](./img/Mcupro-2015-1-8-top-overview.jpg "Mcupro 2015 1 8 Top Overview"){ .glightbox data-gallery="mcupro-logic16-clone" }
<span class="caption">Mcupro 2015 1 8 Top Overview</span>

[![Mcupro 2015 1 8 Bottom Overview](./img/Mcupro-2015-1-8-bottom-overview.jpg)](./img/Mcupro-2015-1-8-bottom-overview.jpg "Mcupro 2015 1 8 Bottom Overview"){ .glightbox data-gallery="mcupro-logic16-clone" }
<span class="caption">Mcupro 2015 1 8 Bottom Overview</span>

[![Mcupro 2018 Case](./img/Mcupro-2018-case.jpg)](./img/Mcupro-2018-case.jpg "Mcupro 2018 Case"){ .glightbox data-gallery="mcupro-logic16-clone" }
<span class="caption">Mcupro 2018 Case</span>

[![Mcupro 2015 1 8 Bottom Markings Intact](./img/Mcupro-2015-1-8-bottom-markings-intact.jpg)](./img/Mcupro-2015-1-8-bottom-markings-intact.jpg "Mcupro 2015 1 8 Bottom Markings Intact"){ .glightbox data-gallery="mcupro-logic16-clone" }
<span class="caption">Mcupro 2015 1 8 Bottom Markings Intact</span>

[![Xl Logic16 100m External](./img/Xl-logic16-100m-external.jpg)](./img/Xl-logic16-100m-external.jpg "Xl Logic16 100m External"){ .glightbox data-gallery="mcupro-logic16-clone" }
<span class="caption">Xl Logic16 100m External</span>

[![Mcupro Logic16 Variant2 Top Flash 2buc](./img/Mcupro_Logic16_Variant2_top_flash_2BuC.jpg)](./img/Mcupro_Logic16_Variant2_top_flash_2BuC.jpg "Mcupro Logic16 Variant2 Top Flash 2buc"){ .glightbox data-gallery="mcupro-logic16-clone" }
<span class="caption">Mcupro Logic16 Variant2 Top Flash 2buc</span>

[![Mcupro Logic16 Overview](./img/Mcupro_Logic16_overview.jpg)](./img/Mcupro_Logic16_overview.png "Mcupro Logic16 Overview"){ .glightbox data-gallery="mcupro-logic16-clone" }
<span class="caption">Mcupro Logic16 Overview</span>

[![Mcupro 2014 1 25 Bottom Overview](./img/Mcupro-2014-1-25-bottom-overview.jpg)](./img/Mcupro-2014-1-25-bottom-overview.jpg "Mcupro 2014 1 25 Bottom Overview"){ .glightbox data-gallery="mcupro-logic16-clone" }
<span class="caption">Mcupro 2014 1 25 Bottom Overview</span>

[![Mcupro 2014 1 25 Bottom Ortho](./img/Mcupro-2014-1-25-bottom_ortho.jpg)](./img/Mcupro-2014-1-25-bottom_ortho.jpg "Mcupro 2014 1 25 Bottom Ortho"){ .glightbox data-gallery="mcupro-logic16-clone" }
<span class="caption">Mcupro 2014 1 25 Bottom Ortho</span>

[![Mcupro 2014 1 25 Top Ortho](./img/Mcupro-2014-1-25-top_ortho.jpg)](./img/Mcupro-2014-1-25-top_ortho.jpg "Mcupro 2014 1 25 Top Ortho"){ .glightbox data-gallery="mcupro-logic16-clone" }
<span class="caption">Mcupro 2014 1 25 Top Ortho</span>

[![Mcupro Logic16 Variant2 Top](./img/Mcupro_Logic16_Variant2_top.jpg)](./img/Mcupro_Logic16_Variant2_top.jpg "Mcupro Logic16 Variant2 Top"){ .glightbox data-gallery="mcupro-logic16-clone" }
<span class="caption">Mcupro Logic16 Variant2 Top</span>

[![Mcupro 2018 Front](./img/Mcupro-2018-front.jpg)](./img/Mcupro-2018-front.jpg "Mcupro 2018 Front"){ .glightbox data-gallery="mcupro-logic16-clone" }
<span class="caption">Mcupro 2018 Front</span>

</div>

## Photos

<div class="photo-grid" markdown>

[![Img 0207 V1](./img/IMG_0207_v1.JPG)](./img/IMG_0207_v1.JPG "Img 0207 V1"){ .glightbox data-gallery="mcupro-logic16-clone" }
<span class="caption">Img 0207 V1</span>

[![Mcupro 2014 1 25 Top Overview](./img/Mcupro-2014-1-25-top-overview.jpg)](./img/Mcupro-2014-1-25-top-overview.jpg "Mcupro 2014 1 25 Top Overview"){ .glightbox data-gallery="mcupro-logic16-clone" }
<span class="caption">Mcupro 2014 1 25 Top Overview</span>

[![Mcupro 2015 1 8 Voltage Regulators](./img/Mcupro-2015-1-8-voltage-regulators.jpg)](./img/Mcupro-2015-1-8-voltage-regulators.jpg "Mcupro 2015 1 8 Voltage Regulators"){ .glightbox data-gallery="mcupro-logic16-clone" }
<span class="caption">Mcupro 2015 1 8 Voltage Regulators</span>

[![Mcupro 2018 Back](./img/Mcupro-2018-back.jpg)](./img/Mcupro-2018-back.jpg "Mcupro 2018 Back"){ .glightbox data-gallery="mcupro-logic16-clone" }
<span class="caption">Mcupro 2018 Back</span>

[![Seleae Logic16 Aliexpress Clone](./img/Seleae-logic16-aliexpress-clone.jpg)](./img/Seleae-logic16-aliexpress-clone.jpg "Seleae Logic16 Aliexpress Clone"){ .glightbox data-gallery="mcupro-logic16-clone" }
<span class="caption">Seleae Logic16 Aliexpress Clone</span>

[![Mcupro 2015 1 8 Top Overview](./img/Mcupro-2015-1-8-top-overview.jpg)](./img/Mcupro-2015-1-8-top-overview.jpg "Mcupro 2015 1 8 Top Overview"){ .glightbox data-gallery="mcupro-logic16-clone" }
<span class="caption">Mcupro 2015 1 8 Top Overview</span>

[![Mcupro 2015 1 8 Bottom Overview](./img/Mcupro-2015-1-8-bottom-overview.jpg)](./img/Mcupro-2015-1-8-bottom-overview.jpg "Mcupro 2015 1 8 Bottom Overview"){ .glightbox data-gallery="mcupro-logic16-clone" }
<span class="caption">Mcupro 2015 1 8 Bottom Overview</span>

[![Mcupro 2018 Case](./img/Mcupro-2018-case.jpg)](./img/Mcupro-2018-case.jpg "Mcupro 2018 Case"){ .glightbox data-gallery="mcupro-logic16-clone" }
<span class="caption">Mcupro 2018 Case</span>

[![Mcupro 2015 1 8 Bottom Markings Intact](./img/Mcupro-2015-1-8-bottom-markings-intact.jpg)](./img/Mcupro-2015-1-8-bottom-markings-intact.jpg "Mcupro 2015 1 8 Bottom Markings Intact"){ .glightbox data-gallery="mcupro-logic16-clone" }
<span class="caption">Mcupro 2015 1 8 Bottom Markings Intact</span>

[![Xl Logic16 100m External](./img/Xl-logic16-100m-external.jpg)](./img/Xl-logic16-100m-external.jpg "Xl Logic16 100m External"){ .glightbox data-gallery="mcupro-logic16-clone" }
<span class="caption">Xl Logic16 100m External</span>

[![Mcupro Logic16 Variant2 Top Flash 2buc](./img/Mcupro_Logic16_Variant2_top_flash_2BuC.jpg)](./img/Mcupro_Logic16_Variant2_top_flash_2BuC.jpg "Mcupro Logic16 Variant2 Top Flash 2buc"){ .glightbox data-gallery="mcupro-logic16-clone" }
<span class="caption">Mcupro Logic16 Variant2 Top Flash 2buc</span>

[![Mcupro Logic16 Overview](./img/Mcupro_Logic16_overview.jpg)](./img/Mcupro_Logic16_overview.png "Mcupro Logic16 Overview"){ .glightbox data-gallery="mcupro-logic16-clone" }
<span class="caption">Mcupro Logic16 Overview</span>

[![Mcupro 2014 1 25 Bottom Overview](./img/Mcupro-2014-1-25-bottom-overview.jpg)](./img/Mcupro-2014-1-25-bottom-overview.jpg "Mcupro 2014 1 25 Bottom Overview"){ .glightbox data-gallery="mcupro-logic16-clone" }
<span class="caption">Mcupro 2014 1 25 Bottom Overview</span>

[![Mcupro 2014 1 25 Bottom Ortho](./img/Mcupro-2014-1-25-bottom_ortho.jpg)](./img/Mcupro-2014-1-25-bottom_ortho.jpg "Mcupro 2014 1 25 Bottom Ortho"){ .glightbox data-gallery="mcupro-logic16-clone" }
<span class="caption">Mcupro 2014 1 25 Bottom Ortho</span>

[![Mcupro 2014 1 25 Top Ortho](./img/Mcupro-2014-1-25-top_ortho.jpg)](./img/Mcupro-2014-1-25-top_ortho.jpg "Mcupro 2014 1 25 Top Ortho"){ .glightbox data-gallery="mcupro-logic16-clone" }
<span class="caption">Mcupro 2014 1 25 Top Ortho</span>

[![Mcupro Logic16 Variant2 Top](./img/Mcupro_Logic16_Variant2_top.jpg)](./img/Mcupro_Logic16_Variant2_top.jpg "Mcupro Logic16 Variant2 Top"){ .glightbox data-gallery="mcupro-logic16-clone" }
<span class="caption">Mcupro Logic16 Variant2 Top</span>

[![Mcupro 2018 Front](./img/Mcupro-2018-front.jpg)](./img/Mcupro-2018-front.jpg "Mcupro 2018 Front"){ .glightbox data-gallery="mcupro-logic16-clone" }
<span class="caption">Mcupro 2018 Front</span>

</div>
## Protocol

See [Saleae_Logic16#Protocol](https://sigrok.org/wiki/Saleae_Logic16#Protocol).

## Firmware
Actel variant
This logic analyzer works with unmodified Saleae software. The Actel FPGA has on-chip flash storage, so it only requires an upload of Cypress FX2LP firmware in order to operate.
Cyclone variant
This logic analyzer works with unmodified Saleae software. The PCB contains an SPI flash chip, so it only requires an upload of Cypress FX2LP firmware in order to operate.
2015-01-08 and 2018 variants
Only requires an upload of Cypress FX2LP firmware to operate. Open-source binaries from [gregani](https://github.com/gregani/la16fw) work, but must be renamed to **saleae-logic16-fx2.fw**. It also requires a [libsigrok](https://sigrok.org/wiki/Libsigrok) more recent than 2014-08-22 to work (see bug [#680](http://sigrok.org/bugzilla/show_bug.cgi?id=680#c4)).
2014-01-25 variant
Seems to have the bitstream in internal flash, so it only requires an upload of Cypress FX2LP firmware in order to operate. This requires a [libsigrok](https://sigrok.org/wiki/Libsigrok) more recent than 2014-08-22 to work (see bug [#680](http://sigrok.org/bugzilla/show_bug.cgi?id=680#c4)).

The firmware extraction steps are identical to [steps for Saleae Logic16](https://sigrok.org/wiki/Saleae_Logic16#Firmware), however you only need to have **saleae-logic16-fx2.fw** installed.

