---
title: PeakTech 4370
---

# PeakTech 4370

<div class="infobox" markdown>

![PeakTech 4370](./img/Peaktech_4370_device_front.jpg){ .infobox-image }

### PeakTech 4370

| | |
|---|---|
| **Status** | supported |
| **Source code** | [serial-dmm](https://github.com/OpenTraceLab/OpenTraceCapture/tree/main/src/hardware/serial-dmm) |
| **Counts** | 2000 |
| **IEC 61010-1** | CAT II (1000V) |
| **Connectivity** | RS232 |
| **Measurements** | voltage, current, frequency, hFE, logic, continuity, diode, resistance, temperature, capacitance |
| **Features** | data hold, min/max, 10 reading memory |

</div>

The **PeakTech 4370** is a 2000 counts, CAT II (1000V) handheld digital multimeter with RS232 connectivity.

This is a rebadged [Metex M-3640D](http://web.archive.org/web/20090221062108/http://imetex.com/html/product/product_model_detail.asp?idx=19) multimeter.

## Hardware
- **3 1/2 digit ADC with bandgap reference**: [Maxim MAX130CPL](http://www.maxim-ic.com/datasheet/index.mvp/id/1288) ([datasheet](http://datasheets.maxim-ic.com/en/ds/MAX130-MAX131.pdf)) (marking: "Maxim MAX130CPL 0138-3 C10039")
- **?**: Metex KS57C2016 (possibly a Samsung KS57C2016 4-bit microcontroller with custom Metex firmware?) (marking: "Metex 95D3 KS57C2016-13 013D 95D3")
- **?**: 4.1856MHz crystal (?)
- **?**: 14027B PBD005
- **?**: 2x 0138 817B Y
- **?**: OP-07 1035B JRC
- **?**: [Intersil ICM7555CBA](http://www.intersil.com/content/intersil/en/products/timing-and-digital/counters-time-base-ics/counter-time-base-ics/ICM7555.html) ([datasheet](http://www.intersil.com/content/dam/Intersil/documents/fn28/fn2867.pdf)) (marking: "7555 CBA P136FAM")
- **Quad analog switch/quad multiplexer**: [ON Semiconductor 14066B](http://www.onsemi.com/PowerSolutions/product.do?id=MC14066B) ([datasheet](http://www.onsemi.com/pub/Collateral/MC14066B-D.PDF)) (marking: "14066B PBV139")
- **?**: New Japan Radio (JRC) NJU4011B (marking: "NJU4011B JRC A1015H")
- **Low level, True RMS-to-DC converter**: [Analog Devices AD636JH](http://www.analog.com/en/special-linear-functions/rms-to-dc-converters/ad636/products/product.html) ([datasheet](http://www.analog.com/static/imported-files/data_sheets/AD636.pdf)) (marking: "AD 636JH 0122")

## Photos

<div class="photo-grid" markdown>

[![Peaktech 4370 Device Front](./img/Peaktech_4370_device_front.jpg)](./img/Peaktech_4370_device_front.png "Peaktech 4370 Device Front"){ .glightbox data-gallery="peaktech-4370" }
<span class="caption">Peaktech 4370 Device Front</span>

</div>
## Protocol

See [Multimeter_ICs#Metex_14-byte_ASCII](https://sigrok.org/wiki/Multimeter_ICs#Metex_14-byte_ASCII).

## Resources

TODO.

