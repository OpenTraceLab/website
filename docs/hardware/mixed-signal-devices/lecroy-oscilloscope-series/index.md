---
title: LeCroy oscilloscope series
---

# LeCroy oscilloscope series

<div class="infobox" markdown>

![LeCroy oscilloscope series](./img/LeCroy_WaveSurfer_24Xs-A_front.png){ .infobox-image }

### LeCroy oscilloscope series

| | |
|---|---|
| **Status** | supported |
| **Source code** | [lecroy-xstream](https://github.com/OpenTraceLab/OpenTraceCapture/tree/main/src/hardware/lecroy-xstream) |
| **Website** | [Teledyne LeCroy](http://teledynelecroy.com/oscilloscope/) |

</div>

LeCroy sells everything from entry-level to very high-end oscilloscopes, making use of own designs as well as contract manufacturers such as Iwatsu and Siglent. One feature that's common to all of those models is the support for LeCroy's waveform template, a data format used to retrieve waveform data using GPIB/SCPI commands. For this reason, this page isn't about a single oscilloscope in particular but all scopes belonging to the X-Stream family.

## Devices

Virtually all devices listed on [http://teledynelecroy.com/oscilloscope/](http://teledynelecroy.com/oscilloscope/) should work (except for the 8-channel, 10-bit and 12-bit models).

| Family | Manufacturer | OS | Bandwidth | Connectivity | Tested? |
|---|---|---|---|---|---|
| WaveAce 1000 | Atten | ? | 40 - 100 MHz | USB | No |
| WaveAce 2000 | Siglent | ? | 70 - 300 MHz | USB | No |
| WaveJet 300 | Iwatsu | ? | 350 - 500 MHz | USB | No |
| WaveSurfer 10 | ? | Windows | 1 GHz | LAN | No |
| WaveSurfer 400 | Iwatsu | Windows | 200 - 500 MHz | LAN | No |
| WaveSurfer 3000 | Siglent | Windows Embedded | 200 - 750 MHz | USB, LAN, GPIB | No |
| WaveSurfer (M)Xs | Iwatsu | Windows XP | 200 MHz - 1 GHz | LAN | Yes |
| WaveRunner 6 Zi | ? | Windows 7 | 400 MHz - 4 GHz | USB, LAN | No |
| WaveRunner 6000 | Iwatsu | Windows 2000 | 350 MHz - 2 GHz | LAN | No |
| WaveRunner 8000 | ? | Windows | 500 MHz - 4 GHz | LAN | No |
| WaveRunner (M)Xi | Iwatsu | Windows XP | 400 MHz - 2 GHz | LAN | Yes |

The digital channels aren't supported yet.

## Protocol

The protocol is based on SCPI commands and there is a USB-GPIB converter available which you can use on all Windows-based models.

## Resources
- [WaveSurfer 3000 family remote control manual](http://teledynelecroy.com/doc/docview.aspx?id=9905)
- [WaveAce family remote control manual](http://cdn.teledynelecroy.com/files/manuals/wa1k2k_remote-control_manual.pdf)

## Photos

<div class="photo-grid" markdown>

[![Lecroy Wavesurfer 24xs A Front](./img/LeCroy_WaveSurfer_24Xs-A_front.png)](./img/LeCroy_WaveSurfer_24Xs-A_front.png "Lecroy Wavesurfer 24xs A Front"){ .glightbox data-gallery="lecroy-oscilloscope-series" }
<span class="caption">Lecroy Wavesurfer 24xs A Front</span>

</div>
