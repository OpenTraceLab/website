# Dreamsourcelab Dslogic U2Basic
| | | |:------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------| | Status | planned | | Source code | [dreamsourcelab-dslogic](http://github.com/OpenTraceLab/?p=OpenTraceCapture.git;a=tree;f=src/hardware/dreamsourcelab-dslogic) | | Channels | 1-16 | | Samplerate | Stream mode: 100MHz(3ch), 50MHz(6ch), 25MHz(12ch), 20MHz(16ch) | | Website | [dreamsourcelab.com](https://www.dreamsourcelab.com) | **DreamSourceLab DSLogic U2Basic** The **DreamSourceLab DSLogic U2Basic** is a 16-channel USB-based logic analyzer, with sampling rates up to 400MHz (when using only 4 channels). See *DreamSourceLab DSLogic U2Basic/Info* for more details (such as **lsusb -v** output) about the device.
## Contents
\- *1 Hardware* \- *2 Photos* \- *3 Firmware* \- *3.1 EEPROM layout* \- *4 Resources*
## Hardware \- **FPGA**: Xilinx Spartan-6 XC6SLX9 \- **USB**: Cypress CY7C68013A (FX2) \- **I²C EEPROM**: ST 4128BRP \- **SDRAM**: Winbond W9864G6KH-6 \- **Crystal**: 24MHz ## Photos \-
[*Image: \1*
Package
\-
[*Image: \1*
Device, top
\-
[*Image: \1*
Device, bottom
\-
[*Image: \1*
USB connector
\-
[*Image: \1*
Probe connector
\-
[*Image: \1*
USB cable
\-
[*Image: \1*
Probe cables
\-
[*Image: \1*
Probes
\-
[*Image: \1*
PCB, top
\-
[*Image: \1*
PCB, bottom
\-
[*Image: \1*
Xilinx XC6SLX9
\-
[*Image: \1*
Cypress FX2
\-
[*Image: \1*
Winbond W9864G6KH-6
\-
[*Image: \1*
USB area
\-
[*Image: \1*
Input stage
\-
[*Image: \1*
24MHz crystal
## Firmware See *DreamSourceLab DSLogic#Firmware*. **Note**: The FX2 firmware is loaded at powerup from the I²C EEPROM on the PCB. ### EEPROM layout The device has an I²C EEPROM with the following layout: c2 0e 2a 29 00 00 00 04 XX XX XX XX XX XX .. .. Description: | | | |----------|--------------------------------------------------------------------------------------------------| | Bytes | Description | | 0 | **0xc2**: FX2 "c2 load" mode, i.e. VID/PID/DID are loaded from EEPROM as the firmware. | | 1-2 | **0x2a0e**: USB vendor ID (VID before firmware renumerate). | | 3-4 | **0x0029**: USB product ID (PID before firmware renumerate). | | 5-6 | **0x0000**: USB device ID (DID before firmware renumerate). | | 7 | **0x04**: FX2 configuration byte (see FX2 TRM for details). | | 8 - 6977 | Firmware (6970 bytes, sha1sum: 47975f295711cf0208bbd963bbfeaf5b36e87b8724cad1e67c0de1a86065b389) | | Rest | Unknown, probably all-0xff. | ## Resources \- [Vendor website](http://www.dreamsourcelab.com) \- [Vendor wiki](http://www.dreamsourcelab.com/wiki/index.php) \- [Vendor forum](http://www.dreamsourcelab.com/forum/index.php) \- *Device specs* \- [Kickstarter page](https://www.kickstarter.com/projects/dreamsourcelab/dslogic-multifunction-instruments-for-everyone)
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=DreamSourceLab_DSLogic_U2Basic&oldid=14983](https://OpenTraceLab.org/w/index.php?title=DreamSourceLab_DSLogic_U2Basic&oldid=14983)"
: \- *Device* \- *Logic analyzer* \- *Planned*
## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
