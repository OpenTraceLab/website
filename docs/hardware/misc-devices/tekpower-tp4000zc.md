# Tekpower Tp4000Zc

| | | |:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------------------:| | [![\1](../../assets/hardware/general/\2)](./File:Tp4000zc_front.png.html) | | | Status | supported | | Source code | [serial-dmm](http://github.com/OpenTraceLab/?p=OpenTraceCapture.git;a=tree;f=src/hardware/serial-dmm) | | Counts | 4000 | | IEC 61010-1 | CAT II (600V) | | Connectivity | [RS232](Device_cables.html#Digitek_DT4000ZC_cable "Device cables") | | Measurements | voltage, resistance, continuity, diode, capacitance, frequency, temperature, current, duty cycle | | Features | autorange, data hold, relative | | Website | [tekpower.us](http://www.tekpower.us) | **TekPower TP4000ZC** The **TekPower TP4000ZC** is a 4000 counts, CAT II (600V) handheld digital multimeter with RS232 connectivity. This multimeter is a rebadged [Digitek DT4000ZC](Digitek_DT4000ZC.html "Digitek DT4000ZC"). 
## Contents 
\- [1 Hardware](TekPower_TP4000ZC.html#Hardware) \- [2 Photos](TekPower_TP4000ZC.html#Photos) \- [3 Protocol](TekPower_TP4000ZC.html#Protocol) \- [4 Resources](TekPower_TP4000ZC.html#Resources) 
## Hardware **Multimeter:** \- **Multimeter IC**: The microcontroller is an unidentifiable plastic blob (based on the communication protocol, probably a [Fortune Semiconductor FS9721_LP3](Multimeter_ICs.html#Fortune_Semiconductor_FS9721_LP3 "Multimeter ICs")) \- LM358 opamp \- HEF4013BT flip-flop \- The RS-232 connector is a standard 3.5m stereo jack, with the ring left unconnected. The transmitter is optically insulated from the rest of the device. **Cable:** \- See [Device_cables#Digitek_DT4000ZC_cable](Device_cables.html#Digitek_DT4000ZC_cable "Device cables"). \- The DB-9 connector has a loopback resistor between the RX and TX pins. ## Photos **Multimeter:** \- 
[![\1](../../assets/hardware/general/\2)](./File:Tp4000zc_angle.png.html)
Device, angle
\- 
[![\1](../../assets/hardware/general/\2)](./File:Tp4000zc_front.png.html)
Mugshot
\- 
[![\1](../../assets/hardware/general/\2)](./File:Tp4000zc_back.jpg.html)
Device, back
\- 
[![\1](../../assets/hardware/general/\2)](./File:Tp4000zc_contents.jpg.html)
Package contents
\- 
[![\1](../../assets/hardware/general/\2)](./File:Tp4000zc_front_nocover.png.html)
Holster removed, front
\- 
[![\1](../../assets/hardware/general/\2)](./File:Tp4000zc_back_nocover.jpg.html)
Holster removed, back
\- 
[![\1](../../assets/hardware/general/\2)](./File:Tp4000zc_batt.jpg.html)
Battery compartment
\- 
[![\1](../../assets/hardware/general/\2)](./File:Tp4000zc_open_back.jpg.html)
Rear cover
\- 
[![\1](../../assets/hardware/general/\2)](./File:Tp4000zc_open_front.jpg.html)
Front cover
\- 
[![\1](../../assets/hardware/general/\2)](./File:Tp4000zc_open_front_noboard.jpg.html)
Rear cover, PCB removed
\- 
[![\1](../../assets/hardware/general/\2)](./File:Tp4000zc_pcb_front.jpg.html)
PCB, front
\- 
[![\1](../../assets/hardware/general/\2)](./File:Tp4000zc_pcb_back.jpg.html)
PCB, back
\- 
[![\1](../../assets/hardware/general/\2)](./File:Tp4000zc_chip.jpg.html)
Chip
\- 
[![\1](../../assets/hardware/general/\2)](./File:Tp4000zc_chip_HEF4013BT.jpg.html)
HEF4013BT flip-flop
\- 
[![\1](../../assets/hardware/general/\2)](./File:Tp4000zc_chip_LM358.jpg.html)
LM358 opamp
\- 
[![\1](../../assets/hardware/general/\2)](./File:Tp4000zc_232_optoisolation.jpg.html)
RS-232 optoisolation
\- 
[![\1](../../assets/hardware/general/\2)](./File:Tp4000zc_232_module.jpg.html)
RS-232 module
\- 
[![\1](../../assets/hardware/general/\2)](./File:Tp4000zc_232_pcb_back.jpg.html)
RS-232 PCB, bottom
\- 
[![\1](../../assets/hardware/general/\2)](./File:Tp4000zc_232_pcb_front.jpg.html)
RS-232 PCB, top
**Cable:** See [Device_cables#Digitek_DT4000ZC_cable](Device_cables.html#Digitek_DT4000ZC_cable "Device cables"). ## Protocol See [Multimeter_ICs#Fortune_Semiconductor_FS9721_LP3](Multimeter_ICs.html#Fortune_Semiconductor_FS9721_LP3 "Multimeter ICs"). User bit 2 is used to indicate temperature measurement in degrees Celsius. ## Resources \- [Video review of TP4000ZC (Part 1/2)](http://www.youtube.com/watch?v=kXzAD74C5As) \- [Video review of TP4000ZC (Part 2/2)](http://www.youtube.com/watch?v=7pbRLom7bNc) \- [TP4000ZC serial protocol](http://www.multimeterwarehouse.com/TP4000ZC/TP4000ZC_serial_protocol.pdf) \- [multimeterwarehouse.com: TP4000ZC](http://www.multimeterwarehouse.com/TP4000ZC.htm) \- [multimeterreviews.com: TekPower TP4000ZC (PC RS232 Interface)](http://www.multimeterreviews.com/tekpower-tp4000zc-pc-based-rs232-interaced-auto-ranging-digital/) \- [mjlorton.com: T4D 22 TekPower TP4000ZC](http://mjlorton.com/forum/index.php?topic=103.0)
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=TekPower_TP4000ZC&oldid=5665](https://OpenTraceLab.org/w/index.php?title=TekPower_TP4000ZC&oldid=5665)" 
[Categories](specialcategories-specialcategories.md): \- [Device](./Category:Device.html "Category:Device") \- [Multimeter](./Category:Multimeter.html "Category:Multimeter") \- [Supported](./Category:Supported.html "Category:Supported")

## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
