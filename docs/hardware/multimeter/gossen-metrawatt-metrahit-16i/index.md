---
title: Gossen Metrawatt Metrahit 16I
---

# Gossen Metrawatt Metrahit 16I

<div class="infobox" markdown>

![Gossen Metrawatt Metrahit 16I](./img/Metrahit_16i_1.jpg){ .infobox-image }

### Gossen Metrawatt Metrahit 16I

| | |
|---|---|
| **Status** | supported |
| **Source code** | [gmc-mh-1x-2x](https://github.com/OpenTraceLab/OpenTraceCapture/tree/main/src/hardware/gmc-mh-1x-2x) |
| **Counts** | 3100 (31000) |
| **IEC 61010-1** | CAT III 1000 V, CAT IV 600 V |
| **Connectivity** | Infrared (RS232) |
| **Measurements** | voltage, current, resistance, capacitance, temperature, diode, continuity |
| **Features** | autorange, data hold, bargraph |
| **Website** | [[1]](http://www.gossenmetrawatt.com/english/produkte/metrahit16i.htm) |

</div>

The **[Gossen Metrawatt](https://sigrok.org/wiki/Gossen_Metrawatt) Metrahit 16I** is a 3100 counts handheld digital multimeter with IR (RS232) connectivity and insulation measurement (500/1000 V).

The resolution is one digit higher on the data interface.

## Hardware
- **Battery**:  *9 V IEC 6 LR 61*
- **Fuse**: None! (not required, no internal amps ranges)
- TODO.

## Photos

<div class="photo-grid" markdown>

[![Metrahit 16i 1](./img/Metrahit_16i_1.jpg)](./img/Metrahit_16i_1.jpg "Metrahit 16i 1"){ .glightbox data-gallery="gossen-metrawatt-metrahit-16i" }
<span class="caption">Metrahit 16i 1</span>

[![Gossen Metrawatt Metrahit 16i Small](./img/Gossen_Metrawatt_Metrahit_16I_small.jpg)](./img/Gossen_Metrawatt_Metrahit_16I_small.png "Gossen Metrawatt Metrahit 16i Small"){ .glightbox data-gallery="gossen-metrawatt-metrahit-16i" }
<span class="caption">Gossen Metrawatt Metrahit 16i Small</span>

[![Metrahit 16i 2](./img/Metrahit_16i_2.jpg)](./img/Metrahit_16i_2.jpg "Metrahit 16i 2"){ .glightbox data-gallery="gossen-metrawatt-metrahit-16i" }
<span class="caption">Metrahit 16i 2</span>

</div>
## Measurement functions and ranges
| Measurement function | Range | Resolution | Deviation | sigrok result | Remarks |
|---|---|---|---|---|---|
| V= | 30 mV | 10 μV | ±(0.5% + 3) | mq V, unit V, mqflags DC | Input impendance >10 GΩ; not covered by autorange, use manual range |
| 300 mV | 100 μV | ±(0.5% + 3) | " | " |
| 3 V | 1 mV | ±(0.25% + 1) | " |  |
| 30 V | 10 mV | " |  |
| 300 V | 100 mV | " |  |
| 600 V | 1 V | ±(0.35% + 1) | " |  |
| V≈ | 3 V | 100 μV | ±(1.0% + 3) (> 10 Digit) | mq V, unit V, mqflags AC,RMS |  |
| 30 V | 100 μV | " |  |
| 300 V | 1 mV | " |  |
| 1000 V | 10 mV | " |  |
| V≃ | 3 V | 100 μV | ±(1.0% + 3) (> 10 Digit) | mq V, unit V, mqflags AC,DC,RMS |  |
| 30 V | 100 μV | " |  |
| 300 V | 1 mV | " |  |
| 1000 V | 10 mV | " |  |
| A≈ (Clamp only) | &#160;30 A | 10 mA | ±(2.5% + 3) (>10 Digit) | mq Curr., unit A, mqflags AC,DC,RMS | Current clamp with 100 mV/A required, e.g. GMC WZ12B |
| 100 A | 100 mA | " |
| Ω | 30.00 Ω | 10 mΩ | ±(0.5% + 3) | mq Res., unit Ω, mqflags - |  |
| 300.0 Ω | 100 mΩ | " |  |
| 3.000 kΩ | 1 Ω | ±(0.4% + 1) | " |  |
| 30.00 kΩ | 10 Ω | " |  |
| 300.0 kΩ | 100 Ω | " |  |
| 3.000 MΩ | 1 kΩ | ±(0.6% + 1) | " |  |
| 30.00 MΩ | 10 kΩ | ±(2.0% + 1) | " |  |
| Ω Iso 500V | 1.600 GΩ | 1 kΩ - 1 MΩ | ±(3% + 2) | mq Res., unit Ω, mqflags - | Altogether 4 ranges with different resolution |
| Ω Iso 1000V | 3.100 GΩ | 1 kΩ - 1 MΩ | mq Res., unit Ω, mqflags - | Altogether 4 ranges with different resolution |
| Diode/Cont. | 3.000 V– | 1 mV | ±(0.25% + 1) | mq V, unit V, mqflags DC,DIODE | Diode and cont. are identical on this device, just without beeper for diode. |
| Cap. F | 30.00 nF | 10 pF | ±(1.0% + 3) | mq Cap., unit F, mqflags - |  |
| 300.0 nF | 100 pF | " |  |
| 3.000 µF | 1 nF | " |  |
| 30.00 µF | 10 nF | ±(3.0% + 3) | " |  |
| Hz= | 300.0 Hz | 0.01 Hz | ±(0.1% + 3) | mq Freq., unit Hz | The protocol does not allow to differ AC and DC. |
| 3.000 kHz | 0.1 Hz | " |  |
| 30.00 kHz | 1 Hz | " |  |
| 100.00 kHz | 10 Hz | " |  |
| Hz≈ | 300.0 Hz | 0.01 Hz | ±(0.1% + 3) | mq Freq., unit Hz | The protocol does not allow to differ AC and DC. |
| 3.000 kHz | 0.1 Hz | " |  |
| 30.00 kHz | 1 Hz | " |  |
| 100.00 kHz | 10 Hz | " |  |
| °C | Pt100 –200.0 - +200.0 °C | 0.1 °C | 2 Kelvin + 5 | mq Temp., unit °C, mqflags - |  |
| Pt100 +200.0 - +800.0 °C | ±(1.0% + 5) | " |  |
| Pt1000 –100.0 - +200.0 °C | 2 Kelvin + 5 | " |  |
| Pt1000 +200.0 - +800.0 °C | ±(1.0% + 5) | " |  |
| Event count |  |  |  |  | Seems not to be present on data output. |
| Data Hold |  |  |  | mqflags += HOLD | Disabled while IR interface is active on [&#160;Matthias'](https://sigrok.org/wiki/User:Matthias_Heidbrink) device. |
| MIN |  |  |  | mqflags += MIN | Influences only display, via IR flag is set, but actual current value is delivered. |
| MAX |  |  |  | mqflags += MAX | Influences only display, via IR flag is set, but actual current value is delivered. |

The column "sigrok result" contains in short form what the driver generates for the resp. data type.

