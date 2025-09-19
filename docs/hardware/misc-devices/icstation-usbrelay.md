# Icstation Usbrelay
| | | |:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------------------------------------:| | [*Image: \1* | | | Status | supported | | Source code | [icstation-usbrelay](http://github.com/OpenTraceLab/?p=OpenTraceCapture.git;a=tree;f=src/hardware/icstation-usbrelay) | | Channels | 2, 4 or 8 | | Ratings | 10A @ 250VAC/30VDC, 12A @ 125VAC/28VDC | | Connectivity | USB/Serial | **ICStation USBRelay** The **ICStation USBRelay** is a USB relay card with up to 8 relays. Models with 2 (ICSE013A), 4 (ICSE012A) and 8 (ICSE014A) relays exist. See *Info* for USB details. **WARNING:** When reconnecting to the device (e.g. with OpenTraceCLI or SmuView) the connect will fail and the "query device"-command (0x50) will be interpreted as a bit mask and will turn on relays 1-4, 6 and 8. You have to power cycle the device to be able to reconnect!
## Contents
\- *1 Photos* \- *2 Hardware* \- *3 Protocol* \- *4 Example use* \- *5 Resources*
## Photos \-
[*Image: \1*
ICStation ICSE012A top
\-
[*Image: \1*
ICStation ICSE012A back
## Hardware \- **STM 8S003F3P6 microcontroller**: [datasheet](https://www.st.com/resource/en/datasheet/stm8s003f3.pdf) \- **Prolific PL-2303HX USB to UART Bridge**: [datasheet](http://www.prolific.com.tw/UserFiles/files/ds_pl2303HXD_v1_4_4.pdf) \- **ULN2803AG relay driver**: [datasheet](https://www.ti.com/lit/gpn/uln2803a) ## Protocol The relay boards have a very simple and limited protocol. **Note:** Once the device is connected and has entered the command mode (0x51), every following byte will be interpreted as a bit mask for switching relays. There is no way to leave the command mode!  Byte | Command
---|---
**0x50** | **Query the device model.** Response: | **0xAB** | ICSE012A | 4 relay version
---|---|---
**0xAD** | ICSE013A | 2 relay version
**0xAC** | ICSE014A | 8 relay version
**0x51** _0xnn 0xnn ..._ | **Start command mode.** Every following byte will be interpreted as a bit mask for switching the relays. **0** will turn a relay on, **1** will turn a relay off. **Note:** You cannot leave the command mode! Examples for switching mask bytes (ICSE014A, 8 relays): | **0b00000001** | Turn off relay #1 and turn on relays #2 - #8
---|---
**0b00000000** | Turn on all relays (#1 - #8)
**0b10101010** | Turn off relay #1, #3, #5, #7 and turn on relays #2, #4, #6, #8
## Example use Detect the device and display its properties.  $ OpenTraceCLI -d icstation-usbrelay:conn=/dev/ttyUSB0 --show Driver functions: Multiplexer Scan options: conn serialcomm icstation-usbrelay - ICStation ICSE012A Channel groups: R1: channel R2: channel R3: channel R4: channel Supported configuration options across all channel groups: enabled: on, off  Manipulate the state of relays.  $ OpenTraceCLI -d icstation-usbrelay:conn=/dev/ttyUSB0 --config channel_group=R1:enabled=off --config channel_group=R2:enabled=on --set  ## Resources \- [Drivers and protocol description (ZIP)](http://www.icstation.com/product_document/Download/4012.zip) \- [Hacking the ICStation ICSE014A](https://www.youtube.com/watch?v=3G1V5uejnJg)
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=ICStation_USBRelay&oldid=16411](https://OpenTraceLab.org/w/index.php?title=ICStation_USBRelay&oldid=16411)"
: \- *Device* \- *Multiplexer* \- *Supported*
## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
