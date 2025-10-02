---
title: Logic Shrimp
---

# Logic Shrimp

<div class="infobox" markdown>

![Logic Shrimp](./img/Logic-shrimp-front.png){ .infobox-image }

### Logic Shrimp

| | |
|---|---|
| **Status** | supported |
| **Source code** | [openbench-logic-sniffer](https://github.com/OpenTraceLab/OpenTraceCapture/tree/main/src/hardware/openbench-logic-sniffer) |
| **Channels** | 4 |
| **Samplerate** | 20MHz |
| **Samplerate (state)** | ? |
| **Triggers** | ? |
| **Min/max voltage** | ? |
| **Memory** | 256ksamples per channel |
| **Compression** | ? |
| **Website** | [dangerousprototypes.com](http://dangerousprototypes.com/docs/Logic_Shrimp_logic_analyzer) |

</div>

The **Dangerous Prototypes Logic Shrimp** is a USB-based, 4-channel logic analyzer with up to 20MHz sampling rate.

The hardware design is available under a Creative Commons (CC-BY-SA) license.

See [Logic Shrimp/Info](https://sigrok.org/wiki/Logic_Shrimp/Info) for more details (such as **lsusb -v** output) about the device.

## Hardware
- **8-bit microcontroller with integrated USB Full-Speed support**: [Microchip PIC18F24J50](http://www.microchip.com/wwwproducts/Devices.aspx?dDocName=en534039) ([datasheet](http://ww1.microchip.com/downloads/en/DeviceDoc/39931d.pdf))
- 4x **32kByte SPI-attached SRAM**: [Microchip 23K256I](http://www.microchip.com/wwwproducts/Devices.aspx?dDocName=en539039) ([datasheet](http://ww1.microchip.com/downloads/en/DeviceDoc/22100F.pdf))
- **Octal transparent D-type latches with 3-state output**: [Texas Instruments SN74LVC573A](http://www.ti.com/product/sn74lvc573a) ([datasheet](http://www.ti.com/lit/gpn/sn74lvc573a))
- 20MHz crystal

The device essentially consists of a Microchip PIC microcontroller running at 20MHz, sampling each of its 4 probes into its own 256kBit (32kByte) SRAM chip. A buffer chip makes the design 5V tolerant.

## Photos

<div class="photo-grid" markdown>

[![Logic Shrimp Front](./img/Logic-shrimp-front.png)](./img/Logic-shrimp-front.png "Logic Shrimp Front"){ .glightbox data-gallery="logic-shrimp" }
<span class="caption">Logic Shrimp Front</span>

[![Logic Shrimp Back](./img/Logic-shrimp-back.png)](./img/Logic-shrimp-back.png "Logic Shrimp Back"){ .glightbox data-gallery="logic-shrimp" }
<span class="caption">Logic Shrimp Back</span>

</div>
## Protocol

The Logic Shrimp uses the [extended SUMP protocol](http://dangerousprototypes.com/docs/The_Logic_Sniffer%27s_extended_SUMP_protocol), as used by the [Openbench Logic Sniffer](https://sigrok.org/wiki/Openbench_Logic_Sniffer) driver. It is thus supported in sigrok out of the box. However, the current firmware in the Logic Shrimp does not properly publish metadata according to its capabilities. In order to get valid data from it, make sure to always restrict the probes sampled to 1-4.

## Resources
- [Logic Shrimp logic analyzer](http://dangerousprototypes.com/docs/Logic_Shrimp_logic_analyzer) (main wiki page)
- [Logic Shrimp forum](http://dangerousprototypes.com/forum/viewforum.php?f=58)

