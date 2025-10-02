---
title: MASTECH MAS345
---

# MASTECH MAS345

<div class="infobox" markdown>

![MASTECH MAS345](./img/Mastech_mas345_pcb_front4.jpg){ .infobox-image }

### MASTECH MAS345

| | |
|---|---|
| **Status** | supported |
| **Source code** | [serial-dmm](https://github.com/OpenTraceLab/OpenTraceCapture/tree/main/src/hardware/serial-dmm) |
| **Counts** | 4000 |
| **IEC 61010-1** | CAT II |
| **Connectivity** | [RS232](https://sigrok.org/wiki/Device_cables#Metex_5-pin_RS232_cable) |
| **Measurements** | voltage, current, resistance, capacitance, temperature, hFE, diode, continuity |
| **Features** | autorange, data hold, bargraph, backlight |
| **Website** | [p-mastech.com](http://web.archive.org/web/20080305031323/http://www.p-mastech.com/products/04_dm/mas345.html) |

</div>

The **MASTECH MAS345** is a 4000 counts, CAT II handheld digital multimeter with RS232 connectivity.

It is also sold under the names [Circuit Specialists CSI345](http://www.circuitspecialists.com/csi345.html)1, [Global Specialties Pro-70](http://web.archive.org/web/20070224223043/http://www.globalspecialties.com/pro70.html), [McVoice M-345pro](http://www.xlsmess.de/html/mcvoice_-_m-345pro.html), [Sinometer MAS345](http://www.sinometer.com/jpg/MAS345.jpg). and [Velleman DVM345DI](http://www.velleman.eu/products/view/?country=ot&lang=de&id=341708).

1 The [software shipped by Circuit Specialists](http://www.circuitspecialists.com/products/csi345.zip) is MasView 1.1.

## Hardware

**Multimeter**:

- **Main chip**: MASTECH Japan M343-01 F0951D174 (80 pins, 16 + 16 + 24 + 24)
- **14-stage binary counter/oscillator**: [ST 74HC4060](http://www.st.com/internet/analog/product/69763.jsp) ([datasheet](http://www.st.com/internet/com/TECHNICAL_RESOURCES/TECHNICAL_LITERATURE/DATASHEET/CD00000318.pdf)) (marking: "ST 74HC4060 N00U732")
- **Precision perational amplifier**: [Texas Instruments OP07C](http://www.ti.com/product/op07c) ([datasheet](http://www.ti.com/lit/gpn/op07c)) (marking: "12AL9JM 0P07CP")
- **CMOS multifunctional time base circuit**: [Green Sea Technology GC7555AP](http://translate.google.com/translate?sl=zh-CN&tl=en&js=n&prev=_t&hl=de&ie=UTF-8&layout=2&eotf=1&u=http%3A%2F%2Fproduct.ch.gongchang.com%2Fd16189061.html&act=url) ([datasheet](http://www.chinaeds.com/zl/201041695739344804_GC7555AD,GC7555APpdf.pdf), [English translation](https://translate.googleusercontent.com/translate_c?act=url&hl=de&ie=UTF8&prev=_t&rurl=translate.google.com&sl=zh-CN&tl=en&u=http://www.chinaeds.com/d.aspx%3Fid%3D298797&usg=ALkJrhh8MzVMH7GdvsM85Mvt0pR1rHF_-w)) (marking: "GC7555AP AA7057HS")
This is an NE555 compatible chip, apparently.
- **General-purpose photocoupler**: [Sharp PC817](http://www.sharpsma.com/optoelectronics/isolation-devices/dc-input-photocouplers/PC817X2J000F) ([datasheet](http://www.sharpsma.com/webfm_send/1092)) (marking: "B > B5 PC817 Sharp")
"B": model = PC817X2J000F/PC817XF2J00F, ">": China factory, "B5": date code == May 1991
- **General-purpose photocoupler**: [Sharp PC817](http://www.sharpsma.com/optoelectronics/isolation-devices/dc-input-photocouplers/PC817X2J000F) ([datasheet](http://www.sharpsma.com/webfm_send/1092))  (marking: "B > B6 PC817 Sharp")
"B": model = PC817X2J000F/PC817XF2J00F, ">": China factory, "B6": date code == June 1991
- **Crystal**: ca. 32kHz
- **Fuse**: 15A/250V (6x30mm) (for the 10A jack; interestingly the PCB silkscreen says "20A" for that jack)

**RS232 cable**:

- See [Device_cables#Metex_5-pin_RS232_cable](https://sigrok.org/wiki/Device_cables#Metex_5-pin_RS232_cable).

## Driver

Uses the driver **mastech-mas345**.  You'll generally need the 'conn' driver option to specify the serial device to use.

Example:

```
 sigrok-cli --driver mastech-mas345:conn=/dev/ttyUSB0 --samples 10

```

## Photos

<div class="photo-grid" markdown>

[![Mastech Mas345 Pcb Front4](./img/Mastech_mas345_pcb_front4.jpg)](./img/Mastech_mas345_pcb_front4.jpg "Mastech Mas345 Pcb Front4"){ .glightbox data-gallery="mastech-mas345" }
<span class="caption">Mastech Mas345 Pcb Front4</span>

[![Mastech Mas345 Package Contents](./img/Mastech_mas345_package_contents.jpg)](./img/Mastech_mas345_package_contents.jpg "Mastech Mas345 Package Contents"){ .glightbox data-gallery="mastech-mas345" }
<span class="caption">Mastech Mas345 Package Contents</span>

[![Mastech Mas345 Device Back](./img/Mastech_mas345_device_back.jpg)](./img/Mastech_mas345_device_back.jpg "Mastech Mas345 Device Back"){ .glightbox data-gallery="mastech-mas345" }
<span class="caption">Mastech Mas345 Device Back</span>

[![Mastech Mas345 Package2](./img/Mastech_mas345_package2.jpg)](./img/Mastech_mas345_package2.jpg "Mastech Mas345 Package2"){ .glightbox data-gallery="mastech-mas345" }
<span class="caption">Mastech Mas345 Package2</span>

[![Mastech Mas345 Pcb Front3](./img/Mastech_mas345_pcb_front3.jpg)](./img/Mastech_mas345_pcb_front3.jpg "Mastech Mas345 Pcb Front3"){ .glightbox data-gallery="mastech-mas345" }
<span class="caption">Mastech Mas345 Pcb Front3</span>

[![Mastech Mas345 Device Front](./img/Mastech_mas345_device_front.jpg)](./img/Mastech_mas345_device_front.jpg "Mastech Mas345 Device Front"){ .glightbox data-gallery="mastech-mas345" }
<span class="caption">Mastech Mas345 Device Front</span>

[![Mastech Mas345 Temperature Sensor](./img/Mastech_mas345_temperature_sensor.jpg)](./img/Mastech_mas345_temperature_sensor.jpg "Mastech Mas345 Temperature Sensor"){ .glightbox data-gallery="mastech-mas345" }
<span class="caption">Mastech Mas345 Temperature Sensor</span>

[![Mastech Mas345 Texas Instruments 12al9jm](./img/Mastech_mas345_texas_instruments_12al9jm.jpg)](./img/Mastech_mas345_texas_instruments_12al9jm.jpg "Mastech Mas345 Texas Instruments 12al9jm"){ .glightbox data-gallery="mastech-mas345" }
<span class="caption">Mastech Mas345 Texas Instruments 12al9jm</span>

[![Mastech Mas345 Pcb Front2](./img/Mastech_mas345_pcb_front2.jpg)](./img/Mastech_mas345_pcb_front2.jpg "Mastech Mas345 Pcb Front2"){ .glightbox data-gallery="mastech-mas345" }
<span class="caption">Mastech Mas345 Pcb Front2</span>

[![Mastech Mas345 Device Front](./img/Mastech_mas345_device_front.png)](./img/Mastech_mas345_device_front.png "Mastech Mas345 Device Front"){ .glightbox data-gallery="mastech-mas345" }
<span class="caption">Mastech Mas345 Device Front</span>

[![Mastech Mas345 Pcb Bottom2](./img/Mastech_mas345_pcb_bottom2.jpg)](./img/Mastech_mas345_pcb_bottom2.jpg "Mastech Mas345 Pcb Bottom2"){ .glightbox data-gallery="mastech-mas345" }
<span class="caption">Mastech Mas345 Pcb Bottom2</span>

[![Mastech Mas345 Display1](./img/Mastech_mas345_display1.jpg)](./img/Mastech_mas345_display1.jpg "Mastech Mas345 Display1"){ .glightbox data-gallery="mastech-mas345" }
<span class="caption">Mastech Mas345 Display1</span>

[![Mastech Mas345 Device Front Rubber](./img/Mastech_mas345_device_front_rubber.jpg)](./img/Mastech_mas345_device_front_rubber.jpg "Mastech Mas345 Device Front Rubber"){ .glightbox data-gallery="mastech-mas345" }
<span class="caption">Mastech Mas345 Device Front Rubber</span>

[![Mastech Mas345 Package1](./img/Mastech_mas345_package1.jpg)](./img/Mastech_mas345_package1.jpg "Mastech Mas345 Package1"){ .glightbox data-gallery="mastech-mas345" }
<span class="caption">Mastech Mas345 Package1</span>

[![Mastech Mas345 Lcd1](./img/Mastech_mas345_lcd1.jpg)](./img/Mastech_mas345_lcd1.jpg "Mastech Mas345 Lcd1"){ .glightbox data-gallery="mastech-mas345" }
<span class="caption">Mastech Mas345 Lcd1</span>

[![Mastech Mas345 Pcb Front1](./img/Mastech_mas345_pcb_front1.jpg)](./img/Mastech_mas345_pcb_front1.jpg "Mastech Mas345 Pcb Front1"){ .glightbox data-gallery="mastech-mas345" }
<span class="caption">Mastech Mas345 Pcb Front1</span>

[![Mastech Mas345 Package3](./img/Mastech_mas345_package3.jpg)](./img/Mastech_mas345_package3.jpg "Mastech Mas345 Package3"){ .glightbox data-gallery="mastech-mas345" }
<span class="caption">Mastech Mas345 Package3</span>

[![Mastech Mas345 Device Plastic](./img/Mastech_mas345_device_plastic.jpg)](./img/Mastech_mas345_device_plastic.jpg "Mastech Mas345 Device Plastic"){ .glightbox data-gallery="mastech-mas345" }
<span class="caption">Mastech Mas345 Device Plastic</span>

[![Mastech Mas345 Gc7555ap](./img/Mastech_mas345_gc7555ap.jpg)](./img/Mastech_mas345_gc7555ap.jpg "Mastech Mas345 Gc7555ap"){ .glightbox data-gallery="mastech-mas345" }
<span class="caption">Mastech Mas345 Gc7555ap</span>

[![Mastech Mas345 Pcb Front Displayremoved](./img/Mastech_mas345_pcb_front_displayremoved.jpg)](./img/Mastech_mas345_pcb_front_displayremoved.jpg "Mastech Mas345 Pcb Front Displayremoved"){ .glightbox data-gallery="mastech-mas345" }
<span class="caption">Mastech Mas345 Pcb Front Displayremoved</span>

[![Mastech Mas345 Mastech M343 01](./img/Mastech_mas345_mastech_m343-01.jpg)](./img/Mastech_mas345_mastech_m343-01.jpg "Mastech Mas345 Mastech M343 01"){ .glightbox data-gallery="mastech-mas345" }
<span class="caption">Mastech Mas345 Mastech M343 01</span>

[![Mastech Mas345 Pcb Bottom1](./img/Mastech_mas345_pcb_bottom1.jpg)](./img/Mastech_mas345_pcb_bottom1.jpg "Mastech Mas345 Pcb Bottom1"){ .glightbox data-gallery="mastech-mas345" }
<span class="caption">Mastech Mas345 Pcb Bottom1</span>

[![Mastech Mas345 Display2](./img/Mastech_mas345_display2.jpg)](./img/Mastech_mas345_display2.jpg "Mastech Mas345 Display2"){ .glightbox data-gallery="mastech-mas345" }
<span class="caption">Mastech Mas345 Display2</span>

[![Mastech Mas345 Lcd2](./img/Mastech_mas345_lcd2.jpg)](./img/Mastech_mas345_lcd2.jpg "Mastech Mas345 Lcd2"){ .glightbox data-gallery="mastech-mas345" }
<span class="caption">Mastech Mas345 Lcd2</span>

[![Mastech Mas345 Probes](./img/Mastech_mas345_probes.jpg)](./img/Mastech_mas345_probes.jpg "Mastech Mas345 Probes"){ .glightbox data-gallery="mastech-mas345" }
<span class="caption">Mastech Mas345 Probes</span>

[![Mastech Mas345 St 74hc4060](./img/Mastech_mas345_st_74hc4060.jpg)](./img/Mastech_mas345_st_74hc4060.jpg "Mastech Mas345 St 74hc4060"){ .glightbox data-gallery="mastech-mas345" }
<span class="caption">Mastech Mas345 St 74hc4060</span>

[![Mastech Mas345 Sharp Pc817](./img/Mastech_mas345_sharp_pc817.jpg)](./img/Mastech_mas345_sharp_pc817.jpg "Mastech Mas345 Sharp Pc817"){ .glightbox data-gallery="mastech-mas345" }
<span class="caption">Mastech Mas345 Sharp Pc817</span>

[![Mastech Mas345 Device Open](./img/Mastech_mas345_device_open.jpg)](./img/Mastech_mas345_device_open.jpg "Mastech Mas345 Device Open"){ .glightbox data-gallery="mastech-mas345" }
<span class="caption">Mastech Mas345 Device Open</span>

[![Mastech Mas345 Pcb Rs232 Connector](./img/Mastech_mas345_pcb_rs232_connector.jpg)](./img/Mastech_mas345_pcb_rs232_connector.jpg "Mastech Mas345 Pcb Rs232 Connector"){ .glightbox data-gallery="mastech-mas345" }
<span class="caption">Mastech Mas345 Pcb Rs232 Connector</span>

</div>
## Protocol

The protocol is (partially) documented in the vendor software's "Help" window (seems to apply to MAS343, MAS344, and MAS345; the M9803R protocol is different).

See [Multimeter_ICs#Metex_14-byte_ASCII](https://sigrok.org/wiki/Multimeter_ICs#Metex_14-byte_ASCII) for the DMM IC protocol.

## Resources
- [Original English vendor manual](http://web.archive.org/web/20080305031323/http://www.p-mastech.com/products/04_dm/mas345_hys004695.pdf) (2008)
- [elv.de: Download zu: Digital-Multimeter MAS-345  (68-04 59 88)](http://www.elv.de/controller.aspx?cid=683&detail=10&detail2=211397):
[German manual from ELV](http://www.elv-downloads.de/service/manuals_hw/45988_MAS345_UM.pdf) (2002)
- ["DMM VIEW" software, version 2.0](http://www.elv-downloads.de/service/manuals_hw/45988_MAS345_Software_V20.zip) (for Win98/NT/ME/2000/XP; supports MAS343, MAS344, MAS345, M9803R)
- [cczwei-forum.de: C# software for reading DMM values](http://www.cczwei-forum.de/cc2/thread.php?threadid=3452)
- [Linux Magazin: E-Werke: Perl misst Stromverbrauch mit Multimeter](http://www.linux-magazin.de/Heft-Abo/Ausgaben/2007/08/E-Werke?category=0)
- [mas-345/marsh: multimeter read and store](https://savannah.nongnu.org/projects/marsh)
- [digitaltrip.hu: Mastech MAS-345 digital multimeter Windows GUI](http://libesz.digitaltrip.hu/mas-345/) ([github](https://github.com/libesz/MAS345_GUI))
- [github: device-mas345-perl](https://github.com/mschilli/device-mas345-perl)
- [b-redemann.de Auslesen von Messgeräten mit RS232 Interface über USB](http://www.b-redemann.de/sp-DMM-auslesen.shtml)
- [tmon](http://freecode.com/projects/tmon) (uses a MASTECH MAS345)

