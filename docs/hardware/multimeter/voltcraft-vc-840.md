# Voltcraft Vc 840
| | | |:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------:| | [*Image: \1* | | | Status | supported | | Source code | [serial-dmm](http://github.com/OpenTraceLab/?p=OpenTraceCapture.git;a=tree;f=src/hardware/serial-dmm) | | Counts | 4000 | | IEC 61010-1 | CAT IV (600V) | | Connectivity | *RS232* / *USB* | | Measurements | voltage, capacitance, continuity, diode, frequency, temperature, current, duty cycle | | Features | autorange, true-rms, hold, relative | | Website | [conrad.de](http://www.conrad.de/ce/de/product/123295/VOLTCRAFT-VC840-DMM/SHOP_AREA_17622&promotionareaSearchDetail=005) | **Voltcraft VC-840** The **Voltcraft VC-840** is a 4000 counts, CAT IV (600V) handheld digital multimeter with RS232 or USB connectivity.
## Contents
\- *1 Hardware* \- *2 Photos* \- *3 Protocol* \- *4 Resources*
## Hardware **Multimeter**: \- **Multimeter IC**: [Fortune Semiconductor FS9721_LP3](http://www.ic-fortune.com/eng/new_product3_3.asp) ([datasheet](http://www.ic-fortune.com/upload/Download/FS9721_LP3-DS-20_EN.pdf)) \- **Low power, True RMS-to-DC converter**: *Analog Devices AD737J* ([datasheet](http://www.analog.com/static/imported-files/data_sheets/AD737.pdf)) \- **Unknown SO-8 chip**: ? \- **Crystal**: likely 4MHz (not verified, though) \- **Fuses**: 10A/250V and 500mA/250V (one glass fuse, one HRV fuse) **RS232 cable:** \- See *Device cables#UNI-T_UT-D02*. **USB cable:** \- See *Device cables#UNI-T_UT-D04*. ## Photos **Multimeter**: \-
[*Image: \1*
Device, front
\-
[*Image: \1*
Device, back
\-
[*Image: \1*
Device, back w/o battery
\-
[*Image: \1*
Battery 1
\-
[*Image: \1*
Battery 2
\-
[*Image: \1*
PCB, front
\-
[*Image: \1*
PCB, back
\-
[*Image: \1*
Analog Devices AD737J
\-
[*Image: \1*
Fortune Semi. FS9721_LP3
**RS232 cable:** See *Device cables#UNI-T_UT-D02*. **USB cable:** See *Device cables#UNI-T_UT-D04*. ## Protocol See *Multimeter_ICs#Fortune_Semiconductor_FS9721_LP3* for the DMM IC protocol. Depending on the cable, additional decoding is needed, though. TODO: Serial cable vs. the two USB HID based cables. A [short protocol description is also available from Voltcraft/Conrad](http://www.produktinfo.conrad.com/datenblaetter/100000-124999/123295-da-01-en-RS232_Protocol_VOLTCRAFT_VC840_DMM.pdf). And [another one](http://www2.produktinfo.conrad.com/datenblaetter/100000-124999/121112-da-01-en-Digitalmultimeter_VC840_Schnittstellenp.pdf). ## Resources \- [Manual](http://www.produktinfo.conrad.com/datenblaetter/100000-124999/123295-an-01-ml-VOLTCRAFT_VC840_DMM_de_en_fr_nl.pdf) \- [Vendor software](http://www.produktinfo.conrad.com/datenblaetter/100000-124999/123295-up-01-en-Win7_32_64_Bit_VC840_DMM.zip) \- [gecius.de: Multimeter VC840](http://www.gecius.de/linux/vc840/) \- [kolleegium.ch: VC 840 Recorder](http://cw.kolleegium.ch/vc840/) \- *true random: driver for the cheap digital multimeter VC 840/VC 820* \- *true random: Software for the multimeters vc840/vc820* \- *Georg Acher: Voltcraft VC820/VC840 und Linux*
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=Voltcraft_VC-840&oldid=6363](https://OpenTraceLab.org/w/index.php?title=Voltcraft_VC-840&oldid=6363)"
: \- *Device* \- *Multimeter* \- *Supported*
## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
