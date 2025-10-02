---
title: Voltcraft M-4650CR
---

# Voltcraft M-4650CR

<div class="infobox" markdown>

![Voltcraft M-4650CR](./img/Voltcraft_m4650cr.jpg){ .infobox-image }

### Voltcraft M-4650CR

| | |
|---|---|
| **Status** | supported |
| **Source code** | [serial-dmm](https://github.com/OpenTraceLab/OpenTraceCapture/tree/main/src/hardware/serial-dmm) |
| **Counts** | 20000 |
| **IEC 61010-1** | — |
| **Connectivity** | RS232 |
| **Measurements** | voltage, current, hFE, logic, capacitance, frequency, resistance, continuity, diode |
| **Features** | hold, relative, min/max, bargraph |
| **Website** | [conrad.de](http://www.conrad.de) |

</div>

The **Voltcraft M-4650CR** is a 20,000 counts, handheld digital multimeter with RS232 connectivity.

It is a rebadged [Metex M-4650CR](https://sigrok.org/wiki/Metex_M-4650CR).

## Hardware

**Multimeter**:

- **Main IC**: Metex 89CR (markings: "Metex 89CR 1146 1G1")
- **8-line to 3-line priority encoder**: 2x 74HC148A (markings: "T 91 16H 74HC148A")
- 2x CD4010BE
- T 91 05H 74HC08A
- M 14027B XXEW045
- M 14512B XXGF111
- TC 7129CKW 9129BCJ
- 2x B6 LTV817
- **Fuse**: 2A/250V fast (5x20mm) (for the A jack; the 20A jack is unfused!)

**RS232 cable**:

- See [Device_cables#Metex_5-pin_RS232_cable](https://sigrok.org/wiki/Device_cables#Metex_5-pin_RS232_cable).

## Photos

<div class="photo-grid" markdown>

[![Voltcraft M4650cr](./img/Voltcraft_m4650cr.jpg)](./img/Voltcraft_m4650cr.png "Voltcraft M4650cr"){ .glightbox data-gallery="voltcraft-m-4650cr" }
<span class="caption">Voltcraft M4650cr</span>

[![Metex M 4650cr Display](./img/METEX_M-4650CR_Display.jpg)](./img/METEX_M-4650CR_Display.jpg "Metex M 4650cr Display"){ .glightbox data-gallery="voltcraft-m-4650cr" }
<span class="caption">Metex M 4650cr Display</span>

</div>
## Protocol

See [Multimeter ICs#Alternative_Protocol](https://sigrok.org/wiki/Multimeter_ICs#Alternative_Protocol).

| Baud | Databits | Stoppbits | Parity | Hard.-hands. | Soft.-hands. | DTR | RTS |
|---|---|---|---|---|---|---|---|
| 1200 | 7 | 2 | no | no | no | enable | disable |

## Resources
- [Calibration instructions](http://www.produktinfo.conrad.com/datenblaetter/125000-149999/126110-an-01-de-DMM4650CR_Kalibrieranleitung.pdf)
- [Manual](http://www.produktinfo.conrad.com/datenblaetter/125000-149999/126110-an-01-ru-DMM4650CR.pdf) (Russian)
- [reinhardweiss.de: DMM info](http://www.reinhardweiss.de/german/metex.htm)
- [gerald-gradl.de: DMM info](http://web.archive.org/web/20061018045026/http://www.gerald-gradl.de/eprojects/multi/body_multi.html)

