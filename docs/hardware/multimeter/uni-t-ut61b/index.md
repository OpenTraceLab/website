---
title: UNI-T UT61B
---

# UNI-T UT61B

<div class="infobox" markdown>

![UNI-T UT61B](./img/Uni-t_ut61b_device.png){ .infobox-image }

### UNI-T UT61B

| | |
|---|---|
| **Status** | supported |
| **Source code** | [uni-t-dmm](https://github.com/OpenTraceLab/OpenTraceCapture/tree/main/src/hardware/uni-t-dmm) |
| **Counts** | 4000 |
| **IEC 61010-1** | CAT II (600V) / CAT III (300V) |
| **Connectivity** | [RS232](https://sigrok.org/wiki/Device_cables#UNI-T_UT-D02) / [USB](https://sigrok.org/wiki/Device_cables#UNI-T_UT-D04) |
| **Measurements** | voltage, current, resistance, capacitance, frequency, duty cycle, diode, continuity, temperature |
| **Features** | autorange, data hold, min/max, rel, bargraph, backlight |
| **Website** | [uni-trend.com](http://www.uni-trend.com/UT61B.html) |

</div>

The **UNI-T UT61B** is a 4000 counts, CAT II (600V) / CAT III (300V) handheld digital multimeter with RS232 or USB connectivity.

See [UNI-T UT61B/Info](https://sigrok.org/wiki/UNI-T_UT61B/Info) for more details (such as **lsusb -v** output) about the device.

## Hardware

**Multimeter**:

- **Multimeter IC**: [Fortune Semiconductor FS9922-DMM3](https://sigrok.org/wiki/Multimeter_ICs#Fortune_Semiconductor_FS9922-DMM3) ([datasheet](http://www.ic-fortune.com/upload/Download/FS9922-DMM3-DS-10_EN.pdf))
- **Crystal**: 4MHz (markings: "3.999")
- **Fuses**: 0.5A/600V and 10A/600V (HRV fuses)

**RS232 cable**:

See [Device cables#UNI-T_UT-D02](https://sigrok.org/wiki/Device_cables#UNI-T_UT-D02).

**USB cable**:

See [Device cables#UNI-T_UT-D04](https://sigrok.org/wiki/Device_cables#UNI-T_UT-D04).

## Photos

<div class="photo-grid" markdown>

[![Uni T Ut61b Device](./img/Uni-t_ut61b_device.png)](./img/Uni-t_ut61b_device.png "Uni T Ut61b Device"){ .glightbox data-gallery="uni-t-ut61b" }
<span class="caption">Uni T Ut61b Device</span>

[![Uni T Ut61b Inside Back](./img/Uni-t_ut61b_inside-back.jpg)](./img/Uni-t_ut61b_inside-back.jpg "Uni T Ut61b Inside Back"){ .glightbox data-gallery="uni-t-ut61b" }
<span class="caption">Uni T Ut61b Inside Back</span>

[![Uni T Ut61b Back](./img/Uni-t_ut61b_back.jpg)](./img/Uni-t_ut61b_back.jpg "Uni T Ut61b Back"){ .glightbox data-gallery="uni-t-ut61b" }
<span class="caption">Uni T Ut61b Back</span>

[![Uni T Ut61b Battery](./img/Uni-t_ut61b_battery.jpg)](./img/Uni-t_ut61b_battery.jpg "Uni T Ut61b Battery"){ .glightbox data-gallery="uni-t-ut61b" }
<span class="caption">Uni T Ut61b Battery</span>

[![Uni T Ut61b Mugshot](./img/Uni-t_ut61b_mugshot.png)](./img/Uni-t_ut61b_mugshot.png "Uni T Ut61b Mugshot"){ .glightbox data-gallery="uni-t-ut61b" }
<span class="caption">Uni T Ut61b Mugshot</span>

[![Uni T Ut61b Pcb Front](./img/Uni-t_ut61b_pcb-front.jpg)](./img/Uni-t_ut61b_pcb-front.jpg "Uni T Ut61b Pcb Front"){ .glightbox data-gallery="uni-t-ut61b" }
<span class="caption">Uni T Ut61b Pcb Front</span>

[![Uni T Ut61b Inside Front](./img/Uni-t_ut61b_inside-front.jpg)](./img/Uni-t_ut61b_inside-front.jpg "Uni T Ut61b Inside Front"){ .glightbox data-gallery="uni-t-ut61b" }
<span class="caption">Uni T Ut61b Inside Front</span>

[![Uni T Ut61b Pcb Back](./img/Uni-t_ut61b_pcb-back.jpg)](./img/Uni-t_ut61b_pcb-back.jpg "Uni T Ut61b Pcb Back"){ .glightbox data-gallery="uni-t-ut61b" }
<span class="caption">Uni T Ut61b Pcb Back</span>

[![Uni T Ut61b Screen](./img/Uni-t_ut61b_screen.jpg)](./img/Uni-t_ut61b_screen.jpg "Uni T Ut61b Screen"){ .glightbox data-gallery="uni-t-ut61b" }
<span class="caption">Uni T Ut61b Screen</span>

</div>
## Protocol

See [Multimeter_ICs#Fortune_Semiconductor_FS9922-DMM3](https://sigrok.org/wiki/Multimeter_ICs#Fortune_Semiconductor_FS9922-DMM3) for the DMM IC protocol. Depending on the cable, additional transport-specific decoding is needed, though.

## Resources
- [Manual](http://www.uni-trend.com/manual2/UT61English.pdf)
- [Vendor software](http://www.uni-trend.com/Web%20site/DMM%20Software/UT61B%20setup.exe)

