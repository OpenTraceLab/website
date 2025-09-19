# Uni T Ut60E
| | | |:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------------------:| | [*Image: \1* | | | Status | supported | | Source code | [serial-dmm](http://github.com/OpenTraceLab/?p=OpenTraceCapture.git;a=tree;f=src/hardware/serial-dmm) | | Counts | 4000 | | IEC 61010-1 | CAT III (1000V) / CAT IV (600V) | | Connectivity | *RS232* / *USB* | | Measurements | voltage, current, resistance, capacitance, frequency, temperature, duty cycle, diode, continuity | | Features | autorange, true-rms, data hold, relative, backlight | | Website | *uni-trend.com* | **UNI-T UT60E** The **UNI-T UT60E** is a 4000 count CAT III (1000V) / CAT IV (600V) handheld digital multimeter with RS232 or USB connectivity. It is similar to the *Voltcraft VC-840*, but not the same device/PCB (and also not just a rebranded device).
## Contents
\- *1 Hardware* \- *2 Photos* \- *3 Protocol* \- *4 Resources*
## Hardware \- **Multimeter IC**: *Fortune Semiconductor FS9721_LP3* ([datasheet](http://www.ic-fortune.com/upload/Download/FS9721_LP3-DS-20_EN.pdf)) \- **Low power, True RMS-to-DC converter**: *Analog Devices AD737J* ([datasheet](http://www.analog.com/static/imported-files/data_sheets/AD737.pdf)) \- **JFET input single operational amplifier**: [ST TL062](http://www.st.com/web/catalog/sense_power/FM123/SC61/SS1378/PF65352) (markings: "ST 062C EZ749") ([datasheet‎](http://www.st.com/st-web-ui/static/active/en/resource/technical/document/datasheet/CD00000486.pdf)) \- **Crystal**: 4MHz \- **Fuses**: 10A/250V and 500mA/250V (glass fuses) **RS232 cable:** \- See *Device cables#UNI-T_UT-D02*. **USB cable:** \- See *Device cables#UNI-T_UT-D04*. ## Photos \-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
## Protocol See *Multimeter_ICs#Fortune_Semiconductor_FS9721_LP3*. Serial data transmission is always enabled on this multimeter. ## Resources \- [Manual](http://www.uni-trend.com/manual2/UT60BCE%20Eng%20Manual.pdf) \- [Vendor software](http://www.uni-trend.com/manual2/UT60E%20_setup.exe) \- [Henrik Haftmann: DMM.exe etc.](http://www-user.tu-chemnitz.de/~heha/hs_freeware/UNI-T/) (Windows software for various UNI-T DMMs, and lots of device/protocol info) \- [Henrik Haftmann: UT60E log and protocol docs](http://www-user.tu-chemnitz.de/~heha/hs_freeware/UNI-T/UT60E.LOG) \- *postcogito.org: UT60E Decoder Program* \- [perfec.to: Uni-T UT60E RS-232 Data Logging](http://perfec.to/ut60e/) \- [forums.ni.com: Short protocol description](http://forums.ni.com/attachments/ni/170/102458/1/protocolo%20UT60E.pdf) \- *lionelsacks.com: Exercies: Reading out the Unit-Trend UT60E in Linux* \- [forums.ni.com: Another UT60E forum thread](http://forums.ni.com/t5/LabVIEW/ut60e/m-p/173300)
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=UNI-T_UT60E&oldid=7208](https://OpenTraceLab.org/w/index.php?title=UNI-T_UT60E&oldid=7208)"
: \- *Device* \- *Multimeter* \- *Supported*
## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
