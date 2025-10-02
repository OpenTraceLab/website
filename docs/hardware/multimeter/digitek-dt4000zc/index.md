---
title: Digitek DT4000ZC
---

# Digitek DT4000ZC

<div class="infobox" markdown>

![Digitek DT4000ZC](./img/Digitek_dt4000zc_device_front.png){ .infobox-image }

### Digitek DT4000ZC

| | |
|---|---|
| **Status** | supported |
| **Source code** | [serial-dmm](https://github.com/OpenTraceLab/OpenTraceCapture/tree/main/src/hardware/serial-dmm) |
| **Counts** | 4000 |
| **IEC 61010-1** | CAT II (600V) |
| **Connectivity** | [RS232](https://sigrok.org/wiki/Device_cables#Digitek_DT4000ZC_cable) |
| **Measurements** | voltage, resistance, continuity, diode, capacitance, frequency, temperature, current, duty cycle |
| **Features** | autorange, data hold, relative |
| **Website** | [digitek.com.hk](http://www.digitek.com.hk/en/cpxx.php?id=697) |

</div>

The **Digitek DT4000ZC** is a 4000 counts, CAT II (600V) handheld digital multimeter with RS232 connectivity.

It is also sold under the name [TekPower TP4000ZC](https://sigrok.org/wiki/TekPower_TP4000ZC).

## Hardware

**Multimeter:**

- TODO.

**Cable:**

- See [Device_cables#Digitek_DT4000ZC_cable](https://sigrok.org/wiki/Device_cables#Digitek_DT4000ZC_cable).

## Photos

<div class="photo-grid" markdown>

[![Digitek Dt4000zc Device Front](./img/Digitek_dt4000zc_device_front.png)](./img/Digitek_dt4000zc_device_front.png "Digitek Dt4000zc Device Front"){ .glightbox data-gallery="digitek-dt4000zc" }
<span class="caption">Digitek Dt4000zc Device Front</span>

</div>
## Protocol

See [Multimeter_ICs#Fortune_Semiconductor_FS9721_LP3](https://sigrok.org/wiki/Multimeter_ICs#Fortune_Semiconductor_FS9721_LP3).

User bit 2 is used to indicate temperature measurement in degrees Celsius.

## Resources
- [Manual](http://www.elv-downloads.de/service/manuals_hw/45986_DT4000_ZD_V1.01_UM.pdf) (German)
- [Vendor software](http://www.elv-downloads.de/Assets/Produkte/4/459/45986/Downloads/45986_Usersoftware_Win7.zip) ([ELV user-contributed Linux software](http://www.elv-downloads.de/service/manuals_hw/45986_DT4000ZC_Linux_Software.tar.gz))
- [Video review of TP4000ZC (Part 1/2)](http://www.youtube.com/watch?v=kXzAD74C5As) (same device as the Digitek DT4000ZC)
- [Video review of TP4000ZC (Part 2/2)](http://www.youtube.com/watch?v=7pbRLom7bNc) (same device as the Digitek DT4000ZC)
- [TP4000ZC serial protocol](http://www.multimeterwarehouse.com/TP4000ZC/TP4000ZC_serial_protocol.pdf) (same device as the Digitek DT4000ZC)
- [thelastinstance.de: Using the DT4000ZC for monitoring purposes](http://thelastinstance.de/elek/project14.phtml)
[45986_DT4000ZC_Linux_Software.tar.gz](http://thelastinstance.de/uploads/files/45986_DT4000ZC_Linux_Software.tar.gz), [readpower.tar.gz](http://thelastinstance.de/uploads/files/readpower.tar.gz)

