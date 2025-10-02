---
title: BENNING MM 12
---

# BENNING MM 12

<div class="infobox" markdown>

![BENNING MM 12](./img/BENNING_MM_12_-_APPA_506B_-_Teardown_-_06.jpg){ .infobox-image }

### BENNING MM 12

| | |
|---|---|
| **Status** | in progress |
| **Source code** | [appa-dmm](https://github.com/OpenTraceLab/OpenTraceCapture/tree/main/src/hardware/appa-dmm) |
| **Counts** | 40000 |
| **IEC 61010-1** | CAT III (1000V) / CAT IV (600V) |
| **Connectivity** | Infrared (USB/RS232), Bluetooth LE |
| **Measurements** | voltage, frequency, period, resistance, continuity, diode, capacitance, current, temperature |
| **Features** | autorange, data hold, auto hold, peak hold, min/max/avg, relative (%/delta), level (dB/dBm), automatic backlight, true-rms, data logging (40000 records), auto store (1000 records), auto-v/LoZ, ac+dc, VFD, secondary display value, auto fuse detector |
| **Website** | [benning.de](https://www.benning.de/products-en/testing-measuring-and-safety-equipment/digital-multimeter/benning-mm-12.html) |

</div>

The **BENNING MM 12** is a 40000 counts, CAT IV (600V) / CAT III (1000V) dual display handheld digital multimeter with USB and Bluetooth LE connectivity.

It is based on the [APPA 506B](https://sigrok.org/wiki/APPA_500_Series), See also: [APPA Multimeters](https://sigrok.org/wiki/APPA_Multimeters).

The driver supporting these APPA-based devices ("appa-dmm" in sigrok) has been created and will be included in mainline sigrok once it passes acception (see developement repository [github.com/Cymaphore/libsigrok branch appa-dmm](https://github.com/Cymaphore/libsigrok)).

# Hardware
- **MCU**: [CYPRESS MB95F718E](https://www.cypress.com/file/238696/download) (1828 6TTL E2)
- **ADC IC**: [CYRUSTEK ES51966A](http://www.cyrustek.com.tw/spec/ES51966A.pdf) (1839-GL9K)
- **LCD IC**: [HOLTEK HT1622](https://www.holtek.com/documents/10179/116711/HT1622v270.pdf) (B829J006QG2)
- **BLE SoC**: [AMICCOM A8105](http://www.amiccom.com.tw/asp_en/product_detail.asp?CATG_ID=15&PRODUCT_ID=84) (F5001AQ5A AMV38041 1932D)
- **EEPROM**: 2 x [Microchip 24LC512](http://ww1.microchip.com/downloads/en/DeviceDoc/21754M.pdf) (I/SM 1810UP4)
- **Fuses**:
**Current range 10A**: Amp rating: 11A, Voltage rating: 1kV, Interrupting rating: 30kA, Opening: Fast acting, Size: 10mm x 38mm
- **Current range 400mA**: Amp rating: 0.44A, Voltage rating: 1kV, Interrupting rating: 10kA, Opening: Fast acting, Size: 10mm x 34.9mm
- **Power supply:** 4 x IEC LR6 1.5V (works fine with IEC HR6 1.2V)
# Photos and Teardown

		- 
			[](./img/Benning_MM_12_-_04_-_SmuView.png)

MM 12 connected to SmuView visualizing readings from the power grid

		- 
			[](./img/Benning_MM_12_-_01_-_Front_Sleeve.png)

Front view

		- 
			[](./img/Benning_MM_12_-_03.jpg)

Measuring voltage and frequency from the power grid

		- 
			[](./img/Benning_MM_12_-_10_-_Display_with_automatic_backlight.jpg)

Display, automatic backlight on

		- 
			[](./img/Benning_MM_12_-_05_-_No_Sleeve.jpg)

Protective sleeve removed

		- 
			[](./img/Benning_MM_12_-_06_-_Rear_view.jpg)

Rear

		- 
			[](./img/Benning_MM_12_-_07_-_Optical_data_interface.jpg)

Optical data port (USB/Serial)

		- 
			[](./img/Benning_MM_12_-_08_-_Data_cable.jpg)

Included data cable ([APPA IC-300U](https://sigrok.org/wiki/Device_cables#APPA_IC-300U))

		- 
			[](./img/Benning_MM_12_-_09_-_Rear_open.jpg)

Batteries and fuses

		- 
			[](./img/BENNING_MM_12_-_APPA_506B_-_Teardown_-_01.jpg)

Teardown 1/14

		- 
			[](./img/BENNING_MM_12_-_APPA_506B_-_Teardown_-_02.jpg)

Teardown 2/14

		- 
			[](./img/BENNING_MM_12_-_APPA_506B_-_Teardown_-_03.jpg)

Teardown 3/14

		- 
			[](./img/BENNING_MM_12_-_APPA_506B_-_Teardown_-_04.jpg)

Teardown 4/14

		- 
			[](./img/BENNING_MM_12_-_APPA_506B_-_Teardown_-_05.jpg)

Teardown 5/14

		- 
			[](./img/BENNING_MM_12_-_APPA_506B_-_Teardown_-_06.jpg)

Teardown 6/14

		- 
			[](./img/BENNING_MM_12_-_APPA_506B_-_Teardown_-_07.jpg)

Teardown 7/14

		- 
			[](./img/BENNING_MM_12_-_APPA_506B_-_Teardown_-_08.jpg)

Teardown 8/14

		- 
			[](./img/BENNING_MM_12_-_APPA_506B_-_Teardown_-_09.jpg)

Teardown 9/14

		- 
			[](./img/BENNING_MM_12_-_APPA_506B_-_Teardown_-_10.jpg)

Teardown 10/14

		- 
			[](./img/BENNING_MM_12_-_APPA_506B_-_Teardown_-_11.jpg)

Teardown 11/14

		- 
			[](./img/BENNING_MM_12_-_APPA_506B_-_Teardown_-_12.jpg)

Teardown 12/14

		- 
			[](./img/BENNING_MM_12_-_APPA_506B_-_Teardown_-_13.jpg)

Teardown 13/14

		- 
			[](./img/BENNING_MM_12_-_APPA_506B_-_Teardown_-_14.jpg)

Teardown 14/14

# Review and Test

Unless noted otherweise, the tests in this section have been performed by [Cymaphore](https://sigrok.org/wiki/User:Cymaphore) on a Benning MM 12, Firmware v1.13

## Usage of rechargable NiMH batteries

The device works quite well with rechargable batteries. Voltage boundaries are well selected to suit the needs of both Alkaline and NiMH cells. For NiMH the reported battery level is of course always too low.

Battery indication

- FULL: >5.66 V (~ 1.415 V/cell)
- HALF: >5.16 V (~ 1.290 V/cell)
- LOW: >4.66 V (~ >1.165 V/cell)
- WARN: >4.06 V (~1.015 V/cell)
- Forced POWER-OFF: <4.06 V (~ 1.015 V/cell)

The cut-off voltage (device turns off with "Battery" error) of about 1V/cell is well suited for NiMH cells.

## Current consumption

Test supply voltage: 4.8 V

### Details
| Function | Bare | w. Backlight active | w. BLE active | w. Optical active | (w. BLE standby) |
|---|---|---|---|---|---|
| AutoV / LoZ | 16.3 mA | 26.2 mA | 21.9 mA | 19.3 mA | 18.7 mA |
| V~ | 16.2 mA | 25.8 mA | 21.7 mA | 18.7 mA | 18.1 mA |
| mV~ | 15.8 mA | 25.6 mA | 21.4 mA | 18.6 mA | 18.3 mA |
| V= | 16.1 mA | 25.8 mA | 21.6 mA | 18.8 mA | 18.2 mA |
| mV= | 15.8 mA | 25.6 mA | 21.8 mA | 18.7 mA | 18.1 mA |
| Ohm | 16.4 mA | 26.4 mA | 22.4 mA | 19.7 mA | 18.5 mA |
| Capacity | 19.6 mA | 30.0 mA | 25.0 mA | 23.0 mA | 21.5 mA |
| Diode | 19.7 mA | 30.0 mA | 25.5 mA | 23.2 mA | 22.0 mA |
| A~ | 16.0 mA | 26.3 mA | 22.5 mA | 19.2 mA | 18.6 mA |
| Temperature | 16.9 mA | 27.3 mA | 25.0 mA | 19.7 mA | 19.6 mA |
|  |  |  |  |  |  |
| Average | 16.9 mA | 26.9 mA | 22.9 mA | 19.9 mA | 19.2 mA |
| Maximum | 19.7 mA | 30.0 mA | 25.5 mA | 23.2 mA | 22.0 mA |
| Minimum | 15.8 mA | 25.6 mA | 21.4 mA | 18.6 mA | 18.1 mA |

### Average, Min, Max
| Average of averages: | 21.639 mA |
|---|---|
| Max of Maximums: | 30.000 mA |
| Min of Minimums: | 15.820 mA |

### Estimated consumption of individual features
| Avg. backlight consumption: | 9.780 mA |
|---|---|
| Avg. BLE active consumption: | 5.580 mA |
| Avg. Serial active consumption: | 2.780 mA |
| Avg. BLE standby consumption: | 2.280 mA |

## Test of Battery duration performance

For this test, a long-duration logging situation was set up.

For the test I used NiMH cells that have only been used a couple of times before.

In this test the device was able to continously work for **89.3 hours while providing data over Bluetooth LE** to a desktop client.

In comparison, the 50 hours of battery life on alkaline cells claimed in the 506B datasheet seem to be a pessimistic worst-case estimation.

### Test parameters
- Display light configured to be always off
- Uninterrupted operation
- Permanent Data acquisition over Bluetooth LE at maximum possible rate
- AC Volt function
- Continuous measurement of Voltage and Frequency of the power grid
### NiMH-Cells used for the test
- 4 x VARTA Endless 56686 (LSD)
- Nominal capacity: 2500mAh
- Fully charged before the test, reported charged capacity of the charger: ~2600mAh/cell (doesn't consider charging efficiency).
### Test results
- Test duration: 89 hours, 17 minutes, 40 seconds
- End condition: Device shut down and reported "BATTERY"
- Cell voltage after end of test: ~1.04 V/cell
# Examples: Establish data connection between sigrok and MM 12

**Important:** Driver is not (yet) part of mainline sigrok - see [this repository in github](https://github.com/Cymaphore/libsigrok) if you want to use it already.

## Serial/USB

Assuming the meter is turned on, plugged in and the usb-serial driver is loadad and up (should happen automatically). /dev/ttyUSB0 is used as an example.

List devices, if unsure what the serial port is:

```
 # sigrok-cli --list-serial
 /dev/ttyUSB0  CP2102 USB to UART Bridge Controller - 2020y000231

```

Scan for MM 12 with USB/Serial connection:

```
 $ sigrok-cli -d benning-dmm:conn=/dev/ttyUSB0 --scan

```

Show readings from connected meter:

```
 $ sigrok-cli -d benning-dmm:conn=/dev/ttyUSB0 --continuous

```

Open in SmuView:

```
 $ smuview --driver benning-dmm:conn=/dev/ttyUSB0

```
## Bluetooth LE

Assuming the meter is turned on and bluetooth activated on the meter and the PC. Important: Your Bluetooth-Controller must support BLE.

Scan for BLE devices:

```
 # sudo sigrok-cli --list-serial
 bt/appa-dmm/18-7A-93-BF-47-62   BENNING MM12 (BLE)

```

If your OS / UI supports it, you can also use the Bluetooth scanning capability from the system tray and pick the MAC address from the details there.

"18:7A:93:BF:47:62" acts as an example for the device address you will find. For sigrok the ":" must be replaced by "-" for now. That device address is used for the following examples, just replace it by the address of your own meter.

The full connection string then would look like this, as seen in the scanning result: bt/appa-dmm/18-7A-93-BF-47-62

Scan for MM 12 with BLE connection:

```
 $ sigrok-cli -d benning-dmm:conn=bt/appa-dmm/18-7A-93-BF-47-62 --scan

```

Show readings from connected meter:

```
 $ sigrok-cli -d benning-dmm:conn=bt/appa-dmm/18-7A-93-BF-47-62 --continuous

```

Open in SmuView:

```
 $ smuview --driver benning-dmm:conn=bt/appa-dmm/18-7A-93-BF-47-62

```
# Protocol

The protocol on Serial and BLE is the same like for most of the APPA based models.

# Resources
- [BENNING MM 12 Product Website](https://www.benning.de/products-en/testing-measuring-and-safety-equipment/digital-multimeter/benning-mm-12.html)

## Photos

<div class="photo-grid" markdown>

[![Benning Mm 12 Appa 506b Teardown 06](./img/BENNING_MM_12_-_APPA_506B_-_Teardown_-_06.jpg)](./img/BENNING_MM_12_-_APPA_506B_-_Teardown_-_06.jpg "Benning Mm 12 Appa 506b Teardown 06"){ .glightbox data-gallery="benning-mm-12" }
<span class="caption">Benning Mm 12 Appa 506b Teardown 06</span>

[![Benning Mm 12 03](./img/Benning_MM_12_-_03.jpg)](./img/Benning_MM_12_-_03.jpg "Benning Mm 12 03"){ .glightbox data-gallery="benning-mm-12" }
<span class="caption">Benning Mm 12 03</span>

[![Benning Mm 12 Appa 506b Teardown 09](./img/BENNING_MM_12_-_APPA_506B_-_Teardown_-_09.jpg)](./img/BENNING_MM_12_-_APPA_506B_-_Teardown_-_09.jpg "Benning Mm 12 Appa 506b Teardown 09"){ .glightbox data-gallery="benning-mm-12" }
<span class="caption">Benning Mm 12 Appa 506b Teardown 09</span>

[![Benning Mm 12 07 Optical Data Interface](./img/Benning_MM_12_-_07_-_Optical_data_interface.jpg)](./img/Benning_MM_12_-_07_-_Optical_data_interface.jpg "Benning Mm 12 07 Optical Data Interface"){ .glightbox data-gallery="benning-mm-12" }
<span class="caption">Benning Mm 12 07 Optical Data Interface</span>

[![Benning Mm 12 10 Display With Automatic Backlight](./img/Benning_MM_12_-_10_-_Display_with_automatic_backlight.jpg)](./img/Benning_MM_12_-_10_-_Display_with_automatic_backlight.jpg "Benning Mm 12 10 Display With Automatic Backlight"){ .glightbox data-gallery="benning-mm-12" }
<span class="caption">Benning Mm 12 10 Display With Automatic Backlight</span>

[![Benning Mm 12 Appa 506b Teardown 12](./img/BENNING_MM_12_-_APPA_506B_-_Teardown_-_12.jpg)](./img/BENNING_MM_12_-_APPA_506B_-_Teardown_-_12.jpg "Benning Mm 12 Appa 506b Teardown 12"){ .glightbox data-gallery="benning-mm-12" }
<span class="caption">Benning Mm 12 Appa 506b Teardown 12</span>

[![Benning Mm 12 Appa 506b Teardown 04](./img/BENNING_MM_12_-_APPA_506B_-_Teardown_-_04.jpg)](./img/BENNING_MM_12_-_APPA_506B_-_Teardown_-_04.jpg "Benning Mm 12 Appa 506b Teardown 04"){ .glightbox data-gallery="benning-mm-12" }
<span class="caption">Benning Mm 12 Appa 506b Teardown 04</span>

[![Benning Mm 12 Appa 506b Teardown 13](./img/BENNING_MM_12_-_APPA_506B_-_Teardown_-_13.jpg)](./img/BENNING_MM_12_-_APPA_506B_-_Teardown_-_13.jpg "Benning Mm 12 Appa 506b Teardown 13"){ .glightbox data-gallery="benning-mm-12" }
<span class="caption">Benning Mm 12 Appa 506b Teardown 13</span>

[![Benning Mm 12 04 Smuview](./img/Benning_MM_12_-_04_-_SmuView.png)](./img/Benning_MM_12_-_04_-_SmuView.png "Benning Mm 12 04 Smuview"){ .glightbox data-gallery="benning-mm-12" }
<span class="caption">Benning Mm 12 04 Smuview</span>

[![Benning Mm 12 Appa 506b Teardown 08](./img/BENNING_MM_12_-_APPA_506B_-_Teardown_-_08.jpg)](./img/BENNING_MM_12_-_APPA_506B_-_Teardown_-_08.jpg "Benning Mm 12 Appa 506b Teardown 08"){ .glightbox data-gallery="benning-mm-12" }
<span class="caption">Benning Mm 12 Appa 506b Teardown 08</span>

[![Benning Mm 12 Appa 506b Teardown 07](./img/BENNING_MM_12_-_APPA_506B_-_Teardown_-_07.jpg)](./img/BENNING_MM_12_-_APPA_506B_-_Teardown_-_07.jpg "Benning Mm 12 Appa 506b Teardown 07"){ .glightbox data-gallery="benning-mm-12" }
<span class="caption">Benning Mm 12 Appa 506b Teardown 07</span>

[![Benning Mm 12 05 No Sleeve](./img/Benning_MM_12_-_05_-_No_Sleeve.jpg)](./img/Benning_MM_12_-_05_-_No_Sleeve.jpg "Benning Mm 12 05 No Sleeve"){ .glightbox data-gallery="benning-mm-12" }
<span class="caption">Benning Mm 12 05 No Sleeve</span>

[![Benning Mm 12 Appa 506b Teardown 01](./img/BENNING_MM_12_-_APPA_506B_-_Teardown_-_01.jpg)](./img/BENNING_MM_12_-_APPA_506B_-_Teardown_-_01.jpg "Benning Mm 12 Appa 506b Teardown 01"){ .glightbox data-gallery="benning-mm-12" }
<span class="caption">Benning Mm 12 Appa 506b Teardown 01</span>

[![Benning Mm 12 Appa 506b Teardown 03](./img/BENNING_MM_12_-_APPA_506B_-_Teardown_-_03.jpg)](./img/BENNING_MM_12_-_APPA_506B_-_Teardown_-_03.jpg "Benning Mm 12 Appa 506b Teardown 03"){ .glightbox data-gallery="benning-mm-12" }
<span class="caption">Benning Mm 12 Appa 506b Teardown 03</span>

[![Benning Mm 12 01 Front Sleeve](./img/Benning_MM_12_-_01_-_Front_Sleeve.png)](./img/Benning_MM_12_-_01_-_Front_Sleeve.png "Benning Mm 12 01 Front Sleeve"){ .glightbox data-gallery="benning-mm-12" }
<span class="caption">Benning Mm 12 01 Front Sleeve</span>

[![Benning Mm 12 06 Rear View](./img/Benning_MM_12_-_06_-_Rear_view.jpg)](./img/Benning_MM_12_-_06_-_Rear_view.jpg "Benning Mm 12 06 Rear View"){ .glightbox data-gallery="benning-mm-12" }
<span class="caption">Benning Mm 12 06 Rear View</span>

[![Benning Mm 12 Appa 506b Teardown 14](./img/BENNING_MM_12_-_APPA_506B_-_Teardown_-_14.jpg)](./img/BENNING_MM_12_-_APPA_506B_-_Teardown_-_14.jpg "Benning Mm 12 Appa 506b Teardown 14"){ .glightbox data-gallery="benning-mm-12" }
<span class="caption">Benning Mm 12 Appa 506b Teardown 14</span>

[![Benning Mm 12 Appa 506b Teardown 05](./img/BENNING_MM_12_-_APPA_506B_-_Teardown_-_05.jpg)](./img/BENNING_MM_12_-_APPA_506B_-_Teardown_-_05.jpg "Benning Mm 12 Appa 506b Teardown 05"){ .glightbox data-gallery="benning-mm-12" }
<span class="caption">Benning Mm 12 Appa 506b Teardown 05</span>

[![Benning Mm 12 09 Rear Open](./img/Benning_MM_12_-_09_-_Rear_open.jpg)](./img/Benning_MM_12_-_09_-_Rear_open.jpg "Benning Mm 12 09 Rear Open"){ .glightbox data-gallery="benning-mm-12" }
<span class="caption">Benning Mm 12 09 Rear Open</span>

[![Benning Mm 12 08 Data Cable](./img/Benning_MM_12_-_08_-_Data_cable.jpg)](./img/Benning_MM_12_-_08_-_Data_cable.jpg "Benning Mm 12 08 Data Cable"){ .glightbox data-gallery="benning-mm-12" }
<span class="caption">Benning Mm 12 08 Data Cable</span>

[![Benning Mm 12 Appa 506b Teardown 10](./img/BENNING_MM_12_-_APPA_506B_-_Teardown_-_10.jpg)](./img/BENNING_MM_12_-_APPA_506B_-_Teardown_-_10.jpg "Benning Mm 12 Appa 506b Teardown 10"){ .glightbox data-gallery="benning-mm-12" }
<span class="caption">Benning Mm 12 Appa 506b Teardown 10</span>

[![Benning Mm 12 Appa 506b Teardown 02](./img/BENNING_MM_12_-_APPA_506B_-_Teardown_-_02.jpg)](./img/BENNING_MM_12_-_APPA_506B_-_Teardown_-_02.jpg "Benning Mm 12 Appa 506b Teardown 02"){ .glightbox data-gallery="benning-mm-12" }
<span class="caption">Benning Mm 12 Appa 506b Teardown 02</span>

[![Benning Mm 12 Appa 506b Teardown 11](./img/BENNING_MM_12_-_APPA_506B_-_Teardown_-_11.jpg)](./img/BENNING_MM_12_-_APPA_506B_-_Teardown_-_11.jpg "Benning Mm 12 Appa 506b Teardown 11"){ .glightbox data-gallery="benning-mm-12" }
<span class="caption">Benning Mm 12 Appa 506b Teardown 11</span>

</div>
