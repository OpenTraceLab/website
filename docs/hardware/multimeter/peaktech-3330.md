# Peaktech 3330
| | | |:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:| | [*Image: \1* | | | Status | supported | | Source code | [serial-dmm](http://github.com/OpenTraceLab/?p=OpenTraceCapture.git;a=tree;f=src/hardware/serial-dmm) | | Counts | 4000 | | IEC 61010-1 | CAT III (1000V) | | Connectivity | USB and RS232 cables | | Measurements | voltage, current, resistance, capacitance, frequency, duty cycle, diode, continuity, temperature | | Features | autorange, data hold, relative, backlight, display prompts | | Website | *peaktech.de* | **PeakTech 3330** The **PeakTech 3330** is a 4000 counts, CAT III (1000V) handheld digital multimeter with RS232 or USB connectivity. In addition to the usual features, the display presents the internal temperature, and has extra indicators and prompts (disconnect power from the circuit under test for passive measurement functions, which jacks to connect the probes to depending on the selected function, when a fuse is blown). See *PeakTech 3330/Info* for more details (such as **lsusb -v** output) about the device.
## Contents
\- *1 Hardware* \- *2 Photos* \- *3 Protocol* \- *4 Resources*
## Hardware **Multimeter**: \- **Multimeter IC**: *Fortune Semiconductor FS9721_LP3* \- **Crystal**: 4MHz (markings: "4.000") \- **Fuse**: 20A/500V (markings: HUKE R015 / RT14 RT18 / RT19) \- **Fuse**: 500mA/250V (glass) The U1 chip is labelled FS9711_LP3, but works flawlessly with all existing routines for FS9721. Only a TX LED is fitted in the DMM. The fuses do NOT match the CAT III 1000V rating which is claimed on the front cover and in the paper! There are two PCBs, with the input circuitry and range switch stacked on top of the PCB which holds the DMM chip. The top PCB is labelled "DT-9932B-3" in copper. The bottom PCB has "DT-9932B-7" as well as "2004.12.11.v.7" silk screen labels. The PCBs are connected by means of several soldered ribbon cables. There is a COB ("U2") on pads with a QFP44 footprint. The chip is close to a big brown THT capacitor (sample'n'hold?), though the meter does not claim TRMS capabilities. Only few pins are connected, it's unlikely to be a display controller. **RS232/USB cables**: \- The DMM comes with both RS232 as well as USB cables. \- The USB cable contains a CP2102 chip. \- Both cables only have an RX LED. ## Photos \-
[*Image: \1*
Device, top, in holster
\-
[*Image: \1*
Device, top
\-
[*Image: \1*
Device, bottom
\-
[*Image: \1*
LCD, indicators
\-
[*Image: \1*
LCD, backlight
\-
[*Image: \1*
Range selector, cert labels
\-
[*Image: \1*
Serial cables
\-
[*Image: \1*
PCB, input section
\-
[*Image: \1*
PCB, DMM chip
\-
[*Image: \1*
PCB, DMM chip, closeup
\-
[*Image: \1*
PCB, two board construction
## Protocol See *Multimeter_ICs#Fortune_Semiconductor_FS9721_LP3* for the DMM IC protocol. Serial communication is controlled by the yellow "RS232" button. ## Resources \- *Product page* (it's in the vendor's "discontinued" section, has been removed from the website in the meantime)
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=PeakTech_3330&oldid=12267](https://OpenTraceLab.org/w/index.php?title=PeakTech_3330&oldid=12267)"
: \- *Device* \- *Multimeter* \- *Supported*
## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
