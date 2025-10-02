---
title: Keysight 34465A
---

# Keysight 34465A

<div class="infobox" markdown>

![Keysight 34465A](./img/Keysight-34465a-back.jpg){ .infobox-image }

### Keysight 34465A

| | |
|---|---|
| **Status** | supported |
| **Source code** | [scpi-dmm](https://github.com/OpenTraceLab/OpenTraceCapture/tree/main/src/hardware/scpi-dmm) |
| **Counts** | 1200000 |
| **IEC 61010-1** | CAT II (300V) |
| **Connectivity** | LAN LXI, USB TMC, optional GPIB |
| **Measurements** | voltage, current, resistance, capacitance, diode, frequency, period, continuity, temperature, DC ratio |
| **Features** | autorange, true RMS, data hold, min/max/avg/sdev, relative, four-wire resistance, dual display, bargraph, trend, histogram, front/rear terminals, external trigger |
| **Website** | [keysight.com](https://www.keysight.com/de/pdx-2891457-pn-34465A/digital-multimeter-6-digit-truevolt-dmm) |

</div>

The **Keysight 34465A** is a 1200000 counts (6.5 digits), 0.003% (30ppm) accuracy, 5000 readings per second, CAT II (300V), benchtop digital multimeter with LAN and USB connectivity. GPIB interface, higher rates and deeper memory, enhanced math/digitizing/triggers are optional.

See [Keysight 34465A/Info](https://sigrok.org/wiki/Keysight_34465A/Info) for more details (such as **lsusb -v** output) about the device.

The Keysight 34465A meter is a member of the Truevolt series, and is considered a replacement for the previous 34410A/34411A models.

## Hardware

TODO

## Photos

<div class="photo-grid" markdown>

[![Keysight 34465a Back](./img/Keysight-34465a-back.jpg)](./img/Keysight-34465a-back.png "Keysight 34465a Back"){ .glightbox data-gallery="keysight-34465a" }
<span class="caption">Keysight 34465a Back</span>

[![Keysight 34465a Mugshot](./img/Keysight-34465a-mugshot.jpg)](./img/Keysight-34465a-mugshot.png "Keysight 34465a Mugshot"){ .glightbox data-gallery="keysight-34465a" }
<span class="caption">Keysight 34465a Mugshot</span>

[![Keysight 34465a Front](./img/Keysight-34465a-front.jpg)](./img/Keysight-34465a-front.png "Keysight 34465a Front"){ .glightbox data-gallery="keysight-34465a" }
<span class="caption">Keysight 34465a Front</span>

</div>
## Protocol

SCPI-1999, IEEE-488.2, 34401A compatible

## Usage

Some initial support got added to mainline, covering the most basic modes.  Full support for the device's feature set is yet to get done.

Scan for connected devices:

```
 $ **sigrok-cli -d scpi-dmm --scan**
 $ **sigrok-cli -d scpi-dmm:conn=usbtmc/2a8d.0101 --scan**
 $ **sigrok-cli -d scpi-dmm:conn=usbtmc/3.21 --scan**

```

See the [Agilent 34405A](https://sigrok.org/wiki/Agilent_34405A) device page for other **scpi-dmm** examples.

## Resources
- [vendor product page](https://www.keysight.com/de/pdx-2891457-pn-34465A/digital-multimeter-6-digit-truevolt-dmm) with links to the data sheet, user manual, programmer's guide, application notes

