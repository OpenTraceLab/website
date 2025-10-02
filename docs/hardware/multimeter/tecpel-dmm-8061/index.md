---
title: Tecpel DMM-8061
---

# Tecpel DMM-8061

<div class="infobox" markdown>

![Tecpel DMM-8061](./img/Tecpel_dmm8061_device_back.jpg){ .infobox-image }

### Tecpel DMM-8061

| | |
|---|---|
| **Status** | supported |
| **Source code** | [serial-dmm](https://github.com/OpenTraceLab/OpenTraceCapture/tree/main/src/hardware/serial-dmm) |
| **Counts** | 4000 |
| **IEC 61010-1** | CAT IV (600V) |
| **Connectivity** | [RS232](https://sigrok.org/wiki/Device_cables#UNI-T_UT-D02) / [USB](https://sigrok.org/wiki/Device_cables#UNI-T_UT-D04) |
| **Measurements** | voltage, capacitance, continuity, diode, frequency, temperature, current, duty cycle |
| **Features** | autorange, true-rms, hold, relative |
| **Website** | [tecpel.net](http://www.tecpel.net/DMM-8061.html) |

</div>

The **Tecpel DMM-8061** is a 4000 counts, CAT IV (600V) handheld digital multimeter with RS232 or USB connectivity.

It seems to be a rebadged [Voltcraft VC-840](https://sigrok.org/wiki/Voltcraft_VC-840) (or vice versa), which is also rebadged (very likely a UNI-T model).

## Hardware

**Multimeter** (*the data below is not verified, just guessed from [Voltcraft VC-840](https://sigrok.org/wiki/Voltcraft_VC-840)*):

- **Multimeter IC**: [Fortune Semiconductor FS9721_LP3](http://www.ic-fortune.com/eng/new_product3_3.asp) ([datasheet](http://www.ic-fortune.com/upload/Download/FS9721_LP3-DS-20_EN.pdf))
- **Low power, True RMS-to-DC converter**: [Analog Devices AD737J](http://www.analog.com/en/special-linear-functions/rms-to-dc-converters/ad737/products/product.html) ([datasheet](http://www.analog.com/static/imported-files/data_sheets/AD737.pdf))
- **Unknown SO-8 chip**:&#160;?
- **Crystal**: likely 4MHz (not verified, though)
- **Fuses**: 10A/250V and 500mA/250V (one glass fuse, one HRV fuse)

**RS232 cable:**

See [Device cables#UNI-T_UT-D02](https://sigrok.org/wiki/Device_cables#UNI-T_UT-D02).

**USB cable:**

See [Device cables#UNI-T_UT-D04](https://sigrok.org/wiki/Device_cables#UNI-T_UT-D04).

## Photos

<div class="photo-grid" markdown>

[![Tecpel Dmm8061 Device Back](./img/Tecpel_dmm8061_device_back.jpg)](./img/Tecpel_dmm8061_device_back.jpg "Tecpel Dmm8061 Device Back"){ .glightbox data-gallery="tecpel-dmm-8061" }
<span class="caption">Tecpel Dmm8061 Device Back</span>

[![Tecpel Dmm8061](./img/Tecpel_dmm8061.png)](./img/Tecpel_dmm8061.png "Tecpel Dmm8061"){ .glightbox data-gallery="tecpel-dmm-8061" }
<span class="caption">Tecpel Dmm8061</span>

[![Tecpel Dmm8061 Device Front](./img/Tecpel_dmm8061_device_front.jpg)](./img/Tecpel_dmm8061_device_front.jpg "Tecpel Dmm8061 Device Front"){ .glightbox data-gallery="tecpel-dmm-8061" }
<span class="caption">Tecpel Dmm8061 Device Front</span>

</div>
## Protocol

See [Multimeter_ICs#Fortune_Semiconductor_FS9721_LP3](https://sigrok.org/wiki/Multimeter_ICs#Fortune_Semiconductor_FS9721_LP3) for the DMM IC protocol.

Depending on the cable, additional decoding is needed, though.

## Resources
- [Datasheet](http://www.tecpel.net/files/DMM8061_Spec_Data1.pdf)

