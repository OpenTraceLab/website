---
title: Gossen Metrawatt T-Com KMM2002
---

# Gossen Metrawatt T-Com KMM2002

<div class="infobox" markdown>

![Gossen Metrawatt T-Com KMM2002](./img/Gmc_kmm2002_logo.png){ .infobox-image }

### Gossen Metrawatt T-Com KMM2002

| | |
|---|---|
| **Status** | supported |
| **Source code** | [gmc-mh-1x-2x](https://github.com/OpenTraceLab/OpenTraceCapture/tree/main/src/hardware/gmc-mh-1x-2x) |
| **Counts** | 3100 (31000) |
| **IEC 61010-1** | CAT II 1000 V |
| **Connectivity** | Infrared (RS232) |
| **Measurements** | voltage, current, resistance, capacitance, temperature, diode, continuity |
| **Features** | autorange, data hold, bargraph, backlight |
| **Website** | [[1]](http://www.gossenmetrawatt.com/english/produkte/metrahit16t.htm) |

</div>

The **[Gossen Metrawatt](https://sigrok.org/wiki/Gossen_Metrawatt) T-Com KMM2002** is a 3100 counts handheld digital multimeter with IR (RS232) connectivity and insulation measurement (100 V). It seems to be an OEM version of the *Metrahit 16T* especially made for T-Com (Deutsche Telekom). Additional features seems to be a backlight and a 30 nF capacity range.

The resolution is one digit higher on the data interface.

## Hardware
- **Battery**:  *9 V IEC 6 LR 61*
- **Fuse**: None! (not required, no internal amps ranges)
- TODO.

## Photos

<div class="photo-grid" markdown>

[![Gmc Kmm2002 Logo](./img/Gmc_kmm2002_logo.png)](./img/Gmc_kmm2002_logo.png "Gmc Kmm2002 Logo"){ .glightbox data-gallery="gossen-metrawatt-t-com-kmm2002" }
<span class="caption">Gmc Kmm2002 Logo</span>

[![Gmc Kmm2002 6](./img/Gmc_kmm2002_6.jpg)](./img/Gmc_kmm2002_6.jpg "Gmc Kmm2002 6"){ .glightbox data-gallery="gossen-metrawatt-t-com-kmm2002" }
<span class="caption">Gmc Kmm2002 6</span>

[![Gmc Kmm2002 1](./img/Gmc_kmm2002_1.jpg)](./img/Gmc_kmm2002_1.png "Gmc Kmm2002 1"){ .glightbox data-gallery="gossen-metrawatt-t-com-kmm2002" }
<span class="caption">Gmc Kmm2002 1</span>

[![Gmc Kmm2002 2](./img/Gmc_kmm2002_2.jpg)](./img/Gmc_kmm2002_2.jpg "Gmc Kmm2002 2"){ .glightbox data-gallery="gossen-metrawatt-t-com-kmm2002" }
<span class="caption">Gmc Kmm2002 2</span>

[![Gmc Kmm2002 5](./img/Gmc_kmm2002_5.jpg)](./img/Gmc_kmm2002_5.jpg "Gmc Kmm2002 5"){ .glightbox data-gallery="gossen-metrawatt-t-com-kmm2002" }
<span class="caption">Gmc Kmm2002 5</span>

[![Gmc Kmm2002 7](./img/Gmc_kmm2002_7.jpg)](./img/Gmc_kmm2002_7.jpg "Gmc Kmm2002 7"){ .glightbox data-gallery="gossen-metrawatt-t-com-kmm2002" }
<span class="caption">Gmc Kmm2002 7</span>

[![Gmc Kmm2002 4](./img/Gmc_kmm2002_4.jpg)](./img/Gmc_kmm2002_4.jpg "Gmc Kmm2002 4"){ .glightbox data-gallery="gossen-metrawatt-t-com-kmm2002" }
<span class="caption">Gmc Kmm2002 4</span>

[![Gmc Kmm2002 3](./img/Gmc_kmm2002_3.jpg)](./img/Gmc_kmm2002_3.jpg "Gmc Kmm2002 3"){ .glightbox data-gallery="gossen-metrawatt-t-com-kmm2002" }
<span class="caption">Gmc Kmm2002 3</span>

</div>
## Measurement functions and ranges

The specifications of the *KMM2002* seem not to be available to the public. The following is taken from the specs of the *Metrahit 16T* which seems to be almost identical and the *Metrahit 16I* .

| Measurement function | Range | Resolution | Deviation | sigrok result | Remarks |
|---|---|---|---|---|---|
| V= | 30 mV | 10 μV | ±(0.5% + 3) | mq V, unit V, mqflags DC | Input impendance >10 GΩ; not covered by autorange, use manual range |
| 300 mV | 100 μV | ±(0.5% + 3) | " | " |
| 3 V | 1 mV | ±(0.25% + 1) | " |  |
| 30 V | 10 mV | " |  |
| 300 V | 100 mV | " |  |
| 1000 V | 1 V | ±(0.35% + 1) | " |  |
| V≈ | 3 V | 100 μV | ±(1.0% + 3) (> 10 Digit) | mq V, unit V, mqflags AC,RMS |  |
| 30 V | 100 μV | " |  |
| 300 V | 1 mV | " |  |
| 1000 V | 10 mV | " |  |
| V≃ | 3 V | 100 μV | ±(1.0% + 3) (> 10 Digit) | mq V, unit V, mqflags AC,DC,RMS |  |
| 30 V | 100 μV | " |  |
| 300 V | 1 mV | " |  |
| 1000 V | 10 mV | " |  |
| A≈ (clamp only) | &#160;30 A | 10 mA | ±(2.5% + 3) (>10 Digit) | mq Curr., unit A, mqflags AC,DC,RMS | Current clamp with 100 mV/A required, e.g. GMC WZ12B |
| 100 A | 100 mA | " |
| Ω | 30.00 Ω | 10 mΩ | ±(0.5% + 3) | mq Res., unit Ω, mqflags - |  |
| 300.0 Ω | 100 mΩ | " |  |
| 3.000 kΩ | 1 Ω | ±(0.4% + 1) | " |  |
| 30.00 kΩ | 10 Ω | " |  |
| 300.0 kΩ | 100 Ω | " |  |
| 3.000 MΩ | 1 kΩ | ±(0.6% + 1) | " |  |
| 30.00 MΩ | 10 kΩ | ±(2.0% + 1) | " |  |
| Ω Iso 100V | 310 MΩ | 100 Ω - 100 kΩ | ±(3% + 2) | mq Res., unit Ω, mqflags - | Altogether 4 ranges with different resolution |
| Diode/Cont. | 3.0000 V– | 1 mV | ±(0.25% + 1) | mq V, unit V, mqflags DC,DIODE | Diode and cont. are identical on this device, just without beeper for diode. |
| Cap. F | 30.00 nF | 10 pF | ±(1.0% + 3) | mq Cap., unit F, mqflags - |  |
| 300.0 nF | 100 pF | " |  |
| 3.000 µF | 1 nF | " |  |
| Hz= | 300.0 Hz | 0.01 Hz | ±(0.1% + 3) | mq Freq., unit Hz | Communication protocol does not allow to differ AC and DC. |
| 3.000 kHz | 0.1 Hz | " |  |
| 30.00 kHz | 1 Hz | " |  |
| 100.00 kHz | 10 Hz | " | Device actually measures up to more than 160 kHz. |
| Hz≈ | 300.0 Hz | 0.01 Hz | ±(0.1% + 3) | mq Freq., unit Hz | Communication protocol does not allow to differ AC and DC. |
| 3.000 kHz | 0.1 Hz | " |  |
| 30.00 kHz | 1 Hz | " |  |
| 100.00 kHz | 10 Hz | " | Device actually measures up to more than 160 kHz. |
| °C | Pt100 –200.0 - +200.0 °C | 0.1 °C | 2 Kelvin + 5 | mq Temp., unit °C, mqflags - | °F temperature ranges accordingly, but not available via serial interface. |
| Pt100 +200.0 - +800.0 °C | ±(1.0% + 5) | " |  |
| Pt1000 –100.0 - +200.0 °C | 2 Kelvin + 5 | " |  |
| Pt1000 +200.0 - +800.0 °C | ±(1.0% + 5) | " |  |
| Event count |  |  |  |  | Seems not to be present on data output. |
| Data Hold |  |  |  | mqflags += HOLD | Disabled while IR interface is active on [&#160;Matthias'](https://sigrok.org/wiki/User:Matthias_Heidbrink) device. |
| MIN |  |  |  | mqflags += MIN | Influences only display, via IR flag is set, but actual current value is delivered. |
| MAX |  |  |  | mqflags += MAX | Influences only display, via IR flag is set, but actual current value is delivered. |

The column "sigrok result" contains in short form what the driver generates for the resp. data type.

