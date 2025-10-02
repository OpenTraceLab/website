---
title: Rigol DS1000Z series
---

# Rigol DS1000Z series

<div class="infobox" markdown>

![Rigol DS1000Z series](./img/Rigol_DS1074Z_front.jpg){ .infobox-image }

### Rigol DS1000Z series

| | |
|---|---|
| **Status** | supported |
| **Channels** | 4 |
| **Samplerate** | 1GSa/s (1ch), 500MSa/s (2ch), 250MSa/s (3 or 4 ch) |
| **Analog bandwidth** | 50-100MHz (depending on model) |
| **Vertical resolution** | 8bits |
| **Triggers** | edge, pulse, runt, windows, nth edge, slope, video, pattern, delay, timeout, duration, setup/hold, RS232/UART, I²C, SPI |
| **Input impedance** | 1MΩ‖13pF 300V RMS CAT I |
| **Memory** | 12/24Mpts (mode/ch-dependent) |
| **Display** | 7 Inch WVGA (800x480) 160,000 colours |
| **Connectivity** | USB host/device, ethernet (LXI), trigger out, pass/fail out |
| **Features** | math: +, —, x, /, FFT, vertical sensitivity: 1 mV/div to 10 V/div |
| **Website** | [rigolna.com](http://www.rigolna.com/products/digital-oscilloscopes/ds1000Z/) |

</div>

The [Rigol DS1000Z Series](http://www.rigolna.com/products/digital-oscilloscopes/ds1000Z/) are 4-channel oscilloscopes with an analog bandwidth of 50-100MHz and 1GSa/s maximum sampling rate.

## Devices
| Model | Bandwidth |
|---|---|
| [Rigol DS1054Z](https://sigrok.org/wiki/Rigol_DS1054Z) | 50MHz |
| [Rigol DS1074Z](https://sigrok.org/wiki/Rigol_DS1074Z) | 70MHz |
| DS1104Z | 100MHz |

## Protocol

The device uses [USBTMC](https://sigrok.org/wiki/USBTMC) or LXI via its Ethernet port for communication with a host PC. The protocol is based on SCPI commands.

If you're getting persistent command errors when attempting to capture via Ethernet (try running sigrok-cli with `-l 5`), make sure your oscilloscope runs at least firmware version 00.04.03.02.

## Resources
- [Batronix: User manual](http://www.batronix.com/pdf/Rigol/UserGuide/DS1000Z_UserGuide_EN.pdf)
- [Batronix: Programming guide](http://www.batronix.com/pdf/Rigol/ProgrammingGuide/MSO1000Z_DS1000Z_ProgrammingGuide_EN.pdf)
- [EEVBlog: High resolution images of DS1054Z](http://www.flickr.com/photos/eevblog/sets/72157646442125864/)

## Photos

<div class="photo-grid" markdown>

[![Rigol Ds1074z Front](./img/Rigol_DS1074Z_front.jpg)](./img/Rigol_DS1074Z_front.png "Rigol Ds1074z Front"){ .glightbox data-gallery="rigol-ds1000z-series" }
<span class="caption">Rigol Ds1074z Front</span>

</div>
