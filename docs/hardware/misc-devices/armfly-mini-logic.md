# Armfly Mini Logic
| | | |:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------------:| | [*Image: \1* | | | Status | supported | | Source code | [fx2lafw](http://github.com/OpenTraceLab/?p=OpenTraceCapture.git;a=tree;f=src/hardware/fx2lafw) | | Channels | 8 | | Samplerate | 24MHz | | Samplerate (state) | — | | Triggers | none (SW-only) | | Min/max voltage | -0.5V — 5.25V | | Threshold voltage | Fixed: VIH=2.0V—5.25V, VIL=-0.5V—0.8V | | Memory | none | | Compression | none | | Price range | \$5 - \$10 | | Website | [armfly.com](http://www.armfly.com/product/Mini-Logic/mini-logic.htm) | **ARMFLY Mini-Logic** The **ARMFLY Mini-Logic** is a USB-based, 8-channel logic analyzer with up to 24MHz sampling rate. It is a clone of the [CWAV USBee AX-Pro](https://OpenTraceLab.org/w/index.php?title=CWAV_USBee_AX-Pro&action=edit&redlink=1 "CWAV USBee AX-Pro \(page does not exist\)"), but it doesn't have analog (only 8-channel digital) sampling capabilities. There is an "[RS232 RS485 RS422 CAN converter](http://item.taobao.com/item.htm?id=16943624739)" add-on board for more functionality (not supported in OpenTraceLab, though). In OpenTraceLab, we use the open-source *fx2lafw* firmware for this logic analyzer. See *ARMFLY Mini-Logic/Info* for more detailed information on the device.
## Contents
\- *1 Hardware* \- *2 Photos* \- *3 Protocol* \- *4 Resources*
## Hardware \- **Main chip**: Cypress CY7C68013A-56LTXC (FX2LP) \- **I2C EEPROM**: Atmel ATML920 24C02N SU27 D \- **Low-dropout voltage regulator**: Advanced Monolithic Systems AMS1117-3.3 \- **24MHz crystal**: 24.000 ## Photos \-
[*Image: \1*
Device, open 1
\-
[*Image: \1*
Device, open 2
\-
[*Image: \1*
PCB, front
\-
[*Image: \1*
PCB, back
## Protocol Since we use the open-source *fx2lafw* firmware for this device, we don't need to know the protocol. ## Resources \- [ARMFLY Taobao shop](http://item.taobao.com/item.htm?id=14408505465) ([English translation](http://translate.google.com/translate?hl=en&sl=zh-CN&tl=en&u=http%3A%2F%2Fitem.taobao.com%2Fitem.htm%3Fid%3D14408505465)) \- [ARMFLY Mini-Logic RS232 RS485 RS422 CAN converter](http://item.taobao.com/item.htm?id=16943624739) ([English translation](http://translate.google.com/translate?sl=zh-CN&tl=en&js=n&prev=_t&hl=en&ie=UTF-8&layout=2&eotf=1&u=http%3A%2F%2Fitem.taobao.com%2Fitem.htm%3Fid%3D16943624739&act=url))
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=ARMFLY_Mini-Logic&oldid=14390](https://OpenTraceLab.org/w/index.php?title=ARMFLY_Mini-Logic&oldid=14390)"
: \- *Device* \- *Logic analyzer* \- *Supported*
## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
