---
title: DreamSourceLab DSLogic Pro
---

# DreamSourceLab DSLogic Pro

<div class="infobox" markdown>

![DreamSourceLab DSLogic Pro](./img/DSLogic_connector.jpg){ .infobox-image }

### DreamSourceLab DSLogic Pro

| | |
|---|---|
| **Status** | supported |
| **Source code** | [dreamsourcelab-dslogic](https://github.com/OpenTraceLab/OpenTraceCapture/tree/main/src/hardware/dreamsourcelab-dslogic) |
| **Channels** | 1-16 |
| **Samplerate** | 400MHz(4ch), 200MHz(8ch), 100MHz(16ch) |
| **Samplerate (state)** | 30MHz (?) or 50MHz (?) |
| **Triggers** | high, low, rising, falling, edge, multi-stage triggers |
| **Min/max voltage** | -0.6V — 6V |
| **Threshold voltage** | configurable: 0-5V (0.1V increments) |
| **Memory** | 32MByte (2MByte/ch) |
| **Compression** | yes |
| **Website** | [dreamsourcelab.com](http://www.dreamsourcelab.com/dslogic.html) |

</div>

The **DreamSourceLab DSLogic Pro** is a 16-channel USB-based logic analyzer, with sampling rates up to 400MHz (when using only 4 channels). This differs slightly from the original DSLogic product in its configurable threshold voltage and different PCB layout. DreamSourceLab doesn't make the distinction between these two products very clear on their website.

See [DreamSourceLab DSLogic Pro/Info](https://sigrok.org/wiki/DreamSourceLab_DSLogic_Pro/Info) for more details (such as **lsusb -v** output) about the device.

## Hardware
- [Xilinx XC6SLX9](http://www.xilinx.com/products/silicon-devices/fpga/spartan-6/) U2: Spartan-6 FPGA (TQG144BIV13337)
- [Micron MT48LC16M16A2P-6A](http://www.micron.com/-/media/Documents/Products/Data%20Sheet/DRAM/256Mb_sdr.pdf) U29: 32MB SDRAM (IC SDRAM 256MBIT 167MHZ TSOP)
- [Cypress CY7C68013A](http://www.cypress.com/?mpn=CY7C68013A-56PVXC) U33: FX2 USB interface chip (IC MCU USB PERIPH HI SPD 56SSOP)
- [Serial EEPROM 16Kbit](http://www.atmel.com/Images/Atmel-8719-SEEPROM-AT24C16C-Datasheet.pdf) U4: ATMLH348 16CM Y 3X3098, I2C/2Wire Serial EEPROM 16Kbit (2048x8) ATMEL AT24C16C
- [ESD Protection](http://www.onsemi.com/pub_link/Collateral/CM1213A.PDF) U9,10,11,12,13,14: D234 ESD Protection CM1213A-04S7 TVS DIODE 3.3VWM 10VC SC746
- [Adjustable 500mA LDO](http://www.micrel.com/products/power-management-ics/ldos/single-ldos/article/80-mic5209.html) U3: Adjustable (configured for 3.3V) 600mA 2MHz Step Down DC-DC Converter MIC5209YM
- [1.2V 600mA LDO](http://www.ti.com/lit/ds/symlink/lm3671.pdf) U31: SBPB 1.2V 600mA 2MHz Step Down DC-DC Converter LM3671MF-1.2/NOPB

## Photos

<div class="photo-grid" markdown>

[![Dslogic Connector](./img/DSLogic_connector.jpg)](./img/DSLogic_connector.jpg "Dslogic Connector"){ .glightbox data-gallery="dreamsourcelab-dslogic-pro" }
<span class="caption">Dslogic Connector</span>

[![Dslogic Usb](./img/DSLogic_USB.jpg)](./img/DSLogic_USB.jpg "Dslogic Usb"){ .glightbox data-gallery="dreamsourcelab-dslogic-pro" }
<span class="caption">Dslogic Usb</span>

[![Dslogic](./img/DSLogic.png)](./img/DSLogic.png "Dslogic"){ .glightbox data-gallery="dreamsourcelab-dslogic-pro" }
<span class="caption">Dslogic</span>

[![Dslogic Pro Pcb Front](./img/DSLogic_Pro_PCB_front.jpg)](./img/DSLogic_Pro_PCB_front.jpg "Dslogic Pro Pcb Front"){ .glightbox data-gallery="dreamsourcelab-dslogic-pro" }
<span class="caption">Dslogic Pro Pcb Front</span>

[![Dslogic Pro Pcb Back](./img/DSLogic_Pro_PCB_back.jpg)](./img/DSLogic_Pro_PCB_back.jpg "Dslogic Pro Pcb Back"){ .glightbox data-gallery="dreamsourcelab-dslogic-pro" }
<span class="caption">Dslogic Pro Pcb Back</span>

</div>
## Firmware

See [DreamSourceLab DSLogic#Firmware](https://sigrok.org/wiki/DreamSourceLab_DSLogic#Firmware).

## Resources
- [Vendor website](http://www.dreamsourcelab.com)
- [Vendor wiki](http://www.dreamsourcelab.com/wiki/index.php)
- [Vendor forum](http://www.dreamsourcelab.com/forum/index.php)
- [Device specs](http://www.dreamsourcelab.com/techspec.html)
- [Kickstarter page](https://www.kickstarter.com/projects/dreamsourcelab/dslogic-multifunction-instruments-for-everyone)

