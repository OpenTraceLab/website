---
title: Saleae Logic Pro 16
---

# Saleae Logic Pro 16

<div class="infobox" markdown>

![Saleae Logic Pro 16](./img/Saleae_Logic_Pro_16_bottom.jpg){ .infobox-image }

### Saleae Logic Pro 16

| | |
|---|---|
| **Status** | supported |
| **Source code** | [saleae-logic-pro](https://github.com/OpenTraceLab/OpenTraceCapture/tree/main/src/hardware/saleae-logic-pro) |
| **Channels** | 16 |
| **Samplerate** | 500/100MHz (4ch/16ch) |
| **Samplerate (state)** | — |
| **Triggers** | none (SW-only) |
| **Min/max voltage** | -50 — 50V tolerant |
| **Threshold voltage** | 1.2V to 5.5V digital, 0 to 10V analog |
| **Memory** | none |
| **Compression** | yes |
| **Website** | [saleae.com](https://www.saleae.com) |

</div>

The **Saleae Logic Pro 16** is a USB 3.0-based, 16-channel logic analyzer with 500/100MHz sampling rate (at 4/16 enabled channels) and analog sampling support on all 16 channels.

It is part of the second-generation Saleae Logic series, which consists of the Logic 4, Logic 8, Logic Pro 8 and Logic Pro 16. See [Saleae Logic](https://sigrok.org/wiki/Saleae_Logic) and [Saleae Logic16](https://sigrok.org/wiki/Saleae_Logic16) for the predecessor products.

The case requires a **Torx T9** screwdriver to open.

See [Saleae Logic Pro 16/Info](https://sigrok.org/wiki/Saleae_Logic_Pro_16/Info) for more details (such as **lsusb -v** output) about the device.

**Note**: Saleae Logic Pro 16 support in sigrok should be considered experimental for now. Only the logic analyzer parts are currently implemented (analog sampling is not).

## Hardware
- **FPGA**: [Xilinx Spartan-6 XC6SLX16](http://www.xilinx.com/support/index.html/content/xilinx/en/supportNav/silicon_devices/fpga/spartan-6.html), 14,579 logic elements ([family overview](http://www.xilinx.com/support/documentation/data_sheets/ds160.pdf)) ([datasheet](http://www.xilinx.com/support/documentation/data_sheets/ds162.pdf))
- **USB interface chip**: [Cypress CYUSB3014-BZXI (FX3)](http://www.cypress.com/?mpn=CYUSB3014-BZXI) ([datasheet](http://www.cypress.com/?docID=50647))
- **ADCs**: 2x [Hittite Microwave HMCAD1100](https://www.hittite.com/products/view.html/view/HMCAD1100) ([datasheet](https://www.hittite.com/content/documents/data_sheet/hmcad1100.pdf))
- **32Kbit I2C EEPROM**: [24C32A](http://www.microchip.com/wwwproducts/Devices.aspx?dDocName=en010774) ([datasheet](http://ww1.microchip.com/downloads/en/DeviceDoc/21709J.pdf))
- **12x amplifiers**: [Analog Devices ADA4891-4](http://www.analog.com/en/high-speed-op-amps/high-speed-rail-to-rail-amplifiers/ada4891-4/products/product.html) ([datasheet](http://www.analog.com/static/imported-files/data_sheets/ADA4891-1_4891-2_4891-3_4891-4.PDF))
- This list is not yet complete.

There are several testpoints on the underside of the PCB. It is not yet certain what these are for. There is no visible JTAG header.

## Photos

<div class="photo-grid" markdown>

[![Saleae Logic Pro 16 Bottom](./img/Saleae_Logic_Pro_16_bottom.jpg)](./img/Saleae_Logic_Pro_16_bottom.jpg "Saleae Logic Pro 16 Bottom"){ .glightbox data-gallery="saleae-logic-pro-16" }
<span class="caption">Saleae Logic Pro 16 Bottom</span>

[![Saleae Logic Pro 16 Top](./img/Saleae_Logic_Pro_16_top.jpg)](./img/Saleae_Logic_Pro_16_top.jpg "Saleae Logic Pro 16 Top"){ .glightbox data-gallery="saleae-logic-pro-16" }
<span class="caption">Saleae Logic Pro 16 Top</span>

[![Saleae Logic Pro 16 Front](./img/Saleae_Logic_Pro_16_front.jpg)](./img/Saleae_Logic_Pro_16_front.jpg "Saleae Logic Pro 16 Front"){ .glightbox data-gallery="saleae-logic-pro-16" }
<span class="caption">Saleae Logic Pro 16 Front</span>

[![Saleae Logic Pro 16 Pcb Front](./img/Saleae_Logic_Pro_16_PCB_front.jpg)](./img/Saleae_Logic_Pro_16_PCB_front.jpg "Saleae Logic Pro 16 Pcb Front"){ .glightbox data-gallery="saleae-logic-pro-16" }
<span class="caption">Saleae Logic Pro 16 Pcb Front</span>

[![Saleae Logic Pro 16 Pcb Rear](./img/Saleae_Logic_Pro_16_PCB_rear.jpg)](./img/Saleae_Logic_Pro_16_PCB_rear.jpg "Saleae Logic Pro 16 Pcb Rear"){ .glightbox data-gallery="saleae-logic-pro-16" }
<span class="caption">Saleae Logic Pro 16 Pcb Rear</span>

</div>
## Firmware

You can use the [sigrok-fwextract-saleae-logic16](http://sigrok.org/gitweb/?p=sigrok-util.git;a=tree;f=firmware/saleae-logic16) (sic!) tool to extract (from the "Logic" Linux binary; tested with the Saleae 1.2.10 software) the FX3 firmware and the FPGA bitstreams required for using the Saleae Logic Pro 16:

```
$ **sigrok-fwextract-saleae-logic16 Logic**
saved 5217 bytes to saleae-logic16-fx2.fw
saved 149516 bytes to saleae-logic16-fpga-18.bitstream
saved 149516 bytes to saleae-logic16-fpga-33.bitstream
saved 178702 bytes from 46 blobs to **saleae-logicpro16-fx3.fw**
saved 178702 bytes from 46 blobs to saleae-logicpro8-fx3.fw
saved 465028 bytes to **saleae-logicpro16-fpga.bitstream**
saved 341160 bytes to saleae-logicpro8-fpga.bitstream

```

Copy these files to the directory where your [libsigrok](https://sigrok.org/wiki/Libsigrok) installation expects them (usually **/usr/local/share/sigrok-firmware**) and they will be found and used automatically by the libsigrok **saleae-logic-pro** driver.

Links to compatible Saleae logic versions for the firmware extractor:

- [https://downloads.saleae.com/logic/1.2.10/Logic%201.2.10%20(64-bit).zip](https://downloads.saleae.com/logic/1.2.10/Logic%201.2.10%20(64-bit).zip)
- [https://web.archive.org/web/20201019100155/https://downloads.saleae.com/logic/1.2.10/Logic%201.2.10%20%2864-bit%29.zip](https://web.archive.org/web/20201019100155/https://downloads.saleae.com/logic/1.2.10/Logic%201.2.10%20%2864-bit%29.zip)
## Resources
- [Manual](http://support.saleae.com/hc/en-us/sections/200114124-get-started-using-the-saleae-logic-analyzer)
- [Vendor software](http://www.saleae.com/downloads)
- [SDKs](http://support.saleae.com/hc/en-us/categories/200077184-sdks-automation-betas)

