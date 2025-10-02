---
title: Noname LHT00SU1
---

# Noname LHT00SU1

<div class="infobox" markdown>

![Noname LHT00SU1](./img/Noname_lht00su1_cypress_fx2.jpg){ .infobox-image }

### Noname LHT00SU1

| | |
|---|---|
| **Status** | supported |
| **Source code** | [fx2lafw](https://github.com/OpenTraceLab/OpenTraceCapture/tree/main/src/hardware/fx2lafw) |
| **Channels** | 8 + 1 |
| **Samplerate** | 8ch @ 24MHz, 8+1ch @ 12MHz |
| **Samplerate (state)** | — |
| **Triggers** | none (SW-only) |
| **Min/max voltage** | Digital: 0V — +5.3VAnalog: ±10V |
| **Threshold voltage** | Fixed: VIH=1.4V, VIL=0.8V |
| **Memory** | none |
| **Compression** | none |
| **Price range** | $20 - $25 |
| **Website** | [aliexpress.com](https://www.aliexpress.com/wholesale?catId=0&amp;initiative_id=SB_20170810062635&amp;SearchText=lht00su1) |

</div>

The **Noname LHT00SU1** is a USB-based, 8-channel logic analyzer with up to 24MHz sampling rate, with 1 additional analog channel (theoretically 2, but only one of them can be used at a time; 3MHz analog bandwidth).

It is a clone of the [CWAV USBee AX-Pro](/w/index.php?title=CWAV_USBee_AX-Pro&action=edit&redlink=1).

In sigrok, we use the open-source [fx2lafw](https://sigrok.org/wiki/Fx2lafw) firmware for this logic analyzer.

**Note**: [fx2lafw](https://sigrok.org/wiki/Fx2lafw) currently doesn't support switching between the two possible analog channels, 1ACH will be used unconditionally.

See [Noname LHT00SU1/Info](https://sigrok.org/wiki/Noname_LHT00SU1/Info) for some more details (such as **lsusb -v** output) on the device.

## Hardware

There's a jumper on the PCB which write-protects the I²C EEPROM when set (it ships in that state) by keeping the WP pin at 3.3V.

## Photos

<div class="photo-grid" markdown>

[![Noname Lht00su1 Cypress Fx2](./img/Noname_lht00su1_cypress_fx2.jpg)](./img/Noname_lht00su1_cypress_fx2.jpg "Noname Lht00su1 Cypress Fx2"){ .glightbox data-gallery="noname-lht00su1" }
<span class="caption">Noname Lht00su1 Cypress Fx2</span>

[![Noname Lht00su1 Device Top](./img/Noname_lht00su1_device_top.jpg)](./img/Noname_lht00su1_device_top.jpg "Noname Lht00su1 Device Top"){ .glightbox data-gallery="noname-lht00su1" }
<span class="caption">Noname Lht00su1 Device Top</span>

[![Linsou21 V1 3 Pcb Bottom](./img/LINSOU21-V1_3-PCB-Bottom.jpg)](./img/LINSOU21-V1_3-PCB-Bottom.jpg "Linsou21 V1 3 Pcb Bottom"){ .glightbox data-gallery="noname-lht00su1" }
<span class="caption">Linsou21 V1 3 Pcb Bottom</span>

[![Noname Lht00su1 Device Bottom](./img/Noname_lht00su1_device_bottom.jpg)](./img/Noname_lht00su1_device_bottom.jpg "Noname Lht00su1 Device Bottom"){ .glightbox data-gallery="noname-lht00su1" }
<span class="caption">Noname Lht00su1 Device Bottom</span>

[![Noname Lht00su1 Package Contents](./img/Noname_lht00su1_package_contents.jpg)](./img/Noname_lht00su1_package_contents.jpg "Noname Lht00su1 Package Contents"){ .glightbox data-gallery="noname-lht00su1" }
<span class="caption">Noname Lht00su1 Package Contents</span>

[![Noname Lht00su1 So8](./img/Noname_lht00su1_so8.jpg)](./img/Noname_lht00su1_so8.jpg "Noname Lht00su1 So8"){ .glightbox data-gallery="noname-lht00su1" }
<span class="caption">Noname Lht00su1 So8</span>

[![Linsou21 V1 3 Pcb Top](./img/LINSOU21-V1_3-PCB-Top.jpg)](./img/LINSOU21-V1_3-PCB-Top.jpg "Linsou21 V1 3 Pcb Top"){ .glightbox data-gallery="noname-lht00su1" }
<span class="caption">Linsou21 V1 3 Pcb Top</span>

[![Noname Lht00su1 Mugshot](./img/Noname_lht00su1_mugshot.jpg)](./img/Noname_lht00su1_mugshot.png "Noname Lht00su1 Mugshot"){ .glightbox data-gallery="noname-lht00su1" }
<span class="caption">Noname Lht00su1 Mugshot</span>

[![Noname Lht00su1 Lm358](./img/Noname_lht00su1_lm358.jpg)](./img/Noname_lht00su1_lm358.jpg "Noname Lht00su1 Lm358"){ .glightbox data-gallery="noname-lht00su1" }
<span class="caption">Noname Lht00su1 Lm358</span>

[![Noname Lht00su1 Pcb Bottom](./img/Noname_lht00su1_pcb_bottom.jpg)](./img/Noname_lht00su1_pcb_bottom.jpg "Noname Lht00su1 Pcb Bottom"){ .glightbox data-gallery="noname-lht00su1" }
<span class="caption">Noname Lht00su1 Pcb Bottom</span>

[![Noname Lht00su1 Hef4051bt](./img/Noname_lht00su1_hef4051bt.jpg)](./img/Noname_lht00su1_hef4051bt.jpg "Noname Lht00su1 Hef4051bt"){ .glightbox data-gallery="noname-lht00su1" }
<span class="caption">Noname Lht00su1 Hef4051bt</span>

[![Noname Lht00su1 Ams1117](./img/Noname_lht00su1_ams1117.jpg)](./img/Noname_lht00su1_ams1117.jpg "Noname Lht00su1 Ams1117"){ .glightbox data-gallery="noname-lht00su1" }
<span class="caption">Noname Lht00su1 Ams1117</span>

[![Noname Lht00su1 Tlc5510i](./img/Noname_lht00su1_tlc5510i.jpg)](./img/Noname_lht00su1_tlc5510i.jpg "Noname Lht00su1 Tlc5510i"){ .glightbox data-gallery="noname-lht00su1" }
<span class="caption">Noname Lht00su1 Tlc5510i</span>

[![Noname Lht00su1 Pcb Top](./img/Noname_lht00su1_pcb_top.jpg)](./img/Noname_lht00su1_pcb_top.jpg "Noname Lht00su1 Pcb Top"){ .glightbox data-gallery="noname-lht00su1" }
<span class="caption">Noname Lht00su1 Pcb Top</span>

[![Noname Lht00su1 Bochen 3296](./img/Noname_lht00su1_bochen_3296.jpg)](./img/Noname_lht00su1_bochen_3296.jpg "Noname Lht00su1 Bochen 3296"){ .glightbox data-gallery="noname-lht00su1" }
<span class="caption">Noname Lht00su1 Bochen 3296</span>

[![Noname Lht00su1 24c02n](./img/Noname_lht00su1_24c02n.jpg)](./img/Noname_lht00su1_24c02n.jpg "Noname Lht00su1 24c02n"){ .glightbox data-gallery="noname-lht00su1" }
<span class="caption">Noname Lht00su1 24c02n</span>

</div>

