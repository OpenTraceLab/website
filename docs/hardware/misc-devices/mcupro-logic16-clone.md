# Mcupro Logic16 Clone

| | | |:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:| | [![\1](../../assets/hardware/general/\2)](./File:Mcupro_Logic16_overview.png.html) | | | Status | supported | | Source code | [saleae-logic16](http://github.com/OpenTraceLab/?p=OpenTraceCapture.git;a=tree;f=src/hardware/saleae-logic16) | | Channels | 3/6/9/16 | | Samplerate | 100/50/32/16MHz | | Samplerate (state) | — | | Triggers | none (SW-only) | | Min/max voltage | -0.9V — 6V | | Threshold voltage | 1.5V (operates with 3.3V logic) | | Memory | none | | Compression | yes | | Price range | \$30 - \$35 | | Website | [aliexpress.com](https://www.aliexpress.com/item/new-USB-Logic-100MHz-16Ch-Logic-Analyzer-for-ARM-FPGA-E4-004/32931358747.html) | **mcupro Logic16 clone** The **mcupro Logic16 clone** is a USB-based, 16-channel logic analyzer with 100/50/32/16MHz sampling rate (at 3/6/9/16 enabled channels). This is a clone of the [Saleae Logic16](Saleae_Logic16.html "Saleae Logic16"). See [mcupro Logic16 clone/Info](Mcupro_Logic16_clone/Info.html "Mcupro Logic16 clone/Info") for more details (such as **lsusb -v** output) about the device. 
## Contents 
\- [1 Hardware (Actel variant)](Mcupro_Logic16_clone.html#Hardware_(Actel_variant)) \- [2 Hardware (Cyclone variant)](Mcupro_Logic16_clone.html#Hardware_(Cyclone_variant)) \- [3 Hardware (2018 variant)](Mcupro_Logic16_clone.html#Hardware_(2018_variant)) \- [4 Hardware (2015-01-08 variant)](Mcupro_Logic16_clone.html#Hardware_(2015-01-08_variant)) \- [5 Hardware (2014-01-25 variant)](Mcupro_Logic16_clone.html#Hardware_(2014-01-25_variant)) \- [6 Photos (Actel)](Mcupro_Logic16_clone.html#Photos_(Actel)) \- [7 Photos (Cyclone)](Mcupro_Logic16_clone.html#Photos_(Cyclone)) \- [8 Photos (2018 variant)](Mcupro_Logic16_clone.html#Photos_(2018_variant)) \- [9 Photos (2015-01-08 variant)](Mcupro_Logic16_clone.html#Photos_(2015-01-08_variant)) \- [10 Photos (2014-01-25 variant)](Mcupro_Logic16_clone.html#Photos_(2014-01-25_variant)) \- [11 Protocol](Mcupro_Logic16_clone.html#Protocol) \- [12 Firmware](Mcupro_Logic16_clone.html#Firmware) 
## Hardware (Actel variant) The PCB is marked "Saleae16 v4.6 By mcupro". \- **FPGA**: [Actel A3P125](https://www.actel.com/documents/PA3_DS.pdf) \- **USB interface chip**: [Cypress CY7C68013A](http://www.cypress.com/?docID=45142) \- **I²C EEPROM**: [Atmel 24C02N](http://www.atmel.com/Images/doc3256.pdf) \- **3.3V voltage regulator**: [Advanced Monolithic Systems AMS1117-3.3](http://ams-semitech.com/attachments/File/AMS1117_20120314.pdf) \- **1.5V voltage regulator**: [Advanced Monolithic Systems AMS1117-1.5](http://ams-semitech.com/attachments/File/AMS1117_20120314.pdf) \- **Crystal**: 24MHz ## Hardware (Cyclone variant) The PCB doesn't have any identifying markings. \- **FPGA**: [Altera Cyclone EP1C3T100](https://www.altera.com/products/fpga/cyclone-series/cyclone/support.html#Cyclone-Device-Handbook--All-Sections-) \- **USB interface chip**: [Cypress CY7C68013A](http://www.cypress.com/?docID=45142) \- **I²C EEPROM**: [Atmel 24C02N](http://www.atmel.com/Images/doc3256.pdf) \- **3.3V voltage regulator**: [Advanced Monolithic Systems AMS1117-3.3](http://ams-semitech.com/attachments/File/AMS1117_20120314.pdf) \- **1.5V voltage regulator**: [Advanced Monolithic Systems AMS1117-1.5](http://ams-semitech.com/attachments/File/AMS1117_20120314.pdf) \- **Crystal (FX2)**: 24MHz \- **Crystal (FPGA)**: 100MHz \- **FPGA bitstream**: ST M25P10VP, 1Mbit SPI NOR flash ([datasheet](https://cdn.datasheetspdf.com/pdf-down/2/5/P/25P10VP-STMicroelectronics.pdf)) \- **Bootstrap controller**: [STCMCU 15F10](http://www.stcmcu.com/datasheet/stc/STC-AD-PDF/STC15.pdf), 8051 compatible ## Hardware (2018 variant) The PCB is marked "Logic 16 Saleae". This variant also comes in a case identical to the [Noname_XL-LOGIC16-100M](Noname_XL-LOGIC16-100M.html "Noname XL-LOGIC16-100M"). \- **FPGA**: Markings ground off, but pinout indicates an Altera Cyclone EP1C3T144. \- **USB interface chip**: [Cypress CY7C68013A](http://www.cypress.com/?docID=45142) \- **I²C EEPROM**: Markings ground off \- **3.3V voltage regulator**: [TD 6810](http://www.techcodesemi.com/cn/products_info.asp?pid=26) adjustable version + 150k/680k resistors pair \- **1.5V voltage regulator**: [TD 6810](http://www.techcodesemi.com/cn/products_info.asp?pid=26) adjustable version + 160k/240k resistors pair \- **Crystal (FX2)**: 24MHz \- **Crystal (FPGA)**: 32MHz \- **FPGA bitstream**: ST M25P10VP, 1Mbit SPI NOR flash ([datasheet](https://cdn.datasheetspdf.com/pdf-down/2/5/P/25P10VP-STMicroelectronics.pdf)) \- **Bootstrap controller**: Not required? ## Hardware (2015-01-08 variant) The PCB is marked "Saleae Logic 16 By MCUPro 2015-1-8". Readily identifiable by the irregular PCB traces, and switching power supplies. This comes in a different case, identical to the [Noname_XL-LOGIC16-100M](Noname_XL-LOGIC16-100M.html "Noname XL-LOGIC16-100M"). \- **FPGA**: Markings ground off \- **USB interface chip**: [Cypress CY7C68013A](http://www.cypress.com/?docID=45142) \- **I²C EEPROM**: Markings ground off \- **3.3V voltage regulator**: [TD 6810](http://www.techcodesemi.com/cn/products_info.asp?pid=26) adjustable version + 150k/680k resistors pair \- **1.5V voltage regulator**: [TD 6810](http://www.techcodesemi.com/cn/products_info.asp?pid=26) adjustable version + 160k/240k resistors pair \- **Crystal (FX2)**: 24MHz \- **Crystal (FPGA)**: Looks like 32MHz? \- **FPGA bitstream**: ST M25P10VP, 1Mbit SPI NOR flash ([datasheet](https://cdn.datasheetspdf.com/pdf-down/2/5/P/25P10VP-STMicroelectronics.pdf)) \- **Bootstrap controller**: Not required? ## Hardware (2014-01-25 variant) The PCB is marked "Saleae Logic 16 mcupro 2014.1.25". The bottom two channels are not GND, but SCK (sample clock out) and HCK (half of SCK out). \- **FPGA**: Markings ground off, but pinout and JTAG (IDCODE 0x020810dd) indicate an Altera Cyclone EP1C3T100. \- **USB interface chip**: Markings sometimes ground off? Cypress CY7C68013A \- **Crystal (FX2)**: marked "DKF 24.000" \- **Crystal (FPGA)**: marked "RAK32.00" \- **FPGA bitstream**: ST M25P10VP, 1Mbit SPI NOR flash ([datasheet](https://cdn.datasheetspdf.com/pdf-down/2/5/P/25P10VP-STMicroelectronics.pdf)) \- **I²C EEPROM**: None? (CY7C68013A I2C port wired to FPGA pins) \- **Bootstrap controller**: Markings ground off, pinout could indicate a [STCMCU 15F10x](http://www.stcmcu.com/datasheet/stc/STC-AD-PDF/STC15.pdf) 8051-based MCU? \- **3.3V voltage regulator**: unknown switching regulator (marked "IC5CJ" ?) + 150k/680k resistors pair \- **1.5V voltage regulator**: unknown switching regulator (marked "IC5CJ" ?) + 160k/240k resistors pair \- **Channel input buffering**: none, only simple resistor (510R) + TVS diode array protection (possibly [Semtech SRV05](http://www.semtech.com/images/datasheet/srv05-4.pdf)) ## Photos (Actel) \- 
[![\1](../../assets/hardware/general/\2)](./File:Mcupro_Logic16_case_top.jpeg.html)
Device, top
\- 
[![\1](../../assets/hardware/general/\2)](./File:Mcupro_Logic16_case_bottom.jpeg.html)
Device, bottom
\- 
[![\1](../../assets/hardware/general/\2)](./File:Mcupro_Logic16_top.jpeg.html)
PCB, top
\- 
[![\1](../../assets/hardware/general/\2)](./File:Mcupro_Logic16_bottom.jpeg.html)
PCB, bottom
## Photos (Cyclone) \- 
[![\1](../../assets/hardware/general/\2)](./File:Mcupro_Logic16_case_top.jpeg.html)
Device, top
\- 
[![\1](../../assets/hardware/general/\2)](./File:Mcupro_Logic16_case_bottom.jpeg.html)
Device, bottom
\- 
[![\1](../../assets/hardware/general/\2)](./File:Mcupro_Logic16_Variant2_top.jpg.html)
PCB with Altera Cyclone, top
\- 
[![\1](../../assets/hardware/general/\2)](./File:IMG_0207_v1.JPG.html)
PCB with Altera Cyclone, bottom
\- 
[![\1](../../assets/hardware/general/\2)](./File:Mcupro_Logic16_Variant2_top_flash+uC.jpg.html)
PCB, top, 1Mbit flash and STCMCU uC
## Photos (2018 variant) \- 
[![\1](../../assets/hardware/general/\2)](./File:Mcupro-2018-case.jpg.html)
Device, top
\- 
[![\1](../../assets/hardware/general/\2)](./File:Mcupro-2018-front.jpg.html)
PCB, top
\- 
[![\1](../../assets/hardware/general/\2)](./File:Mcupro-2018-back.jpg.html)
PCB, bottom
## Photos (2015-01-08 variant) \- 
[![\1](../../assets/hardware/general/\2)](./File:Xl-logic16-100m-external.jpg.html)
Device, top
\- 
[![\1](../../assets/hardware/general/\2)](./File:Mcupro-2015-1-8-top-overview.jpg.html)
PCB, top
\- 
[![\1](../../assets/hardware/general/\2)](./File:Mcupro-2015-1-8-bottom-overview.jpg.html)
PCB, bottom
\- 
[![\1](../../assets/hardware/general/\2)](./File:Mcupro-2015-1-8-voltage-regulators.jpg.html)
PCB, 3.3V and 1.5V voltage regulators
\- 
[![\1](../../assets/hardware/general/\2)](./File:Mcupro-2015-1-8-bottom-markings-intact.jpg.html)
PCB, bottom - chip markings intact
## Photos (2014-01-25 variant) \- 
[![\1](../../assets/hardware/general/\2)](./File:Seleae-logic16-aliexpress-clone.jpg.html)
Device, top
\- 
[![\1](../../assets/hardware/general/\2)](./File:Mcupro-2014-1-25-top_ortho.jpg.html)
PCB, top detail
\- 
[![\1](../../assets/hardware/general/\2)](./File:Mcupro-2014-1-25-bottom_ortho.jpg.html)
PCB, bottom detail
\- 
[![\1](../../assets/hardware/general/\2)](./File:Mcupro-2014-1-25-top-overview.jpg.html)
PCB, top
\- 
[![\1](../../assets/hardware/general/\2)](./File:Mcupro-2014-1-25-bottom-overview.jpg.html)
PCB, bottom
## Protocol See [Saleae_Logic16#Protocol](Saleae_Logic16.html#Protocol "Saleae Logic16"). ## Firmware Actel variant This logic analyzer works with unmodified Saleae software. The Actel FPGA has on-chip flash storage, so it only requires an upload of Cypress FX2LP firmware in order to operate. Cyclone variant This logic analyzer works with unmodified Saleae software. The PCB contains an SPI flash chip, so it only requires an upload of Cypress FX2LP firmware in order to operate. 2015-01-08 and 2018 variants Only requires an upload of Cypress FX2LP firmware to operate. Open-source binaries from [gregani](https://github.com/gregani/la16fw) work, but must be renamed to **saleae-logic16-fx2.fw**. It also requires a [OpenTraceCapture](OpenTraceCapture.html "OpenTraceCapture") more recent than 2014-08-22 to work (see bug [#680](http://OpenTraceLab.org/bugzilla/show_bug.cgi?id=680#c4)). 2014-01-25 variant Seems to have the bitstream in internal flash, so it only requires an upload of Cypress FX2LP firmware in order to operate. This requires a [OpenTraceCapture](OpenTraceCapture.html "OpenTraceCapture") more recent than 2014-08-22 to work (see bug [#680](http://OpenTraceLab.org/bugzilla/show_bug.cgi?id=680#c4)). The firmware extraction steps are identical to [steps for Saleae Logic16](Saleae_Logic16.html#Firmware "Saleae Logic16"), however you only need to have **saleae-logic16-fx2.fw** installed. 
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=Mcupro_Logic16_clone&oldid=14398](https://OpenTraceLab.org/w/index.php?title=Mcupro_Logic16_clone&oldid=14398)" 
[Categories](specialcategories-specialcategories.md): \- [Device](./Category:Device.html "Category:Device") \- [Logic analyzer](./Category:Logic_analyzer.html "Category:Logic analyzer") \- [Supported](./Category:Supported.html "Category:Supported")

## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
