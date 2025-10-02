---
title: SparkFun 70C
---

# SparkFun 70C

<div class="infobox" markdown>

![SparkFun 70C](./img/Sparkfun_70c_mugshot.png){ .infobox-image }

### SparkFun 70C

| | |
|---|---|
| **Status** | supported |
| **Source code** | [serial-dmm](https://github.com/OpenTraceLab/OpenTraceCapture/tree/main/src/hardware/serial-dmm) |
| **Counts** | 6000 |
| **IEC 61010-1** | CAT II |
| **Connectivity** | USB (standard cable) |
| **Measurements** | voltage, current, resistance, continuity, diode, capacitance, frequency, temperature |
| **Features** | max/min, data hold, relative, backlight |
| **Website** | [sparkfun.com](https://www.sparkfun.com/products/12967) |

</div>

The **SparkFun 70C** is a 6000 counts, CAT II handheld digital multimeter with USB connectivity.

It appears to be heavily based on the [Victor 70C](https://sigrok.org/wiki/Victor_70C), but with a USB to serial adapter instead of a USB HID device adapter, and different trimpot adjustments.

## Hardware
- [Fortune Semiconductor FS9922-DMM4](http://www.ic-fortune.com/upload/Download/FS9922-DMM4-DS-11_EN.pdf) multimeter chip
- [Silicon Labs CP2102 USB to Serial adapter](https://octopart.com/cp2102-gm-silicon+labs-519902)

**Unverified hardware (some parts on PCB are not clear enough to read; assumptions based on Victor 70C)**:

- [NXP HEF4066BT](http://datasheet.octopart.com/HEF4066BT-Philips-datasheet-87533.pdf) quadruple bilateral switches
- [Microchip TC7660E](http://datasheet.octopart.com/TC7660EOA-Microchip-datasheet-1009.pdf) charge pump DC-to-DC voltage converter
- [Texas Instruments 27L2C](http://datasheet.octopart.com/TLC27L2CP-Texas-Instruments-datasheet-151061.pdf) precision dual op-amp

**Note**: The USB/HID chip is *in the multimeter* (not in the USB cable/connector) for this device. The device is connected to the PC using a standard USB cable (without any internal logic/chip).

## Photos

<div class="photo-grid" markdown>

[![Sparkfun 70c Mugshot](./img/Sparkfun_70c_mugshot.png)](./img/Sparkfun_70c_mugshot.png "Sparkfun 70c Mugshot"){ .glightbox data-gallery="sparkfun-70c" }
<span class="caption">Sparkfun 70c Mugshot</span>

</div>
## Protocol

See [FS9922-DMM4](https://sigrok.org/wiki/Multimeter_ICs#Fortune_Semiconductor_FS9922-DMM4).

## Resources
- [Manual](https://cdn.sparkfun.com/datasheets/Tools/601e-070c-000abw.pdf)
- [Vendor software](https://cdn.sparkfun.com/datasheets/Tools/setup_70c_multi.rar)

