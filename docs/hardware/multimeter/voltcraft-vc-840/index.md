---
title: Voltcraft VC-840
---

# Voltcraft VC-840

<div class="infobox" markdown>

![Voltcraft VC-840](./img/Voltcraft_vc840_pcb_back.jpg){ .infobox-image }

### Voltcraft VC-840

| | |
|---|---|
| **Status** | supported |
| **Source code** | [serial-dmm](https://github.com/OpenTraceLab/OpenTraceCapture/tree/main/src/hardware/serial-dmm) |
| **Counts** | 4000 |
| **IEC 61010-1** | CAT IV (600V) |
| **Connectivity** | [RS232](https://sigrok.org/wiki/Device_cables#UNI-T_UT-D02) / [USB](https://sigrok.org/wiki/Device_cables#UNI-T_UT-D04) |
| **Measurements** | voltage, capacitance, continuity, diode, frequency, temperature, current, duty cycle |
| **Features** | autorange, true-rms, hold, relative |
| **Website** | [conrad.de](http://www.conrad.de/ce/de/product/123295/VOLTCRAFT-VC840-DMM/SHOP_AREA_17622&amp;promotionareaSearchDetail=005) |

</div>

The **Voltcraft VC-840** is a 4000 counts, CAT IV (600V) handheld digital multimeter with RS232 or USB connectivity.

## Hardware

**Multimeter**:

- **Multimeter IC**: [Fortune Semiconductor FS9721_LP3](http://www.ic-fortune.com/eng/new_product3_3.asp) ([datasheet](http://www.ic-fortune.com/upload/Download/FS9721_LP3-DS-20_EN.pdf))
- **Low power, True RMS-to-DC converter**: [Analog Devices AD737J](http://www.analog.com/en/special-linear-functions/rms-to-dc-converters/ad737/products/product.html) ([datasheet](http://www.analog.com/static/imported-files/data_sheets/AD737.pdf))
- **Unknown SO-8 chip**:&#160;?
- **Crystal**: likely 4MHz (not verified, though)
- **Fuses**: 10A/250V and 500mA/250V (one glass fuse, one HRV fuse)

**RS232 cable:**

- See [Device cables#UNI-T_UT-D02](https://sigrok.org/wiki/Device_cables#UNI-T_UT-D02).

**USB cable:**

- See [Device cables#UNI-T_UT-D04](https://sigrok.org/wiki/Device_cables#UNI-T_UT-D04).

## Photos

<div class="photo-grid" markdown>

[![Voltcraft Vc840 Pcb Back](./img/Voltcraft_vc840_pcb_back.jpg)](./img/Voltcraft_vc840_pcb_back.jpg "Voltcraft Vc840 Pcb Back"){ .glightbox data-gallery="voltcraft-vc-840" }
<span class="caption">Voltcraft Vc840 Pcb Back</span>

[![Voltcraft Vc840 Device Back1](./img/Voltcraft_vc840_device_back1.jpg)](./img/Voltcraft_vc840_device_back1.jpg "Voltcraft Vc840 Device Back1"){ .glightbox data-gallery="voltcraft-vc-840" }
<span class="caption">Voltcraft Vc840 Device Back1</span>

[![Voltcraft Vc840 Device Front](./img/Voltcraft_vc840_device_front.jpg)](./img/Voltcraft_vc840_device_front.png "Voltcraft Vc840 Device Front"){ .glightbox data-gallery="voltcraft-vc-840" }
<span class="caption">Voltcraft Vc840 Device Front</span>

[![Voltcraft Vc840 Device Back2](./img/Voltcraft_vc840_device_back2.jpg)](./img/Voltcraft_vc840_device_back2.jpg "Voltcraft Vc840 Device Back2"){ .glightbox data-gallery="voltcraft-vc-840" }
<span class="caption">Voltcraft Vc840 Device Back2</span>

[![Voltcraft Vc840 Device Front](./img/Voltcraft_vc840_device_front.jpg)](./img/Voltcraft_vc840_device_front.jpg "Voltcraft Vc840 Device Front"){ .glightbox data-gallery="voltcraft-vc-840" }
<span class="caption">Voltcraft Vc840 Device Front</span>

[![Voltcraft Vc840 Battery2](./img/Voltcraft_vc840_battery2.jpg)](./img/Voltcraft_vc840_battery2.jpg "Voltcraft Vc840 Battery2"){ .glightbox data-gallery="voltcraft-vc-840" }
<span class="caption">Voltcraft Vc840 Battery2</span>

[![Voltcraft Vc840 Pcb Front](./img/Voltcraft_vc840_pcb_front.jpg)](./img/Voltcraft_vc840_pcb_front.jpg "Voltcraft Vc840 Pcb Front"){ .glightbox data-gallery="voltcraft-vc-840" }
<span class="caption">Voltcraft Vc840 Pcb Front</span>

[![Voltcraft Vc840 Battery1](./img/Voltcraft_vc840_battery1.jpg)](./img/Voltcraft_vc840_battery1.jpg "Voltcraft Vc840 Battery1"){ .glightbox data-gallery="voltcraft-vc-840" }
<span class="caption">Voltcraft Vc840 Battery1</span>

[![Voltcraft Vc840 Fs9721 Lp3](./img/Voltcraft_vc840_fs9721_lp3.jpg)](./img/Voltcraft_vc840_fs9721_lp3.jpg "Voltcraft Vc840 Fs9721 Lp3"){ .glightbox data-gallery="voltcraft-vc-840" }
<span class="caption">Voltcraft Vc840 Fs9721 Lp3</span>

[![Voltcraft Vc840 Ad737j](./img/Voltcraft_vc840_ad737j.jpg)](./img/Voltcraft_vc840_ad737j.jpg "Voltcraft Vc840 Ad737j"){ .glightbox data-gallery="voltcraft-vc-840" }
<span class="caption">Voltcraft Vc840 Ad737j</span>

</div>
## Protocol

See [Multimeter_ICs#Fortune_Semiconductor_FS9721_LP3](https://sigrok.org/wiki/Multimeter_ICs#Fortune_Semiconductor_FS9721_LP3) for the DMM IC protocol.

Depending on the cable, additional decoding is needed, though.

TODO: Serial cable vs. the two USB HID based cables.

A [short protocol description is also available from Voltcraft/Conrad](http://www.produktinfo.conrad.com/datenblaetter/100000-124999/123295-da-01-en-RS232_Protocol_VOLTCRAFT_VC840_DMM.pdf). And [another one](http://www2.produktinfo.conrad.com/datenblaetter/100000-124999/121112-da-01-en-Digitalmultimeter_VC840_Schnittstellenp.pdf).

## Resources
- [Manual](http://www.produktinfo.conrad.com/datenblaetter/100000-124999/123295-an-01-ml-VOLTCRAFT_VC840_DMM_de_en_fr_nl.pdf)
- [Vendor software](http://www.produktinfo.conrad.com/datenblaetter/100000-124999/123295-up-01-en-Win7_32_64_Bit_VC840_DMM.zip)
- [gecius.de: Multimeter VC840](http://www.gecius.de/linux/vc840/)
- [kolleegium.ch: VC 840 Recorder](http://cw.kolleegium.ch/vc840/)
- [true random: driver for the cheap digital multimeter VC 840/VC 820](http://www.true-random.com/driver-for-the-cheap-digital-multimeter-vc-840vc-820.html)
- [true random: Software for the multimeters vc840/vc820](http://true-random.com/homepage/projects/vc840/index.html)
- [Georg Acher: Voltcraft VC820/VC840 und Linux](http://www.lrr.in.tum.de/~acher/vc840/index.html)

