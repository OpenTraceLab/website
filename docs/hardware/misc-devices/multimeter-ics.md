# Multimeter Ics
This page lists some information about ICs commonly used in various multimeters (DMMs).
## Contents
\- *1 Overview* \- *2 Cyrustek ES51978* \- *2.1 Resources* \- *3 Cyrustek ES51922* \- *3.1 Resources* \- *4 Dream Tech International DTM0660* \- *4.1 Protocol* \- *4.2 Resources* \- *5 Fortune Semiconductor FS9721_LP3* \- *5.1 Protocol* \- *6 Fortune Semiconductor FS9721B* \- *7 Fortune Semiconductor FS9922-DMM3* \- *8 Fortune Semiconductor FS9922-DMM4* \- *8.1 Protocol* \- *9 Metex 14-byte ASCII* \- *9.1 Protocol* \- *9.1.1 Packet structure* \- *9.1.1.1 Example packets* \- *9.2 Alternative Protocol* \- *9.2.1 Packets* \- *9.2.2 Commands* \- *10 WENS98A / Voltcraft GDM 704* \- *10.1 Protocol* \- *10.2 Resources*
# Overview Many multimeters use a special-purpose multimeter IC internally. This table lists those chips, as they're often directly responsible for the protocol and data format of the PC logging functionality of a multimeter.  Vendor | Device | Builtin PC interface | Comments
---|---|---|---
[Cyrustek](http://www.cyrustek.com.tw) | [ES51978](http://www.cyrustek.com.tw/spec/ES51978.pdf) | RS232, TX only, 2400 baud, 7o1 | Data is sent via the **SDO** pin. Data logging can be en/disabled via **RS232** pin.
[Cyrustek](http://www.cyrustek.com.tw) | [ES51922](http://www.cyrustek.com.tw/spec/ES51922.pdf) | RS232, TX only, 19230 baud, 7o1 | Data is sent via the **SDO** pin. Data logging can be en/disabled via **RS232** pin. Some 3rd-party parsing utilities are listed *below*.
*Dream Tech International Ltd* | *DTM0660* | RS232, TX only, 2400 baud, 8n1 | Some people think this chip is a copy of the *HY12P65*. Protocol looks closely to the FS9721_LP3.
[Fortune Semiconductor](http://www.ic-fortune.com/eng/new_product3_3.asp) | [FS9721_LP3](http://www.ic-fortune.com/upload/Download/FS9721_LP3-DS-20_EN.pdf) | RS232, TX only, 2400 baud, 8n1 | Data is sent via the **TXD** pin. Data logging can be en/disabled via **ENTX** pin.
[Fortune Semiconductor](http://www.ic-fortune.com/eng/new_product3_3.asp) | [FS9922_DMM4](http://www.ic-fortune.com/upload/Download/FS9922-DMM4-DS-11_EN.pdf) | RS232, TX only, 2400 baud, 8n1 (?) | Data is sent via the **TXD** pin. Data logging can be en/disabled via **TXEN** pin (?) and the **REL/RS232** pin (?).
Hung Change Co Ltd | HCPD608 | RS232, TX/RX, 9600 baud, 7n1 | Used in Protek 608, Voltcraft VC608
Intersil | ICL7106 | ? |
Intersil | ICL7136 | ? |
Intersil | ICL7139/ICL7149 | none (?) |
MASTECH | M343-01 | ? |
Maxim | MAX130/131 | ? |
Maxim | MAX133/134 | ? |
Metex | KS57C2016 | ? | Possibly a relabel'd Samsung KS57C2016 4-bit microcontroller.
[New Japan Radio](http://semicon.njr.co.jp/eng/) | [NJU9207](http://www.datasheetcatalog.com/datasheets_pdf/N/J/U/9/NJU9207.shtml) | none |
WENS | WENS98A | RS232, TX only, 9600 baud, 8n1 | used in Conrad Electronic / Voltcraft GDM 704
# Cyrustek ES51978 The [Cyrustek](http://www.cyrustek.com.tw) ES51978 is an all-in-one multimeter chip. The data protocol is well described in the datasheet. It is used in many multimeters, e.g. the *ISO-TECH IDM103N* or the ISO-TECH IDM 98II. See *Multimeter ICs/Cyrustek ES519xx* for a detailed comparison of the Cyrustek ES519xx IC series protocols. ## Resources \- [Datasheet](http://www.cyrustek.com.tw/spec/ES51978.pdf) \- *'Unlocking' multimeter RS232 output* (info on hooking up a Cyrustek based multimeter to a computer) # Cyrustek ES51922 The [Cyrustek](http://www.cyrustek.com.tw) ES51922 is an all-in-one multimeter chip. The data protocol is mostly described in the datasheet. It is used in many multimeters, e.g. the *UNI-T UT61E* or the [Wintex TD2200](http://shaddack.twibright.com/projects/reveng_TD2200/). See *Multimeter ICs/Cyrustek ES519xx* for a detailed comparison of the Cyrustek ES519xx IC series protocols. ## Resources \- [Datasheet](http://www.cyrustek.com.tw/spec/ES51922.pdf) \- [Multimeter data parsing utility](https://bitbucket.org/kuzavas/dmm_es51922) complete implementation written in Python \- [diyftw.de: Uni-Trend UT61E (UT-D04 linux treiber)](http://diyftw.de/wiki/doku.php?id=projekte:ut61e) (device info, Linux software using HIDAPI: [ut61e-linux-sw-0.02.tar.gz](http://diyftw.de/wiki/lib/exe/fetch.php?media=projekte:ut61e-linux-sw-0.02.tar.gz)) \- [Steffen Vogel: UNI-TREND UT61E Digital Multimeter](http://www.steffenvogel.de/2009/11/29/uni-trend-ut61e-digital-multimeter/) (device info, Linux software for serial port: [dmmut61e-0.01.tar.gz](http://static.steffenvogel.de/wp-content/uploads/2009/11/dmmut61e-0.01.tar.gz)) # Dream Tech International DTM0660 Very little information is available about this chip, even though it was put on the market in 2013. Most of the information found on the web is in Chinese. Searches suggest that some PeakTech, UNI-T, RadioShack, and Velleman DMMs use that chip.
**Image: \1*
[*
DTM0660 in QFP package
## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
