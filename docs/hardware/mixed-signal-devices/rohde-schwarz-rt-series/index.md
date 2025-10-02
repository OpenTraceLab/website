---
title: Rohde&amp;Schwarz RT series
---

# Rohde&amp;Schwarz RT series

<div class="infobox" markdown>

### Rohde&amp;Schwarz RT series

| | |
|---|---|
| **Status** | supported |
| **Source code** | [hameg-hmo](https://github.com/OpenTraceLab/OpenTraceCapture/tree/main/src/hardware/hameg-hmo) |
| **Channels** | 2 or 4 analog, 8 or 16 digital |
| **Samplerate** | 2-5GSa/s |
| **Analog bandwidth** | 50MHz-1GHz (depending on model) |
| **Vertical resolution** | 8 bits (HiRes up to 16 bits) |
| **Triggers** | slope, pulse width, logic, video, risetime, runt, serial bus (optional) |
| **Input impedance** | 1MΩ‖13pF 200Vp CAT I, 50Ω 5V RMS |
| **Memory** | 2-200 Mpts (depending on model and number of channels used) |
| **Display** | depends on model |
| **Connectivity** | USB host/device, Ethernet, RS232 (optional), GPIB (optional) |
| **Features** | math (+, —, x, /), FFT, pattern generator, statistics, frequency counter, digital voltmeter, vertical sensitivity: 1mV/div - 5V/div |
| **Website** | [[1]](https://www.rohde-schwarz.com/uk/products/test-and-measurement/oscilloscopes/overview_63663.html) |

</div>

The **Rohde&Schwarz RT series** actually consists of multiple series such as: RTC, RTB, RTM and RTA. The several different models are 50MHz-1GHz, 2-5GSa/s, 2 or 4 analog channels and 8 or 16 digital channels mixed-signal oscilloscopes.

All models support different extension modules which provide different connectivity options.

All models come with analog probes (specific probe might depend on the scope capabilities).

Digital probes (8 or 16 channels) are optional and can be purchased separately.

## Devices
| Model | Bandwidth | Analog Channels | Digital Channels |
|---|---|---|---|
| RTC1000 | 50-300MHz | 2 | 8 |
| RTB2000 | 70-300MHz | 2/4 | 16 |
| RTM3000 | 100MHz-1GHz | 2/4 | 16 |
| RTA4000 | 200MHz-1GHz | 4 | 16 |

## Protocol

All the devices use the [SCPI](https://sigrok.org/wiki/IEEE-488) protocol (for reference, see the "*SCPI Programmers Manual*").

The serial parameters are configurable on the device, the standard settings are: 115200 baud, 8n1, no handshake, no flow control.

All models support USB connection to the computer in both TMC and VPC mode, as well as Ethernet connection (raw TCP over a user-configurable port).

## Resources
- [RTC1000 - official resource page](https://www.rohde-schwarz.com/uk/product/rtc1000-productstartpage_63493-515585.html)
- [RTB2000 - official resource page](https://www.rohde-schwarz.com/uk/product/rtb2000-productstartpage_63493-266306.html)
- [RTM3000 - official resource page](https://www.rohde-schwarz.com/uk/product/rtm3000-productstartpage_63493-427459.html)
- [RTA4000 - official resource page](https://www.rohde-schwarz.com/uk/product/rta4000-productstartpage_63493-458432.html)

