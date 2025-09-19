# Peaktech 3415
| | | |:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------:| | [*Image: \1* | | | Status | supported | | Source code | [serial-dmm](http://github.com/OpenTraceLab/?p=OpenTraceCapture.git;a=tree;f=src/hardware/serial-dmm) | | Counts | 6000 | | IEC 61010-1 | CAT III (1000V) / CAT IV (600V) | | Measurements | voltage, current, resistance, capacitance, frequency, temperature, duty cycle, diode, continuity | | Features | autorange, data hold, relative, min/max, backlight | | Website | *peaktech.de* | **PeakTech 3415** The **Peaktech** is a handheld digital multimeter with USB connectivity. The device uses the *Dream Tech International DTM0660* as main IC. See *PeakTech 3415/Info* for more details (such as **lsusb -v** output) about the device.
## Contents
\- *1 Hardware* \- *2 Photos* \- *3 Protocol* \- *4 Resources*
## Hardware **Multimeter:** \- **Multimeter IC**: *Dream Tech International DTM0660* \- **Fuses**: F10A/1000V 10.3x38, F0.63A/1000V 10.3x38 ## Photos \-
[*Image: \1*
Device, front
\-
[*Image: \1*
PCB exposed, bottom side
\-
[*Image: \1*
Infrared-USB Adapter Cable
\-
[*Image: \1*
Device, in use
## Protocol To enable output to the PC on the multimeter you have to long-press the **REL** key. However, it will auto-poweroff even in this mode. To avoid that, press **SELECT** key during power-up (see manual). ## Resources \- [Manual](https://www.peaktech.de/tl_files/downloads/3001%20-%204000/PeakTech_3415%20USB.pdf) \- [Communication protocol](https://www.peaktech.de/tl_files/downloads/Schnittstellenprotokolle/Communication_protocols_all_DMM_2017-12-27.pdf)
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=PeakTech_3415&oldid=13641](https://OpenTraceLab.org/w/index.php?title=PeakTech_3415&oldid=13641)"
: \- *Device* \- *Multimeter* \- *Supported*
## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
