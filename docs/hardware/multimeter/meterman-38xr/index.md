---
title: Meterman 38XR
---

# Meterman 38XR

<div class="infobox" markdown>

![Meterman 38XR](./img/Meterman-38xr-pcb.png){ .infobox-image }

### Meterman 38XR

| | |
|---|---|
| **Status** | supported |
| **Source code** | [serial-dmm](https://github.com/OpenTraceLab/OpenTraceCapture/tree/main/src/hardware/serial-dmm) |
| **Counts** | 10000 |
| **IEC 61010-1** | CAT III (1000V) / CAT IV (600V) |
| **Connectivity** | [ RS232](https://sigrok.org/wiki/Device_cables#Meterman_38XR_RS232_cable) |
| **Measurements** | voltage, current, resistance, continuity, diode, capacitance, temperature, frequency, duty cycle |
| **Features** | autorange, data hold, min/max, backlight |
| **Website** | [tequipment.net](https://www.tequipment.net/Wavetek38XR.html?b=y&amp;v=7973) |

</div>

The **Meterman 38XR** is a 10000 counts, CAT III 1000V, CAT IV 600V, handheld digital multimeter.

Press the **RS232 button** to enable the meter's transmission of measurements to the host.

## Hardware

TODO.

## Photos

<div class="photo-grid" markdown>

[![Meterman 38xr Pcb](./img/Meterman-38xr-pcb.png)](./img/Meterman-38xr-pcb.png "Meterman 38xr Pcb"){ .glightbox data-gallery="meterman-38xr" }
<span class="caption">Meterman 38xr Pcb</span>

[![Meterman 38xr Back](./img/Meterman-38xr-back.png)](./img/Meterman-38xr-back.png "Meterman 38xr Back"){ .glightbox data-gallery="meterman-38xr" }
<span class="caption">Meterman 38xr Back</span>

[![Meterman 38xr](./img/Meterman-38xr.png)](./img/Meterman-38xr.png "Meterman 38xr"){ .glightbox data-gallery="meterman-38xr" }
<span class="caption">Meterman 38xr</span>

[![Meterman 38xr Front](./img/Meterman-38xr-front.png)](./img/Meterman-38xr-front.png "Meterman 38xr Front"){ .glightbox data-gallery="meterman-38xr" }
<span class="caption">Meterman 38xr Front</span>

</div>
## Usage

Press the RS232 button so that RS232 lights up on the LCD.

```
 $ **sigrok-cli -d meterman-38xr:conn=/dev/ttyUSB0 --continuous**
 $ **smuview  --driver meterman-38xr:conn=/dev/ttyUSB0 **

```
## Protocol

The transmission of the measurement data is disabled by default. Pressing the RS232 button lights up the RS232 symbol on the display and starts transmitting data.
Data is sent in 15 byte chunks consisting of 13 hex nibbles encoded in ascii, followed by <CR><LF>

| Header 1 | Header 2 |
|---|---|
| Bytes 0-1 | Function code ie. Voltage DC, Resistance, etc. |
| Bytes 2-5 | BCD (Binary coded decimal) encoding of digits shown on the LCD |
| Bytes 6-7 | Bargraph segment value |
| Byte 8 | Range code, used to convert digits to actual value |
| Byte 9 | Current mode ie AC, DC or AC+DC |
| Byte 10 | Peak status ie. Min/Max/Avg |
| Byte 11 | Range settings ie. Auto, Manual |
| Byte 12 | Polarity of meter reading |

More information can be found in the [Protocol description ](https://www.elfadistrelec.fi/Web/Downloads/od/es/fj38XR-Serial-Output-Codes.pdf) document

## Resources
- [Manual](https://assets.tequipment.net/assets/1/26/Documents/38XR_Manual.pdf)
- [Protocol description ](https://www.elfadistrelec.fi/Web/Downloads/od/es/fj38XR-Serial-Output-Codes.pdf)
- [Protocol discussion in NI forum ](https://forums.ni.com/t5/Digital-Multimeters-DMMs-and/Meterman-DMM/td-p/179597?profile.language=en)
- [EEVBlog forum ](https://www.eevblog.com/forum/chat/meterman-38xr/)

