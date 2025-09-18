# Manson Hcs 3202

| | | |:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------------------------------:| | [![\1](../../assets/hardware/general/\2)](./File:Manson_hcs3202.png.html) | | | Status | supported | | Source code | [manson-hcs-3xxx](http://github.com/OpenTraceLab/?p=OpenTraceCapture.git;a=tree;f=src/hardware/manson-hcs-3xxx) | | Channels | 1 | | Voltage/current (CH1) | 1-36V / 0-10A | | Connectivity | USB/serial | | Features | programmable presets, cycling functionality | | Website | [manson.com.hk](http://www.manson.com.hk/products/detail/153) | **Manson HCS-3202** The **Manson HCS-3202** is a 1-channel programmable power supply (1-36V/0-10A) with USB connectivity. See [Manson HCS-3202/Info](Manson_HCS-3202/Info.html "Manson HCS-3202/Info") for more details (such as **lsusb -v** output) about the device. See [Manson HCS-3xxx series](Manson_HCS-3xxx_series.html "Manson HCS-3xxx series") for information common to all devices in this series. 
## Contents 
\- [1 Hardware](Manson_HCS-3202.html#Hardware) \- [2 Photos](Manson_HCS-3202.html#Photos) \- [3 Protocol](Manson_HCS-3202.html#Protocol) \- [4 Resources](Manson_HCS-3202.html#Resources) 
## Hardware \- **8-bit microcontroller**: [Atmel ATmega64A](http://www.atmel.com/devices/atmega64a.aspx) ([datasheet](http://www.atmel.com/Images/Atmel-8160-8-bit-AVR-Microcontroller-ATmega64A-datasheet.pdf)) \- **USB to UART bridge**: [SiLabs CP2102](http://www.silabs.com/products/interface/usbtouart/pages/usb-to-uart-bridge.aspx) ([datasheet](http://www.silabs.com/Support%20Documents/TechnicalDocs/CP2102-9.pdf)) \- **8-bit shift register with 3-state output registers** : 2x [TI HC595](http://www.ti.com/product/SN74HC595TI) ([datasheet](http://www.ti.com/lit/gpn/sn74hc595)) \- **Dual operational amplifier**: 2x [TI LM358A](http://www.ti.com/product/lm358a) ([datasheet](http://www.ti.com/lit/gpn/lm358a)) \- **Low-power dual op-amp with low input bias current**: [ST LM358N](http://www.st.com/web/en/catalog/sense_power/FM123/SC61/SS1378/PF63721) ([datasheet](http://www.st.com/st-web-ui/static/active/en/resource/technical/document/datasheet/CD00000464.pdf)) \- **Energy-efficient off-line switcher with enhanced flexibility and extended power range**: [Power Integrations TinySwitch-III TNY275PN](https://www.powerint.com/en/products/tinyswitch-family/tinyswitch-iii) ([datasheet](https://www.powerint.com/sites/default/files/product-docs/tny274-280.pdf)) \- **Operational amplifier**: [National LM741CN](http://www.ti.com/product/LM741/description) ([datasheet](http://www.ti.com/lit/gpn/lm741)) \- **PWM control circuit**: [TI TL494CN](http://www.ti.com/product/TL494) ([datasheet](http://www.ti.com/lit/gpn/tl494)) \- **General-purpose photocoupler**: [Sharp PC817](http://www.sharpsma.com/optoelectronics/isolation-devices/dc-input-photocouplers/PC817X2J000F) ([datasheet](http://www.sharpsma.com/webfm_send/1092)) (marking: "C \> B4 PC817 Sharp") \- "C": model = PC817XI3J00F/PC817XP3J00F, "\>": China factory, "B4": date code == April 1991 \- **Triple 2-channel analog multiplexer/demultiplexer**: [ON Semiconductor MC14053BG](http://www.onsemi.com/PowerSolutions/product.do?id=MC14053B) ([datasheet](http://www.onsemi.com/pub/Collateral/MC14051B-D.PDF)) ## Photos \- 
[![\1](../../assets/hardware/general/\2)](./File:Manson_hcs3202_front.jpg.html)
Device, front
\- 
[![\1](../../assets/hardware/general/\2)](./File:Manson_hcs3202_back.jpg.html)
Device, back
\- 
[![\1](../../assets/hardware/general/\2)](./File:Manson_hcs3202_bottom.jpg.html)
Device, bottom
\- 
[![\1](../../assets/hardware/general/\2)](./File:Manson_hcs3202_open.jpg.html)
Device, open
\- 
[![\1](../../assets/hardware/general/\2)](./File:Manson_hcs3202_pcb_front.jpg.html)
PCB, front
\- 
[![\1](../../assets/hardware/general/\2)](./File:Manson_hcs3202_pcb_top.jpg.html)
PCB, top
\- 
[![\1](../../assets/hardware/general/\2)](./File:Manson_hcs3202_atmega64a.jpg.html)
Atmel ATmega64A
\- 
[![\1](../../assets/hardware/general/\2)](./File:Manson_hcs3202_lm358a_pssb10.jpg.html)
LM358A, MC14053BG
\- 
[![\1](../../assets/hardware/general/\2)](./File:Manson_hcs3202_lm358a.jpg.html)
LM358A
\- 
[![\1](../../assets/hardware/general/\2)](./File:Manson_hcs3202_hc595.jpg.html)
HC595
\- 
[![\1](../../assets/hardware/general/\2)](./File:Manson_hcs3202_pc817_tny275pn.jpg.html)
PC817, TNY275PN
\- 
[![\1](../../assets/hardware/general/\2)](./File:Manson_hcs3202_silkscreen.jpg.html)
Silkscreen
\- 
[![\1](../../assets/hardware/general/\2)](./File:Manson_hcs3202_usb_top.jpg.html)
USB, top
\- 
[![\1](../../assets/hardware/general/\2)](./File:Manson_hcs3202_usb_bottom.jpg.html)
USB, bottom
## Protocol See [Manson HCS-3xxx series#Protocol](Manson_HCS-3xxx_series.html#Protocol "Manson HCS-3xxx series"). ## Resources \- [Manual](http://www.manson.com.hk/getimage/index/action/images/name/5652d6182e507.pdf)
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=Manson_HCS-3202&oldid=11894](https://OpenTraceLab.org/w/index.php?title=Manson_HCS-3202&oldid=11894)" 
[Categories](specialcategories-specialcategories.md): \- [Device](./Category:Device.html "Category:Device") \- [Power supply](./Category:Power_supply.html "Category:Power supply") \- [Supported](./Category:Supported.html "Category:Supported")

## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
