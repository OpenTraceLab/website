# Peaktech 2165

| | | |:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------------------------------:| | [![\1](../../assets/hardware/general/\2)](./File:Peaktech2165-front.png.html) | | | Status | supported | | Source code | [serial-lcr](http://github.com/OpenTraceLab/?p=OpenTraceCapture.git;a=tree;f=src/hardware/serial-lcr) | | Counts | 20000 | | IEC 61010-1 | — | | Connectivity | USB, RS232 | | Measurements | resistance, capacitance, inductance | | Features | autorange, relative, auto-poweroff, min-max, tolerance | | Website | [peaktech.de](https://www.peaktech.de/productdetail/kategorie/lcr-messgeraet/produkt/p-2165.html) | **Peaktech 2165** The **Peaktech 2165** is an LCR meter with USB connectivity. It is a 4.5 digits (20000 count) LCR meter with 0.5% basic accuracy (resistance) that can measure at 120Hz and 1kHz, and comes with USB connectivity (serial protocol). It is a [Voltcraft 4080](Voltcraft_4080.html "Voltcraft 4080") lookalike. See [Peaktech_2165/Info](Peaktech_2165/Info.html "Peaktech 2165/Info") for USB details. 
## Contents 
\- [1 Hardware](Peaktech_2165.html#Hardware) \- [2 Photos](Peaktech_2165.html#Photos) \- [3 Protocol](Peaktech_2165.html#Protocol) \- [3.1 Resources](Peaktech_2165.html#Resources) 
## Hardware LCR meter: \- [TI TLC7135C](http://www.ti.com/product/TLC7135) ADC, 4 1/2 digits, 1Ksa/s \- TI MSP430 MCU \- several discrete TI components USB to IR cable: \- FT232R, regular serial port, bidirectional (RX and TX LED) ## Photos \- 
[![\1](../../assets/hardware/general/\2)](./File:Peaktech2165-front.png.html)
Device, front
\- 
[![\1](../../assets/hardware/general/\2)](./File:Vc4080-inside-overview.png.html)
Open case, bird's view (shield, beeper, vertical DC and IR board, battery clip, spare fuse (clockwise))
\- 
[![\1](../../assets/hardware/general/\2)](./File:Vc4080-pcb-top.png.html)
PCB top view
\- 
[![\1](../../assets/hardware/general/\2)](./File:Vc4080-pcb-top-zoom-mcu-adc.png.html)
PCB, zoom in on MCU and ADC
\- 
[![\1](../../assets/hardware/general/\2)](./File:Vc4080-display-all-segments.png.html)
Display, all segments on (not all indicators applicable to this device)
\- 
[![\1](../../assets/hardware/general/\2)](./File:Vc4080-case-dc-ir.png.html)
Case, receptables for external power and IR communication
\- 
[![\1](../../assets/hardware/general/\2)](./File:Vc4080-cable-ir-port.png.html)
IR adapter, RX and TX LEDs, third leg for mechanical fitness
TODO Images above are named "vc4080" but actually are p2165. Rename them to avoid confusion. ## Protocol Serial communication runs at 1200/7e1, uses ASCII characters and is basically human readable. Serial packets consist of 39 ASCII characters that end in the CR-LF termination, contain a lot of single character flags, as well as multiple multi-character fields for the primary and secondary displays. The description of the commands you find [at Conrad](http://www.produktinfo.conrad.com/datenblaetter/100000-124999/121064-da-01-en-Schnittstellenbeschr_LCR_4080_Handmessg.pdf). The [PeakTech 2165 user manual](http://peaktech.de/productdetail/kategorie/lcr-messer/produkt/p-2165.html?file=tl_files/downloads/2001%20-%203000/PeakTech_2165_USB.pdf) has another description, represented differently. See [Voltcraft 4080](Voltcraft_4080.html "Voltcraft 4080") for a few more details. ### Resources \- [PeakTech 2165 product page](http://peaktech.de/productdetail/kategorie/lcr-messer/produkt/p-2165.html) \- [PeakTech user manual](http://peaktech.de/productdetail/kategorie/lcr-messer/produkt/p-2165.html?file=tl_files/downloads/2001%20-%203000/PeakTech_2165_USB.pdf) bilingual (German/English), see chapter 7 for the protocol 
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=Peaktech_2165&oldid=14467](https://OpenTraceLab.org/w/index.php?title=Peaktech_2165&oldid=14467)" 
[Categories](specialcategories-specialcategories.md): \- [Device](./Category:Device.html "Category:Device") \- [LCR meter](./Category:LCR_meter.html "Category:LCR meter") \- [Supported](./Category:Supported.html "Category:Supported")

## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
