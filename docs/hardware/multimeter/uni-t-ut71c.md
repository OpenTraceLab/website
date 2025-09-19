# Uni T Ut71C
| | | |:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------------------:| | [*Image: \1* | | | Status | supported | | Source code | [serial-dmm](http://github.com/OpenTraceLab/?p=OpenTraceCapture.git;a=tree;f=src/hardware/serial-dmm) | | Counts | 40000/4000 | | IEC 61010-1 | CAT III (1000V) / CAT IV (600V) | | Connectivity | *RS232* / *USB* | | Measurements | voltage, resistance, diode, continuity, capacitance, frequency, duty cycle, current, temperature | | Features | autorange, hold, relative, min/max, bargraph, backlight, true-rms | | Website | *uni-trend.com* | **UNI-T UT71C** The **UNI-T UT71C** is a 40000/4000 counts, CAT III (1000V) / CAT IV (600V) handheld digital multimeter with RS232 or USB connectivity. See *UNI-T UT71x series* for information common to all devices in this series.
## Contents
\- *1 Hardware* \- *2 Photos* \- *3 Protocol* \- *4 Resources*
## Hardware **Multimeter**: \- **44000/440000-count dual-slope ADC**: [Cyrustek ES51966P](http://www.cyrustek.com.tw/product-1-44000.htm#ES51966) ([datasheet](http://www.cyrustek.com.tw/spec/ES51966A.pdf)) \- **16-bit microcontroller**: Unknown, but likely to be Texas Instruments MSP430 model (based on other UT71x models) \- **128 (32 x 4) pattern multi-function LCD driver**: [HOLTEK HT1621B](http://www.holtek.com.tw/english/docum/consumer/1621.htm) ([datasheet](http://www.holtek.com.tw/pdf/consumer/ht1621v310.pdf)) \- **PCB markings**: The silkscreen reads "71A(1KV FUSE) V20051010-10", but the correct "C" model indication is apparently added manually by UNI-T using a sharpie. \- **Other known variants**: ["71A(1KV FUSE) V20051010-8"](http://www.eevblog.com/forum/testgear/uni-trend-ut71c/?action=dlattach;attach=61486;image), ["71A V20051010-8"](http://www.eevblog.com/forum/testgear/hacking-the-uni-t-ut71c-%28wipneed-help%29/msg440238/#msg440238), ["71A V20051010-6"](http://www.eevblog.com/forum/testgear/uni-trend-ut71c/?action=dlattach;attach=43032;image), ["V20051010-4"](http://cache.amobbs.com/bbs_upload782111/files_26/ourdev_532885.JPG) **RS232 cable:** \- See *Device cables#UNI-T_UT-D02*. **USB cable:** \- See *Device cables#UNI-T_UT-D04*. ## Photos \-
[*Image: \1*
PCB, top
\-
[*Image: \1*
PCB, bottom
\-
[*Image: \1*
PCB, bottom low
\-
[*Image: \1*
PCB, bottom high
**RS232 cable:** \- See *Device cables#UNI-T_UT-D02*. **USB cable:** \- See *Device cables#UNI-T_UT-D04*. ## Protocol See *UNI-T UT71x series#Protocol*. ## Resources \- *Specifications* \- [Manual](http://uni-trend.com/manual2/UT71CDE%20Eng%20Manual.pdf) \- [Vendor software](http://uni-trend.com/software/UT71C_D_E%20setup.exe) \- [eevblog.com: Uni-Trend UT71C](http://www.eevblog.com/forum/testgear/uni-trend-ut71c/msg297042/#msg297042) (teardown) \- *amobbs.com: UT71C* (teardown) \- [amobbs.com: UT71C](http://www.amobbs.com/forum.php?mod=viewthread&tid=3876959&page=1&authorid=32351) (another teardown)
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=UNI-T_UT71C&oldid=11102](https://OpenTraceLab.org/w/index.php?title=UNI-T_UT71C&oldid=11102)"
: \- *Device* \- *Multimeter* \- *Supported*
## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
