# Gossen Metrawatt Metrahit 29S
**Gossen Metrawatt Metrahit 29S** [*Image: \1* |
---|---
Status | supported
Source code | [gmc-mh-1x-2x](http://github.com/OpenTraceLab/?p=OpenTraceCapture.git;a=tree;f=src/hardware/gmc-mh-1x-2x)
Counts | 310000
IEC 61010-1 | CAT III 1000 V, CAT IV 600 V (older version)
CAT III 600 V, CAT IV 300 V (newer version)
Connectivity | Infrared (RS232/USB)
Measurements | voltage, current, resistance, capacitance, temperature, diode, continuity
Features | autorange, data hold
Website | [[1]](https://www.gossenmetrawatt.com/english/produkte/metrahit29s.htm)
**Gossen Metrawatt Metrahit 29S** The ***Gossen Metrawatt* Metrahit 29S** is a 310000 counts 1000V CAT III/600 V CAT IV (older version) or 600V CAT III/300 V CAT IV (newer version) handheld digital multimeter with IR (RS232/USB) connectivity. It is very similiar to the *Metrahit 28S*, but has additional energy measurement and data logging capabilities. While the device is detected and functions common with the Metrahit 28S are expected to work, some of the additional measurement functions are not implemented yet. Currently energy measurement is supported by driver *gmc-mh-1x-2x-rs232* only. ## Hardware \- **Power supply**: \- Battery: 2x *1,5 V IEC R 6*, *IEC LR 6* or corresponding NiCd rechargeable batteries \- External power supply *NA4/500* by Gossen Metrawatt, 4.2 V, 500 mA (for older version) \- External power supply *NA5/600* by Gossen Metrawatt, 5 V, 600 mA (for newer version, 3-pin plug) \- **Fuse**: \- Current 300 mA: FF (UR) 1,6 A/1000 V AC/DC (10 kA) 6,3 mm x 32 mm \- Current 3A/10A: FF (UR) 10 A/1000 V AC/DC (30 kA) 10 mm x 38 mm A 16A fuse described in older versions of the manual is **wrong** [[2]](https://www.gossenmetrawatt.com/resources/zz_tam/hit28-29s/bbl_dgbfeinl_new_fuse.pdf)! ## Photos \-
[*Image: \1*
Front, with bumper
\-
[*Image: \1*
Front, without bumper
\-
[*Image: \1*
Back
\-
[*Image: \1*
Inside
\-
[*Image: \1*
Inside, inner cover removed
## Measurement functions and ranges Measurement function | Range | Max. Resolution | Accuracy | OpenTraceLab result | Remarks
---|---|---|---|---|---
V= | 300 mV | 1 μV | ±(0,02% + 0,010% + 5) | mq V, unit V, mqflags DC | Accuracy with ZERO; resolution from 2 1/2 to 5 1/2 digits depending on menu _rAtE_ (min. 0.0005 s in storage mode)
3 V | 10 μV | ±(0,02% + 0,005% + 5) | " | "
30 V | 100 μV | " | "
300 V | 1 mV | " | "
1000 V | 10 mV | " | "
V≈ | 300 mV | 10 µV | ±(0.5% + 30) (> 500 Digit)) | mq V, unit V, mqflags AC,RMS | Resolution from 2 1/2 to 5 1/2 digits depending on menu _rAtE_ (min. 0.05 s)
3 V | 100 μV | ±(0.2% + 30) | " | "
30 V | 100 μV | " | "
300 V | 1 mV | " | "
1000 V | 10 mV | " | "
V≃ | 300 mV | 10 μV | ±(0.5% + 30) (> 500 Digit)) | mq V, unit V, mqflags AC,DC,RMS |
3 V | 100 μV | ±(0.2% + 30) | " |
30 V | 100 μV | " |
300 V | 1 mV | " |
1000 V | 10 mV | " |
V db≈ | -48 - 63 dB | 0,01 dB | ± 0.1 dB | mq V, unit V, mqflags AC,RMS | Actually the 5 AC ranges, see there for accuracy.
V db≈ rel | -48 - 63 dB | 0,01 dB | ± 0,1 dB | mq V, unit V, mqflags AC,RMS | Actually the 5 AC ranges, see there for accuracy. To activate, press yellow button in dB mode, then do second measurement. Cannot be distinguished from non-rel measurement remotely.
A= |  300.00 µA | 1 nA | 0.05% + 0.02% + 5 | mq Curr., unit A, mqflags DC |
3.0000 mA | 10 nA | 0.05% + 0.01% + 5 | " |
30.000 mA | 100 nA | 0.05% + 0.01% + 5 | " |
300.00 mA | 1 µA | 0.1% + 0.01% + 5 | " |
3.0000 A | 100 µA | 0.2% + 0.05% + 5 | " |
10.000 A | 1 mA | 0.2% + 0.05% + 5 | " |
A≃ |  300.00 µA | 10 nA | 0.5% + 30 | mq Curr., unit A, mqflags AC,DC,RMS |
3.0000 mA | 100 nA | " |
30.000 mA | 1 µA | " |
300.00 mA | 10 µA | " |
3.0000 A | 100 µA | 0.7% + 30 | " |
10.000 A | 1 mA | 0.5% + 30 | " |
Ω | 300.00 Ω | 1 mΩ | 0.05% + 0.01% + 5 | mq Res., unit Ω, mqflags - |
3.0000 kΩ | 10 mΩ | " |
30.000 kΩ | 100 mΩ | " |
300.00 kΩ | 1 Ω | " |
3.0000 MΩ | 10 Ω | 0.1% + 0.02% + 5 | " |
30.000 MΩ | 100 Ω | 1% + 0.2% + 5 | " |
Ohm/Cont. | 300 Ω | 100 mΩ | 1% + 3% | mq Res., unit Ω, mqflags - |
Diode/Cont. | 300 mV | 100 µV | 0.2% + 3 | mq V, unit V, mqflags DC,DIODE |
Diode | 3 V | 100 µV | 0.2% + 3 | mq V, unit V, mqflags DC,DIODE |
Cap. F | 3.000 nF | 1 pF | 1.0% + 0.2 | mq Cap., unit F, mqflags - |
30.00 nF | 10 pF | " |
300.0 nF | 100 pF | " |
3.000 µF | 1 nF | " |
30.00 µF | 10 nF | " |
300.0 µF | 100 nF | ±(5.0% + 6) | " |
3.000 mF | 1 µF | " |
30.00 mF | 1 µF | " |
Hz≈, ≃ | 300.00 Hz | 0.001 Hz | ±(0.05% + 1) | mq Freq., unit Hz, mqflags AC,DC | To activate in AC, press yellow button twice.
3.0000 kHz | 0.01 Hz | " |
300.000 kHz | 1 Hz | " |
°C | Pt100/Pt1000
–200.0 - +100.0 °C | 0.1 °C | ±(0,5 K + 3) | mq Temp., unit °C, mqflags - |
Pt100/Pt1000
+100.0 - 850.0 °C | ±(0.2% + 3) | mq Temp., unit °C, mqflags - |
K NiCr-Ni -270-+1372,0 °C | ±(0.7% + 3) | " |
J Fe-CuNi -210 - +1200.0 °C | ±(0.8% + 3) | " | Not tested yet due to lack of corresponding sensor.
°F | " | " | " | mq Temp., unit °F, mqflags - | Details and ranges like °C.
W | 1 mW | 0.1 µW |  | mq power, unit W, mqflags AC,DC,RMS | Available in socket _mA_ only. All W ranges implemented in driver gmc-mh-1x-2x-rs232 only currently!
10 mW | 1 µW |  | " | "
100 mW | 10 µW |  | " | "
1 W | 100 µW |  | " | "
10 W | 1 mW |  | " | Available in both sockets _mA_ and _A_!
100 W | 10 mW |  | " | "
1 kW | 100 mW |  | " | "
10 kW | 1 W |  | " | Available in socket _A_ only!
VAR | - | - | - | mq power, unit TODO, mqflags - | Reactive power. Details and 8 ranges like W. Not implemented yet!
VA | - | - | - | mq power, unit va, mqflags - | Details and 8 ranges like W. Not implemented yet!
Event count |  |  |  | mq V, unit V, mqflags AC,RMS,REL | Counts events >= 2500 digits that last >=2s with a break >=2s. To activate, switch to voltage ACDC, press yellow button twice. Press up to 4 times to cycle parameters, press long to stop. See manual. Not useful remotely because the current measurement value is sent, not the counter.
Stop Watch |  | 100 ns |  | (Time data) | Max. 100 Min. To activate, select a 3V-1000V≃ range manually, press yellow button, press AUTO for start/stop, DATA for reset. Using the stop watch delivers only voltage data and sometimes seems to bring the device into a mode where it even sends invalid data packets.
Data Hold |  |  |  | mqflags += HOLD | Disabled while IR interface is active on [ Matthias'](https://OpenTraceLab.org/wiki/User:Matthias_Heidbrink "User:Matthias Heidbrink") test device.
MIN |  |  |  | mqflags += MIN | Influences only display, via IR flag is set, but actual current value is delivered.
MAX |  |  |  | mqflags += MAX | Influences only display, via IR flag is set, but actual current value is delivered.
Energy measurement functions missing yet. The *Accuracy* row was simplified, see manual for exact specs. If the value contains three values, the middle value is % or range. The column "OpenTraceLab result" contains in short form what the driver generates for the resp. data type.
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=Gossen_Metrawatt_Metrahit_29S&oldid=11919](https://OpenTraceLab.org/w/index.php?title=Gossen_Metrawatt_Metrahit_29S&oldid=11919)"
: \- *Device* \- *Multimeter* \- *Supported*
## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
