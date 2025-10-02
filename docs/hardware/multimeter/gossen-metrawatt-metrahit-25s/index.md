---
title: Gossen Metrawatt Metrahit 25S
---

# Gossen Metrawatt Metrahit 25S

<div class="infobox" markdown>

![Gossen Metrawatt Metrahit 25S](./img/Gossen_Metrawatt_Metrahit_25S_Logo.png){ .infobox-image }

### Gossen Metrawatt Metrahit 25S

| | |
|---|---|
| **Status** | supported |
| **Source code** | [gmc-mh-1x-2x](https://github.com/OpenTraceLab/OpenTraceCapture/tree/main/src/hardware/gmc-mh-1x-2x) |
| **Counts** | 31000 |
| **IEC 61010-1** | CAT III 1000 V, CAT IV 600 V |
| **Connectivity** | Infrared (RS232) |
| **Measurements** | voltage, current, resistance, capacitance, temperature, diode, continuity |
| **Features** | autorange, data hold |
| **Website** | [[1]](http://www.gossenmetrawatt.com/english/produkte/metrahit25s.htm) |

</div>

The **[Gossen Metrawatt](https://sigrok.org/wiki/Gossen_Metrawatt) Metrahit 25S** is a 4.5 digit, 31000 counts 1000V CAT III/600 V CAT IV handheld digital multimeter with IR (RS232) connectivity.

## Hardware
- **Power supply**:
Battery: 2x *1,5 V IEC R 6*, *IEC LR 6* or corresponding NiCd rechargeable batteries
- **Fuse**:
Current 300 mA: FF (UR) 1,6 A/1000 V AC/DC (10 kA) 6,3 mm x 32 mm
- Current 3A/10A: FF (UR) 10 A/1000 V AC/DC (30 kA) 10 mm x 38 mm

## Photos

<div class="photo-grid" markdown>

[![Gossen Metrawatt Metrahit 25s Logo](./img/Gossen_Metrawatt_Metrahit_25S_Logo.png)](./img/Gossen_Metrawatt_Metrahit_25S_Logo.png "Gossen Metrawatt Metrahit 25s Logo"){ .glightbox data-gallery="gossen-metrawatt-metrahit-25s" }
<span class="caption">Gossen Metrawatt Metrahit 25s Logo</span>

</div>
## Using the device with sigrok

The device is supported in *Send Mode* using a [ RS232 interface](https://sigrok.org/wiki/Gossen_Metrawatt#Metrahit_RS232) by the driver gmc-mh-1x-2x-rs232 (actually this should work, but with [ Matthias'](https://sigrok.org/wiki/User:Matthias_Heidbrink) test device it did not, so it's untested). Set the multimeter to use the communication adaptor *RS232*.

The multimeter is also supported in bidirectional mode using a [ BD232](https://sigrok.org/wiki/Gossen_Metrawatt#Metrahit_BD232) or [ SI232-II](https://sigrok.org/wiki/Gossen_Metrawatt#Metrahit_SI232-II) interface by the driver gmc-mh-2x-bd232.  Set the multimeter to use the communication adaptor *BD232*.

The device might be not detected by the driver if it is in a mode where it sends data rarely, either with a huge send interval or with a measurement function that delivers a very low data rate, e.g.  temperature measurements with K type sensor. Then it should be set to a mode with higher data rate during the initialisation of the driver.

## Measurement functions and ranges
| Measurement function | Range | Resolution | Accuracy | sigrok result | Remarks |
|---|---|---|---|---|---|
| V= | 300 mV | 10 μV | ±(0.05% 3) | mq V, unit V, mqflags DC |  |
| 3 V | 100 μV | " |  |
| 30 V | 1 mV | " |  |
| 300 V | 10 mV | " |  |
| 1000 V | 100 mV | " |  |
| V≈ | 300 mV | 100 µV | ±(0.5% + 30) (> 500 Digit)) | mq V, unit V, mqflags AC,RMS |  |
| 3 V | 100 μV | ±(0.2% + 30) | " |  |
| 30 V | 1 mV | " |  |
| 300 V | 10 mV | " |  |
| 1000 V | 100 mV | " |  |
| V db≈ | -48 - 63 dB | 0.01 dB | ± 0.1 dB | mq V, unit V, mqflags AC,RMS | Actually the 5 AC ranges, see there for accuracy. |
| A= | &#160;300.00 µA | 10 nA | 0.1% + 5 | mq Curr., unit A, mqflags DC |  |
| 3.0000 mA | 100 nA | " |  |
| 30.000 mA | 1 mA | 0.05% + 5 | " |  |
| 300.00 mA | 10 µA | 0.5% + 5 | " |  |
| 3.0000 A | 100 µA | 0.5% + 10 | " |  |
| 10.000 A | 1 mA | " |  |
| A≃ | &#160;300.00 µA | 10 nA | 0.5% + 30 | mq Curr., unit A, mqflags AC,DC,RMS |  |
| 3.0000 mA | 100 nA | " |  |
| 30.000 mA | 1 µA | " |  |
| 300.00 mA | 10 µA | " |  |
| 3.0000 A | 100 µA | 0.75% + 30 | " |  |
| 10.000 A | 1 mA | " |  |
| Ω | 300.00 Ω | 10 mΩ | 0.1% + 5 | mq Res., unit Ω, mqflags - |  |
| 3.0000 kΩ | 100 mΩ | " |  |
| 30.000 kΩ | 1 Ω | " |  |
| 300.00 kΩ | 10 Ω | " |  |
| 3.0000 MΩ | 100 Ω | " |  |
| 30.000 MΩ | 1k Ω | 2% + 5 | " |  |
| Ohm/Cont. | 300 Ω | 100 mΩ | 1% + 3% | mq Res., unit Ω, mqflags - |  |
| Diode | 3 V | 1 mV | 0.2% + 3 | mq V, unit V, mqflags DC,DIODE |  |
| Cap. F | 3.000 nF | 1 pF | 1.0% + 5 | mq Cap., unit F, mqflags - |  |
| 30.00 nF | 10 pF | " |  |
| 300.0 nF | 100 pF | " |  |
| 3.000 µF | 1 nF | " |  |
| 30.00 µF | 10 nF | " |  |
| 300.0 µF | 100 nF | ±(5.0% + 6) | " |  |
| 3.000 mF | 1 µF | " |  |
| 30.00 mF | 1 µF | ±(5.0% + 30) | " |  |
| Hz≈, ≃ | 300.00 Hz | 0.01 Hz | ±(0.1% + 1) | mq Freq., unit Hz, mqflags AC,DC | To activate in AC, press yellow button twice. |
| 3.0000 kHz | 0.1 Hz | " |  |
| 100.000 kHz | 10 Hz | " |  |
| °C | Pt100/Pt1000 –200.0 - -100.0 °C | 0.1 °C | 1 K | mq Temp., unit °C, mqflags - |  |
| Pt100/Pt1000 -100.0 - +100.0 °C | 0.8 K | " |  |
| Pt100/Pt1000 +100.0 - +850.0 °C | ±(0.5% + 3) | " |  |
| °F | " | " | " | mq Temp., unit °C (!), mqflags - | Details and ranges like °C. The protocol does not allow to distinguish between °C and °F, so the unit is always °C. |
| Event count |  |  |  | mq V, unit V, mqflags AC,RMS,REL | To activate, switch to voltage AC, press yellow button twice. Press up to 4 times to cycle parameters, press long to stop. See manual. Not useful remotely because the voltage measurement value is sent, not the counter. |
| Stop Watch |  | 100 ns |  | (Time data) | Max. 100 Min. Press AUTO for start/stop, DATA for reset. Not useful remotely because the stop watch delivers only zeros. |
| Data Hold |  |  |  | mqflags += HOLD | Disabled while IR interface is active on [&#160;Matthias'](https://sigrok.org/wiki/User:Matthias_Heidbrink) test device. |
| MIN |  |  |  | mqflags += MIN | Influences only display, via IR flag is set, but actual current value is delivered. |
| MAX |  |  |  | mqflags += MAX | Influences only display, via IR flag is set, but actual current value is delivered. |

The *Accuracy* row was simplified, see manual for exact specs. If the value contains three values, the middle value is&#160;% or range.

The column "sigrok result" contains in short form what the driver generates for the resp. data type.

