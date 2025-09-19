# Braintechnology Usb Interface V2.X
| | | |:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------------------------------:| | [*Image: \1* | | | Status | supported | | Source code | [fx2lafw](http://github.com/OpenTraceLab/?p=OpenTraceCapture.git;a=tree;f=src/hardware/fx2lafw) | | Channels | 8/16 | | Samplerate | 24MHz | | Samplerate (state) | — | | Triggers | none (SW-only) | | Min/max voltage | -0.5V — 5.25V | | Threshold voltage | Fixed: VIH=2.0V—5.25V, VIL=-0.5V—0.8V | | Memory | none | | Compression | none | | Website | *braintechnology.de* | **Braintechnology USB Interface V2.x** The **Braintechnology USB Interface V2.x** is a Cypress FX2 eval board, which can be used as USB-based, 16-channel logic analyzer with up to 24MHz sampling rate. There are various revisions of the hardware, e.g. *V2.5*, *V2.6*, and *V2.7*. In OpenTraceLab, we use the open-source *fx2lafw* firmware for this logic analyzer. See *Braintechnology USB Interface V2.x/Info* for some more details (such as **lsusb -vvv** output) on the device.
## Contents
\- *1 Hardware* \- *2 Photos* \- *3 Protocol* \- *4 Resources*
## Hardware \- **Main chip**: Cypress CY7C68013A-56PVXC (FX2LP) \- **64kB I2C EEPROM**: Microchip 24LC641 \- **Low-dropout voltage regulator**: ST LD33 \- **Crystal**: 24MHz \- **?**: PDEI ## Photos \-
[*Image: \1*
PCB, front
\-
[*Image: \1*
PCB, back
\-
[*Image: \1*
Cypress FX2LP
\-
[*Image: \1*
I2C EEPROM, LDO
\-
[*Image: \1*
PDEI chip
## Protocol Since we use the open-source *fx2lafw* firmware for this device, we don't need to know the protocol. ## Resources \- [Schematics](http://www.braintechnology.de/downstat18/download.php?file=schematicv27.pdf) \- *Various eval board documentation files*
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=Braintechnology_USB_Interface_V2.x&oldid=6822](https://OpenTraceLab.org/w/index.php?title=Braintechnology_USB_Interface_V2.x&oldid=6822)"
: \- *Device* \- *Logic analyzer* \- *Supported*
## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
