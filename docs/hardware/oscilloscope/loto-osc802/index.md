---
title: Loto OSC802
---

# Loto OSC802

<div class="infobox" markdown>

![Loto OSC802](./img/Loto_OSC802_02.jpg){ .infobox-image }

### Loto OSC802

| | |
|---|---|
| **Status** | planned |
| **Channels** | 1 |
| **Samplerate** | 1ch @ 80MHz |
| **Analog bandwidth** | 20MHz |
| **Triggers** | Hardware |
| **Memory** | 64K/channel |
| **Connectivity** | USB |
| **Website** | [rockemb.com](http://www.rockemb.com/index.php?m=content&amp;c=index&amp;a=show&amp;catid=96&amp;id=105) |

</div>

The **Loto OSC802** is a USB-based, 2-channel oscilloscope with an analog bandwidth of 20MHz and 80MS/s sampling rate.

See [Loto OSC802/Info](/w/index.php?title=Loto_OSC802/Info&action=edit&redlink=1) for more details (such as **lsusb -v** output) about the device.

See [Loto OSCxxx series](https://sigrok.org/wiki/Loto_OSCxxx_series) for information common to all devices in this series.

## Hardware
- **Main chip**: [Altera MAX II EPM240](https://www.intel.com/content/www/us/en/products/programmable/cpld/max-ii.html) ([pin info](https://www.intel.com/content/dam/www/programmable/us/en/pdfs/literature/dp/max2/epm240.pdf) [device handbook](https://www.intel.com/content/dam/www/programmable/us/en/pdfs/literature/hb/max2/max2_mii5v1.pdf))
- **8-Bit, 80 MSPS Dual A/D Converter**: Analog Devices AD9288 ([datasheet](https://www.analog.com/media/en/technical-documentation/data-sheets/ad9288.pdf))
- **Main oscillator**: 80MHz 80.000 YX NH
- **USB**: Cypress CY7C68013A-100AXC (FX2LP)
- **64K x 16 high-speed CMOS static RAM**: 2x [ISSI IS61LV6416-8TI](http://www.issi.com/products-asynchronous-sram.htm) ([datasheet](http://www.issi.com/WW/pdf/61LV6416_L.pdf))
- **I2C EEPROM**: Microchip 24LC02BI (for the USB VID/PID of the Cypress FX2LP)
- **Main power supply**: [TESLA A0505S-1W-DC isolation power chip 5V ](https://www.chinahao.com/product/559725327304/)

**Input stage (per channel):**

- **Analog Multiplexer/Demultiplexer**: [CD4052](http://www.ti.com/lit/ds/symlink/cd4051b.pdf)

## Photos

<div class="photo-grid" markdown>

[![Loto Osc802 02](./img/Loto_OSC802_02.jpg)](./img/Loto_OSC802_02.jpg "Loto Osc802 02"){ .glightbox data-gallery="loto-osc802" }
<span class="caption">Loto Osc802 02</span>

[![Loto Osc802 03](./img/Loto_OSC802_03.jpg)](./img/Loto_OSC802_03.jpg "Loto Osc802 03"){ .glightbox data-gallery="loto-osc802" }
<span class="caption">Loto Osc802 03</span>

[![Loto Osc802](./img/Loto_OSC802.jpg)](./img/Loto_OSC802.jpg "Loto Osc802"){ .glightbox data-gallery="loto-osc802" }
<span class="caption">Loto Osc802</span>

[![Loto Osc802 04](./img/Loto_OSC802_04.jpg)](./img/Loto_OSC802_04.jpg "Loto Osc802 04"){ .glightbox data-gallery="loto-osc802" }
<span class="caption">Loto Osc802 04</span>

[![Loto Osc802 01](./img/Loto_OSC802_01.jpg)](./img/Loto_OSC802_01.jpg "Loto Osc802 01"){ .glightbox data-gallery="loto-osc802" }
<span class="caption">Loto Osc802 01</span>

</div>
## Protocol

See [Loto OSCxxx series#Protocol](https://sigrok.org/wiki/Loto_OSCxxx_series#Protocol).

## Resources
- [Brochure](http://www.rockemb.com/uploadfile/2019/0220/20190220114957785.pdf)
- [Vendor website](http://www.rockemb.com/index.php?m=content&c=index&a=show&catid=96&id=105)

