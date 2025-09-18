# Acute Pkla 1216

| | | |:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------:| | [![\1](../../assets/hardware/general/\2)](./File:Acute_pkla1216.png.html) | | | Status | planned | | Channels | 16 | | Samplerate | 200MHz | | Samplerate (state) | 75MHz | | Triggers | pattern, edge | | Min/max voltage | -30V — 30V | | Threshold voltage | -7.2V — 6.8V | | Memory | 256Kbit/channel | | Compression | ? | | Website | [acute.com.tw](http://www.acute.com.tw/product/la.php) | **Acute PKLA-1216** The **Acute PKLA-1216** is a 200MHz, 16-channel, USB-based logic analyzer. See [Acute PKLA-1216/Info](Acute_PKLA-1216/Info.html "Acute PKLA-1216/Info") for more details (such as **lsusb -vvv** output) about the device. 
## Contents 
\- [1 Hardware](Acute_PKLA-1216.html#Hardware) \- [2 Photos](Acute_PKLA-1216.html#Photos) \- [3 Protocol](Acute_PKLA-1216.html#Protocol) \- [4 Resources](Acute_PKLA-1216.html#Resources) 
## Hardware \- **Main chip (ASIC)**: Acute AQC20256Q208-7 BAC490X370A V00028 0507 \- **SRAM (4MBit)**: [Cypress CY7C1347G-133AXC](http://www.cypress.com/?mpn=CY7C1347G-133AXC) ([datasheet](http://www.cypress.com/?docID=23463)) \- **USB2.0 to IEEE-1284 / DMA Bridge**: [Genesys GL660USB](http://www.genesyslogic.com/_en/News%20message.php?id=108) \- **One-PLL General-Purpose Flash-Programmable and I2C Programmable Clock Generator**: [Cypress CY22150FC](http://www.cypress.com/?mpn=CY22150FZXC) ([datasheet](http://www.cypress.com/?docID=31685)) \- **Low-Noise, 5.5V-Input, PWM Step-Down Regulator**: [Maxim MAX1692EUB](http://www.maxim-ic.com/datasheet/index.mvp/id/1932/t/al) ([datasheet](http://datasheets.maxim-ic.com/en/ds/MAX1692.pdf)) \- **Dual-Output (Positive and Negative), DC-DC Converter for CCD and LCD**: [Maxim MAX685](http://www.maxim-ic.com/datasheet/index.mvp/id/1859) ([datasheet](http://datasheets.maxim-ic.com/en/ds/MAX685.pdf)) \- **3.3V, Quad 2:1 Mux/DeMux NanoSwitch**: [Pericom PI3B3257Q](http://www.pericom.com/products/switch/digital/PI3B3257/) ([datasheet](http://www.pericom.com/pdf/datasheets/PI3B3257.pdf)) \- **16-Bit Bidirectional Transceiver**: [Pericom PI74LPT16245](http://www.pericom.com/products/logic/PI74LPT16245/) ([datasheet](http://www.pericom.com/pdf/datasheets/PI74LPT16245.pdf)) \- **1kBit Microwire EEPROM**: [M93C46-W](http://www.st.com/internet/mcu/product/63991.jsp) ([datasheet](http://www.st.com/internet/com/TECHNICAL_RESOURCES/TECHNICAL_LITERATURE/DATASHEET/CD00001142.pdf)) \- **Quad Low-Power JFET-Input General-Purpose Operational Amplifier**: [Texas Instruments TL064](http://www.ti.com/product/tl064) ([datasheet](http://www.ti.com/lit/gpn/tl064)) \- **Dual 8-Bit Multiplying Digital-to-Analog Converters**: [TLC7528](http://www.ti.com/product/tlc7528) ([datasheet](http://www.ti.com/lit/gpn/tlc7528)) \- **12MHz crystal**: YI12.000H5 ## Photos \- 
[![\1](../../assets/hardware/general/\2)](./File:Acute_pkla1216_front.jpg.html)
\- 
[![\1](../../assets/hardware/general/\2)](./File:Acute_pkla1216_back.jpg.html)
\- 
[![\1](../../assets/hardware/general/\2)](./File:Acute_pkla1216_connectors.jpg.html)
\- 
[![\1](../../assets/hardware/general/\2)](./File:Acute_pkla1216_usb.jpg.html)
\- 
[![\1](../../assets/hardware/general/\2)](./File:Acute_pkla1216_cables_probes.jpg.html)
\- 
[![\1](../../assets/hardware/general/\2)](./File:Acute_pkla1216_pcb_front.jpg.html)
\- 
[![\1](../../assets/hardware/general/\2)](./File:Acute_pkla1216_pcb_back.jpg.html)
\- 
[![\1](../../assets/hardware/general/\2)](./File:Acute_pkla1216_acute_aqc20256q208_7.jpg.html)
\- 
[![\1](../../assets/hardware/general/\2)](./File:Acute_pkla1216_cypress_cy7c1347g_133axc.jpg.html)
\- 
[![\1](../../assets/hardware/general/\2)](./File:Acute_pkla1216_genesys_gl660usb.jpg.html)
\- 
[![\1](../../assets/hardware/general/\2)](./File:Acute_pkla1216_st_93c46w6.jpg.html)
\- 
[![\1](../../assets/hardware/general/\2)](./File:Acute_pkla1216_cypress_cy22150fc.jpg.html)
\- 
[![\1](../../assets/hardware/general/\2)](./File:Acute_pkla1216_maxim_max685.jpg.html)
\- 
[![\1](../../assets/hardware/general/\2)](./File:Acute_pkla1216_maxim_max1692eub.jpg.html)
\- 
[![\1](../../assets/hardware/general/\2)](./File:Acute_pkla1216_ti_tl064c.jpg.html)
\- 
[![\1](../../assets/hardware/general/\2)](./File:Acute_pkla1216_ti_tlc7528c.jpg.html)
\- 
[![\1](../../assets/hardware/general/\2)](./File:Acute_pkla1216_pericom_pi3b3257q.jpg.html)
\- 
[![\1](../../assets/hardware/general/\2)](./File:Acute_pkla1216_pericom_pi74lpt16245vc.jpg.html)
\- 
[![\1](../../assets/hardware/general/\2)](./File:Acute_pkla1216_jumper_jp1.jpg.html)
## Protocol TODO. ## Resources \- [Vendor manual](http://www.acute.com.tw/Software/manual/enla.pdf) \- [Spec, packing list](http://www.acute.com.tw/Software/spec/pkla.zip)
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=Acute_PKLA-1216&oldid=6851](https://OpenTraceLab.org/w/index.php?title=Acute_PKLA-1216&oldid=6851)" 
[Categories](specialcategories-specialcategories.md): \- [Device](./Category:Device.html "Category:Device") \- [Logic analyzer](./Category:Logic_analyzer.html "Category:Logic analyzer") \- [Planned](./Category:Planned.html "Category:Planned")

## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
