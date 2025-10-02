---
title: Hantek 1008C
---

# Hantek 1008C

<div class="infobox" markdown>

![Hantek 1008C](./img/Hantek_1008C_bottom.jpg){ .infobox-image }

### Hantek 1008C

| | |
|---|---|
| **Status** | planned |
| **Channels** | 8 |
| **Samplerate** | 2.4MS/s (see notes) |
| **Samplerate (state)** | ? |
| **Triggers** | edge on either channel |
| **Min/max voltage** | ±500mV / ±20V |
| **Memory** | 4K samples, 12bits each |
| **Compression** | ? |
| **Website** | [hantek.com](http://www.hantek.com.cn/en/ProductDetail_13_13170.html) |

</div>

The **Hantek 1008C** is a USB-based 8-channel oscilloscope (sampling resolution: 12bits on each channel), with 8 channel digital pattern generator.

See [Hantek 1008C/Info](https://sigrok.org/wiki/Hantek_1008C/Info) for some more details (such as **lsusb -vvv** output) on the device.

## Hardware
- **CPU**: ST Microelectronics STM32F103C6T6A
- **Low-dropout voltage regulator**: Advanced Monolithic Systems AMS1117-3.3
- **8-channel analog multiplexer/demultiplexer:** NXP Semiconductor 74HCT4051D (1 per analog channel)
- **Octal 3-state buffer:** Fairchild Semiconductor MM74HC244SJ (in the path of digital outputs)
- **8-bit shift register with 3-state output:** 74HC595 (3 total)
- **Dual opamp:** in MSOP-8 package, Texas Instruments unknown model (chip markings "TI 25 AVG") (1 per analog channel)

1M impedance, DC coupling

ships with one high pressure ignition probe (inductive)

more recent board revision ("Mini DSO V1.00.14 // 2018-11")

- STM32F103C8T6
- AMS1117-3.3 LDO plus (not identified) SMPS U427, no barrel jack, only USB-B
- 8x NXP 74HC4051D, 8x TI 86 AVG (per analog channel)
- 1x TI HC244 (for digital outputs)
- 1x TI 86 AVG (near IDC pin header, A0/A1 signals)
- 3x HC595

## Photos

<div class="photo-grid" markdown>

[![Hantek 1008c Bottom](./img/Hantek_1008C_bottom.jpg)](./img/Hantek_1008C_bottom.jpg "Hantek 1008c Bottom"){ .glightbox data-gallery="hantek-1008c" }
<span class="caption">Hantek 1008c Bottom</span>

[![Hantek 1008c Pcb Ch123](./img/Hantek-1008c-pcb-ch123.jpg)](./img/Hantek-1008c-pcb-ch123.png "Hantek 1008c Pcb Ch123"){ .glightbox data-gallery="hantek-1008c" }
<span class="caption">Hantek 1008c Pcb Ch123</span>

[![Hantek 1008c Pcb Bottom](./img/Hantek-1008c-pcb-bottom.jpg)](./img/Hantek-1008c-pcb-bottom.png "Hantek 1008c Pcb Bottom"){ .glightbox data-gallery="hantek-1008c" }
<span class="caption">Hantek 1008c Pcb Bottom</span>

[![Hantek 1008c Pcb Bottom](./img/Hantek_1008C_pcb_bottom.jpg)](./img/Hantek_1008C_pcb_bottom.jpg "Hantek 1008c Pcb Bottom"){ .glightbox data-gallery="hantek-1008c" }
<span class="caption">Hantek 1008c Pcb Bottom</span>

[![Hantek 1008c Pcb Reg Mcu Gen](./img/Hantek-1008c-pcb-reg-mcu-gen.jpg)](./img/Hantek-1008c-pcb-reg-mcu-gen.png "Hantek 1008c Pcb Reg Mcu Gen"){ .glightbox data-gallery="hantek-1008c" }
<span class="caption">Hantek 1008c Pcb Reg Mcu Gen</span>

[![Hantek 1008c Ic Hc244sj](./img/Hantek_1008C_IC_hc244sj.jpg)](./img/Hantek_1008C_IC_hc244sj.jpg "Hantek 1008c Ic Hc244sj"){ .glightbox data-gallery="hantek-1008c" }
<span class="caption">Hantek 1008c Ic Hc244sj</span>

[![Hantek 1008c Front](./img/Hantek_1008C_front.jpg)](./img/Hantek_1008C_front.jpg "Hantek 1008c Front"){ .glightbox data-gallery="hantek-1008c" }
<span class="caption">Hantek 1008c Front</span>

[![Hantek 1008c Pcb Top](./img/Hantek_1008C_pcb_top.jpg)](./img/Hantek_1008C_pcb_top.jpg "Hantek 1008c Pcb Top"){ .glightbox data-gallery="hantek-1008c" }
<span class="caption">Hantek 1008c Pcb Top</span>

[![Hantek 1008c Case Blinds 1](./img/Hantek-1008c-case-blinds-1.jpg)](./img/Hantek-1008c-case-blinds-1.png "Hantek 1008c Case Blinds 1"){ .glightbox data-gallery="hantek-1008c" }
<span class="caption">Hantek 1008c Case Blinds 1</span>

[![Hantek 1008c Pcb Mounted](./img/Hantek_1008C_pcb_mounted.jpg)](./img/Hantek_1008C_pcb_mounted.jpg "Hantek 1008c Pcb Mounted"){ .glightbox data-gallery="hantek-1008c" }
<span class="caption">Hantek 1008c Pcb Mounted</span>

[![Hantek 1008c Ic Ams1117](./img/Hantek_1008C_IC_ams1117.jpg)](./img/Hantek_1008C_IC_ams1117.jpg "Hantek 1008c Ic Ams1117"){ .glightbox data-gallery="hantek-1008c" }
<span class="caption">Hantek 1008c Ic Ams1117</span>

[![Hantek 1008c Void If Removed](./img/Hantek_1008C_void_if_removed.jpg)](./img/Hantek_1008C_void_if_removed.jpg "Hantek 1008c Void If Removed"){ .glightbox data-gallery="hantek-1008c" }
<span class="caption">Hantek 1008c Void If Removed</span>

[![Hantek 1008c Package Contents](./img/Hantek_1008C_package_contents.jpg)](./img/Hantek_1008C_package_contents.jpg "Hantek 1008c Package Contents"){ .glightbox data-gallery="hantek-1008c" }
<span class="caption">Hantek 1008c Package Contents</span>

[![Hantek 1008c Stm32f1](./img/Hantek_1008C_stm32f1.jpg)](./img/Hantek_1008C_stm32f1.jpg "Hantek 1008c Stm32f1"){ .glightbox data-gallery="hantek-1008c" }
<span class="caption">Hantek 1008c Stm32f1</span>

[![Hantek 1008c Ic 74hc4051d](./img/Hantek_1008C_IC_74hc4051d.jpg)](./img/Hantek_1008C_IC_74hc4051d.jpg "Hantek 1008c Ic 74hc4051d"){ .glightbox data-gallery="hantek-1008c" }
<span class="caption">Hantek 1008c Ic 74hc4051d</span>

[![Hantek 1008c Input Frontend](./img/Hantek_1008C_input_frontend.jpg)](./img/Hantek_1008C_input_frontend.jpg "Hantek 1008c Input Frontend"){ .glightbox data-gallery="hantek-1008c" }
<span class="caption">Hantek 1008c Input Frontend</span>

[![Hantek 1008c Case Blinds 2](./img/Hantek-1008c-case-blinds-2.jpg)](./img/Hantek-1008c-case-blinds-2.png "Hantek 1008c Case Blinds 2"){ .glightbox data-gallery="hantek-1008c" }
<span class="caption">Hantek 1008c Case Blinds 2</span>

[![Hantek 1008c Ic Hc595](./img/Hantek_1008C_IC_hc595.jpg)](./img/Hantek_1008C_IC_hc595.jpg "Hantek 1008c Ic Hc595"){ .glightbox data-gallery="hantek-1008c" }
<span class="caption">Hantek 1008c Ic Hc595</span>

[![Hantek 1008c Top Cover](./img/Hantek_1008C_top_cover.jpg)](./img/Hantek_1008C_top_cover.jpg "Hantek 1008c Top Cover"){ .glightbox data-gallery="hantek-1008c" }
<span class="caption">Hantek 1008c Top Cover</span>

[![Hantek 1008c](./img/Hantek_1008C.jpg)](./img/Hantek_1008C.png "Hantek 1008c"){ .glightbox data-gallery="hantek-1008c" }
<span class="caption">Hantek 1008c</span>

[![Hantek 1008c Pcb Ch78](./img/Hantek-1008c-pcb-ch78.jpg)](./img/Hantek-1008c-pcb-ch78.png "Hantek 1008c Pcb Ch78"){ .glightbox data-gallery="hantek-1008c" }
<span class="caption">Hantek 1008c Pcb Ch78</span>

[![Hantek 1008c Ic Ti25avg](./img/Hantek_1008C_IC_ti25avg.jpg)](./img/Hantek_1008C_IC_ti25avg.jpg "Hantek 1008c Ic Ti25avg"){ .glightbox data-gallery="hantek-1008c" }
<span class="caption">Hantek 1008c Ic Ti25avg</span>

[![Hantek 1008c Back](./img/Hantek_1008C_back.jpg)](./img/Hantek_1008C_back.jpg "Hantek 1008c Back"){ .glightbox data-gallery="hantek-1008c" }
<span class="caption">Hantek 1008c Back</span>

[![Hantek 1008c Pcb Ch3456](./img/Hantek-1008c-pcb-ch3456.jpg)](./img/Hantek-1008c-pcb-ch3456.png "Hantek 1008c Pcb Ch3456"){ .glightbox data-gallery="hantek-1008c" }
<span class="caption">Hantek 1008c Pcb Ch3456</span>

[![Hantek 1008c Front Input](./img/Hantek_1008C_front_input.jpg)](./img/Hantek_1008C_front_input.jpg "Hantek 1008c Front Input"){ .glightbox data-gallery="hantek-1008c" }
<span class="caption">Hantek 1008c Front Input</span>

[![Hantek 1008c Pcb Top](./img/Hantek-1008c-pcb-top.jpg)](./img/Hantek-1008c-pcb-top.png "Hantek 1008c Pcb Top"){ .glightbox data-gallery="hantek-1008c" }
<span class="caption">Hantek 1008c Pcb Top</span>

[![Hantek 1008c V 1 00 4](./img/Hantek_1008C_v_1_00_4.jpg)](./img/Hantek_1008C_v_1_00_4.jpg "Hantek 1008c V 1 00 4"){ .glightbox data-gallery="hantek-1008c" }
<span class="caption">Hantek 1008c V 1 00 4</span>

</div>
### V1.00.4 2012-03

		- 
			[](./img/Hantek_1008C.png)

Device, top

		- 
			[](./img/Hantek_1008C_bottom.jpg)

Device, bottom

		- 
			[](./img/Hantek_1008C_package_contents.jpg)

Package contents

		- 
			[](./img/Hantek_1008C_front.jpg)

Device, front

		- 
			[](./img/Hantek_1008C_back.jpg)

Device, back

		- 
			[](./img/Hantek_1008C_front_input.jpg)

Front inputs

		- 
			[](./img/Hantek_1008C_void_if_removed.jpg)

Void if removed sticker

		- 
			[](./img/Hantek_1008C_top_cover.jpg)

Top cover

		- 
			[](./img/Hantek_1008C_pcb_mounted.jpg)

Top cover removed

		- 
			[](./img/Hantek_1008C_pcb_top.jpg)

PCB, top

		- 
			[](./img/Hantek_1008C_pcb_bottom.jpg)

PCB, bottom

		- 
			[](./img/Hantek_1008C_v_1_00_4.jpg)

PCB revision, v1.00.4

		- 
			[](./img/Hantek_1008C_stm32f1.jpg)

Main CPU, STM32F1

		- 
			[](./img/Hantek_1008C_IC_74hc4051d.jpg)

74HC4051D

		- 
			[](./img/Hantek_1008C_IC_ams1117.jpg)

AMS1117 3.3V LDO

		- 
			[](./img/Hantek_1008C_IC_hc244sj.jpg)

HC224SJ

		- 
			[](./img/Hantek_1008C_IC_hc595.jpg)

HC595

		- 
			[](./img/Hantek_1008C_IC_ti25avg.jpg)

TI25AVG

		- 
			[](./img/Hantek_1008C_input_frontend.jpg)

Analog input circuit

### V1.00.12 2018-11

There is another version ("Mini DSO V1.00.12 // 2018-11") which differs from the images above: Comes in a pouch, ships with eight BNC to alligator cables, lacks a barrel jack, LED position has moved, rubber bumpers around case edges, no silkscreen labels on the case, signal names "engraved", teardown yet to be done. See the (updated) vendor's product page to get an idea.

		- 
			[](./img/Hantek-1008c-pcb-top.png)

PCB top

		- 
			[](./img/Hantek-1008c-pcb-ch123.png)

PCB top, channels 1-3

		- 
			[](./img/Hantek-1008c-pcb-ch3456.png)

PCB top, channels 3-6

		- 
			[](./img/Hantek-1008c-pcb-ch78.png)

PCB top, channels 7-8

		- 
			[](./img/Hantek-1008c-pcb-reg-mcu-gen.png)

PCB top, regulation, MCU, generator, pin expander

		- 
			[](./img/Hantek-1008c-pcb-bottom.png)

PCB bottom

		- 
			[](./img/Hantek-1008c-case-blinds-1.png)

case walls, connector labels

		- 
			[](./img/Hantek-1008c-case-blinds-2.png)

case walls, generator pinout

## Protocol

Need to continuously send commands to the OUT Endpoint, and for each command receive the result from the IN Endpoint (both Endpoints can transfer max 64 bytes).
The device got logically disconnected automatically if not receive any command after 7 seconds.

### List of commands (incomplete)
- A0 -> set number of channel enabled (ie. A0 02: 2 channels are enabled)
- AA -> set which channel to enable (ie. AA 01 01 00 00 00 00 00 00 enable channel 1 and 2)
- A2 -> set voltage level for each channel (ie. A2 03 03 03 03 03 03 03 03 apply +-20V range on each channel)
- A3 -> set sampling rate (ie. A3 00 set highest sampling rate)
- AC -> set sampling rate (ie. AC 07 D0 00 03 42 00 03 42 set highest sampling rate for 2 channels enabled = 1.2MS/s)
- AB -> set trigger level (ie. AB 08 00)
- C1 -> set trigger source and slope (ie. C1 00 00 for Channel 1, rising slope, C1 01 01 for Channel 2, falling slope)
- F3 -> hardware ping (required to send regularly also when acquisition is stoped, otherwise the hardware disconnect)
### Sample of initialization cycle
- B0
- F3
- B901BF040000
- B700
- BB0800
- B5
- B6
- E5
- F7
- F8
- FA
- F5
- A008
- AA0101010101010101
- A311
- C10000
- A70000
- AC01F40009C50009C5
### Start of waiting cycle for data to be ready into the buffers
- F3
- A2 01 01 01 01 01 01 01 01
- A4 01
- C0
- C2
- A5 5A
- A5 5A
### Buffers Reading Cycle
- C6 02 (return Buffer 1 size)
- A6 02 (acquire 64 bytes, 32 samples of 12 bits each, repeated 60 times get 2000 samples)
- C6 03 (return Buffer 2 size)
- A6 03 (acquire 64 bytes, 32 samples of 12 bits each, repeated 60 times get 2000 samples)
## Notes
- Sample rate: maximum measured 2.4MS/s if just 1 channel is enabled. Drop down to 1.2MS/s if enable 2 channels.
- Acquisition: on each scan acquire 4000 bytes (2000 samples) from 2 buffers (2000 samples each buffer)
- Voltage Selector: the most reliable voltage selection is +/-20V, lower hardware voltages present strong non-linearity which make useless the full ADC range of the device (for example +/-500mV range is linear just in the range +500mV -> -80mV.
- Zero offset on ADC is strongly temperature dependent. It drops fast after the device is turned on (even around 50mV on a scale of +-20V). It is suggested to perform the Zero offset calibration and to use this instrument after few minutes that is on, when the temperature stabilize.
## Resources
- [vendor's product page](http://www.hantek.com.cn/en/ProductDetail_13_13170.html)
- [Manual](http://www.hantek.com/Product/Hantek1008/Hantek1008_Manual.pdf)
- [Vendor software](http://www.hantek.com.cn/Product/Hantek1008/Hantek1008_V1.0.8.zip)
- [Decode .DRC data format](https://forums.ni.com/t5/LabVIEW/Hantek-1008C-data-type/td-p/3240415)
- [giwig hantek1008C](https://github.com/giwig/hantek1008C) and [mfg hantek1008py](https://github.com/mfg92/hantek1008py) github repositories, Apache licensed Python code (somehow related to or derived from each other?)
- [A DIY solution to providing hardware based AC COUPLING to HANTEK 1008](https://www.youtube.com/watch?v=OaPVTmd5ins)
- [Make a DIY AC Coupling Adapter for Hantek 1008C](https://www.youtube.com/watch?v=BjPUbO-U-VA)
- [Make an external DIY AC Coupler](https://www.youtube.com/watch?v=gCd4bbuFPNA&t=79s)

