# Noname Lht00Su1

**Noname LHT00SU1** [![\1](../../assets/hardware/general/\2)](./File:Noname_lht00su1_mugshot.png.html) |   
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
**Noname LHT00SU1** The **Noname LHT00SU1** is a USB-based, 8-channel logic analyzer with up to 24MHz sampling rate, with 1 additional analog channel (theoretically 2, but only one of them can be used at a time; 3MHz analog bandwidth). It is a clone of the [CWAV USBee AX-Pro](https://OpenTraceLab.org/w/index.php?title=CWAV_USBee_AX-Pro&action=edit&redlink=1 "CWAV USBee AX-Pro \(page does not exist\)"). In OpenTraceLab, we use the open-source [fx2lafw](Fx2lafw.html "Fx2lafw") firmware for this logic analyzer. **Note**: [fx2lafw](Fx2lafw.html "Fx2lafw") currently doesn't support switching between the two possible analog channels, 1ACH will be used unconditionally. See [Noname LHT00SU1/Info](Noname_LHT00SU1/Info.html "Noname LHT00SU1/Info") for some more details (such as **lsusb -v** output) on the device. 
## Contents 
\- [1 Hardware](Noname_LHT00SU1.html#Hardware) \- [2 Photos](Noname_LHT00SU1.html#Photos) \- [3 Protocol](Noname_LHT00SU1.html#Protocol) \- [4 Resources](Noname_LHT00SU1.html#Resources) 
## Hardware There's a jumper on the PCB which write-protects the I²C EEPROM when set (it ships in that state) by keeping the WP pin at 3.3V. ## Photos **LTH00SU1-V5.0**: \- 
[![\1](../../assets/hardware/general/\2)](./File:Noname_lht00su1_package_contents.jpg.html)
Package contents
\- 
[![\1](../../assets/hardware/general/\2)](./File:Noname_lht00su1_device_top.jpg.html)
Device, top
\- 
[![\1](../../assets/hardware/general/\2)](./File:Noname_lht00su1_device_bottom.jpg.html)
Device, bottom
\- 
[![\1](../../assets/hardware/general/\2)](./File:Noname_lht00su1_pcb_top.jpg.html)
PCB, top
\- 
[![\1](../../assets/hardware/general/\2)](./File:Noname_lht00su1_pcb_bottom.jpg.html)
PCB, bottom
\- 
[![\1](../../assets/hardware/general/\2)](./File:Noname_lht00su1_cypress_fx2.jpg.html)
Cypress FX2
\- 
[![\1](../../assets/hardware/general/\2)](./File:Noname_lht00su1_tlc5510i.jpg.html)
TLC5510I
\- 
[![\1](../../assets/hardware/general/\2)](./File:Noname_lht00su1_so8.jpg.html)
Unknown SO8
\- 
[![\1](../../assets/hardware/general/\2)](./File:Noname_lht00su1_lm358.jpg.html)
LM358
\- 
[![\1](../../assets/hardware/general/\2)](./File:Noname_lht00su1_hef4051bt.jpg.html)
HEF4051BT
\- 
[![\1](../../assets/hardware/general/\2)](./File:Noname_lht00su1_bochen_3296.jpg.html)
Bochen 3296
\- 
[![\1](../../assets/hardware/general/\2)](./File:Noname_lht00su1_ams1117.jpg.html)
AMS1117-3.3
\- 
[![\1](../../assets/hardware/general/\2)](./File:Noname_lht00su1_24c02n.jpg.html)
24C02N
**LINSOU21-V1.3**: \- 
[![\1](../../assets/hardware/general/\2)](./File:LINSOU21-V1_3-PCB-Top.jpg.html)
PCB, top
\- 
[![\1](../../assets/hardware/general/\2)](./File:LINSOU21-V1_3-PCB-Bottom.jpg.html)
PCB, bottom
**T100-B-V1.2**: \- 
Error creating thumbnail: Unable to save thumbnail to destination

## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
