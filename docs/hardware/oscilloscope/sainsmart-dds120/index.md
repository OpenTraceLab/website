---
title: SainSmart DDS120
---

# SainSmart DDS120

<div class="infobox" markdown>

![SainSmart DDS120](./img/Saintsmart_dds120_microchip_24lc64i.jpg){ .infobox-image }

### SainSmart DDS120

| | |
|---|---|
| **Status** | supported |
| **Source code** | [hantek-6xxx](https://github.com/OpenTraceLab/OpenTraceCapture/tree/main/src/hardware/hantek-6xxx) |
| **Channels** | 2 |
| **Samplerate** | 50MHz |
| **Analog bandwidth** | 20MHz |
| **Vertical resolution** | 8bit |
| **Triggers** | none (SW-only) |
| **Input impedance** | 1MΩ‖25pF |
| **Memory** | none |
| **Display** | none |
| **Connectivity** | USB |
| **Website** | [sainsmart.com](http://www.sainsmart.com/sainsmart-dds-120-20m-50m-s-virtual-oscilloscope-silver.html) |

</div>

The **SainSmart DDS120** is a USB-based, 2-channel oscilloscope with an analog bandwidth of 20MS/s and 50MS/s sampling rate.

This device appears to be a rebadge of the [Rocktech BM102](https://sigrok.org/wiki/Rocktech_BM102) (or vice versa). The [lsusb](https://sigrok.org/wiki/SainSmart_DDS120/Info) is exactly the same, the PCB is exactly the same (both have a "656517" and "102LJT1402" silkscreen), and the components used appear to be the same as well.

The device was apparently [created by someone named "buudai"](https://translate.google.de/translate?sl=auto&tl=en&js=y&prev=_t&hl=en&ie=UTF-8&u=https%3A%2F%2Fweb.archive.org%2Fweb%2F20140520231246%2Fhttp%3A%2F%2Fbbs.21ic.com%2Ficview-350047-1-1.html&edit-text=&act=url) in 2012 (also reflected in the [lsusb](https://sigrok.org/wiki/SainSmart_DDS120/Info) and in the former [buudai.com](https://web.archive.org/web/20130403082149/http://www.buudai.com/) website).

See [SainSmart DDS120/Info](https://sigrok.org/wiki/SainSmart_DDS120/Info) for more details (such as **lsusb -v** output) about the device.

## Hardware
- **USB**: [Cypress CY7C68013A-100AXC](http://www.cypress.com/documentation/datasheets/cy7c68013a-cy7c68014a-cy7c68015a-cy7c68016a-ez-usb-fx2lp-usb) (FX2LP) ([datasheet](http://www.cypress.com/file/138911/download))
- **64-kbyte I²C EEPROM**: [Microchip 24LC64I](http://www.microchip.com/wwwproducts/Devices.aspx?dDocName=en010831) ([datasheet](http://ww1.microchip.com/downloads/en/DeviceDoc/21189f.pdf))
- **Crystal**: 24MHz
- **145 MHz FastFET Opamps**: [AD8065ART-R2](http://www.analog.com/en/products/amplifiers/operational-amplifiers/jfet-input-amplifiers/ad8065.html#product-overview): ([datasheet](http://www.analog.com/static/imported-files/data_sheets/AD8065_8066.pdf))

**Or in newer hardware:**

- **Dual 8bit, 100MSPS ADC**: [MXTronix MXT2088](https://translate.google.com/translate?hl=en&sl=zh-CN&tl=en&u=http%3A%2F%2Fwww.mxtronics.com%2Fn107%2Fn124%2Fn181%2Fn184%2Fc692%2Fcontent.html) ([datasheet](http://www.mxtronics.com/n107/n124/n181/n184/c692/attr/2630.pdf))
- **145 MHz FastFET Opamps**: [AD8065](http://www.analog.com/en/products/amplifiers/operational-amplifiers/jfet-input-amplifiers/ad8065.html#product-overview): ([datasheet](http://www.analog.com/static/imported-files/data_sheets/AD8065_8066.pdf))
- 4x **CMOS differential 4-channel analog mux/demux with logic-level conversion**: [Texas Instruments CD4052B(M)](http://www.ti.com/product/cd4052b/description) ([datasheet](http://www.ti.com/lit/gpn/cd4052b))

## Photos

<div class="photo-grid" markdown>

[![Saintsmart Dds120 Microchip 24lc64i](./img/Saintsmart_dds120_microchip_24lc64i.jpg)](./img/Saintsmart_dds120_microchip_24lc64i.jpg "Saintsmart Dds120 Microchip 24lc64i"){ .glightbox data-gallery="sainsmart-dds120" }
<span class="caption">Saintsmart Dds120 Microchip 24lc64i</span>

[![Sainsmart Dds120 Back 1](./img/Sainsmart_dds120_back_1.jpg)](./img/Sainsmart_dds120_back_1.jpg "Sainsmart Dds120 Back 1"){ .glightbox data-gallery="sainsmart-dds120" }
<span class="caption">Sainsmart Dds120 Back 1</span>

[![Sainsmart Dds120 Front 3](./img/Sainsmart_dds120_front_3.jpg)](./img/Sainsmart_dds120_front_3.jpg "Sainsmart Dds120 Front 3"){ .glightbox data-gallery="sainsmart-dds120" }
<span class="caption">Sainsmart Dds120 Front 3</span>

[![Dds120 Top 20141024 0540p](./img/DDS120_Top_20141024_0540p.jpg)](./img/DDS120_Top_20141024_0540p.jpg "Dds120 Top 20141024 0540p"){ .glightbox data-gallery="sainsmart-dds120" }
<span class="caption">Dds120 Top 20141024 0540p</span>

[![Saintsmart Dds120 Package Contents](./img/Saintsmart_dds120_package_contents.jpg)](./img/Saintsmart_dds120_package_contents.jpg "Saintsmart Dds120 Package Contents"){ .glightbox data-gallery="sainsmart-dds120" }
<span class="caption">Saintsmart Dds120 Package Contents</span>

[![Saintsmart Dds120 Mxt2088](./img/Saintsmart_dds120_mxt2088.jpg)](./img/Saintsmart_dds120_mxt2088.jpg "Saintsmart Dds120 Mxt2088"){ .glightbox data-gallery="sainsmart-dds120" }
<span class="caption">Saintsmart Dds120 Mxt2088</span>

[![Saintsmart Dds120 Sticker](./img/Saintsmart_dds120_sticker.jpg)](./img/Saintsmart_dds120_sticker.jpg "Saintsmart Dds120 Sticker"){ .glightbox data-gallery="sainsmart-dds120" }
<span class="caption">Saintsmart Dds120 Sticker</span>

[![Sainsmart Dds120 Front 5](./img/Sainsmart_dds120_front_5.jpg)](./img/Sainsmart_dds120_front_5.jpg "Sainsmart Dds120 Front 5"){ .glightbox data-gallery="sainsmart-dds120" }
<span class="caption">Sainsmart Dds120 Front 5</span>

[![Saintsmart Dds120 Pcb Bottom](./img/Saintsmart_dds120_pcb_bottom.jpg)](./img/Saintsmart_dds120_pcb_bottom.jpg "Saintsmart Dds120 Pcb Bottom"){ .glightbox data-gallery="sainsmart-dds120" }
<span class="caption">Saintsmart Dds120 Pcb Bottom</span>

[![Sainsmart Dds120 Box 2](./img/Sainsmart_dds120_box_2.jpg)](./img/Sainsmart_dds120_box_2.jpg "Sainsmart Dds120 Box 2"){ .glightbox data-gallery="sainsmart-dds120" }
<span class="caption">Sainsmart Dds120 Box 2</span>

[![Sainsmart Dds120 Back 2](./img/Sainsmart_dds120_back_2.jpg)](./img/Sainsmart_dds120_back_2.jpg "Sainsmart Dds120 Back 2"){ .glightbox data-gallery="sainsmart-dds120" }
<span class="caption">Sainsmart Dds120 Back 2</span>

[![Saintsmart Dds120 Connectors](./img/Saintsmart_dds120_connectors.jpg)](./img/Saintsmart_dds120_connectors.jpg "Saintsmart Dds120 Connectors"){ .glightbox data-gallery="sainsmart-dds120" }
<span class="caption">Saintsmart Dds120 Connectors</span>

[![Sainsmart Dds120 Front 1](./img/Sainsmart_dds120_front_1.jpg)](./img/Sainsmart_dds120_front_1.jpg "Sainsmart Dds120 Front 1"){ .glightbox data-gallery="sainsmart-dds120" }
<span class="caption">Sainsmart Dds120 Front 1</span>

[![Saintsmart Dds120 Device Top](./img/Saintsmart_dds120_device_top.jpg)](./img/Saintsmart_dds120_device_top.jpg "Saintsmart Dds120 Device Top"){ .glightbox data-gallery="sainsmart-dds120" }
<span class="caption">Saintsmart Dds120 Device Top</span>

[![Saintsmart Dds120 Usb](./img/Saintsmart_dds120_usb.jpg)](./img/Saintsmart_dds120_usb.jpg "Saintsmart Dds120 Usb"){ .glightbox data-gallery="sainsmart-dds120" }
<span class="caption">Saintsmart Dds120 Usb</span>

[![Saintsmart Dds120 Pcb Top](./img/Saintsmart_dds120_pcb_top.jpg)](./img/Saintsmart_dds120_pcb_top.jpg "Saintsmart Dds120 Pcb Top"){ .glightbox data-gallery="sainsmart-dds120" }
<span class="caption">Saintsmart Dds120 Pcb Top</span>

[![Saintsmart Dds120 Nais 210eh 347](./img/Saintsmart_dds120_nais_210eh_347.jpg)](./img/Saintsmart_dds120_nais_210eh_347.jpg "Saintsmart Dds120 Nais 210eh 347"){ .glightbox data-gallery="sainsmart-dds120" }
<span class="caption">Saintsmart Dds120 Nais 210eh 347</span>

[![Saintsmart Dds120 Device Bottom](./img/Saintsmart_dds120_device_bottom.jpg)](./img/Saintsmart_dds120_device_bottom.jpg "Saintsmart Dds120 Device Bottom"){ .glightbox data-gallery="sainsmart-dds120" }
<span class="caption">Saintsmart Dds120 Device Bottom</span>

[![Saintsmart Dds120 Ams1117 3.3](./img/Saintsmart_dds120_ams1117-3.3.jpg)](./img/Saintsmart_dds120_ams1117-3.3.jpg "Saintsmart Dds120 Ams1117 3.3"){ .glightbox data-gallery="sainsmart-dds120" }
<span class="caption">Saintsmart Dds120 Ams1117 3.3</span>

[![Dds120 Mugshot](./img/Dds120_mugshot.png)](./img/Dds120_mugshot.png "Dds120 Mugshot"){ .glightbox data-gallery="sainsmart-dds120" }
<span class="caption">Dds120 Mugshot</span>

[![Saintsmart Dds120 Fx2](./img/Saintsmart_dds120_fx2.jpg)](./img/Saintsmart_dds120_fx2.jpg "Saintsmart Dds120 Fx2"){ .glightbox data-gallery="sainsmart-dds120" }
<span class="caption">Saintsmart Dds120 Fx2</span>

[![Saintsmart Dds120 Ti Cd4052bm](./img/Saintsmart_dds120_ti_cd4052bm.jpg)](./img/Saintsmart_dds120_ti_cd4052bm.jpg "Saintsmart Dds120 Ti Cd4052bm"){ .glightbox data-gallery="sainsmart-dds120" }
<span class="caption">Saintsmart Dds120 Ti Cd4052bm</span>

[![Sainsmart Dds120 Front 2](./img/Sainsmart_dds120_front_2.jpg)](./img/Sainsmart_dds120_front_2.jpg "Sainsmart Dds120 Front 2"){ .glightbox data-gallery="sainsmart-dds120" }
<span class="caption">Sainsmart Dds120 Front 2</span>

[![Sainsmart Dds120 Box 1](./img/Sainsmart_dds120_box_1.jpg)](./img/Sainsmart_dds120_box_1.jpg "Sainsmart Dds120 Box 1"){ .glightbox data-gallery="sainsmart-dds120" }
<span class="caption">Sainsmart Dds120 Box 1</span>

[![Sainsmart Dds120 Box 3](./img/Sainsmart_dds120_box_3.jpg)](./img/Sainsmart_dds120_box_3.jpg "Sainsmart Dds120 Box 3"){ .glightbox data-gallery="sainsmart-dds120" }
<span class="caption">Sainsmart Dds120 Box 3</span>

[![Sainsmart Dds120 Front 4](./img/Sainsmart_dds120_front_4.jpg)](./img/Sainsmart_dds120_front_4.jpg "Sainsmart Dds120 Front 4"){ .glightbox data-gallery="sainsmart-dds120" }
<span class="caption">Sainsmart Dds120 Front 4</span>

</div>
## Protocol

We use an open-source firmware for this device (i.e., not the vendor firmware/protocol), hence we do not need to know the vendor protocol. There is some [historic vendor firmware/protocol info](https://sigrok.org/wiki/SainSmart_DDS120/Info#Vendor_firmware) for those interested, though.

## Firmware

In order to use this device, the [sigrok-firmware-fx2lafw](https://sigrok.org/wiki/Fx2lafw) (>= 0.1.4) firmware is required.

The firmware was originally written by Jochen Hoenicke (see [README](http://sigrok.org/gitweb/?p=sigrok-firmware-fx2lafw.git;a=blob;f=README) for details), thanks a lot!

**Note**: The firmware is **not** flashed into the device permanently! You only need to make it available in the usual place where [libsigrok](https://sigrok.org/wiki/Libsigrok) looks for firmware files, it will be used automatically (and "uploaded" to the Cypress FX2's SRAM every time you attach the device to a USB port).

**Note**: On Windows, you will have to [assign the WinUSB driver via Zadig](https://sigrok.org/wiki/Windows#Device_specific_USB_driver) **twice**: the first time for the initial USB VID/PID the device has when attaching it via USB (04b4:602a or 04b5:602a, depending on which vendor driver is currently being used by the device), and a second time after the firmware has been uploaded to the device and the device has "renumerated" with a different VID/PID pair (1d50:608e).

See [this section](https://sigrok.org/wiki/SainSmart_DDS120/Info#Open-source_firmware_details) for technical details about the firmware/hardware.

## Resources
- [EEVBlog forum thread](http://www.eevblog.com/forum/testgear/sainsmart-dds120-usb-oscilloscope-(buudai-bm102)/)
- [Detailed description of the hardware](http://www.360customs.de/en/2014/10/usb-oszilloskop-sainsmart-dds120-2-kanal-20mhz-50msps-buudairocktech-bm102/)
- [Vendor product page](http://www.sainsmart.com/sainsmart-dds-120-20m-50m-s-virtual-oscilloscope-silver.html)
- [Vendor software download links](https://www.eevblog.com/forum/testgear/saintsmart-dds120-software-download/msg818124/#msg818124)

