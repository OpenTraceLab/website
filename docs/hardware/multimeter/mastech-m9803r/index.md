---
title: MASTECH M9803R
---

# MASTECH M9803R

<div class="infobox" markdown>

![MASTECH M9803R](./img/800px-Mastech_m9803r_device_front.png){ .infobox-image }

### MASTECH M9803R

| | |
|---|---|
| **Status** | planned |
| **Counts** | 4000 |
| **IEC 61010-1** | CAT II (1000V) |
| **Connectivity** | RS232 |
| **Measurements** | voltage, resistance, diode, capacitance, frequency, current, hFE |
| **Features** | autorange, true-rms, data hold, delay hold, min/max, relative, bargraph, backlight |
| **Website** | [p-mastech.com](http://web.archive.org/web/20100201191512/http://www.p-mastech.com/products/04_dm/m9803r.html) |

</div>

The **MASTECH M9803R** is a 4000 counts, CAT II (1000V) digital bench multimeter with RS232 connectivity. 

## Hardware

TODO.

## Photos

<div class="photo-grid" markdown>

[![800px Mastech M9803r Device Front](./img/800px-Mastech_m9803r_device_front.png)](./img/800px-Mastech_m9803r_device_front.png "800px Mastech M9803r Device Front"){ .glightbox data-gallery="mastech-m9803r" }
<span class="caption">800px Mastech M9803r Device Front</span>

</div>
## Protocol

The protocol is documented in: [cdmm&#58; M9803R Class Reference](http://www.mtoussaint.de/cdmm/doc/html/classM9803R.html)

```
Detailed Description
M9803R 11 byte binary protocoll.

Reverse engeneered by Matthias Toussaint

    Port settings seem to be 9600 7E1 or 9600 7O1 (looks like a bug)
    Protocoll is 11 bytes binary fixed length
    END OF PACKET is 0x0d 0x0a
    Multimeter continuously sends data

Byte 0: Sign ored together
0x00 -> positive
0x08 -> negative
0x01 -> overflow

Byte 1: Digit 4 binary
Byte 2: Digit 3 binary
Byte 3: Digit 2 binary
Byte 4: Digit 1 binary

Byte 5: Mode
0x00 DCV
0x01 ACV
0x02 DCA
0x03 ACA
0x04 Ohms
0x05 Ohms + Beep
0x06 Diode V
0x07 ADP
0x08 DCA (10A)
0x09 ACA (10A)
0x0A Freq
0x0C Capacity

Byte 6:Decimal point position
Display	Unit	Value
Frequency
0.000	kHz	0x00
00.00	kHz	0x01
00.00	Hz	0x05
000.0	Hz	0x06
Voltage
000.0	mV	0x00
0.000	V	0x01
00.00	V	0x02
000.0	V	0x03
0000.	V	0x04
Current
0.000	mA	0x00
00.00	mA	0x01
000.0	mA	0x02
Capacity
0.000	nF	0x00
00.00	nF	0x01
000.0	nF	0x02
0.000	uF	0x03
00.00	uF	0x04
Resistance
000.0	Ohm	0x00
0.000	kOhm	0x01
00.00	kOhm	0x02
000.0	kOhm	0x03
0000.	kOhm	0x04
00.00	MOhm	0x05

Byte 7: Hold/min/Max/Rel ored together
0x01 Hold
0x02 Rel
0x04 Min
0x08 Max

Byte 8: Auto/Manu
0x01 APOF (AutoPowerOff)
0x02 Manu
0x04 Auto
0x08 MEM

```
## Resources
- [Manual](http://www.pollin.de/shop/downloads/D830256B.PDF)
- [Vendor software](http://www.pollin.de/shop/downloads/D830256S.ZIP)

