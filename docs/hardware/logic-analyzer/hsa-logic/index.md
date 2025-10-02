---
title: HSA Logic
---

# HSA Logic

<div class="infobox" markdown>

![HSA Logic](./img/Hsa-logic_back.jpg){ .infobox-image }

### HSA Logic

| | |
|---|---|
| **Status** | planned |
| **Source code** | [hardware/hsa-tple](https://github.com/OpenTraceLab/OpenTraceCapture/tree/main/src/hardware/hardware/hsa-tple) |
| **Channels** | 8 (24 planned) |
| **Samplerate** | 6.25 MHz |
| **Samplerate (state)** | ? |
| **Triggers** | none (SW-only) |
| **Min/max voltage** | 3.3V; 5.0V |
| **Threshold voltage** | ? |
| **Memory** | 1 MB (245K*16), 262144 samples |
| **Compression** | RLE |
| **Website** | [trac](https://io.informatik.fh-augsburg.de/trac/Logikanalysator/), [project page](https://io.informatik.fh-augsburg.de/projekte/Logikanalysator), [hhwiki](http://elk.informatik.fh-augsburg.de/hhwiki/Logikanalysator) |

</div>

The **HSA Logic** is a USB-based, 8-channel logic analyzer with 6.25 MHz sampling rate. It is an open-hardware / open-source design. Both hardware and software have been developed at [Hochschule Augsburg](http://www.hs-augsburg.de) so far. Everything started with [this bachelor thesis](http://hhoegl.informatik.fh-augsburg.de/da/ba-1/USB-TPLE/Documentation/Latex_Thesis/main.pdf) in 2010. It was continued in 2013/14 as semester project.

## Hardware
- CPLD: Altera Max II EPM240 with 240 logic elements
- microcontroller: Atmel ATmega32u4 (programmed in C)
- 2x RAM organised as 256K*16
- I/O drivers supporting 5V and 3V as input voltage

## Photos

<div class="photo-grid" markdown>

[![Hsa Logic Back](./img/Hsa-logic_back.jpg)](./img/Hsa-logic_back.jpg "Hsa Logic Back"){ .glightbox data-gallery="hsa-logic" }
<span class="caption">Hsa Logic Back</span>

[![Hsa Logic](./img/Hsa-logic.png)](./img/Hsa-logic.png "Hsa Logic"){ .glightbox data-gallery="hsa-logic" }
<span class="caption">Hsa Logic</span>

[![Hsa Logic Front](./img/Hsa-logic_front.jpg)](./img/Hsa-logic_front.jpg "Hsa Logic Front"){ .glightbox data-gallery="hsa-logic" }
<span class="caption">Hsa Logic Front</span>

</div>
## Firmware

CPLD Firmware: written in VHDL,
microcontroller Firmware: written in C (using LUFA)
TODO.

## Protocol

For the sake of simplicity all commands and status messages have been implemented as simple ASCII tokens (single characters).

### Commands
| Command | Description |
|---|---|
| 'g' | = go, start sampling |
| 's' | = stop sampling |
| 'r' | = reset |
| 'd' | = dump data (binary) |
| 'D' | = dump data (ASCII encoded) |
| 'i' | = identify |
| 'S' | = get status |

### Status messages
| Command | Description |
|---|---|
| 'r' | = measurement is running |
| 's' | = measurement stopped/ no measurement |
| 'f' | = memory is full |

### Data format

The samples are blocks of 32 bit: 8 bit data, 16 bit timestamp, 8 bit status. These can be read via the dump command.
The analyzer only stores new samples if any logic level changes.

## Resources

TODO.

