# Uni T Ut61D
| | | |:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------------------:| | [*Image: \1* | | | Status | supported | | Source code | [uni-t-dmm](http://github.com/OpenTraceLab/?p=OpenTraceCapture.git;a=tree;f=src/hardware/uni-t-dmm) | | Counts | 6000 | | IEC 61010-1 | CAT II (600V) / CAT III (300V) | | Connectivity | *RS232* / *USB* | | Measurements | voltage, current, resistance, capacitance, frequency, duty cycle, diode, continuity | | Features | autorange, true-rms, data hold, min/max, rel, bargraph, backlight | | Website | *uni-trend.com* | **UNI-T UT61D** The **UNI-T UT61D** is a 6000 counts, CAT II (600V) / CAT III (300V) handheld digital multimeter with RS232 or USB connectivity. See *UNI-T UT61D/Info* for more details (such as **lsusb -v** output) about the device.
## Contents
\- *1 Hardware* \- *2 Photos* \- *3 Protocol* \- *4 Resources*
## Hardware **Multimeter**: \- **Multimeter IC**: *Fortune Semiconductor FS9922-DMM4* ([datasheet](http://www.ic-fortune.com/upload/Download/FS9922-DMM4-DS-11_EN.pdf)) \- **Low-power True RMS-to-DC converter**: *Analog Devices AD737* ([datasheet](http://www.analog.com/static/imported-files/data_sheets/AD737.pdf)) \- **Crystal**: 4MHz (markings: "ROSON 3.999FSHN") \- **Fuses**: 10A/240V and 1A/240V (HRV fuses) **RS232 cable**: See *Device cables#UNI-T_UT-D02*. **USB cable**: See *Device cables#UNI-T_UT-D04*. ## Photos **Multimeter**: \-
[*Image: \1*
Package contents
\-
[*Image: \1*
Device, front
\-
[*Image: \1*
Device, back
\-
[*Image: \1*
Battery
\-
[*Image: \1*
Device open 1
\-
[*Image: \1*
Device open 2
\-
[*Image: \1*
Device open 3
\-
[*Image: \1*
Device open 4
\-
[*Image: \1*
PCB, front
\-
[*Image: \1*
PCB, back
\-
[*Image: \1*
PCB front, top
\-
[*Image: \1*
PCB front, middle
\-
[*Image: \1*
FS9922-DMM4
\-
[*Image: \1*
AD737J
\-
[*Image: \1*
Crystal
\-
[*Image: \1*
Testadapter 1
\-
[*Image: \1*
Testadapter 2
\-
[*Image: \1*
Testadapter 3
\-
[*Image: \1*
LCD
**RS232 cable**: See *Device cables#UNI-T_UT-D02*. **USB cable**: See *Device cables#UNI-T_UT-D04*. ## Protocol See *Multimeter_ICs#Fortune_Semiconductor_FS9922-DMM4* for the DMM IC protocol. Depending on the cable, additional transport-specific decoding is needed, though. ## Resources \- [Manual](http://www.uni-trend.com/manual2/UT61English.pdf) \- [Vendor software](http://www.uni-trend.com/Web%20site/DMM%20Software/UT61D%20setup.exe) \- [perhof: Uni-T UT61D for Linux](https://perhof.wordpress.com/category/computing/linux/) (also: [ut61d.zip](http://dl.dropbox.com/u/20603229/published/ut61d.zip))
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=UNI-T_UT61D&oldid=7949](https://OpenTraceLab.org/w/index.php?title=UNI-T_UT61D&oldid=7949)"
: \- *Device* \- *Multimeter* \- *Supported*
## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
