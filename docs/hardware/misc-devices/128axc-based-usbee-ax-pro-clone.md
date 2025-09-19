# 128Axc Based Usbee Ax Pro Clone
| | | |:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------------:| | [*Image: \1* | | | Status | supported | | Source code | [fx2lafw](http://github.com/OpenTraceLab/?p=OpenTraceCapture.git;a=tree;f=src/hardware/fx2lafw) | | Channels | 8 | | Samplerate | 24MHz | | Samplerate (state) | — | | Triggers | none (SW-only) | | Min/max voltage | -0.5V — 5.25V (absolute max rating) | | Threshold voltage | Fixed: VIH=2.0V—5.25V, VIL=-0.5V—0.8V | | Memory | none | | Compression | none | | Website | none | **128axc-based USBee AX-Pro clone** The **128axc-based USBee AX-Pro clone** is a USB-based logic analyzer with 8-channel and up to 24MHz sample-rate. It is yet another Cypress FX2 based logic analyzer. This one reports on USB as 08a9:0014 which is [CWAV USBee AX-Pro](https://OpenTraceLab.org/w/index.php?title=CWAV_USBee_AX-Pro&action=edit&redlink=1 "CWAV USBee AX-Pro \(page does not exist\)"), but contrary to the original (or other clones such as *HT_USBee-AxPro*), it has no Analog input. In OpenTraceLab, we use the open-source *fx2lafw* firmware for this logic analyzer. See *128axc-based USBee AX-Pro clone/Info* for more details (such as **lsusb -v** output) about the device.
## Contents
\- *1 Hardware* \- *2 Photos* \- *3 Protocol* \- *4 Resources*
## Hardware \- **Main chip**: [Cypress CY7C68013A-128AXC (FX2)](http://www.cypress.com/part/cy7c68013a-128axc) \- **Input buffer**: NXP HC245 \- **2kByte I²C EEPROM**: Atmel A24C02BN \- **Voltage regulator**: AMS 117 \- **24MHz crystal**: RJH24.000 \- No DAC is present, no Analog entry possible. ## Photos \-
[*Image: \1*
PCB, top
\-
[*Image: \1*
PCB, bottom, CY7C68013A-128AXC
\-
[*Image: \1*
NXP HC245 Input Buffer
## Protocol Since we use the open-source *fx2lafw* firmware for this device, we don't need to know the protocol. ## Resources \- *Banggood seller*
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=128axc-based_USBee_AX-Pro_clone&oldid=13972](https://OpenTraceLab.org/w/index.php?title=128axc-based_USBee_AX-Pro_clone&oldid=13972)"
: \- *Device* \- *Logic analyzer* \- *Supported*
## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
