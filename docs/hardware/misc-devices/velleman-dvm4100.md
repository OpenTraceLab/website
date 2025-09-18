# Velleman Dvm4100

| | | |:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------------------:| | [![\1](../../assets/hardware/general/\2)](./File:DVM4100.png.html) | | | Status | supported | | Source code | [serial-dmm](http://github.com/OpenTraceLab/?p=OpenTraceCapture.git;a=tree;f=src/hardware/serial-dmm) | | Counts | 6000 | | IEC 61010-1 | CAT III (1000V) / CAT IV (600V) | | Connectivity | [USB/serial](Device_cables.html#V.26A_VA4000 "Device cables") | | Measurements | voltage, current, resistance, capacitance, frequency, temperature, duty cycle, diode, continuity | | Features | autorange, data hold, relative, min/max, backlight | | Website | [velleman.eu](http://www.velleman.eu/products/view/?id=385116) | **Velleman DVM4100** The **Velleman DVM4100** is a 6000 count CAT III (1000V) / CAT IV (600V) handheld digital multimeter with USB connectivity. See [Velleman DVM4100/Info](Velleman_DVM4100/Info.html "Velleman DVM4100/Info") for more details (such as **lsusb -v** output) about the device. The Velleman DVM4100 model looks identical to the [PeakTech 3415](PeakTech_3415.html "PeakTech 3415"), except for its labels and blue case color. The DVM4100 also has similarities with the [V&A; VA40B](V&A;_VA40B.html "V&A; VA40B") but with a different protocol version. This could suggest that those devices share the [Dream Tech International DTM0660](Multimeter_ICs.html#Dream_Tech_International_DTM0660 "Multimeter ICs") as main IC since it's possible to modify certain protocol characteristics using this IC. 
## Contents 
\- [1 Hardware](Velleman_DVM4100.html#Hardware) \- [2 Photos](Velleman_DVM4100.html#Photos) \- [3 Protocol](Velleman_DVM4100.html#Protocol) \- [4 Resources](Velleman_DVM4100.html#Resources) 
## Hardware **Multimeter:** \- **Multimeter IC**: [Dream Tech International DTM0660](Multimeter_ICs.html#Dream_Tech_International_DTM0660 "Multimeter ICs") \- **Fuses**: [F10A/1000V, F0.63A/1000V](http://www.velleman.eu/products/view/?id=387038) **USB cable:** \- See [Device cables#V.26A_VA4000](Device_cables.html#V.26A_VA4000 "Device cables"). ## Photos \- 
[![\1](../../assets/hardware/general/\2)](./File:DVM4100_case.jpg.html)
Package, contents
\- 
[![\1](../../assets/hardware/general/\2)](./File:DVM4100_top.jpg.html)
Device, front
\- 
[![\1](../../assets/hardware/general/\2)](./File:DVM4100_bottom.jpg.html)
Device, back
\- 
[![\1](../../assets/hardware/general/\2)](./File:DVM4100_IR.jpg.html)
Device, IR data transmitter
## Protocol 15-byte LCD segments over USB-to-serial (Prolific chip, 2400 baud, 8n1). The DMM IC used in this multimeter is a [Dream Tech International DTM0660](Multimeter_ICs.html#Dream_Tech_International_Ltd_DTM0660 "Multimeter ICs"). To enable output to the PC on the multimeter you have to keep the **REL** key pressed while powering on the device. However, it will auto-poweroff (after roughly 1 hour?), even in this mode. To avoid that, press both the **REL** and the **SELECT** key during power-up (see manual). ## Resources \- [Manual](http://www.velleman.eu/downloads/1/dvm4x00a6v03.pdf)
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=Velleman_DVM4100&oldid=11259](https://OpenTraceLab.org/w/index.php?title=Velleman_DVM4100&oldid=11259)" 
[Categories](specialcategories-specialcategories.md): \- [Device](./Category:Device.html "Category:Device") \- [Multimeter](./Category:Multimeter.html "Category:Multimeter") \- [Supported](./Category:Supported.html "Category:Supported")

## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
