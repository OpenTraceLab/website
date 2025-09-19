# Ht Usbee Axpro
**HT USBee-AxPro** [*Image: \1* |
---|---
Status | supported
Source code | [fx2lafw](http://github.com/OpenTraceLab/?p=OpenTraceCapture.git;a=tree;f=src/hardware/fx2lafw)
Channels | 8 + 1
Samplerate | 8ch @ 24MHz, 8+1ch @ 12MHz
Samplerate (state) | —
Triggers | none (SW-only)
Min/max voltage | Digital: -1V — +6V
Analog: ±10V (±20V max)
Threshold voltage | Fixed: VIH=1.6V, VIL=1.4V
Memory | none
Compression | none
Price range | $35 - $45
Website | *aliexpress.com*
**HT USBee-AxPro** The **HT USBee-AxPro** is a USB-based, 8-channel logic analyzer with up to 24MHz sampling rate, with 1 additional analog channel (3MHz analog bandwidth). It is able to switch between USBee AX-Pro, Salea Logic and Altera USB blaster mode via a button. When pressing the button the USB VID/PID changes. It is a clone of the [CWAV USBee AX-Pro](https://OpenTraceLab.org/w/index.php?title=CWAV_USBee_AX-Pro&action=edit&redlink=1 "CWAV USBee AX-Pro \(page does not exist\)"). In OpenTraceLab, we use the open-source *fx2lafw* firmware for this logic analyzer. See *HT USBee-AxPro/Info* for some more details (such as **lsusb -v** output) on the device.
## Contents
\- *1 Hardware* \- *1.1 FX2LP pin mappings* \- *1.2 Analog frontend* \- *1.3 Pin mappings* \- *2 Photos* \- *3 Protocol* \- *4 Resources*
## Hardware **HT2013 V5.00**: \- **Main chip**: [Cypress CY7C68013A-56SSOP (FX2LP)](http://www.cypress.com/?docID=45142) \- **64Kbit I²C EEPROM**: [Microchip 24LC641](http://ww1.microchip.com/downloads/en/DeviceDoc/21189f.pdf) \- **2Kbit I²C EEPROM**: [Microchip 24LC02B](http://ww1.microchip.com/downloads/en/DeviceDoc/21709c.pdf) \- **Auxiliary 8051 chip**: [ST STM8S003F3](http://www.st.com/web/en/resource/technical/document/datasheet/DM00024550.pdf) (used for handling the button) \- **Supply voltage regulator**: Advanced Monolithic Systems AMS1117-3.3 \- **Analog-to-digital converter**: [Texas Instruments TLC5510I](http://www.ti.com/lit/ds/symlink/tlc5510.pdf) \- **Analog input amplifiers**: [Analog Devices AD8065](http://www.analog.com/static/imported-files/data_sheets/AD8065_8066.pdf) (SMD marking "HRA") \- **Analog amplifiers negative supply**: [Intersil ICL7660 (7660 AIBAZ V120428A)](http://www.intersil.com/content/dam/Intersil/documents/icl7/icl7660.pdf) \- **Crystal**: 24MHz ### FX2LP pin mappings | | | | | |-----|--------|-------------|-----------------| | \\# | Pin | Destination | Remark | | | CTL2 | ADC_CLK | ADC clock | | | PD0..7 | ADC_D1..8 | ADC data output | ### Analog frontend **Schematics**: [*Image: \1* **Notes**: \- Some devices have R2 = 66.5Ω (instead of 66.5kΩ), this basically limits the range to -3.3V — +3.3V. \- TLC5510 is used with ~3.3V "reference" from LDO output which is both out of the allowed range and is a major source of inaccuracy. \- Some devices (probably those that do not have U5 populated) produce bogus min and max spikes when measuring certain voltages, this can probably be remedied by adding small (on the order of 10s pF) capacitance to U5 Vcc and GND pins or to the ADC CLK line. **HT_V6.0**: \- ... ### Pin mappings The FX2 CTL2 and PD0..7 pins are mapped exactly like the **HT2013 V5.00** version. The TLC5510I OE# pin is tied to GND. ## Photos **HT2013 V5.00**: \-
[*Image: \1*
Device package
\-
[*Image: \1*
Case, front
\-
[*Image: \1*
Device
\-
[*Image: \1*
PCB, front
\-
[*Image: \1*
PCB, front
\-
[*Image: \1*
PCB, front
\-
[*Image: \1*
PCB, back
\-
[*Image: \1*
TLC5510I
\-
[*Image: \1*
STM8 1
\-
[*Image: \1*
STM8 2
\-
[*Image: \1*
Probe adaptor
\-
[*Image: \1*
FX2
\-
[*Image: \1*
Expansion board
\-
[*Image: \1*
AMS1117
\-
[*Image: \1*
7660
\-
[*Image: \1*
24LC64
\-
[*Image: \1*
24LC02B
\-
[*Image: \1*
Version without signal generator
\-
[*Image: \1*
Version without signal generator case
**HT2013 V5.00 (no blue button PCB)**: \-
[*Image: \1*
Package contents
\-
[*Image: \1*
Device, top
\-
[*Image: \1*
Device, bottom
\-
[*Image: \1*
Connector
\-
[*Image: \1*
USB
\-
[*Image: \1*
Analog connector, top
\-
[*Image: \1*
Analog connector, bottom
\-
[*Image: \1*
Button connector
\-
[*Image: \1*
PCB, top
\-
[*Image: \1*
PCB, bottom
\-
[*Image: \1*
Cypress FX2
\-
[*Image: \1*
ST STM8S003F3
\-
[*Image: \1*
Microchip 24LC64I
\-
[*Image: \1*
Microchip 24LC02BI
\-
[*Image: \1*
Intersil ICL7660
\-
[*Image: \1*
TI TLC5510I
\-
[*Image: \1*
AMS1117-3.3
**HT_V6.0**: \-
[*Image: \1*
Package contents
\-
[*Image: \1*
Device, top
\-
[*Image: \1*
Device, bottom
\-
[*Image: \1*
Connector
\-
[*Image: \1*
USB
\-
[*Image: \1*
Analog adapter, top
\-
[*Image: \1*
Analog adapter, bottom
\-
[*Image: \1*
PCB, top
\-
[*Image: \1*
PCB, bottom
\-
[*Image: \1*
Cypress FX2
\-
[*Image: \1*
Microchip 24LC02B
\-
[*Image: \1*
TI TLC5510I
\-
[*Image: \1*
Intersil ICL7660S
\-
[*Image: \1*
AMS1117-3.3
\-
[*Image: \1*
HRA
\-
[*Image: \1*
24MHz crystal
## Protocol Since we use the open-source *fx2lafw* firmware for this device, we don't need to know the protocol. ## Resources \- [epanorama.net: HT-USBee AxPro review](http://www.epanorama.net/newepa/2014/06/17/ht-usbee-axpro-review/) \- *Itead: Saleae8 / USBEE AX PRO / Altera Combination: Logic Analyzer*
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=HT_USBee-AxPro&oldid=14406](https://OpenTraceLab.org/w/index.php?title=HT_USBee-AxPro&oldid=14406)"
: \- *Device* \- *Logic analyzer* \- *Oscilloscope* \- *Mixed-signal oscilloscope* \- *Supported*
## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
