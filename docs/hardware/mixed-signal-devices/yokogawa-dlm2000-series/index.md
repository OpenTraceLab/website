---
title: Yokogawa DLM2000 series
---

# Yokogawa DLM2000 series

<div class="infobox" markdown>

![Yokogawa DLM2000 series](./img/Yokogawa_DLM2000_front.jpg){ .infobox-image }

### Yokogawa DLM2000 series

| | |
|---|---|
| **Status** | supported |
| **Source code** | [yokogawa-dlm](https://github.com/OpenTraceLab/OpenTraceCapture/tree/main/src/hardware/yokogawa-dlm) |
| **Channels** | 2 or 4 |
| **Samplerate** | 2.5GSa/s (2chs interleaved), 1.25GSa/s |
| **Analog bandwidth** | 200-500MHz (depending on model) |
| **Vertical resolution** | 8bits |
| **Input impedance** | 1MΩ‖20pF 150V RMS CAT I or 50Ω 5V RMS |
| **Memory** | 6.25 to 250Mpts (model/mode-dependent) |
| **Display** | 8.4" 1024x768 |
| **Connectivity** | USB host/device, Ethernet (optional), Trigger in/out, GO/NOGO, VGA out |
| **Website** | [yokogawa.com](http://tmi.yokogawa.com/us/products/oscilloscopes/digital-and-mixed-signal-oscilloscopes/dlm2000-mso-series/) |

</div>

The [Yokogawa DLM2000 series](http://tmi.yokogawa.com/us/products/oscilloscopes/digital-and-mixed-signal-oscilloscopes/dlm2000-mso-series/) are 2- or 4-channel oscilloscopes with an analog bandwidth of 200-500MHz and 2.5GS/s sampling rate. See [Yokogawa DLM2000 series/Info](https://sigrok.org/wiki/Yokogawa_DLM2000_series/Info) for more details (such as **lsusb -v** output) about the device.

Due to Yokogawa's focus on the controls industry, their oscilloscopes offer extensive analysis and reporting features.

## Devices
| Model | Bandwidth | Channels |
|---|---|---|
| DLM2022 | 200MHz | 2 |
| DLM2032 | 350MHz | 2 |
| DLM2052 | 500MHz | 2 |
| DLM2024 | 200MHz | 4 analog / 3 analog+8 digital |
| DLM2034 | 350MHz | 4 analog / 3 analog+8 digital |
| DLM2054 | 500MHz | 4 analog / 3 analog+8 digital |

## Photos

<div class="photo-grid" markdown>

[![Yokogawa Dlm2000 Front](./img/Yokogawa_DLM2000_front.jpg)](./img/Yokogawa_DLM2000_front.png "Yokogawa Dlm2000 Front"){ .glightbox data-gallery="yokogawa-dlm2000-series" }
<span class="caption">Yokogawa Dlm2000 Front</span>

[![Yokogawa Dlm2000 Back](./img/Yokogawa_DLM2000_back.jpg)](./img/Yokogawa_DLM2000_back.png "Yokogawa Dlm2000 Back"){ .glightbox data-gallery="yokogawa-dlm2000-series" }
<span class="caption">Yokogawa Dlm2000 Back</span>

[![Yokogawa Pbl250](./img/Yokogawa_PBL250.jpg)](./img/Yokogawa_PBL250.png "Yokogawa Pbl250"){ .glightbox data-gallery="yokogawa-dlm2000-series" }
<span class="caption">Yokogawa Pbl250</span>

</div>
## Protocol

The device uses [GPIB](https://sigrok.org/wiki/GPIB), [USBTMC](https://sigrok.org/wiki/USBTMC) or LXI via its ethernet port for communication with a host PC. The protocol is based on SCPI commands.

## Resources
- [EEVblog forums: Some DLM2000 discussion](http://www.eevblog.com/forum/reviews/yokogawa-dlm-2000-have-not-been-tried-it-is-a-200-mhz-1-25-gsampless/)
- [EEVblog forums: Review of the DLM2024](http://www.eevblog.com/forum/chat/yokogawa-dlm2024-oscillocope-review/)
- [DLM2000 product sheet](https://www.yokogawa.com/pdf/provide/E/GW/Bulletin/0000022831/0/BU7101-00E.pdf)
- [DLM2000 communication interface manual](https://www.yokogawa.com/pdf/provide/E/GW/IM/0000022842/0/IM710105-17E.pdf)

