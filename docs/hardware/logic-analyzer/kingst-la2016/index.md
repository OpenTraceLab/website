---
title: Kingst LA2016
---

# Kingst LA2016

<div class="infobox" markdown>

![Kingst LA2016](./img/Kingst_la2016_paper.jpg){ .infobox-image }

### Kingst LA2016

| | |
|---|---|
| **Status** | supported |
| **Source code** | [kingst-la2016](https://github.com/OpenTraceLab/OpenTraceCapture/tree/main/src/hardware/kingst-la2016) |
| **Channels** | 16 |
| **Samplerate** | 200MHz max. |
| **Samplerate (state)** | State analysis not supported |
| **Triggers** | Level (multiple channels)Edge (one channel) |
| **Min/max voltage** | -50V — 50V |
| **Threshold voltage** | Configurable:-4V—4V, min step 0.01V |
| **Memory** | 128MByte DDR2 SDRAM40M—10G samples |
| **Compression** | Yes |
| **Website** | [qdkingst.com](http://www.qdkingst.com/en) |

</div>

The **Kingst LA2016** is a USB-based, 16-channel logic analyser with 200MHz maximum samplerate and 128MiB sample memory. It is part of the [Kingst LA Series](https://sigrok.org/wiki/Kingst_LA_Series) and is supported by the **kingst-la2016** sigrok driver.

The current vendor is "Qingdao Kingst Electronics Co., Ltd." but older models are branded "Jiankun" rather than "Kingst".
Detailed specifications and the vendor software are available on the [Kingst website](http://www.qdkingst.com/en/products).

TODO Move common items to the series' page. Make device pages specific to devices, avoid redundancy.

- **Support Status:**
It is recommended to use recent software (at least mid November 2021, better February 2022), issues with LA2016 and LA1016 got addressed, and support for other devices has improved.
- 2021-11-19 [Open firmware](https://github.com/sigrokproject/sigrok-firmware/pull/1) for the FX2 MCU is available for testing. FPGA bitstreams extraction from vendor software still is required. Behaviour of the vendor's and the open source MCU firmware shall be the same.
- **Known Issues:**
PulseView allows the user to setup multiple edge triggers, but the analyser only supports one. Please only use one edge trigger to avoid undefined behaviour. Note the edge trigger can be combined with any number of level triggers. (gsi: Is this worth mentioning here? It's well understood that software use is contrained by hardware capabilities, all supported devices have constraints.)
- The device supports an input threshold range of -4.0V to +4.0V, but the sigrok driver currently implements a limited set of discrete values. Which covers all popular logic families (0.8V to 5.0V), but omits zero crossing as well as negative values. Which should not be too limiting a constraint.
- The vendor's hardware design does not allow to read back previously written configurations. The software always needs to assign a set of default values upon startup, and cannot continue using a previously applied configuration.
- Unplugging the analyser and then attempting to start a capture causes PulseView to crash.

See [Kingst LA2016/Info](https://sigrok.org/wiki/Kingst_LA2016/Info) for more details (USB identification).

## Hardware

This logic analyser has been on the market since around 2012 and there are a few different revisions of it.
The [schematic](/wimg/2/26/Kingst_LA2016_LA1016_Schematic.zip) has been reverse engineered from
a unit purchased in 2020 containing a PCB marked as v1.3.0. 
The circuitry of older PCBs is similar but may have different voltage regulators, different input
channel routing to the FPGA, and lack the input threshold adjustment.

The LA1016 uses identical hardware with a different FPGA bitstream which limits the sample rate to 100MHz maximum.

All of these devices use the same firmware for the FX2LP MCU but there are four different FPGA bitstreams;
i.e. LA1016 & LA2016 bitstreams and the older versions of these (to swap some of the input channels as required by PCB routing changes).
Once the FX2LP firmware has been loaded, a 'magic number' is read from EEPROM which identifies the
device and thus allows the correct FPGA bitstream to be loaded.

Note that the LA1016 cannot be boosted to 200MHz by changing the 'magic number' or the FPGA bitstream.
When the FPGA initialises, its reads 16 bytes from U10 which are used to authenticate the bitstream; these bytes are different for 100 and 200MHz devices.
Furthermore, the OEM software performs a challenge-response with U10 to authenticate the logic analyser as genuine 'Kingst'.
The good news is that U10 does not impact sigrok support in any way and we don't need to communicate with it.

Main components and their function:

- **MCU** Cypress FX2LP
This MCU only has volatile memory and in this implementation it's firmware is loaded from the host by the application software.
Either the OEM firmware or open source firmware can be used.
In essence, it just performs data moving operations:
- Endpoint 0 to EEPROM read/write
- Endpoint 0 to SPI read/write for FPGA control registers
- Endpoint 2 bulk out to SPI for loading FPGA bitstream
- Endpoint 6 bulk in to read capture data from FPGA/SDRAM
- **EEPROM** Atmel AT24C02 2Kbit
This non-volatile memory stores:
- VID:PID which is 77a1:01a2 for LA1016 and LA2016 devices
- 'magic number' to identify model and revision
- purchase date (presumably for warranty claims)
- other information related to U10 but not of interest to sigrok
- **FPGA** Altera EP4CE6
Currently requires the OEM bitstream.
Has a bank of approximately 60 byte-wide registers accessed via SPI which are used to contol FPGA functions.
Captures 16 input channels, performs compression (run length encoding, 16bit sample plus 8 bit repetition count).
Stores samples to SDRAM (or streams direct to USB but we don't implement that method).
Interestingly, this device (6K LE) shares the same die as the next up device EP4CE10 (10K LE) and can be programmed as such. However, functionality would not be guaranteed as CE6 devices may be CE10 rejects.
If open source FPGA code were to become available there would be capacity to experiment with more advanced triggers, such as pattern trigger for SPI or I2C.
- **SDRAM** Samsung DDR2
Samples are stored as 3 bytes (16bit sample plus 8 bit repetition count).
A 'transfer packet' for upload is 16 bytes = 5 compressed samples plus a sequence number byte.
Burst read/write for this SDRAM is up to 16 bytes, which matches the transfer packet size and is likely used for all SDRAM read/writes.
- **U10** Kingst Authentication Device
Not used by sigrok.
- Provides fixed bytes identifier to FPGA for bitstream validation (either LA1016 100MHz or LA2016 200MHz bitstream)
- Provides challenge-response rolling-code for OEM software to authenticate the device as genuine 'Kingst'

Datasheets:

U1 [EP4CE6F17C8N](https://www.intel.com/content/www/us/en/products/programmable/fpga/cyclone-iv.html) Cyclone IV E FPGA
U2,4,5,7 [	PDWL050019](http://sxsemi.com/upfile/PDWL050019-SOT236.pdf) TVS Diode Array
U3 [CY7C68013A-100AXC](https://www.cypress.com/part/cy7c68013a-100axc) EZUSB MCU
U6,U8 [SGM2019](http://www.sg-micro.com/show-product-510.html) Linear Regulator
U9 [AT24C02](https://www.microchip.com/wwwproducts/en/AT24C02C) EEPROM 2kbit
U10 (device not identified, small MCU of some type)
U11 K4T1G164QG-BCF8, DDR2 SDRAM, obsolete
U12,U13 [SGM6013](http://www.sg-micro.com/show-product-519.html) Switch-mode Regulator
U14 [SGM8272](http://www.sg-micro.com/show-product-203.html) Dual Op-amp
U15 [TPS60403](http://www.ti.com/lit/ds/symlink/tps60403.pdf) Charge Pump Voltage Inverter

## Photos

<div class="photo-grid" markdown>

[![Kingst La2016 Paper](./img/Kingst_la2016_paper.jpg)](./img/Kingst_la2016_paper.jpg "Kingst La2016 Paper"){ .glightbox data-gallery="kingst-la2016" }
<span class="caption">Kingst La2016 Paper</span>

[![Kingst La2016 Mugshot](./img/Kingst_la2016_mugshot.png)](./img/Kingst_la2016_mugshot.png "Kingst La2016 Mugshot"){ .glightbox data-gallery="kingst-la2016" }
<span class="caption">Kingst La2016 Mugshot</span>

[![Kingst La2016 Samsung K4t1g164qg](./img/Kingst_la2016_samsung_k4t1g164qg.jpg)](./img/Kingst_la2016_samsung_k4t1g164qg.jpg "Kingst La2016 Samsung K4t1g164qg"){ .glightbox data-gallery="kingst-la2016" }
<span class="caption">Kingst La2016 Samsung K4t1g164qg</span>

[![Kingst La2016 Unmarked Ic](./img/Kingst_la2016_unmarked_ic.jpg)](./img/Kingst_la2016_unmarked_ic.jpg "Kingst La2016 Unmarked Ic"){ .glightbox data-gallery="kingst-la2016" }
<span class="caption">Kingst La2016 Unmarked Ic</span>

[![Kingst La2016 Package Contents](./img/Kingst_la2016_package_contents.jpg)](./img/Kingst_la2016_package_contents.jpg "Kingst La2016 Package Contents"){ .glightbox data-gallery="kingst-la2016" }
<span class="caption">Kingst La2016 Package Contents</span>

[![Kingst La2016 Device Top](./img/Kingst_la2016_device_top.jpg)](./img/Kingst_la2016_device_top.jpg "Kingst La2016 Device Top"){ .glightbox data-gallery="kingst-la2016" }
<span class="caption">Kingst La2016 Device Top</span>

[![Kingst La2016 Cypress Fx2](./img/Kingst_la2016_cypress_fx2.jpg)](./img/Kingst_la2016_cypress_fx2.jpg "Kingst La2016 Cypress Fx2"){ .glightbox data-gallery="kingst-la2016" }
<span class="caption">Kingst La2016 Cypress Fx2</span>

[![Kingst La2016 Pcb 1.3.0 Top](./img/Kingst-la2016-pcb-1.3.0-top.png)](./img/Kingst-la2016-pcb-1.3.0-top.png "Kingst La2016 Pcb 1.3.0 Top"){ .glightbox data-gallery="kingst-la2016" }
<span class="caption">Kingst La2016 Pcb 1.3.0 Top</span>

[![Kingst La2016 Pcb Top](./img/Kingst_la2016_pcb_top.jpg)](./img/Kingst_la2016_pcb_top.jpg "Kingst La2016 Pcb Top"){ .glightbox data-gallery="kingst-la2016" }
<span class="caption">Kingst La2016 Pcb Top</span>

[![Kingst La2016 Pcb Bottom](./img/Kingst_la2016_pcb_bottom.jpg)](./img/Kingst_la2016_pcb_bottom.jpg "Kingst La2016 Pcb Bottom"){ .glightbox data-gallery="kingst-la2016" }
<span class="caption">Kingst La2016 Pcb Bottom</span>

[![Kingst La2016 Pcb 1.3.0 Bottom](./img/Kingst-la2016-pcb-1.3.0-bottom.png)](./img/Kingst-la2016-pcb-1.3.0-bottom.png "Kingst La2016 Pcb 1.3.0 Bottom"){ .glightbox data-gallery="kingst-la2016" }
<span class="caption">Kingst La2016 Pcb 1.3.0 Bottom</span>

[![Kingst La2016 Altera Cyclone4 Ep4ce6f17c8n](./img/Kingst_la2016_altera_cyclone4_ep4ce6f17c8n.jpg)](./img/Kingst_la2016_altera_cyclone4_ep4ce6f17c8n.jpg "Kingst La2016 Altera Cyclone4 Ep4ce6f17c8n"){ .glightbox data-gallery="kingst-la2016" }
<span class="caption">Kingst La2016 Altera Cyclone4 Ep4ce6f17c8n</span>

[![Kingst La2016 Atmel 24c02n](./img/Kingst_la2016_atmel_24c02n.jpg)](./img/Kingst_la2016_atmel_24c02n.jpg "Kingst La2016 Atmel 24c02n"){ .glightbox data-gallery="kingst-la2016" }
<span class="caption">Kingst La2016 Atmel 24c02n</span>

[![Kingst La2016 Device Bottom](./img/Kingst_la2016_device_bottom.jpg)](./img/Kingst_la2016_device_bottom.jpg "Kingst La2016 Device Bottom"){ .glightbox data-gallery="kingst-la2016" }
<span class="caption">Kingst La2016 Device Bottom</span>

[![Kingst La2016 Fpni](./img/Kingst_la2016_fpni.jpg)](./img/Kingst_la2016_fpni.jpg "Kingst La2016 Fpni"){ .glightbox data-gallery="kingst-la2016" }
<span class="caption">Kingst La2016 Fpni</span>

</div>
## Protocol

See the [Kingst LA Series](https://sigrok.org/wiki/Kingst_LA_Series) page for details, all devices communicate to the host in identical ways.

## Firmware

See the [Kingst LA Series](https://sigrok.org/wiki/Kingst_LA_Series) page for details. All devices share the same firmware extraction requirement.

## Resources
- [Vendor software](http://www.qdkingst.com/en/download)
- [User guide](http://www.qdkingst.com/download/vis_ug_en)
- [Reverse engineered schematic](/wimg/2/26/Kingst_LA2016_LA1016_Schematic.zip)

