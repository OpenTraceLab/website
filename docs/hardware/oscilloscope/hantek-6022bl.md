# Hantek 6022Bl

| | | |:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------------------:| | [![\1](../../assets/hardware/general/\2)](./File:Hantek_6022be_mugshot.png.html) | | | Status | supported | | Source code | [hantek-6xxx](http://github.com/OpenTraceLab/?p=OpenTraceCapture.git;a=tree;f=src/hardware/hantek-6xxx) | | Channels | 2 | | Samplerate | 48MHz | | Analog bandwidth | 20MHz | | Vertical resolution | 8bit | | Triggers | none (SW-only) | | Input impedance | 1MΩ‖25pF | | Memory | none | | Display | none | | Connectivity | USB | | Website | [hantek.com](http://www.hantek.com/en/ProductDetail_2_153.html) | **Hantek 6022BL** The **Hantek 6022BL** is a USB-based, 2-channel oscilloscope with an analog bandwidth of 20MS/s and 48MS/s sampling rate, and an 8-/16-channel logic analyzer with 24MHz sampling rate. The device can either be used as oscilloscope **or** as logic analyzer, but not both at the same time. I.e., it is **not** a mixed-signal-oscilloscope (MSO). Currently only the 8-channel logic analyzer mode is supported. See [Hantek 6022BL/Info](Hantek_6022BL/Info.html "Hantek 6022BL/Info") for more details (such as **lsusb -v** output) about the device. 
## Contents 
\- [1 Hardware](Hantek_6022BL.html#Hardware) \- [2 Photos](Hantek_6022BL.html#Photos) \- [3 Protocol](Hantek_6022BL.html#Protocol) \- [4 Firmware](Hantek_6022BL.html#Firmware) \- [5 Resources](Hantek_6022BL.html#Resources) 
## Hardware \- **USB**: [Cypress CY7C68013A-100AXC](http://www.cypress.com/documentation/datasheets/cy7c68013a-cy7c68014a-cy7c68015a-cy7c68016a-ez-usb-fx2lp-usb) (FX2LP) ([datasheet](http://www.cypress.com/file/138911/download)) or Corebai CBM9002A ([datasheet](http://corebai.com/en/UploadFiles/20211203/100008155.pdf)) \- **256-byte I²C EEPROM**: 2x [Microchip 24LC02BI](http://www.microchip.com/wwwproducts/en/24LC02B) ([datasheet](http://ww1.microchip.com/downloads/en/DeviceDoc/21709J.pdf)) \- **16-Bit bus transceiver with 3-state outputs**: [TI SN74LVC16245A](http://www.ti.com/product/sn74lvc16245a) ([datasheet](http://www.ti.com/lit/ds/symlink/sn74lvc16245a.pdf)) \- **8-channel analog mux/demux**: 2x [NXP 74HC4051D](http://www.nxp.com/products/discretes-and-logic/logic/8-channel-analog-multiplexer-demultiplexer:74HC4051D) ([datasheet](http://cache.nxp.com/documents/data_sheet/74HC_HCT4051.pdf?pspll=1)) \- **1A low-dropout voltage regulator (3.3V):** [Advanced Monolithic Systems AMS1117-3.3](http://www.advanced-monolithic.com/products/voltreg.html#1117) [datasheet](http://www.advanced-monolithic.com/pdf/ds1117.pdf)) \- **2W, fixed input, isolated & unregulated dual/single output DC/DC converter**: [Mornsun A_S-2WR2 (A0505S-2WR2)](http://www.mornsun.cn/html/product/content/A_S-2WR2.html) ([datasheet](http://www.mornsun.cn/uploads/pdf/A_S-2WR2.pdf)) \- **ADC**: (educated guess, IC covered by glued-on heatsink) \- **8-bit, 40/80/100MHz, dual ADC**: [Analog Devices AD9288](http://www.analog.com/en/products/analog-to-digital-converters/ad-converters/ad9288.html) ([datasheet](http://www.analog.com/media/en/technical-documentation/data-sheets/AD9288.pdf)), or \- **8-bit, 100MHz, dual ADC**: [MXTronix MXT2088](https://translate.google.com/translate?hl=en&sl=zh-CN&tl=en&u=http%3A%2F%2Fwww.mxtronics.com%2Fn107%2Fn124%2Fn181%2Fn184%2Fc692%2Fcontent.html) ([datasheet](http://www.mxtronics.com/n107/n124/n181/n184/c692/attr/2630.pdf)) \- **1.4GHz current feedback amplifiers with enable**: 2x [Intersil EL5166](http://www.intersil.com/en/products/amplifiers-and-buffers/all-amplifiers/amplifiers/EL5166.html) ([datasheet](http://www.intersil.com/content/dam/Intersil/documents/el51/el5166-67.pdf)) \- **145 MHz FastFET Opamps**: 2x [AD8065](http://www.analog.com/en/products/amplifiers/operational-amplifiers/jfet-input-amplifiers/ad8065.html#product-overview): ([datasheet](http://www.analog.com/static/imported-files/data_sheets/AD8065_8066.pdf)), markings "HRA" \- **Crystal**: 24MHz \- **Probes**: 2x PP80B 1X/10X 80MHz bandwidth oscilloscope probes \- **Attenuator**: Hantek HT-201 20:1 attenuator (10MHz bandwidth, 1.053M input resistance) The device has a "H/P" button. Depending on whether or not it's pressed it comes up with different USB VID/PIDs: \- **Pressed**: [04b4:602a Cypress Semiconductor Corp.](Hantek_6022BL/Info.html "Hantek 6022BL/Info") (used for oscilloscope mode) \- **Not pressed**: [0925:3881 Lakeview Research Saleae Logic](Hantek_6022BL/Info.html "Hantek 6022BL/Info") ([Saleae Logic](Saleae_Logic.html "Saleae Logic") VID/PID, so [fx2lafw](Fx2lafw.html "Fx2lafw") works out of the box) **NXP 74HC4051D (upper/lower, CH1/CH2) pinout**:  | Y4 | 1- |  O | -16 | VCC  
---|---|---|---|---  
(GND) Y6 | 2- | -15 | Y2  
(upper EL5166, IN-) Z | 3- | -14 | Y1  
(GND) Y7 | 4- | -13 | Y0  
(GND) Y5 | 5- | -12 | Y3  
(GND) E# | 6- | -11 | S0 (FX2 PA1)  
VEE | 7- | -10 | S1 (FX2 PA2)  
GND | 8- | -9 | S2 (FX2 PA3)  
| (GND) Y4 | 1- |  O | -16 | VCC  
---|---|---|---|---  
(GND) Y6 | 2- | -15 | Y2  
(lower EL5166, IN-) Z | 3- | -14 | Y1  
(GND) Y7 | 4- | -13 | Y0  
(GND) Y5 | 5- | -12 | Y3  
(GND) E# | 6- | -11 | S0 (FX2 PA4)  
VEE | 7- | -10 | S1 (FX2 PA5)  
GND | 8- | -9 | S2 (FX2 PA6)  
| | | | | | |-----|-----|-----|---------------|-------------------------| | S2 | S1 | S0 | 74HC4051D Mux | VDIVs (vendor software) | | 0 | 0 | 0 | Y0 to Z | 200mV | | 0 | 0 | 1 | Y1 to Z | 500mV | | 0 | 1 | 0 | Y2 to Z | 5V, 2V, 1V | | 0 | 1 | 1 | Y3 to Z | 100mV, 50mV, 20mV | **Intersil EL5166 (both) pinout**:  | | | | | | |--------------------------------------------------------------:|----:|-----|-----|-----| | NC | 1- | O | -8 | CE# | | (upper/lower 74HC4051D, Z) IN- | 2- | | -7 | VS+ | | (AD8065, IN-/VOUT) IN+ | 3- | | -6 | OUT | | VS- | 4- | | -5 | NC |  **Microchip 24LC02BI (both) pinout**:  | | | | | | |--------------------------------------------------------:|----:|-----|-----|-------------------------------------------------| | (Low, but not GND) A0 | 1- | O | -8 | VCC | | (GND) A1 | 2- | | -7 | WP (GND) | | (GND) A2 | 3- | | -6 | SCL (FX2 SCL) | | VSS | 4- | | -5 | SDA (FX2 SDA) |  **Analog Devices ADS9288 pinout**: | | | |----------------------------------|----------------------------------------------------------------------------| | AD9288 pins | Description | | S1, S2 | S1 depends on FX2 PA7 (see below), S2 is tied to GND. | | DFS | Tied to GND. Data format select = "offset binary" (not "twos complement"). | | AINA, AINB | Analog input channels. | **Cypress FX2 pinout**:  FX2 pins | Description  
---|---  
CTL0 | Connected to AD9288 ENCA and ENCB and FX2 IFCLK.  
PB0-PB7 | Connected to AD9288 D0A-D7A and SN74LVC16245A 1A1-1A8.  
PD0-PD7 | Connected to AD9288 D0B-D7B and SN74LVC16245A 2A1-2A8.  
PA7 | Connected to the SN74LVC16245A's 1OE# and 2OE# pins (both 8bit groups share the signal) as well as 1DIR and 2DIR. Also connected to the ADC's S1 pin (via two discrete inverters with R37, Q2, R13, Q1). This means PA7 selects between digital (low) and analog (high) data paths, data is always at FX2 ports PB and PD, and either carries 16 digital channels, or two eight bit analog channels. The benefit of "variable DIR" in the SN74LVC16245A is questionable, since it shares the signal with OE# and for high levels the output is high-Z anyway -- so the ADC output is _not_ routed to digital pins when PA7 is high, not tying DIR to a fixed level is pointless(?) | PA7 | Description  
---|---  
1 | Selects scope mode. The ADC's S1 pin is high, which means "Normal operation, data align disabled". The SN74LVC16245A's OE# pins are high ("don't enable output", DIR state is irrelevant).  
0 | Selects LA mode. The ADC's S1 pin is low, which means "Standby both channels A and B". The SN74LVC16245A's OE# pins are low ("output enable") and the DIR pins are low ("B data to A bus", i.e. data direction is from LA connector to FX2).  
PC2 | 1kHz probe calibration pin.  
PC0/PC1 | Dual-color (red/green) LED.  | PC1 | PC0 | LED  
---|---|---  
0 | 0 | ?  
0 | 1 | green  
1 | 0 | red  
1 | 1 | off  
## Photos \- 
[![\1](../../assets/hardware/general/\2)](./File:Hantek_6022bl_box.jpg.html)
\- 
[![\1](../../assets/hardware/general/\2)](./File:Hantek_6022bl_accessories.jpg.html)
\- 
[![\1](../../assets/hardware/general/\2)](./File:Hantek_6022bl_probes.jpg.html)
\- 
[![\1](../../assets/hardware/general/\2)](./File:Hantek_6022bl_20_1_attenuator_ht-201_top.jpg.html)
\- 
[![\1](../../assets/hardware/general/\2)](./File:Hantek_6022bl_20_1_attenuator_ht-201_bottom.jpg.html)
\- 
[![\1](../../assets/hardware/general/\2)](./File:Hantek_6022bl_device_top.jpg.html)
\- 
[![\1](../../assets/hardware/general/\2)](./File:Hantek_6022bl_device_bottom.jpg.html)
\- 
[![\1](../../assets/hardware/general/\2)](./File:Hantek_6022bl_device_connectors.jpg.html)
\- 
[![\1](../../assets/hardware/general/\2)](./File:Hantek_6022bl_device_usb.jpg.html)
\- 
[![\1](../../assets/hardware/general/\2)](./File:Hantek_6022bl_pcb_top.jpg.html)
\- 
[![\1](../../assets/hardware/general/\2)](./File:Hantek_6022bl_pcb_bottom.jpg.html)
\- 
[![\1](../../assets/hardware/general/\2)](./File:Hantek_6022bl_pcb_silkscreen.jpg.html)
\- 
[![\1](../../assets/hardware/general/\2)](./File:Hantek_6022bl_input_stage.jpg.html)
\- 
[![\1](../../assets/hardware/general/\2)](./File:Hantek_6022bl_la_input_stage.jpg.html)
\- 
[![\1](../../assets/hardware/general/\2)](./File:Hantek_6022bl_cypress_fx2lp.jpg.html)
\- 
[![\1](../../assets/hardware/general/\2)](./File:Hantek_6022bl_microchip_24lc02bi_button.jpg.html)
\- 
[![\1](../../assets/hardware/general/\2)](./File:Hantek_6022bl_microchip_24lc02bi.jpg.html)
\- 
[![\1](../../assets/hardware/general/\2)](./File:Hantek_6022bl_ams1117.jpg.html)
\- 
[![\1](../../assets/hardware/general/\2)](./File:Hantek_6022bl_ti_lvc16245a.jpg.html)
\- 
[![\1](../../assets/hardware/general/\2)](./File:Hantek_6022bl_s1661sz_b212fg.jpg.html)
\- 
[![\1](../../assets/hardware/general/\2)](./File:Hantek_6022bl_mornsun_a0505s-2wr2.jpg.html)
\- 
[![\1](../../assets/hardware/general/\2)](./File:Hantek_6022BL_PCB.jpg.html)
\- 
[![\1](../../assets/hardware/general/\2)](./File:Hantek6022BL-CPU.jpg.html)
## Protocol See [Hantek 6022BE#Protocol](Hantek_6022BE.html#Protocol "Hantek 6022BE"). When the "H/P" button is **not** pressed, the device can be used as 8-channel 24MHz logic analyzer via [fx2lafw](Fx2lafw.html "Fx2lafw") out of the box (using the fx2lafw protocol). ## Firmware See [Hantek 6022BE#Firmware](Hantek_6022BE.html#Firmware "Hantek 6022BE"). ## Resources \- [Vendor software and manuals](http://1drv.ms/1gWOsUF) \- [geek-mag.com: The overview of an USB oscillograph Hantek DSO-6022BL with the logical analyzer and gikporny](http://geek-mag.com/posts/255290/)
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=Hantek_6022BL&oldid=16233](https://OpenTraceLab.org/w/index.php?title=Hantek_6022BL&oldid=16233)" 
[Categories](specialcategories-specialcategories.md): \- [Device](./Category:Device.html "Category:Device") \- [Oscilloscope](./Category:Oscilloscope.html "Category:Oscilloscope") \- [Logic analyzer](./Category:Logic_analyzer.html "Category:Logic analyzer") \- [Supported](./Category:Supported.html "Category:Supported")

## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
