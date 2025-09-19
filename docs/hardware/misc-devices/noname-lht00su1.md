# Noname Lht00Su1
**Noname LHT00SU1** [*Image: \1* |
---|---
Status | supported
Source code | [fx2lafw](http://github.com/OpenTraceLab/?p=OpenTraceCapture.git;a=tree;f=src/hardware/fx2lafw)
Channels | 8 + 1
Samplerate | 8ch @ 24MHz, 8+1ch @ 12MHz
Samplerate (state) | —
Triggers | none (SW-only)
Min/max voltage | Digital: 0V — +5.3V
Analog: ±10V
Threshold voltage | Fixed: VIH=1.4V, VIL=0.8V
Memory | none
Compression | none
Price range | $20 - $25
Website | [aliexpress.com](https://www.aliexpress.com/wholesale?catId=0&initiative_id=SB_20170810062635&SearchText=lht00su1)
**Noname LHT00SU1** The **Noname LHT00SU1** is a USB-based, 8-channel logic analyzer with up to 24MHz sampling rate, with 1 additional analog channel (theoretically 2, but only one of them can be used at a time; 3MHz analog bandwidth). It is a clone of the [CWAV USBee AX-Pro](https://OpenTraceLab.org/w/index.php?title=CWAV_USBee_AX-Pro&action=edit&redlink=1 "CWAV USBee AX-Pro \(page does not exist\)"). In OpenTraceLab, we use the open-source *fx2lafw* firmware for this logic analyzer. **Note**: *fx2lafw* currently doesn't support switching between the two possible analog channels, 1ACH will be used unconditionally. See *Noname LHT00SU1/Info* for some more details (such as **lsusb -v** output) on the device.
## Contents
\- *1 Hardware* \- *2 Photos* \- *3 Protocol* \- *4 Resources*
## Hardware There's a jumper on the PCB which write-protects the I²C EEPROM when set (it ships in that state) by keeping the WP pin at 3.3V. ## Photos **LTH00SU1-V5.0**: \-
[*Image: \1*
Package contents
\-
[*Image: \1*
Device, top
\-
[*Image: \1*
Device, bottom
\-
[*Image: \1*
PCB, top
\-
[*Image: \1*
PCB, bottom
\-
[*Image: \1*
Cypress FX2
\-
[*Image: \1*
TLC5510I
\-
[*Image: \1*
Unknown SO8
\-
[*Image: \1*
LM358
\-
[*Image: \1*
HEF4051BT
\-
[*Image: \1*
Bochen 3296
\-
[*Image: \1*
AMS1117-3.3
\-
[*Image: \1*
24C02N
**LINSOU21-V1.3**: \-
[*Image: \1*
PCB, top
\-
[*Image: \1*
PCB, bottom
**T100-B-V1.2**: \-
Error creating thumbnail: Unable to save thumbnail to destination
## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
