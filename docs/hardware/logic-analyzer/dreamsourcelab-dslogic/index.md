---
title: DreamSourceLab DSLogic
---

# DreamSourceLab DSLogic

<div class="infobox" markdown>

![DreamSourceLab DSLogic](./img/DSLogic_PCB_front.jpg){ .infobox-image }

### DreamSourceLab DSLogic

| | |
|---|---|
| **Status** | supported |
| **Source code** | [dreamsourcelab-dslogic](https://github.com/OpenTraceLab/OpenTraceCapture/tree/main/src/hardware/dreamsourcelab-dslogic) |
| **Channels** | 1-16 |
| **Samplerate** | 400MHz(4ch), 200MHz(8ch), 100MHz(16ch) |
| **Samplerate (state)** | 50MHz |
| **Triggers** | high, low, rising, falling, edge, multi-stage triggers |
| **Min/max voltage** | -0.6V — 6V |
| **Threshold voltage** | configurable: 3.3V, 5V |
| **Memory** | 32MByte (2MByte/ch) |
| **Compression** | no |
| **Price range** | $60 - $70 |
| **Website** | [dreamsourcelab.com](http://www.dreamsourcelab.com/dslogic.html) |

</div>

The **DreamSourceLab DSLogic** is a 16-channel USB-based logic analyzer, with sampling rates up to 400MHz (when using only 4 channels).

See [DreamSourceLab DSLogic/Info](https://sigrok.org/wiki/DreamSourceLab_DSLogic/Info) for more details (such as **lsusb -v** output) about the device.

## Hardware
- [Xilinx XC6SLX9](http://www.xilinx.com/products/silicon-devices/fpga/spartan-6/) Spartan-6 FPGA (TQG144BIV13337)
- [Micron MT48LC16M16A2P-6A](http://www.micron.com/-/media/Documents/Products/Data%20Sheet/DRAM/256Mb_sdr.pdf) 32MB SDRAM (IC SDRAM 256MBIT 167MHZ TSOP)
- [Cypress CY7C68013A](http://www.cypress.com/?mpn=CY7C68013A-56PVXC) FX2 USB interface chip (IC MCU USB PERIPH HI SPD 56SSOP)
- [Serial EEPROM 16Kbit](http://www.atmel.com/Images/Atmel-8719-SEEPROM-AT24C16C-Datasheet.pdf) U4: ATMLH348 16CM Y 3X3098, I2C/2Wire Serial EEPROM 16Kbit (2048x8) ATMEL AT24C16C
- [ESD Protection](http://www.onsemi.com/pub_link/Collateral/CM1213A.PDF) U9,10,11,12,13,14 D234 ESD Protection CM1213A-04S7 TVS DIODE 3.3VWM 10VC SC746
- [1.2V 600mA LDO](http://www.ti.com/lit/ds/symlink/lm3671.pdf) U32 SBPB 1.2V 600mA 2MHz Step Down DC-DC Converter LM3671MF-1.2/NOPB
- [3.3V 600mA LDO](http://www.ti.com/lit/ds/symlink/lm3671.pdf) U31 SJEB 3.3V 600mA 2MHz Step Down DC-DC Converter LM3671MF-3.3/NOPB

## Photos

<div class="photo-grid" markdown>

[![Dslogic Pcb Front](./img/DSLogic_PCB_front.jpg)](./img/DSLogic_PCB_front.jpg "Dslogic Pcb Front"){ .glightbox data-gallery="dreamsourcelab-dslogic" }
<span class="caption">Dslogic Pcb Front</span>

[![Dslogic Connector](./img/DSLogic_connector.jpg)](./img/DSLogic_connector.jpg "Dslogic Connector"){ .glightbox data-gallery="dreamsourcelab-dslogic" }
<span class="caption">Dslogic Connector</span>

[![Dslogic Usb](./img/DSLogic_USB.jpg)](./img/DSLogic_USB.jpg "Dslogic Usb"){ .glightbox data-gallery="dreamsourcelab-dslogic" }
<span class="caption">Dslogic Usb</span>

[![Dslogic](./img/DSLogic.jpg)](./img/DSLogic.png "Dslogic"){ .glightbox data-gallery="dreamsourcelab-dslogic" }
<span class="caption">Dslogic</span>

[![Dslogic Pcb Back](./img/DSLogic_PCB_back.jpg)](./img/DSLogic_PCB_back.jpg "Dslogic Pcb Back"){ .glightbox data-gallery="dreamsourcelab-dslogic" }
<span class="caption">Dslogic Pcb Back</span>

</div>
## Firmware

In order to use this device with [libsigrok](https://sigrok.org/wiki/Libsigrok) the [vendor firmare and bitstream files](https://github.com/DreamSourceLab/DSView/raw/886b847c21c606df3138ce7ad8f8e8c363ee758b/DSView/res) (v0.97) are required.

### Installing firmware files via a bash script

The easiest method to install those is to use the [sigrok-fwextract-dreamsourcelab-dslogic](http://sigrok.org/gitweb/?p=sigrok-util.git;a=blob;f=firmware/dreamsourcelab-dslogic/sigrok-fwextract-dreamsourcelab-dslogic) script. It will download the correct files, rename them to the correct filenames as expected by libsigrok and install them.

**Example usage**:

```
$ **PREFIX=$HOME/sr ./sigrok-fwextract-dreamsourcelab-dslogic**

```

This will install the files into **$HOME/sr/share/sigrok-fimware**. Without **PREFIX**, the files will be installed into **/usr/local/share/sigrok-firmware** by default.

### Installing firmware files manually

If you want to avoid using the script, you can **manually download and rename** the files as follows:

| Downloaded file | Rename to | MD5 sum |
|---|---|---|
| DSLogic |
| [DSLogic50.bin](https://github.com/DreamSourceLab/DSView/raw/886b847c21c606df3138ce7ad8f8e8c363ee758b/DSView/res/DSLogic50.bin) | dreamsourcelab-dslogic-fpga-5v.fw | c3735b82e8b2b8310bec9c2c05ea8b47 |
| [DSLogic33.bin](https://github.com/DreamSourceLab/DSView/raw/886b847c21c606df3138ce7ad8f8e8c363ee758b/DSView/res/DSLogic33.bin) | dreamsourcelab-dslogic-fpga-3v3.fw | 1599ee538d3ff99ddc014b0243cbf60d |
| [DSLogic.fw](https://github.com/DreamSourceLab/DSView/raw/886b847c21c606df3138ce7ad8f8e8c363ee758b/DSView/res/DSLogic.fw) | dreamsourcelab-dslogic-fx2.fw | 80db51aabc377cb215df2f213621355f |
| DScope |
| [DSCope.bin](https://github.com/DreamSourceLab/DSView/raw/886b847c21c606df3138ce7ad8f8e8c363ee758b/DSView/res/DSCope.bin) | dreamsourcelab-dscope-fpga.fw | 80a64ccd9ce8ee71a7165a27dbb30ede |
| [DSCope.fw](https://github.com/DreamSourceLab/DSView/raw/886b847c21c606df3138ce7ad8f8e8c363ee758b/DSView/res/DSCope.fw) | dreamsourcelab-dscope-fx2.fw | 4a2ab71e1ef726e2e65019f9d42a6e50 |
| DSLogic Pro |
| [DSLogicPro.bin](https://github.com/DreamSourceLab/DSView/raw/886b847c21c606df3138ce7ad8f8e8c363ee758b/DSView/res/DSLogicPro.bin) | dreamsourcelab-dslogic-pro-fpga.fw | 1adf30ff49522cf6944e67b19a8736ed |
| [DSLogicPro.fw](https://github.com/DreamSourceLab/DSView/raw/886b847c21c606df3138ce7ad8f8e8c363ee758b/DSView/res/DSLogicPro.fw) | dreamsourcelab-dslogic-pro-fx2.fw | 0555bf649719d11e714f159f2fdc5a57 |
| DSLogic Plus |
| [DSLogicPlus.bin](https://github.com/DreamSourceLab/DSView/raw/886b847c21c606df3138ce7ad8f8e8c363ee758b/DSView/res/DSLogicPlus.bin) | dreamsourcelab-dslogic-plus-fpga.fw | 0ebc84bf40cf1f9c60998794bc3dba1f |
| [DSLogicPlus.fw](https://github.com/DreamSourceLab/DSView/raw/886b847c21c606df3138ce7ad8f8e8c363ee758b/DSView/res/DSLogicPlus.fw) | dreamsourcelab-dslogic-plus-fx2.fw | 6f1805fcb5040498ae1b522a7defae5d |
| DSLogic Basic |
| [DSLogicBasic.bin](https://github.com/DreamSourceLab/DSView/raw/886b847c21c606df3138ce7ad8f8e8c363ee758b/DSView/res/DSLogicBasic.bin) | dreamsourcelab-dslogic-basic-fpga.fw | 3d19924ab211967c2496681fce9e17ed |
| [DSLogicBasic.fw](https://github.com/DreamSourceLab/DSView/raw/886b847c21c606df3138ce7ad8f8e8c363ee758b/DSView/res/DSLogicBasic.fw) | dreamsourcelab-dslogic-basic-fx2.fw | ab6f5788ce7228ab26933a3cda7abc7b |

You have to place the files into the **sigrok-firmware** sub-directory of where-ever you installed [sigrok-cli](https://sigrok.org/wiki/Sigrok-cli) or [PulseView](https://sigrok.org/wiki/PulseView).

### Example run

After firmware is correctly installed, you can see if it's worked like this:

```
sigrok-cli --driver=dreamsourcelab-dslogic -l 5 --scan

```

You should see the driver detected and uploading the firmware

```
sr: [00:00.014417] resource: Opened '/usr/local/share/sigrok-firmware/dreamsourcelab-dslogic-basic-fx2.fw'.
sr: [00:00.014454] ezusb: Uploading firmware 'dreamsourcelab-dslogic-basic-fx2.fw'.
sr: [00:00.014972] ezusb: Uploaded 4096 bytes.
sr: [00:00.015481] ezusb: Uploaded 4024 bytes.
sr: [00:00.015492] ezusb: Firmware upload done.
sr: [00:00.015497] ezusb: setting CPU reset mode off...
sr: [00:00.015606] hwdriver: Scan found 1 devices (dreamsourcelab-dslogic).
The following devices were found:
dreamsourcelab-dslogic - DreamSourceLab DSLogic Basic with 16 channels: 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
sr: [00:00.015691] hwdriver: Cleaning up all drivers.

```
## Capabilities

Use --show to fetch the current available options

```
sigrok-cli --driver=dreamsourcelab-dslogic --show

```

This example shows how to use sigrok-cli to capture 1k samples at 500khz on channels 0 and 1, with voltage threshold of 2.5v

```
sigrok-cli -C 0,1 --driver=dreamsourcelab-dslogic  -c "samplerate=500k:voltage_threshold=2.5-2.5" --samples 1k

```

This example shows continuous capture (requires the device config to include 'continuous=on')

```
sigrok-cli -c "samplerate=10k:voltage_threshold=2.5-2.5:continuous=on" --driver=dreamsourcelab-dslogic --continuous

```
## Resources
- [Vendor website](http://www.dreamsourcelab.com)
- [Kickstarter page](https://www.kickstarter.com/projects/dreamsourcelab/dslogic-multifunction-instruments-for-everyone)

