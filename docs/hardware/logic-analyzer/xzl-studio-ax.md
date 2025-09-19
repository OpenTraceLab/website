# Xzl Studio Ax
**XZL_Studio AX** [*Image: \1* |
---|---
Status | supported
Source code | [fx2lafw](http://github.com/OpenTraceLab/?p=OpenTraceCapture.git;a=tree;f=src/hardware/fx2lafw)
Channels | 8 + 1
Samplerate | 8ch @ 24MHz, 8+1ch @ 12MHz
Samplerate (state) | —
Triggers | 1 independent trigger + (SW-probe 0,1)
Min/max voltage | Digital: max. 5.5V
Analog: -10V — +10V
Threshold voltage | Digital: Fixed: VIH=1.4V, VIL=0.8V
Memory | none
Compression | none
Price range | $20 - 35
Website | *hotmcu.com*
**XZL_Studio AX** The **XZL_Studio AX** is a USB-based, 8-channel logic analyzer with up to 24MHz sampling rate, with 1 additional analog channel (theoretically 2, but only one of them can be used at a time; 3MHz analog bandwidth). It is a clone of the [CWAV USBee AX-Pro](https://OpenTraceLab.org/w/index.php?title=CWAV_USBee_AX-Pro&action=edit&redlink=1 "CWAV USBee AX-Pro \(page does not exist\)"). In OpenTraceLab, we use the open-source *fx2lafw* firmware for this logic analyzer. **Note**: *fx2lafw* currently doesn't support switching between the two possible analog channels, 1ACH (TODO: not verified on hardware) will be used unconditionally. See *XZL_Studio AX/Info* for some more details (such as **lsusb -v** output) on the device.
## Contents
\- *1 Hardware* \- *2 Photos* \- *3 Protocol* \- *4 Resources*
## Hardware \- **Main chip**: Cypress CY7C68013A-56LTXC (FX2LP), U6 \- **ADC**: 1x Texas Instruments TLC5510I (SO 24pin package), 8-Bit, 20 MSPS ADC, Single Channel, U10, outputs D1-D8 connected to PD0-PD7, OE# grounded, CLOCK from CTL2 on U6 \- **I2C EEPROM**: Atmel 24C02C \- **Low-dropout voltage regulator**: Advanced Monolithic Systems AMS1117-3.3 \- **Crystal**: 24MHz \- **Multiplexer**: HCF4051 - Single 8-Channel Analog Multiplexer/Demultiplexer, U12, channel selectors B and C grounded, selector A controlled by PA0 on U6 \- **Op Amp**: LM358 - Single Supply Dual Operational Amplifiers, U15 \- ... ## Photos \-
[*Image: \1*
Device, front
\-
[*Image: \1*
Probe port
\-
[*Image: \1*
USB port
\-
[*Image: \1*
Device, back
\-
[*Image: \1*
PCB, top
\-
[*Image: \1*
PCB, bottom
\-
[*Image: \1*
Probe clips
## Protocol Since we use the open-source *fx2lafw* firmware for this device, we don't need to know the protocol. ## Resources \- *EE Electronics ESLA201A* - the same circuit (from firmware's point of view). PCB has been copied and altered, same silkscreen labels. No electrolytic caps, no resistive trimmers, larger screw-hole-keepouts, no cap on pin 13 at U10, no U13 (second MAX1044/ICL7660). Has extra button inside the box!
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=XZL_Studio_AX&oldid=14405](https://OpenTraceLab.org/w/index.php?title=XZL_Studio_AX&oldid=14405)"
: \- *Device* \- *Logic analyzer* \- *Oscilloscope* \- *Mixed-signal oscilloscope* \- *Supported*
## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
