---
title: Noname XL-LOGIC16-100M
---

# Noname XL-LOGIC16-100M

<div class="infobox" markdown>

![Noname XL-LOGIC16-100M](./img/Noname_xl_logic16_100m_cypress_fx2lp.jpg){ .infobox-image }

### Noname XL-LOGIC16-100M

| | |
|---|---|
| **Status** | in progress |
| **Source code** | [saleae-logic16](https://github.com/OpenTraceLab/OpenTraceCapture/tree/main/src/hardware/saleae-logic16) |
| **Channels** | 3/6/9/16 |
| **Samplerate** | 100/50/32/16MHz |
| **Samplerate (state)** | — |
| **Triggers** | none (SW-only) |
| **Min/max voltage** | -0.9V — 6V |
| **Threshold voltage** | configurable:for 1.8V to 3.6V systems: VIH=1.4V, VIL=0.7Vfor 5V systems: VIH=3.6V, VIL=1.4V |
| **Memory** | none |
| **Compression** | yes |
| **Price range** | $30 - $35 |
| **Website** | [aliexpress.com](http://www.aliexpress.com/item/Free-Shipping-Saleae-24MHz-8Channels-Logic-Analyzer-Fully-Checked-Best-quality-Input-buffered/1731200392.html) |

</div>

The **Noname  XL-LOGIC16-100M** is a USB-based, 16-channel logic analyzer with up to 100MHz sampling rate.

It is labelled and sold as a [Saleae Logic16](https://sigrok.org/wiki/Saleae_Logic16) clone, and comes with "modified" Saleae Logic software on a CD-ROM.

See [Noname XL-LOGIC16-100M/Info](https://sigrok.org/wiki/Noname_XL-LOGIC16-100M/Info) for more details (such as **lsusb -v** output) about the device.

## Variants in same case

The 2015-1-8 version of the [Mcupro_Logic16_clone](https://sigrok.org/wiki/Mcupro_Logic16_clone) comes in the same case as this device.  Unlike this device, the mcupro version works with sigrok!

## Hardware

A single Phillips head screw holds the case together. Most notable are the complete lack of test points or programming headers! There are some unpopulated resistor/capacitor pairs on the backside.

- **FPGA**: [Xilinx Spartan-3A XC3S200A](http://www.xilinx.com/support/index.html/content/xilinx/en/supportNav/silicon_devices/fpga/spartan-3a.html), 200K gates ([datasheeet](http://www.xilinx.com/support/documentation/data_sheets/ds529.pdf))
- **USB interface chip**: [Cypress CY7C68013A-56PVXC (FX2LP)](http://www.cypress.com/?mpn=CY7C68013A-56PVXC) ([datasheet](http://www.cypress.com/?docID=34060))
- **I2C EEPROM**: 2Kbit [Atmel 24C02B](http://www.atmel.com/devices/AT24C02B.aspx) (markings: "ATMEL317 24C02BN SU27 D") ([datasheet](http://www.atmel.com/Images/doc5126.pdf))
- **16-Bit 2.5V to 3.3V/3.3V to 5V level shifting transceiver with 3-state outputs**: [TI SN74ALVC164245](http://www.ti.com/product/SN74ALVC164245) ([datasheet](http://www.ti.com/lit/gpn/sn74alvc164245))
- **3.3V voltage regulator**: [Advanced Monolithic Systems AMS1117-3.3](http://www.advanced-monolithic.com/products/voltreg.html#1117) ([datasheet](http://ams-semitech.com/attachments/File/AMS1117_20120314.pdf), [older datasheet](http://www.advanced-monolithic.com/pdf/ds1117.pdf))
- **1.2V voltage regulator**: [Advanced Monolithic Systems AMS1117-1.2](http://www.advanced-monolithic.com/products/voltreg.html#1117) ([datasheet](http://ams-semitech.com/attachments/File/AMS1117_20120314.pdf), [older datasheet](http://www.advanced-monolithic.com/pdf/ds1117.pdf))
- **Crystal:** 24.000

Three LEDs (USB/green, COM/blue, and RUN/red) are on the board.

## Photos

<div class="photo-grid" markdown>

[![Noname Xl Logic16 100m Cypress Fx2lp](./img/Noname_xl_logic16_100m_cypress_fx2lp.jpg)](./img/Noname_xl_logic16_100m_cypress_fx2lp.jpg "Noname Xl Logic16 100m Cypress Fx2lp"){ .glightbox data-gallery="noname-xl-logic16-100m" }
<span class="caption">Noname Xl Logic16 100m Cypress Fx2lp</span>

[![Noname Xl Logic16 100m Pcb Top](./img/Noname_xl_logic16_100m_pcb_top.jpg)](./img/Noname_xl_logic16_100m_pcb_top.jpg "Noname Xl Logic16 100m Pcb Top"){ .glightbox data-gallery="noname-xl-logic16-100m" }
<span class="caption">Noname Xl Logic16 100m Pcb Top</span>

[![Xl Logic16 100m Black Pcb Top](./img/Xl_logic16_100m_black_pcb_top.jpg)](./img/Xl_logic16_100m_black_pcb_top.jpg "Xl Logic16 100m Black Pcb Top"){ .glightbox data-gallery="noname-xl-logic16-100m" }
<span class="caption">Xl Logic16 100m Black Pcb Top</span>

[![Noname Xl Logic16 100m Package](./img/Noname_xl_logic16_100m_package.jpg)](./img/Noname_xl_logic16_100m_package.jpg "Noname Xl Logic16 100m Package"){ .glightbox data-gallery="noname-xl-logic16-100m" }
<span class="caption">Noname Xl Logic16 100m Package</span>

[![Xl Logic16 100m Pcb Bottom](./img/Xl-logic16-100m-pcb-bottom.jpg)](./img/Xl-logic16-100m-pcb-bottom.jpg "Xl Logic16 100m Pcb Bottom"){ .glightbox data-gallery="noname-xl-logic16-100m" }
<span class="caption">Xl Logic16 100m Pcb Bottom</span>

[![Xl Logic16 100m Black Pcb Bottom](./img/Xl_logic16_100m_black_pcb_bottom.jpg)](./img/Xl_logic16_100m_black_pcb_bottom.jpg "Xl Logic16 100m Black Pcb Bottom"){ .glightbox data-gallery="noname-xl-logic16-100m" }
<span class="caption">Xl Logic16 100m Black Pcb Bottom</span>

[![Noname Xl Logic16 100m Ams1117 12](./img/Noname_xl_logic16_100m_ams1117_12.jpg)](./img/Noname_xl_logic16_100m_ams1117_12.jpg "Noname Xl Logic16 100m Ams1117 12"){ .glightbox data-gallery="noname-xl-logic16-100m" }
<span class="caption">Noname Xl Logic16 100m Ams1117 12</span>

[![Noname Xl Logic16 100m Pcb Bottom](./img/Noname_xl_logic16_100m_pcb_bottom.jpg)](./img/Noname_xl_logic16_100m_pcb_bottom.jpg "Noname Xl Logic16 100m Pcb Bottom"){ .glightbox data-gallery="noname-xl-logic16-100m" }
<span class="caption">Noname Xl Logic16 100m Pcb Bottom</span>

[![Noname Xl Logic16 100m Device Connector](./img/Noname_xl_logic16_100m_device_connector.jpg)](./img/Noname_xl_logic16_100m_device_connector.jpg "Noname Xl Logic16 100m Device Connector"){ .glightbox data-gallery="noname-xl-logic16-100m" }
<span class="caption">Noname Xl Logic16 100m Device Connector</span>

[![Xl Logic16 100m V2 Bottom](./img/Xl-logic16-100m-v2-bottom.jpg)](./img/Xl-logic16-100m-v2-bottom.jpg "Xl Logic16 100m V2 Bottom"){ .glightbox data-gallery="noname-xl-logic16-100m" }
<span class="caption">Xl Logic16 100m V2 Bottom</span>

[![Noname Xl Logic16 100m Device Bottom](./img/Noname_xl_logic16_100m_device_bottom.jpg)](./img/Noname_xl_logic16_100m_device_bottom.jpg "Noname Xl Logic16 100m Device Bottom"){ .glightbox data-gallery="noname-xl-logic16-100m" }
<span class="caption">Noname Xl Logic16 100m Device Bottom</span>

[![Xl Logic16 100m V2 External](./img/Xl-logic16-100m-v2-external.jpg)](./img/Xl-logic16-100m-v2-external.jpg "Xl Logic16 100m V2 External"){ .glightbox data-gallery="noname-xl-logic16-100m" }
<span class="caption">Xl Logic16 100m V2 External</span>

[![Noname Xl Logic16 100m Device Usb](./img/Noname_xl_logic16_100m_device_usb.jpg)](./img/Noname_xl_logic16_100m_device_usb.jpg "Noname Xl Logic16 100m Device Usb"){ .glightbox data-gallery="noname-xl-logic16-100m" }
<span class="caption">Noname Xl Logic16 100m Device Usb</span>

[![Noname Xl Logic16 100m Mugshot](./img/Noname_xl_logic16_100m_mugshot.png)](./img/Noname_xl_logic16_100m_mugshot.png "Noname Xl Logic16 100m Mugshot"){ .glightbox data-gallery="noname-xl-logic16-100m" }
<span class="caption">Noname Xl Logic16 100m Mugshot</span>

[![Xl Logic16 100m External](./img/Xl-logic16-100m-external.jpg)](./img/Xl-logic16-100m-external.jpg "Xl Logic16 100m External"){ .glightbox data-gallery="noname-xl-logic16-100m" }
<span class="caption">Xl Logic16 100m External</span>

[![Xl Logic16 100m Black Device Top](./img/Xl_logic16_100m_black_device_top.jpg)](./img/Xl_logic16_100m_black_device_top.jpg "Xl Logic16 100m Black Device Top"){ .glightbox data-gallery="noname-xl-logic16-100m" }
<span class="caption">Xl Logic16 100m Black Device Top</span>

[![Xl Logic16 100m V2 Top](./img/Xl-logic16-100m-v2-top.jpg)](./img/Xl-logic16-100m-v2-top.jpg "Xl Logic16 100m V2 Top"){ .glightbox data-gallery="noname-xl-logic16-100m" }
<span class="caption">Xl Logic16 100m V2 Top</span>

[![Noname Xl Logic16 100m Device Top](./img/Noname_xl_logic16_100m_device_top.jpg)](./img/Noname_xl_logic16_100m_device_top.jpg "Noname Xl Logic16 100m Device Top"){ .glightbox data-gallery="noname-xl-logic16-100m" }
<span class="caption">Noname Xl Logic16 100m Device Top</span>

[![Noname Xl Logic16 100m Atmel 24c02bn](./img/Noname_xl_logic16_100m_atmel_24c02bn.jpg)](./img/Noname_xl_logic16_100m_atmel_24c02bn.jpg "Noname Xl Logic16 100m Atmel 24c02bn"){ .glightbox data-gallery="noname-xl-logic16-100m" }
<span class="caption">Noname Xl Logic16 100m Atmel 24c02bn</span>

[![Noname Xl Logic16 100m Ti Alvc164245](./img/Noname_xl_logic16_100m_ti_alvc164245.jpg)](./img/Noname_xl_logic16_100m_ti_alvc164245.jpg "Noname Xl Logic16 100m Ti Alvc164245"){ .glightbox data-gallery="noname-xl-logic16-100m" }
<span class="caption">Noname Xl Logic16 100m Ti Alvc164245</span>

[![Noname Xl Logic16 100m Xilinx Spartan Xc3s200a](./img/Noname_xl_logic16_100m_xilinx_spartan_xc3s200a.jpg)](./img/Noname_xl_logic16_100m_xilinx_spartan_xc3s200a.jpg "Noname Xl Logic16 100m Xilinx Spartan Xc3s200a"){ .glightbox data-gallery="noname-xl-logic16-100m" }
<span class="caption">Noname Xl Logic16 100m Xilinx Spartan Xc3s200a</span>

[![Noname Xl Logic16 100m V05](./img/Noname_xl_logic16_100m_v05.jpg)](./img/Noname_xl_logic16_100m_v05.jpg "Noname Xl Logic16 100m V05"){ .glightbox data-gallery="noname-xl-logic16-100m" }
<span class="caption">Noname Xl Logic16 100m V05</span>

[![Xl Logic16 100m Pcb Top](./img/Xl-logic16-100m-pcb-top.jpg)](./img/Xl-logic16-100m-pcb-top.jpg "Xl Logic16 100m Pcb Top"){ .glightbox data-gallery="noname-xl-logic16-100m" }
<span class="caption">Xl Logic16 100m Pcb Top</span>

[![Noname Xl Logic16 100m Ams1117 33](./img/Noname_xl_logic16_100m_ams1117_33.jpg)](./img/Noname_xl_logic16_100m_ams1117_33.jpg "Noname Xl Logic16 100m Ams1117 33"){ .glightbox data-gallery="noname-xl-logic16-100m" }
<span class="caption">Noname Xl Logic16 100m Ams1117 33</span>

</div>
## Firmware

You can use the [sigrok-fwextract-saleae-logic16](http://sigrok.org/gitweb/?p=sigrok-util.git;a=tree;f=firmware/saleae-logic16) tool to extract (from the "Logic" Linux binary) the FX2 firmware and the FPGA bitstreams, exactly [as for a real Saleae Logic16](https://sigrok.org/wiki/Saleae_Logic16). Note, the md5sum of the FX2 firmware is identical to the original Saleae firmware, but the FPGA bitstreams are different. Attempting to connect to this device with the "modified" FPGA bitstream, which _works_ with the vendor supplied "modified" Logic software fails to load in sigrok, with a FPGA version mismatch. The FX2 firmware loads successfully, at least in as much as the LED blinks a heartbeat pattern as expected.

Update: July 4, 2015: marcus_c has written some open source fpga bitstream for spartan based logic16s, and _this_ bitstream does work with this device.  However, at this time, binaries are not available.  See [[1]](https://github.com/zeldin/logic16_bitstream) for the source.
Update: September 3, 2015 blight has an alternative open source fpga bitstream.  It also works.  See [[2]](https://github.com/gregani/la16fw) for both source and binaries

## Protocol

See [Saleae Logic16#Protocol](https://sigrok.org/wiki/Saleae_Logic16#Protocol).

## Resources
- Random aliexpress.com vendors: [vendor1](http://www.aliexpress.com/item/Free-Shipping-Saleae-24MHz-8Channels-Logic-Analyzer-Fully-Checked-Best-quality-Input-buffered/1731200392.html), [vendor2](http://www.aliexpress.com/item/Saleae-logic16-USB-100MHz-Real-Time-Logic-Analyzers/1856825810.html)

