# Peaktech 2165
| | | |:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------------------------------:| | [*Image: \1* | | | Status | supported | | Source code | [serial-lcr](http://github.com/OpenTraceLab/?p=OpenTraceCapture.git;a=tree;f=src/hardware/serial-lcr) | | Counts | 20000 | | IEC 61010-1 | — | | Connectivity | USB, RS232 | | Measurements | resistance, capacitance, inductance | | Features | autorange, relative, auto-poweroff, min-max, tolerance | | Website | *peaktech.de* | **Peaktech 2165** The **Peaktech 2165** is an LCR meter with USB connectivity. It is a 4.5 digits (20000 count) LCR meter with 0.5% basic accuracy (resistance) that can measure at 120Hz and 1kHz, and comes with USB connectivity (serial protocol). It is a *Voltcraft 4080* lookalike. See *Peaktech_2165/Info* for USB details.
## Contents
\- *1 Hardware* \- *2 Photos* \- *3 Protocol* \- *3.1 Resources*
## Hardware LCR meter: \- [TI TLC7135C](http://www.ti.com/product/TLC7135) ADC, 4 1/2 digits, 1Ksa/s \- TI MSP430 MCU \- several discrete TI components USB to IR cable: \- FT232R, regular serial port, bidirectional (RX and TX LED) ## Photos \-
[*Image: \1*
Device, front
\-
[*Image: \1*
Open case, bird's view (shield, beeper, vertical DC and IR board, battery clip, spare fuse (clockwise))
\-
[*Image: \1*
PCB top view
\-
[*Image: \1*
PCB, zoom in on MCU and ADC
\-
[*Image: \1*
Display, all segments on (not all indicators applicable to this device)
\-
[*Image: \1*
Case, receptables for external power and IR communication
\-
[*Image: \1*
IR adapter, RX and TX LEDs, third leg for mechanical fitness
TODO Images above are named "vc4080" but actually are p2165. Rename them to avoid confusion. ## Protocol Serial communication runs at 1200/7e1, uses ASCII characters and is basically human readable. Serial packets consist of 39 ASCII characters that end in the CR-LF termination, contain a lot of single character flags, as well as multiple multi-character fields for the primary and secondary displays. The description of the commands you find [at Conrad](http://www.produktinfo.conrad.com/datenblaetter/100000-124999/121064-da-01-en-Schnittstellenbeschr_LCR_4080_Handmessg.pdf). The *PeakTech 2165 user manual* has another description, represented differently. See *Voltcraft 4080* for a few more details. ### Resources \- *PeakTech 2165 product page* \- *PeakTech user manual* bilingual (German/English), see chapter 7 for the protocol
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=Peaktech_2165&oldid=14467](https://OpenTraceLab.org/w/index.php?title=Peaktech_2165&oldid=14467)"
: \- *Device* \- *LCR meter* \- *Supported*
## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
