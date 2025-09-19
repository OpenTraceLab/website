# Voltcraft Vc 96
| | | |:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------------------:| | [*Image: \1* | | | Status | supported | | Source code | [serial-dmm](http://github.com/OpenTraceLab/?p=OpenTraceCapture.git;a=tree;f=src/hardware/serial-dmm) | | Counts | 4000 | | Connectivity | RS232 | | Measurements | voltage, capacitance, continuity, diode, frequency, current, | | Features | autorange, hold, relative, min-max, hfe, bargraph | | Website | [kappenberg.com](http://www.kappenberg.com/pages/wandler/gat048.htm) | **Voltcraft VC-96** The **Voltcraft VC-96** is an 4000 counts handheld, digital multimeter with RS232 (D-sub, DB-25 connector) connectivity.
## Contents
\- *1 Hardware* \- *2 Photos* \- *3 Protocol* \- *4 Resources*
## Hardware ## Photos \-
[*Image: \1*
Device, top
\-
[*Image: \1*
Device, bottom
\-
[*Image: \1*
Device, left
\-
[*Image: \1*
PCB, top
\-
[*Image: \1*
PCB, bottom
\-
[*Image: \1*
Main chip
\-
[*Image: \1*
Rectifier
\-
[*Image: \1*
Chip, top
\-
[*Image: \1*
Chip, left
\-
[*Image: \1*
Chip, LED
\-
[*Image: \1*
Chip
\-
[*Image: \1*
Chip
\-
[*Image: \1*
USB modification
\-
[*Image: \1*
Micro-USB instead of DB-25
\-
[*Image: \1*
Modification schematics
## Protocol The device sends always (without request) about 4 telegrams per second with 1200 baud, 8N2 over the LED through the case. The location of the LED is marked on the back (the little circle above the screw). The converter originally has a RS232 25pin sub-d and needs an 9VDC power supply, but can be modified with a little TTL serial to USB board. The handling remains the same except using /dev/ttyUSBx instead of /dev/ttySx. Example packets:  ACV 0.0 V\r\n ACV 0.00 V\r\n DCV 00uV\r\n DCV 0.0 V\r\n DCV- 0.1mV\r\n OHM OL M<0xEA>\r\n DIO OL V\r\n BEP OL K<0xEA>\r\n DIO OL V\r\n DCA 00uA\r\n hfe 0.0 \r\n DCA 02uA\r\n DCA 0.0mA\r\n DCA 00mA\r\n ACA 761mA\r\n ACA 0.0mA\r\n  The device does not send packets in CAP and in FREQ mode. ## Resources \- [kappenberg.com: Basic device info](http://www.kappenberg.com/pages/wandler/gat048.htm)
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=Voltcraft_VC-96&oldid=14680](https://OpenTraceLab.org/w/index.php?title=Voltcraft_VC-96&oldid=14680)"
: \- *Device* \- *Multimeter* \- *Supported*
## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
