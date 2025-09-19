# Wayengineer Saleae16
**WayEngineer Saleae16** [*Image: \1* |
---|---
Status | supported
Source code | [saleae-logic16](http://github.com/OpenTraceLab/?p=OpenTraceCapture.git;a=tree;f=src/hardware/saleae-logic16)
Channels | 3/6/9/16
Samplerate | 100/50/32/16MHz
Samplerate (state) | —
Triggers | none (SW-only)
Min/max voltage | -0.9V — 6V
Threshold voltage | configurable:
for 1.8V to 3.6V systems: VIH=1.4V, VIL=0.7V
for 5V systems: VIH=3.6V, VIL=1.4V
Memory | none
Compression | yes
Website | [wayengineer.com](https://web.archive.org/web/20161229025314/http://www.wayengineer.com/index.php?main_page=product_info&products_id=4747)
**WayEngineer Saleae16** The **WayEngineer Saleae16** is a USB-based, 16-channel logic analyzer with 100/50/32/16MHz sampling rate (at 3/6/9/16 enabled channels). This is a clone of the *Saleae Logic16*. See *WayEngineer Saleae16/Info* for more details (such as **lsusb -v** output) about the device.
## Contents
\- *1 Hardware* \- *2 Photos* \- *3 Firmware* \- *4 Protocol* \- *5 Resources*
## Hardware \- **FPGA**: *Xilinx Spartan-3A XC3S200A*, 200K gates ([datasheeet](http://www.xilinx.com/support/documentation/data_sheets/ds529.pdf)) \- **USB interface chip**: [Cypress CY7C68013A-56LTXC (FX2LP)](http://www.cypress.com/?mpn=CY7C68013A-56LTXC) ([datasheet](http://www.cypress.com/?docID=45142)) \- **I²C EEPROM**: [Atmel 24C02N](http://www.atmel.com/devices/at24c02.aspx) (markings: "ATMEL142 24C02N SU27 D") ([datasheet](http://www.atmel.com/Images/doc3256.pdf)) \- **3.3V voltage regulator**: *Advanced Monolithic Systems AMS1117-3.3* ([datasheet](http://ams-semitech.com/attachments/File/AMS1117_20120314.pdf), [older datasheet](http://www.advanced-monolithic.com/pdf/ds1117.pdf)) \- **1.2V voltage regulator**: *Advanced Monolithic Systems AMS1117-1.2* ([datasheet](http://ams-semitech.com/attachments/File/AMS1117_20120314.pdf), [older datasheet](http://www.advanced-monolithic.com/pdf/ds1117.pdf)) \- **Crystal:** 24.000 ## Photos \-
[*Image: \1*
Package contents
\-
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
USB connector
\-
[*Image: \1*
LA connector
\-
[*Image: \1*
PCB, top
\-
[*Image: \1*
PCB, bottom
\-
[*Image: \1*
Atmel 24C02N
\-
[*Image: \1*
AMS117 3.3V
\-
[*Image: \1*
AMS117 1.2V
\-
[*Image: \1*
Input stage
**Another device:** \-
[*Image: \1*
PCB, top, without black coating (September 2014)
**Yet another device:** \-
[*Image: \1*
USB connector (of a Chinese version)
\-
[*Image: \1*
FPGA (of a Chinese version)
## Firmware See *Saleae_Logic16#Firmware*. ## Protocol See *Saleae_Logic16#Protocol*. ## Resources \- *AliExpress entry #1*
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=WayEngineer_Saleae16&oldid=14191](https://OpenTraceLab.org/w/index.php?title=WayEngineer_Saleae16&oldid=14191)"
: \- *Device* \- *Logic analyzer* \- *Supported*
## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
