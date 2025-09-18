# Mcu123 Saleae Logic Clone

| | | |:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:| | [![\1](../../assets/hardware/general/\2)](./File:Mcu123_saleae_logic_clone.png.html) | | | Status | supported | | Source code | [fx2lafw](http://github.com/OpenTraceLab/?p=OpenTraceCapture.git;a=tree;f=src/hardware/fx2lafw) | | Channels | 8 | | Samplerate | 24MHz | | Samplerate (state) | — | | Triggers | none (SW-only) | | Min/max voltage | -0.5V — 5.25V | | Threshold voltage | Fixed: VIH=2.0V—5.25V, VIL=-0.5V—0.8V | | Memory | none | | Compression | none | | Price range | \$5 - \$10 | | Website | [mcu123.com](http://translate.google.de/translate?sl=zh-CN&tl=en&js=n&prev=_t&hl=de&ie=UTF-8&eotf=1&u=http%3A%2F%2Fwww.mcu123.com%2Fwww%2Fprodshow.asp%3FProdId%3DNO054&act=url) | **MCU123 Saleae Logic clone** The **MCU123 Saleae Logic clone** is a USB-based, 8-channel logic analyzer with up to 24MHz sampling rate. It is a clone of the [Saleae Logic](Saleae_Logic.html "Saleae Logic"). It's also *very* similar to the [MCU123 USBee AX Pro clone](MCU123_USBee_AX_Pro_clone.html "MCU123 USBee AX Pro clone") minus the different USB vendor/device IDs. In OpenTraceLab, we use the open-source [fx2lafw](Fx2lafw.html "Fx2lafw") firmware for this logic analyzer. See [MCU123 Saleae Logic clone/Info](MCU123_Saleae_Logic_clone/Info.html "MCU123 Saleae Logic clone/Info") for more detailed information on the device. 
## Contents 
\- [1 Hardware](MCU123_Saleae_Logic_clone.html#Hardware) \- [2 Photos](MCU123_Saleae_Logic_clone.html#Photos) \- [3 Protocol](MCU123_Saleae_Logic_clone.html#Protocol) \- [4 Resources](MCU123_Saleae_Logic_clone.html#Resources) 
## Hardware \- **Main chip**: Cypress CY7C68013-56PVC (FX2) \- **Input buffer**: NXP 74HC245 (markings: "NXP HC245 2A7K508 UnD2 18E") \- **256-byte I2C EEPROM**: Atmel AT24C02 (markings: "ATMEL211 24C02N SU27 D") \- **3.3V low-dropout voltage regulator**: Advanced Monolithic Systems AMS1117-3.3 (markings: "AMS1117 3.3 HT240E") \- **24MHz crystal**: 24.000 ## Photos \- 
[![\1](../../assets/hardware/general/\2)](./File:Mcu123_saleae_logic_clone_package_contents.jpg.html)
Package contents
\- 
[![\1](../../assets/hardware/general/\2)](./File:Mcu123_saleae_logic_clone_top.jpg.html)
Device, front
\- 
[![\1](../../assets/hardware/general/\2)](./File:Mcu123_saleae_logic_clone_bottom.jpg.html)
Device, back
\- 
[![\1](../../assets/hardware/general/\2)](./File:Mcu123_saleae_logic_clone_pcb_top.jpg.html)
PCB, top
\- 
[![\1](../../assets/hardware/general/\2)](./File:Mcu123_saleae_logic_clone_pcb_bottom.jpg.html)
PCB, bottom
\- 
[![\1](../../assets/hardware/general/\2)](./File:Mcu123_saleae_logic_clone_eeprom.jpg.html)
EEPROM
## Protocol Since we use the open-source [fx2lafw](Fx2lafw.html "Fx2lafw") firmware for this device, we don't need to know the protocol. ## Resources \- [Random aliexpress.com vendor](http://www.aliexpress.com/item/USB-Saleae-24M-8CH-Saleae-24MHz-8Channel-Logic-Analyzer-saleae-24M-8CH-Latest-support-1-1/737326718.html) (there are many) \- [Random Taobao vendor](http://translate.google.com/translate?act=url&hl=de&ie=UTF8&prev=_t&rurl=translate.google.com&sl=zh-CN&tl=en&u=http://item.taobao.com/item.htm%3Fid%3D15872520745) (there are many) \- [hotmcu.com shop](http://www.hotmcu.com/saleae-24mhz-8channel-logic-analyzer-p-28.html)
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=MCU123_Saleae_Logic_clone&oldid=14389](https://OpenTraceLab.org/w/index.php?title=MCU123_Saleae_Logic_clone&oldid=14389)" 
[Categories](specialcategories-specialcategories.md): \- [Device](./Category:Device.html "Category:Device") \- [Logic analyzer](./Category:Logic_analyzer.html "Category:Logic analyzer") \- [Supported](./Category:Supported.html "Category:Supported")

## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
