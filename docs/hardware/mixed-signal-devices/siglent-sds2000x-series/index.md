---
title: Siglent SDS2000X series
---

# Siglent SDS2000X series

<div class="infobox" markdown>

![Siglent SDS2000X series](./img/Sds2304x-mugshot.png){ .infobox-image }

### Siglent SDS2000X series

| | |
|---|---|
| **Status** | supported |
| **Source code** | [siglent-sds](https://github.com/OpenTraceLab/OpenTraceCapture/tree/main/src/hardware/siglent-sds) |
| **Channels** | 2-4 analog, 16 digital |
| **Samplerate** | up to 2GSa/s |
| **Analog bandwidth** | 70-300MHz |
| **Vertical resolution** | 8bits |
| **Triggers** | edge, slope, pulse width, window, runt, interval, dropout, pattern, video, serial bus |
| **Input impedance** | 1MΩ‖18pF 400Vp CAT I, 50Ω 5V RMS |
| **Memory** | 140Mpts |
| **Display** | 8" VGA (800x480) |
| **Connectivity** | USB host/device, ethernet, pass/fail, trig out, GPIB (optional) |
| **Website** | [siglent.com](http://www.siglent.com/ens/) |

</div>

The **Siglent SDS2000X series** of oscilloscopes supports samplerates of 2GSa/s, up to 4 analog channels with up to 300MHz bandwidth, and up to 16 logic channels with up to 500MSa/s.

See [Siglent SDS2000X series/Info](https://sigrok.org/wiki/Siglent_SDS2000X_series/Info) for more details (such as **lsusb -v** output) about the device.

## Hardware

The Siglent SDS2000X series oscilloscopes are capable of sampling up to 2GSa/s 140 Mpts/CH memory for the analog channels. Due to the fact that the 2 channels are shared, if both channels are on the sampling is limited to 1GSa/s and 70 Mpts/CH memory per channel. This is also true with the 4 channel devices. The analog channels have history memory where 80000 frames are stored and can be viewed via the scopes History function.

All devices have the logic analyzer and DDS arbitrary waveform generator built-in. Keep in mind that for the logic analyzer and waveform generator an extra software option must be purchased. For the logic analyzer an additional probe device (SPL2016) must also be purchased. The logic analyzer is capable 500 MSa/s with 140 Mpts/CH memory.

The older series SDS2000X Logic Analyzer function does not support acquisition of the LA channels over VXI or USB. Due to flash memory program limitations the code for this function does not fit. Its not clear if newer "E" scopes will come functionality for the SDS2000 series scopes. 

An extra software option to decode serial protocols is also available on all devices.

| Model | Bandwidth | Analog channels | Digital channels |
|---|---|---|---|
| SDS2304X | 300MHz | 4 | 16 |
| SDS2302X | 300MHz | 2 | 16 |
| SDS2204X | 200MHz | 4 | 16 |
| SDS2202X | 200MHz | 2 | 16 |
| SDS2104X | 100MHz | 4 | 16 |
| SDS2102X | 100MHz | 2 | 16 |
| SDS2074X | 70MHz | 4 | 16 |
| SDS2072X | 70MHz | 2 | 16 |

## Photos

<div class="photo-grid" markdown>

[![Sds2304x Mugshot](./img/Sds2304x-mugshot.png)](./img/Sds2304x-mugshot.png "Sds2304x Mugshot"){ .glightbox data-gallery="siglent-sds2000x-series" }
<span class="caption">Sds2304x Mugshot</span>

[![Sds2000x Logic Probe 3](./img/Sds2000x-logic-probe-3.png)](./img/Sds2000x-logic-probe-3.png "Sds2000x Logic Probe 3"){ .glightbox data-gallery="siglent-sds2000x-series" }
<span class="caption">Sds2000x Logic Probe 3</span>

[![Sds2000x Connectors](./img/Sds2000x-connectors.png)](./img/Sds2000x-connectors.png "Sds2000x Connectors"){ .glightbox data-gallery="siglent-sds2000x-series" }
<span class="caption">Sds2000x Connectors</span>

[![Sds2000x Logic Probe 1](./img/Sds2000x-logic-probe-1.png)](./img/Sds2000x-logic-probe-1.png "Sds2000x Logic Probe 1"){ .glightbox data-gallery="siglent-sds2000x-series" }
<span class="caption">Sds2000x Logic Probe 1</span>

[![Sds2000x Analog Probe](./img/Sds2000x-analog-probe.png)](./img/Sds2000x-analog-probe.png "Sds2000x Analog Probe"){ .glightbox data-gallery="siglent-sds2000x-series" }
<span class="caption">Sds2000x Analog Probe</span>

[![Sds2000x Logic Probe 2](./img/Sds2000x-logic-probe-2.png)](./img/Sds2000x-logic-probe-2.png "Sds2000x Logic Probe 2"){ .glightbox data-gallery="siglent-sds2000x-series" }
<span class="caption">Sds2000x Logic Probe 2</span>

[![Sds2304x Front](./img/Sds2304x-front.png)](./img/Sds2304x-front.png "Sds2304x Front"){ .glightbox data-gallery="siglent-sds2000x-series" }
<span class="caption">Sds2304x Front</span>

</div>
## Protocol

All devices support USB (USBTMC) and LAN (VXI-11) by default, and are implementing the IEEE488.2 protocol.

## Resources
- [SDS2000X Series Oscilloscopes - Data Sheet](http://www.siglentamerica.com/USA_website_2014/Documents/DataSheet/SDS2000X_Datasheet_DS0102X-E01B.pdf)
- [SIGLENT_Digital Oscilloscopes Remote Control Manual](http://www.siglentamerica.com/USA_website_2014/Documents/Program_Material/SIGLENT_Digital_Oscilloscopes_Remote%20Control%20Manual.pdf)

