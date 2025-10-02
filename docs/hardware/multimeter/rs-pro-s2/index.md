---
title: RS PRO S2
---

# RS PRO S2

<div class="infobox" markdown>

![RS PRO S2](./img/RS_PRO_S2_-_Teardown_-_03.jpg){ .infobox-image }

### RS PRO S2

| | |
|---|---|
| **Status** | in progress |
| **Source code** | [appa-dmm](https://github.com/OpenTraceLab/OpenTraceCapture/tree/main/src/hardware/appa-dmm) |
| **Counts** | 6000 |
| **IEC 61010-1** | CAT III (1000V) / CAT IV (600V) |
| **Connectivity** | Bluetooth LE |
| **Measurements** | voltage, frequency, resistance, continuity, diode, capacitance, current, temperature |
| **Features** | autorange, data hold, min/max, relative, non-contact voltage detection hi/lo, backlight, true-rms, data logging, single value storage, auto-v/loz, VFD, built-in magnetic sticker, µA current range |
| **Website** | [rsonline-privat.de](https://www.rsonline-privat.de/Products/ProductDetail/RS-PRO-Digital-Multimeter-1000V-ac-400mA-ac-40M-Bluetooth-Kat-III-Kat-IV-1993847) |

</div>

The **RS PRO S2** is a 6000 counts, CAT IV (600V) / CAT III (1000V) handheld logging digital multimeter with Bluetooth LE connectivity and long battery duration. It is marketed as a "HVAC Multimeter" (optimized for the needs of heating, ventilation, and air conditioning technicians).

It is based on the [APPA S2](https://sigrok.org/wiki/APPA_S_Series), See also: [APPA Multimeters](https://sigrok.org/wiki/APPA_Multimeters).

A sigrok-driver supporting these APPA-based devices ("appa-dmm" in sigrok) has been created and will be included in mainline sigrok once it passes acception (see developement repository [github.com/Cymaphore/libsigrok branch appa-dmm](https://github.com/Cymaphore/libsigrok)).

# Hardware
- **MCU**: [Atmel ATSAML22N18A-U](https://ww1.microchip.com/downloads/en/DeviceDoc/60001465A.pdf)
- **ADC-ID**: [Hycontek HY12P65](http://www.hycontek.com/wp-content/uploads/DS-HY12P65-TC.pdf)
- **BLE-SoC**: [AMICCOM A8105](http://www.amiccom.com.tw/asp_en/product_detail.asp?CATG_ID=15&PRODUCT_ID=84)
- **Fuses**:
**Current range 400mA**: Amp rating: 0.44A, Voltage rating: 1kV, Interrupting rating: 10kA, Opening: Fast acting, Size: 10mm x 34.9mm
- **Power supply:** 2 x IEC LR6 1.5V (works fine with IEC HR6 1.2V)
# Photos and Teardown

		- 
			[](./img/RS_PRO_S2_-_01_-_Front.png)

Front view

		- 
			[](./img/RS_PRO_S2_-_02_-_SmuView.png)

S2 connected to SmuView visualizing readings from the power grid

		- 
			[](./img/RS_PRO_S2_-_03.jpg)

Measuring voltage from the power grid

		- 
			[](./img/RS_PRO_S2_-_04_-_Display-Light.jpg)

Display close-up with backlight on

		- 
			[](./img/RS_PRO_S2_-_05_-_Rear.jpg)

Rear view

		- 
			[](./img/RS_PRO_S2_-_06_-_Magnetic_sticker.jpg)

Magnetic sticker close up

		- 
			[](./img/RS_PRO_S2_-_Magnetic_sticker.jpg)

Magnetic sticker inside view

		- 
			[](./img/RS_PRO_S2_-_07.jpg)

Protective sleeve removed

		- 
			[](./img/RS_PRO_S2_-_08_-_Rear.jpg)

Rear

		- 
			[](./img/RS_PRO_S2_-_Teardown_-_01.jpg)

Teardown 1/12

		- 
			[](./img/RS_PRO_S2_-_Teardown_-_02.jpg)

Teardown 2/12

		- 
			[](./img/RS_PRO_S2_-_Teardown_-_03.jpg)

Teardown 3/12

		- 
			[](./img/RS_PRO_S2_-_Teardown_-_04.jpg)

Teardown 4/12

		- 
			[](./img/RS_PRO_S2_-_Teardown_-_05.jpg)

Teardown 5/12

		- 
			[](./img/RS_PRO_S2_-_Teardown_-_06.jpg)

Teardown 6/12

		- 
			[](./img/RS_PRO_S2_-_Teardown_-_07.jpg)

Teardown 7/12

		- 
			[](./img/RS_PRO_S2_-_Teardown_-_08.jpg)

Teardown 8/12

		- 
			[](./img/RS_PRO_S2_-_Teardown_-_09.jpg)

Teardown 9/12

		- 
			[](./img/RS_PRO_S2_-_Teardown_-_10.jpg)

Teardown 10/12

		- 
			[](./img/RS_PRO_S2_-_Teardown_-_11.jpg)

Teardown 11/12

		- 
			[](./img/RS_PRO_S2_-_Teardown_-_12.jpg)

Teardown 12/12

# Tests

Unless noted otherweise, the tests in this section have been performed by [Cymaphore](https://sigrok.org/wiki/User:Cymaphore) on a RS PRO S2, Firmware v2015 / 808

## Usage of rechargable NiMH batteries

The device works acceptable with rechargable batteries. Voltage boundaries are however a bit unsuitablefor NiMH cells, battery cut-off level of 1.14V/cell is to early, even for alkaline cells, this way the full capacity of the cells can not be used.

Battery indication

- FULL: >2.86 V (~ 1.43 V/cell)
- HALF: >2.68 V (~ 1.34 V/cell)
- LOW: >2.46 V (~ >1.23 V/cell)
- WARN: >2.28 V (~1.14 V/cell)
- Forced POWER-OFF: <2.28 V (~ 1.14 V/cell)
## Current consumption

Test supply voltage: 2.4 V

### Details

All functions measured, average value over measurements taken.

- Device active: 2.952 mA
- With Bluetooth LE active in standby: 4.211 mA
- With Bluetooth LE in active data acquisition: 7.538 mA
- With display backlight on: 17.251 mA

If the device is in APO or low battery power off mode, it consumes 9µA.

Based on that numbers, with backlight off the device should be able to surpass the battery duration specified in the datasheet by a lot, making long duration logging sessions possible.

# Resources
- [RS PRO S2 product page](https://www.rsonline-privat.de/Products/ProductDetail/RS-PRO-Digital-Multimeter-1000V-ac-400mA-ac-40M-Bluetooth-Kat-III-Kat-IV-1993847)

## Photos

<div class="photo-grid" markdown>

[![Rs Pro S2 Teardown 03](./img/RS_PRO_S2_-_Teardown_-_03.jpg)](./img/RS_PRO_S2_-_Teardown_-_03.jpg "Rs Pro S2 Teardown 03"){ .glightbox data-gallery="rs-pro-s2" }
<span class="caption">Rs Pro S2 Teardown 03</span>

[![Rs Pro S2 02 Smuview](./img/RS_PRO_S2_-_02_-_SmuView.jpg)](./img/RS_PRO_S2_-_02_-_SmuView.png "Rs Pro S2 02 Smuview"){ .glightbox data-gallery="rs-pro-s2" }
<span class="caption">Rs Pro S2 02 Smuview</span>

[![Rs Pro S2 05 Rear](./img/RS_PRO_S2_-_05_-_Rear.jpg)](./img/RS_PRO_S2_-_05_-_Rear.jpg "Rs Pro S2 05 Rear"){ .glightbox data-gallery="rs-pro-s2" }
<span class="caption">Rs Pro S2 05 Rear</span>

[![Rs Pro S2 08 Rear](./img/RS_PRO_S2_-_08_-_Rear.jpg)](./img/RS_PRO_S2_-_08_-_Rear.jpg "Rs Pro S2 08 Rear"){ .glightbox data-gallery="rs-pro-s2" }
<span class="caption">Rs Pro S2 08 Rear</span>

[![Rs Pro S2 07](./img/RS_PRO_S2_-_07.jpg)](./img/RS_PRO_S2_-_07.jpg "Rs Pro S2 07"){ .glightbox data-gallery="rs-pro-s2" }
<span class="caption">Rs Pro S2 07</span>

[![Rs Pro S2 Teardown 11](./img/RS_PRO_S2_-_Teardown_-_11.jpg)](./img/RS_PRO_S2_-_Teardown_-_11.jpg "Rs Pro S2 Teardown 11"){ .glightbox data-gallery="rs-pro-s2" }
<span class="caption">Rs Pro S2 Teardown 11</span>

[![Rs Pro S2 04 Display Light](./img/RS_PRO_S2_-_04_-_Display-Light.jpg)](./img/RS_PRO_S2_-_04_-_Display-Light.jpg "Rs Pro S2 04 Display Light"){ .glightbox data-gallery="rs-pro-s2" }
<span class="caption">Rs Pro S2 04 Display Light</span>

[![Rs Pro S2 Teardown 01](./img/RS_PRO_S2_-_Teardown_-_01.jpg)](./img/RS_PRO_S2_-_Teardown_-_01.jpg "Rs Pro S2 Teardown 01"){ .glightbox data-gallery="rs-pro-s2" }
<span class="caption">Rs Pro S2 Teardown 01</span>

[![Rs Pro S2 Teardown 04](./img/RS_PRO_S2_-_Teardown_-_04.jpg)](./img/RS_PRO_S2_-_Teardown_-_04.jpg "Rs Pro S2 Teardown 04"){ .glightbox data-gallery="rs-pro-s2" }
<span class="caption">Rs Pro S2 Teardown 04</span>

[![Rs Pro S2 Magnetic Sticker](./img/RS_PRO_S2_-_Magnetic_sticker.jpg)](./img/RS_PRO_S2_-_Magnetic_sticker.jpg "Rs Pro S2 Magnetic Sticker"){ .glightbox data-gallery="rs-pro-s2" }
<span class="caption">Rs Pro S2 Magnetic Sticker</span>

[![Rs Pro S2 Teardown 10](./img/RS_PRO_S2_-_Teardown_-_10.jpg)](./img/RS_PRO_S2_-_Teardown_-_10.jpg "Rs Pro S2 Teardown 10"){ .glightbox data-gallery="rs-pro-s2" }
<span class="caption">Rs Pro S2 Teardown 10</span>

[![Rs Pro S2 06 Magnetic Sticker](./img/RS_PRO_S2_-_06_-_Magnetic_sticker.jpg)](./img/RS_PRO_S2_-_06_-_Magnetic_sticker.jpg "Rs Pro S2 06 Magnetic Sticker"){ .glightbox data-gallery="rs-pro-s2" }
<span class="caption">Rs Pro S2 06 Magnetic Sticker</span>

[![Rs Pro S2 Teardown 08](./img/RS_PRO_S2_-_Teardown_-_08.jpg)](./img/RS_PRO_S2_-_Teardown_-_08.jpg "Rs Pro S2 Teardown 08"){ .glightbox data-gallery="rs-pro-s2" }
<span class="caption">Rs Pro S2 Teardown 08</span>

[![Rs Pro S2 Teardown 05](./img/RS_PRO_S2_-_Teardown_-_05.jpg)](./img/RS_PRO_S2_-_Teardown_-_05.jpg "Rs Pro S2 Teardown 05"){ .glightbox data-gallery="rs-pro-s2" }
<span class="caption">Rs Pro S2 Teardown 05</span>

[![Rs Pro S2 Teardown 09](./img/RS_PRO_S2_-_Teardown_-_09.jpg)](./img/RS_PRO_S2_-_Teardown_-_09.jpg "Rs Pro S2 Teardown 09"){ .glightbox data-gallery="rs-pro-s2" }
<span class="caption">Rs Pro S2 Teardown 09</span>

[![Rs Pro S2 01 Front](./img/RS_PRO_S2_-_01_-_Front.jpg)](./img/RS_PRO_S2_-_01_-_Front.png "Rs Pro S2 01 Front"){ .glightbox data-gallery="rs-pro-s2" }
<span class="caption">Rs Pro S2 01 Front</span>

[![Rs Pro S2 Teardown 12](./img/RS_PRO_S2_-_Teardown_-_12.jpg)](./img/RS_PRO_S2_-_Teardown_-_12.jpg "Rs Pro S2 Teardown 12"){ .glightbox data-gallery="rs-pro-s2" }
<span class="caption">Rs Pro S2 Teardown 12</span>

[![Rs Pro S2 Teardown 02](./img/RS_PRO_S2_-_Teardown_-_02.jpg)](./img/RS_PRO_S2_-_Teardown_-_02.jpg "Rs Pro S2 Teardown 02"){ .glightbox data-gallery="rs-pro-s2" }
<span class="caption">Rs Pro S2 Teardown 02</span>

[![Rs Pro S2 Teardown 06](./img/RS_PRO_S2_-_Teardown_-_06.jpg)](./img/RS_PRO_S2_-_Teardown_-_06.jpg "Rs Pro S2 Teardown 06"){ .glightbox data-gallery="rs-pro-s2" }
<span class="caption">Rs Pro S2 Teardown 06</span>

[![Rs Pro S2 Teardown 07](./img/RS_PRO_S2_-_Teardown_-_07.jpg)](./img/RS_PRO_S2_-_Teardown_-_07.jpg "Rs Pro S2 Teardown 07"){ .glightbox data-gallery="rs-pro-s2" }
<span class="caption">Rs Pro S2 Teardown 07</span>

[![Rs Pro S2 03](./img/RS_PRO_S2_-_03.jpg)](./img/RS_PRO_S2_-_03.jpg "Rs Pro S2 03"){ .glightbox data-gallery="rs-pro-s2" }
<span class="caption">Rs Pro S2 03</span>

</div>
