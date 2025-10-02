---
title: XMOS XTAG-2
---

# XMOS XTAG-2

<div class="infobox" markdown>

![XMOS XTAG-2](./img/Xmos_xtag2.png){ .infobox-image }

### XMOS XTAG-2

| | |
|---|---|
| **Status** | planned |
| **Channels** | ???? |
| **Samplerate** | 50MHz @ 2ch, 16MHz @ 7ch |
| **Samplerate (state)** | ? |
| **Triggers** | ? |
| **Min/max voltage** | ? |
| **Threshold voltage** | ? |
| **Memory** | ? |
| **Compression** | ? |
| **Website** | [xmos.com](http://www.xmos.com/products/xkits/debug) |

</div>

The **XMOS XTAG-2** is a USB based,&#160;????-channel logic analyzer with up to 50MHz sampling rate.

The XTAG-2 is actually a debug/eval board for XMOS ICs, but it can be used as a logic analyzer with a [firmware written by Henk Muller](http://www.mail-archive.com/sigrok-devel@lists.sourceforge.net/msg00094.html).

See [XMOS XTAG-2/Info](https://sigrok.org/wiki/XMOS_XTAG-2/Info) for more details (such as **lsusb -vvv** output) about the device.

## Hardware

The main chip is an XMOS XS1-L1 [XS1-L01A-LQ64 Datasheet](https://www.xmos.com/en/download/public/XS1-L01A-LQ64-Datasheet%28X1135E%29.pdf).
In the above picture, the 7-pin header markings are barely unreadable, but that's the jtag port for the xmos chip. From right to left: TDO, TDI, TCK, TMS, TRST#, RST# and GND.

The secondary chip is an [SMSC HS Usb 2.0 transceiver](http://ww1.microchip.com/downloads/en/DeviceDoc/3310.pdf).

## Photos

<div class="photo-grid" markdown>

[![Xmos Xtag2](./img/Xmos_xtag2.png)](./img/Xmos_xtag2.png "Xmos Xtag2"){ .glightbox data-gallery="xmos-xtag-2" }
<span class="caption">Xmos Xtag2</span>

[![Xtag 2 Front](./img/Xtag-2_front.png)](./img/Xtag-2_front.png "Xtag 2 Front"){ .glightbox data-gallery="xmos-xtag-2" }
<span class="caption">Xtag 2 Front</span>

</div>
## Protocol

TODO.

## Resources
- [XMOS project page of the logic analyzer firmware](http://github.xcore.com/repo_index/sw_logic_analyzer_readme.html)
- [sw_logic_analyzer github repo](https://github.com/xcore/sw_logic_analyzer)
- [XTAG-2 quickstart guide](https://www.xmos.com/download/public/XTAG-2-Quick-Start-Guide(1.1).pdf)
- [XTAG-2 hardware manual](https://www.xmos.com/download/public/XTAG-2-Hardware-Manual(1.0).pdf)
- [XTAG-2 loader (binary)](https://www.xmos.com/download/public/XTAG-2-Loader-%28Binary%29%280.02%29.xe)
- [XTAG-2 design files](http://www.xmos.com/published/xtag-2-design-files)

