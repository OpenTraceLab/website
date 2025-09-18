# Mcu123 Usbee Ax Pro Clone

| | | |:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------------------:| | [![\1](../../assets/hardware/general/\2)](./File:Usbee_ax_clone_front.png.html) | | | Status | supported | | Source code | [fx2lafw](http://github.com/OpenTraceLab/?p=OpenTraceCapture.git;a=tree;f=src/hardware/fx2lafw) | | Channels | 8 | | Samplerate | 24MHz | | Samplerate (state) | — | | Triggers | none (SW-only) | | Min/max voltage | -0.5V — 5.25V | | Threshold voltage | Fixed: VIH=2.0V—5.25V, VIL=-0.5V—0.8V | | Memory | none | | Compression | none | | Price range | \$5 - \$10 | | Website | [dx.com](http://dx.com/p/logic-analyzer-w-dupont-lines-and-usb-cable-for-scm-black-148945) | **MCU123 USBee AX Pro clone** The **MCU123 USBee AX Pro clone** is a USB-based, 8-channel logic analyzer with up to 24MHz sampling rate. It is a clone of the [CWAV USBee AX-Pro](https://OpenTraceLab.org/w/index.php?title=CWAV_USBee_AX-Pro&action=edit&redlink=1 "CWAV USBee AX-Pro \(page does not exist\)"), but it doesn't have analog (only 8-channel digital) sampling capabilities. It's also *very* similar to the [MCU123 Saleae Logic clone](MCU123_Saleae_Logic_clone.html "MCU123 Saleae Logic clone") minus the different USB vendor/device IDs. In OpenTraceLab, we use the open-source [fx2lafw](Fx2lafw.html "Fx2lafw") firmware for this logic analyzer. See [MCU123 USBee AX Pro clone/Info](MCU123_USBee_AX_Pro_clone/Info.html "MCU123 USBee AX Pro clone/Info") for more detailed information on the device. 
## Contents 
\- [1 Hardware](MCU123_USBee_AX_Pro_clone.html#Hardware) \- [2 Photos](MCU123_USBee_AX_Pro_clone.html#Photos) \- [3 Protocol](MCU123_USBee_AX_Pro_clone.html#Protocol) \- [4 Resources](MCU123_USBee_AX_Pro_clone.html#Resources) 
## Hardware \- **Main chip**: Cypress CY7C68013A-56PVXC (FX2LP) \- **Input buffer**: NXP 74HC245 (markings: "NXP HC245 2A7K508 UnD2 18E") \- **256-byte I2C EEPROM**: Atmel AT24C02 (markings: "ATMEL218 24C02N SU27 D") \- **3.3V low-dropout voltage regulator**: Advanced Monolithic Systems AMS1117-3.3 (markings: "AMS1117 3.3 HT240E") \- **24MHz crystal**: 24.000 ## Photos \- 
[![\1](../../assets/hardware/general/\2)](./File:Usbee_ax_clone_front.png.html)
Device, front
\- 
[![\1](../../assets/hardware/general/\2)](./File:Usbee_ax_clone_angle.jpg.html)
Device, angle
\- 
[![\1](../../assets/hardware/general/\2)](./File:Usbee_ax_clone_back.jpg.html)
Device, back
\- 
[![\1](../../assets/hardware/general/\2)](./File:Usbee_ax_clone_opened.jpg.html)
Device, opened
\- 
[![\1](../../assets/hardware/general/\2)](./File:Usbee_ax_clone_pcb_front.jpg.html)
PCB, front
\- 
[![\1](../../assets/hardware/general/\2)](./File:Usbee_ax_clone_pcb_back.jpg.html)
PCB, back
## Protocol Since we use the open-source [fx2lafw](Fx2lafw.html "Fx2lafw") firmware for this device, we don't need to know the protocol. ## Resources \- [DealExtreme online shop](http://dx.com/p/logic-analyzer-w-dupont-lines-and-usb-cable-for-scm-black-148945)
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=MCU123_USBee_AX_Pro_clone&oldid=14391](https://OpenTraceLab.org/w/index.php?title=MCU123_USBee_AX_Pro_clone&oldid=14391)" 
[Categories](specialcategories-specialcategories.md): \- [Device](./Category:Device.html "Category:Device") \- [Logic analyzer](./Category:Logic_analyzer.html "Category:Logic analyzer") \- [Supported](./Category:Supported.html "Category:Supported")

## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
