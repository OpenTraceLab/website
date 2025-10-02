---
title: Voltcraft VC-940
---

# Voltcraft VC-940

<div class="infobox" markdown>

![Voltcraft VC-940](./img/Voltcraft_vc940.jpg){ .infobox-image }

### Voltcraft VC-940

| | |
|---|---|
| **Status** | supported |
| **Source code** | [serial-dmm](https://github.com/OpenTraceLab/OpenTraceCapture/tree/main/src/hardware/serial-dmm) |
| **Counts** | 40000/4000 |
| **IEC 61010-1** | CAT III (1000V) / CAT IV (600V) |
| **Connectivity** | [RS232](https://sigrok.org/wiki/Device_cables#UNI-T_UT-D02) / [USB](https://sigrok.org/wiki/Device_cables#UNI-T_UT-D04) |
| **Measurements** | voltage, resistance, diode, continuity, capacitance, frequency, duty cycle, current, temperature |
| **Features** | autorange, hold, relative, min/max, bargraph, backlight, true-rms |
| **Website** | [conrad.de](https://web.archive.org/web/20131107075144/http://www.conrad.de/ce/de/product/123297/VOLTCRAFT-VC940-TRMS-Digital-Multimeter-m-Software-und-Leistungsmessadapter-VC900-Serie-400004000-Counts-CAT-IV-600V) |

</div>

The **Voltcraft VC-940** is a 40000/4000 counts, CAT III (1000V) / CAT IV (600V) handheld digital multimeter with RS232 or USB connectivity.

This is a rebadged [UNI-T UT71E](http://uni-trend.com/UT71E.html).

See [UNI-T UT71x series](https://sigrok.org/wiki/UNI-T_UT71x_series) for information common to all devices in this series.

## Hardware

**Multimeter**:

- [Cyrustek ES51966F](http://www.cyrustek.com.tw/spec/ES51966A.pdf) multimeter chip
- [Texas Instruments MSP430F149](http://www.ti.com/product/msp430f149) 16 bit microcontroller with 60K flash and 2K RAM on board
- [Texas Instruments MSP430FE425](http://www.ti.com/product/msp430fe425) 16 bit microcontroller for energy meters with 16K flash and 512B RAM on board
- [HOLTEK HT1621B](http://www.holtek.com.tw/english/docum/consumer/1621.htm) 128 (32 x 4) pattern multi-function LCD driver
- **PCB markings**: The silkscreen reads "71E V20051120-3", but the correct "940" model indication is apparently added manually by UNI-T using a sticker.

**RS232 cable:**

- See [Device cables#UNI-T_UT-D02](https://sigrok.org/wiki/Device_cables#UNI-T_UT-D02).

**USB cable:**

- See [Device cables#UNI-T_UT-D04](https://sigrok.org/wiki/Device_cables#UNI-T_UT-D04).

## Photos

<div class="photo-grid" markdown>

[![Voltcraft Vc940](./img/Voltcraft_vc940.jpg)](./img/Voltcraft_vc940.png "Voltcraft Vc940"){ .glightbox data-gallery="voltcraft-vc-940" }
<span class="caption">Voltcraft Vc940</span>

[![Voltcraft Vc940 Pcb Bottom](./img/Voltcraft_vc940_pcb_bottom.jpg)](./img/Voltcraft_vc940_pcb_bottom.jpg "Voltcraft Vc940 Pcb Bottom"){ .glightbox data-gallery="voltcraft-vc-940" }
<span class="caption">Voltcraft Vc940 Pcb Bottom</span>

[![Voltcraft Vc940 Pcb Top](./img/Voltcraft_vc940_pcb_top.jpg)](./img/Voltcraft_vc940_pcb_top.jpg "Voltcraft Vc940 Pcb Top"){ .glightbox data-gallery="voltcraft-vc-940" }
<span class="caption">Voltcraft Vc940 Pcb Top</span>

</div>
## Protocol

See [UNI-T UT71x series#Protocol](https://sigrok.org/wiki/UNI-T_UT71x_series#Protocol).

## Resources
- [Manual](http://www.produktinfo.conrad.com/datenblaetter/100000-124999/123297-an-01-ml-VOLTCRAFT_VC940_DMM_de_en_fr_nl.pdf)
- [Vendor software](http://www.produktinfo.conrad.com/datenblaetter/100000-124999/123297-up-01-en-VC940DMM_WIN7_32_64bit_V3_00.zip)
- [Calibration instructions](http://www.produktinfo.conrad.com/datenblaetter/100000-124999/123297-an-01-en-Kalibrieranleitung_VC940.pdf)
- [Schematic](http://elektrotanya.com/unit_multimeter_vc940.pdf/download.html)

