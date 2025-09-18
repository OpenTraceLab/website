# Uni T Ut325

| | | |:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------:| | [![\1](../../assets/hardware/general/\2)](./File:Uni-t_ut325_front.png.html) | | | Status | supported | | Source code | [uni-t-ut32x](http://github.com/OpenTraceLab/?p=OpenTraceCapture.git;a=tree;f=src/hardware/uni-t-ut32x) | | Measurements | temperature | | Features | data hold, min/max, backlight | | Website | [uni-trend.com](http://www.uni-trend.com/html/product/Environmental/Environmental_Tester/UT320_Contact_Type/UT325.html) | **UNI-T UT325** The **UNI-T UT325** is a logging thermometer with two thermocouple inputs and USB connectivity. It supports K,J,T,E,R,S,N thermocouple types. See [UNI-T UT325/Info](UNI-T_UT325/Info.html "UNI-T UT325/Info") for more details (such as **lsusb -v** output) about the device. The device sends temperature measurements at 6Hz to the host. 
## Contents 
\- [1 Hardware](UNI-T_UT325.html#Hardware) \- [2 Photos](UNI-T_UT325.html#Photos) \- [3 Protocol](UNI-T_UT325.html#Protocol) \- [3.1 Commands](UNI-T_UT325.html#Commands) \- [3.2 Received data](UNI-T_UT325.html#Received_data) \- [4 Driver status](UNI-T_UT325.html#Driver_status) \- [5 Resources](UNI-T_UT325.html#Resources) 
## Hardware \- [Texas Instruments MSP430FE427](http://www.msp430.net/msp430fe427.pdf) (MSP430) microcontroller with 32KiB flash. \- ATMEL 16KiB EEPROM, various models. \- [WCH CH9325](WCH_CH9325.html "WCH CH9325") USB interface chip. \- [Holtek HT1621B](http://www.holtek.com/ENGLISH/docum/consumer/1621.htm) LCD driver. ## Photos \- 
[![\1](../../assets/hardware/general/\2)](./File:Uni-t_ut325_packaging.jpg.html)
Packaging
\- 
[![\1](../../assets/hardware/general/\2)](./File:Uni-t_ut325_perspective.jpg.html)
Device, side
\- 
[![\1](../../assets/hardware/general/\2)](./File:Uni-t_ut325_front.jpg.html)
Device, front
\- 
[![\1](../../assets/hardware/general/\2)](./File:Uni-t_ut325_top.jpg.html)
Device, top
\- 
[![\1](../../assets/hardware/general/\2)](./File:Uni-t_ut325_back_wo_bail.jpg.html)
Device, back
\- 
[![\1](../../assets/hardware/general/\2)](./File:Uni-t_ut325_back_battery.jpg.html)
Device, battery
\- 
[![\1](../../assets/hardware/general/\2)](./File:Uni-t_ut325_case_open.jpg.html)
Device, open
\- 
[![\1](../../assets/hardware/general/\2)](./File:Uni-t_ut325_fpanel_back.jpg.html)
Front panel, back
\- 
[![\1](../../assets/hardware/general/\2)](./File:Uni-t_ut325_pcb_bottom.jpg.html)
PCB, bottom
\- 
[![\1](../../assets/hardware/general/\2)](./File:Uni-t_ut325_pcb_front_w_display.jpg.html)
PCB, top, display
\- 
[![\1](../../assets/hardware/general/\2)](./File:Uni-t_ut325_pcb_front.jpg.html)
PCB, top
\- 
[![\1](../../assets/hardware/general/\2)](./File:UNI-T_UT325_LCD.png.html)
LCD
\- 
[![\1](../../assets/hardware/general/\2)](./File:UNI-T_UT325_USB_cable_connector.png.html)
USB connector
## Protocol The device communicates with the host via a [WCH CH9325](WCH_CH9325.html "WCH CH9325") USB interface chip. See the [protocol](WCH_CH9325.html#Protocol "WCH CH9325") section of that page to extract the protocol as described here. #### Commands | | | |------|---------------------------------------------------------| | Byte | Description | | 0x01 | Start sending realtime data | | 0x02 | Stop sending data | | 0x03 | Set device to "debug" mode (calibration mode) | | 0x04 | When sent twice in succession, clears all stored memory | | 0x07 | Start sending stored data | #### Received data Temperature is encoded as ASCII digits. The number represents the temperature \\* 10. A negative sign is represented by 0x3b (ASCII semicolon). Unused digits are represented by 0x3a (ASCII colon), and should be ignored. A completely invalid measurement is represented as four times 0x3b (ASCII semicolon). This happens when no probe is connected. The data comes out of the USB HID encoding in packets of 19 bytes each: | | | |-------|---------------------------------------------------------------------------------------------------------------------------------------------------------| | Byte | Description | | 0 | ASCII digit: 0=measurement from memory, 2=realtime measurement, 6=*unknown* | | 1-4 | Temperature. | | 5 | ASCII digit 1-3, representing the measurement unit: Celcius, Fahrenheit or Kelvin respectively, or 0 when unknown (in recall mode; unit is not stored.) | | 6-7 | Number of stored reading in recall mode, as ASCII digits 00-99. Always 00 in realtime mode. | | 8 | *Unknown, always ASCII digit 0* | | 9-10 | Hour, as ASCII digits. | | 11-12 | Minutes, as ASCII digits. | | 13 | Selected probe, as ASCII digits 0-3: 0=T1, 1=T2, 2=T1-T2 (T1 on main display, 3=T1-T2 (T2 on main display). | | 14-15 | *unknown* | | 16 | *Unknown, always ASCII digit 1* | | 17-18 | Always `0x0d 0x0a` (CRLF), denoting end of packet. | ## Driver status The device does not send the status of the Hold button, or of the Max/Min/Avg setting, thus these are not reported back to a frontend. Although the meter features dual display, the serial packet only communicates the content of the main display. This display reflects the user's choice (T1, T2, or T1-T2, selected by means of pressing buttons), but the remote (i.e the PC side driver) cannot pick which value to display. ## Resources \- [Jumper One: UNI-T UT325 Thermometer Review](http://jumperone.com/2011/11/ut325-thermometer-review/) \- [Jumper One: Uni-T UT325 Thermometer tear down](http://jumperone.com/2011/11/ut325-thermometer-teardown/)
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=UNI-T_UT325&oldid=14304](https://OpenTraceLab.org/w/index.php?title=UNI-T_UT325&oldid=14304)" 
[Categories](specialcategories-specialcategories.md): \- [Device](./Category:Device.html "Category:Device") \- [Thermometer](./Category:Thermometer.html "Category:Thermometer") \- [Supported](./Category:Supported.html "Category:Supported")

## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
