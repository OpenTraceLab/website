---
title: Voltcraft VC-920
---

# Voltcraft VC-920

<div class="infobox" markdown>

![Voltcraft VC-920](./img/Voltcraft_vc920_pcb_bottom.jpg){ .infobox-image }

### Voltcraft VC-920

| | |
|---|---|
| **Status** | supported |
| **Source code** | [serial-dmm](https://github.com/OpenTraceLab/OpenTraceCapture/tree/main/src/hardware/serial-dmm) |
| **Counts** | 40000/4000 |
| **IEC 61010-1** | CAT III (1000V) / CAT IV (600V) |
| **Connectivity** | [RS232](https://sigrok.org/wiki/Device_cables#UNI-T_UT-D02) / [USB](https://sigrok.org/wiki/Device_cables#UNI-T_UT-D04) |
| **Measurements** | voltage, resistance, diode, continuity, capacitance, frequency, duty cycle, current, temperature |
| **Features** | autorange, hold, relative, min/max, bargraph, backlight |
| **Website** | [conrad.de](https://web.archive.org/web/20120824044029/http://www.conrad.de/ce/de/product/123296/VOLTCRAFT-VC920-TRMS-Digital-Multimeter-m-Software-VC900-Serie-400004000-Counts-CAT-IV-600V) |

</div>

The **Voltcraft VC-920** is a 40000/4000 counts, CAT III (1000V) / CAT IV (600V) handheld digital multimeter with RS232 or USB connectivity.

This is a rebadged [UNI-T UT71A](http://uni-trend.com/UT71A.html).

See [UNI-T UT71x series](https://sigrok.org/wiki/UNI-T_UT71x_series) for information common to all devices in this series.

## Hardware

**Multimeter**:

- **44000/440000-count dual-slope ADC**: [Cyrustek ES51966P](http://www.cyrustek.com.tw/product-1-44000.htm#ES51966) ([datasheet](http://www.cyrustek.com.tw/spec/ES51966A.pdf))
- **16-bit microcontroller**: [Texas Instruments MSP430F149](http://www.ti.com/product/msp430f149) (markings "TI 87E817T G4 LSD0007 REV N") ([datasheet](http://www.ti.com/lit/gpn/msp430f149))
- **128 (32 x 4) pattern multi-function LCD driver'**: [Holtek HT1621B](http://www.holtek.com.tw/english/docum/consumer/1621.htm) ([datasheet](http://www.holtek.com.tw/pdf/consumer/ht1621v310.pdf))
- **PCB markings**: The silkscreen reads "71A V20051010-6", but the correct "920" model indication is apparently added manually by UNI-T using a sticker.

**RS232 cable:**

- See [Device cables#UNI-T_UT-D02](https://sigrok.org/wiki/Device_cables#UNI-T_UT-D02).

**USB cable:**

- See [Device cables#UNI-T_UT-D04](https://sigrok.org/wiki/Device_cables#UNI-T_UT-D04).

## Photos

<div class="photo-grid" markdown>

[![Voltcraft Vc920 Pcb Bottom](./img/Voltcraft_vc920_pcb_bottom.jpg)](./img/Voltcraft_vc920_pcb_bottom.jpg "Voltcraft Vc920 Pcb Bottom"){ .glightbox data-gallery="voltcraft-vc-920" }
<span class="caption">Voltcraft Vc920 Pcb Bottom</span>

[![Voltcraft Vc920 Pcb Top](./img/Voltcraft_vc920_pcb_top.jpg)](./img/Voltcraft_vc920_pcb_top.jpg "Voltcraft Vc920 Pcb Top"){ .glightbox data-gallery="voltcraft-vc-920" }
<span class="caption">Voltcraft Vc920 Pcb Top</span>

[![Voltcraft Vc920](./img/Voltcraft_vc920.png)](./img/Voltcraft_vc920.png "Voltcraft Vc920"){ .glightbox data-gallery="voltcraft-vc-920" }
<span class="caption">Voltcraft Vc920</span>

</div>
## Protocol

See [UNI-T UT71x series#Protocol](https://sigrok.org/wiki/UNI-T_UT71x_series#Protocol).

## Resources
- [Manual](http://www.produktinfo.conrad.com/datenblaetter/100000-124999/123296-an-01-ml-VOLTCRAFT_VC920_DMM_de_en_fr_nl.pdf)
- [Vendor software](http://www.produktinfo.conrad.com/datenblaetter/100000-124999/123296-up-01-en-VC920DMM_WIN7_32_64bit_V3_00.zip)

