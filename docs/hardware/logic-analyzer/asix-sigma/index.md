---
title: ASIX SIGMA
---

# ASIX SIGMA

<div class="infobox" markdown>

![ASIX SIGMA](./img/ASIX_SIGMA_2_back.jpg){ .infobox-image }

### ASIX SIGMA

| | |
|---|---|
| **Status** | supported |
| **Source code** | [asix-sigma](https://github.com/OpenTraceLab/OpenTraceCapture/tree/main/src/hardware/asix-sigma) |
| **Channels** | 16 |
| **Samplerate** | 200MHz @ 4ch, 100MHz @ 8ch, 50MHz @ 16ch |
| **Samplerate (state)** | 50MHz |
| **Triggers** | value, edge, duration, sequence, counter, logical ops |
| **Min/max voltage** | -0.3V — 5.5V |
| **Threshold voltage** | Fixed: VIH=2.0V, VIL=0.8V (suitable for TTL, LVTTL, 2.7-5.5V CMOS) |
| **Memory** | 32MByte (SDRAM) |
| **Compression** | "real-time hardware data compression" |
| **Website** | [asix.net](http://tools.asix.net/dbg_sigma.htm) |

</div>

The **ASIX SIGMA/SIGMA2** is a USB-based, 16-channel logic analyzer with up to 200MHz sampling rate.

See [ASIX SIGMA/Info](https://sigrok.org/wiki/ASIX_SIGMA/Info) for more details (such as **lsusb -vvv** output) about the device.

Many thanks to the vendor ([ASIX](http://www.asix.net/)) for providing information on the protocol used to communicate with the device and for releasing the device's firmware / FPGA bitstreams under a [license which allows us to distribute the files](http://sigrok.org/gitweb/?p=sigrok-firmware.git;a=blob;f=asix-sigma/LICENSE.Sigma).

Notice that the device's firmware supports quite complex hardware triggers, but the software driver is limited to data pattern (values) and edge (slope) triggers. Sample rates above 50MHz further limit the number of available channels, and trigger options.

## Hardware
- Xilinx Spartan XC3S50 (FPGA)
- FTDI FT245RL (USB UART/FIFO, includes EEPROM)
- 2x TI SN74LVC245AN (input buffer)
- MT 48LC16M16A2 (32MiB DRAM)
- voltage regulation (3V3, 2V5, 1V2)
- 2x TI '04 logic (hex inverters, for level shifting)

## Photos

<div class="photo-grid" markdown>

[![Asix Sigma 2 Back](./img/ASIX_SIGMA_2_back.jpg)](./img/ASIX_SIGMA_2_back.jpg "Asix Sigma 2 Back"){ .glightbox data-gallery="asix-sigma" }
<span class="caption">Asix Sigma 2 Back</span>

[![Asix Sigma 2 Usb](./img/ASIX_SIGMA_2_USB.jpg)](./img/ASIX_SIGMA_2_USB.jpg "Asix Sigma 2 Usb"){ .glightbox data-gallery="asix-sigma" }
<span class="caption">Asix Sigma 2 Usb</span>

[![Asix Sigma](./img/ASIX_SIGMA.jpg)](./img/ASIX_SIGMA.jpg "Asix Sigma"){ .glightbox data-gallery="asix-sigma" }
<span class="caption">Asix Sigma</span>

[![Asix Sigma 2 Pcb Top](./img/ASIX_SIGMA_2_PCB_top.jpg)](./img/ASIX_SIGMA_2_PCB_top.jpg "Asix Sigma 2 Pcb Top"){ .glightbox data-gallery="asix-sigma" }
<span class="caption">Asix Sigma 2 Pcb Top</span>

[![Sigma](./img/Sigma.jpg)](./img/Sigma.jpg "Sigma"){ .glightbox data-gallery="asix-sigma" }
<span class="caption">Sigma</span>

[![Asix Sigma 2 Header](./img/ASIX_SIGMA_2_header.jpg)](./img/ASIX_SIGMA_2_header.jpg "Asix Sigma 2 Header"){ .glightbox data-gallery="asix-sigma" }
<span class="caption">Asix Sigma 2 Header</span>

[![Asix Sigma 2 Pcb Bottom](./img/ASIX_SIGMA_2_PCB_bottom.jpg)](./img/ASIX_SIGMA_2_PCB_bottom.jpg "Asix Sigma 2 Pcb Bottom"){ .glightbox data-gallery="asix-sigma" }
<span class="caption">Asix Sigma 2 Pcb Bottom</span>

[![Asix Sigma 2](./img/ASIX_SIGMA_2.png)](./img/ASIX_SIGMA_2.png "Asix Sigma 2"){ .glightbox data-gallery="asix-sigma" }
<span class="caption">Asix Sigma 2</span>

</div>
### ASIX SIGMA

		- 
			[](./img/ASIX_SIGMA.jpg)

		- 
			[](./img/Sigma.jpg)

### ASIX SIGMA 2

		- 
			[](./img/ASIX_SIGMA_2_back.jpg)

		- 
			[](./img/ASIX_SIGMA_2_USB.jpg)

		- 
			[](./img/ASIX_SIGMA_2_header.jpg)

		- 
			[](./img/ASIX_SIGMA_2_PCB_top.jpg)

		- 
			[](./img/ASIX_SIGMA_2_PCB_bottom.jpg)

## Documentation

The ASIX SIGMA/SIGMA2 firmware files are generously provided by the vendor for distribution. As a result, the device works out of the box with sigrok.

Sample rates can be:

- 200MHz or 100MHz (fixed) with special firmware, limited number of available channels
- 50MHz divided by an integer in the 1..256 range, which results in a rough range of 200kHz to 50MHz
- external clock on one of the 16 input pins, rate up to some 20MHz (gets sampled at 50MHz)

Trigger support is limited to basic use:

- An edge on one of the 4 (200MHz) or 8 (100MHz) input pins. Common limitation of the device firmware.
- One edge on one of the 16 (50MHz) input pins, in addition to:
- A data pattern (levels, including "don't care", up to 50MHz) across the 16 input pins.

In theory up to two edge conditions on two pins could be used, but their transition had to occur in the same 20ns check interval to consider this a match, which limits the practical use of this feature.

Pulse width, event counts, and logic combination of several combinations are not supported in trigger conditions (the hardware does, the software doesn't). External trigger (TO trigger output, TI trigger input) currently isn't supported by the software either.

The device has local memory which can hold up to 14 MiSa (14 million samples) for input signals that keep changing all the time. When input signals don't change for a number of sample points, then hardware supported RLE compression takes effect, and can reduce memory consumption by a factor of up to 8192. Which results in a best case sample memory capacity that spans 128 GiSa (128 billion samples). Rates above 50MHz increase the number of samples taken, but at the same time reduce the number of available channels.

## Example usage

An example that captures from 4 probes, for 100ms at 10MHz, with trigger condition 1:high, 2:rising, 3:low, 4:high.

```
$ **sigrok-cli --driver asix-sigma --config samplerate=10m --wait-trigger \**
  **--triggers 1=1,2=r,3=0,4=1 --output-format bits --probes 1-4 --time 100ms**

```
## Firmware

The firmware files (FPGA bitstreams) for the ASIX SIGMA/SIGMA2 have been provided by the vendor under a [license which allows redistribution](http://sigrok.org/gitweb/?p=sigrok-firmware.git;a=blob;f=asix-sigma/LICENSE.Sigma), and are available from the [sigrok-firmware](http://sigrok.org/gitweb/?p=sigrok-firmware.git) repository. See [Firmware](https://sigrok.org/wiki/Firmware) for installation instructions.

## Differences between SIGMA and SIGMA2

The hardware of SIGMA and SIGMA2 is almost identical, up to few exceptions:

- Seven one-color LEDs were replaced with two two-color LEDs.
- A button was added. It can be used to start, stop, trigger.
- The SIGMA has input TTLs in DIL sockets, SIGMA2 is has input TTLs in SMD package.

The new hardware revision requires the new firmware files to support the button and the different LED wiring. The new firmware is usable for both SIGMA **and** SIGMA2. However, the new hardware revision cannot work with the old firmware files.

## Resources
- [Initial support for Asix Sigma in Sigrok](http://labs.ping.uio.no/2010/04/initial-support-for-asix-sigma-in-sigrok/)
- [PING Labs: Sampi – A Logic Analyzer](http://labs.ping.uio.no/2009/09/sampi-a-logic-analyzer/)
- [flickr: ASIX SIGMA in chlunde's photostream](http://www.flickr.com/photos/chlunde/3383669140/) (photos and more information about the device)

