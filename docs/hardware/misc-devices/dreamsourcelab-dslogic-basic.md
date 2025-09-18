# Dreamsourcelab Dslogic Basic

| | | |:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------:| | [![\1](../../assets/hardware/general/\2)](./File:DSLogic.png.html) | | | Status | supported | | Source code | [dreamsourcelab-dslogic](http://github.com/OpenTraceLab/?p=OpenTraceCapture.git;a=tree;f=src/hardware/dreamsourcelab-dslogic) | | Channels | 1-16 | | Samplerate | 100MHz(3ch), 100MHz(6ch), 50MHz(9ch), 32MHz(12ch), 16MHz(16ch) | | Samplerate (state) | 30MHz (?) or 50MHz (?) | | Triggers | high, low, rising, falling, edge, multi-stage triggers | | Min/max voltage | -0.6V — 6V | | Threshold voltage | configurable: 0-5V (0.1V increments) | | Memory | None | | Compression | yes | | Website | [dreamsourcelab.com](http://www.dreamsourcelab.com/dslogic.html) | **DreamSourceLab DSLogic Basic** The **DreamSourceLab DSLogic Basic** is a 16-channel USB-based logic analyzer, with sampling rates up to 400MHz (when using only 4 channels). See [DreamSourceLab DSLogic Basic/Info](DreamSourceLab_DSLogic_Basic/Info.html "DreamSourceLab DSLogic Basic/Info") for more details (such as **lsusb -v** output) about the device. 
## Contents 
\- [1 Hardware](DreamSourceLab_DSLogic_Basic.html#Hardware) \- [2 Photos](DreamSourceLab_DSLogic_Basic.html#Photos) \- [3 Firmware](DreamSourceLab_DSLogic_Basic.html#Firmware) \- [3.1 EEPROM layout](DreamSourceLab_DSLogic_Basic.html#EEPROM_layout) \- [4 Resources](DreamSourceLab_DSLogic_Basic.html#Resources) 
## Hardware \- **FPGA**: Xilinx Spartan-6 XC6SLX9 \- **USB**: Cypress CY7C68013A (FX2) \- **I²C EEPROM**: ST 4128BRP \- **Crystal**: 24MHz ## Photos **Device**: **Cables**: \- 
[![\1](../../assets/hardware/general/\2)](./File:Dreamsourcelab_dslogic_basic_cable_1.jpg.html)
\- 
[![\1](../../assets/hardware/general/\2)](./File:Dreamsourcelab_dslogic_basic_cable_2.jpg.html)
\- 
[![\1](../../assets/hardware/general/\2)](./File:Dreamsourcelab_dslogic_basic_cable_3.jpg.html)
\- 
[![\1](../../assets/hardware/general/\2)](./File:Dreamsourcelab_dslogic_basic_cable_4.jpg.html)
\- 
[![\1](../../assets/hardware/general/\2)](./File:Dreamsourcelab_dslogic_basic_cable_5.jpg.html)
\- 
[![\1](../../assets/hardware/general/\2)](./File:Dreamsourcelab_dslogic_basic_cable_6.jpg.html)
\- 
[![\1](../../assets/hardware/general/\2)](./File:Dreamsourcelab_dslogic_basic_cable_7.jpg.html)
\- 
[![\1](../../assets/hardware/general/\2)](./File:Dreamsourcelab_dslogic_basic_cable_8.jpg.html)
\- 
[![\1](../../assets/hardware/general/\2)](./File:Dreamsourcelab_dslogic_basic_probe_circuit.png.html)
Probe cable circuit
## Firmware See [DreamSourceLab DSLogic#Firmware](DreamSourceLab_DSLogic.html#Firmware "DreamSourceLab DSLogic"). **Note**: The FX2 firmware is loaded at powerup from the I²C EEPROM on the PCB. ### EEPROM layout The device has an I²C EEPROM with the following layout: c2 0e 2a 21 00 00 00 04 XX XX XX XX XX XX .. .. Description: | | | |----------|--------------------------------------------------------------------------------------------------| | Bytes | Description | | 0 | **0xc2**: FX2 "c2 load" mode, i.e. VID/PID/DID are loaded from EEPROM as the firmware. | | 1-2 | **0x2a0e**: USB vendor ID (VID before firmware renumerate). | | 3-4 | **0x0021**: USB product ID (PID before firmware renumerate). | | 5-6 | **0x0000**: USB device ID (DID before firmware renumerate). | | 7 | **0x04**: FX2 configuration byte (see FX2 TRM for details). | | 8 - 6778 | Firmware (6771 bytes, sha1sum: 79784d038800e4b4757eba15de33813ac76819945f1b39239df6cf0a096dce55) | | Rest | Unknown, probably all-0xff. | ## Resources \- [Vendor website](http://www.dreamsourcelab.com) \- [Vendor wiki](http://www.dreamsourcelab.com/wiki/index.php) \- [Vendor forum](http://www.dreamsourcelab.com/forum/index.php) \- [Device specs](http://www.dreamsourcelab.com/techspec.html) \- [Kickstarter page](https://www.kickstarter.com/projects/dreamsourcelab/dslogic-multifunction-instruments-for-everyone)
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=DreamSourceLab_DSLogic_Basic&oldid=14965](https://OpenTraceLab.org/w/index.php?title=DreamSourceLab_DSLogic_Basic&oldid=14965)" 
[Categories](specialcategories-specialcategories.md): \- [Device](./Category:Device.html "Category:Device") \- [Logic analyzer](./Category:Logic_analyzer.html "Category:Logic analyzer") \- [Supported](./Category:Supported.html "Category:Supported")

## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
