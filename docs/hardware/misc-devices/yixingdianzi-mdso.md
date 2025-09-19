# Yixingdianzi Mdso
| | | |:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------------------:| | [*Image: \1* | | | Status | supported | | Source code | [hantek-6xxx](http://github.com/OpenTraceLab/?p=OpenTraceCapture.git;a=tree;f=src/hardware/hantek-6xxx) | | Channels | 2 | | Samplerate | 48MHz | | Analog bandwidth | 20MHz | | Vertical resolution | 8bit | | Triggers | none (SW-only) | | Input impedance | 1MΩ‖25pF | | Memory | none | | Display | none | | Connectivity | USB | **YiXingDianZi MDSO** The **YiXingDianZi MDSO** (also known as **Wosontel MDSO**) is a USB-based, 2-channel oscilloscope with an analog bandwidth of 20MS/s and 48MS/s sampling rate. It comes in very compact plastic case (82x65x23mm) without any branding, USB type B input, 2c BNC inputs, and a red LED. The YiXingDianZi manufacturer is probably the same as Instrustar (Chinese characters match, lsusb is almost exactly the same). See *YiXingDianZi MDSO/Info* for more details (such as **lsusb -v** output) on the device.
## Contents
\- *1 Hardware* \- *2 Firmware* \- *2.1 EEPROM layout* \- *3 Photos* \- *4 Resources*
## Hardware \- Cypress FX2LP CY7C68013A-56PVXC (USB 2.0 HS controller) \- ADC: Analog Devices AD9288 \- EEPROM: Microchip 24LC64I (64K I²C EEPROM) \- 2x ST 74HC4051 (8-Channel analog mux) \- Crystal oscillator 24MHz (crystal) \- 4x 145 MHz FastFET op amp: Analog Devices AD8065 (top markings HRA) \- Unmarked DC/DC converter \- 3.3V LDO: AMS1117-3.3 **Cypress FX2 pinout:**  | | | | | | |----------------------------------------------------------------------------------------------------:|----:|-----|-----|---------------------------------------------------------------------------------------------------| | (AD9288 D5B) PD5 | 1- | O | -56 | PD4 (AD9288 D4B) | | (AD9288 D6B) PD6 | 2- | | -55 | PD3 (AD9288 D3B) | | (AD9288 D7B) PD7 | 3- | | -54 | PD2 (AD9288 D2B) | | GND | 4- | | -53 | PD1 (AD9288 D1B) | | CLKOUT | 5- | | -52 | PD0 (AD9288 D0B) | | VCC | 6- | | -51 | \\*WAKEUP | | GND | 7- | | -50 | VCC | | RDY0/\\*SLRD | 8- | | -49 | RESET# | | RDY1/\\*SLWR | 9- | | -48 | GND | | AVCC | 10- | | -47 | PA7 | | (24MHz crystal) XTALOUT | 11- | | -46 | PA6 (CH2 74HC4051 S2) | | (24MHz crystal) XTALIN | 12- | | -45 | PA5 (CH2 74HC4051 S1) | | AGND | 13- | | -44 | PA4 (CH2 74HC4051 S0) | | AVCC | 14- | | -43 | PA3 (CH1 74HC4051 S2) | | (USB D+) DPLUS | 15- | | -42 | PA2 (CH1 74HC4051 S1) | | (USB D-) DMINUS | 16- | | -41 | PA1 (CH1 74HC4051 S0) | | AGND | 17- | | -40 | PA0 | | VCC | 18- | | -39 | VCC | | GND | 19- | | -38 | CTL2 | | (FX2 CTL0) (AD9288 ENCA/B) \\*IFCLK | 20- | | -37 | CTL1 | | RESERVED | 21- | | -36 | CTL0 (AD9288 ENCA/B) (FX2 IFCLK) | | (EEPROM SCL) SCL | 22- | | -35 | GND | | (EEPROM SDA) SDA | 23- | | -34 | VCC | | VCC | 24- | | -33 | GND | | (AD9288 D0A) PB0 | 25- | | -32 | PB7 (AD9288 D7A) | | (AD9288 D1A) PB1 | 26- | | -31 | PB6 (AD9288 D6A) | | (AD9288 D2A) PB2 | 27- | | -30 | PB5 (AD9288 D5A) | | (AD9288 D3A) PB3 | 28- | | -29 | PB4 (AD9288 D4A) |  **ST 74HC4051 (upper/lower, CH1/CH2) pinout**:  CH1 (U13) | CH2 (U10)
---|---
| Y4 | 1- |  O | -16 | VCC
---|---|---|---|---
Y6 | 2- | -15 | Y2 (AD8065 out)
(AD8065 -in, via 1k to GND) Z | 3- | -14 | Y1 (AD8065 out via 1k)
Y7 | 4- | -13 | Y0 (AD8065 out via 3.9k)
Y5 | 5- | -12 | Y3 (AD8065 out via 15k)
(GND) E# | 6- | -11 | S0 (FX2 PA1)
VEE | 7- | -10 | S1 (FX2 PA2)
GND | 8- | -9 | S2 (FX2 PA3)
| Y4 | 1- |  O | -16 | VCC
---|---|---|---|---
Y6 | 2- | -15 | Y2 (AD8065 out)
(AD8065 -in, via 1k to GND) Z | 3- | -14 | Y1 (AD8065 out via 1k)
Y7 | 4- | -13 | Y0 (AD8065 out via 3.9k)
Y5 | 5- | -12 | Y3 (AD8065 out via 15k)
(GND) E# | 6- | -11 | S0 (FX2 PA4)
VEE | 7- | -10 | S1 (FX2 PA5)
GND | 8- | -9 | S2 (FX2 PA6)
**Input stage gain**: | | | | | | | |-----|-----|-----|----------------|-----------------|--------| | S2 | S1 | S0 | 74HC4051D Mux | Gain | VDIVs | | 0 | 0 | 0 | Y0 to Z (3.9k) | 5 (4.9 in fact) | 200mV | | 0 | 0 | 1 | Y1 to Z (1k) | 2 | 500mV | | 0 | 1 | 0 | Y2 to Z (0) | 1 | 1V | | 0 | 1 | 1 | Y3 to Z (15k) | 16 | 62.5mV | **Microchip 24LC64I pinout**:  | | | | | | |-------------------------------------------:|----:|-----|-----|-------------------------------------------------| | (VCC) A0 | 1- | O | -8 | VCC | | (GND) A1 | 2- | | -7 | WP (GND) | | (GND) A2 | 3- | | -6 | SCL (FX2 SCL) | | VSS | 4- | | -5 | SDA (FX2 SDA) |  **Analog Devices AD9288 pinout**: | | | |----------------------------------|----------------------------------------------------------------------------| | AD9288 pins | Description | | S1, S2 | S1=VCC, S2=GND. "Normal operation, data align disabled". | | DFS | Tied to GND. Data format select = "offset binary" (not "twos complement"). | | AINA, AINB | Analog input channels. | | D0A-D7A | Connected to FX2 PB0-PB7. | | D0B-D7B | Connected to FX2 PD0-PD7. | ## Firmware **Note**: The firmware is flashed into the device permanently. ### EEPROM layout The device has a 8KB I²C EEPROM with the following layout: c2 47 05 31 21 00 00 04 XX XX XX XX XX XX .. .. Description: | | | |--------------|----------------------------------------------------------------------------------------| | Bytes | Description | | 0 | **0xc2**: FX2 "c2 load" mode, i.e. VID/PID/DID are loaded from EEPROM as the firmware. | | 1-2 | **0x0547**: USB vendor ID (VID before firmware renumerate). | | 3-4 | **0x2131**: USB product ID (PID before firmware renumerate). | | 5-6 | **0x0000**: USB device ID (DID before firmware renumerate). | | 7 | **0x04**: FX2 configuration byte (see FX2 TRM for details). | | 8-1917h | Firmware. | | 1918h -1fffh | All-0xff. | ## Photos \-
[*Image: \1*
Packaging
\-
[*Image: \1*
Device, top
\-
[*Image: \1*
Inside
\-
[*Image: \1*
PCB, top
\-
[*Image: \1*
PCB, bottom
\-
[*Image: \1*
PCB, USB side
\-
[*Image: \1*
PCB, analog frontend
## Resources \- *Aliexpress page*
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=YiXingDianZi_MDSO&oldid=13986](https://OpenTraceLab.org/w/index.php?title=YiXingDianZi_MDSO&oldid=13986)"
: \- *Device* \- *Oscilloscope* \- *Supported*
## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
