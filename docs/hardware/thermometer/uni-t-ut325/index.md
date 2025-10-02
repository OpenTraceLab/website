---
title: UNI-T UT325
---

# UNI-T UT325

<div class="infobox" markdown>

![UNI-T UT325](./img/Uni-t_ut325_top.jpg){ .infobox-image }

### UNI-T UT325

| | |
|---|---|
| **Status** | supported |
| **Source code** | [uni-t-ut32x](https://github.com/OpenTraceLab/OpenTraceCapture/tree/main/src/hardware/uni-t-ut32x) |
| **Measurements** | temperature |
| **Features** | data hold, min/max, backlight |
| **Website** | [uni-trend.com](http://www.uni-trend.com/html/product/Environmental/Environmental_Tester/UT320_Contact_Type/UT325.html) |

</div>

The **UNI-T UT325** is a logging thermometer with two thermocouple inputs and USB connectivity. It supports K,J,T,E,R,S,N thermocouple types.

See [UNI-T UT325/Info](https://sigrok.org/wiki/UNI-T_UT325/Info) for more details (such as **lsusb -v** output) about the device.

The device sends temperature measurements at 6Hz to the host.

## Hardware
- [Texas Instruments MSP430FE427](http://www.msp430.net/msp430fe427.pdf) (MSP430) microcontroller with 32KiB flash.
- ATMEL 16KiB EEPROM, various models.
- [WCH CH9325](https://sigrok.org/wiki/WCH_CH9325) USB interface chip.
- [Holtek HT1621B](http://www.holtek.com/ENGLISH/docum/consumer/1621.htm) LCD driver.

## Photos

<div class="photo-grid" markdown>

[![Uni T Ut325 Top](./img/Uni-t_ut325_top.jpg)](./img/Uni-t_ut325_top.jpg "Uni T Ut325 Top"){ .glightbox data-gallery="uni-t-ut325" }
<span class="caption">Uni T Ut325 Top</span>

[![Uni T Ut325 Front](./img/Uni-t_ut325_front.jpg)](./img/Uni-t_ut325_front.png "Uni T Ut325 Front"){ .glightbox data-gallery="uni-t-ut325" }
<span class="caption">Uni T Ut325 Front</span>

[![Uni T Ut325 Perspective](./img/Uni-t_ut325_perspective.jpg)](./img/Uni-t_ut325_perspective.jpg "Uni T Ut325 Perspective"){ .glightbox data-gallery="uni-t-ut325" }
<span class="caption">Uni T Ut325 Perspective</span>

[![Uni T Ut325 Back Battery](./img/Uni-t_ut325_back_battery.jpg)](./img/Uni-t_ut325_back_battery.jpg "Uni T Ut325 Back Battery"){ .glightbox data-gallery="uni-t-ut325" }
<span class="caption">Uni T Ut325 Back Battery</span>

[![Uni T Ut325 Fpanel Back](./img/Uni-t_ut325_fpanel_back.jpg)](./img/Uni-t_ut325_fpanel_back.jpg "Uni T Ut325 Fpanel Back"){ .glightbox data-gallery="uni-t-ut325" }
<span class="caption">Uni T Ut325 Fpanel Back</span>

[![Uni T Ut325 Usb Cable Connector](./img/UNI-T_UT325_USB_cable_connector.jpg)](./img/UNI-T_UT325_USB_cable_connector.png "Uni T Ut325 Usb Cable Connector"){ .glightbox data-gallery="uni-t-ut325" }
<span class="caption">Uni T Ut325 Usb Cable Connector</span>

[![Uni T Ut325 Back Wo Bail](./img/Uni-t_ut325_back_wo_bail.jpg)](./img/Uni-t_ut325_back_wo_bail.jpg "Uni T Ut325 Back Wo Bail"){ .glightbox data-gallery="uni-t-ut325" }
<span class="caption">Uni T Ut325 Back Wo Bail</span>

[![Uni T Ut325 Lcd](./img/UNI-T_UT325_LCD.jpg)](./img/UNI-T_UT325_LCD.png "Uni T Ut325 Lcd"){ .glightbox data-gallery="uni-t-ut325" }
<span class="caption">Uni T Ut325 Lcd</span>

[![Uni T Ut325 Pcb Front W Display](./img/Uni-t_ut325_pcb_front_w_display.jpg)](./img/Uni-t_ut325_pcb_front_w_display.jpg "Uni T Ut325 Pcb Front W Display"){ .glightbox data-gallery="uni-t-ut325" }
<span class="caption">Uni T Ut325 Pcb Front W Display</span>

[![Uni T Ut325 Packaging](./img/Uni-t_ut325_packaging.jpg)](./img/Uni-t_ut325_packaging.jpg "Uni T Ut325 Packaging"){ .glightbox data-gallery="uni-t-ut325" }
<span class="caption">Uni T Ut325 Packaging</span>

[![Uni T Ut325 Front](./img/Uni-t_ut325_front.jpg)](./img/Uni-t_ut325_front.jpg "Uni T Ut325 Front"){ .glightbox data-gallery="uni-t-ut325" }
<span class="caption">Uni T Ut325 Front</span>

[![Uni T Ut325 Case Open](./img/Uni-t_ut325_case_open.jpg)](./img/Uni-t_ut325_case_open.jpg "Uni T Ut325 Case Open"){ .glightbox data-gallery="uni-t-ut325" }
<span class="caption">Uni T Ut325 Case Open</span>

[![Uni T Ut325 Pcb Front](./img/Uni-t_ut325_pcb_front.jpg)](./img/Uni-t_ut325_pcb_front.jpg "Uni T Ut325 Pcb Front"){ .glightbox data-gallery="uni-t-ut325" }
<span class="caption">Uni T Ut325 Pcb Front</span>

[![Uni T Ut325 Pcb Bottom](./img/Uni-t_ut325_pcb_bottom.jpg)](./img/Uni-t_ut325_pcb_bottom.jpg "Uni T Ut325 Pcb Bottom"){ .glightbox data-gallery="uni-t-ut325" }
<span class="caption">Uni T Ut325 Pcb Bottom</span>

</div>
## Protocol

The device communicates with the host via a [WCH CH9325](https://sigrok.org/wiki/WCH_CH9325) USB interface chip. See the [protocol](https://sigrok.org/wiki/WCH_CH9325#Protocol) section of that page to extract the protocol as described here.

#### Commands
| Byte | Description |
|---|---|
| 0x01 | Start sending realtime data |
| 0x02 | Stop sending data |
| 0x03 | Set device to "debug" mode (calibration mode) |
| 0x04 | When sent twice in succession, clears all stored memory |
| 0x07 | Start sending stored data |

#### Received data

Temperature is encoded as ASCII digits. The number represents the temperature * 10. A negative sign is represented by 0x3b (ASCII semicolon). Unused digits are represented by 0x3a (ASCII colon), and should be ignored. A completely invalid measurement is represented as four times 0x3b (ASCII semicolon). This happens when no probe is connected.

The data comes out of the USB HID encoding in packets of 19 bytes each:

| Byte | Description |
|---|---|
| 0 | ASCII digit: 0=measurement from memory, 2=realtime measurement, 6=*unknown* |
| 1-4 | Temperature. |
| 5 | ASCII digit 1-3, representing the measurement unit: Celcius, Fahrenheit or Kelvin  respectively, or 0 when unknown (in recall mode; unit is not stored.) |
| 6-7 | Number of stored reading in recall mode, as ASCII digits 00-99. Always 00 in realtime mode. |
| 8 | *Unknown, always ASCII digit 0* |
| 9-10 | Hour, as ASCII digits. |
| 11-12 | Minutes, as ASCII digits. |
| 13 | Selected probe, as ASCII digits 0-3: 0=T1, 1=T2, 2=T1-T2 (T1 on main display, 3=T1-T2 (T2 on main display). |
| 14-15 | *unknown* |
| 16 | *Unknown, always ASCII digit 1* |
| 17-18 | Always `0x0d 0x0a` (CRLF), denoting end of packet. |

## Driver status

The device does not send the status of the Hold button, or of the Max/Min/Avg setting, thus these are not reported back to a frontend.

Although the meter features dual display, the serial packet only communicates the content of the main display. This display reflects the user's choice (T1, T2, or T1-T2, selected by means of pressing buttons), but the remote (i.e the PC side driver) cannot pick which value to display.

## Resources
- [Jumper One: UNI-T UT325 Thermometer Review](http://jumperone.com/2011/11/ut325-thermometer-review/)
- [Jumper One: Uni-T UT325 Thermometer tear down](http://jumperone.com/2011/11/ut325-thermometer-teardown/)

