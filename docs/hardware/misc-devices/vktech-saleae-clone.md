# Vktech Saleae Clone

| | | |:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------------:| | [![\1](../../assets/hardware/general/\2)](./File:VKTECH_thumb.jpg.html) | | | Status | supported | | Source code | [fx2lafw](http://github.com/OpenTraceLab/?p=OpenTraceCapture.git;a=tree;f=src/hardware/fx2lafw) | | Channels | 8 | | Samplerate | 24MHz | | Samplerate (state) | — | | Triggers | none (SW-only) | | Min/max voltage | max. 5.25V | | Threshold voltage | Fixed: VIH=1.4V, VIL=0.8V | | Memory | none | | Compression | none | | Price range | \$5 - \$10 | | Website | [[1]](http://xxxx) | **VKTECH** The **VKTECH** is a fairly standard Cypress FX2 based 8 channel 24 MHz logic analyzer, it is most similar to the [ARMFLY_Mini-Logic](ARMFLY_Mini-Logic.html "ARMFLY Mini-Logic") and [MCU123_USBee_AX_Pro_clone](MCU123_USBee_AX_Pro_clone.html "MCU123 USBee AX Pro clone") devices, though has differences from both of them (SMD LEDs, QFN package unlike MCU123, transceiver IC unlike ARMFLY). OpenTraceLab uses the open-source [fx2lafw](Fx2lafw.html "Fx2lafw") firmware for this logic analyzer. The device uses USB\VID_0925&PID;_3881 so is indistinguishable from a [Saleae_Logic](Saleae_Logic.html "Saleae Logic") device Mine was purchased from [AliExpress](https://aliexpress.com/item/24MHz-8-Channel-Logic-Analyzer/32814170174.html) and arrived in 6 days. ## Hardware \- **Main chip**: Cypress CY7C68013A-56LTXC (FX2LP in QFN package) \- **Transceiver** NXP LVC245A \- **3.3V voltage regulator**: 6206A 1711/33 \- **I²C EEPROM**: ATMHK218 24C02N \- **Crystal**: 24MHz ## Photos \- 
[![\1](../../assets/hardware/general/\2)](./File:VKTECH_case.jpg.html)
Device, case
\- 
[![\1](../../assets/hardware/general/\2)](./File:VKTECH_PCB_front.jpg.html)
Device, PCB front
\- 
[![\1](../../assets/hardware/general/\2)](./File:VKTECH_PCB_rear.jpg.html)
Device, PCB rear
\- 
[![\1](../../assets/hardware/general/\2)](./File:VKTECH_connected.jpg.html)
Device, Connected
## Links [neko.ne.jp/~freewing](http://www.neko.ne.jp/~freewing/hardware/usb_logic_analyzer_cy7c68013a_clone)
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=VKTECH_saleae_clone&oldid=14394](https://OpenTraceLab.org/w/index.php?title=VKTECH_saleae_clone&oldid=14394)" 
[Categories](specialcategories-specialcategories.md): \- [Device](./Category:Device.html "Category:Device") \- [Logic analyzer](./Category:Logic_analyzer.html "Category:Logic analyzer") \- [Supported](./Category:Supported.html "Category:Supported")

## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
