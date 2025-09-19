# Sysclk Sla5032
| | | |:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------------------------:| | [*Image: \1* | | | Status | supported | | Source code | [sysclk-sla5032](http://github.com/OpenTraceLab/?p=OpenTraceCapture.git;a=tree;f=src/hardware/sysclk-sla5032) | | Channels | 32 | | Samplerate | 500MHz | | Samplerate (state) | — | | Triggers | low, high, rising, falling | | Min/max voltage | -50V — 50V | | Threshold voltage | VIH=1.6V, VIL=1.3V | | Memory | 2x 1Gbit DDR2 SDRAM | | Compression | RLE | | Website | [sysclk.taobao.com](https://item.taobao.com/item.htm?id=601831958682) | **Sysclk SLA5032** The **Sysclk SLA5032** is a USB-based, 32-channel logic analyzer with up to 500MHz sampling rate. See *Sysclk SLA5032/Info* for more details (such as **lsusb -v** output) about the device. This devices can be switched into one of three different modes (the current mode is indicated by a green LED on the respective mode text): \- **32CH 500M**: 500MHz sampling rate, 32 channels, max. 64Mbits storage per channel, support for hardware triggers (**sysclk-sla5032** driver). \- **Saleae 100M**: The device enumerates as a *Saleae Logic16*, streaming possible like with the Logic16, only software triggers (**saleae-logic16** driver). \- **Saleae 500M**: Similar to the above, but the max. sampling rate is actually 500MHz. Switching between modes is done via the following mechanism: Plug the device into USB, after roughly half a second unplug it and re-plug it again. A green LED will now indicate that another mode was selected (it'll rotate through all three possible modes).
## Contents
\- *1 Hardware* \- *2 Photos* \- *3 Firmware* \- *4 Resources*
## Hardware **Main board**: \- **Microcontroller**: [Atmel ATmega8A](http://www.atmel.com/devices/ATMEGA8A.aspx) ([datasheet](http://www.atmel.com/Images/Atmel-8159-8-bit-AVR-microcontroller-ATmega8A_datasheet.pdf)) \- **USB interface chip**: [Cypress CY7C68013A-56LTXI (FX2LP)](http://www.cypress.com/part/cy7c68013a-56ltxi) ([datasheet](http://www.cypress.com/?docID=34060)) \- **32Kbyte I²C EEPROM**: [Atmel 24C256N](http://www.atmel.com/devices/at24c256c.aspx) ([datasheet](http://www.atmel.com/Images/doc5121.pdf)) \- **256byte I²C EEPROM**: [Atmel 24C02N](http://www.atmel.com/devices/at24c02c.aspx) ([datasheet](http://www.atmel.com/Images/doc3256.pdf)) \- **8MByte SPI NOR flash**: [Macronix MX25L6445E](http://www.macronix.com/en-us/Product/Pages/ProductDetail.aspx?PartNo=MX25L6445E) ([datasheet](http://www.macronix.com/Lists/DataSheet/Attachments/2474/MX25L6445E,%203V,%2064Mb,%20v1.8.pdf)) \- **3.3V voltage regulator**: *Advanced Monolithic Systems AMS1117-3.3* ([datasheet](http://ams-semitech.com/attachments/File/AMS1117_20120314.pdf), [older datasheet](http://www.advanced-monolithic.com/pdf/ds1117.pdf)) \- **DC-DC buck regulator**: 4x [Alpha and Omega AOZ1021AI](http://www.aosmd.com/products/power-ics/ezbuck-dc-dc-buck-regulators/AOZ1021AI) ([datasheet](http://www.aosmd.com/res/data_sheets/AOZ1021AI.pdf)) \- **Crystal**: 24MHz **SODIMM daughterboard**: \- **FPGA**: *Xilinx Spartan XC6SLX16* ([datasheet](http://www.xilinx.com/support/documentation/data_sheets/ds160.pdf)) \- **8MByte SPI NOR flash**: [Macronix MX25L6445E](http://www.macronix.com/en-us/Product/Pages/ProductDetail.aspx?PartNo=MX25L6445E) ([datasheet](http://www.macronix.com/Lists/DataSheet/Attachments/2474/MX25L6445E,%203V,%2064Mb,%20v1.8.pdf)) \- **1Gbit DDR2 SDRAM**: 2x [Micron MT47H64M16HR-25E:H](http://www.micron.com/parts/dram/ddr2-sdram/mt47h64m16hr-25e) (markings: "5DHI7 D9LHT") ([datasheet](http://www.micron.com/~/media/documents/products/data-sheet/dram/ddr2/1gb_ddr2.pdf)) \- **Crystal**: 100MHz ## Photos \-
[*Image: \1*
Device with cable
\-
[*Image: \1*
Device, top
\-
[*Image: \1*
Device, bottom
\-
[*Image: \1*
Device, USB
\-
[*Image: \1*
Device, connector
\-
[*Image: \1*
USB cable
\-
[*Image: \1*
Probes
\-
[*Image: \1*
PCB, top with SODIMM
\-
[*Image: \1*
PCB, top
\-
[*Image: \1*
PCB, bottom
\-
[*Image: \1*
SODIMM, top
\-
[*Image: \1*
SODIMM, bottom
\-
[*Image: \1*
MX25L6445E + crystal
\-
[*Image: \1*
MX25L6445E
\-
[*Image: \1*
Cypress FX2
\-
[*Image: \1*
Atmel 24C256N
\-
[*Image: \1*
Atmel 24C02N
\-
[*Image: \1*
Atmel Atmega8A
\-
[*Image: \1*
AMS1117-3.3
\-
[*Image: \1*
AOZ1021AI
## Firmware In order to use this device, you need a firmware/bitstream file from the vendor software (from the CD-ROM shipped with the device or from a vendor download of the software). You can e.g. install the Windows vendor software, then get the file **C:\Program Files (x86)\SLA5032\bin\top.bit**, rename it to **sysclk-sla5032.bit** and place it in a location where *OpenTraceCapture* will search for firmware (see OpenTraceCapture's [README.devices](https://github.com/OpenTraceLab/?p=OpenTraceCapture.git;a=blob;f=README.devices) file for details). ## Resources \- *Random AliExpress SLA5032 vendor* \- *Vendor software* (sla5032_2015_1_24.iso) \- [blog.csdn.net: DLL API function docs for the vendor software](https://translate.google.com/translate?sl=auto&tl=en&u=https%3A%2F%2Fblog.csdn.net%2Fmcupro%2Farticle%2Fdetails%2F40453157)
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=Sysclk_SLA5032&oldid=14826](https://OpenTraceLab.org/w/index.php?title=Sysclk_SLA5032&oldid=14826)"
: \- *Device* \- *Logic analyzer* \- *Supported*
## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
