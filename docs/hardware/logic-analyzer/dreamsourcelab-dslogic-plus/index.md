---
title: DreamSourceLab DSLogic Plus
---

# DreamSourceLab DSLogic Plus

<div class="infobox" markdown>

![DreamSourceLab DSLogic Plus](./img/Dslogic_plus_V421_pcb_front.jpg){ .infobox-image }

### DreamSourceLab DSLogic Plus

| | |
|---|---|
| **Status** | supported |
| **Source code** | [dreamsourcelab-dslogic](https://github.com/OpenTraceLab/OpenTraceCapture/tree/main/src/hardware/dreamsourcelab-dslogic) |
| **Channels** | 1-16 |
| **Samplerate** | 400MHz(4ch), 200MHz(8ch), 100MHz(16ch) |
| **Samplerate (state)** | 30MHz (?) or 50MHz (?) |
| **Triggers** | high, low, rising, falling, edge, multi-stage triggers |
| **Min/max voltage** | -0.6V — 6V, +-30V with provided probe-wires |
| **Threshold voltage** | configurable: 0-5V (0.1V increments) |
| **Memory** | 256MBit |
| **Compression** | yes |
| **Website** | [dreamsourcelab.com](http://www.dreamsourcelab.com/dslogic.html) |

</div>

The **DreamSourceLab DSLogic Plus** is a 16-channel USB-based logic analyzer, with sampling rates up to 400MHz (when using only 4 channels). This differs slightly from the original DSLogic product in its configurable threshold voltage and different PCB layout. DreamSourceLab doesn't make the distinction between these two products very clear on their website.

See [DreamSourceLab DSLogic Plus/Info](https://sigrok.org/wiki/DreamSourceLab_DSLogic_Plus/Info) for more details (such as **lsusb -v** output) about the device.

## Hardware
- [Xilinx XC6SLX9](http://www.xilinx.com/products/silicon-devices/fpga/spartan-6/) U3: Spartan-6 FPGA (TQG144BIV13337)
- Sample memory:
Original version: [Alliance AS4C16M16SA-7TCN](https://www.alliancememory.com/wp-content/uploads/pdf/dram/256Mb-AS4C16M16SA-C&I_V3.0_March%202015.pdf) U1: 256Mbit SDRAM
- V211: [Micron MT48LC16M16A2 256Mbit SDRAM](https://www.micron.com/~/media/Documents/Products/Data%20Sheet/DRAM/256Mb_sdr.pdf)
- [Cypress CY7C68013A](http://www.cypress.com/?mpn=CY7C68013A-56PVXC) U2: FX2LP USB interface chip
- [128Kbit I²C EEPROM](http://www.st.com/content/ccc/resource/technical/document/datasheet/59/05/c9/5b/7b/41/48/b6/CD00259167.pdf/files/CD00259167.pdf/jcr:content/translations/en.CD00259167.pdf) U4: ST M24128-BR
- [TI TPS62400](http://www.ti.com/product/TPS62400) U10: Dual, Adjustable, 400mA and 600mA, 2.25MHz Step-Down Converter (3.3V and 1.2V output)
- [24.0Mhz Crystal](http://file1.jzsc8.com/mallpropdf/16/04/28/151237988.pdf) Y1: [YSX321SL series](http://www.yxc.hk/u_file/product/17_08_22/YSX321SL.pdf) 20ppm (markings: YXC 24.0SBJI)
## Hardware (V421/Pango Variant)

New hardware variant received early 2023, enumerates as 2a0e:0030, and uses a different vendor's FPGA. Currently incompatible with sigrok.

- [PangoMicro Logos PGL12G](https://www-pangomicro-com.translate.goog/procenter/detail4.html?_x_tr_sl=auto&_x_tr_tl=en&_x_tr_hl=en&_x_tr_pto=wapp) U13: PGL12G, 12k LUT, LPG144 package
- [Winbond W9825G6KH-6](https://www.winbond.com/resource-files/w9825g6kh_a04.pdf) U6: 256Mbit SDRAM
- [Cypress CY7C68013A](http://www.cypress.com/?mpn=CY7C68013A-56PVXC) U2: FX2LP USB interface chip
- [128Kbit I²C EEPROM](http://www.st.com/content/ccc/resource/technical/document/datasheet/59/05/c9/5b/7b/41/48/b6/CD00259167.pdf/files/CD00259167.pdf/jcr:content/translations/en.CD00259167.pdf) U4: ST M24128-BR
- Unmarked 3.3V and 1.2V regulators
- [24.0Mhz Crystal](http://file1.jzsc8.com/mallpropdf/16/04/28/151237988.pdf) Y1: [YSX321SL series](http://www.yxc.hk/u_file/product/17_08_22/YSX321SL.pdf) 20ppm (markings: YXC 24.0SBJI)

## Photos

<div class="photo-grid" markdown>

[![Dslogic Plus V421 Pcb Front](./img/Dslogic_plus_V421_pcb_front.jpg)](./img/Dslogic_plus_V421_pcb_front.jpg "Dslogic Plus V421 Pcb Front"){ .glightbox data-gallery="dreamsourcelab-dslogic-plus" }
<span class="caption">Dslogic Plus V421 Pcb Front</span>

[![Dslogic Plus V421 Pcb Rear](./img/Dslogic_plus_V421_pcb_rear.jpg)](./img/Dslogic_plus_V421_pcb_rear.jpg "Dslogic Plus V421 Pcb Rear"){ .glightbox data-gallery="dreamsourcelab-dslogic-plus" }
<span class="caption">Dslogic Plus V421 Pcb Rear</span>

[![Dreamsourcelab Dslogic Plus Cable B Xray 1](./img/Dreamsourcelab_dslogic_plus_cable_B_xray_1.jpg)](./img/Dreamsourcelab_dslogic_plus_cable_B_xray_1.jpg "Dreamsourcelab Dslogic Plus Cable B Xray 1"){ .glightbox data-gallery="dreamsourcelab-dslogic-plus" }
<span class="caption">Dreamsourcelab Dslogic Plus Cable B Xray 1</span>

[![Dreamsourcelab Dslogic Plus Cable B Xray 2](./img/Dreamsourcelab_dslogic_plus_cable_B_xray_2.jpg)](./img/Dreamsourcelab_dslogic_plus_cable_B_xray_2.jpg "Dreamsourcelab Dslogic Plus Cable B Xray 2"){ .glightbox data-gallery="dreamsourcelab-dslogic-plus" }
<span class="caption">Dreamsourcelab Dslogic Plus Cable B Xray 2</span>

[![Dslogic Plus Pcb Back](./img/Dslogic_plus_pcb_back.jpg)](./img/Dslogic_plus_pcb_back.jpg "Dslogic Plus Pcb Back"){ .glightbox data-gallery="dreamsourcelab-dslogic-plus" }
<span class="caption">Dslogic Plus Pcb Back</span>

[![Dslogic](./img/DSLogic.jpg)](./img/DSLogic.png "Dslogic"){ .glightbox data-gallery="dreamsourcelab-dslogic-plus" }
<span class="caption">Dslogic</span>

[![Dslogic Plus Pcb Front](./img/Dslogic_plus_pcb_front.jpg)](./img/Dslogic_plus_pcb_front.jpg "Dslogic Plus Pcb Front"){ .glightbox data-gallery="dreamsourcelab-dslogic-plus" }
<span class="caption">Dslogic Plus Pcb Front</span>

[![Dreamsourcelab Dslogic Plus Cable 5](./img/Dreamsourcelab_dslogic_plus_cable_5.jpg)](./img/Dreamsourcelab_dslogic_plus_cable_5.jpg "Dreamsourcelab Dslogic Plus Cable 5"){ .glightbox data-gallery="dreamsourcelab-dslogic-plus" }
<span class="caption">Dreamsourcelab Dslogic Plus Cable 5</span>

[![Dreamsourcelab Dslogic Plus Cable 4](./img/Dreamsourcelab_dslogic_plus_cable_4.jpg)](./img/Dreamsourcelab_dslogic_plus_cable_4.jpg "Dreamsourcelab Dslogic Plus Cable 4"){ .glightbox data-gallery="dreamsourcelab-dslogic-plus" }
<span class="caption">Dreamsourcelab Dslogic Plus Cable 4</span>

[![Dreamsourcelab Dslogic Plus Cable 1](./img/Dreamsourcelab_dslogic_plus_cable_1.jpg)](./img/Dreamsourcelab_dslogic_plus_cable_1.jpg "Dreamsourcelab Dslogic Plus Cable 1"){ .glightbox data-gallery="dreamsourcelab-dslogic-plus" }
<span class="caption">Dreamsourcelab Dslogic Plus Cable 1</span>

[![Dreamsourcelab Dslogic Plus Probe Circuit](./img/Dreamsourcelab_dslogic_plus_probe_circuit.png)](./img/Dreamsourcelab_dslogic_plus_probe_circuit.png "Dreamsourcelab Dslogic Plus Probe Circuit"){ .glightbox data-gallery="dreamsourcelab-dslogic-plus" }
<span class="caption">Dreamsourcelab Dslogic Plus Probe Circuit</span>

[![Dreamsourcelab Dslogic Plus Cable 3](./img/Dreamsourcelab_dslogic_plus_cable_3.jpg)](./img/Dreamsourcelab_dslogic_plus_cable_3.jpg "Dreamsourcelab Dslogic Plus Cable 3"){ .glightbox data-gallery="dreamsourcelab-dslogic-plus" }
<span class="caption">Dreamsourcelab Dslogic Plus Cable 3</span>

[![Dreamsourcelab Dslogic Plus Cable 2](./img/Dreamsourcelab_dslogic_plus_cable_2.jpg)](./img/Dreamsourcelab_dslogic_plus_cable_2.jpg "Dreamsourcelab Dslogic Plus Cable 2"){ .glightbox data-gallery="dreamsourcelab-dslogic-plus" }
<span class="caption">Dreamsourcelab Dslogic Plus Cable 2</span>

</div>
## Firmware

See [DreamSourceLab DSLogic#Firmware](https://sigrok.org/wiki/DreamSourceLab_DSLogic#Firmware).

## Resources
- [Vendor website](http://www.dreamsourcelab.com)
- [Vendor datasheet](https://www.dreamsourcelab.com/doc/DSLogic_Plus_Datasheet.pdf)
- [Kickstarter page](https://www.kickstarter.com/projects/dreamsourcelab/dslogic-multifunction-instruments-for-everyone)

