# Sparkfun 70C

| | | |:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------------------:| | [![\1](../../assets/hardware/general/\2)](./File:Sparkfun_70c_mugshot.png.html) | | | Status | supported | | Source code | [serial-dmm](http://github.com/OpenTraceLab/?p=OpenTraceCapture.git;a=tree;f=src/hardware/serial-dmm) | | Counts | 6000 | | IEC 61010-1 | CAT II | | Connectivity | USB (standard cable) | | Measurements | voltage, current, resistance, continuity, diode, capacitance, frequency, temperature | | Features | max/min, data hold, relative, backlight | | Website | [sparkfun.com](https://www.sparkfun.com/products/12967) | **SparkFun 70C** The **SparkFun 70C** is a 6000 counts, CAT II handheld digital multimeter with USB connectivity. It appears to be heavily based on the [Victor 70C](Victor_70C.html "Victor 70C"), but with a USB to serial adapter instead of a USB HID device adapter, and different trimpot adjustments. 
## Contents 
\- [1 Hardware](SparkFun_70C.html#Hardware) \- [2 Photos](SparkFun_70C.html#Photos) \- [3 Protocol](SparkFun_70C.html#Protocol) \- [4 Resources](SparkFun_70C.html#Resources) 
## Hardware \- [Fortune Semiconductor FS9922-DMM4](http://www.ic-fortune.com/upload/Download/FS9922-DMM4-DS-11_EN.pdf) multimeter chip \- [Silicon Labs CP2102 USB to Serial adapter](https://octopart.com/cp2102-gm-silicon+labs-519902) **Unverified hardware (some parts on PCB are not clear enough to read; assumptions based on Victor 70C)**: \- [NXP HEF4066BT](http://datasheet.octopart.com/HEF4066BT-Philips-datasheet-87533.pdf) quadruple bilateral switches \- [Microchip TC7660E](http://datasheet.octopart.com/TC7660EOA-Microchip-datasheet-1009.pdf) charge pump DC-to-DC voltage converter \- [Texas Instruments 27L2C](http://datasheet.octopart.com/TLC27L2CP-Texas-Instruments-datasheet-151061.pdf) precision dual op-amp **Note**: The USB/HID chip is *in the multimeter* (not in the USB cable/connector) for this device. The device is connected to the PC using a standard USB cable (without any internal logic/chip). ## Photos \- 
[![\1](../../assets/hardware/general/\2)](./File:SparkFun_70C_mugshot.jpeg.html)
Device, front
\- 
[![\1](../../assets/hardware/general/\2)](./File:SparkFun_70C_PCB_Top.jpeg.html)
PCB, top
\- 
[![\1](../../assets/hardware/general/\2)](./File:SparkFun_70C_PCB_Bottom.jpeg.html)
PCB, bottom
\- 
[![\1](../../assets/hardware/general/\2)](./File:SparkFun_70C_LCD_controller.jpeg.html)
DMM/LCD chip
\- 
[![\1](../../assets/hardware/general/\2)](./File:SparkFun_70C_LCD.jpeg.html)
LCD
\- 
[![\1](../../assets/hardware/general/\2)](./File:SparkFun_70C_highly_generic_packaging.jpeg.html)
Package
\- 
[![\1](../../assets/hardware/general/\2)](./File:SparkFun_70C_unboxed.jpeg.html)
Package contents
## Protocol See [FS9922-DMM4](Multimeter_ICs.html#Fortune_Semiconductor_FS9922-DMM4). ## Resources \- [Manual](https://cdn.sparkfun.com/datasheets/Tools/601e-070c-000abw.pdf) \- [Vendor software](https://cdn.sparkfun.com/datasheets/Tools/setup_70c_multi.rar)
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=SparkFun_70C&oldid=12536](https://OpenTraceLab.org/w/index.php?title=SparkFun_70C&oldid=12536)" 
[Categories](specialcategories-specialcategories.md): \- [Device](./Category:Device.html "Category:Device") \- [Multimeter](./Category:Multimeter.html "Category:Multimeter") \- [Supported](./Category:Supported.html "Category:Supported")

## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
