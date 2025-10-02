---
title: Hantek 6254BD
---

# Hantek 6254BD

<div class="infobox" markdown>

![Hantek 6254BD](./img/Hantek_6254bd_device_bottom.jpg){ .infobox-image }

### Hantek 6254BD

| | |
|---|---|
| **Status** | planned |
| **Channels** | 4 |
| **Samplerate** | 1GSa/s |
| **Analog bandwidth** | 250MHz |
| **Vertical resolution** | 8bit |
| **Triggers** | edge, pulse, video, alternative |
| **Input impedance** | 1MΩ‖25pF |
| **Memory** | 64K |
| **Display** | none |
| **Connectivity** | USB |
| **Website** | [hantek.com](http://www.hantek.com/en/ProductDetail_2_10164.html) |

</div>

The **Hantek 6254BD** is a USB-based, 4-channel oscilloscope with an analog bandwidth of 250MHz and 1GSa/s sampling rate.

See [Hantek 6254BD/Info](https://sigrok.org/wiki/Hantek_6254BD/Info) for more details (such as **lsusb -v** output) about the device.

## Hardware
- **FPGA**: [Xilinix Spartan-6 XC6SLX16](https://www.xilinx.com/products/silicon-devices/fpga/spartan-6.html#tabAnchor-productTable) ([datasheet](https://www.xilinx.com/support/documentation/data_sheets/ds160.pdf))
- **SPI flash**: [Macronix MX25L4006E](http://www.macronix.com/en-us/products/NOR-Flash/Serial-NOR-Flash/Pages/spec.aspx?p=MX25L4006E) ([datasheet](http://www.macronix.com/Lists/Datasheet/Attachments/6705/MX25L4006E,%203V,%204Mb,%20v1.6.pdf))
- **8-bit 1GSa/s ADC**: [Analog Devices HMCAD1511](http://www.analog.com/en/products/analog-to-digital-converters/standard-adc/high-speed-ad-10msps/hmcad1511.html) ([datasheet](http://www.analog.com/media/en/technical-documentation/data-sheets/hmcad1511.pdf))
- **Integrated synthesizer and VCO**: [Analog Devices ADF4360-7](http://www.analog.com/en/products/clock-and-timing/phase-locked-loop/phase-locked-loop-w-integrated-vco/adf4360-7.html#product-overview) ([datasheet](http://www.analog.com/media/en/technical-documentation/data-sheets/ADF4360-7.pdf))
- **12-bit 165MSa/s DAC**: [Texas Instruments DAC902E](http://www.ti.com/product/DAC902) ([datasheet](http://www.ti.com/general/docs/lit/getliterature.tsp?genericPartNumber=dac902&fileType=pdf))
- **USB controller**: [Cypress CY7C68013A (FX2)](http://www.cypress.com/products/ez-usb-fx2lp) ([datasheet](http://www.cypress.com/file/138911/download))
- **6Kbit I²C EEPROM**: [Microchip 24LC64](https://www.microchip.com/wwwproducts/en/24LC64)
- **3-State shift register**: [ON Semiconductor MC74HC595A](http://www.onsemi.com/PowerSolutions/product.do?id=MC74HC595A) ([datasheet](http://www.onsemi.com/pub/Collateral/MC74HC595A-D.PDF))

## Photos

<div class="photo-grid" markdown>

[![Hantek 6254bd Device Bottom](./img/Hantek_6254bd_device_bottom.jpg)](./img/Hantek_6254bd_device_bottom.jpg "Hantek 6254bd Device Bottom"){ .glightbox data-gallery="hantek-6254bd" }
<span class="caption">Hantek 6254bd Device Bottom</span>

[![Hantek 6254bd Mugshot](./img/Hantek_6254bd_mugshot.jpg)](./img/Hantek_6254bd_mugshot.png "Hantek 6254bd Mugshot"){ .glightbox data-gallery="hantek-6254bd" }
<span class="caption">Hantek 6254bd Mugshot</span>

[![Hantek 6254bd Device Top](./img/Hantek_6254bd_device_top.jpg)](./img/Hantek_6254bd_device_top.jpg "Hantek 6254bd Device Top"){ .glightbox data-gallery="hantek-6254bd" }
<span class="caption">Hantek 6254bd Device Top</span>

[![Hantek 6254bd Bottom](./img/Hantek_6254bd_bottom.jpg)](./img/Hantek_6254bd_bottom.jpg "Hantek 6254bd Bottom"){ .glightbox data-gallery="hantek-6254bd" }
<span class="caption">Hantek 6254bd Bottom</span>

[![Hantek 6254bd Top](./img/Hantek_6254bd_top.jpg)](./img/Hantek_6254bd_top.jpg "Hantek 6254bd Top"){ .glightbox data-gallery="hantek-6254bd" }
<span class="caption">Hantek 6254bd Top</span>

</div>
## Resources
- [Manual](http://www.hantek.com/down.aspx?url=http%3a%2f%2fwww.hantek.com%2fProduct%2fHantek6000BX%2fHT6004BX_Manual.pdf)
- [Vendor software](http://www.hantek.com/down.aspx?url=http%3a%2f%2fwww.hantek.com%2fProduct%2fHantek6000BX%2fHT6004BX_Software.zip)
- [Vendor driver](http://www.hantek.com/down.aspx?url=http%3a%2f%2fwww.hantek.com%2fProduct%2fHantek6000BX%2fHT6004BX_Driver.zip)
- [Vendor SDK](http://www.hantek.com/down.aspx?url=http%3a%2f%2fwww.hantek.com%2fProduct%2fHantek6000BX%2fHT6004BX_SDK.zip)
- [eevblog.com: Hantek 6254BD 250MHz 1GSa/s PC/USB DSO](http://www.eevblog.com/forum/testgear/hantek-6254bd-250mhz-1gsas-pcusb-dso/)
- [github libhantek6xx4](https://github.com/pvachon/libhantek6xx4), [github pyhantek](https://github.com/danielkucera/pyhantek), [github hantek6004](https://github.com/hackhantek/hantek6004)

