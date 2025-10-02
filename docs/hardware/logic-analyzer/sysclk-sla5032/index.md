---
title: Sysclk SLA5032
---

# Sysclk SLA5032

<div class="infobox" markdown>

![Sysclk SLA5032](./img/Sysclk_sla5032_fx2.jpg){ .infobox-image }

### Sysclk SLA5032

| | |
|---|---|
| **Status** | supported |
| **Source code** | [sysclk-sla5032](https://github.com/OpenTraceLab/OpenTraceCapture/tree/main/src/hardware/sysclk-sla5032) |
| **Channels** | 32 |
| **Samplerate** | 500MHz |
| **Samplerate (state)** | — |
| **Triggers** | low, high, rising, falling |
| **Min/max voltage** | -50V — 50V |
| **Threshold voltage** | VIH=1.6V, VIL=1.3V |
| **Memory** | 2x 1Gbit DDR2 SDRAM |
| **Compression** | RLE |
| **Website** | [sysclk.taobao.com](https://item.taobao.com/item.htm?id=601831958682) |

</div>

The **Sysclk SLA5032** is a USB-based, 32-channel logic analyzer with up to 500MHz sampling rate.

See [Sysclk SLA5032/Info](https://sigrok.org/wiki/Sysclk_SLA5032/Info) for more details (such as **lsusb -v** output) about the device.

This devices can be switched into one of three different modes (the current mode is indicated by a green LED on the respective mode text):

- **32CH 500M**: 500MHz sampling rate, 32 channels, max. 64Mbits storage per channel, support for hardware triggers (**sysclk-sla5032** driver).
- **Saleae 100M**: The device enumerates as a [Saleae Logic16](https://sigrok.org/wiki/Saleae_Logic16), streaming possible like with the Logic16, only software triggers (**saleae-logic16** driver).
- **Saleae 500M**: Similar to the above, but the max. sampling rate is actually 500MHz.

Switching between modes is done via the following mechanism: Plug the device into USB, after roughly half a second unplug it and re-plug it again. A green LED will now indicate that another mode was selected (it'll rotate through all three possible modes).

## Hardware

**Main board**:

- **Microcontroller**: [Atmel ATmega8A](http://www.atmel.com/devices/ATMEGA8A.aspx) ([datasheet](http://www.atmel.com/Images/Atmel-8159-8-bit-AVR-microcontroller-ATmega8A_datasheet.pdf))
- **USB interface chip**: [Cypress CY7C68013A-56LTXI (FX2LP)](http://www.cypress.com/part/cy7c68013a-56ltxi) ([datasheet](http://www.cypress.com/?docID=34060))
- **32Kbyte I²C EEPROM**: [Atmel 24C256N](http://www.atmel.com/devices/at24c256c.aspx) ([datasheet](http://www.atmel.com/Images/doc5121.pdf))
- **256byte I²C EEPROM**: [Atmel 24C02N](http://www.atmel.com/devices/at24c02c.aspx) ([datasheet](http://www.atmel.com/Images/doc3256.pdf))
- **8MByte SPI NOR flash**: [Macronix MX25L6445E](http://www.macronix.com/en-us/Product/Pages/ProductDetail.aspx?PartNo=MX25L6445E) ([datasheet](http://www.macronix.com/Lists/DataSheet/Attachments/2474/MX25L6445E,%203V,%2064Mb,%20v1.8.pdf))
- **3.3V voltage regulator**: [Advanced Monolithic Systems AMS1117-3.3](http://www.advanced-monolithic.com/products/voltreg.html#1117) ([datasheet](http://ams-semitech.com/attachments/File/AMS1117_20120314.pdf), [older datasheet](http://www.advanced-monolithic.com/pdf/ds1117.pdf))
- **DC-DC buck regulator**: 4x [Alpha and Omega AOZ1021AI](http://www.aosmd.com/products/power-ics/ezbuck-dc-dc-buck-regulators/AOZ1021AI) ([datasheet](http://www.aosmd.com/res/data_sheets/AOZ1021AI.pdf))
- **Crystal**: 24MHz

**SODIMM daughterboard**:

- **FPGA**: [Xilinx Spartan XC6SLX16](http://www.xilinx.com/products/silicon-devices/fpga/spartan-6/lx.html) ([datasheet](http://www.xilinx.com/support/documentation/data_sheets/ds160.pdf))
- **8MByte SPI NOR flash**: [Macronix MX25L6445E](http://www.macronix.com/en-us/Product/Pages/ProductDetail.aspx?PartNo=MX25L6445E) ([datasheet](http://www.macronix.com/Lists/DataSheet/Attachments/2474/MX25L6445E,%203V,%2064Mb,%20v1.8.pdf))
- **1Gbit DDR2 SDRAM**: 2x [Micron MT47H64M16HR-25E:H](http://www.micron.com/parts/dram/ddr2-sdram/mt47h64m16hr-25e) (markings: "5DHI7 D9LHT") ([datasheet](http://www.micron.com/~/media/documents/products/data-sheet/dram/ddr2/1gb_ddr2.pdf))
- **Crystal**: 100MHz

## Photos

<div class="photo-grid" markdown>

[![Sysclk Sla5032 Fx2](./img/Sysclk_sla5032_fx2.jpg)](./img/Sysclk_sla5032_fx2.jpg "Sysclk Sla5032 Fx2"){ .glightbox data-gallery="sysclk-sla5032" }
<span class="caption">Sysclk Sla5032 Fx2</span>

[![Sysclk Sla5032 Pcb Top2](./img/Sysclk_sla5032_pcb_top2.jpg)](./img/Sysclk_sla5032_pcb_top2.jpg "Sysclk Sla5032 Pcb Top2"){ .glightbox data-gallery="sysclk-sla5032" }
<span class="caption">Sysclk Sla5032 Pcb Top2</span>

[![Sysclk Sla5032 Pcb Module Bottom](./img/Sysclk_sla5032_pcb_module_bottom.jpg)](./img/Sysclk_sla5032_pcb_module_bottom.jpg "Sysclk Sla5032 Pcb Module Bottom"){ .glightbox data-gallery="sysclk-sla5032" }
<span class="caption">Sysclk Sla5032 Pcb Module Bottom</span>

[![Sysclk Sla5032 Probes](./img/Sysclk_sla5032_probes.jpg)](./img/Sysclk_sla5032_probes.jpg "Sysclk Sla5032 Probes"){ .glightbox data-gallery="sysclk-sla5032" }
<span class="caption">Sysclk Sla5032 Probes</span>

[![Sysclk Sla5032 Device With Cable](./img/Sysclk_sla5032_device_with_cable.jpg)](./img/Sysclk_sla5032_device_with_cable.jpg "Sysclk Sla5032 Device With Cable"){ .glightbox data-gallery="sysclk-sla5032" }
<span class="caption">Sysclk Sla5032 Device With Cable</span>

[![Sysclk Sla5032 Atmel 24c02n](./img/Sysclk_sla5032_atmel_24c02n.jpg)](./img/Sysclk_sla5032_atmel_24c02n.jpg "Sysclk Sla5032 Atmel 24c02n"){ .glightbox data-gallery="sysclk-sla5032" }
<span class="caption">Sysclk Sla5032 Atmel 24c02n</span>

[![Sysclk Sla5032 Device Top](./img/Sysclk_sla5032_device_top.jpg)](./img/Sysclk_sla5032_device_top.jpg "Sysclk Sla5032 Device Top"){ .glightbox data-gallery="sysclk-sla5032" }
<span class="caption">Sysclk Sla5032 Device Top</span>

[![Sysclk Sla5032 Device Usb](./img/Sysclk_sla5032_device_usb.jpg)](./img/Sysclk_sla5032_device_usb.jpg "Sysclk Sla5032 Device Usb"){ .glightbox data-gallery="sysclk-sla5032" }
<span class="caption">Sysclk Sla5032 Device Usb</span>

[![Sysclk Sla5032 Z1021ai](./img/Sysclk_sla5032_z1021ai.jpg)](./img/Sysclk_sla5032_z1021ai.jpg "Sysclk Sla5032 Z1021ai"){ .glightbox data-gallery="sysclk-sla5032" }
<span class="caption">Sysclk Sla5032 Z1021ai</span>

[![Sysclk Sla5032 Device Bottom](./img/Sysclk_sla5032_device_bottom.jpg)](./img/Sysclk_sla5032_device_bottom.jpg "Sysclk Sla5032 Device Bottom"){ .glightbox data-gallery="sysclk-sla5032" }
<span class="caption">Sysclk Sla5032 Device Bottom</span>

[![Sysclk Sla5032 Device Connector](./img/Sysclk_sla5032_device_connector.jpg)](./img/Sysclk_sla5032_device_connector.jpg "Sysclk Sla5032 Device Connector"){ .glightbox data-gallery="sysclk-sla5032" }
<span class="caption">Sysclk Sla5032 Device Connector</span>

[![Sysclk Sla5032 Pcb Top1](./img/Sysclk_sla5032_pcb_top1.jpg)](./img/Sysclk_sla5032_pcb_top1.jpg "Sysclk Sla5032 Pcb Top1"){ .glightbox data-gallery="sysclk-sla5032" }
<span class="caption">Sysclk Sla5032 Pcb Top1</span>

[![Sysclk Sla5032 Pcb Bottom](./img/Sysclk_sla5032_pcb_bottom.jpg)](./img/Sysclk_sla5032_pcb_bottom.jpg "Sysclk Sla5032 Pcb Bottom"){ .glightbox data-gallery="sysclk-sla5032" }
<span class="caption">Sysclk Sla5032 Pcb Bottom</span>

[![Sysclk Sla5032 Mx25l6445e 100mhz Crystal](./img/Sysclk_sla5032_mx25l6445e_100mhz_crystal.jpg)](./img/Sysclk_sla5032_mx25l6445e_100mhz_crystal.jpg "Sysclk Sla5032 Mx25l6445e 100mhz Crystal"){ .glightbox data-gallery="sysclk-sla5032" }
<span class="caption">Sysclk Sla5032 Mx25l6445e 100mhz Crystal</span>

[![Sysclk Sla5032 Atmel 24c256n](./img/Sysclk_sla5032_atmel_24c256n.jpg)](./img/Sysclk_sla5032_atmel_24c256n.jpg "Sysclk Sla5032 Atmel 24c256n"){ .glightbox data-gallery="sysclk-sla5032" }
<span class="caption">Sysclk Sla5032 Atmel 24c256n</span>

[![Sysclk Sla5032 Pcb Module Top](./img/Sysclk_sla5032_pcb_module_top.jpg)](./img/Sysclk_sla5032_pcb_module_top.jpg "Sysclk Sla5032 Pcb Module Top"){ .glightbox data-gallery="sysclk-sla5032" }
<span class="caption">Sysclk Sla5032 Pcb Module Top</span>

[![Sysclk Sla5032 Mx25l6445e](./img/Sysclk_sla5032_mx25l6445e.jpg)](./img/Sysclk_sla5032_mx25l6445e.jpg "Sysclk Sla5032 Mx25l6445e"){ .glightbox data-gallery="sysclk-sla5032" }
<span class="caption">Sysclk Sla5032 Mx25l6445e</span>

[![Sysclk Sla5032 Atmega8a 24mhz Crystal](./img/Sysclk_sla5032_atmega8a_24mhz_crystal.jpg)](./img/Sysclk_sla5032_atmega8a_24mhz_crystal.jpg "Sysclk Sla5032 Atmega8a 24mhz Crystal"){ .glightbox data-gallery="sysclk-sla5032" }
<span class="caption">Sysclk Sla5032 Atmega8a 24mhz Crystal</span>

[![Sysclk Sla5032 Ams1117 Y125](./img/Sysclk_sla5032_ams1117_y125.jpg)](./img/Sysclk_sla5032_ams1117_y125.jpg "Sysclk Sla5032 Ams1117 Y125"){ .glightbox data-gallery="sysclk-sla5032" }
<span class="caption">Sysclk Sla5032 Ams1117 Y125</span>

[![Sysclk Sla5032 Usb Cable](./img/Sysclk_sla5032_usb_cable.jpg)](./img/Sysclk_sla5032_usb_cable.jpg "Sysclk Sla5032 Usb Cable"){ .glightbox data-gallery="sysclk-sla5032" }
<span class="caption">Sysclk Sla5032 Usb Cable</span>

[![Sysclk Sla5032 Mugshot](./img/Sysclk_sla5032_mugshot.jpg)](./img/Sysclk_sla5032_mugshot.png "Sysclk Sla5032 Mugshot"){ .glightbox data-gallery="sysclk-sla5032" }
<span class="caption">Sysclk Sla5032 Mugshot</span>

</div>
## Firmware

In order to use this device, you need a firmware/bitstream file from the vendor software (from the CD-ROM shipped with the device or from a vendor download of the software). You can e.g. install the Windows vendor software, then get the file **C:\Program Files (x86)\SLA5032\bin\top.bit**, rename it to **sysclk-sla5032.bit** and place it in a location where [libsigrok](https://sigrok.org/wiki/Libsigrok) will search for firmware (see libsigrok's [README.devices](https://sigrok.org/gitweb/?p=libsigrok.git;a=blob;f=README.devices) file for details). 

## Resources
- [Random AliExpress SLA5032 vendor](https://web.archive.org/web/20170324192912/http://de.aliexpress.com/item/500M-32-channel-logic-analyzer-compatible-LOGIC-16-accurate-indicator-actual-parameters/32286574687.html)
- [Vendor software](https://translate.google.com/translate?sl=auto&tl=en&u=https%3A%2F%2Fwww.0933.me%2Fshare%2F3585641.html) (sla5032_2015_1_24.iso)
- [blog.csdn.net: DLL API function docs for the vendor software](https://translate.google.com/translate?sl=auto&tl=en&u=https%3A%2F%2Fblog.csdn.net%2Fmcupro%2Farticle%2Fdetails%2F40453157)

