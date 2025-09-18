# Braintechnology Usb Interface V2.X

| | | |:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------------------------------:| | [![\1](../../assets/hardware/general/\2)](./File:Braintechnology_usb_interface_v26.png.html) | | | Status | supported | | Source code | [fx2lafw](http://github.com/OpenTraceLab/?p=OpenTraceCapture.git;a=tree;f=src/hardware/fx2lafw) | | Channels | 8/16 | | Samplerate | 24MHz | | Samplerate (state) | — | | Triggers | none (SW-only) | | Min/max voltage | -0.5V — 5.25V | | Threshold voltage | Fixed: VIH=2.0V—5.25V, VIL=-0.5V—0.8V | | Memory | none | | Compression | none | | Website | [braintechnology.de](http://www.braintechnology.de/braintechnology/en/usb_fastinterface27.html) | **Braintechnology USB Interface V2.x** The **Braintechnology USB Interface V2.x** is a Cypress FX2 eval board, which can be used as USB-based, 16-channel logic analyzer with up to 24MHz sampling rate. There are various revisions of the hardware, e.g. [V2.5](http://www.braintechnology.de/braintechnology/en/usb_fastinterface25.html), [V2.6](http://www.braintechnology.de/braintechnology/en/usb_fastinterface26.html), and [V2.7](http://www.braintechnology.de/braintechnology/en/usb_fastinterface27.html). In OpenTraceLab, we use the open-source [fx2lafw](Fx2lafw.html "Fx2lafw") firmware for this logic analyzer. See [Braintechnology USB Interface V2.x/Info](Braintechnology_USB_Interface_V2.x/Info.html "Braintechnology USB Interface V2.x/Info") for some more details (such as **lsusb -vvv** output) on the device. 
## Contents 
\- [1 Hardware](Braintechnology_USB_Interface_V2.x.html#Hardware) \- [2 Photos](Braintechnology_USB_Interface_V2.x.html#Photos) \- [3 Protocol](Braintechnology_USB_Interface_V2.x.html#Protocol) \- [4 Resources](Braintechnology_USB_Interface_V2.x.html#Resources) 
## Hardware \- **Main chip**: Cypress CY7C68013A-56PVXC (FX2LP) \- **64kB I2C EEPROM**: Microchip 24LC641 \- **Low-dropout voltage regulator**: ST LD33 \- **Crystal**: 24MHz \- **?**: PDEI ## Photos \- 
[![\1](../../assets/hardware/general/\2)](./File:Braintechnology_usb_interface_v2x_pcb_front.jpg.html)
PCB, front
\- 
[![\1](../../assets/hardware/general/\2)](./File:Braintechnology_usb_interface_v2x_pcb_back.jpg.html)
PCB, back
\- 
[![\1](../../assets/hardware/general/\2)](./File:Braintechnology_usb_interface_v2x_fx2.jpg.html)
Cypress FX2LP
\- 
[![\1](../../assets/hardware/general/\2)](./File:Braintechnology_usb_interface_v2x_eeprom_ldo.jpg.html)
I2C EEPROM, LDO
\- 
[![\1](../../assets/hardware/general/\2)](./File:Braintechnology_usb_interface_v2x_pdei.jpg.html)
PDEI chip
## Protocol Since we use the open-source [fx2lafw](Fx2lafw.html "Fx2lafw") firmware for this device, we don't need to know the protocol. ## Resources \- [Schematics](http://www.braintechnology.de/downstat18/download.php?file=schematicv27.pdf) \- [Various eval board documentation files](http://www.braintechnology.de/braintechnology/en/usb_fastinterface27.html)
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=Braintechnology_USB_Interface_V2.x&oldid=6822](https://OpenTraceLab.org/w/index.php?title=Braintechnology_USB_Interface_V2.x&oldid=6822)" 
[Categories](specialcategories-specialcategories.md): \- [Device](./Category:Device.html "Category:Device") \- [Logic analyzer](./Category:Logic_analyzer.html "Category:Logic analyzer") \- [Supported](./Category:Supported.html "Category:Supported")

## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
