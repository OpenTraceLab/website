---
title: KingST KQS3506-LA16100
---

# KingST KQS3506-LA16100

<div class="infobox" markdown>

![KingST KQS3506-LA16100](./img/Kingst_kqs3506_la16100_package.jpg){ .infobox-image }

### KingST KQS3506-LA16100

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
| **Website** | [taobao.com](http://item.taobao.com/item.htm?id=20369792793) |

</div>

The **KingST KQS3506-LA16100** is a USB-based, 16-channel logic analyzer with 100/50/32/16MHz sampling rate (at 3/6/9/16 enabled channels).

This is a clone of the [Saleae Logic16](https://sigrok.org/wiki/Saleae_Logic16).

See [KingST KQS3506-LA16100/Info](https://sigrok.org/wiki/KingST_KQS3506-LA16100/Info) for more details (such as **lsusb -v** output) about the device.

## Hardware
- **FPGA**: [Xilinx Spartan-3A XC3S200A](http://www.xilinx.com/support/index.html/content/xilinx/en/supportNav/silicon_devices/fpga/spartan-3a.html), 200K gates ([datasheet](http://www.xilinx.com/support/documentation/data_sheets/ds529.pdf))
- **CPLD**: [Altera EPM3032A](http://www.altera.com/literature/lit-m3k.jsp), 600 gates, 32 macrocells ([datasheet](http://www.altera.com/literature/ds/m3000a.pdf), [pinout](http://www.altera.com/literature/dp/max3k/epm3032a.pdf)).
- **USB interface chip**: [Cypress CY7C68013A-56PVXC (FX2LP)](http://www.cypress.com/?mpn=CY7C68013A-56PVXC) ([datasheet](http://www.cypress.com/?docID=34060))
- **I2C EEPROM**: [Microchip 24LC02B](http://www.microchip.com/wwwproducts/Devices.aspx?dDocName=en010810) ([datasheet](http://ww1.microchip.com/downloads/en/DeviceDoc/21709J.pdf))
- **3.3V voltage regulator**: [Advanced Monolithic Systems AMS1117-3.3](http://www.advanced-monolithic.com/products/voltreg.html#1117) ([datasheet](http://ams-semitech.com/attachments/File/AMS1117_20120314.pdf), [older datasheet](http://www.advanced-monolithic.com/pdf/ds1117.pdf))
- **1.2V voltage regulator**: [Advanced Monolithic Systems AMS1117-1.2](http://www.advanced-monolithic.com/products/voltreg.html#1117) ([datasheet](http://ams-semitech.com/attachments/File/AMS1117_20120314.pdf), [older datasheet](http://www.advanced-monolithic.com/pdf/ds1117.pdf))
- **Crystal**: 24.000

**Pinouts and connections:**

**I2C EEPROM:**

The Microchip 24LC02B is connected to the Cypress FX2. The **WP** pin of the EEPROM can be jumpered to low or high, in order to write-protect it (or not). The address pins (A0-A2) are all connected to GND, which makes the I2C slave address of the EEPROM 0x50.

| (GND) A0 | 1- | &#160;&#160;O | -8 | VCC (3.3V) |
|---|---|---|---|---|
| (GND) A1 | 2- | -7 | WP (jumper W2) |
| (GND) A2 | 3- | -6 | SCL (FX2 SCL) |
| GND | 4- | -5 | SDA (FX2 SDA) |

**CLPD:**

The Altera EPM3032A JTAG pins are available on the **J3** pin header.

| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |
|---|---|---|---|---|---|---|---|---|---|---|
| JTAG TDI | I/O (FX2 PA7) | I/O (FX2 PA6) | GND | I/O (FX2 PA5) | I/O (FX2 PA4) | JTAG TMS | I/O (FX2 PA3) | VCC | I/O (FX2 PA2) | GND |
| 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 |
| I/O (FX2 PA1) | I/O (FX2 PA0) | I/O (FPGA PROG_B) | I/O (FPGA 94, IO_L05N_0) | GND | VCC | I/O (FPGA 85, IO_L03P_0) | I/O (FX2 CTL2) | I/O (FX2 CTL1) | I/O (FX2 CTL0) | I/O (FPGA 51, DIN/MISO) |
| 23 | 24 | 25 | 26 | 27 | 28 | 29 | 30 | 31 | 32 | 33 |
| I/O (NC?) | GND | I/O (FPGA 97, IP0) | JTAG TCK | I/O (FPGA 53, CCLK) | I/O (NC?) | VCC | GND | I/O (FPGA 3, IO_L01P_3) | JTAG TDO | I/O (NC?) |
| 34 | 35 | 36 | 37 | 38 | 39 | 40 | 41 | 42 | 43 | 44 |
| I/O (NC?) | I/O (NC?) | GND | I/O (NC?) | I/O (NC?) | I/O (NC?) | I/O (NC?) | VCC | I/O (NC?) | I/O (NC?) | I/O (NC?) |

**JTAG header (CPLD):**

The **J3** pin header is a JTAG connector wired to the CPLD (it is **not** additionally wired to the FPGA in a JTAG chain). The pins are (from left to right):

| 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|
| TMS | TDI | TCK | TDO | GND | 3.3V |

## Photos

<div class="photo-grid" markdown>

[![Kingst Kqs3506 La16100 Package](./img/Kingst_kqs3506_la16100_package.jpg)](./img/Kingst_kqs3506_la16100_package.jpg "Kingst Kqs3506 La16100 Package"){ .glightbox data-gallery="kingst-kqs3506-la16100" }
<span class="caption">Kingst Kqs3506 La16100 Package</span>

[![Kingst Kqs3506 La16100 Input Stage1](./img/Kingst_kqs3506_la16100_input_stage1.jpg)](./img/Kingst_kqs3506_la16100_input_stage1.jpg "Kingst Kqs3506 La16100 Input Stage1"){ .glightbox data-gallery="kingst-kqs3506-la16100" }
<span class="caption">Kingst Kqs3506 La16100 Input Stage1</span>

[![Kingst Kqs3506 La16100](./img/Kingst_kqs3506_la16100.png)](./img/Kingst_kqs3506_la16100.png "Kingst Kqs3506 La16100"){ .glightbox data-gallery="kingst-kqs3506-la16100" }
<span class="caption">Kingst Kqs3506 La16100</span>

[![Kingst Kqs3506 La16100 Device Usb](./img/Kingst_kqs3506_la16100_device_usb.jpg)](./img/Kingst_kqs3506_la16100_device_usb.jpg "Kingst Kqs3506 La16100 Device Usb"){ .glightbox data-gallery="kingst-kqs3506-la16100" }
<span class="caption">Kingst Kqs3506 La16100 Device Usb</span>

[![Kingst Kqs3506 La16100 Xilinx Spartan Xc3s200a](./img/Kingst_kqs3506_la16100_xilinx_spartan_xc3s200a.jpg)](./img/Kingst_kqs3506_la16100_xilinx_spartan_xc3s200a.jpg "Kingst Kqs3506 La16100 Xilinx Spartan Xc3s200a"){ .glightbox data-gallery="kingst-kqs3506-la16100" }
<span class="caption">Kingst Kqs3506 La16100 Xilinx Spartan Xc3s200a</span>

[![Kingst Kqs3506 La16100 Cypress Fx2](./img/Kingst_kqs3506_la16100_cypress_fx2.jpg)](./img/Kingst_kqs3506_la16100_cypress_fx2.jpg "Kingst Kqs3506 La16100 Cypress Fx2"){ .glightbox data-gallery="kingst-kqs3506-la16100" }
<span class="caption">Kingst Kqs3506 La16100 Cypress Fx2</span>

[![Kingst Kqs3506 La16100 Altera Epm3032a](./img/Kingst_kqs3506_la16100_altera_epm3032a.jpg)](./img/Kingst_kqs3506_la16100_altera_epm3032a.jpg "Kingst Kqs3506 La16100 Altera Epm3032a"){ .glightbox data-gallery="kingst-kqs3506-la16100" }
<span class="caption">Kingst Kqs3506 La16100 Altera Epm3032a</span>

[![Kingst Kqs3506 La16100 Ams1117 12](./img/Kingst_kqs3506_la16100_ams1117_12.jpg)](./img/Kingst_kqs3506_la16100_ams1117_12.jpg "Kingst Kqs3506 La16100 Ams1117 12"){ .glightbox data-gallery="kingst-kqs3506-la16100" }
<span class="caption">Kingst Kqs3506 La16100 Ams1117 12</span>

[![Kingst Kqs3506 La16100 Paper](./img/Kingst_kqs3506_la16100_paper.jpg)](./img/Kingst_kqs3506_la16100_paper.jpg "Kingst Kqs3506 La16100 Paper"){ .glightbox data-gallery="kingst-kqs3506-la16100" }
<span class="caption">Kingst Kqs3506 La16100 Paper</span>

[![Kingst Kqs3506 La16100 Ams1117 33](./img/Kingst_kqs3506_la16100_ams1117_33.jpg)](./img/Kingst_kqs3506_la16100_ams1117_33.jpg "Kingst Kqs3506 La16100 Ams1117 33"){ .glightbox data-gallery="kingst-kqs3506-la16100" }
<span class="caption">Kingst Kqs3506 La16100 Ams1117 33</span>

[![Kingst Kqs3506 La16100 At88sc0104 Silkscreen](./img/Kingst_kqs3506_la16100_at88sc0104_silkscreen.jpg)](./img/Kingst_kqs3506_la16100_at88sc0104_silkscreen.jpg "Kingst Kqs3506 La16100 At88sc0104 Silkscreen"){ .glightbox data-gallery="kingst-kqs3506-la16100" }
<span class="caption">Kingst Kqs3506 La16100 At88sc0104 Silkscreen</span>

[![Kingst Kqs3506 La16100 Pcb Bottom](./img/Kingst_kqs3506_la16100_pcb_bottom.jpg)](./img/Kingst_kqs3506_la16100_pcb_bottom.jpg "Kingst Kqs3506 La16100 Pcb Bottom"){ .glightbox data-gallery="kingst-kqs3506-la16100" }
<span class="caption">Kingst Kqs3506 La16100 Pcb Bottom</span>

[![Kingst Kqs3506 La16100 Device Connector](./img/Kingst_kqs3506_la16100_device_connector.jpg)](./img/Kingst_kqs3506_la16100_device_connector.jpg "Kingst Kqs3506 La16100 Device Connector"){ .glightbox data-gallery="kingst-kqs3506-la16100" }
<span class="caption">Kingst Kqs3506 La16100 Device Connector</span>

[![Kingst Kqs3506 La16100 Schematic V6](./img/Kingst_kqs3506_la16100_schematic_v6.png)](./img/Kingst_kqs3506_la16100_schematic_v6.png "Kingst Kqs3506 La16100 Schematic V6"){ .glightbox data-gallery="kingst-kqs3506-la16100" }
<span class="caption">Kingst Kqs3506 La16100 Schematic V6</span>

[![Kingst Kqs3506 La16100 Device Top](./img/Kingst_kqs3506_la16100_device_top.jpg)](./img/Kingst_kqs3506_la16100_device_top.jpg "Kingst Kqs3506 La16100 Device Top"){ .glightbox data-gallery="kingst-kqs3506-la16100" }
<span class="caption">Kingst Kqs3506 La16100 Device Top</span>

[![Kingst Kqs3506 La16100 Device Bottom](./img/Kingst_kqs3506_la16100_device_bottom.jpg)](./img/Kingst_kqs3506_la16100_device_bottom.jpg "Kingst Kqs3506 La16100 Device Bottom"){ .glightbox data-gallery="kingst-kqs3506-la16100" }
<span class="caption">Kingst Kqs3506 La16100 Device Bottom</span>

[![Kingst Kqs3506 La16100 Pcb V6 Top](./img/Kingst_kqs3506_la16100_pcb_v6_top.jpg)](./img/Kingst_kqs3506_la16100_pcb_v6_top.jpg "Kingst Kqs3506 La16100 Pcb V6 Top"){ .glightbox data-gallery="kingst-kqs3506-la16100" }
<span class="caption">Kingst Kqs3506 La16100 Pcb V6 Top</span>

[![Kingst Kqs3506 La16100 Inputstage 2](./img/Kingst_kqs3506_la16100_inputstage_2.jpg)](./img/Kingst_kqs3506_la16100_inputstage_2.jpg "Kingst Kqs3506 La16100 Inputstage 2"){ .glightbox data-gallery="kingst-kqs3506-la16100" }
<span class="caption">Kingst Kqs3506 La16100 Inputstage 2</span>

[![Kingst Kqs3506 La16100 Microchip 24lc02b](./img/Kingst_kqs3506_la16100_microchip_24lc02b.jpg)](./img/Kingst_kqs3506_la16100_microchip_24lc02b.jpg "Kingst Kqs3506 La16100 Microchip 24lc02b"){ .glightbox data-gallery="kingst-kqs3506-la16100" }
<span class="caption">Kingst Kqs3506 La16100 Microchip 24lc02b</span>

[![Kingst Kqs3506 La16100 Pcb V6 Bottom](./img/Kingst_kqs3506_la16100_pcb_v6_bottom.jpg)](./img/Kingst_kqs3506_la16100_pcb_v6_bottom.jpg "Kingst Kqs3506 La16100 Pcb V6 Bottom"){ .glightbox data-gallery="kingst-kqs3506-la16100" }
<span class="caption">Kingst Kqs3506 La16100 Pcb V6 Bottom</span>

[![Kingst Kqs3506 La16100 Pcb Top](./img/Kingst_kqs3506_la16100_pcb_top.jpg)](./img/Kingst_kqs3506_la16100_pcb_top.jpg "Kingst Kqs3506 La16100 Pcb Top"){ .glightbox data-gallery="kingst-kqs3506-la16100" }
<span class="caption">Kingst Kqs3506 La16100 Pcb Top</span>

</div>
## Firmware

See [Saleae_Logic16#Firmware](https://sigrok.org/wiki/Saleae_Logic16#Firmware).

## Protocol

See [Saleae_Logic16#Protocol](https://sigrok.org/wiki/Saleae_Logic16#Protocol).

## Resources
- [kstmcu.taobao.com](http://kstmcu.taobao.com/)
- [kingst.org forum](http://www.kingst.org/forum/index)
- [MCU123 article](http://translate.google.com/translate?sl=zh-CN&tl=en&js=n&prev=_t&hl=de&ie=UTF-8&eotf=1&u=http%3A%2F%2Fwww.mcu123.com%2Fnews%2FArticle%2FPC%2FPCB%2F201210%2F4905.html&act=url)

