# Hantek 6022Be
| | | |:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------------------:| | [*Image: \1* | | | Status | supported | | Source code | [hantek-6xxx](http://github.com/OpenTraceLab/?p=OpenTraceCapture.git;a=tree;f=src/hardware/hantek-6xxx) | | Channels | 2 | | Samplerate | 48MHz | | Analog bandwidth | 20MHz | | Vertical resolution | 8bit | | Triggers | none (SW-only) | | Input impedance | 1MΩ‖25pF | | Memory | none | | Display | none | | Connectivity | USB | | Website | *hantek.com* | **Hantek 6022BE** The **Hantek 6022BE** is a USB-based, 2-channel oscilloscope with an analog bandwidth of 20MS/s and 48MS/s sampling rate. See *Hantek 6022BE/Info* for more details (such as **lsusb -v** output) about the device.
## Contents
\- *1 Hardware* \- *2 Photos* \- *3 Protocol* \- *4 Firmware* \- *5 Resources*
## Hardware \- **USB**: [Cypress CY7C68013A-100AXC](http://www.cypress.com/documentation/datasheets/cy7c68013a-cy7c68014a-cy7c68015a-cy7c68016a-ez-usb-fx2lp-usb) (FX2LP) ([datasheet](http://www.cypress.com/file/138911/download)) \- **256-byte I²C EEPROM**: [Microchip 24LC02BI](http://www.microchip.com/wwwproducts/en/24LC02B) ([datasheet](http://ww1.microchip.com/downloads/en/DeviceDoc/21709J.pdf)) \- 2x **8-channel analog multiplexer/demultiplexer**: *NXP 74HC4051D* ([datasheet](http://assets.nexperia.com/documents/data-sheet/74HC_HCT4051.pdf)) \- **1A low-dropout voltage regulator (3.3V):** *Advanced Monolithic Systems AMS1117-3.3* ([datasheet](http://www.advanced-monolithic.com/pdf/ds1117.pdf)) \- **2W, fixed input, isolated & unregulated dual/single output DC/DC converter**: *Mornsun A_S-2WR2 (A0505S-2WR2)* ([datasheet](http://www.mornsun.cn/uploads/pdf/A_S-2WR2.pdf)) \- **8-bit, 40/80/100MHz, dual ADC**: *Analog Devices AD9288* ([datasheet](http://www.analog.com/media/en/technical-documentation/data-sheets/AD9288.pdf)) \- 4x **145 MHz FastFET Op Amp**: *Analog Devices AD8065* ([datasheet](http://www.analog.com/media/en/technical-documentation/data-sheets/AD8065-KGD-CHIP.pdf)) \- **Crystal**: 24MHz **NXP 74HC4051D (upper/lower, CH1/CH2) pinout**:  | (GND) Y4 | 1- |  O | -16 | VCC
---|---|---|---|---
(GND) Y6 | 2- | -15 | Y2
Z | 3- | -14 | Y1
(GND) Y7 | 4- | -13 | Y0
(GND) Y5 | 5- | -12 | Y3
(GND) E# | 6- | -11 | S0 (FX2 PC2)
VEE | 7- | -10 | S1 (FX2 PC3)
GND | 8- | -9 | S2 (FX2 PC4)
| (GND) Y4 | 1- |  O | -16 | VCC
---|---|---|---|---
(GND) Y6 | 2- | -15 | Y2
Z | 3- | -14 | Y1
(GND) Y7 | 4- | -13 | Y0
(GND) Y5 | 5- | -12 | Y3
(GND) E# | 6- | -11 | S0 (FX2 PC5)
VEE | 7- | -10 | S1 (FX2 PC6)
GND | 8- | -9 | S2 (FX2 PC7)
| | | | | | |-----|-----|-----|---------------|-------------------------| | S2 | S1 | S0 | 74HC4051D Mux | VDIVs (vendor software) | | 0 | 0 | 0 | Y0 to Z | 200mV | | 0 | 0 | 1 | Y1 to Z | 500mV | | 0 | 1 | 0 | Y2 to Z | 5V, 2V, 1V | | 0 | 1 | 1 | Y3 to Z | 100mV, 50mV, 20mV | **Microchip 24LC02BI pinout**:  | | | | | | |--------------------------------------------------------:|----:|-----|-----|-------------------------------------------------| | (Low, but not GND) A0 | 1- | O | -8 | VCC | | (GND) A1 | 2- | | -7 | WP (GND) | | (GND) A2 | 3- | | -6 | SCL (FX2 SCL) | | VSS | 4- | | -5 | SDA (FX2 SDA) |  **Analog Devices ADS9288 pinout**: | | | |----------------------------------|----------------------------------------------------------------------------| | AD9288 pins | Description | | S1, S2 | S1=VCC, S2=GND. "Normal operation, data align disabled". | | DFS | Tied to GND. Data format select = "offset binary" (not "twos complement"). | | AINA, AINB | Analog input channels. | **Cypress FX2 pinout**:  FX2 pins | Description
---|---
CTL2 | Connected to AD9288 ENCA and ENCB and FX2 IFCLK.
PB0-PB7 | Connected to AD9288 D0A-D7A.
PD0-PD7 | Connected to AD9288 D0B-D7B.
PA7 | 1kHz probe calibration pin.
PC0/PC1 | Dual-color (red/green) LED.  | PC1 | PC0 | LED
---|---|---
0 | 0 | ?
0 | 1 | green
1 | 0 | red
1 | 1 | off
## Photos \-
[*Image: \1*
Box
\-
[*Image: \1*
Accessories
\-
[*Image: \1*
Probes
\-
[*Image: \1*
Device, top
\-
[*Image: \1*
Device, bottom
\-
[*Image: \1*
Device, connectors
\-
[*Image: \1*
Device, USB
\-
[*Image: \1*
PCB, top
\-
[*Image: \1*
PCB, bottom
\-
[*Image: \1*
Input stage
\-
[*Image: \1*
Cypress FX2LP
\-
[*Image: \1*
Microchip 24LC02BI
\-
[*Image: \1*
NXP 74HC4051D
\-
[*Image: \1*
AMS AMS1117
\-
[*Image: \1*
Mornsun A0505S-2WR
**Another teardown**: \-
[*Image: \1*
Device, top
\-
[*Image: \1*
PCB, top
\-
[*Image: \1*
PCB, bottom
\-
[*Image: \1*
Feedback resistor selector
\-
[*Image: \1*
Cypress FX2LP
## Protocol | | | | |------------------------|----------------|--------------------------------------------------------------------------| | Oscilloscope command | bRequest value | Notes | | Set CH0 voltage range | 0xE0 | Possible values: 1, 2, 5, 10 (5V, 2.5V, 1V, 500mV). | | Set CH1 voltage range | 0xE1 | Possible values: 1, 2, 5, 10 (5V, 2.5V, 1V, 500mV). | | Set sampling rate | 0xE2 | Possible values: 48, 30, 24, 16, 8, 4, 1 (MHz) and 50, 20, 10 (\\*10kHz). | | Trigger oscilloscope | 0xE3 | Possible values: 1 == start sampling. 0 == ignored currently. | | Set number of channels | 0xE4 | Possible values: 1, 2. | ## Firmware In order to use this device, the *OpenTraceLab-firmware-fx2lafw* (\>= 0.1.4) firmware is required. The firmware was originally written by Jochen Hoenicke (see [README](http://github.com/OpenTraceLab/?p=OpenTraceLab-firmware-fx2lafw.git;a=blob;f=README) for details), thanks a lot! **Note**: The firmware is **not** flashed into the device permanently! You only need to make it available in the usual place where *OpenTraceCapture* looks for firmware files, it will be used automatically (and "uploaded" to the Cypress FX2's SRAM every time you attach the device to a USB port). **Note**: On Windows, you will have to *assign the WinUSB driver via Zadig* **twice**: the first time for the initial USB VID/PID the device has when attaching it via USB (04b4:6022 or 04b5:6022, depending on which vendor driver is currently being used by the device), and a second time after the firmware has been uploaded to the device and the device has "renumerated" with a different VID/PID pair (1d50:608e). ## Resources \- [Vendor software and manuals](http://1drv.ms/1gWOsUF) \- [openhantek.org forum: Protocol info](https://web.archive.org/web/20140422004136/http://www.openhantek.org/forum/topic/4/13/)
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=Hantek_6022BE&oldid=14941](https://OpenTraceLab.org/w/index.php?title=Hantek_6022BE&oldid=14941)"
: \- *Device* \- *Oscilloscope* \- *Supported*
## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
