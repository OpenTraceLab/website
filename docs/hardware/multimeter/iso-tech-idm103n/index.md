---
title: ISO-TECH IDM103N
---

# ISO-TECH IDM103N

<div class="infobox" markdown>

![ISO-TECH IDM103N](./img/Idm103n_01_front.png){ .infobox-image }

### ISO-TECH IDM103N

| | |
|---|---|
| **Status** | supported |
| **Source code** | [serial-dmm](https://github.com/OpenTraceLab/OpenTraceCapture/tree/main/src/hardware/serial-dmm) |
| **Counts** | 4000 |
| **IEC 61010-1** | CAT II (1000V) / CAT III (600V) |
| **Connectivity** | RS232 |
| **Measurements** | voltage, current, resistance, capacitance, frequency, rpm, diode, continuity |
| **Features** | autorange, data hold, bargraph, backlight |
| **Website** | [iso-tech.com.cn](http://iso-tech.com.cn/html/product.asp?id=279) |

</div>

The **ISO-TECH IDM103N** is a 4000 counts, CAT II (1000V) / CAT III (600V) handheld digital multimeter with RS232 connectivity.

## Hardware
- **Multimeter IC**: [Cyrustek ES51978](https://sigrok.org/wiki/Multimeter_ICs#Cyrustek_ES51978)
- **Crystal**: 4MHz

## Photos

<div class="photo-grid" markdown>

[![Idm103n 01 Front](./img/Idm103n_01_front.png)](./img/Idm103n_01_front.png "Idm103n 01 Front"){ .glightbox data-gallery="iso-tech-idm103n" }
<span class="caption">Idm103n 01 Front</span>

</div>
## Protocol

See [Multimeter_ICs#Cyrustek ES51978](https://sigrok.org/wiki/Multimeter_ICs#Cyrustek_ES51978) for the DMM IC protocol.

The transmission of the measurement data is disabled by default. The respective Cyrustek ES51978 pin (45, **RS232**) is hooked to an IR phototransitor so an IR LED has to be turned on in front of it to enable RS232 output. Pressing any button on any TV remote in front of it is enough to turn on the measurement transmission.

## Resources
- [Photo of ISO-TECH IDM73 RS232 cable](http://www.yeint.lv/en/e-store/detail.php?SECTION_ID=643&ELEMENT_ID=13195)

