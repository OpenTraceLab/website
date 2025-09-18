# Voltcraft Vc 96

| | | |:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------------------:| | [![\1](../../assets/hardware/general/\2)](./File:Voltcraft_vc96_mugshot.png.html) | | | Status | supported | | Source code | [serial-dmm](http://github.com/OpenTraceLab/?p=OpenTraceCapture.git;a=tree;f=src/hardware/serial-dmm) | | Counts | 4000 | | Connectivity | RS232 | | Measurements | voltage, capacitance, continuity, diode, frequency, current, | | Features | autorange, hold, relative, min-max, hfe, bargraph | | Website | [kappenberg.com](http://www.kappenberg.com/pages/wandler/gat048.htm) | **Voltcraft VC-96** The **Voltcraft VC-96** is an 4000 counts handheld, digital multimeter with RS232 (D-sub, DB-25 connector) connectivity. 
## Contents 
\- [1 Hardware](Voltcraft_VC-96.html#Hardware) \- [2 Photos](Voltcraft_VC-96.html#Photos) \- [3 Protocol](Voltcraft_VC-96.html#Protocol) \- [4 Resources](Voltcraft_VC-96.html#Resources) 
## Hardware ## Photos \- 
[![\1](../../assets/hardware/general/\2)](./File:Voltcraft_vc96_top.jpg.html)
Device, top
\- 
[![\1](../../assets/hardware/general/\2)](./File:Voltcraft_vc96_back.jpg.html)
Device, bottom
\- 
[![\1](../../assets/hardware/general/\2)](./File:Voltcraft_vc96_left_with_adapter.jpg.html)
Device, left
\- 
[![\1](../../assets/hardware/general/\2)](./File:Voltcraft_vc96_pcb_front.jpg.html)
PCB, top
\- 
[![\1](../../assets/hardware/general/\2)](./File:Voltcraft_vc96_pcb_back.jpg.html)
PCB, bottom
\- 
[![\1](../../assets/hardware/general/\2)](./File:Voltcraft_vc96_main_chip.jpg.html)
Main chip
\- 
[![\1](../../assets/hardware/general/\2)](./File:Voltcraft_vc96_front_rectifier_under_shunt.jpg.html)
Rectifier
\- 
[![\1](../../assets/hardware/general/\2)](./File:Voltcraft_vc96_chip_top_right.jpg.html)
Chip, top
\- 
[![\1](../../assets/hardware/general/\2)](./File:Voltcraft_vc96_chip_left.jpg.html)
Chip, left
\- 
[![\1](../../assets/hardware/general/\2)](./File:Voltcraft_vc96_chip_led_center.jpg.html)
Chip, LED
\- 
[![\1](../../assets/hardware/general/\2)](./File:Voltcraft_vc96_chip_front_top_left.jpg.html)
Chip
\- 
[![\1](../../assets/hardware/general/\2)](./File:Voltcraft_vc96_chip_front_bottom_right.jpg.html)
Chip
\- 
[![\1](../../assets/hardware/general/\2)](./File:Voltcraft_vc96_usb_modification.jpg.html)
USB modification
\- 
[![\1](../../assets/hardware/general/\2)](./File:Voltcraft_vc96_usb_micro_instead_subd25.jpg.html)
Micro-USB instead of DB-25
\- 
[![\1](../../assets/hardware/general/\2)](./File:Voltcraft_vc96_usb_modification_schematics.png.html)
Modification schematics
## Protocol The device sends always (without request) about 4 telegrams per second with 1200 baud, 8N2 over the LED through the case. The location of the LED is marked on the back (the little circle above the screw). The converter originally has a RS232 25pin sub-d and needs an 9VDC power supply, but can be modified with a little TTL serial to USB board. The handling remains the same except using /dev/ttyUSBx instead of /dev/ttySx. Example packets:  ACV 0.0 V\r\n ACV 0.00 V\r\n DCV 00uV\r\n DCV 0.0 V\r\n DCV- 0.1mV\r\n OHM OL M<0xEA>\r\n DIO OL V\r\n BEP OL K<0xEA>\r\n DIO OL V\r\n DCA 00uA\r\n hfe 0.0 \r\n DCA 02uA\r\n DCA 0.0mA\r\n DCA 00mA\r\n ACA 761mA\r\n ACA 0.0mA\r\n  The device does not send packets in CAP and in FREQ mode. ## Resources \- [kappenberg.com: Basic device info](http://www.kappenberg.com/pages/wandler/gat048.htm)
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=Voltcraft_VC-96&oldid=14680](https://OpenTraceLab.org/w/index.php?title=Voltcraft_VC-96&oldid=14680)" 
[Categories](specialcategories-specialcategories.md): \- [Device](./Category:Device.html "Category:Device") \- [Multimeter](./Category:Multimeter.html "Category:Multimeter") \- [Supported](./Category:Supported.html "Category:Supported")

## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
