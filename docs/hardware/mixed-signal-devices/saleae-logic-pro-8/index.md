---
title: Saleae Logic Pro 8
---

# Saleae Logic Pro 8

<div class="infobox" markdown>

![Saleae Logic Pro 8](./img/Saleae_logic_pro_8-pcb_bottom.jpg){ .infobox-image }

### Saleae Logic Pro 8

| | |
|---|---|
| **Status** | planned |
| **Source code** | [saleae-logic-pro](https://github.com/OpenTraceLab/OpenTraceCapture/tree/main/src/hardware/saleae-logic-pro) |
| **Channels** | 8 |
| **Samplerate** | 500/100MHz (4ch/8ch) |
| **Samplerate (state)** | — |
| **Triggers** | none (SW-only) |
| **Min/max voltage** | -25 — 25V tolerant |
| **Threshold voltage** | 1.2V to 12V digital, -10 to 10V analog |
| **Memory** | none |
| **Compression** | yes |
| **Price range** | $619 |
| **Website** | [saleae.com](https://www.saleae.com) |

</div>

The **Saleae Logic Pro 8** is a USB 3.0-based, 8-channel logic analyzer with 500/100MHz sampling rate (at 4/8 enabled channels) and analog sampling support on all 8 channels.

It is part of the second-generation Saleae Logic series, which consists of the Logic 4, Logic 8, Logic Pro 8 and Logic Pro 16. See [Saleae Logic](https://sigrok.org/wiki/Saleae_Logic) and [Saleae Logic8](https://sigrok.org/wiki/Saleae_Logic8) for the predecessor products.

The case requires a **Torx TX6** screwdriver to open.

See [Saleae Logic Pro 8/Info](https://sigrok.org/wiki/Saleae_Logic_Pro_8/Info) for more details (such as **lsusb -v** output) about the device.

**Note**: Saleae Logic Pro 8 support in sigrok should be considered experimental for now. Only the logic analyzer parts are currently implemented (analog sampling is not).

## Hardware
- **FPGA**: [Xilinx Spartan-6 XC6SLX9](https://www.xilinx.com/support/index.html/content/xilinx/en/supportNav/silicon_devices/fpga/spartan-6.html), 9,152 logic elements ([family overview](https://www.xilinx.com/support/documentation/data_sheets/ds160.pdf)) ([datasheet](https://www.xilinx.com/support/documentation/data_sheets/ds162.pdf))
- **USB interface chip**: [Cypress CYUSB3014-BZXI (FX3)](http://www.cypress.com/?mpn=CYUSB3014-BZXI) ([datasheet](http://www.cypress.com/?docID=50647))
- **ADCs**: 1x [Exar CDK8307B](https://www.exar.com/product/sensing-and-signal-conditioning/data-converters/analog-to-digital-converters/cdk8307b) ([datasheet](https://www.exar.com/ds/cdk8307_ds.pdf)) (seems to have same I2C reg mapping than HMCAD1100 used in [Saleae Logic Pro 16](https://sigrok.org/wiki/Saleae_Logic_Pro_16))
- **32Kbit I2C EEPROM**: [24C32A](https://www.microchip.com/wwwproducts/en/24C32A) ([datasheet](http://ww1.microchip.com/downloads/en/DeviceDoc/21163E.pdf))
- **6x amplifiers**: [Analog Devices ADA4891-4](http://www.analog.com/en/high-speed-op-amps/high-speed-rail-to-rail-amplifiers/ada4891-4/products/product.html) ([datasheet](http://www.analog.com/media/en/technical-documentation/data-sheets/ADA4891-1_4891-2_4891-3_4891-4.PDF))

## Photos

<div class="photo-grid" markdown>

[![Saleae Logic Pro 8 Pcb Bottom](./img/Saleae_logic_pro_8-pcb_bottom.jpg)](./img/Saleae_logic_pro_8-pcb_bottom.jpg "Saleae Logic Pro 8 Pcb Bottom"){ .glightbox data-gallery="saleae-logic-pro-8" }
<span class="caption">Saleae Logic Pro 8 Pcb Bottom</span>

[![Saleae Logic Pro 8 Cysub3014](./img/Saleae_logic_pro_8-cysub3014.jpg)](./img/Saleae_logic_pro_8-cysub3014.jpg "Saleae Logic Pro 8 Cysub3014"){ .glightbox data-gallery="saleae-logic-pro-8" }
<span class="caption">Saleae Logic Pro 8 Cysub3014</span>

[![Saleae Logic Pro 8 Bottom](./img/Saleae_logic_pro_8-bottom.png)](./img/Saleae_logic_pro_8-bottom.png "Saleae Logic Pro 8 Bottom"){ .glightbox data-gallery="saleae-logic-pro-8" }
<span class="caption">Saleae Logic Pro 8 Bottom</span>

[![Saleae Logic Pro 8 24c32a](./img/Saleae_logic_pro_8-24c32a.jpg)](./img/Saleae_logic_pro_8-24c32a.jpg "Saleae Logic Pro 8 24c32a"){ .glightbox data-gallery="saleae-logic-pro-8" }
<span class="caption">Saleae Logic Pro 8 24c32a</span>

[![Saleae Logic Pro 8 Xc6slx9](./img/Saleae_logic_pro_8-xc6slx9.jpg)](./img/Saleae_logic_pro_8-xc6slx9.jpg "Saleae Logic Pro 8 Xc6slx9"){ .glightbox data-gallery="saleae-logic-pro-8" }
<span class="caption">Saleae Logic Pro 8 Xc6slx9</span>

[![Saleae Logic Pro 8 Pcb Top](./img/Saleae_logic_pro_8-pcb_top.jpg)](./img/Saleae_logic_pro_8-pcb_top.jpg "Saleae Logic Pro 8 Pcb Top"){ .glightbox data-gallery="saleae-logic-pro-8" }
<span class="caption">Saleae Logic Pro 8 Pcb Top</span>

[![Saleae Logic Pro 8 Ada4891 4](./img/Saleae_logic_pro_8-ada4891-4.jpg)](./img/Saleae_logic_pro_8-ada4891-4.jpg "Saleae Logic Pro 8 Ada4891 4"){ .glightbox data-gallery="saleae-logic-pro-8" }
<span class="caption">Saleae Logic Pro 8 Ada4891 4</span>

[![Saleae Logic Pro 8 Cdk8307](./img/Saleae_logic_pro_8-cdk8307.jpg)](./img/Saleae_logic_pro_8-cdk8307.jpg "Saleae Logic Pro 8 Cdk8307"){ .glightbox data-gallery="saleae-logic-pro-8" }
<span class="caption">Saleae Logic Pro 8 Cdk8307</span>

</div>
## Firmware

You can use the [sigrok-fwextract-saleae-logic16](http://sigrok.org/gitweb/?p=sigrok-util.git;a=tree;f=firmware/saleae-logic16) (sic!) tool to extract (from the "Logic" Linux binary; tested with the Saleae 1.2.10 software) the FX3 firmware and the FPGA bitstreams required for using the Saleae Logic Pro 16:

```
$ **sigrok-fwextract-saleae-logic16 Logic**
saved 5217 bytes to saleae-logic16-fx2.fw
saved 149516 bytes to saleae-logic16-fpga-18.bitstream
saved 149516 bytes to saleae-logic16-fpga-33.bitstream
saved 178702 bytes from 46 blobs to saleae-logicpro16-fx3.fw
saved 178702 bytes from 46 blobs to **saleae-logicpro8-fx3.fw**
saved 465028 bytes to saleae-logicpro16-fpga.bitstream
saved 341160 bytes to **saleae-logicpro8-fpga.bitstream**

```

Copy these files to the directory where your [libsigrok](https://sigrok.org/wiki/Libsigrok) installation expects them (usually **/usr/local/share/sigrok-firmware**) and they will be found and used automatically by the libsigrok **saleae-logic-pro** driver.

**Note that sigrok-util (commit 20e302a2) only works Saleae Logic software up to 1.2.10&#160;!**

## Resources
- [User guide](https://support.saleae.com/user-guide)
- [Download vendor software](https://www.saleae.com/downloads)
- [Vendor software version 1.2.10 32-bit](https://downloads.saleae.com/logic/1.2.10/Logic%201.2.10%20(32-bit).zip) (needed to extract firmwares)
- [SDKs](https://support.saleae.com/saleae-api-and-sdk)

