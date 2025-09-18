# Peaktech 3415

| | | |:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------:| | [![\1](../../assets/hardware/general/\2)](./File:Peaktech3415_top.png.html) | | | Status | supported | | Source code | [serial-dmm](http://github.com/OpenTraceLab/?p=OpenTraceCapture.git;a=tree;f=src/hardware/serial-dmm) | | Counts | 6000 | | IEC 61010-1 | CAT III (1000V) / CAT IV (600V) | | Measurements | voltage, current, resistance, capacitance, frequency, temperature, duty cycle, diode, continuity | | Features | autorange, data hold, relative, min/max, backlight | | Website | [peaktech.de](https://www.peaktech.de/productdetail/kategorie/digital---handmultimeter/produkt/peaktech-3415-usb.815.html) | **PeakTech 3415** The **Peaktech** is a handheld digital multimeter with USB connectivity. The device uses the [Dream Tech International DTM0660](Multimeter_ICs.html#Dream_Tech_International_DTM0660 "Multimeter ICs") as main IC. See [PeakTech 3415/Info](PeakTech_3415/Info.html "PeakTech 3415/Info") for more details (such as **lsusb -v** output) about the device. 
## Contents 
\- [1 Hardware](PeakTech_3415.html#Hardware) \- [2 Photos](PeakTech_3415.html#Photos) \- [3 Protocol](PeakTech_3415.html#Protocol) \- [4 Resources](PeakTech_3415.html#Resources) 
## Hardware **Multimeter:** \- **Multimeter IC**: [Dream Tech International DTM0660](Multimeter_ICs.html#Dream_Tech_International_DTM0660 "Multimeter ICs") \- **Fuses**: F10A/1000V 10.3x38, F0.63A/1000V 10.3x38 ## Photos \- 
[![\1](../../assets/hardware/general/\2)](./File:Peaktech3415_top.png.html)
Device, front
\- 
[![\1](../../assets/hardware/general/\2)](./File:Peaktech3415_pcb.jpg.html)
PCB exposed, bottom side
\- 
[![\1](../../assets/hardware/general/\2)](./File:Peaktech3415_cable.JPG.html)
Infrared-USB Adapter Cable
\- 
[![\1](../../assets/hardware/general/\2)](./File:Peaktech3415_operation.JPG.html)
Device, in use
## Protocol To enable output to the PC on the multimeter you have to long-press the **REL** key. However, it will auto-poweroff even in this mode. To avoid that, press **SELECT** key during power-up (see manual). ## Resources \- [Manual](https://www.peaktech.de/tl_files/downloads/3001%20-%204000/PeakTech_3415%20USB.pdf) \- [Communication protocol](https://www.peaktech.de/tl_files/downloads/Schnittstellenprotokolle/Communication_protocols_all_DMM_2017-12-27.pdf)
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=PeakTech_3415&oldid=13641](https://OpenTraceLab.org/w/index.php?title=PeakTech_3415&oldid=13641)" 
[Categories](specialcategories-specialcategories.md): \- [Device](./Category:Device.html "Category:Device") \- [Multimeter](./Category:Multimeter.html "Category:Multimeter") \- [Supported](./Category:Supported.html "Category:Supported")

## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
