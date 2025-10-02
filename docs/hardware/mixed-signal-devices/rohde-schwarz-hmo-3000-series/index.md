---
title: Rohde&amp;Schwarz HMO 3000 series
---

# Rohde&amp;Schwarz HMO 3000 series

<div class="infobox" markdown>

### Rohde&amp;Schwarz HMO 3000 series

| | |
|---|---|
| **Status** | supported |
| **Source code** | [hameg-hmo](https://github.com/OpenTraceLab/OpenTraceCapture/tree/main/src/hardware/hameg-hmo) |
| **Channels** | 2 or 4 analog, 16 digital |
| **Samplerate** | 4GSa/s (interleaved), 2GSa/s (non interleaved) |
| **Analog bandwidth** | 300-500MHz (depending on model) |
| **Vertical resolution** | 8 bits (HiRes up to 16 bits) |
| **Triggers** | slope, pulse width, logic, video, risetime, runt, serial bus (optional) |
| **Input impedance** | 1MΩ‖13pF 200Vp CAT I, 50Ω 5V RMS |
| **Memory** | 4 or 8 Mpts (depending on number of channels used) |
| **Display** | 6.5" VGA (640x480), 256 colors |
| **Connectivity** | USB host/device, Ethernet, RS232 (optional), GPIB (optional) |
| **Features** | math (+, —, x, /), FFT, pattern generator, statistics, frequency counter, digital voltmeter, vertical sensitivity: 1mV/div - 5V/div |
| **Website** | [rohde-schwarz.com](https://www.rohde-schwarz.com/uk/product/hmo3000-productstartpage_63493-42344.html) |

</div>

The **Rohde&Schwarz HMO3000 series** are 300-500MHz, 4GSa/s, 2 or 4 analog channels and 16 digital channels mixed-signal oscilloscopes. This series was previously branded Hameg.

The HMO3522 and HMO3524 are an earlier series from Hameg and are also supported by this driver.

All models support different extension modules which provide different connectivity options.

Most models come with a [HO730](https://sigrok.org/wiki/Hameg_HO730) (USB, Ethernet) module, other modules like the [HO720](https://sigrok.org/wiki/Hameg_HO720) (RS232, USB) and the [HO740](/w/index.php?title=Hameg_HO740&action=edit&redlink=1) (GPIB) are available optionally.

All models come with analog probes (specific probe might depend on the scope capabilities).

Digital probes (8 or 16 channels) are optional and can be purchased separately, see [HO3508](https://sigrok.org/wiki/Hameg_HO3508).

The latest available firmware version from the HMO3000 series is V 6.005 (dated 21 April 2017).

The HMO3000 series has been discontinued in the first-half of 2018.

## Devices
| Model | Bandwidth | Analog Channels | Digital Channels |
|---|---|---|---|
| HMO3032 | 300MHz | 2 | 16 |
| HMO3034 | 300MHz | 4 | 16 |
| HMO3042 | 400MHz | 2 | 16 |
| HMO3044 | 400MHz | 4 | 16 |
| HMO3052 | 500MHz | 2 | 16 |
| HMO3054 | 500MHz | 4 | 16 |
| HMO3522 | 350MHz | 2 | 16 |
| HMO3524 | 350MHz | 4 | 16 |

## Protocol

All the devices use the [SCPI](https://sigrok.org/wiki/IEEE-488) protocol (for reference, see the "*SCPI Programmers Manual*").

The serial parameters are configurable on the device, the standard settings are: 115200 baud, 8n1, no handshake, no flow control.

All models support USB connection to the computer in both TMC and VPC mode, as well as Ethernet connection (raw TCP over a user-configurable port).

## Resources
- [Rohde&Schwarz HMO3000 Manuals - official resource page](https://www.rohde-schwarz.com/uk/manual/hmo3000/)
- [Rohde&Schwarz HMO3000 - Latest firmware version (V 6.005)](https://www.rohde-schwarz.com/uk/firmware/hmo3000/)

