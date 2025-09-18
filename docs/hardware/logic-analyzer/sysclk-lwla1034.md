# Sysclk Lwla1034

| | | |:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:| | [![\1](../../assets/hardware/general/\2)](./File:Sysclk_lwla1034_mugshot.png.html) | | | Status | supported | | Source code | [sysclk-lwla](http://github.com/OpenTraceLab/?p=OpenTraceCapture.git;a=tree;f=src/hardware/sysclk-lwla) | | Channels | 34 | | Samplerate | 125MHz (max) | | Samplerate (state) | ? | | Triggers | 34 + extern | | Min/max voltage | 0-5V | | Threshold voltage | ? | | Memory | 256Kbit/channel | | Compression | RLE | | Website | [aliexpress.com](http://www.aliexpress.com/item/free-shipping-New-arrival-Powerful-100MHz-34-channels-LA1034-Logic-Analyzer-Timing-State-Logic-Analyzer/1227957767.html) | **Sysclk LWLA1034** The **Sysclk LWLA1034** is a USB-based, 34-channel logic analyzer with up to 125MHz sampling rate. See [Sysclk LWLA1034/Info](Sysclk_LWLA1034/Info.html "Sysclk LWLA1034/Info") for more details (such as **lsusb -v** output) about the device. 
## Contents 
\- [1 Hardware](Sysclk_LWLA1034.html#Hardware) \- [2 Photos](Sysclk_LWLA1034.html#Photos) \- [3 Software](Sysclk_LWLA1034.html#Software) \- [4 Firmware](Sysclk_LWLA1034.html#Firmware) \- [5 Resources](Sysclk_LWLA1034.html#Resources) 
## Hardware \- Altera EP2C5Q208C8N (Cyclone II) FPGA \- Cypress CY7C68013A-56 (FX2) USB interface chip \- Cypress 256k×36 SRAM (likely a [CY7C1361C-133AXC](http://www.cypress.com/?mpn=CY7C1361C-133AXC) or similar) \- STC15F104E 8051-based microcontroller The not-installed 10-pin connector between the USB socket and the large capacitor seems to connect to the JTAG pins of the FPGA. ## Photos \- 
[![\1](../../assets/hardware/general/\2)](./File:Sysclk_lwla1034_device_top.jpg.html)
\- 
[![\1](../../assets/hardware/general/\2)](./File:Sysclk_lwla1034_device_bottom.jpg.html)
\- 
[![\1](../../assets/hardware/general/\2)](./File:Sysclk_lwla1034_device_connector.jpg.html)
\- 
[![\1](../../assets/hardware/general/\2)](./File:Sysclk_lwla1034_device_usb.jpg.html)
\- 
[![\1](../../assets/hardware/general/\2)](./File:Sysclk_lwla1034_device_open.jpg.html)
\- 
[![\1](../../assets/hardware/general/\2)](./File:Sysclk_lwla1034_pcb_top2.jpg.html)
\- 
[![\1](../../assets/hardware/general/\2)](./File:Sysclk_lwla1034_pcb_bottom2.jpg.html)
\- 
[![\1](../../assets/hardware/general/\2)](./File:Sysclk_lwla1034_altera_cyclone2.jpg.html)
\- 
[![\1](../../assets/hardware/general/\2)](./File:Sysclk_lwla1034_cypress_sram.jpg.html)
\- 
[![\1](../../assets/hardware/general/\2)](./File:Sysclk_lwla1034_cypress_fx2.jpg.html)
\- 
[![\1](../../assets/hardware/general/\2)](./File:Sysclk_lwla1034_24c64n_otherso8_crystal.jpg.html)
\- 
[![\1](../../assets/hardware/general/\2)](./File:Sysclk_lwla1034_crystal_50mhz.jpg.html)
\- 
[![\1](../../assets/hardware/general/\2)](./File:Sysclk_lwla1034_crystal_40mhz.jpg.html)
\- 
[![\1](../../assets/hardware/general/\2)](./File:Sysclk_lwla1034_ams1117_33.jpg.html)
\- 
[![\1](../../assets/hardware/general/\2)](./File:Sysclk_lwla1034_ams1117_12.jpg.html)
(Note: The yellow/greenish markings weren't there, they're added by the photographer) **PCB for another device**: \- 
[![\1](../../assets/hardware/general/\2)](./File:Sysclk_lwla1034_pcb_top.jpg.html)
PCB, top
\- 
[![\1](../../assets/hardware/general/\2)](./File:Sysclk_lwla1034_pcb_bottom.jpg.html)
PCB, bottom
\- 
[![\1](../../assets/hardware/general/\2)](./File:Sysclk_lwla1034_pcb_closeup.jpg.html)
PCB, close-up
\- 
[![\1](../../assets/hardware/general/\2)](./File:Sysclk_lwla1034_chip2.jpg.html)
Cypress FX2
\- 
[![\1](../../assets/hardware/general/\2)](./File:Sysclk_lwla1034_chip3_removed_marking.jpg.html)
SRAM (marking removed)
## Software [![\1](../../assets/hardware/general/\2)](./File:Sysclk_lwla1034_software.png.html) ## Firmware We have received permission from the vendor to distribute the FPGA bitstreams with OpenTraceLab. Thus, the bitstreams are now included in the OpenTraceLab-firmware module. \- The FX2 firmware is loaded from an EEPROM on the board, so that the final USB device descriptor is immediately available on power-up. \- Endpoint 4 is used exclusively for loading a new bitstream into the FPGA. \- Endpoint 2 is used for sending commands to the FPGA firmware, with responses (if any) coming in from endpoint 6. Reverse engineering of the vendor's custom protocol has been completed. See [Sysclk LWLA1034/Protocol](Sysclk_LWLA1034/Protocol.html "Sysclk LWLA1034/Protocol") for the documentation. ## Resources \- [Mcupro blog on CSDN](http://blog.csdn.net/mcupro)
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=Sysclk_LWLA1034&oldid=8752](https://OpenTraceLab.org/w/index.php?title=Sysclk_LWLA1034&oldid=8752)" 
[Categories](specialcategories-specialcategories.md): \- [Device](./Category:Device.html "Category:Device") \- [Logic analyzer](./Category:Logic_analyzer.html "Category:Logic analyzer") \- [Supported](./Category:Supported.html "Category:Supported")

## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
