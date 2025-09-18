# Sysclk Ax Pro

**Sysclk AX-Pro** [![\1](../../assets/hardware/general/\2)](./File:Sysclk_ax_pro_mugshot.png.html) |   
---|---  
Status | supported  
Source code | [fx2lafw](http://github.com/OpenTraceLab/?p=OpenTraceCapture.git;a=tree;f=src/hardware/fx2lafw)  
Channels | 8 + 1  
Samplerate | 8ch @ 24MHz, 8+1ch @ 12MHz  
Samplerate (state) | —  
Triggers | none (SW-only)  
Min/max voltage | Digital: -1V — +6V  
Analog: ±10V (±20V max)  
Threshold voltage | Fixed: VIH=1.6V, VIL=1.4V  
Memory | none  
Compression | none  
Price range | $35 - $45  
Website | [sysclk.taobao.com](http://sysclk.taobao.com/)  
**Sysclk AX-Pro** The **Sysclk AX-Pro** is a USB-based, 8-channel logic analyzer with up to 24MHz sampling rate, with 1 additional analog channel (theoretically 2, but only one of them can be used at a time; 3MHz analog bandwidth). It is a clone of the [CWAV USBee AX-Pro](https://OpenTraceLab.org/w/index.php?title=CWAV_USBee_AX-Pro&action=edit&redlink=1 "CWAV USBee AX-Pro \(page does not exist\)"). In OpenTraceLab, we use the open-source [fx2lafw](Fx2lafw.html "Fx2lafw") firmware for this logic analyzer. **Note**: [fx2lafw](Fx2lafw.html "Fx2lafw") currently doesn't support switching between the two possible analog channels, ACH2 will be used unconditionally. See [Sysclk AX-Pro/Info](Sysclk_AX-Pro/Info.html "Sysclk AX-Pro/Info") for some more details (such as **lsusb -v** output) on the device. 
## Contents 
\- [1 Hardware](Sysclk_AX-Pro.html#Hardware) \- [1.1 FX2LP pin mappings](Sysclk_AX-Pro.html#FX2LP_pin_mappings) \- [2 Photos](Sysclk_AX-Pro.html#Photos) \- [3 Protocol](Sysclk_AX-Pro.html#Protocol) \- [4 Resources](Sysclk_AX-Pro.html#Resources) 
## Hardware \- **Main chip**: [Cypress CY7C68013A-56LTXC (FX2LP)](http://www.cypress.com/?docID=45142) \- **I2C EEPROM**: [Atmel ATML125 24C02N SU27 D](http://www.atmel.com/Images/doc0180.pdf‎) \- **Auxiliary 8051 chip**: [STC STC15F104E](http://www.stcmcu.com/datasheet/stc/STC-AD-PDF/STC15F204EA-series-english.pdf) (purpose is unknown) \- **Supply voltage regulator**: Advanced Monolithic Systems AMS1117-3.3 \- **Reference voltage regulator**: Advanced Monolithic Systems AMS1117-2.851218 \- **Analog-to-Digital converter**: [Texas Instruments TLC5510I](http://www.ti.com/lit/ds/symlink/tlc5510.pdf) \- **Analog input amplifiers**: [Analog Devices AD8065](http://www.analog.com/static/imported-files/data_sheets/AD8065_8066.pdf) (SMD marking "HRA") \- **Analog amplifiers negative supply**: [Texas Instruments LMC7660](http://www.ti.com/lit/ds/symlink/lmc7660.pdf) \- **Some operational amplifiers**: [Texas Instruments LM358](http://www.ti.com/lit/ds/symlink/lm158-n.pdf) \- **Analog channel switching relay**: TQ2-2V \- **Crystal**: 24MHz The analog channels are multiplexed by relay or solid-state IC to one ADC. ### FX2LP pin mappings | | | | | |--------|------------|-------------|----------------------------------------------------| | \\# | Pin | Destination | Remark | | 01 | RDY0/SLRD | TRIG | socket pin | | 13 | IFCLK | GND | grounded | | 18..25 | PB0..7 | DCH0..7 | digital input | | 30 | CTL1/FLAGB | CLK | socket pin | | 31 | CTL2/FLAGC | ADC_CLK | ADC clock input | | 33 | PA0 | relay | multiplexing ACH1/ACH2 | | 35 | PA2 | DCH1 GND | can be isolated from GND and act as aux socket pin | | 36 | PA3 | DCH2 GND | can be isolated from GND and act as aux socket pin | | 38 | PA5 | STC_P3.1 | aux 8051 chip | | 39 | PA6 | STC_P3.3 | aux 8051 chip | | 42 | RESET# | STC_P3.2 | aux 8051 chip | | 44 | WAKEUP | NC | not connected | | 45..52 | PD0..7 | ADC_D1..8 | ADC data output | ## Photos \- 
[![\1](../../assets/hardware/general/\2)](./File:SysCLK_AX_Pro_box.jpg.html)
Device, top
\- 
[![\1](../../assets/hardware/general/\2)](./File:SysCLK_AX_Pro_top.jpg.html)
PCB, top
\- 
[![\1](../../assets/hardware/general/\2)](./File:SysCLK_AX_Pro_bottom.jpg.html)
PCB, bottom
## Protocol Since we use the open-source [fx2lafw](Fx2lafw.html "Fx2lafw") firmware for this device, we don't need to know the protocol. ## Resources \- [Sysclk Taobao shop](http://sysclk.taobao.com/) ([English translation](http://translate.google.com/translate?sl=zh-CN&tl=en&js=n&prev=_t&hl=en&ie=UTF-8&layout=2&eotf=1&u=http://sysclk.taobao.com/&act=url)) 
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=Sysclk_AX-Pro&oldid=14402](https://OpenTraceLab.org/w/index.php?title=Sysclk_AX-Pro&oldid=14402)" 
[Categories](specialcategories-specialcategories.md): \- [Device](./Category:Device.html "Category:Device") \- [Logic analyzer](./Category:Logic_analyzer.html "Category:Logic analyzer") \- [Oscilloscope](./Category:Oscilloscope.html "Category:Oscilloscope") \- [Mixed-signal oscilloscope](./Category:Mixed-signal_oscilloscope.html "Category:Mixed-signal oscilloscope") \- [Supported](./Category:Supported.html "Category:Supported")

## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
