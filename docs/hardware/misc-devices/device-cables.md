# Device Cables
This page contains information and teardown photos of various multimeter/datalogger/etc. PC connectivity cables and adapters. See the [README.devices](https://github.com/OpenTraceLab/?p=OpenTraceCapture.git;a=blob;f=README.devices;hb=HEAD) file for connection types, as well as for details on automatic detection and mandatory or optional parameters.
## Contents
\- *1 Multimeters* \- *1.1 Agilent U1173A* \- *1.2 Agilent U1173B* \- *1.3 Agilent U1177A* \- *1.4 Agilent U5481A* \- *1.5 Amprobe 38SW-A* \- *1.6 APPA / ISO-TECH IC-50* \- *1.7 APPA / ISO-TECH IC-70* \- *1.8 APPA IC-300* \- *1.9 APPA IC-300U* \- *1.10 Brymen BC-85X(-1)*) \- *1.10.1 Brymen BR85X interface kit* \- *1.11 Brymen BRUA-20X* \- *1.12 Brymen BRUA-85Xa kit* \- *1.13 Brymen BC-85Xa* \- *1.13.1 Extech SW-810a kit* \- *1.14 Brymen BU-86X* \- *1.14.1 Brymen BU-86X interface kit* \- *1.15 Digitek DT4000ZC cable* \- *1.16 Fluke IR189USB* \- *1.17 Fluke OC4USB* \- *1.18 Fluke PM9080* \- *1.19 Gossen Metrawatt* \- *1.20 GreenLee DMSC-9U* \- *1.21 Meterman 38XR RS232 cable* \- *1.22 Metex 5-pin RS232 cable* \- *1.22.1 Version 1* \- *1.22.2 Version 2* \- *1.22.3 Cable pinout* \- *1.23 UNI-T UT-D02* \- *1.24 UNI-T UT-D04* \- *1.25 UNI-T UT-D07A* \- *1.26 UNI-T UT-D09* \- *1.27 V&A; VA4000* \- *1.28 V&A; VA4001* \- *1.29 Victor 86C USB cable* \- *2 Sound level meters* \- *2.1 Colead SL-5868P cables* \- *2.2 Tondaj SL-814 cable* \- *3 Programmable electronic loads* \- *3.1 M133* \- *4 Scales* \- *4.1 KERN EW 6200-2NM cable* \- *5 See also*
# Multimeters ## Agilent U1173A The [Agilent U1173A](http://www.home.agilent.com/agilent/product.jspx?cc=DE&lc=ger&ckey=792204&nid=-536906710.536910943.00&id=792204&pselect=SR.GENERAL) is an IR-USB cable. **Hardware**: \- Prolific PL2303HX (max. baudrate 19200, according to the Agilent website) **Works with**: \- Agilent U1230/40/50/70 series \- Note: For the U1240 series, the additional [U1179A](http://www.home.agilent.com/agilent/redirector.jspx?action=ref&lc=ger&cc=DE&nfr=-536906710.536910943&ckey=2101709&cname=PRODUCT) IR bracket is required.[1](http://www.home.agilent.com/agilent/product.jspx?cc=DE&lc=ger&nid=-536906710.536910943&pageMode=OV) **Where to buy**: \- [Agilent](http://www.home.agilent.com/agilent/product.jspx?cc=DE&lc=ger&ckey=792204&nid=-536906710.536910943.00&id=792204&pselect=SR.GENERAL) (\$31) \- [Newark](http://www.newark.com/keysight-technologies/u1173b/pc-connectivity-cable-handheld/dp/05X9288?rpsku=rel3%3AU1173A) (\$32) *no longer available, U1173B is the suggested replacement* \- [Datatec](http://www.datatec.de/U1173A-Agilent-Adapterkabel.htm) (€23)  \-
[*Image: \1*
Device, front
\-
[*Image: \1*
PCB, front
\-
[*Image: \1*
PCB, back
## Agilent U1173B The [Agilent U1173B](http://www.keysight.com/en/pd-2314431-pn-U1173B/handheld-digital-multimeter-pc-connectivity-cable?&cc=CH&lc=ger) is an IR-USB cable. See *Device cables/Info#Agilent_U1173B* for more details (such as **lsusb -v** output) about the cable. **Hardware**: \- Prolific PL2303TA  \-
[*Image: \1*
Case, opened, from inside
\-
[*Image: \1*
PCB, front
\-
[*Image: \1*
PCB, back
## Agilent U1177A The [Agilent U1177A](http://www.home.agilent.com/agilent/product.jspx?cc=DE&lc=ger&ckey=2090364&nid=-536902461.1006710.00&id=2090364&pselect=SR.GENERAL) is an IR-Bluetooth interface module. Notes: 9600 baud, 8n1 settings on the PC. The protocol (AT commands, documented in the [Agilent U1177A configuration guide](http://cp.literature.agilent.com/litweb/pdf/U1177-90002.pdf)) allows changing the baud rate to 19200, among other things.[1](http://www.home.agilent.com/agilent/redirector.jspx?action=ref&cname=AGILENT_EDITORIAL&ckey=2150265&lc=ger&cc=DE&nfr=-536902461.1006710.00) Default Bluetooth PIN: 1234. For the U1240 series, the additional [U1179A](http://www.home.agilent.com/agilent/redirector.jspx?action=ref&lc=ger&cc=DE&nfr=-536906710.536910943&ckey=2101709&cname=PRODUCT) IR bracket is required.[2](http://www.home.agilent.com/agilent/product.jspx?cc=DE&lc=ger&nid=-536906710.536910943&pageMode=OV) **Hardware**: \- CSR BC417... (Bluetooth classic, SPP aka RFCOMM) \- Macronix MX... \- PCB markings: U1177-26500, REV004, MSD-02 **Works with**: \- Agilent U1230/40/50/70 series **Where to buy**: It is often given away free as a promotion with one of the Agilent U12xxA meters, but can also be purchased separately: \- [Agilent](http://www.home.agilent.com/agilent/product.jspx?cc=DE&lc=ger&ckey=2090364&nid=-536902461.1006710.00&id=2090364&pselect=SR.GENERAL) (\$49) \- [Datatec](http://www.datatec.de/Agilent-1177A-Bluetooth.htm) (€36)  \-
[*Image: \1*
Device, front
\-
[*Image: \1*
Device, back
\-
[*Image: \1*
Battery compartment
\-
[*Image: \1*
PCB, front
\-
[*Image: \1*
PCB, back
## Agilent U5481A The [Agilent U5481A](http://www.keysight.com/en/pd-1691186/ir-to-usb-cable) is an IR-USB cable. **Works with**: \- Agilent U1700B series LCR meters, U1401A calibrator/meter ## Amprobe 38SW-A The [Amprobe 38SW-A](http://www.amprobe.eu/en_GB/showproduct/234/38SW-A/) is an RS232 PC interface cable for the [Amprobe 38XR-A](http://www.amprobe.eu/en_GB/showproduct/134/38XR-A/) multimeter. The "38SW-A" name is also used to refer to the respective PC software for use with the serial cable. **Hardware**: \- TODO. **Works with**: \- [Amprobe 38XR-A](http://www.amprobe.eu/en_GB/showproduct/134/38XR-A/) **Where to buy**: \- [Digikey](http://www.digikey.com/product-detail/en/38SW-A/38SW-A-ND/1540519), [TME.eu](http://www.tme.eu/de/details/38sw-a/messgerate-software/amprobe/38sw/), [RS Components](http://de.rs-online.com/mobile/p/digital-multimeter/0411722/), *Mercateo*, [testersandtools.com](http://www.testersandtools.com/Amprobe-38SW-A-RS232-Software-Cable.php), [Newark](http://www.newark.com/amprobe-instruments/38sw-a/rs-232-cable-software-38xr-a/dp/29M6230), [Distrelec](https://www.distrelec.de/interfacekabel-und-software/amprobe/38sw-a/911905/de), and various others. \- The usual price is around €20-€35, depending on vendor and location.  \-
[*Image: \1*
Package, top
\-
[*Image: \1*
Package, bottom
\-
[*Image: \1*
Cable, top
\-
[*Image: \1*
Cable, bottom
\-
[*Image: \1*
CD-ROM, top
\-
[*Image: \1*
CD-ROM, bottom
\-
[*Image: \1*
CD-ROM, contents
\-
[*Image: \1*
Cable, opened
\-
[*Image: \1*
Housing 1
\-
[*Image: \1*
Housing 2
\-
[*Image: \1*
PCB, top
\-
[*Image: \1*
PCB, bottom
\-
[*Image: \1*
PCB, pinout
## APPA / ISO-TECH IC-50 The IC50 is a USB PC interface cable for some APPA and ISO-TECH multimeters and thermometers. **Works with**: \- [APPA 70](http://www.appatech.com/appa_product_home.php?pdid=2005102401295373290&kindid=2005081003113623241) series multimeters (and ISO-TECH IDM 70 series clone) \- [APPA 50](http://www.appatech.com/appa_product_home.php?pdid=20051220112048498347&kindid=20050810031145946832) series thermometer (and RS 50 series clone) **Where to buy**: \- [RS 704-8135](http://uk.rs-online.com/web/p/multimeter-accessories/7048135/) \- The price is around 40 € ## APPA / ISO-TECH IC-70 The IC70 is an RS232 PC interface cable for some APPA and ISO-TECH multimeters and thermometers. **Works with**: \- [APPA 70](http://www.appatech.com/appa_product_home.php?pdid=2005102401295373290&kindid=2005081003113623241) series multimeters (and ISO-TECH IDM 70 series clone) \- [APPA 50](http://www.appatech.com/appa_product_home.php?pdid=20051220112048498347&kindid=20050810031145946832) series thermometer (and RS 50 series clone) **Where to buy**: \- [RS 460-9881](http://uk.rs-online.com/web/p/digital-multimeters/4609881/) \- The price is around 20 €  \-
[*Image: \1*
Cable
## APPA IC-300 The IC-300U is an optical to RS232 serial interface cable for the *APPA 500 Series* based handheld multimeters as well as the *APPA 200 Series* based bench multimeters of various brands. It is usually included with the older models. ## APPA IC-300U The IC-300U is an optical to USB serial interface cable for the *APPA 500 Series* based handheld multimeters as well as the *APPA 200 Series* based bench multimeters of various brands. It is usually included with the newer models. \-
[*Image: \1*
Optical data port of the APPA 500 Series
\-
[*Image: \1*
APPA IC-300U cable
## Brymen BC-85X(-1) Not compatible with BC-85Xa. TODO. **Hardware**: \- TODO. **Works with**: \- Brymen BM857/BM859 (non-a versions) **Where to buy**: \- Available from Greenlee as DMSC-9 (not DMSC-9U). \- [TME](http://www.tme.eu/en/details/kitrs232c/meters-software/) (€26.82) ### Brymen BR85X interface kit \-
[*Image: \1*
Kit contents (software disc not shown)
\-
[*Image: \1*
BC-85X-1 DB9 connector
\-
[*Image: \1*
BC-85Xa DMM connector
## Brymen BRUA-20X **Hardware**: \- IR to DSub-9 cable, connecting the DMM to a COM port \- DSub-9 to USB converter (Prolific 2303 chip, USB CDC, regular COM port), and USB A-B cable to connect to a computer's USB port **Works with**: \- Brymen BM20x and BM25x series **Where to buy**: \- [TME](http://www.tme.eu/en/details/kitbrua-20x/meters-software/brymen/) (€30) \- [Welectron](https://www.welectron.com/Brymen-BRUA-20X-USB-Interface) \-
[*Image: \1*
Package, top
\-
[*Image: \1*
Package, side
\-
[*Image: \1*
Package contents
\-
[*Image: \1*
BUA-2303, front
\-
[*Image: \1*
BUA-2303, bottom
\-
[*Image: \1*
BC-20X, cable
\-
[*Image: \1*
BC-20X, attached
## Brymen BRUA-85Xa kit Kit provided by Brymen, contains \- **Bs-Software** on CD \- **BC-85Xa** cable with infrared and D-sub 9 connector ends \- **BUA-2303** USB to serial converter (PL2303 converter, Sipex SP213 transceiver) and USB-A to USB-B cable available at [welectron](https://www.welectron.com/Brymen-USB-Interfaces), announced to work with the BM850s series appears to be the same as the *Extech SW-810a kit* \-
[*Image: \1*
kit contents, IR to RS232, RS232 to USB, USB cable, CDROM
\-
[*Image: \1*
box, front
\-
[*Image: \1*
box, side (list of content)
\-
[*Image: \1*
box, back (discusses adapter/converter interaction)
## Brymen BC-85Xa Not compatible with BC-85X. TODO. **Hardware**: \- TODO. **Works with**: \- Brymen BM857a/BM859a, also tested with BM859s \- Extech MM570A/MM560A/MP530A/MP510A **Where to buy**: \- Available from Extech in a kit with USB-to-serial converter and software disc, under the name SW-810a. \- [Mouser](http://de.mouser.com/Search/ProductDetail.aspx?qs=zS8Kl81wrHovBIt5EskF9A==) (€65.99) \- [TME](http://www.tme.eu/de/details/sw810a/umgebungsmesser-sonstige/extech/) (€60.60) ### Extech SW-810a kit This is a kit sold by Extech, containing the BC-85Xa RS232 cable, the BUA2303 USB-to-serial adapter, a USB cable, and a software disc. \-
[*Image: \1*
Kit contents (software disc not shown)
\-
[*Image: \1*
BC-85Xa DB9 connector
\-
[*Image: \1*
BC-85Xa DMM connector
\-
[*Image: \1*
BUA2303 USB-to-serial converter
\-
[*Image: \1*
BUA2303 USB-to-serial converter, back
\-
[*Image: \1*
BUA2303 USB-to-serial converter, bottom
\-
[*Image: \1*
IR side, opened
\-
[*Image: \1*
IR side casing
\-
[*Image: \1*
IR side PCB, top
\-
[*Image: \1*
IR side PCB, botoom
\-
[*Image: \1*
BUA2303 PCB, top
\-
[*Image: \1*
BUA2303 PCB, bottom
## Brymen BU-86X See *Brymen BU-86X/Info* for more details (such as lsusb -v output). **Hardware**: \- Cypress CY7C63743 enCoRe USB **Works with**: \- Brymen BM867/BM869 **Where to buy**: \- [TME](http://www.tme.eu/en/details/kitbu-86x/instruments-de-mesure-logiciels/brymen/) (40 €) ### Brymen BU-86X interface kit \-
[*Image: \1*
Kit content (software disc not shown)
\-
[*Image: \1*
BC-86X USB connector
\-
[*Image: \1*
BC-86X DMM connector
## Digitek DT4000ZC cable The *Digitek DT4000ZC* (and the rebadged *TekPower TP4000ZC*) ship with this RS232 to 3.5mm stereo plug cable. The ring on the plug is left unconnected. The cable works on the assumption that TX (pin 3) and DTR (pin 4) are at a fixed voltage and will not be toggled. TX should be below -3 V, and the resistor acts as a pull-down. DTR should be abouve 3V. The photodiode/phototransistor in the DMM will pull the RX pin above 3V when the IR diode is on. **Hardware**: \- SMD resistor between TX and RX pins. **Works with**: \- *Digitek DT4000ZC*, *TekPower TP4000ZC* **Where to buy**: \- The cable ships with the multimeter. It's unclear whether it can be bought standalone (without DMM). *Digitek DT4000ZC* photos: \-
[*Image: \1*
Device, front
\-
[*Image: \1*
Device, back
\-
[*Image: \1*
Device, open
\-
[*Image: \1*
Device, open 2
\-
[*Image: \1*
Resistor
*TekPower TP4000ZC* photos: \-
[*Image: \1*
Supplied RS-232 cable
\-
[*Image: \1*
RS-232 cable, disassembled
\-
[*Image: \1*
RS-232 cable, detail
## Fluke IR189USB The *Fluke IR189USB* is a USB interface cable for Fluke-18x and 28x series DMMs. It is a basic USB-serial cable, based on the [FTDI FT232RL](http://www.ftdichip.com/Products/ICs/FT232R.htm) chip. \-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
In the EEVblog forum a DIY cable for Fluke 289 was discussed: [USB to IR with FT232R and LM393](https://www.eevblog.com/forum/projects/fluke-187-ir-cable/?action=dlattach;attach=230869;image) ## Fluke OC4USB The *Fluke OC4USB* is a USB interface cable for the Fluke 120 series, 190 series scope meter, and the 430 series power quality analyzer. Resources: \- [DIY optical link cable for the Fluke Scopemeter 190 series](http://omapalvelin.homedns.org/fluke/) ## Fluke PM9080 The *Fluke PM9080* is an RS232 interface cable for "digital hard-copy output to serial printer or remote control via a PC". The max. supported baud rate is 57600. **Hardware**: No active components are on the PCB. Pinout: \- black: pin 2 (RX) \- brown: pin 3 (TX) \- red: pin 7, 8 (RTS, CTS) \- orange: pin 1, 4, 6 (DCD, DTR, DSR) \- yellow: pin 5 (GND) **Works with**: \- Fluke scope meter test tools, power harmonics analyzers, graphical multimeters and multifunction counters. **Where to buy**: \- *flukeonlinestore.com* (\$185.95) \- [fluke.eu](http://www.fluke.eu/comx/show_product.aspx?locale=dede&pid=31870) (€240.-) \- [Farnell](http://de.farnell.com/fluke/pm9080/pm9080-rs-232-adapter-kabel-optisch/dp/252384) (€240.-) \- [instrumentation2000.com](http://www.instrumentation2000.com/flukepm9080opticallyisolatedrs-232adaptercable.aspx) (\$187.95) \- [RS-Online](http://de.rs-online.com/web/p/interface-adapter/4256752/) (€245.-) \- [Amazon](http://www.amazon.com/Fluke-PM9080-101-Optically-Isolated/dp/B000LEDHHS) (\$168.23) **Resources**: \- [DIY optical link cable for the Fluke Scopemeter 190 series](http://omapalvelin.homedns.org/fluke/) \- [PM9080 Optically-isolated RS-232C Interface Adapter](http://www.scopemeter.com/accessories/PM9080.htm) (comparison of the different cable revisions)  \-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
## Gossen Metrawatt See *Gossen Metrawatt* page. ## GreenLee DMSC-9U TODO. **Hardware**: \- TODO. **Works with**: \- GreenLee DM-800 series, DML-430A **Where to buy**: \- TODO. ## Meterman 38XR RS232 cable The Meterman 38SW is an optically isolated RS232 PC interface cable for the Meterman 38XR multimeter. The "38SW" name is also used to refer to the respective PC software for use with the serial cable. By all accounts this cable is probably the same as the Amprobe 38SW-A cable as Amprobe bought Meterman. **Works with** \- *Meterman 38XR*  \-
[*Image: \1*
## Metex 5-pin RS232 cable This type of 5-pin RS232 cable is used in various Metex (and rebadged) multimeters. The cable exists in two flavours, an older version with equal pin distance (can be inserted the wrong way) and a newer version with a gap between pins 3 and 4 (fits only one way). ### Version 1 **Hardware**: \- No active components. \- 25-pin RS232 connector **Works with**: \- *Voltcraft M-3650CR*, *PeakTech 4380*, many others. **Where to buy**: \- The cable ships with the respective multimeter. It's unclear whether it can be bought standalone (without DMM).  \-
[*Image: \1*
25-pin RS-232 cable
\-
[*Image: \1*
DB-25F opened, wiring
### Version 2 **Hardware**: \- No active components. \- 9-pin RS232 connector **Works with**: \- *MASTECH MAS345*, *Voltcraft M-3650CR* (plug with equal pin distances!), *RadioShack 22-168*, *Voltcraft M-3650D*, many others. **Where to buy**: \- The cable ships with the respective multimeter. It's unclear whether it can be bought standalone (without DMM). *MASTECH MAS345*: \-
[*Image: \1*
Cable
\-
[*Image: \1*
Cable, connected
*RadioShack 22-168*: \-
[*Image: \1*
RS-232 cable
\-
[*Image: \1*
DMM connector
\-
[*Image: \1*
DMM connector, protective sheath removed
\-
[*Image: \1*
DB9 connector, opened
\-
[*Image: \1*
DB9 connections
**DIY:** \-
[*Image: \1*
DIY adapter
\-
[*Image: \1*
Pin numbers (Metex DMM)
### Cable pinout | | | | | | |----------------------------|----------------------|-----------------------|------------------------|-----------------------------------------------------| | Metex-connector pin (male) | RS-232 25-pin female | RS-232 DE9-female pin | Signal (computer side) | Remarks | | 1 | 7 | 5 | GND | | | 2 | 2 | 3 | TX | | | 3 | 4 | 7 | RTS | Used to power receiver in multimeter, must be OFF. | | 4 | 20 | 4 | DTR | Used to power receiver in multimeter, must be ON. | | 5 | 3 | 2 | RX | | ## UNI-T UT-D02 The *UNI-T UT-D02* is an RS232 cable for various UNI-T multimeters (and rebranded models) with PC connectivity. **Hardware**: \- TODO. **Works with**: \- UNI-T UT61D/... \- Voltcraft VC820/VC840/... **Where to buy**: \- *Reichelt* (€15.95) \- [Conrad/Voltcraft](http://www.conrad.de/ce/de/product/125640/VOLTCRAFT-RS-232-SCHNITTSTELLENADAPTER/SHOP_AREA_17626&promotionareaSearchDetail=005) (€9.95) \- *Pinnesonne* (€5.00) \- [eBay, various sellers](http://www.ebay.de/itm/UNI-T-UT-D02-RS232-Data-Cable-/360492337424) (€7.99)  \-
[*Image: \1*
Cable
\-
[*Image: \1*
Cable, IR
\-
[*Image: \1*
Cable, open
\-
[*Image: \1*
PCB, front
\-
[*Image: \1*
PCB, back
## UNI-T UT-D04 The *UNI-T UT-D04* (see also [uni-trend.com.cn](http://www.uni-trend.com.cn/cp-show.asp?yy=%D6%D0%CE%C4&ProductNO=386)) is a USB/HID cable for various UNI-T multimeters (and rebranded models) with PC connectivity. There have been (at least) two versions of this cable, the older one with Hoitek HE2325U USB/HID chip, the newer one using a WCH CH9325 USB/HID chip. See *Device cables/Info#UNI-T_UT-D04* for more details (such as **lsusb -v** output) about the cable. **Hardware (old version)**: \- Hoitek HE2325U **Hardware (new version)**: \- *WCH CH9325* **Works with**: \- *UNI-T UT61B* / *UT61C* / *UT61D* / *UT61E*, various other UNI-T DMMs \- *Voltcraft VC-820* / *VC-830* / *VC-840*, various other Voltcraft rebadges of UNI-T DMMs \- *Tenma 72-7745* and various other Tenma/Farnell rebadges of UNI-T DMMs **Where to buy**: \- *Reichelt* (€9.95) \- [Conrad/Voltcraft](http://www.conrad.de/ce/de/product/120317/Voltcraft-USB-SCHNITTSTELLENADPTER/SHOP_AREA_17626&promotionareaSearchDetail=005) (€25.95) \- *Pinnesonne* (€8.90) \- [eBay, various sellers](http://www.ebay.de/itm/UT-D04-USB-INFRARED-INTERFACE-CABLE-FOR-UT71-and-UT81-/180687967854) (€12.37)  \-
[*Image: \1*
Cable
\-
[*Image: \1*
Cable, IR
\-
[*Image: \1*
Attached cable
\-
[*Image: \1*
Opened 1
\-
[*Image: \1*
Opened 2
\-
[*Image: \1*
PCB, front
\-
[*Image: \1*
PCB, back
other cable, but only with different silkscreen (another batch?) \-
[*Image: \1*
Cable
\-
[*Image: \1*
Cable, IR
\-
[*Image: \1*
Opened
\-
[*Image: \1*
PCB, front
\-
[*Image: \1*
PCB, back
Voltcraft sells rebranded, UNI-T made DMMs, and also ships with the same USB/HID cable, but with a Voltcraft logo/marking on it. It is likely that Voltcraft also shipped both the old and new version of the cable at some point. \-
[*Image: \1*
Voltcraft cable
\-
[*Image: \1*
Voltcraft cable, IR
## UNI-T UT-D07A BLE adapter ("cable") for more recent UNI-T devices (UT-181A), mechanical fit with other devices, too (can be used anywhere instead of UT-D02, UT-D04, or UT-D09?) PIC18LF25K22 and BL79BLETRMC2 (ISSC) chips inside, teardown in an [EEVBlog forum post](https://www.eevblog.com/forum/projects/uni-t-ut-d07a-bluetooth/msg1346931/#msg1346931), including links to datasheets The ISSC BLETR module is a "Bluetooth SMART" aka BLE peripheral, and currently is not supported by OpenTraceCapture's serial communication layer. There is ObjectiveC source code for Apple's mobile devices at <https://github.com/ISSC/BLETR> which might help add support to OpenTraceCapture. TODO Need to determine the "initiation sequence", sending TX data from PC to device via adapter appears to work (device beeps when a request is sent). Getting RX data (BLE notifications) is yet to get done. Sniffing existing apps might help. Participation and feedback would be appreciated. Without it, progress will be stuck. see *Bluetooth* ## UNI-T UT-D09 mechanically compatible to UT-D02, UT-D04, and UT-D07 -- can be used with a wide range of UNI-T and compatible meters bidirectional (TX as well as RX), CP2110 HID chip, supported by OpenTraceCapture's serial communication layer ## V&A; VA4000 The [V&A VA4000](http://www.mastech.com.cn/html/en/products-accessories.htm) is a USB PC interface cable for various V&A; multimeters. It seems there have been at least two different revisions of the cable. The older one used a Sunplus SPCP825 USB-to-serial chip (see [here](http://www.mikrocontroller.net/topic/160215#2032176), [here](http://multimeter.schewe.com/), or also check the drivers from *here*), the newer revisions use a Prolific PL2303HX chip. See *Device cables/Info#V.26A_VA4000* for more details (such as **lsusb -v** output) about the cable. **Hardware** (old cable version): \- **USB to serial chip**: Sunplus SPCP825 \- **Crystal**: ? **Hardware** (new cable version): \- **USB to serial chip**: Prolific PL2303HX YR0903A \- **Crystal**: 12MHz **Works with**: \- V&A; VA18B, V&A; VA-38 **Where to buy**: \- [Komerci](http://www.komerci.de/shop/product_info.php?products_id=427&cPath=26_42&osCsid=0c0a8cf5d72cd931528b26aeb5af7ce5) (€6.50) Old cable with Sunplus SPCP825 chip from a *V&A; VA18B*: \-
[*Image: \1*
USB cable
\-
[*Image: \1*
Cable, dismantled
\-
[*Image: \1*
PCB, top
\-
[*Image: \1*
PCB, bottom
New cable with Prolific PL2303HX from a *V&A; VA18B*: \-
[*Image: \1*
USB cable
\-
[*Image: \1*
USB cable PCB, front
\-
[*Image: \1*
USB cable PCB, back
Another cable shipped with a *V&A; VA40B* (it has the same Prolific PL2303HX PCB as the V&A; 18B above, but seem to have a thinner mechanical plug): \-
[*Image: \1*
USB cable
\-
[*Image: \1*
USB cable, optical connector
## V&A; VA4001 The [V&A VA4001](http://www.mastech.com.cn/html/en/products-accessories.htm) is an RS232 PC interface cable for various V&A; multimeters. TODO. ## Victor 86C USB cable The *Victor 86C* PC interface cable (doesn't seem to have a specific name or part number) contains a USB/HID chip. **Hardware**: \- **USB/HID chip**: *Unmarked SO-20 chip* **Works with**: \- Victor 86C. Maybe other Victor models(?) **Where to buy**: \- The cable ships with the Victor 86C. It's unclear whether it can be bought standalone (without DMM).  \-
[*Image: \1*
USB cable
\-
[*Image: \1*
USB cable, open
\-
[*Image: \1*
USB cable PCB, front
\-
[*Image: \1*
USB cable PCB, back
More information about the USB chip and the protocol it uses to communicate with the PC can be found on the *Victor protocol* page. # Sound level meters ## Colead SL-5868P cables Some distributors sell the *Colead SL-5868P* sound level meter with a set of two cables: one 3.5mm jack to female DB9, and one male DB9 to USB, which has a Prolific PL-2303 chip in the DB9. This cable does not work; the device's serial port needs a 2.5mm jack. \-
[*Image: \1*
A really bad idea
\-
[*Image: \1*
DB9 to USB, top
\-
[*Image: \1*
DB9 to USB, bottom
\-
[*Image: \1*
3.5mm jack to DB9, top
\-
[*Image: \1*
3.5mm jack to DB9, bottom
The SL-5868P is also available with bluetooth connectivity instead of serial. ## Tondaj SL-814 cable The *Tondaj SL-814* sound level meter ships with this USB PC interface cable. **Hardware**: \- **USB to serial chip**: Prolific PL2303HX LFC10073A \- **Crystal**: 12MHz **Works with**: \- *Tondaj SL-814* (maybe other Tondaj gear?) **Where to buy**: \- The cable ships with the *Tondaj SL-814*. It's unclear whether it can be bought standalone (without the sound level meter).  \-
[*Image: \1*
Cable
\-
[*Image: \1*
Cable, connector
\-
[*Image: \1*
Cable, open
\-
[*Image: \1*
Cable, open 2
\-
[*Image: \1*
PCB, top
\-
[*Image: \1*
PCB, bottom
# Programmable electronic loads ## M133 The **M133** (vendor unknown) cable ships with the *ATTEN ATZ9711* programmable electronic load. It's unclear whether this is a custom cable for this device, or a generic RS232 isolator cable. The 28-pin chip is a standard Prolific PL-2303HX serial-USB chip. The other chip is presumably an optocoupler, but the vendor/model is unknown. \-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
In the EEVblog forum DIY cables for M97 and compatible loads were discussed: [M97 cable with FT232R and ADUM2402 isolator](https://www.eevblog.com/forum/testgear/maynuo-m9711-dc-electronic-load-any-good/?action=dlattach;attach=172720;image) # Scales ## KERN EW 6200-2NM cable The *KERN EW 6200-2NM* weighing scale ships with this RS232 interface cable. **Hardware**: \- No active components \- 9-pin RS232 connector **Works with**: \- *KERN EW 6200-2NM* (and likely other scales from the *KERN scale series*) **Where to buy**: \- The cable ships with the *KERN EW 6200-2NM*. It's unclear whether it can be bought standalone (without the scale).  \-
[*Image: \1*
Cable
# See also \- *Multimeter ICs* \- *Serial port* \- *Bluetooth*
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=Device_cables&oldid=15954](https://OpenTraceLab.org/w/index.php?title=Device_cables&oldid=15954)"
## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
