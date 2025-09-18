# Braintechnology Usb Lps

| | | |:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------------------------------------------:| | [![\1](../../assets/hardware/general/\2)](./File:Braintechnology_usb_lps.png.html) | | | Status | supported | | Source code | [fx2lafw](http://github.com/OpenTraceLab/?p=OpenTraceCapture.git;a=tree;f=src/hardware/fx2lafw) | | Channels | 8/16 | | Samplerate | 24MHz | | Samplerate (state) | — | | Triggers | none (SW-only) | | Min/max voltage | -0.5V — 5.25V | | Threshold voltage | Fixed: VIH=2.0V—5.25V, VIL=-0.5V—0.8V | | Memory | none | | Compression | none | | Website | [braintechnology.de](http://www.braintechnology.de/webshop/catalog/product_info.php?&products_id=105) | **Braintechnology USB-LPS** The **Braintechnology USB-LPS** is a Cypress FX2 based 16-channel, 24MHz, USB-based logic analyzer and signal/pattern generator. In OpenTraceLab, the open-source [fx2lafw](Fx2lafw.html "Fx2lafw") firmware and driver is used for this device. See [Braintechnology USB-LPS/Info](Braintechnology_USB-LPS/Info.html "Braintechnology USB-LPS/Info") for some more details (such as **lsusb -v** output) on the device. 
## Contents 
\- [1 Hardware](Braintechnology_USB-LPS.html#Hardware) \- [2 Photos](Braintechnology_USB-LPS.html#Photos) \- [3 Protocol](Braintechnology_USB-LPS.html#Protocol) \- [4 Resources](Braintechnology_USB-LPS.html#Resources) 
## Hardware \- **Main chip:** Cypress CY7C68013A-56PVXC (FX2LP) \- **I²C EEPROM**: Atmel ATtiny13-20SU \- **3.3V voltage regulator**: LD33 \- **Crystal**: 24MHz ## Photos \- 
[![\1](../../assets/hardware/general/\2)](./File:Braintechnology_usb_lps.jpg.html)
Device, front
\- 
[![\1](../../assets/hardware/general/\2)](./File:Braintechnology_usb_lps_pcb_front.jpg.html)
PCB, front
\- 
[![\1](../../assets/hardware/general/\2)](./File:Braintechnology_usb_lps_pcb_front_details.jpg.html)
PCB, front, details
\- 
[![\1](../../assets/hardware/general/\2)](./File:Braintechnology_usb_lps_pcb_back.jpg.html)
PCB, back
## Protocol Since we use the open-source [fx2lafw](Fx2lafw.html "Fx2lafw") firmware for this device, we don't need to know the protocol. However, for those interested in this, see our old [vendor protocol docs](Braintechnology_USB-LPS/Info.html#Vendor_USB_protocol "Braintechnology USB-LPS/Info"). ## Resources \- [Manual](http://www.braintechnology.de/downstat18/download.php?file=lps_doc.pdf) \- [Vendor software](http://www.braintechnology.de/downstat18/download.php?file=lpssetup10723.exe) \- [Driver](http://www.braintechnology.de/downstat18/download.php?file=lpsdriver_32_64bit.zip)
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=Braintechnology_USB-LPS&oldid=12472](https://OpenTraceLab.org/w/index.php?title=Braintechnology_USB-LPS&oldid=12472)" 
[Categories](specialcategories-specialcategories.md): \- [Device](./Category:Device.html "Category:Device") \- [Logic analyzer](./Category:Logic_analyzer.html "Category:Logic analyzer") \- [Supported](./Category:Supported.html "Category:Supported")

## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
