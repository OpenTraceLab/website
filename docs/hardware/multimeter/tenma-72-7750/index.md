---
title: Tenma 72-7750
---

# Tenma 72-7750

<div class="infobox" markdown>

![Tenma 72-7750](./img/Tenma_72-7750_PCB_top.jpg){ .infobox-image }

### Tenma 72-7750

| | |
|---|---|
| **Status** | supported |
| **Source code** | [serial-dmm](https://github.com/OpenTraceLab/OpenTraceCapture/tree/main/src/hardware/serial-dmm) |
| **Counts** | 6000 |
| **IEC 61010-1** | CAT III (1000V) / CAT IV (600V) |
| **Connectivity** | [RS232](https://sigrok.org/wiki/Device_cables#UNI-T_UT-D02) / [USB](https://sigrok.org/wiki/Device_cables#UNI-T_UT-D04) |
| **Measurements** | voltage, current, resistance, capacitance, frequency, duty cycle, temperature, diode, continuity |
| **Features** | autorange, true-rms, data hold, relative, backlight |
| **Website** | [mcmelectronics.com](http://www.mcmelectronics.com/product/TENMA-72-7750-/72-7750) |

</div>

The **Tenma 72-7750** is a 6000 count CAT III (1000V) / CAT IV (600V) handheld digital multimeter with RS232 or USB connectivity.

It is a rebadged [UNI-T UT60G](http://www.uni-trend.com/UT60G.html).

See [Tenma 72-7750/Info](https://sigrok.org/wiki/Tenma_72-7750/Info) for more details (such as **lsusb -v** output) about the device.

## Hardware
- **Multimeter IC**: [Cyrustek ES51986A](https://sigrok.org/wiki/Multimeter_ICs/Cyrustek_ES519xx) (markings: "cyrustek.com.tw ES51986A 1216-GH91")
- **Low-power JFET dual operational amplifiers**: [ST TL062C](http://www.st.com/web/en/catalog/sense_power/FM123/SC61/SS1378/PF65352) (markings: "ST 062C eZ048") ([datasheet](http://www.st.com/st-web-ui/static/active/en/resource/technical/document/datasheet/CD00000486.pdf))
- **Crystal**: 4MHz (markings: "3.999")
- **Fuses**: F500mA/250V, F10A/H250V (both are glass fuses)
- **Random PCB silkscreen markings**: "TRMS", "2008.12.10", "0604026"

**RS232 cable:**

- See [Device cables#UNI-T_UT-D02](https://sigrok.org/wiki/Device_cables#UNI-T_UT-D02).

**USB cable:**

- See [Device cables#UNI-T_UT-D04](https://sigrok.org/wiki/Device_cables#UNI-T_UT-D04).

## Photos

<div class="photo-grid" markdown>

[![Tenma 72 7750 Pcb Top](./img/Tenma_72-7750_PCB_top.jpg)](./img/Tenma_72-7750_PCB_top.jpg "Tenma 72 7750 Pcb Top"){ .glightbox data-gallery="tenma-72-7750" }
<span class="caption">Tenma 72 7750 Pcb Top</span>

[![Tenma 72 7750](./img/Tenma_72-7750.png)](./img/Tenma_72-7750.png "Tenma 72 7750"){ .glightbox data-gallery="tenma-72-7750" }
<span class="caption">Tenma 72 7750</span>

[![Tenma 72 7750 Pcb Bottom](./img/Tenma_72-7750_PCB_bottom.jpg)](./img/Tenma_72-7750_PCB_bottom.jpg "Tenma 72 7750 Pcb Bottom"){ .glightbox data-gallery="tenma-72-7750" }
<span class="caption">Tenma 72 7750 Pcb Bottom</span>

</div>
## Protocol

See [Multimeter ICs/Cyrustek ES519xx](https://sigrok.org/wiki/Multimeter_ICs/Cyrustek_ES519xx) for the DMM IC protocol. Depending on the cable, additional transport-specific decoding is needed, though.

## Resources
- [Manual](http://www.farnell.com/datasheets/70028.pdf)
- [Vendor software](http://www.mcmelectronics.com/content/ProductData/downloads/72-7750-Software.zip)
- [swharden.com: Tenma 72-7750 Multimeter Excellent for RF Engineering](http://www.swharden.com/blog/2013-04-17-tenma-72-7750-multimeter-excellent-for-rf-engineering/) (review)

