---
title: Rohde&amp;Schwarz HMP 4000 series
---

# Rohde&amp;Schwarz HMP 4000 series

<div class="infobox" markdown>

![Rohde&amp;Schwarz HMP 4000 series](./img/Rs_hmp4040_front.jpg){ .infobox-image }

### Rohde&amp;Schwarz HMP 4000 series

| | |
|---|---|
| **Status** | supported |
| **Source code** | [scpi-pps](https://github.com/OpenTraceLab/OpenTraceCapture/tree/main/src/hardware/scpi-pps) |
| **Channels** | 3 / 4 |
| **Voltage/current (CH1)** | 0-32V / 0-10A |
| **Voltage/current (CH2)** | 0-32V / 0-10A |
| **Voltage/current (CH3)** | 0-32V / 0-10A |
| **Voltage/current (CH4)** | 0-32V / 0-10A |
| **Connectivity** | USB CDC, USB TMC, LAN |
| **Website** | [rohde-schwarz.com](https://www.rohde-schwarz.com/product/hmp4000) |

</div>

The **Rohde&Schwarz HMP 4000** series consists of the **HMP 4030** (3 channels) and **HMP 4040** (4 channels) models. Each channel provides up to 32V and up to 10A, with a maximum of 160W per channel, and a maximum of 384W for the total supply. The isolated channels can get connected in series or parallel to get higher voltages or currents (up to 128V or 40A).

The device ships with USB (CDC and TMC) and LAN by default, see the [ HO732](https://sigrok.org/wiki/Hameg_HO732) interface. GPIB is available as an option.

The **HMP 2000** series provides models with fewer channels and lower capabilities.

## Photos

<div class="photo-grid" markdown>

[![Rs Hmp4040 Front](./img/Rs_hmp4040_front.jpg)](./img/Rs_hmp4040_front.png "Rs Hmp4040 Front"){ .glightbox data-gallery="rohdeamp;schwarz-hmp-4000-series" }
<span class="caption">Rs Hmp4040 Front</span>

[![Rs Hmp4040 Back](./img/Rs_hmp4040_back.jpg)](./img/Rs_hmp4040_back.png "Rs Hmp4040 Back"){ .glightbox data-gallery="rohdeamp;schwarz-hmp-4000-series" }
<span class="caption">Rs Hmp4040 Back</span>

[![Rs Hmp4040 Mugshot](./img/Rs_hmp4040_mugshot.jpg)](./img/Rs_hmp4040_mugshot.png "Rs Hmp4040 Mugshot"){ .glightbox data-gallery="rohdeamp;schwarz-hmp-4000-series" }
<span class="caption">Rs Hmp4040 Mugshot</span>

</div>
## Use
```
 $ **sigrok-cli -d scpi-pps --scan**
 The following devices were found:
 scpi-pps - ROHDE&SCHWARZ HMP4040 HW50020003/SW2.62 [S/N: 104xxx] with 8 channels: V1 I1 V2 I2 V3 I3 V4 I4

```
```
 $ **sigrok-cli -d scpi-pps --show**
 Driver functions:
     Power supply
 Scan options:
     conn
     serialcomm
 scpi-pps - ROHDE&SCHWARZ HMP4040 HW50020003/SW2.62 [S/N: 104xxx] with 8 channels: V1 I1 V2 I2 V3 I3 V4 I4
 Channel groups:
     1: channels V1 I1
     2: channels V2 I2
     3: channels V3 I3
     4: channels V4 I4
 Supported configuration options across all channel groups:
     continuous: on, off
     limit_samples: 0 (current)
     limit_time: 0 (current)

```
## Resources
- [vendor's product page](https://www.rohde-schwarz.com/product/hmp4000) (redirects to some localized version)
- EEVBlog [episode 1173 forum thread](https://www.eevblog.com/forum/blog/eevblog-1173-rohde-schwarz-power-supply-bonanza/), [episode 1174 teardown video](https://www.youtube.com/watch?v=Z6F7Pwi6WLI)

