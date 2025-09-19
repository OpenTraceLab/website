# Dreamsourcelab Dslogic Plus
| | | |:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------:| | [*Image: \1* | | | Status | supported | | Source code | [dreamsourcelab-dslogic](http://github.com/OpenTraceLab/?p=OpenTraceCapture.git;a=tree;f=src/hardware/dreamsourcelab-dslogic) | | Channels | 1-16 | | Samplerate | 400MHz(4ch), 200MHz(8ch), 100MHz(16ch) | | Samplerate (state) | 30MHz (?) or 50MHz (?) | | Triggers | high, low, rising, falling, edge, multi-stage triggers | | Min/max voltage | -0.6V — 6V, +-30V with provided probe-wires | | Threshold voltage | configurable: 0-5V (0.1V increments) | | Memory | 256MBit | | Compression | yes | | Website | *dreamsourcelab.com* | **DreamSourceLab DSLogic Plus** The **DreamSourceLab DSLogic Plus** is a 16-channel USB-based logic analyzer, with sampling rates up to 400MHz (when using only 4 channels). This differs slightly from the original DSLogic product in its configurable threshold voltage and different PCB layout. DreamSourceLab doesn't make the distinction between these two products very clear on their website. See *DreamSourceLab DSLogic Plus/Info* for more details (such as **lsusb -v** output) about the device.
## Contents
\- *1 Hardware* \- *2 Hardware (V421/Pango Variant)*) \- *3 Photos* \- *4 Firmware* \- *5 Resources*
## Hardware \- [Xilinx XC6SLX9](http://www.xilinx.com/products/silicon-devices/fpga/spartan-6/) U3: Spartan-6 FPGA (TQG144BIV13337) \- Sample memory: \- Original version: [Alliance AS4C16M16SA-7TCN](https://www.alliancememory.com/wp-content/uploads/pdf/dram/256Mb-AS4C16M16SA-C&I_V3.0_March%202015.pdf) U1: 256Mbit SDRAM \- V211: [Micron MT48LC16M16A2 256Mbit SDRAM](https://www.micron.com/~/media/Documents/Products/Data%20Sheet/DRAM/256Mb_sdr.pdf) \- [Cypress CY7C68013A](http://www.cypress.com/?mpn=CY7C68013A-56PVXC) U2: FX2LP USB interface chip \- [128Kbit I²C EEPROM](http://www.st.com/content/ccc/resource/technical/document/datasheet/59/05/c9/5b/7b/41/48/b6/CD00259167.pdf/files/CD00259167.pdf/jcr:content/translations/en.CD00259167.pdf) U4: ST M24128-BR \- [TI TPS62400](http://www.ti.com/product/TPS62400) U10: Dual, Adjustable, 400mA and 600mA, 2.25MHz Step-Down Converter (3.3V and 1.2V output) \- [24.0Mhz Crystal](http://file1.jzsc8.com/mallpropdf/16/04/28/151237988.pdf) Y1: [YSX321SL series](http://www.yxc.hk/u_file/product/17_08_22/YSX321SL.pdf) 20ppm (markings: YXC 24.0SBJI) ## Hardware (V421/Pango Variant) New hardware variant received early 2023, enumerates as 2a0e:0030, and uses a different vendor's FPGA. Currently incompatible with OpenTraceLab. \- *PangoMicro Logos PGL12G* U13: PGL12G, 12k LUT, LPG144 package \- [Winbond W9825G6KH-6](https://www.winbond.com/resource-files/w9825g6kh_a04.pdf) U6: 256Mbit SDRAM \- [Cypress CY7C68013A](http://www.cypress.com/?mpn=CY7C68013A-56PVXC) U2: FX2LP USB interface chip \- [128Kbit I²C EEPROM](http://www.st.com/content/ccc/resource/technical/document/datasheet/59/05/c9/5b/7b/41/48/b6/CD00259167.pdf/files/CD00259167.pdf/jcr:content/translations/en.CD00259167.pdf) U4: ST M24128-BR \- Unmarked 3.3V and 1.2V regulators \- [24.0Mhz Crystal](http://file1.jzsc8.com/mallpropdf/16/04/28/151237988.pdf) Y1: [YSX321SL series](http://www.yxc.hk/u_file/product/17_08_22/YSX321SL.pdf) 20ppm (markings: YXC 24.0SBJI) ## Photos **Device**: \-
[*Image: \1*
PCB, front
\-
[*Image: \1*
PCB, back (mirrored)
\-
[*Image: \1*
PCB V211, front
\-
[*Image: \1*
PCB V211, back
\-
[*Image: \1*
PCB V421, front
\-
[*Image: \1*
PCB V421, back
**Cables**: \-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
Probe cable circuit
\-
[*Image: \1*
Revised Probe cable
\-
[*Image: \1*
Revised Probe cable
## Firmware See *DreamSourceLab DSLogic#Firmware*. ## Resources \- [Vendor website](http://www.dreamsourcelab.com) \- [Vendor datasheet](https://www.dreamsourcelab.com/doc/DSLogic_Plus_Datasheet.pdf) \- [Kickstarter page](https://www.kickstarter.com/projects/dreamsourcelab/dslogic-multifunction-instruments-for-everyone)
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=DreamSourceLab_DSLogic_Plus&oldid=16468](https://OpenTraceLab.org/w/index.php?title=DreamSourceLab_DSLogic_Plus&oldid=16468)"
: \- *Device* \- *Logic analyzer* \- *Supported*
## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
