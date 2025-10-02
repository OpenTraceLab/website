---
title: GW Instek GPD series
---

# GW Instek GPD series

<div class="infobox" markdown>

![GW Instek GPD series](./img/Gwinstek-gpd-3303s.jpg){ .infobox-image }

### GW Instek GPD series

| | |
|---|---|
| **Status** | supported |
| **Source code** | [gwinstek-gpd](https://github.com/OpenTraceLab/OpenTraceCapture/tree/main/src/hardware/gwinstek-gpd) |
| **Channels** | 2/3/4 |
| **Voltage/current (CH1)** | 0-30V / 0-3A |
| **Voltage/current (CH2)** | 0-30V / 0-3A |
| **Voltage/current (CH3)** | various |
| **Voltage/current (CH4)** | various |
| **Connectivity** | USB/serial |
| **Features** | memory save/recall, key lock |
| **Website** | [gwinstek.com](https://www.gwinstek.com/en-US/products/detail/GPD-Series) |

</div>

The **GW Instek GPD series** are 2/3/4 channel programmable linear DC power supplies with USB/serial connectivity.

## Devices
| Device | Channels | Voltage range | Current range | Power |
|---|---|---|---|---|
| [GPD-2303S](https://sigrok.org/wiki/GW_Instek_GPD-2303S) | 2 | 0-30 V, 0-30 V | 0-3 A, 0-3 A | 180 W |
| [GPD-3303S](https://sigrok.org/wiki/GW_Instek_GPD-3303S) | 3 | 0-30 V, 0-30 V, 2.5/3.3/5.0 V | 0-3 A, 0-3 A, 0-3 A | 195 W |
| GPD-4303S | 4 | 0-30 V, 0-30 V, 0-5 V or 5-10 V, 0-5 V | 0-3 A, 0-3 A, 0-3 A or 0-1 A, 0-1 A | 195 W |
| GPD-3303D | 3 | 0-30 V, 0-30 V, 2.5/3.3/5.0 V | 0-3 A, 0-3 A, 0-3 A | 195 W |

So far, only the GPD-2303S is supported and tested. Adding support for the other devices should be relatively easy for someone with hardware access, though. Patches welcome!

## Hardware

There was two hardware revisions (versions) of these units released. Model numbes did not change so it is difficult to
determine whether unit is the "old" or "new" hardware revision.
However, at least on GPD-3303S there is slight change to unit front panels;
older units have slight space in output jacks between "CH1" and "FIXED" channel, while newer units have even spacing.

It would appear that older hardware revision units have firmware version < v2.00, but this has not been confirmed (based on anecdotal evidence only).

## Protocol

These units use SCPI like command protocol. However, units do not implement all mandatory SCPI commands.

There appears to be difference in the protocol between old and new hardware revision units.
Output from STATUS? command differs:

| Bit | New Units | Old Units |
|---|---|---|
| 0 | CH1 (0=CC, 1=CV) |
| 1 | CH2 (0=Cc, 1=CV) |
| 2,3 | Tracking (01=Independent, 11=Series, 10=Parallel) |
| 4 | Beep (0=OFF, 1=ON) |
| 5 | Output (0=OFF, 1=ON) | N/A |
| 6 | Baud (00=115200, 01=57600, 00=9600) | Output (0=OFF, 1=ON) |
| 7 | N/A |

Example output to *STATUS? command:

Old units:

```
0 0 0 1 0 X 0 X  
bit0:(CH1)0=CC,1=CV;bit1:(CH2)0=CC,1=CV;bit23=(TRACK)01=INDEP,11=SER,10=PAR;
bit4:(BEEP)0=OFF,1=ON;bit6:(OUT)0=OFF,1=ON;

```

New units:

```
0 0 0 1 0 0 0 0

```

See the [vendor user manual](https://www.gwinstek.com/en-US/products/downloadSeriesDownNew/7840/1477) for more details.

## Resources
- [Specification](https://www.gwinstek.com/en-US/products/downloadSeriesSpec/1479) (PDF)
- [Downloads](https://www.gwinstek.com/en-US/products/detail/GPD-Series) (datasheet, user manuals, drivers, vendor software)

## Photos

<div class="photo-grid" markdown>

[![Gwinstek Gpd 3303s](./img/Gwinstek-gpd-3303s.jpg)](./img/Gwinstek-gpd-3303s.png "Gwinstek Gpd 3303s"){ .glightbox data-gallery="gw-instek-gpd-series" }
<span class="caption">Gwinstek Gpd 3303s</span>

</div>
