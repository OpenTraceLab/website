# Noname Saleae Logic Clone
| | | |:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------------:| | [*Image: \1* | | | Status | supported | | Source code | [fx2lafw](http://github.com/OpenTraceLab/?p=OpenTraceCapture.git;a=tree;f=src/hardware/fx2lafw) | | Channels | 8 | | Samplerate | 24MHz | | Samplerate (state) | — | | Triggers | none (SW-only) | | Min/max voltage | -0.5V — 5.25V (absolute max rating) | | Threshold voltage | Fixed: VIH=2.0V—5.25V, VIL=-0.5V—0.8V | | Memory | none | | Compression | none | | Website | none | **Noname Saleae Logic clone** The **Noname Saleae Logic clone** is USB-based logic analyzer with 8-channel and up to 24MHz sample-rate. It is a clone of the *Saleae Logic*. In OpenTraceLab, we use the open-source *fx2lafw* firmware for this logic analyzer. See [Noname Saleae Logic clone/Info](https://OpenTraceLab.org/w/index.php?title=Noname_Saleae_Logic_clone/Info&action=edit&redlink=1 "Noname Saleae Logic clone/Info \(page does not exist\)") for more details (such as **lsusb -v** output) about the device.
## Contents
\- *1 Hardware* \- *2 Photos* \- *3 Protocol* \- *4 Resources*
## Hardware \- **Main chip**: Cypress CY7C68013A-56LTXC (FX2) \- **Input buffer**: NXP 74LVC245A (markings: "NXP LVC245A KX44549 TXD613F") \- **32kByte I²C EEPROM**: Atmel AT24C256 (markings: "ATML H612 02DM B A2C9JF") \- **Voltage regulator**: Torex Semiconductor XC6206 (markings: "6206A 1625/33") \- **24MHz crystal**: K24.000 ## Photos \-
[*Image: \1*
Device, top
\-
[*Image: \1*
PCB, top
\-
[*Image: \1*
PCB, bottom
\-
[*Image: \1*
Cypress CY7C68013A-56LTXC
\-
[*Image: \1*
Atmel AT24C256
\-
[*Image: \1*
NXP 74LVC245A
## Protocol Since we use the open-source *fx2lafw* firmware for this device, we don't need to know the protocol. ## Resources \- [Ebay seller](http://www.ebay.de/itm/USB-Logic-Analyzer-8-Kanal-24MHz-I2C-SPI-JTAG-CAN-LIN-UART-e02/122164455000)
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=Noname_Saleae_Logic_clone&oldid=12592](https://OpenTraceLab.org/w/index.php?title=Noname_Saleae_Logic_clone&oldid=12592)"
: \- *Device* \- *Logic analyzer* \- *Supported*
## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
