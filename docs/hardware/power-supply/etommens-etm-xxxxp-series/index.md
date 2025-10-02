---
title: ETommens eTM-xxxxP Series
---

# ETommens eTM-xxxxP Series

<div class="infobox" markdown>

![ETommens eTM-xxxxP Series](./img/Sigrok_logo_no_text_transparent_512.png){ .infobox-image }

### ETommens eTM-xxxxP Series

| | |
|---|---|
| **Status** | in progress |
| **Source code** | [etommens-etm-xxxxp](https://github.com/OpenTraceLab/OpenTraceCapture/tree/main/src/hardware/etommens-etm-xxxxp) |
| **Channels** | 1 |
| **Voltage/current (CH1)** | various |
| **Connectivity** | USB/serial, RS232 |
| **Features** | programmable presets, over voltage protection, over current protection, output on/off |
| **Website** | [etommens.com](http://www.etommens.com/products-258560-258566-0.html#bodycontent) |

</div>

The **eTommens eTM-xxxxP** series are 1 channel switch-mode programmable DC power supplies with both USB/serial and RS232 connectivity.

The devices are also sold as rebranded versions by e.g. [Hanmatek](https://sigrok.org/wiki/Hanmatek_HM305P) and Rockseed.

## Devices
| Device | OEM/Rebranded | Voltage range | Current range | Power | Resolution | Port Class, Model |
|---|---|---|---|---|---|---|
| [eTommens eTM305P](http://www.etommens.com/products-258560-258566-0.html#bodycontent) | [Hanmatek HM305P](https://sigrok.org/wiki/Hanmatek_HM305P), Rockseed RS305P | 0-30 V | 0-5 A | 150 W | 10mv | 0x4B50, 305 |
| [eTommens eTM3010P](http://www.etommens.com/products-258560-258566-0.html#bodycontent) | Hanmatek HM310P, [RockSeed RS310P](https://sigrok.org/wiki/RockSeed_RS310P) | 0-30 V | 0-10 A | 300 W | 10mv | 0x4B50, 3010 |
| [eTommens eTM1003P](http://www.etommens.com/products-258560-258566-0.html#bodycontent) | — | 0-100 V | 0-3 A | 300 W | 10mv | — |
| [eTommens eTM1520P](http://www.etommens.com/products-258560-258566-0.html#bodycontent) | — | 0-15 V | 0-20 A | 300 W | 10mv | — |
| [eTommens eTM605P](http://www.etommens.com/products-258560-258566-0.html#bodycontent) | Rockseed RS605P | 0-60 V | 0-5 A | 300 W | 10mv | — |
| [eTommens eTM1502P](http://www.etommens.com/products-258560-258566-0.html#bodycontent) | — | 0-150 V | 0-2 A | 300 W | 10mv | — |

**Note:** libsigrok support for these devices is pending the merge of this PR - [https://github.com/sigrokproject/libsigrok/pull/100](https://github.com/sigrokproject/libsigrok/pull/100)

**Note:** The libsigrok driver needs to know about the device's class and model, retrievable with [hm305.py](https://github.com/markrages/py_test_interface) please let us know.

## Protocol

Modbus RTU only function codes 0x03 and 0x06 are supported (according to the pdf that came with the device).([Wikipedia](https://en.wikipedia.org/wiki/Modbus#Frame_formats)). Baudrate defaults to 9600, 1 start bit, 8 data bits, no checkbits and 1 stop bit. Registers are 16bits, bigendian.

| Name | Register Address | Access |
|---|---|---|
| Output State | 0x0001 | RW |
| Protection State | 0x0002 | R |
| Model ID | 0x0004 | R |
| Output Voltage | 0x0010 | R |
| Output Current | 0x0011 | R |
| Output Power high bits | 0x0012 | R |
| Output Power low bits | 0x0013 | R |
| Voltage Target | 0x0030 | RW |
| Current Limit | 0x0031 | RW |
| OVP Value | 0x0020 | RW |
| OCP Value | 0x0021 | RW |
| OPP Value high bits | 0x0022 | RW |
| OPP Value low bits | 0x0023 | RW |
| Decimals | 0x0005 | R |

1. There is actually no OPP button on the power supply, but the protocol documentation lists, the address for it. Not relevant at the moment for a driver, since sigrok seems to have no OPP support anyway.
2. In the protocol documentation there is no mention of how to set the presets M1 to M6. But it seems they start at address 0x1000. This needs to be researched still, but I currently do not know how to handle presets in sigrok, so I need to find that out too.
Also there is some other addresses listed in config files that are with the software provided, these need to be researched too.

3. The Protection State registers contains looks as follow and the designated bit goes high if the protection state is active:

| Bit | Designation | Description |
|---|---|---|
| 0 | OVP | Over Voltage Protection |
| 1 | OCP | Over Current Protection |
| 2 | OPP | Over Power Protection |
| 3 | OTP | Over Temperature Protection |
| 4 | SCP | Short Circuit Protection |
| 5 |  |  |
| 6 |  |  |
| 7 |  |  |
| 8 |  |  |

the 2nd byte does not give any information, and seems to always be 0.

4. The decimals registers contains the the decimal information for Voltage, Current and Power. The lower 12 bits are used with 4bits for each value. If the register content is 0x0321, it means Voltage has 3 decimals, Current 2 and Power 1.

Researched Registers:

| Name | Register Address | Access | Notes |
|---|---|---|---|
| Voltage upper Limit (UH) | 0xC11E | R | 4 bytes long, contains high voltage limit (like the limit you get when turning the knob on the device), did not even try to write to it, values are same as current in format so divide int value by 10^digits |
| Current upper Limit (IH) | 0xC12E | R | 4 bytes long, contains high current limit (like the limit you get when turning the knob on the device), did not even try to write to it, values are same as current in format so divide int value by 10^digits |
| Voltage lower Limit? (UL) | 0xC110 | R | 4 bytes long, not sure what this is, it contains the value 10. But my supply outputs at 1 already. |
| Current lower Limit? (IL) | 0xC120 | R | 4 bytes long, not sure what this is, it contains the value 21. And my power supply actually only starts outputting when set to 21mA or above. |
| Buzzer | 0x8804 | RW | 2 bytes long, you can enable (write 0x0001) or disable (write 0x0000) the buzzer. It beeps on every single click (and on startup ) so probably no one wants to enable this ever. |
| defaultshow | 0x8802 | ? | 2 bytes long, no idea what it is about |
| powerstat | 0x8801 | ? | 2 bytes long, no idea what it is about |
| scp | 0x8803 | R | 2 bytes long, no idea what it is about, i can't write to it, maybe my model just has no scp support? |
| sdtime | 0xCCCC | ? | 2 bytes long, no idea what it is about |
| settimespan | 0x0032 | ? | 2 bytes long, timespan till it auto disables output, but only if you use the preset list function. Don't see how this is useful for anything since the value only matters per preset. |
| preset voltage | 0x1000+(0 to 5)*10 | RW | 2 bytes long, registers for presets M1 to M6 |
| preset current | 0x1001+(0 to 5)*10 | RW | 2 bytes long, registers for presets M1 to M6 |
| preset timespan | 0x1002+(0 to 5)*10 | RW | 2 bytes long, registers for presets M1 to M6, max value 9999 (this is seconds, so max is about 2,78h) |
| preset enabled (included in list) | 0x1003+(0 to 5)*10 | RW | 2 bytes long, registers for presets M1 to M6 |

## Resources
- [EEVblog forum thread](https://www.eevblog.com/forum/testgear/power-supply-ripe-for-the-picking/)
- [GitHub - Basic Python control script](https://github.com/markrages/py_test_interface)
- [GitHub - Python control script with proper CLI, SCPI support and more](https://github.com/JackDoan/hm305_ctrl)
- [GitHub - Electron based application, offers Charts and CSV Export](https://github.com/hobbyquaker/hanmatek-hm310p)

## Photos

<div class="photo-grid" markdown>

[![Sigrok Logo No Text Transparent 512](./img/Sigrok_logo_no_text_transparent_512.png)](./img/Sigrok_logo_no_text_transparent_512.png "Sigrok Logo No Text Transparent 512"){ .glightbox data-gallery="etommens-etm-xxxxp-series" }
<span class="caption">Sigrok Logo No Text Transparent 512</span>

</div>
