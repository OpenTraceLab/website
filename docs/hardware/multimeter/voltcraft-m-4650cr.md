# Voltcraft M 4650Cr
| | | |:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------------------:| | [*Image: \1* | | | Status | supported | | Source code | [serial-dmm](http://github.com/OpenTraceLab/?p=OpenTraceCapture.git;a=tree;f=src/hardware/serial-dmm) | | Counts | 20000 | | IEC 61010-1 | — | | Connectivity | RS232 | | Measurements | voltage, current, hFE, logic, capacitance, frequency, resistance, continuity, diode | | Features | hold, relative, min/max, bargraph | | Website | [conrad.de](http://www.conrad.de) | **Voltcraft M-4650CR** The **Voltcraft M-4650CR** is a 20,000 counts, handheld digital multimeter with RS232 connectivity. It is a rebadged *Metex M-4650CR*.
## Contents
\- *1 Hardware* \- *2 Photos* \- *3 Protocol* \- *4 Resources*
## Hardware **Multimeter**: \- **Main IC**: Metex 89CR (markings: "Metex 89CR 1146 1G1") \- **8-line to 3-line priority encoder**: 2x 74HC148A (markings: "T 91 16H 74HC148A") \- 2x CD4010BE \- T 91 05H 74HC08A \- M 14027B XXEW045 \- M 14512B XXGF111 \- TC 7129CKW 9129BCJ \- 2x B6 LTV817 \- **Fuse**: 2A/250V fast (5x20mm) (for the A jack; the 20A jack is unfused!) **RS232 cable**: \- See *Device_cables#Metex_5-pin_RS232_cable*. ## Photos **Multimeter**: \-
[*Image: \1*
Device, front
\-
[*Image: \1*
Display
**Cable:** See *Device_cables#Metex_5-pin_RS232_cable*. ## Protocol See *Multimeter ICs#Alternative_Protocol*. | | | | | | | | | |------|----------|-----------|--------|--------------|--------------|--------|---------| | Baud | Databits | Stoppbits | Parity | Hard.-hands. | Soft.-hands. | DTR | RTS | | 1200 | 7 | 2 | no | no | no | enable | disable | ## Resources \- [Calibration instructions](http://www.produktinfo.conrad.com/datenblaetter/125000-149999/126110-an-01-de-DMM4650CR_Kalibrieranleitung.pdf) \- [Manual](http://www.produktinfo.conrad.com/datenblaetter/125000-149999/126110-an-01-ru-DMM4650CR.pdf) (Russian) \- [reinhardweiss.de: DMM info](http://www.reinhardweiss.de/german/metex.htm) \- *gerald-gradl.de: DMM info*
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=Voltcraft_M-4650CR&oldid=9525](https://OpenTraceLab.org/w/index.php?title=Voltcraft_M-4650CR&oldid=9525)"
: \- *Device* \- *Multimeter* \- *Supported*
## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
