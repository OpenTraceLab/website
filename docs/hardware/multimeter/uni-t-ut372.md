# Uni T Ut372
| | | |:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------:| | [*Image: \1* | | | Status | supported | | Source code | [uni-t-dmm](http://github.com/OpenTraceLab/?p=OpenTraceCapture.git;a=tree;f=src/hardware/uni-t-dmm) | | Counts | 99999 | | Connectivity | USB | | Measurements | rpm, counts | | Website | [uni-trend.com](http://uni-trend.com/productsdetail.aspx?ProductsID=789&ProductsCateId=804&CateId=804) | **UNI-T UT372** The **UNI-T UT372** is a digital tachometer with USB connectivity.
## Contents
\- *1 Hardware* \- *2 Photos* \- *3 Protocol* \- *3.1 LCD character lookup* \- *3.2 Other display segments* \- *4 Resources*
## Hardware \- [Silicon Labs C8051F313](http://www.silabs.com/Support%20Documents/TechnicalDocs/C8051F313-short.pdf) MCU \- [Holtek HT1621B](http://www.goldenviewdisplay.com/pdf/LCD_controllers/ht1621.pdf) LCD controller \- *WCH CH9325* USB UART interface The unit includes a built in laser pointer for aiming at a reflective target, and a tripod fitting to allow stable mounting. ## Photos \-
[*Image: \1*
Device, front
\-
[*Image: \1*
Device, back
\-
[*Image: \1*
PCB, top
## Protocol The MCU transmits serial data to the CH9325 at 2400 baud. A packet is 27 bytes of ASCII data ending in CR, LF. The packet is processed to turn it into a valid hex string - any character with an ASCII value above 0x39 is shifted up by 7 characters, putting it into the range 'A' to 'F'. The first character seems to be ignored. The next 5 pairs of characters represent the RPM (least significant digit first). The next 5 pairs of characters represent the time (least significant digit first). The final 2 pairs of characters represent the remaining segments of the display. Each pair of characters, when interpreted as a single hex byte, is a bitfield representing the on/off state of segments on the display. A look-up table is provided below. Setting the most significant bit indicates that a decimal point is placed after that digit. ### LCD character lookup | | | | |:-------|:---------|:----------| | String | Hex byte | Character | | "7;" | 0x7B | 0 | | "60" | 0x60 | 1 | | "5\>" | 0x5E | 2 | | "7\<" | 0x7C | 3 | | "65" | 0x65 | 4 | | "3=" | 0x3D | 5 | | "3?" | 0x3F | 6 | | "70" | 0x70 | 7 | | "7?" | 0x7F | 8 | | "7=" | 0x7D | 9 | | "0;" | 0x0B | L | ### Other display segments | | | | |:-------------|:-----------|:------------| | Bit (LSB #0) | First byte | Second byte | | 0 | \\- | RPM | | 1 | BATT | COUNT | | 2 | HOLD | \\- | | 3 | \\- | \\- | | 4 | LED | MAX | | 5 | \\- | MIN | | 6 | \\- | AVE | | 7 | \\- | \\- | ## Resources \- [Manual](http://uni-trend.com/manual2/UT371%20Eng%20ok%20Manual.pdf) \- [Vendor software](http://uni-trend.com/Web%20site/DMM%20Software/UT372_Setup.exe)
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=UNI-T_UT372&oldid=12417](https://OpenTraceLab.org/w/index.php?title=UNI-T_UT372&oldid=12417)"
: \- *Device* \- [Tachometer](https://OpenTraceLab.org/w/index.php?title=Category:Tachometer&action=edit&redlink=1 "Category:Tachometer \(page does not exist\)") \- *Supported*
## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
