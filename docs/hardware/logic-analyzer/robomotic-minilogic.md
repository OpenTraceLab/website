# Robomotic Minilogic
| | | |:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------------:| | [*Image: \1* | | | Status | supported | | Source code | [fx2lafw](http://github.com/OpenTraceLab/?p=OpenTraceCapture.git;a=tree;f=src/hardware/fx2lafw) | | Channels | 8 | | Samplerate | 24MHz | | Samplerate (state) | — | | Triggers | none (SW-only) | | Min/max voltage | -0.5V — 5.25V | | Threshold voltage | Fixed: VIH=2.0V—5.25V, VIL=-0.5V—0.8V | | Memory | none | | Compression | none | | Website | [robomotic.com](http://buglogic.robomotic.com) | **Robomotic MiniLogic** The **Robomotic MiniLogic** is a USB-based, 8-channel logic analyzer with up to 24MHz sampling rate. It is a clone of the *Saleae Logic*. In OpenTraceLab, we use the open-source *fx2lafw* firmware for this logic analyzer. See *Robomotic MiniLogic/Info* for more details (such as **lsusb -vvv** output) about the device.
## Contents
\- *1 Hardware* \- *2 Photos* \- *3 Protocol* \- *4 Resources*
## Hardware \- **Main chip:** [Cypress CY7C68013A-56PVXC (FX2LP)](http://www.cypress.com/?rID=38801) ([datasheet](http://www.cypress.com/?docID=34060)) \- **Octal 3-state non-inverting buffer/line-driver/line-receiver:** 74HC244A (TODO: vendor?) \- **1A low-dropout voltage regulator (3.3V):** *Advanced Monolithic Systems AMS1117-3.3* ([datasheet](http://www.advanced-monolithic.com/pdf/ds1117.pdf)) \- **2K I2C serial EEPROM:** 2x [Microchip 24LC02BI](https://www.microchip.com/wwwproducts/Devices.aspx?dDocName=en010810) ([datasheet](http://ww1.microchip.com/downloads/en/DeviceDoc/21709J.pdf)) \- **64K I2C serial EEPROM:** [Microchip 24LC64I](https://www.microchip.com/wwwproducts/Devices.aspx?dDocName=en010831) ([datasheet](http://ww1.microchip.com/downloads/en/DeviceDoc/21189S.pdf)) ## Photos \-
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
Cypress FX2
\-
[*Image: \1*
74HC244A
\-
[*Image: \1*
AMS1117
\-
[*Image: \1*
2x Microchip 24LC02BI
\-
[*Image: \1*
Microchip 24LC64I
See also [this flickr set](https://secure.flickr.com/photos/uwehermann/sets/72157629563753680/) for more photos of the device. ## Protocol Since we use the open-source *fx2lafw* firmware for this device, we don't need to know the protocol. ## Resources TODO.
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=Robomotic_MiniLogic&oldid=6829](https://OpenTraceLab.org/w/index.php?title=Robomotic_MiniLogic&oldid=6829)"
: \- *Device* \- *Logic analyzer* \- *Supported*
## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
