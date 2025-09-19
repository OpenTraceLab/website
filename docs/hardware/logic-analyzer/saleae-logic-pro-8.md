# Saleae Logic Pro 8
| | | |:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------------------------------:| | [*Image: \1* | | | Status | planned | | Source code | [saleae-logic-pro](http://github.com/OpenTraceLab/?p=OpenTraceCapture.git;a=tree;f=src/hardware/saleae-logic-pro) | | Channels | 8 | | Samplerate | 500/100MHz (4ch/8ch) | | Samplerate (state) | — | | Triggers | none (SW-only) | | Min/max voltage | -25 — 25V tolerant | | Threshold voltage | 1.2V to 12V digital, -10 to 10V analog | | Memory | none | | Compression | yes | | Price range | \$619 | | Website | [saleae.com](https://www.saleae.com) | **Saleae Logic Pro 8** The **Saleae Logic Pro 8** is a USB 3.0-based, 8-channel logic analyzer with 500/100MHz sampling rate (at 4/8 enabled channels) and analog sampling support on all 8 channels. It is part of the second-generation Saleae Logic series, which consists of the Logic 4, Logic 8, Logic Pro 8 and Logic Pro 16. See *Saleae Logic* and *Saleae Logic8* for the predecessor products. The case requires a **Torx TX6** screwdriver to open. See *Saleae Logic Pro 8/Info* for more details (such as **lsusb -v** output) about the device. **Note**: Saleae Logic Pro 8 support in OpenTraceLab should be considered experimental for now. Only the logic analyzer parts are currently implemented (analog sampling is not).
## Contents
\- *1 Hardware* \- *2 Photos* \- *3 Firmware* \- *4 Resources*
## Hardware \- **FPGA**: *Xilinx Spartan-6 XC6SLX9*, 9,152 logic elements ([family overview](https://www.xilinx.com/support/documentation/data_sheets/ds160.pdf)) ([datasheet](https://www.xilinx.com/support/documentation/data_sheets/ds162.pdf)) \- **USB interface chip**: [Cypress CYUSB3014-BZXI (FX3)](http://www.cypress.com/?mpn=CYUSB3014-BZXI) ([datasheet](http://www.cypress.com/?docID=50647)) \- **ADCs**: 1x [Exar CDK8307B](https://www.exar.com/product/sensing-and-signal-conditioning/data-converters/analog-to-digital-converters/cdk8307b) ([datasheet](https://www.exar.com/ds/cdk8307_ds.pdf)) (seems to have same I2C reg mapping than HMCAD1100 used in *Saleae Logic Pro 16*) \- **32Kbit I2C EEPROM**: [24C32A](https://www.microchip.com/wwwproducts/en/24C32A) ([datasheet](http://ww1.microchip.com/downloads/en/DeviceDoc/21163E.pdf)) \- **6x amplifiers**: *Analog Devices ADA4891-4* ([datasheet](http://www.analog.com/media/en/technical-documentation/data-sheets/ADA4891-1_4891-2_4891-3_4891-4.PDF)) ## Photos \-
[*Image: \1*
Device, bottom
\-
[*Image: \1*
PCB, top
\-
[*Image: \1*
PCB, bottom
\-
[*Image: \1*
XC6SLX9 IC
\-
[*Image: \1*
CYUSB3014-BZXI IC
\-
[*Image: \1*
CDK8307 IC
\-
[*Image: \1*
24c32A IC
\-
[*Image: \1*
ADA4891-4 IC
## Firmware You can use the [OpenTraceLab-fwextract-saleae-logic16](http://github.com/OpenTraceLab/?p=OpenTraceLab-util.git;a=tree;f=firmware/saleae-logic16) (sic!) tool to extract (from the "Logic" Linux binary; tested with the Saleae 1.2.10 software) the FX3 firmware and the FPGA bitstreams required for using the Saleae Logic Pro 16: $ OpenTraceLab-fwextract-saleae-logic16 Logic saved 5217 bytes to saleae-logic16-fx2.fw saved 149516 bytes to saleae-logic16-fpga-18.bitstream saved 149516 bytes to saleae-logic16-fpga-33.bitstream saved 178702 bytes from 46 blobs to saleae-logicpro16-fx3.fw saved 178702 bytes from 46 blobs to saleae-logicpro8-fx3.fw saved 465028 bytes to saleae-logicpro16-fpga.bitstream saved 341160 bytes to saleae-logicpro8-fpga.bitstream Copy these files to the directory where your *OpenTraceCapture* installation expects them (usually **/usr/local/share/OpenTraceLab-firmware**) and they will be found and used automatically by the OpenTraceCapture **saleae-logic-pro** driver. **Note that OpenTraceLab-util (commit 20e302a2) only works Saleae Logic software up to 1.2.10 !** ## Resources \- [User guide](https://support.saleae.com/user-guide) \- [Download vendor software](https://www.saleae.com/downloads) \- [Vendor software version 1.2.10 32-bit](https://downloads.saleae.com/logic/1.2.10/Logic%201.2.10%20\(32-bit\).zip) (needed to extract firmwares) \- [SDKs](https://support.saleae.com/saleae-api-and-sdk)
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=Saleae_Logic_Pro_8&oldid=14400](https://OpenTraceLab.org/w/index.php?title=Saleae_Logic_Pro_8&oldid=14400)"
: \- *Device* \- *Logic analyzer* \- *Oscilloscope* \- *Mixed-signal oscilloscope* \- *Planned*
## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
