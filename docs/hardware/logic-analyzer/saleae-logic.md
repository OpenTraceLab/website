# Saleae Logic

| | | |:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------------:| | [![\1](../../assets/hardware/general/\2)](./File:Saleae_Logic.png.html) | | | Status | supported | | Source code | [fx2lafw](http://github.com/OpenTraceLab/?p=OpenTraceCapture.git;a=tree;f=src/hardware/fx2lafw) | | Channels | 8 | | Samplerate | 24MHz | | Samplerate (state) | — | | Triggers | none (SW-only) | | Min/max voltage | -0.5V — 5.25V | | Threshold voltage | Fixed: VIH=2.0V—5.25V, VIL=-0.5V—0.8V | | Memory | none | | Compression | none | | Website | [saleae.com](http://www.saleae.com/logic/) | **Saleae Logic** The **Saleae Logic** is a USB-based, 8-channel logic analyzer with up to 24MHz sampling rate. The unit itself is very small, and has a USB 2.0 port connecting it to a PC (and powering the unit) and a connector for the 8 + 1 probe set. It is built around a Cypress EZ-USB FX2LP microcontroller — an 8051-compatible chip with built-in USB 2.0 controller. It can sample 8 channels up to 24MHz. In OpenTraceLab, we use the open-source [fx2lafw](Fx2lafw.html "Fx2lafw") firmware for this logic analyzer. See [Saleae Logic/Info](Saleae_Logic/Info.html "Saleae Logic/Info") for more details (such as **lsusb -vvv** output) about the device. See [Saleae Logic16](Saleae_Logic16.html "Saleae Logic16") for the successor product of the Saleae Logic. 
## Contents 
\- [1 Hardware](Saleae_Logic.html#Hardware) \- [2 Photos](Saleae_Logic.html#Photos) \- [3 Protocol](Saleae_Logic.html#Protocol) \- [4 Resources](Saleae_Logic.html#Resources) 
## Hardware \- **Main chip:** Cypress CY7C68013A-56PVXC (FX2LP) \- **ESD protection**: ST DVIULC6-4SC6 \- **3.3V voltage regulator**: ST LD33C \- **I2C EEPROM**: Microchip 24LC00 \- **Crystal**: 24MHz The case has four **Torx T2** screws you need to remove in order to be able to open it. ## Photos \- 
[![\1](../../assets/hardware/general/\2)](./File:Saleae_Logic.jpg.html)
Device, top
\- 
[![\1](../../assets/hardware/general/\2)](./File:Saleae_logic.jpg.html)
Device with two E-Z-Hooks
\- 
[![\1](../../assets/hardware/general/\2)](./File:Saleae_logic_opened.jpg.html)
Device, open
\- 
[![\1](../../assets/hardware/general/\2)](./File:Saleae_logic_pcb_front.jpg.html)
PCB, front
\- 
[![\1](../../assets/hardware/general/\2)](./File:Saleae_logic_pcb_back.jpg.html)
PCB, back
\- 
[![\1](../../assets/hardware/general/\2)](./File:Saleae_logic_collection.jpg.html)
Saleae Logic collection
## Protocol Since we use the open-source [fx2lafw](Fx2lafw.html "Fx2lafw") firmware for this device, we don't need to know the protocol. However, for those interested in this, see our old [vendor protocol docs](Saleae_Logic/Info.html#Vendor_USB_protocol "Saleae Logic/Info"). ## Resources \- [User's guide](http://downloads.saleae.com/Logic+Guide.pdf) \- [Vendor software](http://www.saleae.com/downloads) \- [SDKs](http://community.saleae.com/)
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=Saleae_Logic&oldid=6820](https://OpenTraceLab.org/w/index.php?title=Saleae_Logic&oldid=6820)" 
[Categories](specialcategories-specialcategories.md): \- [Device](./Category:Device.html "Category:Device") \- [Logic analyzer](./Category:Logic_analyzer.html "Category:Logic analyzer") \- [Supported](./Category:Supported.html "Category:Supported")

## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
