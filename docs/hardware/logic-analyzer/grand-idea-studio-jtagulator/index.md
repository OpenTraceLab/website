---
title: Grand Idea Studio JTAGulator
---

# Grand Idea Studio JTAGulator

<div class="infobox" markdown>

![Grand Idea Studio JTAGulator](./img/Jtagulator-annotated.jpg){ .infobox-image }

### Grand Idea Studio JTAGulator

| | |
|---|---|
| **Status** | supported |
| **Source code** | [openbench-logic-sniffer](https://github.com/OpenTraceLab/OpenTraceCapture/tree/main/src/hardware/openbench-logic-sniffer) |
| **Channels** | 24 |
| **Samplerate** | 1.2MHz |
| **Samplerate (state)** | — |
| **Triggers** | 4 |
| **Min/max voltage** | 1.4 - 3.3V |
| **Memory** | 1024 samples |
| **Compression** | none |
| **Website** | [jtagulator.com](http://jtagulator.com/) |

</div>

The **Grand Idea Studio JTAGulator** is a tool to identify interfaces.
It also supports a logic analyzer mode, and can thus be used to capture signals.
See the vendor's [logic analyzer mode wiki page](https://github.com/grandideastudio/jtagulator/wiki/Logic-Analyzer) for details.

See [JTAGulator/Info](https://sigrok.org/wiki/JTAGulator/Info) for lsusb details and SUMP metadata.

## Hardware
- Parallax Propeller P8X32A
- FTDI FT232RL
- TI TXS0108EPWR

## Photos

<div class="photo-grid" markdown>

[![Jtagulator Annotated](./img/Jtagulator-annotated.jpg)](./img/Jtagulator-annotated.jpg "Jtagulator Annotated"){ .glightbox data-gallery="grand-idea-studio-jtagulator" }
<span class="caption">Jtagulator Annotated</span>

[![Jtagulator Transparent](./img/Jtagulator-transparent.jpg)](./img/Jtagulator-transparent.png "Jtagulator Transparent"){ .glightbox data-gallery="grand-idea-studio-jtagulator" }
<span class="caption">Jtagulator Transparent</span>

</div>
## Protocol

JTAGulator (in logic analyzer mode) implements the ["extended SUMP" protocol](https://sigrok.org/wiki/Openbench_Logic_Sniffer#Protocol).

## Resources
- [vendor's main wiki page](https://github.com/grandideastudio/jtagulator/wiki)
- [vendor's logic analyzer mode wiki page](https://github.com/grandideastudio/jtagulator/wiki/Logic-Analyzer)

