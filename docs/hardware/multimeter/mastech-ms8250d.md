# Mastech Ms8250D
| | | |:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------------------:| | [*Image: \1* | | | Status | supported | | Source code | [serial-dmm](http://github.com/OpenTraceLab/?p=OpenTraceCapture.git;a=tree;f=src/hardware/serial-dmm) | | Counts | 6600 | | IEC 61010-1 | CAT III (1000V) / CAT IV (600V) | | Connectivity | USB/serial | | Measurements | voltage, current, resistance, capacitance, frequency, duty cycle, diode, continuity | | Features | autorange, true-rms, data hold, min/max, relative, bargraph, backlight, ncv | | Website | [mastech-group.com](http://www.mastech-group.com/products.php?cate=123&PNo=142) | **MASTECH MS8250D** The **MASTECH MS8250D** is a 6600 counts, CAT III (1000V) / CAT IV (600V) handheld digital multimeter with USB connectivity. See *MASTECH MS8250D/Info* for more details (such as **lsusb -v** output) about the device.
## Contents
\- *1 Hardware* \- *2 Photos* \- *3 Protocol* \- *4 Resources*
## Hardware \- CP2102 USB to UART bridge controller \- HY11P14 embedded 18-Bit Σ∆ADC 8-Bit RISC-like mixed signal microcontroller ([datasheet](http://www.hycontek.com/wp-content/uploads/HY11P14_EN.pdf)) \- DTA0660L multimeter chip \- ATMLH538 EEPROM ## Photos \-
[*Image: \1*
Device, front
\-
[*Image: \1*
PCB, front
\-
[*Image: \1*
Device, inside
\-
[*Image: \1*
USB / serial interface
## Protocol The chip periodically sends 18-byte packets at 2400 baud, 8n1. There is no checksum or CRC in the packet. The payload is composed of a 1-1 mapping of the LCD segments. ## Resources \- [Manual](http://www.mastech-group.com/download_s.php?id=62) \- [Vendor software](http://www.mastech-group.com/download_s.php?id=210)
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=MASTECH_MS8250D&oldid=13459](https://OpenTraceLab.org/w/index.php?title=MASTECH_MS8250D&oldid=13459)"
: \- *Device* \- *Multimeter* \- *Supported*
## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
