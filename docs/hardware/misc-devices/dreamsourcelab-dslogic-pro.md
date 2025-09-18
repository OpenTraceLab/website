# Dreamsourcelab Dslogic Pro

| | | |:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------:| | [![\1](../../assets/hardware/general/\2)](./File:DSLogic.png.html) | | | Status | supported | | Source code | [dreamsourcelab-dslogic](http://github.com/OpenTraceLab/?p=OpenTraceCapture.git;a=tree;f=src/hardware/dreamsourcelab-dslogic) | | Channels | 1-16 | | Samplerate | 400MHz(4ch), 200MHz(8ch), 100MHz(16ch) | | Samplerate (state) | 30MHz (?) or 50MHz (?) | | Triggers | high, low, rising, falling, edge, multi-stage triggers | | Min/max voltage | -0.6V — 6V | | Threshold voltage | configurable: 0-5V (0.1V increments) | | Memory | 32MByte (2MByte/ch) | | Compression | yes | | Website | [dreamsourcelab.com](http://www.dreamsourcelab.com/dslogic.html) | **DreamSourceLab DSLogic Pro** The **DreamSourceLab DSLogic Pro** is a 16-channel USB-based logic analyzer, with sampling rates up to 400MHz (when using only 4 channels). This differs slightly from the original DSLogic product in its configurable threshold voltage and different PCB layout. DreamSourceLab doesn't make the distinction between these two products very clear on their website. See [DreamSourceLab DSLogic Pro/Info](DreamSourceLab_DSLogic_Pro/Info.html "DreamSourceLab DSLogic Pro/Info") for more details (such as **lsusb -v** output) about the device. 
## Contents 
\- [1 Hardware](DreamSourceLab_DSLogic_Pro.html#Hardware) \- [2 Photos](DreamSourceLab_DSLogic_Pro.html#Photos) \- [3 Firmware](DreamSourceLab_DSLogic_Pro.html#Firmware) \- [4 Resources](DreamSourceLab_DSLogic_Pro.html#Resources) 
## Hardware \- [Xilinx XC6SLX9](http://www.xilinx.com/products/silicon-devices/fpga/spartan-6/) U2: Spartan-6 FPGA (TQG144BIV13337) \- [Micron MT48LC16M16A2P-6A](http://www.micron.com/-/media/Documents/Products/Data%20Sheet/DRAM/256Mb_sdr.pdf) U29: 32MB SDRAM (IC SDRAM 256MBIT 167MHZ TSOP) \- [Cypress CY7C68013A](http://www.cypress.com/?mpn=CY7C68013A-56PVXC) U33: FX2 USB interface chip (IC MCU USB PERIPH HI SPD 56SSOP) \- [Serial EEPROM 16Kbit](http://www.atmel.com/Images/Atmel-8719-SEEPROM-AT24C16C-Datasheet.pdf) U4: ATMLH348 16CM Y 3X3098, I2C/2Wire Serial EEPROM 16Kbit (2048x8) ATMEL AT24C16C \- [ESD Protection](http://www.onsemi.com/pub_link/Collateral/CM1213A.PDF) U9,10,11,12,13,14: D234 ESD Protection CM1213A-04S7 TVS DIODE 3.3VWM 10VC SC746 \- [Adjustable 500mA LDO](http://www.micrel.com/products/power-management-ics/ldos/single-ldos/article/80-mic5209.html) U3: Adjustable (configured for 3.3V) 600mA 2MHz Step Down DC-DC Converter MIC5209YM \- [1.2V 600mA LDO](http://www.ti.com/lit/ds/symlink/lm3671.pdf) U31: SBPB 1.2V 600mA 2MHz Step Down DC-DC Converter LM3671MF-1.2/NOPB ## Photos \- 
[![\1](../../assets/hardware/general/\2)](./File:DSLogic.png.html)
Device, top
\- 
[![\1](../../assets/hardware/general/\2)](./File:DSLogic_connector.jpg.html)
Probe connector
\- 
[![\1](../../assets/hardware/general/\2)](./File:DSLogic_USB.jpg.html)
USB connector
\- 
[![\1](../../assets/hardware/general/\2)](./File:DSLogic_Pro_PCB_front.jpg.html)
PCB, top
\- 
[![\1](../../assets/hardware/general/\2)](./File:DSLogic_Pro_PCB_back.jpg.html)
PCB, bottom
## Firmware See [DreamSourceLab DSLogic#Firmware](DreamSourceLab_DSLogic.html#Firmware "DreamSourceLab DSLogic"). ## Resources \- [Vendor website](http://www.dreamsourcelab.com) \- [Vendor wiki](http://www.dreamsourcelab.com/wiki/index.php) \- [Vendor forum](http://www.dreamsourcelab.com/forum/index.php) \- [Device specs](http://www.dreamsourcelab.com/techspec.html) \- [Kickstarter page](https://www.kickstarter.com/projects/dreamsourcelab/dslogic-multifunction-instruments-for-everyone)
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=DreamSourceLab_DSLogic_Pro&oldid=13114](https://OpenTraceLab.org/w/index.php?title=DreamSourceLab_DSLogic_Pro&oldid=13114)" 
[Categories](specialcategories-specialcategories.md): \- [Device](./Category:Device.html "Category:Device") \- [Logic analyzer](./Category:Logic_analyzer.html "Category:Logic analyzer") \- [Supported](./Category:Supported.html "Category:Supported")

## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
