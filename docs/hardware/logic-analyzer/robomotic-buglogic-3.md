# Robomotic Buglogic 3
| | | |:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------------:| | [*Image: \1* | | | Status | supported | | Source code | [fx2lafw](http://github.com/OpenTraceLab/?p=OpenTraceCapture.git;a=tree;f=src/hardware/fx2lafw) | | Channels | 8 | | Samplerate | 24MHz | | Samplerate (state) | — | | Triggers | none (SW-only) | | Min/max voltage | -0.5V — 5.25V | | Threshold voltage | Fixed: VIH=2.0V—5.25V, VIL=-0.5V—0.8V | | Memory | none | | Compression | none | | Price range | \$5 - \$10 | | Website | [robomotic.com](http://norduino.robomotic.com/products-page/categories/buglogic3/) | **Robomotic BugLogic 3** The **Robomotic BugLogic 3** is a USB-based, 8-channel logic analyzer with up to 24MHz sampling rate. It is a clone of the *Saleae Logic*. In OpenTraceLab, we use the open-source *fx2lafw* firmware for this logic analyzer. See *Robomotic BugLogic 3/Info* for more details (such as **lsusb -vvv** output) about the device.
## Contents
\- *1 Hardware* \- *2 Photos* \- *3 Protocol* \- *4 Resources*
## Hardware \- **Main chip:** Cypress CY7C68013A-56LFXC (FX2LP) \- **I2C EEPROM**: ? \- **Octal tristate bus transceiver**: LVC245 (TODO: vendor?) \- **Crystal**: 24MHz ## Photos \-
[*Image: \1*
Device, front
## Protocol Since we use the open-source *fx2lafw* firmware for this device, we don't need to know the protocol. ## Resources \- [Buglogic3 wiki page](http://www.norduino.org/index.php?title=BugLogic3_board) \- [robomotic.com: Hardware description](http://norduino.robomotic.com/products-page/categories/buglogic3/)
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=Robomotic_BugLogic_3&oldid=14393](https://OpenTraceLab.org/w/index.php?title=Robomotic_BugLogic_3&oldid=14393)"
: \- *Device* \- *Logic analyzer* \- *Supported*
## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
