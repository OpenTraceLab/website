---
title: UNI-T UT71C
---

# UNI-T UT71C

<div class="infobox" markdown>

![UNI-T UT71C](./img/Ut71c_pcb_front.jpg){ .infobox-image }

### UNI-T UT71C

| | |
|---|---|
| **Status** | supported |
| **Source code** | [serial-dmm](https://github.com/OpenTraceLab/OpenTraceCapture/tree/main/src/hardware/serial-dmm) |
| **Counts** | 40000/4000 |
| **IEC 61010-1** | CAT III (1000V) / CAT IV (600V) |
| **Connectivity** | [RS232](https://sigrok.org/wiki/Device_cables#UNI-T_UT-D02) / [USB](https://sigrok.org/wiki/Device_cables#UNI-T_UT-D04) |
| **Measurements** | voltage, resistance, diode, continuity, capacitance, frequency, duty cycle, current, temperature |
| **Features** | autorange, hold, relative, min/max, bargraph, backlight, true-rms |
| **Website** | [uni-trend.com](http://uni-trend.com/UT71C.html) |

</div>

The **UNI-T UT71C** is a 40000/4000 counts, CAT III (1000V) / CAT IV (600V) handheld digital multimeter with RS232 or USB connectivity.

See [UNI-T UT71x series](https://sigrok.org/wiki/UNI-T_UT71x_series) for information common to all devices in this series.

## Hardware

**Multimeter**:

- **44000/440000-count dual-slope ADC**: [Cyrustek ES51966P](http://www.cyrustek.com.tw/product-1-44000.htm#ES51966) ([datasheet](http://www.cyrustek.com.tw/spec/ES51966A.pdf))
- **16-bit microcontroller**: Unknown, but likely to be Texas Instruments MSP430 model (based on other UT71x models)
- **128 (32 x 4) pattern multi-function LCD driver**: [HOLTEK HT1621B](http://www.holtek.com.tw/english/docum/consumer/1621.htm) ([datasheet](http://www.holtek.com.tw/pdf/consumer/ht1621v310.pdf))
- **PCB markings**: The silkscreen reads "71A(1KV FUSE) V20051010-10", but the correct "C" model indication is apparently added manually by UNI-T using a sharpie.
**Other known variants**: ["71A(1KV FUSE) V20051010-8"](http://www.eevblog.com/forum/testgear/uni-trend-ut71c/?action=dlattach;attach=61486;image), ["71A V20051010-8"](http://www.eevblog.com/forum/testgear/hacking-the-uni-t-ut71c-%28wipneed-help%29/msg440238/#msg440238), ["71A V20051010-6"](http://www.eevblog.com/forum/testgear/uni-trend-ut71c/?action=dlattach;attach=43032;image), ["V20051010-4"](http://cache.amobbs.com/bbs_upload782111/files_26/ourdev_532885.JPG)

**RS232 cable:**

- See [Device cables#UNI-T_UT-D02](https://sigrok.org/wiki/Device_cables#UNI-T_UT-D02).

**USB cable:**

- See [Device cables#UNI-T_UT-D04](https://sigrok.org/wiki/Device_cables#UNI-T_UT-D04).

## Photos

<div class="photo-grid" markdown>

[![Ut71c Pcb Front](./img/Ut71c_pcb_front.jpg)](./img/Ut71c_pcb_front.jpg "Ut71c Pcb Front"){ .glightbox data-gallery="uni-t-ut71c" }
<span class="caption">Ut71c Pcb Front</span>

[![Ut71c Mugshot](./img/Ut71c_mugshot.jpg)](./img/Ut71c_mugshot.png "Ut71c Mugshot"){ .glightbox data-gallery="uni-t-ut71c" }
<span class="caption">Ut71c Mugshot</span>

[![Ut71c Pcb Backside](./img/Ut71c_pcb_backside.jpg)](./img/Ut71c_pcb_backside.jpg "Ut71c Pcb Backside"){ .glightbox data-gallery="uni-t-ut71c" }
<span class="caption">Ut71c Pcb Backside</span>

[![Ut71c Pcb Backside Lower](./img/Ut71c_pcb_backside_lower.jpg)](./img/Ut71c_pcb_backside_lower.jpg "Ut71c Pcb Backside Lower"){ .glightbox data-gallery="uni-t-ut71c" }
<span class="caption">Ut71c Pcb Backside Lower</span>

[![Ut71c Pcb Backside Upper](./img/Ut71c_pcb_backside_upper.jpg)](./img/Ut71c_pcb_backside_upper.jpg "Ut71c Pcb Backside Upper"){ .glightbox data-gallery="uni-t-ut71c" }
<span class="caption">Ut71c Pcb Backside Upper</span>

</div>
## Protocol

See [UNI-T UT71x series#Protocol](https://sigrok.org/wiki/UNI-T_UT71x_series#Protocol).

## Resources
- [Specifications](http://uni-trend.com/UT71C.html)
- [Manual](http://uni-trend.com/manual2/UT71CDE%20Eng%20Manual.pdf)
- [Vendor software](http://uni-trend.com/software/UT71C_D_E%20setup.exe)
- [eevblog.com: Uni-Trend UT71C](http://www.eevblog.com/forum/testgear/uni-trend-ut71c/msg297042/#msg297042) (teardown)
- [amobbs.com: UT71C](http://www.amobbs.com/thread-3876959-1-1.html) (teardown)
- [amobbs.com: UT71C](http://www.amobbs.com/forum.php?mod=viewthread&tid=3876959&page=1&authorid=32351) (another teardown)

