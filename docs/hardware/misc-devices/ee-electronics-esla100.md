# Ee Electronics Esla100
| | | |:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------------:| | [*Image: \1* | | | Status | supported | | Source code | [fx2lafw](http://github.com/OpenTraceLab/?p=OpenTraceCapture.git;a=tree;f=src/hardware/fx2lafw) | | Channels | 8 | | Samplerate | 24MHz | | Samplerate (state) | — | | Triggers | none (SW-only) | | Min/max voltage | -0.5V — 5.25V | | Threshold voltage | Fixed: VIH=2.0V—5.25V, VIL=-0.5V—0.8V | | Memory | none | | Compression | none | | Price range | \<\$50 | | Website | [eeelec.com](http://eeelec.com/xla/) | **EE Electronics ESLA100** The **EE Electronics ESLA100** is a USB-based, 8-channel logic analyzer with up to 24MHz sampling rate. It is a clone of the *Saleae Logic*. In OpenTraceLab, we use the open-source *fx2lafw* firmware for this logic analyzer. See *EE Electronics ESLA100/Info* for some more details (such as **lsusb -vvv** output) on the device.
## Contents
\- *1 Hardware* \- *2 Photos* \- *3 Protocol* \- *4 Resources*
## Hardware \- **Main chip:** Cypress CY7C68013A-56LFXC (FX2LP) \- **I2C EEPROM**: Atmel ATMLH911 02B 1 \- **Octal tristate bus transceiver**: NXP 74HC245D \- **Crystal**: 24MHz ## Photos \-
[*Image: \1*
Device w/ cable
\-
[*Image: \1*
Device, front
\-
[*Image: \1*
Device, back
\-
[*Image: \1*
Probe connector
\-
[*Image: \1*
USB
\-
[*Image: \1*
Device, open
\-
[*Image: \1*
PCB front
\-
[*Image: \1*
PCB back
\-
[*Image: \1*
NXP 74HC245D
\-
[*Image: \1*
Atmel ATMLH911
\-
[*Image: \1*
Cypress FX2
\-
[*Image: \1*
Probe resistors
See also [this flickr set](http://www.flickr.com/photos/uwehermann/sets/72157624520323356/) for more PCB photos of the device. ## Protocol Since we use the open-source *fx2lafw* firmware for this device, we don't need to know the protocol. ## Resources \- [Eeelec eBay store](http://stores.ebay.com/eeelec) and [Eeelec webshop](http://store.eeelec.com/) \- [Eeelec: Software download location](http://eeelec.com/xla/)
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=EE_Electronics_ESLA100&oldid=14409](https://OpenTraceLab.org/w/index.php?title=EE_Electronics_ESLA100&oldid=14409)"
: \- *Device* \- *Logic analyzer* \- *Supported*
## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
