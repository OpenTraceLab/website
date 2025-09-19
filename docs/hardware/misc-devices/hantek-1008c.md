# Hantek 1008C
| | | |:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:| | [*Image: \1* | | | Status | planned | | Channels | 8 | | Samplerate | 2.4MS/s (see notes) | | Samplerate (state) | ? | | Triggers | edge on either channel | | Min/max voltage | ±500mV / ±20V | | Memory | 4K samples, 12bits each | | Compression | ? | | Website | *hantek.com* | **Hantek 1008C** The **Hantek 1008C** is a USB-based 8-channel oscilloscope (sampling resolution: 12bits on each channel), with 8 channel digital pattern generator. See *Hantek 1008C/Info* for some more details (such as **lsusb -vvv** output) on the device.
## Contents
\- *1 Hardware* \- *2 Photos* \- *2.1 V1.00.4 2012-03* \- *2.2 V1.00.12 2018-11* \- *3 Protocol* \- *3.1 List of commands (incomplete)*) \- *3.2 Sample of initialization cycle* \- *3.3 Start of waiting cycle for data to be ready into the buffers* \- *3.4 Buffers Reading Cycle* \- *4 Notes* \- *5 Resources*
## Hardware \- **CPU**: ST Microelectronics STM32F103C6T6A \- **Low-dropout voltage regulator**: Advanced Monolithic Systems AMS1117-3.3 \- **8-channel analog multiplexer/demultiplexer:** NXP Semiconductor 74HCT4051D (1 per analog channel) \- **Octal 3-state buffer:** Fairchild Semiconductor MM74HC244SJ (in the path of digital outputs) \- **8-bit shift register with 3-state output:** 74HC595 (3 total) \- **Dual opamp:** in MSOP-8 package, Texas Instruments unknown model (chip markings "TI 25 AVG") (1 per analog channel) 1M impedance, DC coupling ships with one high pressure ignition probe (inductive) more recent board revision ("Mini DSO V1.00.14 // 2018-11") \- STM32F103C8T6 \- AMS1117-3.3 LDO plus (not identified) SMPS U427, no barrel jack, only USB-B \- 8x NXP 74HC4051D, 8x TI 86 AVG (per analog channel) \- 1x TI HC244 (for digital outputs) \- 1x TI 86 AVG (near IDC pin header, A0/A1 signals) \- 3x HC595 ## Photos ### V1.00.4 2012-03 \-
[*Image: \1*
Device, top
\-
[*Image: \1*
Device, bottom
\-
[*Image: \1*
Package contents
\-
[*Image: \1*
Device, front
\-
[*Image: \1*
Device, back
\-
[*Image: \1*
Front inputs
\-
[*Image: \1*
Void if removed sticker
\-
[*Image: \1*
Top cover
\-
[*Image: \1*
Top cover removed
\-
[*Image: \1*
PCB, top
\-
[*Image: \1*
PCB, bottom
\-
[*Image: \1*
PCB revision, v1.00.4
\-
[*Image: \1*
Main CPU, STM32F1
\-
[*Image: \1*
74HC4051D
\-
[*Image: \1*
AMS1117 3.3V LDO
\-
[*Image: \1*
HC224SJ
\-
[*Image: \1*
HC595
\-
[*Image: \1*
TI25AVG
\-
[*Image: \1*
Analog input circuit
### V1.00.12 2018-11 There is another version ("Mini DSO V1.00.12 // 2018-11") which differs from the images above: Comes in a pouch, ships with eight BNC to alligator cables, lacks a barrel jack, LED position has moved, rubber bumpers around case edges, no silkscreen labels on the case, signal names "engraved", teardown yet to be done. See the (updated) vendor's product page to get an idea. \-
[*Image: \1*
PCB top
\-
[*Image: \1*
PCB top, channels 1-3
\-
[*Image: \1*
PCB top, channels 3-6
\-
[*Image: \1*
PCB top, channels 7-8
\-
[*Image: \1*
PCB top, regulation, MCU, generator, pin expander
\-
[*Image: \1*
PCB bottom
\-
[*Image: \1*
case walls, connector labels
\-
[*Image: \1*
case walls, generator pinout
## Protocol Need to continuously send commands to the OUT Endpoint, and for each command receive the result from the IN Endpoint (both Endpoints can transfer max 64 bytes). The device got logically disconnected automatically if not receive any command after 7 seconds. ### List of commands (incomplete) \- A0 -\> set number of channel enabled (ie. A0 02: 2 channels are enabled) \- AA -\> set which channel to enable (ie. AA 01 01 00 00 00 00 00 00 enable channel 1 and 2) \- A2 -\> set voltage level for each channel (ie. A2 03 03 03 03 03 03 03 03 apply +-20V range on each channel) \- A3 -\> set sampling rate (ie. A3 00 set highest sampling rate) \- AC -\> set sampling rate (ie. AC 07 D0 00 03 42 00 03 42 set highest sampling rate for 2 channels enabled = 1.2MS/s) \- AB -\> set trigger level (ie. AB 08 00) \- C1 -\> set trigger source and slope (ie. C1 00 00 for Channel 1, rising slope, C1 01 01 for Channel 2, falling slope) \- F3 -\> hardware ping (required to send regularly also when acquisition is stoped, otherwise the hardware disconnect) ### Sample of initialization cycle \- B0 \- F3 \- B901BF040000 \- B700 \- BB0800 \- B5 \- B6 \- E5 \- F7 \- F8 \- FA \- F5 \- A008 \- AA0101010101010101 \- A311 \- C10000 \- A70000 \- AC01F40009C50009C5 ### Start of waiting cycle for data to be ready into the buffers \- F3 \- A2 01 01 01 01 01 01 01 01 \- A4 01 \- C0 \- C2 \- A5 5A \- A5 5A ### Buffers Reading Cycle \- C6 02 (return Buffer 1 size) \- A6 02 (acquire 64 bytes, 32 samples of 12 bits each, repeated 60 times get 2000 samples) \- C6 03 (return Buffer 2 size) \- A6 03 (acquire 64 bytes, 32 samples of 12 bits each, repeated 60 times get 2000 samples) ## Notes \- Sample rate: maximum measured 2.4MS/s if just 1 channel is enabled. Drop down to 1.2MS/s if enable 2 channels. \- Acquisition: on each scan acquire 4000 bytes (2000 samples) from 2 buffers (2000 samples each buffer) \- Voltage Selector: the most reliable voltage selection is +/-20V, lower hardware voltages present strong non-linearity which make useless the full ADC range of the device (for example +/-500mV range is linear just in the range +500mV -\> -80mV. \- Zero offset on ADC is strongly temperature dependent. It drops fast after the device is turned on (even around 50mV on a scale of +-20V). It is suggested to perform the Zero offset calibration and to use this instrument after few minutes that is on, when the temperature stabilize. ## Resources \- *vendor's product page* \- [Manual](http://www.hantek.com/Product/Hantek1008/Hantek1008_Manual.pdf) \- [Vendor software](http://www.hantek.com.cn/Product/Hantek1008/Hantek1008_V1.0.8.zip) \- [Decode .DRC data format](https://forums.ni.com/t5/LabVIEW/Hantek-1008C-data-type/td-p/3240415) \- [giwig hantek1008C](https://github.com/giwig/hantek1008C) and [mfg hantek1008py](https://github.com/mfg92/hantek1008py) github repositories, Apache licensed Python code (somehow related to or derived from each other?)  \- [A DIY solution to providing hardware based AC COUPLING to HANTEK 1008](https://www.youtube.com/watch?v=OaPVTmd5ins) \- [Make a DIY AC Coupling Adapter for Hantek 1008C](https://www.youtube.com/watch?v=BjPUbO-U-VA) \- [Make an external DIY AC Coupler](https://www.youtube.com/watch?v=gCd4bbuFPNA&t=79s)
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=Hantek_1008C&oldid=15112](https://OpenTraceLab.org/w/index.php?title=Hantek_1008C&oldid=15112)"
: \- *Device* \- *Oscilloscope* \- *Planned*
## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
