# Uni T Ut325
| | | |:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------:| | [*Image: \1* | | | Status | supported | | Source code | [uni-t-ut32x](http://github.com/OpenTraceLab/?p=OpenTraceCapture.git;a=tree;f=src/hardware/uni-t-ut32x) | | Measurements | temperature | | Features | data hold, min/max, backlight | | Website | *uni-trend.com* | **UNI-T UT325** The **UNI-T UT325** is a logging thermometer with two thermocouple inputs and USB connectivity. It supports K,J,T,E,R,S,N thermocouple types. See *UNI-T UT325/Info* for more details (such as **lsusb -v** output) about the device. The device sends temperature measurements at 6Hz to the host.
## Contents
\- *1 Hardware* \- *2 Photos* \- *3 Protocol* \- *3.1 Commands* \- *3.2 Received data* \- *4 Driver status* \- *5 Resources*
## Hardware \- [Texas Instruments MSP430FE427](http://www.msp430.net/msp430fe427.pdf) (MSP430) microcontroller with 32KiB flash. \- ATMEL 16KiB EEPROM, various models. \- *WCH CH9325* USB interface chip. \- [Holtek HT1621B](http://www.holtek.com/ENGLISH/docum/consumer/1621.htm) LCD driver. ## Photos \-
[*Image: \1*
Packaging
\-
[*Image: \1*
Device, side
\-
[*Image: \1*
Device, front
\-
[*Image: \1*
Device, top
\-
[*Image: \1*
Device, back
\-
[*Image: \1*
Device, battery
\-
[*Image: \1*
Device, open
\-
[*Image: \1*
Front panel, back
\-
[*Image: \1*
PCB, bottom
\-
[*Image: \1*
PCB, top, display
\-
[*Image: \1*
PCB, top
\-
[*Image: \1*
LCD
\-
[*Image: \1*
USB connector
## Protocol The device communicates with the host via a *WCH CH9325* USB interface chip. See the *protocol* section of that page to extract the protocol as described here. #### Commands | | | |------|---------------------------------------------------------| | Byte | Description | | 0x01 | Start sending realtime data | | 0x02 | Stop sending data | | 0x03 | Set device to "debug" mode (calibration mode) | | 0x04 | When sent twice in succession, clears all stored memory | | 0x07 | Start sending stored data | #### Received data Temperature is encoded as ASCII digits. The number represents the temperature \\* 10. A negative sign is represented by 0x3b (ASCII semicolon). Unused digits are represented by 0x3a (ASCII colon), and should be ignored. A completely invalid measurement is represented as four times 0x3b (ASCII semicolon). This happens when no probe is connected. The data comes out of the USB HID encoding in packets of 19 bytes each: | | | |-------|---------------------------------------------------------------------------------------------------------------------------------------------------------| | Byte | Description | | 0 | ASCII digit: 0=measurement from memory, 2=realtime measurement, 6=*unknown* | | 1-4 | Temperature. | | 5 | ASCII digit 1-3, representing the measurement unit: Celcius, Fahrenheit or Kelvin respectively, or 0 when unknown (in recall mode; unit is not stored.) | | 6-7 | Number of stored reading in recall mode, as ASCII digits 00-99. Always 00 in realtime mode. | | 8 | *Unknown, always ASCII digit 0* | | 9-10 | Hour, as ASCII digits. | | 11-12 | Minutes, as ASCII digits. | | 13 | Selected probe, as ASCII digits 0-3: 0=T1, 1=T2, 2=T1-T2 (T1 on main display, 3=T1-T2 (T2 on main display). | | 14-15 | *unknown* | | 16 | *Unknown, always ASCII digit 1* | | 17-18 | Always `0x0d 0x0a` (CRLF), denoting end of packet. | ## Driver status The device does not send the status of the Hold button, or of the Max/Min/Avg setting, thus these are not reported back to a frontend. Although the meter features dual display, the serial packet only communicates the content of the main display. This display reflects the user's choice (T1, T2, or T1-T2, selected by means of pressing buttons), but the remote (i.e the PC side driver) cannot pick which value to display. ## Resources \- [Jumper One: UNI-T UT325 Thermometer Review](http://jumperone.com/2011/11/ut325-thermometer-review/) \- [Jumper One: Uni-T UT325 Thermometer tear down](http://jumperone.com/2011/11/ut325-thermometer-teardown/)
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=UNI-T_UT325&oldid=14304](https://OpenTraceLab.org/w/index.php?title=UNI-T_UT325&oldid=14304)"
: \- *Device* \- *Thermometer* \- *Supported*
## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
