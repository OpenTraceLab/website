# Dreamsourcelab Dslogic U2Basic

| | | |:------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------| | Status | planned | | Source code | [dreamsourcelab-dslogic](http://github.com/OpenTraceLab/?p=OpenTraceCapture.git;a=tree;f=src/hardware/dreamsourcelab-dslogic) | | Channels | 1-16 | | Samplerate | Stream mode: 100MHz(3ch), 50MHz(6ch), 25MHz(12ch), 20MHz(16ch) | | Website | [dreamsourcelab.com](https://www.dreamsourcelab.com) | **DreamSourceLab DSLogic U2Basic** The **DreamSourceLab DSLogic U2Basic** is a 16-channel USB-based logic analyzer, with sampling rates up to 400MHz (when using only 4 channels). See [DreamSourceLab DSLogic U2Basic/Info](DreamSourceLab_DSLogic_U2Basic/Info.html "DreamSourceLab DSLogic U2Basic/Info") for more details (such as **lsusb -v** output) about the device. 
## Contents 
\- [1 Hardware](DreamSourceLab_DSLogic_U2Basic.html#Hardware) \- [2 Photos](DreamSourceLab_DSLogic_U2Basic.html#Photos) \- [3 Firmware](DreamSourceLab_DSLogic_U2Basic.html#Firmware) \- [3.1 EEPROM layout](DreamSourceLab_DSLogic_U2Basic.html#EEPROM_layout) \- [4 Resources](DreamSourceLab_DSLogic_U2Basic.html#Resources) 
## Hardware \- **FPGA**: Xilinx Spartan-6 XC6SLX9 \- **USB**: Cypress CY7C68013A (FX2) \- **I²C EEPROM**: ST 4128BRP \- **SDRAM**: Winbond W9864G6KH-6 \- **Crystal**: 24MHz ## Photos \- 
[![\1](../../assets/hardware/general/\2)](./File:Dreamsourcelab_dslogic_u2basic_package.jpg.html)
Package
\- 
[![\1](../../assets/hardware/general/\2)](./File:Dreamsourcelab_dslogic_u2basic_device_top.jpg.html)
Device, top
\- 
[![\1](../../assets/hardware/general/\2)](./File:Dreamsourcelab_dslogic_u2basic_device_bottom.jpg.html)
Device, bottom
\- 
[![\1](../../assets/hardware/general/\2)](./File:Dreamsourcelab_dslogic_u2basic_usb_connector.jpg.html)
USB connector
\- 
[![\1](../../assets/hardware/general/\2)](./File:Dreamsourcelab_dslogic_u2basic_probe_connector.jpg.html)
Probe connector
\- 
[![\1](../../assets/hardware/general/\2)](./File:Dreamsourcelab_dslogic_u2basic_usb_cable.jpg.html)
USB cable
\- 
[![\1](../../assets/hardware/general/\2)](./File:Dreamsourcelab_dslogic_u2basic_probe_cables.jpg.html)
Probe cables
\- 
[![\1](../../assets/hardware/general/\2)](./File:Dreamsourcelab_dslogic_u2basic_probes.jpg.html)
Probes
\- 
[![\1](../../assets/hardware/general/\2)](./File:Dreamsourcelab_dslogic_u2basic_pcb_top.jpg.html)
PCB, top
\- 
[![\1](../../assets/hardware/general/\2)](./File:Dreamsourcelab_dslogic_u2basic_pcb_bottom.jpg.html)
PCB, bottom
\- 
[![\1](../../assets/hardware/general/\2)](./File:Dreamsourcelab_dslogic_u2basic_xilinx_xc6slx9.jpg.html)
Xilinx XC6SLX9
\- 
[![\1](../../assets/hardware/general/\2)](./File:Dreamsourcelab_dslogic_u2basic_cypress_fx2.jpg.html)
Cypress FX2
\- 
[![\1](../../assets/hardware/general/\2)](./File:Dreamsourcelab_dslogic_u2basic_winbond_w9864g6kh-6.jpg.html)
Winbond W9864G6KH-6
\- 
[![\1](../../assets/hardware/general/\2)](./File:Dreamsourcelab_dslogic_u2basic_usb.jpg.html)
USB area
\- 
[![\1](../../assets/hardware/general/\2)](./File:Dreamsourcelab_dslogic_u2basic_input_stage.jpg.html)
Input stage
\- 
[![\1](../../assets/hardware/general/\2)](./File:Dreamsourcelab_dslogic_u2basic_24mhz_crystal.jpg.html)
24MHz crystal
## Firmware See [DreamSourceLab DSLogic#Firmware](DreamSourceLab_DSLogic.html#Firmware "DreamSourceLab DSLogic"). **Note**: The FX2 firmware is loaded at powerup from the I²C EEPROM on the PCB. ### EEPROM layout The device has an I²C EEPROM with the following layout: c2 0e 2a 29 00 00 00 04 XX XX XX XX XX XX .. .. Description: | | | |----------|--------------------------------------------------------------------------------------------------| | Bytes | Description | | 0 | **0xc2**: FX2 "c2 load" mode, i.e. VID/PID/DID are loaded from EEPROM as the firmware. | | 1-2 | **0x2a0e**: USB vendor ID (VID before firmware renumerate). | | 3-4 | **0x0029**: USB product ID (PID before firmware renumerate). | | 5-6 | **0x0000**: USB device ID (DID before firmware renumerate). | | 7 | **0x04**: FX2 configuration byte (see FX2 TRM for details). | | 8 - 6977 | Firmware (6970 bytes, sha1sum: 47975f295711cf0208bbd963bbfeaf5b36e87b8724cad1e67c0de1a86065b389) | | Rest | Unknown, probably all-0xff. | ## Resources \- [Vendor website](http://www.dreamsourcelab.com) \- [Vendor wiki](http://www.dreamsourcelab.com/wiki/index.php) \- [Vendor forum](http://www.dreamsourcelab.com/forum/index.php) \- [Device specs](http://www.dreamsourcelab.com/techspec.html) \- [Kickstarter page](https://www.kickstarter.com/projects/dreamsourcelab/dslogic-multifunction-instruments-for-everyone)
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=DreamSourceLab_DSLogic_U2Basic&oldid=14983](https://OpenTraceLab.org/w/index.php?title=DreamSourceLab_DSLogic_U2Basic&oldid=14983)" 
[Categories](specialcategories-specialcategories.md): \- [Device](./Category:Device.html "Category:Device") \- [Logic analyzer](./Category:Logic_analyzer.html "Category:Logic analyzer") \- [Planned](./Category:Planned.html "Category:Planned")

## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
