# Tekpower Tp4000Zc
| | | |:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------------------:| | [*Image: \1* | | | Status | supported | | Source code | [serial-dmm](http://github.com/OpenTraceLab/?p=OpenTraceCapture.git;a=tree;f=src/hardware/serial-dmm) | | Counts | 4000 | | IEC 61010-1 | CAT II (600V) | | Connectivity | *RS232* | | Measurements | voltage, resistance, continuity, diode, capacitance, frequency, temperature, current, duty cycle | | Features | autorange, data hold, relative | | Website | [tekpower.us](http://www.tekpower.us) | **TekPower TP4000ZC** The **TekPower TP4000ZC** is a 4000 counts, CAT II (600V) handheld digital multimeter with RS232 connectivity. This multimeter is a rebadged *Digitek DT4000ZC*.
## Contents
\- *1 Hardware* \- *2 Photos* \- *3 Protocol* \- *4 Resources*
## Hardware **Multimeter:** \- **Multimeter IC**: The microcontroller is an unidentifiable plastic blob (based on the communication protocol, probably a *Fortune Semiconductor FS9721_LP3*) \- LM358 opamp \- HEF4013BT flip-flop \- The RS-232 connector is a standard 3.5m stereo jack, with the ring left unconnected. The transmitter is optically insulated from the rest of the device. **Cable:** \- See *Device_cables#Digitek_DT4000ZC_cable*. \- The DB-9 connector has a loopback resistor between the RX and TX pins. ## Photos **Multimeter:** \-
[*Image: \1*
Device, angle
\-
[*Image: \1*
Mugshot
\-
[*Image: \1*
Device, back
\-
[*Image: \1*
Package contents
\-
[*Image: \1*
Holster removed, front
\-
[*Image: \1*
Holster removed, back
\-
[*Image: \1*
Battery compartment
\-
[*Image: \1*
Rear cover
\-
[*Image: \1*
Front cover
\-
[*Image: \1*
Rear cover, PCB removed
\-
[*Image: \1*
PCB, front
\-
[*Image: \1*
PCB, back
\-
[*Image: \1*
Chip
\-
[*Image: \1*
HEF4013BT flip-flop
\-
[*Image: \1*
LM358 opamp
\-
[*Image: \1*
RS-232 optoisolation
\-
[*Image: \1*
RS-232 module
\-
[*Image: \1*
RS-232 PCB, bottom
\-
[*Image: \1*
RS-232 PCB, top
**Cable:** See *Device_cables#Digitek_DT4000ZC_cable*. ## Protocol See *Multimeter_ICs#Fortune_Semiconductor_FS9721_LP3*. User bit 2 is used to indicate temperature measurement in degrees Celsius. ## Resources \- [Video review of TP4000ZC (Part 1/2)](http://www.youtube.com/watch?v=kXzAD74C5As) \- [Video review of TP4000ZC (Part 2/2)](http://www.youtube.com/watch?v=7pbRLom7bNc) \- [TP4000ZC serial protocol](http://www.multimeterwarehouse.com/TP4000ZC/TP4000ZC_serial_protocol.pdf) \- [multimeterwarehouse.com: TP4000ZC](http://www.multimeterwarehouse.com/TP4000ZC.htm) \- [multimeterreviews.com: TekPower TP4000ZC (PC RS232 Interface)](http://www.multimeterreviews.com/tekpower-tp4000zc-pc-based-rs232-interaced-auto-ranging-digital/) \- [mjlorton.com: T4D 22 TekPower TP4000ZC](http://mjlorton.com/forum/index.php?topic=103.0)
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=TekPower_TP4000ZC&oldid=5665](https://OpenTraceLab.org/w/index.php?title=TekPower_TP4000ZC&oldid=5665)"
: \- *Device* \- *Multimeter* \- *Supported*
## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
