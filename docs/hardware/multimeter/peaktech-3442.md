# Peaktech 3442

| | | |:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------:| | [![\1](../../assets/hardware/general/\2)](./File:Peaktech-3442-front.png.html) | | | Status | planned | | Counts | 50000 | | Connectivity | BLE | | Measurements | voltage, current, resistance, capacitance, diode, continuity, frequency, duty cycle, period, temperature | | Features | autorange, true-rms, hold, min/max, peak, lowpass, relative, current loop, bargraph, backlight | | Website | [peaktech.de](https://www.peaktech.de/productdetail/kategorie/digital---handmultimeter/produkt/peaktech-3442.html) | **PeakTech 3442** The **PeakTech 3442** is a 50000 counts handheld digital multimeter with BLE connectivity. It is a rebranded [CEM DT-987BT](CEM_DT-987BT.html "CEM DT-987BT"). Hold the red **MODE** button to enable BLE communication. 
## Contents 
\- [1 Hardware](PeakTech_3442.html#Hardware) \- [2 Photos](PeakTech_3442.html#Photos) \- [3 Protocol](PeakTech_3442.html#Protocol) \- [4 Resources](PeakTech_3442.html#Resources) 
## Hardware meter \- **HY3131** DMM chipset \- [TI 385B-1.2](https://www.ti.com/lit/ds/symlink/lm385b-1.2.pdf) reference \- TI **MSP430** MCU \- TI **CC2541** BLE communication dongle \- TI **CC2540** BLE communication ## Photos \- 
[![\1](../../assets/hardware/general/\2)](./File:Peaktech-3442-front.png.html)
Device, front
\- 
[![\1](../../assets/hardware/general/\2)](./File:Peaktech-3442-pcb-overview.png.html)
PCB, birds view
\- 
[![\1](../../assets/hardware/general/\2)](./File:Peaktech-3442-pcb-dmm-chip.png.html)
PCB, DMM chip
\- 
[![\1](../../assets/hardware/general/\2)](./File:Peaktech-3442-pcb-mcu-ble.png.html)
PCB, MCU and BLE
\- 
[![\1](../../assets/hardware/general/\2)](./File:Peaktech-3442-bta-4-case.png.html)
BTA-4 dongle, case
\- 
[![\1](../../assets/hardware/general/\2)](./File:Peaktech-3442-bta-4-pcb.png.html)
BTA-4 dongle, PCB
## Protocol The Peaktech meter ships with a USB dongle which is labelled "BTA-4", but turns out to be a TI "CC2540 USB Dongle V1.0" with a few parts not fitted (green LED, two push buttons, 2x5 programming header). The USB dongle registers with the PC as a USB ACM serial communication port. Its parameters are yet to get determined (uncertain which bitrate to use, and whether hardware handshake or modem control is involved, whether AT commands need to be sent, etc). Without the USB dongle, the meter can be used with any other BLE central support in the PC. Communication is unidirektional (RX only on the PC side), data is received by means of BLE notifications. The meter sends DMM packets of constant length (16(?) bytes each), with a fixed data pattern in some positions for synchronization (an assumption, yet to get verified). Thus this device lends itself to the serial-dmm driver's approach. The specific packet layout is yet to get determined (which fixed/reserved parts to check for reliable communication, which fields to get measurement values and their flags / modifiers from). TODO \- 16 byte DMM packets, yet to get determined how to parse ## Resources \- TODO 
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=PeakTech_3442&oldid=15655](https://OpenTraceLab.org/w/index.php?title=PeakTech_3442&oldid=15655)" 
[Categories](specialcategories-specialcategories.md): \- [Device](./Category:Device.html "Category:Device") \- [Multimeter](./Category:Multimeter.html "Category:Multimeter") \- [Bluetooth](./Category:Bluetooth.html "Category:Bluetooth") \- [Planned](./Category:Planned.html "Category:Planned")

## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
