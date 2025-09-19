# Gw Instek Gdm 397
| | | |:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------------------:| | [*Image: \1* | | | Status | supported | | Source code | [serial-dmm](http://github.com/OpenTraceLab/?p=OpenTraceCapture.git;a=tree;f=src/hardware/serial-dmm) | | Counts | 4000 | | IEC 61010-1 | CAT III (1000V) / CAT IV (600V) | | Connectivity | *RS232* | | Measurements | voltage, current, resistance, capacitance, frequency, temperature, duty cycle, diode, continuity | | Features | autorange, data hold, relative, backlight | | Website | [gwinstek.com](https://www.gwinstek.com/en-global/products/detail/GDM-400_GDM-300) | **GW Instek GDM-397** The **GW Instek GDM-397** is a 4000 count CAT III (1000V) / CAT IV (600V) handheld digital multimeter with RS232 connectivity. It is similar to the *UNI-T UT61B*, but not the same device/PCB (this appears to have improvet input protection along with HRC fuses). Press and hold the **REL** button to enable serial data transmission.
## Contents
\- *1 Hardware* \- *2 Photos* \- *3 Protocol* \- *4 Resources*
## Hardware **Multimeter**: \- **Multimeter IC**: *Fortune Semiconductor FS9922-DMM3* ([datasheet](http://www.ic-fortune.com/upload/Download/FS9922-DMM3-DS-10_EN.pdf)) \- **Crystal**: 4MHz (markings: "3.999") \- **Fuses**: 600mA H 1000V (6.35x31.8mm) and 10A H 1000V (10.3x38.1mm) (HRC fuses) **RS232 cable**: \- Included (appears to be same as *Device cables#UNI-T_UT-D02*). **USB cable**: \- Optional (appears to be same as *Device cables#UNI-T_UT-D04*). ## Photos \-
[*Image: \1*
Front
\-
[*Image: \1*
PCB
\-
[*Image: \1*
RS-232 Cable
## Protocol See *Multimeter_ICs#Fortune_Semiconductor_FS9922-DMM3* for the DMM IC protocol. Depending on the cable, additional transport-specific decoding is needed, though. Serial data transmission must be enabled by a long press on the "REL" button. ## Resources \- [Datasheet](https://www.gwinstek.com/en-global/products/downloadSeriesDownNew/9914/718) \- [Manual](https://www.gwinstek.com/en-global/products/downloadSeriesDownNew/9890/718)
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=GW_Instek_GDM-397&oldid=15417](https://OpenTraceLab.org/w/index.php?title=GW_Instek_GDM-397&oldid=15417)"
: \- *Device* \- *Multimeter* \- *Supported*
## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
