# Cwav Usbee Sx
| | | |:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------------:| | [*Image: \1* | | | Status | supported | | Source code | [fx2lafw](http://github.com/OpenTraceLab/?p=OpenTraceCapture.git;a=tree;f=src/hardware/fx2lafw) | | Channels | 8 | | Samplerate | 24MHz | | Samplerate (state) | — | | Triggers | none (SW-only) | | Min/max voltage | max. 5.5V | | Threshold voltage | Fixed: VIH=1.4V, VIL=0.8V | | Memory | none | | Compression | none | | Price range | \$130 | | Website | *usbee.com* | **CWAV USBee SX** The **USBee SX** is a USB-based, 8-channel logic analyzer (and signal generator) with up to 24MHz sampling rate. In OpenTraceLab, we use the open-source *fx2lafw* firmware for this logic analyzer. See *CWAV USBee SX/Info* for some more details (such as **lsusb -vvv** output) on the device. CWAV, Inc. [has been closed and no longer sells](http://usbee.com/company.htm) the USBee test pods (has chosen to go out of business effective September 10, 2015). But there are a lot of clones, like *MCU123 USBee AX Pro clone*. Just search for **24mhz 8ch logic analyzer** on <http://ebay.com/> or <http://aliexpress.com/> for one (usually under \$10).
## Contents
\- *1 Hardware* \- *2 Photos* \- *3 Protocol* \- *4 Resources*
## Hardware \- **Main chip**: Cypress CY7C68013A-56PVXC (FX2LP) \- **Note:** Older versions used the Cypress CY7C68013-56PVC (FX2), which is different in some ways (e.g. less SRAM) \- **3.3V voltage regulator**: ST LD33 \- **I2C EEPROM**: Microchip 24LC01B \- **Crystal**: 24MHz ## Photos **New version with Cypress CY7C68013A (FX2LP):** \-
[*Image: \1*
Device, front
\-
[*Image: \1*
Device, back
\-
[*Image: \1*
Device, open
\-
[*Image: \1*
PCB, front
\-
[*Image: \1*
PCB, back
**Old version with Cypress CY7C68013 (FX2):** \-
[*Image: \1*
Device, front
\-
[*Image: \1*
Device, back
\-
[*Image: \1*
PCB, front
\-
[*Image: \1*
PCB, back
\-
[*Image: \1*
"USBee ZX" marking
## Protocol Since we use the open-source *fx2lafw* firmware for this device, we don't need to know the protocol. However, for those interested in this, someone else has already [decoded most of it](https://blog.visucore.com/tags/usbee). ## Resources \- [USBee SX help files](http://usbee.com/software/ZXHelpFiles.zip) \- [USBee Suite manual](http://usbee.com/usbeesuitemanual.pdf) \- [Vendor software](http://usbee.com/usbeesuitesw.zip) \- [Visucore Blog: JTAG using USBee SX](https://blog.visucore.com/2010/5/23/jtag-using-cypress-fx2-usb) \- [Visucore Blog: PWM on the USBee with custom firmware](https://blog.visucore.com/2010/5/28/pwm-on-the-usbee-hardware-using-custom-firmware)
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=CWAV_USBee_SX&oldid=14408](https://OpenTraceLab.org/w/index.php?title=CWAV_USBee_SX&oldid=14408)"
: \- *Device* \- *Logic analyzer* \- *Supported*
## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
