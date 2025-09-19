# Radioshack 22 812
| | | |:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------------------:| | [*Image: \1* | | | Status | supported | | Source code | [serial-dmm](http://github.com/OpenTraceLab/?p=OpenTraceCapture.git;a=tree;f=src/hardware/serial-dmm) | | Counts | 4000 | | IEC 61010-1 | CAT II (600V) | | Connectivity | RS232 (standard DB9 connector) | | Measurements | voltage, temperature, current, resistance, capacitance, continuity, diode, logic, frequency, hFE, duty cycle, pulse width | | Features | autorange, data hold, min/max, dBmW (600Ω) | | Website | [radioshack.com](https://www.radioshack.com/search/softwareResults.jsp?kw=22-812) | **RadioShack 22-812** The **RadioShack 22-812** is a 4000 counts, CAT II (600V) handheld digital multimeter with RS-232 connectivity. It is no longer sold under this part number, and for a while, it appeared to have been discontinued. RadioShack does sell a visually identical multimeter, the [RadioShack 22-039](https://www.radioshack.com/product/index.jsp?productId=12988573). It is not yet clear if the 22-039 is the same device as the 22-812.
## Contents
\- *1 Hardware* \- *2 Photos* \- *3 Protocol* \- *3.1 Packet structure* \- *3.2 Segment lettering* \- *3.3 Mode byte* \- *4 Resources*
## Hardware The microcontroller is an unidentifiable plastic blob. This devices has a standard DB-9 connector at the top, and does not require a special adapter cable. The RS-232 transmitter is optically insulated from the rest of the device. The transmitter uses a separate PCB, integrated into the multimeter's housing. The RS-232 module is powered from the serial port. ## Photos \-
[*Image: \1*
Mugshot
\-
[*Image: \1*
Device, angle
\-
[*Image: \1*
RS-232 connector
\-
[*Image: \1*
Holster removed, front
\-
[*Image: \1*
Holster removed, back
\-
[*Image: \1*
Battery location
\-
[*Image: \1*
Opened up
\-
[*Image: \1*
PCB removed
\-
[*Image: \1*
PCB, front
\-
[*Image: \1*
PCB, back
\-
[*Image: \1*
Buttons PCB
\-
[*Image: \1*
RS-232 module
\-
[*Image: \1*
RS-232 transmitter
\-
[*Image: \1*
RS-232 PCB, top
\-
[*Image: \1*
RS-232 PCB, bottom
\-
[*Image: \1*
Banana sockets connecting to PCB
\-
[*Image: \1*
Spare fuse
\-
[*Image: \1*
Multimeter IC
\-
[*Image: \1*
Calibration pots
## Protocol The device periodically sends 9-byte packets at 4800 baud, 8n1. The packet includes a mode indicator, payload and checksum. The payload is a 1-1 mapping of the LCD segments. ### Packet structure | | | | | | | | | | |------|----------|-------|-----|------|-----|-----|-------|------| | Byte | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 | | 0 | Mode | | | | | | | | | 1 | Hz | Ohms | k | M | F | A | V | m | | 2 | u | n | dBm | s | % | hFE | REL | MIN | | 3 | 4D | 4C | 4G | 4B | DP3 | 4E | 4F | 4A | | 4 | 3D | 3C | 3G | 3B | DP2 | 3E | 3F | 3A | | 5 | 2D | 2C | 2G | 2B | DP1 | 2E | 2F | 2A | | 6 | 1D | 1C | 1G | 1B | MAX | 1E | 1F | 1A | | 7 | Beep | Diode | Bat | Hold | \\- | ~ | RS232 | Auto | | 8 | Checksum | | | | | | | | ### Segment lettering | | | | |-----|:---:|-----| | | A | | | | | | | F | | B | | | | | | | G | | | | | | | E | | C | | | | | | | D | | ### Mode byte | | | |-------|--------------------------------| | Value | Meaning | | 0 | DC V | | 1 | AC V | | 2 | DC uA | | 3 | DC mA | | 4 | DC A | | 5 | AC uA | | 6 | AC mA | | 7 | AC A | | 8 | Ohm | | 9 | Capacitance | | 10 | Hz (dial set to Hz) | | 11 | Hz (dial set to DCV) | | 12 | Hz (dial set to mA/A) | | 13 | Duty cycle (dial set to Hz) | | 14 | Duty cycle (dial set to DCV) | | 15 | Duty cycle (dial set to mA/A) | | 16 | Pulse width (dial set to Hz) | | 17 | Pulse width (dial set to DCV) | | 18 | Pulse width (dial set to mA/A) | | 19 | Diode | | 20 | Continuity (beep) | | 21 | hFE | | 22 | LOGIC | | 23 | dBm | | 24 | (Unknown) | | 25 | Temp | ## Resources \- [rs22812.py project page](http://code.google.com/p/rs22812/) (Python interface to RadioShack 22-812 DMM) \- [RadioShack 22-812 user manual](http://www.radioshack.com/graphics/uc/rsk/Support/ProductManuals/2200812A_PM_EN.pdf)
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=RadioShack_22-812&oldid=5307](https://OpenTraceLab.org/w/index.php?title=RadioShack_22-812&oldid=5307)"
: \- *Device* \- *Multimeter* \- *Supported*
## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
