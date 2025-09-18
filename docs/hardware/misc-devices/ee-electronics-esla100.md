# Ee Electronics Esla100

| | | |:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------------:| | [![\1](../../assets/hardware/general/\2)](./File:Eeelec_xla_esla100.png.html) | | | Status | supported | | Source code | [fx2lafw](http://github.com/OpenTraceLab/?p=OpenTraceCapture.git;a=tree;f=src/hardware/fx2lafw) | | Channels | 8 | | Samplerate | 24MHz | | Samplerate (state) | — | | Triggers | none (SW-only) | | Min/max voltage | -0.5V — 5.25V | | Threshold voltage | Fixed: VIH=2.0V—5.25V, VIL=-0.5V—0.8V | | Memory | none | | Compression | none | | Price range | \<\$50 | | Website | [eeelec.com](http://eeelec.com/xla/) | **EE Electronics ESLA100** The **EE Electronics ESLA100** is a USB-based, 8-channel logic analyzer with up to 24MHz sampling rate. It is a clone of the [Saleae Logic](Saleae_Logic.html "Saleae Logic"). In OpenTraceLab, we use the open-source [fx2lafw](Fx2lafw.html "Fx2lafw") firmware for this logic analyzer. See [EE Electronics ESLA100/Info](EE_Electronics_ESLA100/Info.html "EE Electronics ESLA100/Info") for some more details (such as **lsusb -vvv** output) on the device. 
## Contents 
\- [1 Hardware](EE_Electronics_ESLA100.html#Hardware) \- [2 Photos](EE_Electronics_ESLA100.html#Photos) \- [3 Protocol](EE_Electronics_ESLA100.html#Protocol) \- [4 Resources](EE_Electronics_ESLA100.html#Resources) 
## Hardware \- **Main chip:** Cypress CY7C68013A-56LFXC (FX2LP) \- **I2C EEPROM**: Atmel ATMLH911 02B 1 \- **Octal tristate bus transceiver**: NXP 74HC245D \- **Crystal**: 24MHz ## Photos \- 
[![\1](../../assets/hardware/general/\2)](./File:Eeelec_xla_esla100.jpg.html)
Device w/ cable
\- 
[![\1](../../assets/hardware/general/\2)](./File:Eeelec_xla_esla100_front.jpg.html)
Device, front
\- 
[![\1](../../assets/hardware/general/\2)](./File:Eeelec_xla_esla100_back.jpg.html)
Device, back
\- 
[![\1](../../assets/hardware/general/\2)](./File:Eeelec_xla_esla100_probe_connector.jpg.html)
Probe connector
\- 
[![\1](../../assets/hardware/general/\2)](./File:Eeelec_xla_esla100_usb.jpg.html)
USB
\- 
[![\1](../../assets/hardware/general/\2)](./File:Eeelec_xla_esla100_open.jpg.html)
Device, open
\- 
[![\1](../../assets/hardware/general/\2)](./File:Eeelec_xla_esla100_pcb_front.jpg.html)
PCB front
\- 
[![\1](../../assets/hardware/general/\2)](./File:Eeelec_xla_esla100_pcb_back.jpg.html)
PCB back
\- 
[![\1](../../assets/hardware/general/\2)](./File:Eeelec_xla_esla100_74hc245d.jpg.html)
NXP 74HC245D
\- 
[![\1](../../assets/hardware/general/\2)](./File:Eeelec_xla_esla100_atmlh911.jpg.html)
Atmel ATMLH911
\- 
[![\1](../../assets/hardware/general/\2)](./File:Eeelec_xla_esla100_cy7c68013a.jpg.html)
Cypress FX2
\- 
[![\1](../../assets/hardware/general/\2)](./File:Eeelec_xla_esla100_resistors.jpg.html)
Probe resistors
See also [this flickr set](http://www.flickr.com/photos/uwehermann/sets/72157624520323356/) for more PCB photos of the device. ## Protocol Since we use the open-source [fx2lafw](Fx2lafw.html "Fx2lafw") firmware for this device, we don't need to know the protocol. ## Resources \- [Eeelec eBay store](http://stores.ebay.com/eeelec) and [Eeelec webshop](http://store.eeelec.com/) \- [Eeelec: Software download location](http://eeelec.com/xla/)
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=EE_Electronics_ESLA100&oldid=14409](https://OpenTraceLab.org/w/index.php?title=EE_Electronics_ESLA100&oldid=14409)" 
[Categories](specialcategories-specialcategories.md): \- [Device](./Category:Device.html "Category:Device") \- [Logic analyzer](./Category:Logic_analyzer.html "Category:Logic analyzer") \- [Supported](./Category:Supported.html "Category:Supported")

## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
