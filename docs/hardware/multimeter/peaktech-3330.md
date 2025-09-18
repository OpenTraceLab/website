# Peaktech 3330

| | | |:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:| | [![\1](../../assets/hardware/general/\2)](./File:Peaktech_3330_mugshot.png.html) | | | Status | supported | | Source code | [serial-dmm](http://github.com/OpenTraceLab/?p=OpenTraceCapture.git;a=tree;f=src/hardware/serial-dmm) | | Counts | 4000 | | IEC 61010-1 | CAT III (1000V) | | Connectivity | USB and RS232 cables | | Measurements | voltage, current, resistance, capacitance, frequency, duty cycle, diode, continuity, temperature | | Features | autorange, data hold, relative, backlight, display prompts | | Website | [peaktech.de](http://www.peaktech.de/productdetail/kategorie/auslaufmodelle-nur-solange-der-vorrat-reicht/produkt/p-3330.html) | **PeakTech 3330** The **PeakTech 3330** is a 4000 counts, CAT III (1000V) handheld digital multimeter with RS232 or USB connectivity. In addition to the usual features, the display presents the internal temperature, and has extra indicators and prompts (disconnect power from the circuit under test for passive measurement functions, which jacks to connect the probes to depending on the selected function, when a fuse is blown). See [PeakTech 3330/Info](PeakTech_3330/Info.html "PeakTech 3330/Info") for more details (such as **lsusb -v** output) about the device. 
## Contents 
\- [1 Hardware](PeakTech_3330.html#Hardware) \- [2 Photos](PeakTech_3330.html#Photos) \- [3 Protocol](PeakTech_3330.html#Protocol) \- [4 Resources](PeakTech_3330.html#Resources) 
## Hardware **Multimeter**: \- **Multimeter IC**: [Fortune Semiconductor FS9721_LP3](Multimeter_ICs.html#Fortune_Semiconductor_FS9721_LP3 "Multimeter ICs") \- **Crystal**: 4MHz (markings: "4.000") \- **Fuse**: 20A/500V (markings: HUKE R015 / RT14 RT18 / RT19) \- **Fuse**: 500mA/250V (glass) The U1 chip is labelled FS9711_LP3, but works flawlessly with all existing routines for FS9721. Only a TX LED is fitted in the DMM. The fuses do NOT match the CAT III 1000V rating which is claimed on the front cover and in the paper! There are two PCBs, with the input circuitry and range switch stacked on top of the PCB which holds the DMM chip. The top PCB is labelled "DT-9932B-3" in copper. The bottom PCB has "DT-9932B-7" as well as "2004.12.11.v.7" silk screen labels. The PCBs are connected by means of several soldered ribbon cables. There is a COB ("U2") on pads with a QFP44 footprint. The chip is close to a big brown THT capacitor (sample'n'hold?), though the meter does not claim TRMS capabilities. Only few pins are connected, it's unlikely to be a display controller. **RS232/USB cables**: \- The DMM comes with both RS232 as well as USB cables. \- The USB cable contains a CP2102 chip. \- Both cables only have an RX LED. ## Photos \- 
[![\1](../../assets/hardware/general/\2)](./File:P3330_front_holster.png.html)
Device, top, in holster
\- 
[![\1](../../assets/hardware/general/\2)](./File:P3330_device_front.png.html)
Device, top
\- 
[![\1](../../assets/hardware/general/\2)](./File:P3330_device_back.png.html)
Device, bottom
\- 
[![\1](../../assets/hardware/general/\2)](./File:P3330_lcd_indicator.png.html)
LCD, indicators
\- 
[![\1](../../assets/hardware/general/\2)](./File:P3330_lcd_backlight.png.html)
LCD, backlight
\- 
[![\1](../../assets/hardware/general/\2)](./File:P3330_range_labels.png.html)
Range selector, cert labels
\- 
[![\1](../../assets/hardware/general/\2)](./File:P3330_serial_cables.png.html)
Serial cables
\- 
[![\1](../../assets/hardware/general/\2)](./File:P3330_pcb_input.png.html)
PCB, input section
\- 
[![\1](../../assets/hardware/general/\2)](./File:P3330_pcb_dmmchip.png.html)
PCB, DMM chip
\- 
[![\1](../../assets/hardware/general/\2)](./File:P3330_pcb_dmmchip_closeup.png.html)
PCB, DMM chip, closeup
\- 
[![\1](../../assets/hardware/general/\2)](./File:P3330_pcb_twoboard.png.html)
PCB, two board construction
## Protocol See [Multimeter_ICs#Fortune_Semiconductor_FS9721_LP3](Multimeter_ICs.html#Fortune_Semiconductor_FS9721_LP3 "Multimeter ICs") for the DMM IC protocol. Serial communication is controlled by the yellow "RS232" button. ## Resources \- [Product page](http://www.peaktech.de/productdetail/kategorie/auslaufmodelle-nur-solange-der-vorrat-reicht/produkt/p-3330.html) (it's in the vendor's "discontinued" section, has been removed from the website in the meantime) 
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=PeakTech_3330&oldid=12267](https://OpenTraceLab.org/w/index.php?title=PeakTech_3330&oldid=12267)" 
[Categories](specialcategories-specialcategories.md): \- [Device](./Category:Device.html "Category:Device") \- [Multimeter](./Category:Multimeter.html "Category:Multimeter") \- [Supported](./Category:Supported.html "Category:Supported")

## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
