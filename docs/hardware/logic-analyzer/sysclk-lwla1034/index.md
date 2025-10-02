---
title: Sysclk LWLA1034
---

# Sysclk LWLA1034

<div class="infobox" markdown>

![Sysclk LWLA1034](./img/Sysclk_lwla1034_pcb_top.jpg){ .infobox-image }

### Sysclk LWLA1034

| | |
|---|---|
| **Status** | supported |
| **Source code** | [sysclk-lwla](https://github.com/OpenTraceLab/OpenTraceCapture/tree/main/src/hardware/sysclk-lwla) |
| **Channels** | 34 |
| **Samplerate** | 125MHz (max) |
| **Samplerate (state)** | ? |
| **Triggers** | 34 + extern |
| **Min/max voltage** | 0-5V |
| **Threshold voltage** | ? |
| **Memory** | 256Kbit/channel |
| **Compression** | RLE |
| **Website** | [aliexpress.com](http://www.aliexpress.com/item/free-shipping-New-arrival-Powerful-100MHz-34-channels-LA1034-Logic-Analyzer-Timing-State-Logic-Analyzer/1227957767.html) |

</div>

The **Sysclk LWLA1034** is a USB-based, 34-channel logic analyzer with up to 125MHz sampling rate.

See [Sysclk LWLA1034/Info](https://sigrok.org/wiki/Sysclk_LWLA1034/Info) for more details (such as **lsusb -v** output) about the device.

## Hardware
- Altera EP2C5Q208C8N (Cyclone II) FPGA
- Cypress CY7C68013A-56 (FX2) USB interface chip
- Cypress 256k×36 SRAM (likely a [CY7C1361C-133AXC](http://www.cypress.com/?mpn=CY7C1361C-133AXC) or similar)
- STC15F104E 8051-based microcontroller

The not-installed 10-pin connector between the USB socket and the large capacitor seems to connect to the JTAG pins of the FPGA.

## Photos

<div class="photo-grid" markdown>

[![Sysclk Lwla1034 Pcb Top](./img/Sysclk_lwla1034_pcb_top.jpg)](./img/Sysclk_lwla1034_pcb_top.jpg "Sysclk Lwla1034 Pcb Top"){ .glightbox data-gallery="sysclk-lwla1034" }
<span class="caption">Sysclk Lwla1034 Pcb Top</span>

[![Sysclk Lwla1034 Pcb Closeup](./img/Sysclk_lwla1034_pcb_closeup.jpg)](./img/Sysclk_lwla1034_pcb_closeup.jpg "Sysclk Lwla1034 Pcb Closeup"){ .glightbox data-gallery="sysclk-lwla1034" }
<span class="caption">Sysclk Lwla1034 Pcb Closeup</span>

[![Sysclk Lwla1034 Chip3 Removed Marking](./img/Sysclk_lwla1034_chip3_removed_marking.jpg)](./img/Sysclk_lwla1034_chip3_removed_marking.jpg "Sysclk Lwla1034 Chip3 Removed Marking"){ .glightbox data-gallery="sysclk-lwla1034" }
<span class="caption">Sysclk Lwla1034 Chip3 Removed Marking</span>

[![Sysclk Lwla1034 Cypress Sram](./img/Sysclk_lwla1034_cypress_sram.jpg)](./img/Sysclk_lwla1034_cypress_sram.jpg "Sysclk Lwla1034 Cypress Sram"){ .glightbox data-gallery="sysclk-lwla1034" }
<span class="caption">Sysclk Lwla1034 Cypress Sram</span>

[![Sysclk Lwla1034 Mugshot](./img/Sysclk_lwla1034_mugshot.png)](./img/Sysclk_lwla1034_mugshot.png "Sysclk Lwla1034 Mugshot"){ .glightbox data-gallery="sysclk-lwla1034" }
<span class="caption">Sysclk Lwla1034 Mugshot</span>

[![Sysclk Lwla1034 Device Usb](./img/Sysclk_lwla1034_device_usb.jpg)](./img/Sysclk_lwla1034_device_usb.jpg "Sysclk Lwla1034 Device Usb"){ .glightbox data-gallery="sysclk-lwla1034" }
<span class="caption">Sysclk Lwla1034 Device Usb</span>

[![Sysclk Lwla1034 Device Connector](./img/Sysclk_lwla1034_device_connector.jpg)](./img/Sysclk_lwla1034_device_connector.jpg "Sysclk Lwla1034 Device Connector"){ .glightbox data-gallery="sysclk-lwla1034" }
<span class="caption">Sysclk Lwla1034 Device Connector</span>

[![Sysclk Lwla1034 Pcb Bottom](./img/Sysclk_lwla1034_pcb_bottom.jpg)](./img/Sysclk_lwla1034_pcb_bottom.jpg "Sysclk Lwla1034 Pcb Bottom"){ .glightbox data-gallery="sysclk-lwla1034" }
<span class="caption">Sysclk Lwla1034 Pcb Bottom</span>

[![Sysclk Lwla1034 Device Open](./img/Sysclk_lwla1034_device_open.jpg)](./img/Sysclk_lwla1034_device_open.jpg "Sysclk Lwla1034 Device Open"){ .glightbox data-gallery="sysclk-lwla1034" }
<span class="caption">Sysclk Lwla1034 Device Open</span>

[![Sysclk Lwla1034 Crystal 40mhz](./img/Sysclk_lwla1034_crystal_40mhz.jpg)](./img/Sysclk_lwla1034_crystal_40mhz.jpg "Sysclk Lwla1034 Crystal 40mhz"){ .glightbox data-gallery="sysclk-lwla1034" }
<span class="caption">Sysclk Lwla1034 Crystal 40mhz</span>

[![Sysclk Lwla1034 Crystal 50mhz](./img/Sysclk_lwla1034_crystal_50mhz.jpg)](./img/Sysclk_lwla1034_crystal_50mhz.jpg "Sysclk Lwla1034 Crystal 50mhz"){ .glightbox data-gallery="sysclk-lwla1034" }
<span class="caption">Sysclk Lwla1034 Crystal 50mhz</span>

[![Sysclk Lwla1034 Software](./img/Sysclk_lwla1034_software.png)](./img/Sysclk_lwla1034_software.png "Sysclk Lwla1034 Software"){ .glightbox data-gallery="sysclk-lwla1034" }
<span class="caption">Sysclk Lwla1034 Software</span>

[![Sysclk Lwla1034 Altera Cyclone2](./img/Sysclk_lwla1034_altera_cyclone2.jpg)](./img/Sysclk_lwla1034_altera_cyclone2.jpg "Sysclk Lwla1034 Altera Cyclone2"){ .glightbox data-gallery="sysclk-lwla1034" }
<span class="caption">Sysclk Lwla1034 Altera Cyclone2</span>

[![Sysclk Lwla1034 Ams1117 12](./img/Sysclk_lwla1034_ams1117_12.jpg)](./img/Sysclk_lwla1034_ams1117_12.jpg "Sysclk Lwla1034 Ams1117 12"){ .glightbox data-gallery="sysclk-lwla1034" }
<span class="caption">Sysclk Lwla1034 Ams1117 12</span>

[![Sysclk Lwla1034 Device Top](./img/Sysclk_lwla1034_device_top.jpg)](./img/Sysclk_lwla1034_device_top.jpg "Sysclk Lwla1034 Device Top"){ .glightbox data-gallery="sysclk-lwla1034" }
<span class="caption">Sysclk Lwla1034 Device Top</span>

[![Sysclk Lwla1034 Chip2](./img/Sysclk_lwla1034_chip2.jpg)](./img/Sysclk_lwla1034_chip2.jpg "Sysclk Lwla1034 Chip2"){ .glightbox data-gallery="sysclk-lwla1034" }
<span class="caption">Sysclk Lwla1034 Chip2</span>

[![Sysclk Lwla1034 Pcb Bottom2](./img/Sysclk_lwla1034_pcb_bottom2.jpg)](./img/Sysclk_lwla1034_pcb_bottom2.jpg "Sysclk Lwla1034 Pcb Bottom2"){ .glightbox data-gallery="sysclk-lwla1034" }
<span class="caption">Sysclk Lwla1034 Pcb Bottom2</span>

[![Sysclk Lwla1034 24c64n Otherso8 Crystal](./img/Sysclk_lwla1034_24c64n_otherso8_crystal.jpg)](./img/Sysclk_lwla1034_24c64n_otherso8_crystal.jpg "Sysclk Lwla1034 24c64n Otherso8 Crystal"){ .glightbox data-gallery="sysclk-lwla1034" }
<span class="caption">Sysclk Lwla1034 24c64n Otherso8 Crystal</span>

[![Sysclk Lwla1034 Cypress Fx2](./img/Sysclk_lwla1034_cypress_fx2.jpg)](./img/Sysclk_lwla1034_cypress_fx2.jpg "Sysclk Lwla1034 Cypress Fx2"){ .glightbox data-gallery="sysclk-lwla1034" }
<span class="caption">Sysclk Lwla1034 Cypress Fx2</span>

[![Sysclk Lwla1034 Device Bottom](./img/Sysclk_lwla1034_device_bottom.jpg)](./img/Sysclk_lwla1034_device_bottom.jpg "Sysclk Lwla1034 Device Bottom"){ .glightbox data-gallery="sysclk-lwla1034" }
<span class="caption">Sysclk Lwla1034 Device Bottom</span>

[![Sysclk Lwla1034 Pcb Top2](./img/Sysclk_lwla1034_pcb_top2.jpg)](./img/Sysclk_lwla1034_pcb_top2.jpg "Sysclk Lwla1034 Pcb Top2"){ .glightbox data-gallery="sysclk-lwla1034" }
<span class="caption">Sysclk Lwla1034 Pcb Top2</span>

[![Sysclk Lwla1034 Ams1117 33](./img/Sysclk_lwla1034_ams1117_33.jpg)](./img/Sysclk_lwla1034_ams1117_33.jpg "Sysclk Lwla1034 Ams1117 33"){ .glightbox data-gallery="sysclk-lwla1034" }
<span class="caption">Sysclk Lwla1034 Ams1117 33</span>

</div>
## Software

[](./img/Sysclk_lwla1034_software.png)

## Firmware

We have received permission from the vendor to distribute the FPGA bitstreams with sigrok. Thus, the bitstreams are now included in the sigrok-firmware module.

- The FX2 firmware is loaded from an EEPROM on the board, so that the final USB device descriptor is immediately available on power-up.
- Endpoint 4 is used exclusively for loading a new bitstream into the FPGA.
- Endpoint 2 is used for sending commands to the FPGA firmware, with responses (if any) coming in from endpoint 6.

Reverse engineering of the vendor's custom protocol has been completed. See [Sysclk LWLA1034/Protocol](https://sigrok.org/wiki/Sysclk_LWLA1034/Protocol) for the documentation.

## Resources
- [Mcupro blog on CSDN](http://blog.csdn.net/mcupro)

