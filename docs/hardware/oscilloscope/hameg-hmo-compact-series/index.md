---
title: Hameg HMO compact series
---

# Hameg HMO compact series

<div class="infobox" markdown>

![Hameg HMO compact series](./img/Hameg_HMO2024.jpg){ .infobox-image }

### Hameg HMO compact series

| | |
|---|---|
| **Status** | supported |
| **Source code** | [hameg-hmo](https://github.com/OpenTraceLab/OpenTraceCapture/tree/main/src/hardware/hameg-hmo) |
| **Channels** | 2-4 analog, 8 digital |
| **Samplerate** | 2GSa/s (interleaved), 1GSA/s (non interleaved) |
| **Analog bandwidth** | 70-200MHz (depending on model) |
| **Vertical resolution** | 8bits (HiRes up to 10bits) |
| **Triggers** | pulse width, slope, video, pattern, serial bus (optional) |
| **Input impedance** | 1MΩ‖14pF 200Vp CAT I, 50Ω 5V RMS (model dependent) |
| **Memory** | 2Mpts (mode/ch-dependent) |
| **Display** | 6.5" VGA (640x480), 256 colors |
| **Connectivity** | USB host/device, RS232, ethernet (optional), GPIB (optional) |
| **Features** | math: + / — / x / FFT, statistics, vertical sensitivity: 1mV/div - 10V/div |
| **Website** | [hameg.com](http://www.hameg.com/0.616.0.html) |

</div>

The **Hameg HMO compact series** are 70-200MHz, 2GSa/s, 2-4 analog channel and 8 digital channel digital storage oscilloscopes.

All models support different extension modules which provide different connectivity.

Most models come with a [HO720](https://sigrok.org/wiki/Hameg_HO720) (RS232, USB) module, other modules like the [HO730](https://sigrok.org/wiki/Hameg_HO730) (USB, ethernet) and the [HO740](/w/index.php?title=Hameg_HO740&action=edit&redlink=1) (GPIB) are available optionally.

All models come with analog probes (specific probe might depend on the scope's capabilities).

Digital probes are optional extra, see [HO3508](https://sigrok.org/wiki/Hameg_HO3508).

## Devices
| Model | Bandwidth | Analog Channels | Digital Channels |
|---|---|---|---|
| HMO722 | 70MHz | 2 | 8 |
| HMO1022 | 100MHz | 2 | 8 |
| HMO1522 | 150MHz | 2 | 8 |
| HMO2022 | 200MHz | 2 | 8 |
| HMO724 | 70MHz | 4 | 8 |
| HMO1024 | 100MHz | 4 | 8 |
| [ HMO1524](https://sigrok.org/wiki/Hameg_HMO1524) | 150MHz | 4 | 8 |
| [ HMO2024](https://sigrok.org/wiki/Hameg_HMO2024) | 200MHz | 4 | 8 |
| [ HMO2524](https://sigrok.org/wiki/Hameg_HMO2524) | 250MHz | 4 | 16 |

Note that it's uncertain whether HMO2524 strictly belongs to the "HMO compact" series, as it has features that are unique to the HMO3000 series, and comes in a different case. Nevertheless, the [HMO2524](https://sigrok.org/wiki/Hameg_HMO2524) is supported by libsigrok's **hameg-hmo** driver.

## Protocol

All the devices use same [SCPI](https://sigrok.org/wiki/IEEE-488) protocol.

The serial parameters are configurable on the device, the standard settings are: 115200 baud, 8n1, no handshake.

Some models optionally support USBTMC.

## Resources
- [Hameg - resource page](http://www.hameg.com/manuals.0.html?no_cache=1)
- [Hameg HMO - programming guide](http://midas.herts.ac.uk/helpsheets/hameg_scpi_hmo72.pdf)
- [R&S HMO Compact Series Digital Oscilloscope - SCPI Programmer's Manual](https://cdn.rohde-schwarz.com/pws/dl_downloads/dl_common_library/dl_manuals/gb_1/h/hmo72x_202x/HMO72x_202x_SCPI_ProgrammersManual_en_02.pdf) (Version 02 as of 2015, 196 pages, refers to "72x_202x")
- [Hameg HMO compact series - datasheet](http://www.soselectronic.cz/a_info/resource/l/hameg/HAMEG_Addendum_HMO_EN%5B1%5D.pdf)

## Photos

<div class="photo-grid" markdown>

[![Hameg Hmo2024](./img/Hameg_HMO2024.jpg)](./img/Hameg_HMO2024.png "Hameg Hmo2024"){ .glightbox data-gallery="hameg-hmo-compact-series" }
<span class="caption">Hameg Hmo2024</span>

</div>
