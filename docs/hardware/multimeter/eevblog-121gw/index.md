---
title: EEVBlog 121GW
---

# EEVBlog 121GW

<div class="infobox" markdown>

![EEVBlog 121GW](./img/Eevblog_121gw_mugshot.png){ .infobox-image }

### EEVBlog 121GW

| | |
|---|---|
| **Status** | supported |
| **Source code** | [serial-dmm](https://github.com/OpenTraceLab/OpenTraceCapture/tree/main/src/hardware/serial-dmm) |
| **Counts** | 50000 |
| **IEC 61010-1** | CAT III (600V) |
| **Connectivity** | BLE, SD card |
| **Measurements** | voltage, current, power, resistance, capacitance, diode, continuity, frequency, duty cycle, period, temperature |
| **Features** | autorange, true-rms, auto hold, min/max, 1ms peak, 1kHz lowpass, relative, bargraph, backlight, 3V/15V diode, SD card logging |
| **Website** | [eevblog.com](https://www.eevblog.com/product/121gw/) |

</div>

The **EEVBlog 121GW** is a 50000 counts, CAT III (600V) handheld digital multimeter with SD card (firmware update, data logging) and BLE connectivity.

The EEVBlog host Dave Jones participated in the design of the device which gets manufactured by UEi. Some features are rare, or their combination has not been seen in other devices (15V diode test, builtin uCurrent to reduce burden voltage in current measurement, open schematics and hackable firmware).

Hold the **1ms PEAK** button to enable BLE communication. Either use sigrok on a platform where BLE is supported, or make the BLE communication available on a COM port (e.g. by means of the BLE to UART gateway discussed below).

## Hardware
- **HY3131** DMM
- **AD8436** TRMS
- **ADR3412** Reference
- **MAX4238** Opamp (uCurrent)
- **STM32L152ZDT6** MCU
- **BLE122** BLE module
- **NJU6350R** RTC, CR1220 battery
- Split terminals and opamp for plug detection
- Several **4052/4053** muxes

The Uni-T UT171A and Keysight U1282A meters are said to use the same HY3131 multimeter chipset.

The 121GW meter's schematics is open, as is the source code for the mobile app. 

The meter is announced as having "hackable firmware" but its source code is not available and probably never will. Alternative OpenSource firmware is possible but would have to start at square one. There are connector pads to program the MCU and the BLE module.

The STM32 MCU communicates to the HY3131 chip via SPI, and to the BLE112 module via UART. The BLE112 passes the MCU's serial data in verbatim form (cable replacement mode). Which means that one might as well grab the meter's serial output at the MCU to BLE connection.

## Photos

<div class="photo-grid" markdown>

[![Eevblog 121gw Mugshot](./img/Eevblog_121gw_mugshot.png)](./img/Eevblog_121gw_mugshot.png "Eevblog 121gw Mugshot"){ .glightbox data-gallery="eevblog-121gw" }
<span class="caption">Eevblog 121gw Mugshot</span>

[![Eev121gw Back Text](./img/Eev121gw-back-text.png)](./img/Eev121gw-back-text.png "Eev121gw Back Text"){ .glightbox data-gallery="eevblog-121gw" }
<span class="caption">Eev121gw Back Text</span>

[![Eev121gw Display Volt Xmpl](./img/Eev121gw-display-volt-xmpl.png)](./img/Eev121gw-display-volt-xmpl.png "Eev121gw Display Volt Xmpl"){ .glightbox data-gallery="eevblog-121gw" }
<span class="caption">Eev121gw Display Volt Xmpl</span>

[![Eev121gw Batt Fuse Sd](./img/Eev121gw-batt-fuse-sd.png)](./img/Eev121gw-batt-fuse-sd.png "Eev121gw Batt Fuse Sd"){ .glightbox data-gallery="eevblog-121gw" }
<span class="caption">Eev121gw Batt Fuse Sd</span>

[![Eev121gw Display Most Segments](./img/Eev121gw-display-most-segments.png)](./img/Eev121gw-display-most-segments.png "Eev121gw Display Most Segments"){ .glightbox data-gallery="eevblog-121gw" }
<span class="caption">Eev121gw Display Most Segments</span>

[![Eev121gw Pcb All](./img/Eev121gw-pcb-all.png)](./img/Eev121gw-pcb-all.png "Eev121gw Pcb All"){ .glightbox data-gallery="eevblog-121gw" }
<span class="caption">Eev121gw Pcb All</span>

[![Eev121gw Front Sleeve](./img/Eev121gw-front-sleeve.png)](./img/Eev121gw-front-sleeve.png "Eev121gw Front Sleeve"){ .glightbox data-gallery="eevblog-121gw" }
<span class="caption">Eev121gw Front Sleeve</span>

</div>
## Protocol
### SD

SD card logging generates CSV style files, with several header lines (non-comments) describing the test setup and start of recording, followed by data lines, and a final (non-comment) line when recording stops.

Example SD card logfile:

```
 START,2016/10/04,03:15:27,
 ID,170800000,
 INTERVAL,000,sec,
 ,MAIN,,,SUB-1,,,SUB-2,,,Remark,
 No. ,Func. ,Value,Unit,Func. ,Value,Unit,Func. ,Value,Unit,
 1,DCV,00.0003,V,,,,,,,,
 2,DCV,-00.0009,V,,,,,,,,
 3,DCV,-00.0106,V,,,,,,,,
 4,DCV,-00.0005,V,,,,,,,,
 --- 8< --- snip snip --- >8 ---
 890,DCV,-00.0002,V,,,,,,,,
 891,DCV,00.0004,V,,,,,,,,
 MAX,865,DCV,00.0752,V,
 MIN,537,DCV,-00.0558,V,

```
### BLE

Several firmware versions implemented different protocol versions, as lessons were learned during development of the BLE communication and apps for mobile devices. Recent versions use packets of 19 bytes each with binary data, to reduce the probability of data loss in the communication, and to slightly increase throughput since BLE is considered "low speed". The "Revised-Packet-Format-Blob-V2" PDF outlines the frame layout.

BLE communication is reported to be slow (some two samples per second), and occassionally flaky (truncated packets, reduced rate including gaps of non-activity, increasing error counts after longer periods of logging). The firmware and the protocol provide basic functionality, but may see some more development before becoming full featured and stable, or before more performance increases are seen.

To enable BLE communication **hold** the **1ms PEAK** button until the **BT** indicator changes. The BLE module is used in cable extender mode, transparently passing the UART data of the meter's STM32 controller. The BLE module needs to receive a CCCD trigger before it starts sending UART data as BLE notifications. The libsigrok library's serial layer transparently supports the BLE module used in this DMM (on some of the sigrok supported platforms, others can use the BLE to UART gateway, see below). This trigger is not needed for each sample (like some serial DMMs do), but it'd be required to re-establish communication after the connection was lost (when the meter went to sleep, or BT comm was disabled, or the device went out of the receiver's range).

Each 19-byte packet communicates data for three displays ("main", "sub", and "bar", i.e. the two displays and the bargraph) as well as some "icon" state (indicators).

Quick experiment, manual inspection of BLE communication:

```
 $ **hcitool lescan**
 LE Scan ...
 88:6B:12:34:56:78 (unknown)
 88:6B:12:34:56:78 121GW
 $ **gatttool -b DEV_ADDR --char-write-req -a 9 -n 0300 --listen**
 Characteristic value was written successfully
 Indication   handle = 0x0008 value: f2 17 80 01 21 01 40 00 15 64 01 00 f0 00 00 0e 40 00 ca f2 
 Indication   handle = 0x0008 value: 17 80 01 21 01 40 00 01 64 01 00 f0 00 00 0e 40 00 de f2 17 
 Indication   handle = 0x0008 value: 80 01 21 01 00 00 1f 64 01 00 ef 00 00 0e 40 00 9f f2 17 80 
 Indication   handle = 0x0008 value: 01 21 01 40 9c f2 17 80 01 21 01 40 00 1d 64 01 00 f0 00 00 
 Indication   handle = 0x0008 value: 0e 40 00 c2 
 Indication   handle = 0x0008 value: f2 
 Indication   handle = 0x0008 value: 17 80 01 21 01 00 00 0f 64 01 00 f0 04 00 0e 40 00 94 
 Indication   handle = 0x0008 value: f2 
 Indication   handle = 0x0008 value: 17 80 01 21 01 40 00 1b 64 01 00 f0 00 00 0e 40 00 c4 
 Indication   handle = 0x0008 value: f2 
 Indication   handle = 0x0008 value: 17 80 01 21 01 00 00 73 64 01 00 f0 00 00 0e 40 00 ec

```

Native BLE communication on a platform which supports it:

```
 $ **sigrok-cli -d eevblog-121gw:conn=bt/ble122/88-6B-12-34-56-78 --scan**
 The following devices were found:
 eevblog-121gw - EEVblog 121GW with 3 channels: main sub bar

```

Python based [BLE to UART gateway](https://sigrok.org/gitweb/?p=sigrok-util.git;a=tree;f=util/eevblog-121gw), using the bluepy Python module:
Users are reported to run BLE to UART gateways on ESP or nRF hardware, as well as on RPi or PC machines.

```
 (needs permissions to scan for and communicate to the device)
 # **pip install pyserial bluepy**
 # **./eev121gw-ble-uart-relay -p /dev/ttyUSB1 -v**

```

Using the UART attached 121GW multimeter:

```
 $ **sigrok-cli -d eevblog-121gw:conn=/dev/ttyUSB0 --scan**
 The following devices were found:
 eevblog-121gw - EEVblog 121GW with 3 channels: main sub bar

```
```
 $ **sigrok-cli -d eevblog-121gw:conn=/dev/ttyUSB0 --continuous**
 main: 2.1074 V DC AUTO
 sub: 26.9 °C
 bar: 1.8
 main: 1.9905 V DC AUTO
 sub: 26.9 °C
 bar: 1.8 
 main: 1.8712 V DC AUTO
 sub: 26.9 °C
 bar: 1.6 
 main: 1.7528 V DC AUTO
 sub: 26.9 °C
 bar: 1.4 
 main: 1.6335 V DC AUTO
 sub: 26.9 °C
 bar: 1.4 
 main: 1.5142 V DC AUTO
 sub: 27.0 °C
 bar: 1.2 
 ...

```
```
 $ **./sigrok-meter -d eevblog-121gw:conn=/dev/ttyUSB0 &**

```
## Resources
- [Vendor product page](https://www.eevblog.com/product/121gw/) (download links for firmware, user manual, schematics, mobile apps, packet format, as well as an issue report form)
- [Welectron](https://www.welectron.com/EEVBlog-121GW-Data-Logging-Multimeter-mit-Bluetooth) (European distributor)
- [Mobile app repo](https://gitlab.com/Sepps/app-121gw/) (maintained by Dave2)
- Dozens of forum threads with hundreds of pages on the [EEVBlog site](https://www.eevblog.com/forum)
- [lygte-info.dk Review and teardown](https://lygte-info.dk/review/DMMEEVBlog%20121GW%20UK.html)

