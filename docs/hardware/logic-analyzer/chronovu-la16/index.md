---
title: ChronoVu LA16
---

# ChronoVu LA16

<div class="infobox" markdown>

![ChronoVu LA16](./img/Chronovu_la16.png){ .infobox-image }

### ChronoVu LA16

| | |
|---|---|
| **Status** | supported |
| **Source code** | [chronovu-la](https://github.com/OpenTraceLab/OpenTraceCapture/tree/main/src/hardware/chronovu-la) |
| **Channels** | 16 |
| **Samplerate** | 200MHz |
| **Samplerate (state)** | — |
| **Triggers** | high/low/any state, rising/falling/any edge |
| **Min/max voltage** | -0.5 — 6V |
| **Threshold voltage** | Fixed: VIH=2V—5.5V, VIL=0V—0.8V |
| **Memory** | 8Mbyte (SDRAM) |
| **Compression** | none |
| **Website** | [chronovu.com](http://www.chronovu.com/) |

</div>

The **ChronoVu LA16** is a USB-based 16-channel logic analyzer with up to 200MHz sampling rate.  See [ChronoVu LA8](https://sigrok.org/wiki/ChronoVu_LA8) for an 8 channel version.

It features a Xilinx FPGA for sampling, 8MByte of built-in SDRAM to store the samples, and can trigger on low/high/any state or rising/falling/any edge of any combination of probes. After the 8MByte sample buffer is full, the data is transferred to the host via an FTDI FT245RL chip.

See [ChronoVu LA16/Info](https://sigrok.org/wiki/ChronoVu_LA16/Info) for more details (such as **lsusb -v** output) about the device.

Many thanks to the vendor ([ChronoVu](http://www.chronovu.com/)) for freely providing information on the protocol used to communicate with the device. This helped us implement the libsigrok hardware driver more quickly. We're happy to see more open-source friendly vendors support sigrok!

## Hardware
- Xilinx XC3S50AN
- Micron MT48LC2M32B2 SDRAM (8 MByte)
- FTDI FT245RL
- ...

## Photos

<div class="photo-grid" markdown>

[![Chronovu La16](./img/Chronovu_la16.png)](./img/Chronovu_la16.png "Chronovu La16"){ .glightbox data-gallery="chronovu-la16" }
<span class="caption">Chronovu La16</span>

</div>
## Protocol

Similar to the [ChonoVu LA8 protocol](https://sigrok.org/wiki/ChronoVu_LA8#Protocol), more info will follow.

## Resources
- [Manual](http://www.chronovu.com/downloads/ReadMeFile%20LA16-4.00.pdf)
- [Vendor FAQ](http://www.chronovu.com/help/docs/faq/)
- [Vendor software](http://www.chronovu.com/download/)

