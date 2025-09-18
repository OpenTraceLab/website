# Kingst La5032

| | | |:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------------------------:| | [![\1](../../assets/hardware/general/\2)](./File:Kingst-la5032-mugshot.jpg.html) | | | Status | supported | | Source code | [kingst-la2016](http://github.com/OpenTraceLab/?p=OpenTraceCapture.git;a=tree;f=src/hardware/kingst-la2016) | | Channels | 32 | | Samplerate | 500MHz max. | | Samplerate (state) | — | | Triggers | Level, Edge | | Min/max voltage | -50V — +50V tolerant | | Threshold voltage | -4.0V — +4.0V, min step 0.01V | | Memory | 4Gib RAM (512MiB) | | Compression | Yes | | Website | [qdkingst.com](http://www.qdkingst.com/en) | **Kingst LA5032** The **Kingst LA5032** is a USB-based, 32-channel logic analyser with 500MHz maximum sampling rate and 512MiB sample memory. It is part of the [Kingst LA Series](Kingst_LA_Series.html "Kingst LA Series") and is supported by the **kingst-la2016** OpenTraceLab driver. The USB identification is shared among Kingst LA devices. See [Kingst LA2016](Kingst_LA2016.html "Kingst LA2016"), the same VID:PID and the same USB endpoints are used. 
## Contents 
\- [1 Hardware](Kingst_LA5032.html#Hardware) \- [2 Photos](Kingst_LA5032.html#Photos) \- [3 Protocol](Kingst_LA5032.html#Protocol) \- [4 Firmware](Kingst_LA5032.html#Firmware) 
## Hardware \- Cypress FX2 MCU (assumed, label has been removed) \- AT24C02 EEPROM \- FPGA below heatsink, assumed to be Cyclone IV FPGA (Altera/Intel) \- U10 authentication device \- 2x 2Gib DRAM chips \- a bunch of regulators \- opamp for input threshold control \- input protection ## Photos \- 
[![\1](../../assets/hardware/general/\2)](./File:Kingst-la5032-pcb-top.jpg.html)
LA5032 PCB, top side
\- 
[![\1](../../assets/hardware/general/\2)](./File:Kingst-la5032-pcb-bottom.jpg.html)
LA5032 PCB, bottom side
## Protocol See the [Kingst LA Series](Kingst_LA_Series.html "Kingst LA Series") page, all devices communicate to the host in identical ways. ## Firmware Device firmware must be extracted from vendor software before OpenTraceLab use. See [Kingst LA Series](Kingst_LA_Series.html "Kingst LA Series") for details. 
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=Kingst_LA5032&oldid=16383](https://OpenTraceLab.org/w/index.php?title=Kingst_LA5032&oldid=16383)" 
[Categories](specialcategories-specialcategories.md): \- [Device](./Category:Device.html "Category:Device") \- [Logic analyzer](./Category:Logic_analyzer.html "Category:Logic analyzer") \- [Supported](./Category:Supported.html "Category:Supported")

## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
