# Brymen Bm857
| | | |:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:| | [*Image: \1* | | | Status | supported | | Source code | [serial-dmm](http://github.com/OpenTraceLab/?p=OpenTraceCapture.git;a=tree;f=src/hardware/serial-dmm) | | Counts | 50000, 500000(DCV), 999999(Hz) | | IEC 61010-1 | CAT III (1000V) / CAT IV (600V) | | Connectivity | RS232 | | Measurements | voltage, frequency, diode, resistance, continuity, capacitance, current | | Features | autorange, data hold, crest, backlight, true-rms, dBm (selectable impedance), %4-20mA | | Website | brymen.com *BM857s* *BM859s* | **Brymen BM857** The **Brymen BM857** is a 50000 counts (500000 DC V), CAT III (1000V) / CAT IV (600V) handheld digital multimeter with RS232 connectivity. The **BM859s** is also supported, it uses the same protocol. Adapter kits ship with IR to RS232 cables, and include RS232 to USB converters. Higher end models support dual temperature sensors and difference mode, and the reference impedance for dBm measurements can be chosen in a range between 4 and 1200 Ohms.
## Contents
\- *1 Hardware* \- *2 Photos* \- *3 BM850s series* \- *4 Protocol* \- *5 Resources*
## Hardware **Multimeter:** \- **Multimeter IC**: TBD \- **Precision +2.5V Voltage reference**: *Analog Devices REF43* \- **True RMS-to-DC converter**: *Analog Devices AD737* \- **EEPROM(?)**: Chip marked S24C0. \- **Unidentified**: Several 062-JRC chips. These appear to be JFET opamps. \- **Unidentified**: Two QFP64 chips. \- TODO **Cable:** \- TODO \- See the *BRUA-85Xa kit* and the *BC-85Xa adapter* \- See *User_talk:Mrnuke#BM857_PC_Interface_cable* ## Photos **Multimeter:** \-
[*Image: \1*
Box
\-
[*Image: \1*
Mughsot
\-
[*Image: \1*
Device, back
\-
[*Image: \1*
Package contents
\-
[*Image: \1*
Probe cable storage clips
\-
[*Image: \1*
LCD Backlight
\-
[*Image: \1*
Holster removed, front
\-
[*Image: \1*
Holster removed, back
\-
[*Image: \1*
Case opened
\-
[*Image: \1*
Rear cover
\-
[*Image: \1*
Front cover
\-
[*Image: \1*
Rear cover, PCB removed
\-
[*Image: \1*
Upper PCB, top
\-
[*Image: \1*
Upper PCB, bottom
\-
[*Image: \1*
Main PCB, top
\-
[*Image: \1*
Main PCB, bottom
\-
[*Image: \1*
High voltage isolation slots.
\-
[*Image: \1*
High voltage isolation walls, designed to fit in the isolation slots.
\-
[*Image: \1*
Input circuit near the V jack
\-
[*Image: \1*
Microcontroller (right), and LCD controller (left)
\-
[*Image: \1*
Microcontroller (right), and LCD controller (left)
\-
[*Image: \1*
LCD controller and connector
\-
[*Image: \1*
ICs on the main PCB
\-
[*Image: \1*
More ICs
**Cable:** This can use either the BC-85X or the BC-85X-1 cables. See *Device_cables#Brymen_BC-85X(-1)* "Device cables"). Currently, mrnuke is working on an improvised USB-to-infrared converter cable. See *User_talk:Mrnuke#BM857_PC_interface_cable* for more details. Newer models (BM850a/BM850s) are said to require the BU-85Xa adapter. These different versions of meters and adapters are not compatible to each other.  \-
[*Image: \1*
Cable hookup
\-
[*Image: \1*
Cable hookup, detail
\-
[*Image: \1*
Cable hookup, closeup
\-
[*Image: \1*
Cable hookup, top detail
## BM850s series The BM857s and BM859s meters (the BM850s series) uses the same protocol and works with the *BC-85Xa adapters*.  \-
[*Image: \1*
BM859s front with sleeve
\-
[*Image: \1*
BM859s front
\-
[*Image: \1*
BM859s manual
\-
[*Image: \1*
BM859s box front
\-
[*Image: \1*
BM859s display segments
## Protocol Serial communication (genuine COM port), textual presentation of measurement values (floating point, normalized mantissa plus exponent), combined with binary bit fields for current meter's function and thus measured unit, variable length records with control chars in the header/footer (DLE, STX/ETX) around the mode flags and value's text, up to 22 bytes per DMM packet. See resources below for a full description of the protocol.  ## Resources \- vendor's *BM810/BM830/BM850 page* which links to individual 857/859 devices \- vendor's *download area*, *BM850 section*, [BM850s protocol details](http://brymen.com/product-html/images/DownloadList/ProtocolList/BM850-BM850a-BM850s_List/BM850-BM850a-BM850s-500000-count-DMM-protocol-BC85X-BC85Xa.zip) (links have changed in the past, might too in the future) \- BM850/BM850a/BM850s protocol documentation *download area* and [ZIP with PDF](http://brymen.com/product-html/images/DownloadList/ProtocolList/BM850-BM850a-BM850s_List/BM850-BM850a-BM850s-500000-count-DMM-protocol-BC85X-BC85Xa.zip) (worked as of 2019-06-10, vendor may change that)
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=Brymen_BM857&oldid=15616](https://OpenTraceLab.org/w/index.php?title=Brymen_BM857&oldid=15616)"
: \- *Device* \- *Multimeter* \- *Supported*
## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
