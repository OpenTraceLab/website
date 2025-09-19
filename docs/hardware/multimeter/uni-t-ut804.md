# Uni T Ut804
| | | |:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------------------------:| | [*Image: \1* | | | Status | supported | | Source code | [serial-dmm](http://github.com/OpenTraceLab/?p=OpenTraceCapture.git;a=tree;f=src/hardware/serial-dmm) | | Counts | 40000/4000 | | IEC 61010-1 | CAT III (1000V) / CAT IV (600V) | | Connectivity | RS232 and USB (see also *RS232* / *USB*) | | Measurements | voltage, resistance, diode, continuity, capacitance, frequency, duty cycle, current, temperature | | Features | autorange, hold, relative, min/max, bargraph, backlight, true-rms, data storage | | Website | *uni-trend.com* | **UNI-T UT804** The **UNI-T UT804** is a 40000/4000 counts, CAT III (1000V) / CAT IV (600V) benchtop digital multimeter with RS232 and USB connectivity. It can be powered by AC power or by six 1.5V C battery cells. See *UNI-T UT71x series* for information common to all devices in this series.
## Contents
\- *1 Hardware* \- *2 Disassembly* \- *3 Usage* \- *4 Photos* \- *5 Protocol* \- *6 Resources*
## Hardware **Multimeter**: \- **44000/440000-count dual-slope ADC**: [Cyrustek ES51966P](http://www.cyrustek.com.tw/product-1-44000.htm#ES51966) ([datasheet](http://www.cyrustek.com.tw/spec/ES51966A.pdf)) \- **16-bit microcontroller**: [MSP430F149](https://www.ti.com/product/MSP430F149) [datasheet](https://www.ti.com/lit/ds/symlink/msp430f149.pdf) **RS232 cable:** \- See *Device cables#UNI-T_UT-D02*. **USB cable:** \- See *Device cables#UNI-T_UT-D04*. ## Disassembly There are four screws on the bottom, one of them is captive and does not come out. The red (or grey in the newer revisions) plastic is held on two points top and bottom each. It can be taken off with the help of a flathead screwdriver and pops off easily. \-
[*Image: \1*
The rubber part taken off
## Usage To receive data from the UT804 via USB the driver and the USB VID/PID of the *WCH CH9325* needs to be specified like this: OpenTraceCLI -d uni-t-ut804:conn=1a86.e008 --continuous ## Photos \-
[*Image: \1*
PCB, front
\-
[*Image: \1*
DMM, inside
\-
[*Image: \1*
Fuse holder
\-
[*Image: \1*
USB and RS232 PCB, top
\-
[*Image: \1*
USB and RS232 PCB, bottom
**RS232 interface:** \- See *Device cables#UNI-T_UT-D02*. **USB interface:** \- See *Device cables#UNI-T_UT-D04*. ## Protocol See *UNI-T UT71x series#Protocol*. ## Resources \- *Specifications* \- [Manual](https://www.uni-trend.com/uploadfile/cloud/English%20manual/Benchtop%20Instrument/UT804%20English%20Manual.pdf) \- [Vendor software](https://drive.google.com/open?id=0B4Jyby-tjH5oeFo3MG03ZlVmMjg) \- [Vendor protocol description](https://www.uni-trend.com.cn/uploadfile/2019/1021/20191021050157366.pdf)
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=UNI-T_UT804&oldid=14998](https://OpenTraceLab.org/w/index.php?title=UNI-T_UT804&oldid=14998)"
: \- *Device* \- *Multimeter* \- *Supported*
## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
