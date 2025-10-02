---
title: Tenma 72-7730
---

# Tenma 72-7730

<div class="infobox" markdown>

![Tenma 72-7730](./img/Tenma_72-7730_PCB_MCU.jpg){ .infobox-image }

### Tenma 72-7730

| | |
|---|---|
| **Status** | supported |
| **Source code** | [serial-dmm](https://github.com/OpenTraceLab/OpenTraceCapture/tree/main/src/hardware/serial-dmm) |
| **Counts** | 20000/2000 |
| **IEC 61010-1** | CAT III (1000V) / CAT IV (600V) |
| **Connectivity** | [RS232](https://sigrok.org/wiki/Device_cables#UNI-T_UT-D02) / [USB](https://sigrok.org/wiki/Device_cables#UNI-T_UT-D04) |
| **Measurements** | voltage, current, resistance, capacitance, frequency, temperature, duty cycle, diode, continuity |
| **Features** | autorange, true-rms, data hold, relative, backlight |
| **Website** | [mcmelectronics.com](http://www.mcmelectronics.com/product/TENMA-72-7730-/72-7730) |

</div>

The **Tenma 72-7730** is a 20000/2000 count CAT III (1000V) / CAT IV (600V) handheld digital multimeter with RS232 or USB connectivity.

It is a rebadged [UNI-T UT71-B](https://sigrok.org/wiki/UNI-T_UT71x_series).

See [UNI-T UT71x series](https://sigrok.org/wiki/UNI-T_UT71x_series) for information common to all devices in this series.

## Hardware

**Multimeter**:

- **44000/440000-count dual-slope ADC**: [Cyrustek ES51966P](http://www.cyrustek.com.tw/product-1-44000.htm#ES51966) ([datasheet](http://www.cyrustek.com.tw/spec/ES51966A.pdf))
- **16-bit microcontroller**: [Texas Instruments MSP430F149](http://www.ti.com/product/msp430f149) (markings "TI 14AH00W G4 LSD0007 REV S") ([datasheet](http://www.ti.com/lit/gpn/msp430f149))
- **128 (32 x 4) pattern multi-function LCD driver'**: [Holtek HT1621B](http://www.holtek.com.tw/english/docum/consumer/1621.htm) ([datasheet](http://www.holtek.com.tw/pdf/consumer/ht1621v310.pdf))
- **PCB markings**: The silkscreen reads "71A V20051010-8", but the correct "B" model indication is apparently added manually by UNI-T using a a sharpie and a sticker.

**RS232 cable:**

- See [Device cables#UNI-T_UT-D02](https://sigrok.org/wiki/Device_cables#UNI-T_UT-D02).

**USB cable:**

- See [Device cables#UNI-T_UT-D04](https://sigrok.org/wiki/Device_cables#UNI-T_UT-D04).

## Photos

<div class="photo-grid" markdown>

[![Tenma 72 7730 Pcb Mcu](./img/Tenma_72-7730_PCB_MCU.jpg)](./img/Tenma_72-7730_PCB_MCU.jpg "Tenma 72 7730 Pcb Mcu"){ .glightbox data-gallery="tenma-72-7730" }
<span class="caption">Tenma 72 7730 Pcb Mcu</span>

[![Tenma 72 7730 Pcb Front](./img/Tenma_72-7730_PCB_front.jpg)](./img/Tenma_72-7730_PCB_front.jpg "Tenma 72 7730 Pcb Front"){ .glightbox data-gallery="tenma-72-7730" }
<span class="caption">Tenma 72 7730 Pcb Front</span>

[![Tenma 72 7730 Pcb Back](./img/Tenma_72-7730_PCB_back.jpg)](./img/Tenma_72-7730_PCB_back.jpg "Tenma 72 7730 Pcb Back"){ .glightbox data-gallery="tenma-72-7730" }
<span class="caption">Tenma 72 7730 Pcb Back</span>

[![Tenma 72 7730](./img/Tenma_72-7730.jpg)](./img/Tenma_72-7730.png "Tenma 72 7730"){ .glightbox data-gallery="tenma-72-7730" }
<span class="caption">Tenma 72 7730</span>

</div>
## Protocol

See [UNI-T UT71x series#Protocol](https://sigrok.org/wiki/UNI-T_UT71x_series#Protocol).

## Resources
- [Manual](http://www.mcmelectronics.com/content/ProductData/Manuals/72-7730.pdf)
- [Vendor software](http://www.mcmelectronics.com/content/ProductData/downloads/72-7730-Software.zip)
- [Calibration procedure](http://www.element14.com/community/servlet/JiveServlet/download/1856-1718/UT71B%20Calibration%20Procedure.xls)

