---
title: Microchip PICkit2
---

# Microchip PICkit2

<div class="infobox" markdown>

![Microchip PICkit2](./img/Microchip_pickit2_pcb_back.jpg){ .infobox-image }

### Microchip PICkit2

| | |
|---|---|
| **Status** | supported |
| **Source code** | [microchip-pickit2](https://github.com/OpenTraceLab/OpenTraceCapture/tree/main/src/hardware/microchip-pickit2) |
| **Channels** | 3 |
| **Samplerate** | 1MHz |
| **Triggers** | value, edge, counter |
| **Min/max voltage** | 2.5V — 5.0V |
| **Memory** | 1024 samples |
| **Compression** | no |
| **Website** | [microchip.com](https://www.microchip.com/DevelopmentTools/ProductDetails/pg164120) |

</div>

The [Microchip PICkit2](https://www.microchip.com/DevelopmentTools/ProductDetails/pg164120) is a programmer/debugger for PIC microcontrollers, but it can also be used as a general purpose I/O device, virtual COM port, or 3-channel logic analyzer (up to 1MHz samplerate, 1024 samples memory depth, hardware/firmware trigger support).

See [Microchip PICkit2/Info](https://sigrok.org/wiki/Microchip_PICkit2/Info) for more details (such as **lsusb -v** output) about the device.

The sigrok project includes a **microchip-pickit2** driver which supports data acquisition with the PICkit2 device. But trigger support is incomplete and needs more attention. Reviews/feedback/patches are very much appreciated.

## Hardware

Essential components:

- Microchip PIC18F2550-I/SO
- 24LC512 (2x)

Pinout:

- 1: Vpp programming voltage, gets provided by the PICkit, also MCLR, or "pin 0" (output only) in some vendor or external applications
- 2: Vdd target supply voltage, can get sensed or provided by the PICkit
- 3: Vss aka ground
- 4: PGD, ICSP data, "channel 1" in pk2la, input or output, RX in the "UART tool"
- 5: PGC, ICSP clock, "channel 2" in pk2la, input or output, TX in the "UART tool"
- 6: AUX, "channel 3" in pk2la, input or output, fixed voltage threshold

Hardware/firmware constraints:

- Vdd **must** be powered (internally or externally) to detect voltages on input pins (see the "UART Tool" and "Logic Tool User Guide" documents)
- (externally provided) Vdd can be in the 2.5V to 5.0V range
- pins 4 and 5 can detect logic levels down to 2.5V families, pin 6 is fixed to 3.6V families (the user guide states unreliable detection for lower voltage levels, and ST characteristics)
- in logic analyzer mode (including the phase which waits for the trigger condition) the device is unable to communicate to the PC, the user needs to press the button to cancel a pending acquisition if the trigger condition isn't seen

## Photos

<div class="photo-grid" markdown>

[![Microchip Pickit2 Pcb Back](./img/Microchip_pickit2_pcb_back.jpg)](./img/Microchip_pickit2_pcb_back.jpg "Microchip Pickit2 Pcb Back"){ .glightbox data-gallery="microchip-pickit2" }
<span class="caption">Microchip Pickit2 Pcb Back</span>

[![Microchip Pickit2 Device Front](./img/Microchip_pickit2_device_front.jpg)](./img/Microchip_pickit2_device_front.jpg "Microchip Pickit2 Device Front"){ .glightbox data-gallery="microchip-pickit2" }
<span class="caption">Microchip Pickit2 Device Front</span>

[![Microchip Pickit2 Pcb Front](./img/Microchip_pickit2_pcb_front.jpg)](./img/Microchip_pickit2_pcb_front.jpg "Microchip Pickit2 Pcb Front"){ .glightbox data-gallery="microchip-pickit2" }
<span class="caption">Microchip Pickit2 Pcb Front</span>

[![Microchip Pickit2](./img/Microchip_pickit2.png)](./img/Microchip_pickit2.png "Microchip Pickit2"){ .glightbox data-gallery="microchip-pickit2" }
<span class="caption">Microchip Pickit2</span>

[![Microchip Pickit2 Device Back](./img/Microchip_pickit2_device_back.jpg)](./img/Microchip_pickit2_device_back.jpg "Microchip Pickit2 Device Back"){ .glightbox data-gallery="microchip-pickit2" }
<span class="caption">Microchip Pickit2 Device Back</span>

[![Microchip Pickit2 Package Front](./img/Microchip_pickit2_package_front.jpg)](./img/Microchip_pickit2_package_front.jpg "Microchip Pickit2 Package Front"){ .glightbox data-gallery="microchip-pickit2" }
<span class="caption">Microchip Pickit2 Package Front</span>

</div>
## Protocol

The PICkit2 can be used as a general purpose I/O device, where up to four pins are under software control, and can be either input or output pins with a user specified logic level. This mode is slow, and is intended for interactive use, or visualization of slowly changing signals. There is a logic analyzer mode, where a setup packet is sent to the device, then acquisition takes place under the device's control (and without communication to the PC), then acquired data gets uploaded to the PC and is available for visualization or processing.

Trigger capabilities: Can trigger on high or low level, or rising or falling edge on any of pins 4, 5, and 6. There is an optional trigger count (trigger only takes effect after the specified condition was observed for the specified number of times). The relation of acquired data and the trigger position is adjustable (see the software paragraph below).

Software constraints (vendor software, and pk2la which is modelled after the vendor software):
The user can chose from six options where the trigger position shall reside: At (roughly) 10/50/90% within the display window's width of 1K samples (referred to as "keeps (just over) one division before/after the trigger"). Or data optionally gets displayed 1/2/3 windows worth after the trigger condition (referred to as "delay N windows"). This latter choice is especially useful due to the limited memory depth, it allows to e.g. trigger on the start of a frame yet inspect later bits in that frame while acquisition uses high enough a samplerate. This would not be possible if the trigger must be in the 1024 samples range that gets acquired and displayed. For repetitive waveforms users could even "piece together" multiple acquisitions and thus get recordings with some 4K samples length.

USB communication is done in 64-byte packets (padding applies when payload is less than 64 bytes). Communication timeouts are non-fatal. Those requests which result in responses just keep reading until response data became available.

The rough outline of the communication sequence for LA mode is:

- (optional) setup Vdd if not provided externally
- send the SETUP packet, check the response's status (user initiated cancel, or data availability)
- retrieve sample data which is kept in four segments: select a bank (and offset within the bank), read two 64 byte packets from that bank
- decode the (packed) raw acquisition data, to feed the sigrok session with the required amount of samples

The samplerate is 1MHz divided by an integer in the 1..256 range. If a trigger condition was specified by the user, the set of involved channels, their respective level, and level/edge selection gets communicated in the SETUP packet. As are the trigger count and the trigger position.

The SETUP packet uses a 16bit value for the trigger position. The pk2la project maps the above six-values user choice to some magic values while their calculation is uncertain (gsi: can't spot a pattern in those values, they're not related to percentage values or sample counts).

Raw acquisition data gets retrieved in 64-byte chunks (the USB endpoint's size). 512 bytes of raw data carry 1024 samples of three channels each.

Most of the above information was gathered from the GPL licensed pk2la project.

## Compatibility

Fun fact: The [PICKit3 device](https://www.microchip.com/Developmenttools/ProductDetails/PG164130) was marketed as an upgrade to the PICKit2, but reduced the feature set and turned it into a mere programmer/debugger. The versatility of alternatively providing software controlled I/O, virtual COM port, and logic analyzer mode is unique to the PICKit2. See a slightly ticked off Dave Jones in [EEVblog episode #39](https://www.youtube.com/watch?v=LjfIS65mwn8), a review which compares the PICkit3 and PICkit2 devices and their feature set ([blog article](https://www.eevblog.com/2009/10/21/eevblog-39-pickit-3-programmerdebugger-review/)). And see the [Microchip response video](https://www.youtube.com/watch?v=3YUvlrVlNao).&#160;:)

Microchip EOLed the PICkit2 (and PICkit3), though clones are available for sale as well as DIY. See Wikipedia and the references section below.

## Resources
- [PICkit2 vendor's product page](https://www.microchip.com/DevelopmentTools/ProductDetails/pg164120)
- [user manual](http://ww1.microchip.com/downloads/en/DeviceDoc/51553E.pdf), schematics in appendix B
- [Logic Tool User Guide](http://ww1.microchip.com/downloads/en/DeviceDoc/PICkit%202%20Logic%20Tool%20User%20Guide.pdf)
- The [pk2-la project](http://sourceforge.net/projects/pk2-la/) has basic protocol docs and a Python implementation.
- [Wikipedia PICkit article](https://en.wikipedia.org/wiki/PICKit)
- [instructables How to make a PICkit 2 clone](https://www.instructables.com/id/How-to-Make-a-PIC-Programmer-PicKit-2-clone/)

