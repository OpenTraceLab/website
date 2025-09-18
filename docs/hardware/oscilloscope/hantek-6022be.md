# Hantek 6022Be

| | | |:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------------------:| | [![\1](../../assets/hardware/general/\2)](./File:Hantek_6022be_mugshot.png.html) | | | Status | supported | | Source code | [hantek-6xxx](http://github.com/OpenTraceLab/?p=OpenTraceCapture.git;a=tree;f=src/hardware/hantek-6xxx) | | Channels | 2 | | Samplerate | 48MHz | | Analog bandwidth | 20MHz | | Vertical resolution | 8bit | | Triggers | none (SW-only) | | Input impedance | 1MΩ‖25pF | | Memory | none | | Display | none | | Connectivity | USB | | Website | [hantek.com](http://www.hantek.com/en/ProductDetail_2_31.html) | **Hantek 6022BE** The **Hantek 6022BE** is a USB-based, 2-channel oscilloscope with an analog bandwidth of 20MS/s and 48MS/s sampling rate. See [Hantek 6022BE/Info](Hantek_6022BE/Info.html "Hantek 6022BE/Info") for more details (such as **lsusb -v** output) about the device. 
## Contents 
\- [1 Hardware](Hantek_6022BE.html#Hardware) \- [2 Photos](Hantek_6022BE.html#Photos) \- [3 Protocol](Hantek_6022BE.html#Protocol) \- [4 Firmware](Hantek_6022BE.html#Firmware) \- [5 Resources](Hantek_6022BE.html#Resources) 
## Hardware \- **USB**: [Cypress CY7C68013A-100AXC](http://www.cypress.com/documentation/datasheets/cy7c68013a-cy7c68014a-cy7c68015a-cy7c68016a-ez-usb-fx2lp-usb) (FX2LP) ([datasheet](http://www.cypress.com/file/138911/download)) \- **256-byte I²C EEPROM**: [Microchip 24LC02BI](http://www.microchip.com/wwwproducts/en/24LC02B) ([datasheet](http://ww1.microchip.com/downloads/en/DeviceDoc/21709J.pdf)) \- 2x **8-channel analog multiplexer/demultiplexer**: [NXP 74HC4051D](http://www.nexperia.com/products/logic/switches-multiplexers-de-multiplexers/digital-switches/74HC4051D.html) ([datasheet](http://assets.nexperia.com/documents/data-sheet/74HC_HCT4051.pdf)) \- **1A low-dropout voltage regulator (3.3V):** [Advanced Monolithic Systems AMS1117-3.3](http://www.advanced-monolithic.com/products/voltreg.html#1117) ([datasheet](http://www.advanced-monolithic.com/pdf/ds1117.pdf)) \- **2W, fixed input, isolated & unregulated dual/single output DC/DC converter**: [Mornsun A_S-2WR2 (A0505S-2WR2)](http://www.mornsun.cn/html/product/content/A_S-2WR2.html) ([datasheet](http://www.mornsun.cn/uploads/pdf/A_S-2WR2.pdf)) \- **8-bit, 40/80/100MHz, dual ADC**: [Analog Devices AD9288](http://www.analog.com/en/products/analog-to-digital-converters/ad-converters/ad9288.html) ([datasheet](http://www.analog.com/media/en/technical-documentation/data-sheets/AD9288.pdf)) \- 4x **145 MHz FastFET Op Amp**: [Analog Devices AD8065](http://www.analog.com/en/products/amplifiers/operational-amplifiers/jfet-input-amplifiers/ad8065.html) ([datasheet](http://www.analog.com/media/en/technical-documentation/data-sheets/AD8065-KGD-CHIP.pdf)) \- **Crystal**: 24MHz **NXP 74HC4051D (upper/lower, CH1/CH2) pinout**:  | (GND) Y4 | 1- |  O | -16 | VCC  
---|---|---|---|---  
(GND) Y6 | 2- | -15 | Y2  
Z | 3- | -14 | Y1  
(GND) Y7 | 4- | -13 | Y0  
(GND) Y5 | 5- | -12 | Y3  
(GND) E# | 6- | -11 | S0 (FX2 PC2)  
VEE | 7- | -10 | S1 (FX2 PC3)  
GND | 8- | -9 | S2 (FX2 PC4)  
| (GND) Y4 | 1- |  O | -16 | VCC  
---|---|---|---|---  
(GND) Y6 | 2- | -15 | Y2  
Z | 3- | -14 | Y1  
(GND) Y7 | 4- | -13 | Y0  
(GND) Y5 | 5- | -12 | Y3  
(GND) E# | 6- | -11 | S0 (FX2 PC5)  
VEE | 7- | -10 | S1 (FX2 PC6)  
GND | 8- | -9 | S2 (FX2 PC7)  
| | | | | | |-----|-----|-----|---------------|-------------------------| | S2 | S1 | S0 | 74HC4051D Mux | VDIVs (vendor software) | | 0 | 0 | 0 | Y0 to Z | 200mV | | 0 | 0 | 1 | Y1 to Z | 500mV | | 0 | 1 | 0 | Y2 to Z | 5V, 2V, 1V | | 0 | 1 | 1 | Y3 to Z | 100mV, 50mV, 20mV | **Microchip 24LC02BI pinout**:  | | | | | | |--------------------------------------------------------:|----:|-----|-----|-------------------------------------------------| | (Low, but not GND) A0 | 1- | O | -8 | VCC | | (GND) A1 | 2- | | -7 | WP (GND) | | (GND) A2 | 3- | | -6 | SCL (FX2 SCL) | | VSS | 4- | | -5 | SDA (FX2 SDA) |  **Analog Devices ADS9288 pinout**: | | | |----------------------------------|----------------------------------------------------------------------------| | AD9288 pins | Description | | S1, S2 | S1=VCC, S2=GND. "Normal operation, data align disabled". | | DFS | Tied to GND. Data format select = "offset binary" (not "twos complement"). | | AINA, AINB | Analog input channels. | **Cypress FX2 pinout**:  FX2 pins | Description  
---|---  
CTL2 | Connected to AD9288 ENCA and ENCB and FX2 IFCLK.  
PB0-PB7 | Connected to AD9288 D0A-D7A.  
PD0-PD7 | Connected to AD9288 D0B-D7B.  
PA7 | 1kHz probe calibration pin.  
PC0/PC1 | Dual-color (red/green) LED.  | PC1 | PC0 | LED  
---|---|---  
0 | 0 | ?  
0 | 1 | green  
1 | 0 | red  
1 | 1 | off  
## Photos \- 
[![\1](../../assets/hardware/general/\2)](./File:Hantek_6022be_box.jpg.html)
Box
\- 
[![\1](../../assets/hardware/general/\2)](./File:Hantek_6022be_accessories.jpg.html)
Accessories
\- 
[![\1](../../assets/hardware/general/\2)](./File:Hantek_6022be_probes.jpg.html)
Probes
\- 
[![\1](../../assets/hardware/general/\2)](./File:Hantek_6022be_device_top.jpg.html)
Device, top
\- 
[![\1](../../assets/hardware/general/\2)](./File:Hantek_6022be_device_bottom.jpg.html)
Device, bottom
\- 
[![\1](../../assets/hardware/general/\2)](./File:Hantek_6022be_device_connectors.jpg.html)
Device, connectors
\- 
[![\1](../../assets/hardware/general/\2)](./File:Hantek_6022be_device_usb.jpg.html)
Device, USB
\- 
[![\1](../../assets/hardware/general/\2)](./File:Hantek_6022be_pcb_top.jpg.html)
PCB, top
\- 
[![\1](../../assets/hardware/general/\2)](./File:Hantek_6022be_pcb_bottom.jpg.html)
PCB, bottom
\- 
[![\1](../../assets/hardware/general/\2)](./File:Hantek_6022be_pcb_input_stage.jpg.html)
Input stage
\- 
[![\1](../../assets/hardware/general/\2)](./File:Hantek_6022be_cypress_fx2lp.jpg.html)
Cypress FX2LP
\- 
[![\1](../../assets/hardware/general/\2)](./File:Hantek_6022be_microchip_24lc02bi.jpg.html)
Microchip 24LC02BI
\- 
[![\1](../../assets/hardware/general/\2)](./File:Hantek_6022be_nxp_74hc4051d.jpg.html)
NXP 74HC4051D
\- 
[![\1](../../assets/hardware/general/\2)](./File:Hantek_6022be_ams1117.jpg.html)
AMS AMS1117
\- 
[![\1](../../assets/hardware/general/\2)](./File:Hantek_6022be_mornsun_a0505s-2wr.jpg.html)
Mornsun A0505S-2WR
**Another teardown**: \- 
[![\1](../../assets/hardware/general/\2)](./File:Hantek_6022be.jpg.html)
Device, top
\- 
[![\1](../../assets/hardware/general/\2)](./File:Hantek_6022be_1.jpg.html)
PCB, top
\- 
[![\1](../../assets/hardware/general/\2)](./File:Hantek_6022be_2.jpg.html)
PCB, bottom
\- 
[![\1](../../assets/hardware/general/\2)](./File:Hantek_6022be_zoomed_1.jpg.html)
Feedback resistor selector
\- 
[![\1](../../assets/hardware/general/\2)](./File:Hantek_6022be_zoomed_2.jpg.html)
Cypress FX2LP
## Protocol | | | | |------------------------|----------------|--------------------------------------------------------------------------| | Oscilloscope command | bRequest value | Notes | | Set CH0 voltage range | 0xE0 | Possible values: 1, 2, 5, 10 (5V, 2.5V, 1V, 500mV). | | Set CH1 voltage range | 0xE1 | Possible values: 1, 2, 5, 10 (5V, 2.5V, 1V, 500mV). | | Set sampling rate | 0xE2 | Possible values: 48, 30, 24, 16, 8, 4, 1 (MHz) and 50, 20, 10 (\\*10kHz). | | Trigger oscilloscope | 0xE3 | Possible values: 1 == start sampling. 0 == ignored currently. | | Set number of channels | 0xE4 | Possible values: 1, 2. | ## Firmware In order to use this device, the [OpenTraceLab-firmware-fx2lafw](Fx2lafw.html "Fx2lafw") (\>= 0.1.4) firmware is required. The firmware was originally written by Jochen Hoenicke (see [README](http://github.com/OpenTraceLab/?p=OpenTraceLab-firmware-fx2lafw.git;a=blob;f=README) for details), thanks a lot! **Note**: The firmware is **not** flashed into the device permanently! You only need to make it available in the usual place where [OpenTraceCapture](OpenTraceCapture.html "OpenTraceCapture") looks for firmware files, it will be used automatically (and "uploaded" to the Cypress FX2's SRAM every time you attach the device to a USB port). **Note**: On Windows, you will have to [assign the WinUSB driver via Zadig](Windows.html#Device_specific_USB_driver "Windows") **twice**: the first time for the initial USB VID/PID the device has when attaching it via USB (04b4:6022 or 04b5:6022, depending on which vendor driver is currently being used by the device), and a second time after the firmware has been uploaded to the device and the device has "renumerated" with a different VID/PID pair (1d50:608e). ## Resources \- [Vendor software and manuals](http://1drv.ms/1gWOsUF) \- [openhantek.org forum: Protocol info](https://web.archive.org/web/20140422004136/http://www.openhantek.org/forum/topic/4/13/)
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=Hantek_6022BE&oldid=14941](https://OpenTraceLab.org/w/index.php?title=Hantek_6022BE&oldid=14941)" 
[Categories](specialcategories-specialcategories.md): \- [Device](./Category:Device.html "Category:Device") \- [Oscilloscope](./Category:Oscilloscope.html "Category:Oscilloscope") \- [Supported](./Category:Supported.html "Category:Supported")

## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
