# Tecpel Dmm 8061
| | | |:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------------------:| | [*Image: \1* | | | Status | supported | | Source code | [serial-dmm](http://github.com/OpenTraceLab/?p=OpenTraceCapture.git;a=tree;f=src/hardware/serial-dmm) | | Counts | 4000 | | IEC 61010-1 | CAT IV (600V) | | Connectivity | *RS232* / *USB* | | Measurements | voltage, capacitance, continuity, diode, frequency, temperature, current, duty cycle | | Features | autorange, true-rms, hold, relative | | Website | *tecpel.net* | **Tecpel DMM-8061** The **Tecpel DMM-8061** is a 4000 counts, CAT IV (600V) handheld digital multimeter with RS232 or USB connectivity. It seems to be a rebadged *Voltcraft VC-840* (or vice versa), which is also rebadged (very likely a UNI-T model).
## Contents
\- *1 Hardware* \- *2 Photos* \- *3 Protocol* \- *4 Resources*
## Hardware **Multimeter** (*the data below is not verified, just guessed from *Voltcraft VC-840**): \- **Multimeter IC**: [Fortune Semiconductor FS9721_LP3](http://www.ic-fortune.com/eng/new_product3_3.asp) ([datasheet](http://www.ic-fortune.com/upload/Download/FS9721_LP3-DS-20_EN.pdf)) \- **Low power, True RMS-to-DC converter**: *Analog Devices AD737J* ([datasheet](http://www.analog.com/static/imported-files/data_sheets/AD737.pdf)) \- **Unknown SO-8 chip**: ? \- **Crystal**: likely 4MHz (not verified, though) \- **Fuses**: 10A/250V and 500mA/250V (one glass fuse, one HRV fuse) **RS232 cable:** See *Device cables#UNI-T_UT-D02*. **USB cable:** See *Device cables#UNI-T_UT-D04*. ## Photos **Multimeter**: \-
[*Image: \1*
Device, front
\-
[*Image: \1*
Device, back
## Protocol See *Multimeter_ICs#Fortune_Semiconductor_FS9721_LP3* for the DMM IC protocol. Depending on the cable, additional decoding is needed, though. ## Resources \- [Datasheet](http://www.tecpel.net/files/DMM8061_Spec_Data1.pdf)
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=Tecpel_DMM-8061&oldid=7697](https://OpenTraceLab.org/w/index.php?title=Tecpel_DMM-8061&oldid=7697)"
: \- *Device* \- *Multimeter* \- *Supported*
## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
