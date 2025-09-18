# Mastech Mas345

| | | |:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------:| | [![\1](../../assets/hardware/general/\2)](./File:Mastech_mas345_device_front.png.html) | | | Status | supported | | Source code | [serial-dmm](http://github.com/OpenTraceLab/?p=OpenTraceCapture.git;a=tree;f=src/hardware/serial-dmm) | | Counts | 4000 | | IEC 61010-1 | CAT II | | Connectivity | [RS232](Device_cables.html#Metex_5-pin_RS232_cable "Device cables") | | Measurements | voltage, current, resistance, capacitance, temperature, hFE, diode, continuity | | Features | autorange, data hold, bargraph, backlight | | Website | [p-mastech.com](http://web.archive.org/web/20080305031323/http://www.p-mastech.com/products/04_dm/mas345.html) | **MASTECH MAS345** The **MASTECH MAS345** is a 4000 counts, CAT II handheld digital multimeter with RS232 connectivity. It is also sold under the names [Circuit Specialists CSI345](http://www.circuitspecialists.com/csi345.html)1, [Global Specialties Pro-70](http://web.archive.org/web/20070224223043/http://www.globalspecialties.com/pro70.html), [McVoice M-345pro](http://www.xlsmess.de/html/mcvoice_-_m-345pro.html), [Sinometer MAS345](http://www.sinometer.com/jpg/MAS345.jpg). and [Velleman DVM345DI](http://www.velleman.eu/products/view/?country=ot&lang=de&id=341708). 1 The [software shipped by Circuit Specialists](http://www.circuitspecialists.com/products/csi345.zip) is MasView 1.1.
## Contents 
\- [1 Hardware](MASTECH_MAS345.html#Hardware) \- [2 Driver](MASTECH_MAS345.html#Driver) \- [3 Photos](MASTECH_MAS345.html#Photos) \- [4 Protocol](MASTECH_MAS345.html#Protocol) \- [5 Resources](MASTECH_MAS345.html#Resources) 
## Hardware **Multimeter**: \- **Main chip**: MASTECH Japan M343-01 F0951D174 (80 pins, 16 + 16 + 24 + 24) \- **14-stage binary counter/oscillator**: [ST 74HC4060](http://www.st.com/internet/analog/product/69763.jsp) ([datasheet](http://www.st.com/internet/com/TECHNICAL_RESOURCES/TECHNICAL_LITERATURE/DATASHEET/CD00000318.pdf)) (marking: "ST 74HC4060 N00U732") \- **Precision perational amplifier**: [Texas Instruments OP07C](http://www.ti.com/product/op07c) ([datasheet](http://www.ti.com/lit/gpn/op07c)) (marking: "12AL9JM 0P07CP") \- **CMOS multifunctional time base circuit**: [Green Sea Technology GC7555AP](http://translate.google.com/translate?sl=zh-CN&tl=en&js=n&prev=_t&hl=de&ie=UTF-8&layout=2&eotf=1&u=http%3A%2F%2Fproduct.ch.gongchang.com%2Fd16189061.html&act=url) ([datasheet](http://www.chinaeds.com/zl/201041695739344804_GC7555AD,GC7555APpdf.pdf), [English translation](https://translate.googleusercontent.com/translate_c?act=url&hl=de&ie=UTF8&prev=_t&rurl=translate.google.com&sl=zh-CN&tl=en&u=http://www.chinaeds.com/d.aspx%3Fid%3D298797&usg=ALkJrhh8MzVMH7GdvsM85Mvt0pR1rHF_-w)) (marking: "GC7555AP AA7057HS") \- This is an NE555 compatible chip, apparently. \- **General-purpose photocoupler**: [Sharp PC817](http://www.sharpsma.com/optoelectronics/isolation-devices/dc-input-photocouplers/PC817X2J000F) ([datasheet](http://www.sharpsma.com/webfm_send/1092)) (marking: "B \> B5 PC817 Sharp") \- "B": model = PC817X2J000F/PC817XF2J00F, "\>": China factory, "B5": date code == May 1991 \- **General-purpose photocoupler**: [Sharp PC817](http://www.sharpsma.com/optoelectronics/isolation-devices/dc-input-photocouplers/PC817X2J000F) ([datasheet](http://www.sharpsma.com/webfm_send/1092)) (marking: "B \> B6 PC817 Sharp") \- "B": model = PC817X2J000F/PC817XF2J00F, "\>": China factory, "B6": date code == June 1991 \- **Crystal**: ca. 32kHz \- **Fuse**: 15A/250V (6x30mm) (for the 10A jack; interestingly the PCB silkscreen says "20A" for that jack) **RS232 cable**: \- See [Device_cables#Metex_5-pin_RS232_cable](Device_cables.html#Metex_5-pin_RS232_cable "Device cables"). ## Driver Uses the driver **mastech-mas345**. You'll generally need the 'conn' driver option to specify the serial device to use. Example: OpenTraceCLI --driver mastech-mas345:conn=/dev/ttyUSB0 --samples 10 ## Photos **Multimeter**: \- 
[![\1](../../assets/hardware/general/\2)](./File:Mastech_mas345_package1.jpg.html)
Outer package
\- 
[![\1](../../assets/hardware/general/\2)](./File:Mastech_mas345_package2.jpg.html)
Package
\- 
[![\1](../../assets/hardware/general/\2)](./File:Mastech_mas345_package3.jpg.html)
Package, open
\- 
[![\1](../../assets/hardware/general/\2)](./File:Mastech_mas345_package_contents.jpg.html)
Package contents
\- 
[![\1](../../assets/hardware/general/\2)](./File:Mastech_mas345_device_front_rubber.jpg.html)
Device, rubber holster
\- 
[![\1](../../assets/hardware/general/\2)](./File:Mastech_mas345_device_front.jpg.html)
Device, front
\- 
[![\1](../../assets/hardware/general/\2)](./File:Mastech_mas345_device_back.jpg.html)
Device, back
\- 
[![\1](../../assets/hardware/general/\2)](./File:Mastech_mas345_probes.jpg.html)
Probes
\- 
[![\1](../../assets/hardware/general/\2)](./File:Mastech_mas345_temperature_sensor.jpg.html)
Temperature probe
\- 
[![\1](../../assets/hardware/general/\2)](./File:Mastech_mas345_lcd1.jpg.html)
LCD
\- 
[![\1](../../assets/hardware/general/\2)](./File:Mastech_mas345_lcd2.jpg.html)
LCD w/ backlight
\- 
[![\1](../../assets/hardware/general/\2)](./File:Mastech_mas345_device_open.jpg.html)
Device, open
\- 
[![\1](../../assets/hardware/general/\2)](./File:Mastech_mas345_device_plastic.jpg.html)
Front cover
\- 
[![\1](../../assets/hardware/general/\2)](./File:Mastech_mas345_pcb_front1.jpg.html)
PCB, front
\- 
[![\1](../../assets/hardware/general/\2)](./File:Mastech_mas345_pcb_front_displayremoved.jpg.html)
PCB, front, w/o LCD
\- 
[![\1](../../assets/hardware/general/\2)](./File:Mastech_mas345_pcb_front2.jpg.html)
PCB, front top
\- 
[![\1](../../assets/hardware/general/\2)](./File:Mastech_mas345_pcb_front3.jpg.html)
PCB, front middle
\- 
[![\1](../../assets/hardware/general/\2)](./File:Mastech_mas345_pcb_front4.jpg.html)
PCB, front bottom
\- 
[![\1](../../assets/hardware/general/\2)](./File:Mastech_mas345_pcb_bottom1.jpg.html)
PCB, back 1
\- 
[![\1](../../assets/hardware/general/\2)](./File:Mastech_mas345_pcb_bottom2.jpg.html)
PCB, back 2
\- 
[![\1](../../assets/hardware/general/\2)](./File:Mastech_mas345_display1.jpg.html)
LCD 1
\- 
[![\1](../../assets/hardware/general/\2)](./File:Mastech_mas345_display2.jpg.html)
LCD 2
\- 
[![\1](../../assets/hardware/general/\2)](./File:Mastech_mas345_pcb_rs232_connector.jpg.html)
RS232 connector
\- 
[![\1](../../assets/hardware/general/\2)](./File:Mastech_mas345_mastech_m343-01.jpg.html)
MASTECH M343-01
\- 
[![\1](../../assets/hardware/general/\2)](./File:Mastech_mas345_gc7555ap.jpg.html)
GC7555AP
\- 
[![\1](../../assets/hardware/general/\2)](./File:Mastech_mas345_sharp_pc817.jpg.html)
Sharp PC817
\- 
[![\1](../../assets/hardware/general/\2)](./File:Mastech_mas345_st_74hc4060.jpg.html)
ST 74HC4060
\- 
[![\1](../../assets/hardware/general/\2)](./File:Mastech_mas345_texas_instruments_12al9jm.jpg.html)
TI OP07C
**RS232 cable**: See [Device_cables#Metex_5-pin_RS232_cable](Device_cables.html#Metex_5-pin_RS232_cable "Device cables"). ## Protocol The protocol is (partially) documented in the vendor software's "Help" window (seems to apply to MAS343, MAS344, and MAS345; the M9803R protocol is different). See [Multimeter_ICs#Metex_14-byte_ASCII](Multimeter_ICs.html#Metex_14-byte_ASCII "Multimeter ICs") for the DMM IC protocol. ## Resources \- [Original English vendor manual](http://web.archive.org/web/20080305031323/http://www.p-mastech.com/products/04_dm/mas345_hys004695.pdf) (2008) \- [elv.de: Download zu: Digital-Multimeter MAS-345 (68-04 59 88)](http://www.elv.de/controller.aspx?cid=683&detail=10&detail2=211397): \- [German manual from ELV](http://www.elv-downloads.de/service/manuals_hw/45988_MAS345_UM.pdf) (2002) \- ["DMM VIEW" software, version 2.0](http://www.elv-downloads.de/service/manuals_hw/45988_MAS345_Software_V20.zip) (for Win98/NT/ME/2000/XP; supports MAS343, MAS344, MAS345, M9803R) \- [cczwei-forum.de: C# software for reading DMM values](http://www.cczwei-forum.de/cc2/thread.php?threadid=3452) \- [Linux Magazin: E-Werke: Perl misst Stromverbrauch mit Multimeter](http://www.linux-magazin.de/Heft-Abo/Ausgaben/2007/08/E-Werke?category=0) \- [mas-345/marsh: multimeter read and store](https://savannah.nongnu.org/projects/marsh) \- [digitaltrip.hu: Mastech MAS-345 digital multimeter Windows GUI](http://libesz.digitaltrip.hu/mas-345/) ([github](https://github.com/libesz/MAS345_GUI)) \- [github: device-mas345-perl](https://github.com/mschilli/device-mas345-perl) \- [b-redemann.de Auslesen von Messgeräten mit RS232 Interface über USB](http://www.b-redemann.de/sp-DMM-auslesen.shtml) \- [tmon](http://freecode.com/projects/tmon) (uses a MASTECH MAS345) 
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=MASTECH_MAS345&oldid=11384](https://OpenTraceLab.org/w/index.php?title=MASTECH_MAS345&oldid=11384)" 
[Categories](specialcategories-specialcategories.md): \- [Device](./Category:Device.html "Category:Device") \- [Multimeter](./Category:Multimeter.html "Category:Multimeter") \- [Supported](./Category:Supported.html "Category:Supported")

## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
