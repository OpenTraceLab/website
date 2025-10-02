---
title: GW Instek GDM-397
---

# GW Instek GDM-397

<div class="infobox" markdown>

![GW Instek GDM-397](./img/Gdm-397_rs232cable.jpg){ .infobox-image }

### GW Instek GDM-397

| | |
|---|---|
| **Status** | supported |
| **Source code** | [serial-dmm](https://github.com/OpenTraceLab/OpenTraceCapture/tree/main/src/hardware/serial-dmm) |
| **Counts** | 4000 |
| **IEC 61010-1** | CAT III (1000V) / CAT IV (600V) |
| **Connectivity** | [RS232](https://sigrok.org/wiki/Device_cables#UNI-T_UT-D02) |
| **Measurements** | voltage, current, resistance, capacitance, frequency, temperature, duty cycle, diode, continuity |
| **Features** | autorange, data hold, relative, backlight |
| **Website** | [gwinstek.com](https://www.gwinstek.com/en-global/products/detail/GDM-400_GDM-300) |

</div>

The **GW Instek GDM-397** is a 4000 count CAT III (1000V) / CAT IV (600V) handheld digital multimeter with RS232 connectivity.

It is similar to the [UNI-T UT61B](https://sigrok.org/wiki/UNI-T_UT61B), but not the same device/PCB (this appears to have improvet input protection along with HRC fuses).

Press and hold the **REL** button to enable serial data transmission.

## Hardware

**Multimeter**:

- **Multimeter IC**: [Fortune Semiconductor FS9922-DMM3](https://sigrok.org/wiki/Multimeter_ICs#Fortune_Semiconductor_FS9922-DMM3) ([datasheet](http://www.ic-fortune.com/upload/Download/FS9922-DMM3-DS-10_EN.pdf))
- **Crystal**: 4MHz (markings: "3.999")
- **Fuses**: 600mA H 1000V (6.35x31.8mm) and 10A H 1000V (10.3x38.1mm) (HRC fuses)

**RS232 cable**:

- Included (appears to be same as [Device cables#UNI-T_UT-D02](https://sigrok.org/wiki/Device_cables#UNI-T_UT-D02)).

**USB cable**:

- Optional (appears to be same as [Device cables#UNI-T_UT-D04](https://sigrok.org/wiki/Device_cables#UNI-T_UT-D04)).

## Photos

<div class="photo-grid" markdown>

[![Gdm 397 Rs232cable](./img/Gdm-397_rs232cable.jpg)](./img/Gdm-397_rs232cable.jpg "Gdm 397 Rs232cable"){ .glightbox data-gallery="gw-instek-gdm-397" }
<span class="caption">Gdm 397 Rs232cable</span>

[![Gdm 397 Front](./img/Gdm-397_front.jpg)](./img/Gdm-397_front.png "Gdm 397 Front"){ .glightbox data-gallery="gw-instek-gdm-397" }
<span class="caption">Gdm 397 Front</span>

[![Gdm 397 Pcb](./img/Gdm-397_pcb.jpg)](./img/Gdm-397_pcb.jpg "Gdm 397 Pcb"){ .glightbox data-gallery="gw-instek-gdm-397" }
<span class="caption">Gdm 397 Pcb</span>

</div>
## Protocol

See [Multimeter_ICs#Fortune_Semiconductor_FS9922-DMM3](https://sigrok.org/wiki/Multimeter_ICs#Fortune_Semiconductor_FS9922-DMM3) for the DMM IC protocol. Depending on the cable, additional transport-specific decoding is needed, though.

Serial data transmission must be enabled by a long press on the "REL" button.

## Resources
- [Datasheet](https://www.gwinstek.com/en-global/products/downloadSeriesDownNew/9914/718)
- [Manual](https://www.gwinstek.com/en-global/products/downloadSeriesDownNew/9890/718)

