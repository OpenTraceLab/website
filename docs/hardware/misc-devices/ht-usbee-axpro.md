# Ht Usbee Axpro

**HT USBee-AxPro** [![\1](../../assets/hardware/general/\2)](./File:Ht_usbee_axpro_v5_mugshot.png.html) |   
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
Website | [aliexpress.com](http://de.aliexpress.com/item/New-3-in-1-Tool-Oscilloscope-Logic-Analyzer-ALTERA-Saleae8-USBEE-AX-PRO-Altera-USB-Blaster/32236912930.html)  
**HT USBee-AxPro** The **HT USBee-AxPro** is a USB-based, 8-channel logic analyzer with up to 24MHz sampling rate, with 1 additional analog channel (3MHz analog bandwidth). It is able to switch between USBee AX-Pro, Salea Logic and Altera USB blaster mode via a button. When pressing the button the USB VID/PID changes. It is a clone of the [CWAV USBee AX-Pro](https://OpenTraceLab.org/w/index.php?title=CWAV_USBee_AX-Pro&action=edit&redlink=1 "CWAV USBee AX-Pro \(page does not exist\)"). In OpenTraceLab, we use the open-source [fx2lafw](Fx2lafw.html "Fx2lafw") firmware for this logic analyzer. See [HT USBee-AxPro/Info](HT_USBee-AxPro/Info.html "HT USBee-AxPro/Info") for some more details (such as **lsusb -v** output) on the device. 
## Contents 
\- [1 Hardware](HT_USBee-AxPro.html#Hardware) \- [1.1 FX2LP pin mappings](HT_USBee-AxPro.html#FX2LP_pin_mappings) \- [1.2 Analog frontend](HT_USBee-AxPro.html#Analog_frontend) \- [1.3 Pin mappings](HT_USBee-AxPro.html#Pin_mappings) \- [2 Photos](HT_USBee-AxPro.html#Photos) \- [3 Protocol](HT_USBee-AxPro.html#Protocol) \- [4 Resources](HT_USBee-AxPro.html#Resources) 
## Hardware **HT2013 V5.00**: \- **Main chip**: [Cypress CY7C68013A-56SSOP (FX2LP)](http://www.cypress.com/?docID=45142) \- **64Kbit I²C EEPROM**: [Microchip 24LC641](http://ww1.microchip.com/downloads/en/DeviceDoc/21189f.pdf) \- **2Kbit I²C EEPROM**: [Microchip 24LC02B](http://ww1.microchip.com/downloads/en/DeviceDoc/21709c.pdf) \- **Auxiliary 8051 chip**: [ST STM8S003F3](http://www.st.com/web/en/resource/technical/document/datasheet/DM00024550.pdf) (used for handling the button) \- **Supply voltage regulator**: Advanced Monolithic Systems AMS1117-3.3 \- **Analog-to-digital converter**: [Texas Instruments TLC5510I](http://www.ti.com/lit/ds/symlink/tlc5510.pdf) \- **Analog input amplifiers**: [Analog Devices AD8065](http://www.analog.com/static/imported-files/data_sheets/AD8065_8066.pdf) (SMD marking "HRA") \- **Analog amplifiers negative supply**: [Intersil ICL7660 (7660 AIBAZ V120428A)](http://www.intersil.com/content/dam/Intersil/documents/icl7/icl7660.pdf) \- **Crystal**: 24MHz ### FX2LP pin mappings | | | | | |-----|--------|-------------|-----------------| | \\# | Pin | Destination | Remark | | | CTL2 | ADC_CLK | ADC clock | | | PD0..7 | ADC_D1..8 | ADC data output | ### Analog frontend **Schematics**: [![\1](../../assets/hardware/general/\2)](./File:Ht-usbee-axpro_analog_schematics.svg.html) **Notes**: \- Some devices have R2 = 66.5Ω (instead of 66.5kΩ), this basically limits the range to -3.3V — +3.3V. \- TLC5510 is used with ~3.3V "reference" from LDO output which is both out of the allowed range and is a major source of inaccuracy. \- Some devices (probably those that do not have U5 populated) produce bogus min and max spikes when measuring certain voltages, this can probably be remedied by adding small (on the order of 10s pF) capacitance to U5 Vcc and GND pins or to the ADC CLK line. **HT_V6.0**: \- ... ### Pin mappings The FX2 CTL2 and PD0..7 pins are mapped exactly like the **HT2013 V5.00** version. The TLC5510I OE# pin is tied to GND. ## Photos **HT2013 V5.00**: \- 
[![\1](../../assets/hardware/general/\2)](./File:Ht-usbee-axpro_package.jpg.html)
Device package
\- 
[![\1](../../assets/hardware/general/\2)](./File:Ht-usbee_case_front.jpg.html)
Case, front
\- 
[![\1](../../assets/hardware/general/\2)](./File:Ht-usbee_device.jpg.html)
Device
\- 
[![\1](../../assets/hardware/general/\2)](./File:Ht-usbee_pcb_front.jpg.html)
PCB, front
\- 
[![\1](../../assets/hardware/general/\2)](./File:PCB3.jpg.html)
PCB, front
\- 
[![\1](../../assets/hardware/general/\2)](./File:Ht-usbee_pcb.jpg.html)
PCB, front
\- 
[![\1](../../assets/hardware/general/\2)](./File:Ht-usbee_backside.jpg.html)
PCB, back
\- 
[![\1](../../assets/hardware/general/\2)](./File:TLC5510I.jpg.html)
TLC5510I
\- 
[![\1](../../assets/hardware/general/\2)](./File:STM8_1.jpg.html)
STM8 1
\- 
[![\1](../../assets/hardware/general/\2)](./File:SM8_2.jpg.html)
STM8 2
\- 
[![\1](../../assets/hardware/general/\2)](./File:Probe_adaptor.jpg.html)
Probe adaptor
\- 
[![\1](../../assets/hardware/general/\2)](./File:FX2.jpg.html)
FX2
\- 
[![\1](../../assets/hardware/general/\2)](./File:Expansion_board.jpg.html)
Expansion board
\- 
[![\1](../../assets/hardware/general/\2)](./File:AMS1117.jpg.html)
AMS1117
\- 
[![\1](../../assets/hardware/general/\2)](./File:7660.jpg.html)
7660
\- 
[![\1](../../assets/hardware/general/\2)](./File:24LC64.jpg.html)
24LC64
\- 
[![\1](../../assets/hardware/general/\2)](./File:24LC02B.jpg.html)
24LC02B
\- 
[![\1](../../assets/hardware/general/\2)](./File:Ht-usbee-axpro_no_siggen_pcb.jpg.html)
Version without signal generator
\- 
[![\1](../../assets/hardware/general/\2)](./File:Ht-usbee-axpro_no_siggen_case.jpg.html)
Version without signal generator case
**HT2013 V5.00 (no blue button PCB)**: \- 
[![\1](../../assets/hardware/general/\2)](./File:Ht_usbee_axpro_v5_package_contents.jpg.html)
Package contents
\- 
[![\1](../../assets/hardware/general/\2)](./File:Ht_usbee_axpro_v5_device_top.jpg.html)
Device, top
\- 
[![\1](../../assets/hardware/general/\2)](./File:Ht_usbee_axpro_v5_device_bottom.jpg.html)
Device, bottom
\- 
[![\1](../../assets/hardware/general/\2)](./File:Ht_usbee_axpro_v5_connector.jpg.html)
Connector
\- 
[![\1](../../assets/hardware/general/\2)](./File:Ht_usbee_axpro_v5_usb.jpg.html)
USB
\- 
[![\1](../../assets/hardware/general/\2)](./File:Ht_usbee_axpro_v5_analog_connector_top.jpg.html)
Analog connector, top
\- 
[![\1](../../assets/hardware/general/\2)](./File:Ht_usbee_axpro_v5_analog_connector_bottom.jpg.html)
Analog connector, bottom
\- 
[![\1](../../assets/hardware/general/\2)](./File:Ht_usbee_axpro_v5_button_conn.jpg.html)
Button connector
\- 
[![\1](../../assets/hardware/general/\2)](./File:Ht_usbee_axpro_v5_pcb_top.jpg.html)
PCB, top
\- 
[![\1](../../assets/hardware/general/\2)](./File:Ht_usbee_axpro_v5_pcb_bottom.jpg.html)
PCB, bottom
\- 
[![\1](../../assets/hardware/general/\2)](./File:Ht_usbee_axpro_v5_cypress_fx2.jpg.html)
Cypress FX2
\- 
[![\1](../../assets/hardware/general/\2)](./File:Ht_usbee_axpro_v5_st_stm8s003f3.jpg.html)
ST STM8S003F3
\- 
[![\1](../../assets/hardware/general/\2)](./File:Ht_usbee_axpro_v5_microchip_24lc64i.jpg.html)
Microchip 24LC64I
\- 
[![\1](../../assets/hardware/general/\2)](./File:Ht_usbee_axpro_v5_microchip_24lc02bi.jpg.html)
Microchip 24LC02BI
\- 
[![\1](../../assets/hardware/general/\2)](./File:Ht_usbee_axpro_v5_intersil_icl7660.jpg.html)
Intersil ICL7660
\- 
[![\1](../../assets/hardware/general/\2)](./File:Ht_usbee_axpro_v5_ti_tlc5510i.jpg.html)
TI TLC5510I
\- 
[![\1](../../assets/hardware/general/\2)](./File:Ht_usbee_axpro_v5_ams1117-3.3.jpg.html)
AMS1117-3.3
**HT_V6.0**: \- 
[![\1](../../assets/hardware/general/\2)](./File:Ht_usbee_axpro_package_contents.jpg.html)
Package contents
\- 
[![\1](../../assets/hardware/general/\2)](./File:Ht_usbee_axpro_device_top.jpg.html)
Device, top
\- 
[![\1](../../assets/hardware/general/\2)](./File:Ht_usbee_axpro_device_bottom.jpg.html)
Device, bottom
\- 
[![\1](../../assets/hardware/general/\2)](./File:Ht_usbee_axpro_connector.jpg.html)
Connector
\- 
[![\1](../../assets/hardware/general/\2)](./File:Ht_usbee_axpro_usb.jpg.html)
USB
\- 
[![\1](../../assets/hardware/general/\2)](./File:Ht_usbee_axpro_analog_adapter_top.jpg.html)
Analog adapter, top
\- 
[![\1](../../assets/hardware/general/\2)](./File:Ht_usbee_axpro_analog_adapter_bottom.jpg.html)
Analog adapter, bottom
\- 
[![\1](../../assets/hardware/general/\2)](./File:Ht_usbee_axpro_pcb_top.jpg.html)
PCB, top
\- 
[![\1](../../assets/hardware/general/\2)](./File:Ht_usbee_axpro_pcb_bottom.jpg.html)
PCB, bottom
\- 
[![\1](../../assets/hardware/general/\2)](./File:Ht_usbee_axpro_cypress_fx2.jpg.html)
Cypress FX2
\- 
[![\1](../../assets/hardware/general/\2)](./File:Ht_usbee_axpro_microchip_24lc02b.jpg.html)
Microchip 24LC02B
\- 
[![\1](../../assets/hardware/general/\2)](./File:Ht_usbee_axpro_tlc5510i.jpg.html)
TI TLC5510I
\- 
[![\1](../../assets/hardware/general/\2)](./File:Ht_usbee_axpro_intersil_icl7660s.jpg.html)
Intersil ICL7660S
\- 
[![\1](../../assets/hardware/general/\2)](./File:Ht_usbee_axpro_ams1117-3.3.jpg.html)
AMS1117-3.3
\- 
[![\1](../../assets/hardware/general/\2)](./File:Ht_usbee_axpro_hra.jpg.html)
HRA
\- 
[![\1](../../assets/hardware/general/\2)](./File:Ht_usbee_axpro_24mhz_crystal.jpg.html)
24MHz crystal
## Protocol Since we use the open-source [fx2lafw](Fx2lafw.html "Fx2lafw") firmware for this device, we don't need to know the protocol. ## Resources \- [epanorama.net: HT-USBee AxPro review](http://www.epanorama.net/newepa/2014/06/17/ht-usbee-axpro-review/) \- [Itead: Saleae8 / USBEE AX PRO / Altera Combination: Logic Analyzer](https://www.itead.cc/saleae8-usbee-ax-pro-altera-combination-logic-analyzer.html)
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=HT_USBee-AxPro&oldid=14406](https://OpenTraceLab.org/w/index.php?title=HT_USBee-AxPro&oldid=14406)" 
[Categories](specialcategories-specialcategories.md): \- [Device](./Category:Device.html "Category:Device") \- [Logic analyzer](./Category:Logic_analyzer.html "Category:Logic analyzer") \- [Oscilloscope](./Category:Oscilloscope.html "Category:Oscilloscope") \- [Mixed-signal oscilloscope](./Category:Mixed-signal_oscilloscope.html "Category:Mixed-signal oscilloscope") \- [Supported](./Category:Supported.html "Category:Supported")

## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
