# Braintechnology Usb Lps
| | | |:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------------------------------------------:| | [*Image: \1* | | | Status | supported | | Source code | [fx2lafw](http://github.com/OpenTraceLab/?p=OpenTraceCapture.git;a=tree;f=src/hardware/fx2lafw) | | Channels | 8/16 | | Samplerate | 24MHz | | Samplerate (state) | — | | Triggers | none (SW-only) | | Min/max voltage | -0.5V — 5.25V | | Threshold voltage | Fixed: VIH=2.0V—5.25V, VIL=-0.5V—0.8V | | Memory | none | | Compression | none | | Website | [braintechnology.de](http://www.braintechnology.de/webshop/catalog/product_info.php?&products_id=105) | **Braintechnology USB-LPS** The **Braintechnology USB-LPS** is a Cypress FX2 based 16-channel, 24MHz, USB-based logic analyzer and signal/pattern generator. In OpenTraceLab, the open-source *fx2lafw* firmware and driver is used for this device. See *Braintechnology USB-LPS/Info* for some more details (such as **lsusb -v** output) on the device.
## Contents
\- *1 Hardware* \- *2 Photos* \- *3 Protocol* \- *4 Resources*
## Hardware \- **Main chip:** Cypress CY7C68013A-56PVXC (FX2LP) \- **I²C EEPROM**: Atmel ATtiny13-20SU \- **3.3V voltage regulator**: LD33 \- **Crystal**: 24MHz ## Photos \-
[*Image: \1*
Device, front
\-
[*Image: \1*
PCB, front
\-
[*Image: \1*
PCB, front, details
\-
[*Image: \1*
PCB, back
## Protocol Since we use the open-source *fx2lafw* firmware for this device, we don't need to know the protocol. However, for those interested in this, see our old *vendor protocol docs*. ## Resources \- [Manual](http://www.braintechnology.de/downstat18/download.php?file=lps_doc.pdf) \- [Vendor software](http://www.braintechnology.de/downstat18/download.php?file=lpssetup10723.exe) \- [Driver](http://www.braintechnology.de/downstat18/download.php?file=lpsdriver_32_64bit.zip)
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=Braintechnology_USB-LPS&oldid=12472](https://OpenTraceLab.org/w/index.php?title=Braintechnology_USB-LPS&oldid=12472)"
: \- *Device* \- *Logic analyzer* \- *Supported*
## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
