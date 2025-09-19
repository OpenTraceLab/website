# Gossen Metrawatt Metrahit 27I
| | | |:-------------|------------------------------------------------------------------------------------------------------------------------------| | Status | planned | | Counts | 31000 | | IEC 61010-1 | CAT II 600 V | | Connectivity | Infrared (RS232/USB) | | Measurements | voltage, resistance, temperature, diode, continuity | | Features | autorange, data hold, backlight, insulation measurement, data logging | | Website | [[1]](http://www.gossenmetrawatt.com/english/produkte/metrahit27i.htm) | **Gossen Metrawatt 27I** **Please note: This page is a work in progress and still partly incorrect.** The ***Gossen Metrawatt* Metrahit 27I** is a 3100/31000 counts 600 V CAT II handheld digital multimeter with bidirectional IR (RS232/USB) connectivity. It supports milliohm and insulation (megaohm) measurements and has data logging capabilities. There are two versions of this device, an older one with yellow rotary switch and a newer one with red rotary switch. They also have different power supply connectors.
## Contents
\- *1 Hardware* \- *2 Photos* \- *3 Communication Protocol* \- *4 Measurement functions and ranges*
## Hardware \- **Power supply**: \- Battery: 3x *1,2 V NiMH* rechargeable batteries \- External power supply *NA HIT 27* (Art. Z218J) by Gossen Metrawatt, 5V, 600 mA (newer version) \- **Fuse**: \- FF (UR) 1,6 A/1000 V AC/DC (10 kA) 6,3 mm x 32 mm ## Photos ## Communication Protocol The complete description is available on request from the manufacturer. ## Measurement functions and ranges Measurement function | Range | Resolution | Accuracy | OpenTraceLab result | Remarks
---|---|---|---|---|---
V= | 3 V | 100 μV | ±(0.1% + 10) | mq V, unit V, mqflags DC |
30 V | 1 mV | ±(0.1% + 5) | " |
300 V | 10 mV | " |
600 V | 100 mV | " |
V≈ | 3 V | 100 μV | ±(0.2% + 10) | mq V, unit V, mqflags AC |
30 V | 1 mV | " |
300 V | 10 mV | " |
600 V | 100 mV | " |
mΩ@1A | 3 mΩ | 0.001 mΩ | ±(1% + 10) | mq Res., unit Ω, mqflags - | 4-wire Kelvin measurement
30 mΩ | 0.001 mΩ | ±(0.5% + 10) | " | "
300 mΩ | 0.01 mΩ | " | "
mΩ@200 mA | 30 mΩ | 0.01 mΩ | ±(0.25% + 10) | " | "
300 mΩ | 0.01 mΩ | " | "
3 Ω | 0.1 mΩ | " | "
30 Ω | 1 mΩ | " | "
Ω | 300.00 Ω | 1 mΩ | ±(0.1% + 10) | " | ZERO with yellow button
3.0000 kΩ | 10 mΩ | ±(0.1% + 5) | " | "
30.000 kΩ | 100 mΩ | " |
300.00 kΩ | 1 Ω | " |
3.0000 MΩ | 10 Ω | " |
30.000 MΩ | 100 Ω | ±(1.5% + 10) | " |
MΩ (Insulation) | 30 MΩ | 10 kΩ | ±(2% + 10) | " | Insulation measurement, test voltage selectable 50/100/250/500 V
300 MΩ | 100 kΩ | " | "
3 GΩ | 1 MΩ | ±(3% + 10) | " | "
Cont. | 310 Ω | 100 mΩ | ±(1% + 5) | mq Res., unit Ω, mqflags - | Signal < about 10 Ω
Diode | 3 V | 100 µV | ±(1% + 5) | mq V, unit V, mqflags DC,DIODE |
Hz | 300.00 Hz | 0.01 Hz | ±(0.05% + 5) | mq Freq., unit Hz, mqflags AC |
3.000 kHz | 0.1 Hz | " |
°C | Pt100/Pt1000
–200.0 - +100.0 °C | 0.1 °C | ±(1 K + 5) | mq Temp., unit °C, mqflags - |
Pt100/Pt1000
+100.0 - 850.0 °C | ±(0.5K + 5) | " |
Ni 100/Ni1000
-60-+180 °C | " | Not tested yet due to lack of corresponding sensor.
°F | " | " | " | mq Temp., unit °F, mqflags - | Details and ranges like °C.
Data Hold |  |  |  | mqflags += HOLD |
MIN |  |  |  | mqflags += MIN |
MAX |  |  |  | mqflags += MAX |
The *Accuracy* row was simplified, see manual for exact specs. The column "OpenTraceLab result" contains in short form what the driver generates for the resp. data type. This device has an uncommon input impendance of 2.1 MΩ in AC/DC voltage measurement modes.
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=Gossen_Metrawatt_Metrahit_27I&oldid=12093](https://OpenTraceLab.org/w/index.php?title=Gossen_Metrawatt_Metrahit_27I&oldid=12093)"
: \- *Device* \- *Multimeter* \- *Planned*
## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
