---
title: Envox EEZ Bench Box 3
---

# Envox EEZ Bench Box 3

<div class="infobox" markdown>

![Envox EEZ Bench Box 3](./img/Envox_eez_bb3_enclosure_prototype.jpg){ .infobox-image }

### Envox EEZ Bench Box 3

| | |
|---|---|
| **Status** | supported |
| **Source code** | [scpi-pps](https://github.com/OpenTraceLab/OpenTraceCapture/tree/main/src/hardware/scpi-pps) |
| **Channels** | up to 6, depending on installed modules |
| **Connectivity** | SCPI over USB serial or TCP |
| **Website** | [www.envox.eu](https://www.envox.eu) |

</div>

The *Envox EEZ Bench Box 3* (or "BB3") is an open hardware and open source platform design intended to support various modular test equipment modules, with an emphasis (at least, for now) on power supply use-cases.

At the time of writing, [BB3 kits are available on Crowd Supply](https://www.crowdsupply.com/envox/eez-bb3), and the project page also serves as a summary/overview of the features and design of this equipment.

## Hardware

Due to being an open hardware design, there is comprehensive documentation of all of the hardware on [the project website](https://www.envox.eu/eez-bb3/).

The system is designed as a modular platform which can support a number of different components of different kinds. Each of the modules might present a different sort of functionality as far as Sigrok is concerned. However, the power supply components behave similarly to those in the BB3's predecessor, the [EEZ H24005](https://sigrok.org/wiki/Envox_EEZ_H24005), and so the power supply functionality can share a common Sigrok driver as long as it's designed to dynamically configure itself based on the device capabilities.

With the available modules specified at the time of writing, up to six independently-controllable power supply channels are possible if all three of the module slots are populated with dual power supply modules.

## Protocol

The EEZ BB3 has a SCPI-based protocol available either over USB Serial or over TCP/IP on the device's Ethernet port. The project website has [a comprehensive guide to the SCPI implementation](https://www.envox.eu/eez-bench-box-3/bb3-scpi-reference-manual/bb3-scpi-introduction/).

The SCPI protocol is compatible with that of the BB3's predecessor, the [EEZ H24005](https://sigrok.org/wiki/Envox_EEZ_H24005), and so it's possible to share a protocol implementation across both platforms in the `scpi-pps` driver, as long as the implementation probes the device for how many channels it has and what their individual capabilities are.

There is [an online simulator](https://www.envox.eu/web-simulator/) which allows exercising both the touch user interface and the SCPI port. The simulator is an emscripten build of a variant of the real system firmware, so its behavior is pretty realistic aside from (of course) having just a software model of the power supply module behavior.

## Sigrok Support

The part of the sigrok `scpi-pps` driver which implements EEZ PSU support was provided by [User:Apparentlymart](https://sigrok.org/wiki/User:Apparentlymart). It was tested with a genuine [the EEZ H24005](https://sigrok.org/wiki/Envox_EEZ_H24005), and written to current documentation and tested with simulated BB3 devices.

## See also
- [Programmable power supply](https://sigrok.org/wiki/Programmable_power_supply)
- [Power supply comparison](https://sigrok.org/wiki/Power_supply_comparison)

## Photos

<div class="photo-grid" markdown>

[![Envox Eez Bb3 Enclosure Prototype](./img/Envox_eez_bb3_enclosure_prototype.jpg)](./img/Envox_eez_bb3_enclosure_prototype.jpg "Envox Eez Bb3 Enclosure Prototype"){ .glightbox data-gallery="envox-eez-bench-box-3" }
<span class="caption">Envox Eez Bb3 Enclosure Prototype</span>

</div>
