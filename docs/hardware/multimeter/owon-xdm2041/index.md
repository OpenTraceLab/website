---
title: Owon XDM2041
---

# Owon XDM2041

<div class="infobox" markdown>

![Owon XDM2041](./img/Owon_XDM2041.JPG){ .infobox-image }

### Owon XDM2041

| | |
|---|---|
| **Status** | in progress |
| **Source code** | [scpi-dmm](https://github.com/OpenTraceLab/OpenTraceCapture/tree/main/src/hardware/scpi-dmm) |
| **Counts** | 55000 |
| **IEC 61010-1** | CAT I (1000V) / CAT II (600V) |
| **Connectivity** | RS232 |
| **Measurements** | voltage, current, resistance, capacitance, diode, frequency, continuity, temperature |
| **Features** | autorange, true RMS, data hold, min/max/avg, relative, four-wire resistance, dual display, record |
| **Website** | [owon.com.hk](https://www.owon.com.hk/) |

</div>

The Owon XDM2041 is a 55000 count (4.5 digits), 0.025% accuracy, 65 readings/s benchtop digital multimeter with RS232 connectivity.

Also sold rebranded as [PeakTech 4095](https://www.peaktech.de/productdetail/kategorie/digital---tischmultimeter/produkt/peaktech-4095.html).

## Protocol

Protocol is SCPI over RS232. Manufacturer manual is available here: [Programming manual for XDM2041 Digital Multimeter](http://files.owon.com.cn/probook/XDM2041_Digital_Multimeter_Programming_Manual.pdf).

Notes:

- The XDM2041 does not support ***OPC?** command, which SCPI standard specifies should report whether operation is complete.
- The programming manual does not specify how to run / stop measurement.
- The programming manual does not specify how to retrieve recorded data or how to configure one.

There is Windows software available that could be used to check whether there are extra commands.

## Hardware

There is reverse-engineered information available on the [Owon XDM2041 hardware ](https://github.com/PetteriAimonen/owon-xdm2041-info/).

## Photos

<div class="photo-grid" markdown>

[![Owon Xdm2041](./img/Owon_XDM2041.JPG)](./img/Owon_XDM2041.JPG "Owon Xdm2041"){ .glightbox data-gallery="owon-xdm2041" }
<span class="caption">Owon Xdm2041</span>

</div>
