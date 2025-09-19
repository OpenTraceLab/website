# Rs Pro S2
| | | |:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:| | [*Image: \1* | | | Status | in progress | | Source code | [appa-dmm](http://github.com/OpenTraceLab/?p=OpenTraceCapture.git;a=tree;f=src/hardware/appa-dmm) | | Counts | 6000 | | IEC 61010-1 | CAT III (1000V) / CAT IV (600V) | | Connectivity | Bluetooth LE | | Measurements | voltage, frequency, resistance, continuity, diode, capacitance, current, temperature | | Features | autorange, data hold, min/max, relative, non-contact voltage detection hi/lo, backlight, true-rms, data logging, single value storage, auto-v/loz, VFD, built-in magnetic sticker, µA current range | | Website | [rsonline-privat.de](https://www.rsonline-privat.de/Products/ProductDetail/RS-PRO-Digital-Multimeter-1000V-ac-400mA-ac-40M-Bluetooth-Kat-III-Kat-IV-1993847) | **RS PRO S2** The **RS PRO S2** is a 6000 counts, CAT IV (600V) / CAT III (1000V) handheld logging digital multimeter with Bluetooth LE connectivity and long battery duration. It is marketed as a "HVAC Multimeter" (optimized for the needs of heating, ventilation, and air conditioning technicians). It is based on the *APPA S2*, See also: *APPA Multimeters*. A OpenTraceLab-driver supporting these APPA-based devices ("appa-dmm" in OpenTraceLab) has been created and will be included in mainline OpenTraceLab once it passes acception (see developement repository [github.com/Cymaphore/OpenTraceCapture branch appa-dmm](https://github.com/Cymaphore/OpenTraceCapture)).
## Contents
\- *1 Hardware* \- *2 Photos and Teardown* \- *3 Tests* \- *3.1 Usage of rechargable NiMH batteries* \- *3.2 Current consumption* \- *3.2.1 Details* \- *4 Resources*
# Hardware \- **MCU**: [Atmel ATSAML22N18A-U](https://ww1.microchip.com/downloads/en/DeviceDoc/60001465A.pdf) \- **ADC-ID**: [Hycontek HY12P65](http://www.hycontek.com/wp-content/uploads/DS-HY12P65-TC.pdf) \- **BLE-SoC**: [AMICCOM A8105](http://www.amiccom.com.tw/asp_en/product_detail.asp?CATG_ID=15&PRODUCT_ID=84) \- **Fuses**: \- **Current range 400mA**: Amp rating: 0.44A, Voltage rating: 1kV, Interrupting rating: 10kA, Opening: Fast acting, Size: 10mm x 34.9mm \- **Power supply:** 2 x IEC LR6 1.5V (works fine with IEC HR6 1.2V) # Photos and Teardown \-
[*Image: \1*
Front view
\-
[*Image: \1*
S2 connected to SmuView visualizing readings from the power grid
\-
[*Image: \1*
Measuring voltage from the power grid
\-
[*Image: \1*
Display close-up with backlight on
\-
[*Image: \1*
Rear view
\-
[*Image: \1*
Magnetic sticker close up
\-
[*Image: \1*
Magnetic sticker inside view
\-
[*Image: \1*
Protective sleeve removed
\-
[*Image: \1*
Rear
\-
[*Image: \1*
Teardown 1/12
\-
[*Image: \1*
Teardown 2/12
\-
[*Image: \1*
Teardown 3/12
\-
[*Image: \1*
Teardown 4/12
\-
[*Image: \1*
Teardown 5/12
\-
[*Image: \1*
Teardown 6/12
\-
[*Image: \1*
Teardown 7/12
\-
[*Image: \1*
Teardown 8/12
\-
[*Image: \1*
Teardown 9/12
\-
[*Image: \1*
Teardown 10/12
\-
[*Image: \1*
Teardown 11/12
\-
[*Image: \1*
Teardown 12/12
# Tests Unless noted otherweise, the tests in this section have been performed by *Cymaphore* on a RS PRO S2, Firmware v2015 / 808 ## Usage of rechargable NiMH batteries The device works acceptable with rechargable batteries. Voltage boundaries are however a bit unsuitablefor NiMH cells, battery cut-off level of 1.14V/cell is to early, even for alkaline cells, this way the full capacity of the cells can not be used. Battery indication \- FULL: \>2.86 V (~ 1.43 V/cell) \- HALF: \>2.68 V (~ 1.34 V/cell) \- LOW: \>2.46 V (~ \>1.23 V/cell) \- WARN: \>2.28 V (~1.14 V/cell) \- Forced POWER-OFF: \<2.28 V (~ 1.14 V/cell) ## Current consumption Test supply voltage: 2.4 V ### Details All functions measured, average value over measurements taken. \- Device active: 2.952 mA \- With Bluetooth LE active in standby: 4.211 mA \- With Bluetooth LE in active data acquisition: 7.538 mA \- With display backlight on: 17.251 mA If the device is in APO or low battery power off mode, it consumes 9µA. Based on that numbers, with backlight off the device should be able to surpass the battery duration specified in the datasheet by a lot, making long duration logging sessions possible. # Resources \- [RS PRO S2 product page](https://www.rsonline-privat.de/Products/ProductDetail/RS-PRO-Digital-Multimeter-1000V-ac-400mA-ac-40M-Bluetooth-Kat-III-Kat-IV-1993847)
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=RS_PRO_S2&oldid=15934](https://OpenTraceLab.org/w/index.php?title=RS_PRO_S2&oldid=15934)"
: \- *Device* \- *Multimeter* \- *Bluetooth* \- *In progress*
## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
