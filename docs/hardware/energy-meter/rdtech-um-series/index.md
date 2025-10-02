---
title: RDTech UM series
---

# RDTech UM series

<div class="infobox" markdown>

![RDTech UM series](./img/UM24C_board_3.jpg){ .infobox-image }

### RDTech UM series

| | |
|---|---|
| **Status** | supported |
| **Source code** | [rdtech-um](https://github.com/OpenTraceLab/OpenTraceCapture/tree/main/src/hardware/rdtech-um) |
| **Connectivity** | serial over Bluetooth |
| **Measurements** | voltage, current, power, energy, voltage over USB data lines |
| **Features** | measures USB devices; color display (26x26mm, 128x128px) |
| **Website** | [rdtech.aliexpress.com](http://rdtech.aliexpress.com/) |

</div>

The RDTech UM24C, UM25C and UM34C are USB load meters which can measure various properties for USB devices including their voltage, amperage, wattage, resistance, capacity, temperature, data line voltage, and charging mode.

## Model dependent features

The RDTech UM24C, UM25C and UM34C can measure supply voltage, supply current, supply power, cable resistance, charged capacity, (measurement device's) temperature, USB data line voltage, and USB charging mode. They can track up to 11 groups of mAh/mWh capacity data, one of which is ephemeral (and disappears after replugging the device), nine of which are persistent until cleared, and one of which whose recording is only activated above a certain current threshold (and which can be recorded in parallel with any of the other 10 data groups). They also allow graphing the amperage and voltage over time, on the device's display itself, as well as rotating the display contents into any orientation.

The UM24C, UM25C and UM34C are extremely similar, but have several differences:

- UM24C supports USB-A male / USB-microB female line, USB-A female load.
- UM25C supports USB-A male / USB-microB female / USB-C female line, USB-A female / USB-C female load.
- UM34C supports USB-A male / USB-microB female / USB-C female line, USB-A female load.
- UM34C supports USB 3.0 data passthrough; UM24C/UM25C are USB 2.0 only.
- UM25C displays and sends 1mV / 0.1mA live resolution, UM24C/UM34C are 10mV / 1mA live resolution.  Note that this is applicable for instantaneous view only; aggregates are the same for all three models.
- UM24C is maximum 3A current, UM34C is 4A, UM25C is 5A.
- UM24C only supports detection of unknown (normal) charging mode, QC2.0 and QC3.0, UM25C and UM34C support detecting additional charging modes.  This does not affect the line/load from negotiating a charging mode, just the meter's ability to detect it.
- UM25C and UM34C have a switch which lets you turn on and off the Bluetooth functionality.
- UM24C is not supported by their Apple app, only UM25C and UM34C.

The UM25C is the most fully featured of the three, but is missing USB 3.0 data passthrough (UM34C only).  If you have to buy one, get the UM25C, but if possible get both the UM25C and UM34C.  The UM24C is a slightly older product feature-wise.

The meter can be connected to power by plugging it into any one of the supported line inputs (see above; the different line options vary by model).  Besides allowing for different connection options, there is a function within the UI to calculate the impedance of a cable by running a test first directly plugged in to a power supply, then unplugging and running again via the cable.  Otherwise, line functionality is identical no matter which line input you choose.

The manufacturer has indicated that the firmware is not designed to be upgradeable and doesn't provide updates; nevertheless, the SWIM pin for the on-board STM8 chip is exposed, as are the other necessary pins for STM8 debugging. It's unclear whether the chip will allow eg. dumping, though.

It's unclear whether measurement of data lines is accurate enough to theoretically be used as a logic analyzer, but given the strange stability of the values during testing (unlike the voltage on the power lines) and the low-end STM8 chip, I suspect it's not.

## Example use

```
 $ **sigrok-cli -d rdtech-um:conn=bt/rfcomm/00-15-a3-00-4f-dd --scan**
 The following devices were found:
 rdtech-um - RDTech UM25C with 6 channels: V I D+ D- T E

``````
 $ **sigrok-cli -d rdtech-um:conn=bt/rfcomm/00-15-a3-00-4f-dd --frames 10**
 V: 5.19 V
 I: 0 mA
 D+: 0.00 V
 D-: 0.00 V
 T: 29 C
 E: 0 mWh
 ...

```

## Bluetooth communication

Unlike most devices of this type, these communicate through serial-over-Bluetooth (RFCOMM); the manufacturer provides apps (for Android, Windows and Apple iOS; downloads including device documentation [here](https://www.mediafire.com/folder/0jt6xx2cyn7jt/UM24)), but not protocol documentation nor source code.  On the C models, the Bluetooth board is a separate layer that connects to the serial pads using pogo pins (UM24C) or scissor-spring tension pins (UM25C, UM34C).  UM24C has a generic open module board with a Beken BK3231 chipset. UM25C and UM34C have a shielded DX-BT18 module board (which should be compatible with HC-05/HC-06).

There is no Enable pin passed between the Bluetooth board and the main board; the model name is (presumably) programmed into the module in Command mode at the factory, and the module is always in Data mode during normal operation. Some devices provide power switches for the Bluetooth module. Communication between the boards is done at 9600 8-N-1.

Note that this is specifically about the **C** models - the UM24, UM25 and UM34 are the exact same functionality but *without* Bluetooth communication.  The UM25 and UM34 have pads which you could solder a TTL adapter to (if you disassemble the device) and get the same functionality.  The UM24 has pads, but the firmware does not appear to support communication.

## Protocol

Approximately 500ms after applying power, the device sends 0xff.  However, this is usually before a Bluetooth connection can be established, so the host end will likely never see it.

1-byte commands are sent to the device, and in the case of 0xf0, the device responds with a 130-byte data dump of the current device status.  All other commands return no acknowledgement.

Each device (UM24C, UM25C, UM34C) has a similar command and response format, but the commands and responses vary slightly by device type.  These variations are documented below.  Unfortunately this means you will need to know what type of device you are communicating with to take full advantage of it.

### Commands to send

Multiple commands may be sent at once; e.g. you could set the recording threshold to 0.28 A and rotate the screen by sending 0xccf2 immediately.  An exception appears to be requesting the data dump; it doesn't seem to return the 130-byte response unless you wait a bit (approximately 0.2 seconds) after sending other commands.

| Device | Byte | Type | Meaning |
|---|---|---|---|
| UM24C/UM25C/UM34C | 0xf0 | device control | Request new data dump; this triggers a 130-byte response |
| UM24C/UM25C/UM34C | 0xf1 | device control | Go to next screen |
| UM24C/UM25C/UM34C | 0xf2 | device control | Rotate screen |
| UM24C | 0xf3 | device control | Switch to next data group |
| UM25C/UM34C | 0xf3 | device control | Go to the previous screen |
| UM24C/UM25C/UM34C | 0xf4 | device control | Clear data group |
| UM25C/UM34C | 0xa0 - 0xa9 | device control | Set the selected data group (0-9) |
| UM24C/UM25C/UM34C | 0xb0 - 0xce | configuration | Set recording threshold to a value between 0.00 and 0.30 A (inclusive); add the value after the decimal point to 0xb0 (0.00 is 0xb0, 0.30 is 0xce) |
| UM24C/UM25C/UM34C | 0xd0 - 0xd5 | configuration | Set device backlight level between 0 and 5 (inclusive); 0 is dim, 5 is full brightness |
| UM24C/UM25C/UM34C | 0xe0 - 0xe9 | configuration | Set screen timeout ("screensaver") between 0 and 9 minutes (inclusive), where 0 disables the screensaver |

### Response format

All byte offsets are in decimal, and inclusive. All values are big-endian and unsigned.

| Offset | Length | Type | Meaning |
|---|---|---|---|
| 0 | 2 | model | Model ID (see below) |
| 2 | 2 | measurement | Voltage - UM25C: millivolts (divide by 1000 to get V), UM24C/UM34C: centivolts (divide by 100 to get V) |
| 4 | 2 | measurement | Amperage - UM25C tenth-milliamps (divide by 10000 to get A), UM24C/UM34C: milliamps (divide by 1000 to get A) |
| 6 | 4 | measurement | Wattage (in mW, divide by 1000 to get W) |
| 10 | 2 | measurement | Temperature (in Celsius) |
| 12 | 2 | measurement | Temperature (in Fahrenheit) |
| 14 | 2 | configuration | Currently selected data group, zero-indexed |
| 16 | 80 | measurement | Array of 10 main capacity data groups (where the first one, group 0, is the ephemeral one) -- for each data group: 4 bytes mAh, 4 bytes mWh |
| 96 | 2 | measurement | USB data line voltage (positive) in centivolts (divide by 100 to get V) |
| 98 | 2 | measurement | USB data line voltage (negative) in centivolts (divide by 100 to get V) |
| 100 | 2 | measurement | Charging mode index, see below |
| 102 | 4 | measurement | mAh from threshold-based recording |
| 106 | 4 | measurement | mWh from threshold-based recording |
| 110 | 2 | configuration | Currently configured threshold for recording (in centiamps, divide by 100 to get A) |
| 112 | 4 | measurement | Duration of threshold recording, in cumulative seconds |
| 116 | 2 | configuration | Threshold recording active (1 if recording, 0 if not) |
| 118 | 2 | configuration | Current screen timeout setting, in minutes (0-9, 0 is no screen timeout) |
| 120 | 2 | configuration | Current backlight setting (0-5, 0 is dim, 5 is full brightness) |
| 122 | 4 | measurement | Resistance in deci-ohms (divide by 10 to get ohms) |
| 126 | 2 | configuration | Current screen (zero-indexed, same order as on device) |
| 128 | 1 | unknown | See below |
| 129 | 1 | checksum/unknown | Checksum (UM34C) or unknown. See below. |

### Known models

The Android app uses the first two bytes to determine the model number. The following models are known:

| ID | Model |
|---|---|
| 0x0963 | UM24C |
| 0x09c9 | UM25C |
| 0x0d4c | UM34C |

### Charging modes

Not all devices support detection of all listed charging modes, but the index between devices is consistent (e.g. index 1 will always be QC2).

| Index | Display | Meaning |
|---|---|---|
| 0 | UNKNOWN | Unknown, or normal (non-custom mode) |
| 1 | QC2 | Qualcomm Quick Charge 2.0 |
| 2 | QC3 | Qualcomm Quick Charge 3.0 |
| 3 | APP2.4A | Apple, max 2.4 Amp |
| 4 | APP2.1A | Apple, max 2.1 Amp |
| 5 | APP1.0A | Apple, max 1.0 Amp |
| 6 | APP0.5A | Apple, max 0.5 Amp |
| 7 | DCP1.5A | Dedicated Charging Port, max 1.5 Amp (D+ to D- short) |
| 8 | SAMSUNG | Samsung (Adaptive Fast Charging?) |

### Unknown response fields

Bytes 128+129 are not entirely known yet.  They are believed to be stop markers.

On UM24C and UM25C, all observed units seem to be 0xfff1 so far.

On UM34C, the last two bytes vary each time the device is polled.  The values drift up and down over time, but will change completely after a device reset.  For example:

```
2019-02-09 16:55:35,150 DEBUG: Start: 0x0d4c, end: 0x79cd
2019-02-09 16:55:47,837 DEBUG: Start: 0x0d4c, end: 0x75f8
2019-02-09 16:55:49,031 DEBUG: Start: 0x0d4c, end: 0x78c3
2019-02-09 16:56:08,855 DEBUG: Start: 0x0d4c, end: 0x7bd9
[reset]
2019-02-09 16:58:01,091 DEBUG: Start: 0x0d4c, end: 0x2c2d
2019-02-09 16:58:52,247 DEBUG: Start: 0x0d4c, end: 0x19e5
2019-02-09 16:59:10,683 DEBUG: Start: 0x0d4c, end: 0x19e5
2019-02-09 16:59:29,816 DEBUG: Start: 0x0d4c, end: 0x18ea

```

These are most likely checksums of some sort.  Here's some full sample dumps:

```
0d 4c 01 fe 00 00 00 00 00 00 00 14 00 44 00 00 00 00 00 0b 00 00 00 38 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 01 00 00 00 07 00 00 00 00 00 00 00 00 00 0a 00 00 00 00 00 00 00 02 00 04 00 01 86 9f 00 00 68 8c
0d 4c 01 fe 00 00 00 00 00 00 00 14 00 45 00 00 00 00 00 0b 00 00 00 38 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 07 00 00 00 00 00 00 00 00 00 0a 00 00 00 00 00 00 00 02 00 04 00 01 86 9f 00 00 68 8d
0d 4c 01 fe 00 00 00 00 00 00 00 15 00 46 00 00 00 00 00 0b 00 00 00 38 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 07 00 00 00 00 00 00 00 00 00 0a 00 00 00 00 00 00 00 02 00 04 00 01 86 9f 00 00 68 8d
0d 4c 01 fe 00 00 00 00 00 00 00 15 00 46 00 00 00 00 00 0b 00 00 00 38 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 07 00 00 00 00 00 00 00 00 00 0a 00 00 00 00 00 00 00 02 00 04 00 01 86 9f 00 00 68 8d
0d 4c 01 fc 00 00 00 00 00 00 00 15 00 46 00 00 00 00 00 0b 00 00 00 38 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 07 00 00 00 00 00 00 00 00 00 0a 00 00 00 00 00 00 00 02 00 04 00 01 86 9f 00 00 68 8f

```

Samples 3 and 4 are identical, but were captured at different times.  Samples 1 and 2 have two bytes different (44 -> 45 earlier and 01 -> 00 later) which should have an identical result if it were a simple sum, but result in 688c -> 688d.  Samples 2 and 3 have two bytes different (14 -> 15 and 45 -> 46, a cumulative difference of 2), but both result in 688d.  Samples 4 and 5 have one byte different (fe -> fc), but result in 688d -> 688f.

All of these suggest some sort of "add if even or subtract if odd" iteration, but I haven't been able to find a process which results in the expected checksum differences.

## Checksum (UM34C)

The last byte of the packet is a checksum and can be calculated using the following Python snippet:

```
def checksum(pkt):
    positions = [
        1, 3, 7, 9, 15, 17, 19, 23, 31, 39, 41, 45, 49, 53, 55, 57, 59, 63,
        67, 69, 73, 79, 83, 89, 97, 99, 109, 111, 113, 119, 121, 127,
    ]

    csum = 0
    for pos in positions:
        csum = csum ^ pkt[pos]
    return csum

```

Note: The checksum only covers odd bytes of the packet!

## Hardware
### UM24C

Not great pictures, but hopefully they'll be useful.

		- 
			[](./img/UM24C_board_1.jpg)

		- 
			[](./img/UM24C_board_2.jpg)

		- 
			[](./img/UM24C_board_3.jpg)

		- 
			[](./img/UM24C_board_4.jpg)

		- 
			[](./img/UM24C_board_5.jpg)

		- 
			[](./img/UM24C_board_6.jpg)

		- 
			[](./img/UM24C_board_7.jpg)

### UM25C

User perceivable peripherals:

- USB-A male, and USB-B micro female, and USB-C female for "the line" (host / power adapter provides supply to the device under test)
- USB-A female, and USB-C female connect to the device under test
- slide switch to enable Bluetooth communication
- Bluetooth status LED (blinks when enabled and idle, steady when connected)
- four push buttons "in each corner" of the display
- square colour dot matrix display, optionally rotated to any of four orientations in software

Hardware components on the PCB:

- STM8S005 microcontroller
- U4 and U6, SOT23-6 and smaller, unknown chips near the shunt, markings "CAEU" and "AB14"
- R010 shunt
- M5333B voltage regulator
- Bluetooth module on separate PCB, DX-BT18 by DX-SMART, local LED, local regulation with power switch, UART communication to the main board

		- 
			[](./img/Rdtech-um25c-pcb-top.png)

		- 
			[](./img/Rdtech-um25c-pcb-bottom.png)

		- 
			[](./img/Rdtech-um25c-pcb-rf-zoom.png)

## References
- [RDTech AliExpress store](https://rdtech.aliexpress.com/store/923042)
- [rdumtool repo by rfinnie at github](https://github.com/rfinnie/rdumtool) - RDTech UM24C/UM25C/UM34C Bluetooth interface tool (Python 3)

## Photos

<div class="photo-grid" markdown>

[![Um24c Board 3](./img/UM24C_board_3.jpg)](./img/UM24C_board_3.jpg "Um24c Board 3"){ .glightbox data-gallery="rdtech-um-series" }
<span class="caption">Um24c Board 3</span>

[![Um24c Board 6](./img/UM24C_board_6.jpg)](./img/UM24C_board_6.jpg "Um24c Board 6"){ .glightbox data-gallery="rdtech-um-series" }
<span class="caption">Um24c Board 6</span>

[![Um24c Display](./img/UM24C_display.jpg)](./img/UM24C_display.jpg "Um24c Display"){ .glightbox data-gallery="rdtech-um-series" }
<span class="caption">Um24c Display</span>

[![Um24c Board 2](./img/UM24C_board_2.jpg)](./img/UM24C_board_2.jpg "Um24c Board 2"){ .glightbox data-gallery="rdtech-um-series" }
<span class="caption">Um24c Board 2</span>

[![Um24c Board 5](./img/UM24C_board_5.jpg)](./img/UM24C_board_5.jpg "Um24c Board 5"){ .glightbox data-gallery="rdtech-um-series" }
<span class="caption">Um24c Board 5</span>

[![Rdtech Um25c Pcb Rf Zoom](./img/Rdtech-um25c-pcb-rf-zoom.png)](./img/Rdtech-um25c-pcb-rf-zoom.png "Rdtech Um25c Pcb Rf Zoom"){ .glightbox data-gallery="rdtech-um-series" }
<span class="caption">Rdtech Um25c Pcb Rf Zoom</span>

[![Um24c Board 1](./img/UM24C_board_1.jpg)](./img/UM24C_board_1.jpg "Um24c Board 1"){ .glightbox data-gallery="rdtech-um-series" }
<span class="caption">Um24c Board 1</span>

[![Um24c Board 7](./img/UM24C_board_7.jpg)](./img/UM24C_board_7.jpg "Um24c Board 7"){ .glightbox data-gallery="rdtech-um-series" }
<span class="caption">Um24c Board 7</span>

[![Um24c Board 4](./img/UM24C_board_4.jpg)](./img/UM24C_board_4.jpg "Um24c Board 4"){ .glightbox data-gallery="rdtech-um-series" }
<span class="caption">Um24c Board 4</span>

[![Rdtech Um25c Pcb Bottom](./img/Rdtech-um25c-pcb-bottom.png)](./img/Rdtech-um25c-pcb-bottom.png "Rdtech Um25c Pcb Bottom"){ .glightbox data-gallery="rdtech-um-series" }
<span class="caption">Rdtech Um25c Pcb Bottom</span>

[![Rdtech Um25c Pcb Top](./img/Rdtech-um25c-pcb-top.png)](./img/Rdtech-um25c-pcb-top.png "Rdtech Um25c Pcb Top"){ .glightbox data-gallery="rdtech-um-series" }
<span class="caption">Rdtech Um25c Pcb Top</span>

</div>
