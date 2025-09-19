# Voltcraft M 3650Cr
| | | |:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------------------:| | [*Image: \1* | | | Status | supported | | Source code | [serial-dmm](http://github.com/OpenTraceLab/?p=OpenTraceCapture.git;a=tree;f=src/hardware/serial-dmm) | | Counts | 2000 | | IEC 61010-1 | — | | Connectivity | *RS232* | | Measurements | voltage, current, resistance, capacitance, hFE, diode, continuity, frequency, logic | | Features | data hold, bargraph, difference | **Voltcraft M-3650CR** The **Voltcraft M-3650CR** is a 2000 counts handheld digital multimeter with RS232 connectivity. It came into the market 1991 and is a rebadged Metex M-3650CR.
## Contents
\- *1 Hardware* \- *2 Photos* \- *3 Protocol* \- *4 Resources* \- *5 Measurement functions and ranges*
## Hardware **Multimeter**: \- **Fuse**: 2A/250V (5x20mm) (for the A jack; the 20A jack is unfused!) \- TODO. **RS232 cable**: \- See *Device_cables#Metex_5-pin_RS232_cable*. ## Photos **Multimeter**: \-
[*Image: \1*
Package
\-
[*Image: \1*
Package, open
\-
[*Image: \1*
Device, front
\-
[*Image: \1*
Device, right side
\-
[*Image: \1*
Device, back
\-
[*Image: \1*
Device, size
\-
[*Image: \1*
Device, display self test on power on.
\-
[*Image: \1*
Device with test probes
\-
[*Image: \1*
Battery pack opened
\-
[*Image: \1*
Device opened
**RS232 cable**: See *Device_cables#Metex_5-pin_RS232_cable*. ## Protocol The protocol is (partially) documented in the manual of the *Voltcraft M-3650CR* and was determined completely by testing. See *Multimeter ICs#Alternative Protocol*. ## Resources \- ## Measurement functions and ranges | | | | | | | |----------------------|------------|------------|-------------|--------------------------------|-------------------------------------------| | Measurement function | Range | Resolution | Accuracy | OpenTraceLab result | Remarks | | V= | 200.0 mV | 100 μV | ±(0.3% + 1) | mq V, unit V, mqflags DC | | | | 2.000 V | 1 mV | | " | | | | 20.00 V | 10 mV | | " | | | | 200.0 V | 100 mV | | " | | | | 1000 V | 1 V | | " | | | V≈ | 200.0 mV | 100 μV | ±(0.8% + 3) | mq V, unit V, mqflags AC | | | | 2.000 V | 1 mV | | " | | | | 20.00 V | 10 mV | | " | | | | 200.0 V | 100 mV | | " | | | | 750 V | 1 V | ±(1.2% + 3) | " | | | A= | 2.000 mA | 1 µA | ±(0.5% + 1) | mq Curr., unit A, mqflags DC | | | | 200.0 mA | 100 µA | ±(1,2% + 1) | " | | | | 20.00 A | 10 mA | ±(2,0% + 5) | " | Max. 20 min.; unfused! | | A≈ | 2.000 mA | 10 µA | ±(1,0% + 5) | mq Curr., unit A, mqflags AC | | | | 200.0 mA | 100 µA | ±(1,8% + 5) | " | | | | 20.00 A | 10 mA | ±(3.0% + 7) | " | Max. 20 min.; unfused! | | Ω | 200.0 Ω | 100 mΩ | | mq Res., unit Ω, mqflags - | | | | 2.000 kΩ | 1 Ω | | " | | | | 20.00 kΩ | 10 Ω | | " | | | | 200.0 kΩ | 100 Ω | | " | | | | 2.000 MΩ | 1 kΩ | | " | | | | 20.00 MΩ | 10 kΩ | | " | | | Cap. F | 2000 pF | 1 pF | ±(2.0% + 3) | mq Cap., unit F, mqflags - | | | | 200.0 nF | 100 pF | | " | | | | 20.00 µF | 10 nF | ±(3.0% + 5) | " | | | Hz= | 20.00 kHz | 1 Hz | ±(2% + 3) | mq Freq., unit Hz, mqflags DC | | | | 200.00 kHz | 10 Hz | | " | | | Logic | | | | \\- | | | hFE | | | | ? | IB=10 µA, UCE=2,8 V | | Diode | | | | mq V, unit V, mqflags DC,DIODE | | | Data Hold | | | | \\- | Not supported by protocol. | The column "OpenTraceLab result" contains in short form what the driver generates for the resp. data type.
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=Voltcraft_M-3650CR&oldid=10803](https://OpenTraceLab.org/w/index.php?title=Voltcraft_M-3650CR&oldid=10803)"
: \- *Device* \- *Multimeter* \- *Supported*
## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
