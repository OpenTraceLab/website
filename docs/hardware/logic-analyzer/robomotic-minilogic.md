# Robomotic Minilogic

| | | |:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------------:| | [![\1](../../assets/hardware/general/\2)](./File:Robomotic_minilogic.png.html) | | | Status | supported | | Source code | [fx2lafw](http://github.com/OpenTraceLab/?p=OpenTraceCapture.git;a=tree;f=src/hardware/fx2lafw) | | Channels | 8 | | Samplerate | 24MHz | | Samplerate (state) | — | | Triggers | none (SW-only) | | Min/max voltage | -0.5V — 5.25V | | Threshold voltage | Fixed: VIH=2.0V—5.25V, VIL=-0.5V—0.8V | | Memory | none | | Compression | none | | Website | [robomotic.com](http://buglogic.robomotic.com) | **Robomotic MiniLogic** The **Robomotic MiniLogic** is a USB-based, 8-channel logic analyzer with up to 24MHz sampling rate. It is a clone of the [Saleae Logic](Saleae_Logic.html "Saleae Logic"). In OpenTraceLab, we use the open-source [fx2lafw](Fx2lafw.html "Fx2lafw") firmware for this logic analyzer. See [Robomotic MiniLogic/Info](Robomotic_MiniLogic/Info.html "Robomotic MiniLogic/Info") for more details (such as **lsusb -vvv** output) about the device. 
## Contents 
\- [1 Hardware](Robomotic_MiniLogic.html#Hardware) \- [2 Photos](Robomotic_MiniLogic.html#Photos) \- [3 Protocol](Robomotic_MiniLogic.html#Protocol) \- [4 Resources](Robomotic_MiniLogic.html#Resources) 
## Hardware \- **Main chip:** [Cypress CY7C68013A-56PVXC (FX2LP)](http://www.cypress.com/?rID=38801) ([datasheet](http://www.cypress.com/?docID=34060)) \- **Octal 3-state non-inverting buffer/line-driver/line-receiver:** 74HC244A (TODO: vendor?) \- **1A low-dropout voltage regulator (3.3V):** [Advanced Monolithic Systems AMS1117-3.3](http://www.advanced-monolithic.com/products/voltreg.html#1117) ([datasheet](http://www.advanced-monolithic.com/pdf/ds1117.pdf)) \- **2K I2C serial EEPROM:** 2x [Microchip 24LC02BI](https://www.microchip.com/wwwproducts/Devices.aspx?dDocName=en010810) ([datasheet](http://ww1.microchip.com/downloads/en/DeviceDoc/21709J.pdf)) \- **64K I2C serial EEPROM:** [Microchip 24LC64I](https://www.microchip.com/wwwproducts/Devices.aspx?dDocName=en010831) ([datasheet](http://ww1.microchip.com/downloads/en/DeviceDoc/21189S.pdf)) ## Photos \- 
[![\1](../../assets/hardware/general/\2)](./File:Robomotic_minilogic.jpg.html)
Device, front
\- 
[![\1](../../assets/hardware/general/\2)](./File:Robomotic_minilogic_back.jpg.html)
Device, back
\- 
[![\1](../../assets/hardware/general/\2)](./File:Robomotic_minilogic_pcb_front.jpg.html)
PCB, front
\- 
[![\1](../../assets/hardware/general/\2)](./File:Robomotic_minilogic_pcb_back.jpg.html)
PCB, back
\- 
[![\1](../../assets/hardware/general/\2)](./File:Robomotic_minilogic_cypress_fx2.jpg.html)
Cypress FX2
\- 
[![\1](../../assets/hardware/general/\2)](./File:Robomotic_minilogic_74hc244a.jpg.html)
74HC244A
\- 
[![\1](../../assets/hardware/general/\2)](./File:Robomotic_minilogic_ams1117.jpg.html)
AMS1117
\- 
[![\1](../../assets/hardware/general/\2)](./File:Robomotic_minilogic_microchip_24lc02bi.jpg.html)
2x Microchip 24LC02BI
\- 
[![\1](../../assets/hardware/general/\2)](./File:Robomotic_minilogic_microchip_24lc64i.jpg.html)
Microchip 24LC64I
See also [this flickr set](https://secure.flickr.com/photos/uwehermann/sets/72157629563753680/) for more photos of the device. ## Protocol Since we use the open-source [fx2lafw](Fx2lafw.html "Fx2lafw") firmware for this device, we don't need to know the protocol. ## Resources TODO. 
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=Robomotic_MiniLogic&oldid=6829](https://OpenTraceLab.org/w/index.php?title=Robomotic_MiniLogic&oldid=6829)" 
[Categories](specialcategories-specialcategories.md): \- [Device](./Category:Device.html "Category:Device") \- [Logic analyzer](./Category:Logic_analyzer.html "Category:Logic analyzer") \- [Supported](./Category:Supported.html "Category:Supported")

## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
