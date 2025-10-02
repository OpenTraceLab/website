---
title: Tenma 72-9380A
---

# Tenma 72-9380A

<div class="infobox" markdown>

![Tenma 72-9380A](./img/Tenma_72-9380A.jpg){ .infobox-image }

### Tenma 72-9380A

| | |
|---|---|
| **Status** | supported |
| **Source code** | [serial-dmm](https://github.com/OpenTraceLab/OpenTraceCapture/tree/main/src/hardware/serial-dmm) |
| **Counts** | 40000/4000 |
| **IEC 61010-1** | CAT III (1000V) / CAT IV (600V) |
| **Connectivity** | [RS232](https://sigrok.org/wiki/Device_cables#UNI-T_UT-D02) / [USB](https://sigrok.org/wiki/Device_cables#UNI-T_UT-D04) |
| **Measurements** | voltage, current, power, resistance, capacitance, frequency, temperature, duty cycle, diode, continuity |
| **Features** | autorange, true-rms, data hold, relative, backlight |
| **Website** | [mcmelectronics.com](http://www.mcmelectronics.com/product/TENMA-72-9380A-/72-9380A) |

</div>

The **Tenma 72-9380A** is a 40000/4000 count CAT III (1000V) / CAT IV (600V) handheld digital multimeter with RS232 or USB connectivity.

It is a rebadged [UNI-T UT71-E](https://sigrok.org/wiki/UNI-T_UT71x_series).

See [UNI-T UT71x series](https://sigrok.org/wiki/UNI-T_UT71x_series) for information common to all devices in this series.

## Hardware

**Multimeter**:

- LSD0007 (possibly TI MSP430 MCU?)
- [TI MSP430FE425](http://www.ti.com/product/msp430fe425) microcontroller
- [Cyrustek ES51966](http://www.cyrustek.com.tw/spec/ES51966A.pdf) DMM chip
- [Holtek HT1621](http://www.holtek.com/english/docum/consumer/1621.htm) LCD driver
- **PCB markings**: The silkscreen reads "71E (1KV FUSE) V20051120-9", but an additional "E" model indication is apparently added manually by UNI-T using a sticker.

**RS232 cable:**

- See [Device cables#UNI-T_UT-D02](https://sigrok.org/wiki/Device_cables#UNI-T_UT-D02).

**USB cable:**

- See [Device cables#UNI-T_UT-D04](https://sigrok.org/wiki/Device_cables#UNI-T_UT-D04).

## Photos

<div class="photo-grid" markdown>

[![Tenma 72 9380a](./img/Tenma_72-9380A.jpg)](./img/Tenma_72-9380A.png "Tenma 72 9380a"){ .glightbox data-gallery="tenma-72-9380a" }
<span class="caption">Tenma 72 9380a</span>

[![Tenma 72 9380a Pcb Front](./img/Tenma_72-9380A_PCB_front.jpg)](./img/Tenma_72-9380A_PCB_front.jpg "Tenma 72 9380a Pcb Front"){ .glightbox data-gallery="tenma-72-9380a" }
<span class="caption">Tenma 72 9380a Pcb Front</span>

[![Tenma 72 9380a Pcb Mcu Sticker](./img/Tenma_72-9380A_PCB_MCU_sticker.jpg)](./img/Tenma_72-9380A_PCB_MCU_sticker.jpg "Tenma 72 9380a Pcb Mcu Sticker"){ .glightbox data-gallery="tenma-72-9380a" }
<span class="caption">Tenma 72 9380a Pcb Mcu Sticker</span>

[![Tenma 72 9380a Pcb Mcu No Sticker](./img/Tenma_72-9380A_PCB_MCU_no_sticker.jpg)](./img/Tenma_72-9380A_PCB_MCU_no_sticker.jpg "Tenma 72 9380a Pcb Mcu No Sticker"){ .glightbox data-gallery="tenma-72-9380a" }
<span class="caption">Tenma 72 9380a Pcb Mcu No Sticker</span>

[![Tenma 72 9380a Pcb Back](./img/Tenma_72-9380A_PCB_back.jpg)](./img/Tenma_72-9380A_PCB_back.jpg "Tenma 72 9380a Pcb Back"){ .glightbox data-gallery="tenma-72-9380a" }
<span class="caption">Tenma 72 9380a Pcb Back</span>

</div>
## Protocol

See [UNI-T UT71x series#Protocol](https://sigrok.org/wiki/UNI-T_UT71x_series#Protocol).

## Resources
- [Manual](http://www.mcmelectronics.com/content/ProductData/Manuals/72-9380A.pdf)
- [Vendor software](http://www.mcmelectronics.com/content/ProductData/downloads/72-9380-Software.zip)

