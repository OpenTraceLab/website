# Mcupro Logic16 Clone
| | | |:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:| | [*Image: \1* | | | Status | supported | | Source code | [saleae-logic16](http://github.com/OpenTraceLab/?p=OpenTraceCapture.git;a=tree;f=src/hardware/saleae-logic16) | | Channels | 3/6/9/16 | | Samplerate | 100/50/32/16MHz | | Samplerate (state) | — | | Triggers | none (SW-only) | | Min/max voltage | -0.9V — 6V | | Threshold voltage | 1.5V (operates with 3.3V logic) | | Memory | none | | Compression | yes | | Price range | \$30 - \$35 | | Website | *aliexpress.com* | **mcupro Logic16 clone** The **mcupro Logic16 clone** is a USB-based, 16-channel logic analyzer with 100/50/32/16MHz sampling rate (at 3/6/9/16 enabled channels). This is a clone of the *Saleae Logic16*. See *mcupro Logic16 clone/Info* for more details (such as **lsusb -v** output) about the device.
## Contents
\- *1 Hardware (Actel variant)*) \- *2 Hardware (Cyclone variant)*) \- *3 Hardware (2018 variant)*) \- *4 Hardware (2015-01-08 variant)*) \- *5 Hardware (2014-01-25 variant)*) \- *6 Photos (Actel)*) \- *7 Photos (Cyclone)*) \- *8 Photos (2018 variant)*) \- *9 Photos (2015-01-08 variant)*) \- *10 Photos (2014-01-25 variant)*) \- *11 Protocol* \- *12 Firmware*
## Hardware (Actel variant) The PCB is marked "Saleae16 v4.6 By mcupro". \- **FPGA**: [Actel A3P125](https://www.actel.com/documents/PA3_DS.pdf) \- **USB interface chip**: [Cypress CY7C68013A](http://www.cypress.com/?docID=45142) \- **I²C EEPROM**: [Atmel 24C02N](http://www.atmel.com/Images/doc3256.pdf) \- **3.3V voltage regulator**: [Advanced Monolithic Systems AMS1117-3.3](http://ams-semitech.com/attachments/File/AMS1117_20120314.pdf) \- **1.5V voltage regulator**: [Advanced Monolithic Systems AMS1117-1.5](http://ams-semitech.com/attachments/File/AMS1117_20120314.pdf) \- **Crystal**: 24MHz ## Hardware (Cyclone variant) The PCB doesn't have any identifying markings. \- **FPGA**: *Altera Cyclone EP1C3T100* \- **USB interface chip**: [Cypress CY7C68013A](http://www.cypress.com/?docID=45142) \- **I²C EEPROM**: [Atmel 24C02N](http://www.atmel.com/Images/doc3256.pdf) \- **3.3V voltage regulator**: [Advanced Monolithic Systems AMS1117-3.3](http://ams-semitech.com/attachments/File/AMS1117_20120314.pdf) \- **1.5V voltage regulator**: [Advanced Monolithic Systems AMS1117-1.5](http://ams-semitech.com/attachments/File/AMS1117_20120314.pdf) \- **Crystal (FX2)**: 24MHz \- **Crystal (FPGA)**: 100MHz \- **FPGA bitstream**: ST M25P10VP, 1Mbit SPI NOR flash ([datasheet](https://cdn.datasheetspdf.com/pdf-down/2/5/P/25P10VP-STMicroelectronics.pdf)) \- **Bootstrap controller**: [STCMCU 15F10](http://www.stcmcu.com/datasheet/stc/STC-AD-PDF/STC15.pdf), 8051 compatible ## Hardware (2018 variant) The PCB is marked "Logic 16 Saleae". This variant also comes in a case identical to the *Noname_XL-LOGIC16-100M*. \- **FPGA**: Markings ground off, but pinout indicates an Altera Cyclone EP1C3T144. \- **USB interface chip**: [Cypress CY7C68013A](http://www.cypress.com/?docID=45142) \- **I²C EEPROM**: Markings ground off \- **3.3V voltage regulator**: [TD 6810](http://www.techcodesemi.com/cn/products_info.asp?pid=26) adjustable version + 150k/680k resistors pair \- **1.5V voltage regulator**: [TD 6810](http://www.techcodesemi.com/cn/products_info.asp?pid=26) adjustable version + 160k/240k resistors pair \- **Crystal (FX2)**: 24MHz \- **Crystal (FPGA)**: 32MHz \- **FPGA bitstream**: ST M25P10VP, 1Mbit SPI NOR flash ([datasheet](https://cdn.datasheetspdf.com/pdf-down/2/5/P/25P10VP-STMicroelectronics.pdf)) \- **Bootstrap controller**: Not required? ## Hardware (2015-01-08 variant) The PCB is marked "Saleae Logic 16 By MCUPro 2015-1-8". Readily identifiable by the irregular PCB traces, and switching power supplies. This comes in a different case, identical to the *Noname_XL-LOGIC16-100M*. \- **FPGA**: Markings ground off \- **USB interface chip**: [Cypress CY7C68013A](http://www.cypress.com/?docID=45142) \- **I²C EEPROM**: Markings ground off \- **3.3V voltage regulator**: [TD 6810](http://www.techcodesemi.com/cn/products_info.asp?pid=26) adjustable version + 150k/680k resistors pair \- **1.5V voltage regulator**: [TD 6810](http://www.techcodesemi.com/cn/products_info.asp?pid=26) adjustable version + 160k/240k resistors pair \- **Crystal (FX2)**: 24MHz \- **Crystal (FPGA)**: Looks like 32MHz? \- **FPGA bitstream**: ST M25P10VP, 1Mbit SPI NOR flash ([datasheet](https://cdn.datasheetspdf.com/pdf-down/2/5/P/25P10VP-STMicroelectronics.pdf)) \- **Bootstrap controller**: Not required? ## Hardware (2014-01-25 variant) The PCB is marked "Saleae Logic 16 mcupro 2014.1.25". The bottom two channels are not GND, but SCK (sample clock out) and HCK (half of SCK out). \- **FPGA**: Markings ground off, but pinout and JTAG (IDCODE 0x020810dd) indicate an Altera Cyclone EP1C3T100. \- **USB interface chip**: Markings sometimes ground off? Cypress CY7C68013A \- **Crystal (FX2)**: marked "DKF 24.000" \- **Crystal (FPGA)**: marked "RAK32.00" \- **FPGA bitstream**: ST M25P10VP, 1Mbit SPI NOR flash ([datasheet](https://cdn.datasheetspdf.com/pdf-down/2/5/P/25P10VP-STMicroelectronics.pdf)) \- **I²C EEPROM**: None? (CY7C68013A I2C port wired to FPGA pins) \- **Bootstrap controller**: Markings ground off, pinout could indicate a [STCMCU 15F10x](http://www.stcmcu.com/datasheet/stc/STC-AD-PDF/STC15.pdf) 8051-based MCU? \- **3.3V voltage regulator**: unknown switching regulator (marked "IC5CJ" ?) + 150k/680k resistors pair \- **1.5V voltage regulator**: unknown switching regulator (marked "IC5CJ" ?) + 160k/240k resistors pair \- **Channel input buffering**: none, only simple resistor (510R) + TVS diode array protection (possibly [Semtech SRV05](http://www.semtech.com/images/datasheet/srv05-4.pdf)) ## Photos (Actel) \-
[*Image: \1*
Device, top
\-
[*Image: \1*
Device, bottom
\-
[*Image: \1*
PCB, top
\-
[*Image: \1*
PCB, bottom
## Photos (Cyclone) \-
[*Image: \1*
Device, top
\-
[*Image: \1*
Device, bottom
\-
[*Image: \1*
PCB with Altera Cyclone, top
\-
[*Image: \1*
PCB with Altera Cyclone, bottom
\-
[*Image: \1*
PCB, top, 1Mbit flash and STCMCU uC
## Photos (2018 variant) \-
[*Image: \1*
Device, top
\-
[*Image: \1*
PCB, top
\-
[*Image: \1*
PCB, bottom
## Photos (2015-01-08 variant) \-
[*Image: \1*
Device, top
\-
[*Image: \1*
PCB, top
\-
[*Image: \1*
PCB, bottom
\-
[*Image: \1*
PCB, 3.3V and 1.5V voltage regulators
\-
[*Image: \1*
PCB, bottom - chip markings intact
## Photos (2014-01-25 variant) \-
[*Image: \1*
Device, top
\-
[*Image: \1*
PCB, top detail
\-
[*Image: \1*
PCB, bottom detail
\-
[*Image: \1*
PCB, top
\-
[*Image: \1*
PCB, bottom
## Protocol See *Saleae_Logic16#Protocol*. ## Firmware Actel variant This logic analyzer works with unmodified Saleae software. The Actel FPGA has on-chip flash storage, so it only requires an upload of Cypress FX2LP firmware in order to operate. Cyclone variant This logic analyzer works with unmodified Saleae software. The PCB contains an SPI flash chip, so it only requires an upload of Cypress FX2LP firmware in order to operate. 2015-01-08 and 2018 variants Only requires an upload of Cypress FX2LP firmware to operate. Open-source binaries from [gregani](https://github.com/gregani/la16fw) work, but must be renamed to **saleae-logic16-fx2.fw**. It also requires a *OpenTraceCapture* more recent than 2014-08-22 to work (see bug [#680](http://OpenTraceLab.org/bugzilla/show_bug.cgi?id=680#c4)). 2014-01-25 variant Seems to have the bitstream in internal flash, so it only requires an upload of Cypress FX2LP firmware in order to operate. This requires a *OpenTraceCapture* more recent than 2014-08-22 to work (see bug [#680](http://OpenTraceLab.org/bugzilla/show_bug.cgi?id=680#c4)). The firmware extraction steps are identical to *steps for Saleae Logic16*, however you only need to have **saleae-logic16-fx2.fw** installed.
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=Mcupro_Logic16_clone&oldid=14398](https://OpenTraceLab.org/w/index.php?title=Mcupro_Logic16_clone&oldid=14398)"
: \- *Device* \- *Logic analyzer* \- *Supported*
## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
