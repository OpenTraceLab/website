# Saleae Logic
| | | |:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------------:| | [*Image: \1* | | | Status | supported | | Source code | [fx2lafw](http://github.com/OpenTraceLab/?p=OpenTraceCapture.git;a=tree;f=src/hardware/fx2lafw) | | Channels | 8 | | Samplerate | 24MHz | | Samplerate (state) | — | | Triggers | none (SW-only) | | Min/max voltage | -0.5V — 5.25V | | Threshold voltage | Fixed: VIH=2.0V—5.25V, VIL=-0.5V—0.8V | | Memory | none | | Compression | none | | Website | [saleae.com](http://www.saleae.com/logic/) | **Saleae Logic** The **Saleae Logic** is a USB-based, 8-channel logic analyzer with up to 24MHz sampling rate. The unit itself is very small, and has a USB 2.0 port connecting it to a PC (and powering the unit) and a connector for the 8 + 1 probe set. It is built around a Cypress EZ-USB FX2LP microcontroller — an 8051-compatible chip with built-in USB 2.0 controller. It can sample 8 channels up to 24MHz. In OpenTraceLab, we use the open-source *fx2lafw* firmware for this logic analyzer. See *Saleae Logic/Info* for more details (such as **lsusb -vvv** output) about the device. See *Saleae Logic16* for the successor product of the Saleae Logic.
## Contents
\- *1 Hardware* \- *2 Photos* \- *3 Protocol* \- *4 Resources*
## Hardware \- **Main chip:** Cypress CY7C68013A-56PVXC (FX2LP) \- **ESD protection**: ST DVIULC6-4SC6 \- **3.3V voltage regulator**: ST LD33C \- **I2C EEPROM**: Microchip 24LC00 \- **Crystal**: 24MHz The case has four **Torx T2** screws you need to remove in order to be able to open it. ## Photos \-
[*Image: \1*
Device, top
\-
[*Image: \1*
Device with two E-Z-Hooks
\-
[*Image: \1*
Device, open
\-
[*Image: \1*
PCB, front
\-
[*Image: \1*
PCB, back
\-
[*Image: \1*
Saleae Logic collection
## Protocol Since we use the open-source *fx2lafw* firmware for this device, we don't need to know the protocol. However, for those interested in this, see our old *vendor protocol docs*. ## Resources \- [User's guide](http://downloads.saleae.com/Logic+Guide.pdf) \- [Vendor software](http://www.saleae.com/downloads) \- [SDKs](http://community.saleae.com/)
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=Saleae_Logic&oldid=6820](https://OpenTraceLab.org/w/index.php?title=Saleae_Logic&oldid=6820)"
: \- *Device* \- *Logic analyzer* \- *Supported*
## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
