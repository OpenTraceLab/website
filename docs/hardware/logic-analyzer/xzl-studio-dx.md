# Xzl Studio Dx

**XZL_Studio DX** [![\1](../../assets/hardware/general/\2)](./File:Xzl_studio-dx_mugshot.png.html) |   
---|---  
Status | supported  
Source code | [fx2lafw](http://github.com/OpenTraceLab/?p=OpenTraceCapture.git;a=tree;f=src/hardware/fx2lafw)  
Channels | 16 + 2  
Samplerate | 24MHz  
Samplerate (state) | —  
Triggers | none (SW-only)  
Min/max voltage | Digital 0 — 5.4V  
Analog ±10V  
Threshold voltage | Fixed: VIH=1.4V, VIL=0.8V  
Memory | none  
Compression | none  
Website | [hotmcu.com](http://www.hotmcu.com/xzl-studio-dx-mixed-signal-oscilloscope-logic-analyzer-p-13.html)  
**XZL_Studio DX** The **XZL_Studio DX** is a USB-based, 16-channel logic analyzer with up to 24MHz sampling rate, and with 2 additional analog channels. It is a clone of the [CWAV USBee DX](https://OpenTraceLab.org/w/index.php?title=CWAV_USBee_DX&action=edit&redlink=1 "CWAV USBee DX \(page does not exist\)"). See [XZL_Studio DX/Info](XZL_Studio_DX/Info.html "XZL Studio DX/Info") for some more details (such as **lsusb -vvv** output) on the device. **Note**:You need to chose one of "CWAV USBee DX" devices found in system ( *OpenTraceLab-ok --scan* ). One of them is digital (supported, 16 channels). Other show 16 digital channels too, but it is for 2x analog input and not working yet. **Note**: Due to the fact that this device has two FX2 chips behind a USB hub inside, this will need extra code to enumerate correctly in OpenTraceLab. Do you have this device? Let us know! **Note**: Idea how sync 2 chips works. Second FX2 is responsible for reading ADC data only, but it can't initialise processing. It can only get info from first chip that he need to read data -\> pin SLWR. So it means that if second chip do conversions only when triggered, then there are exactly that same number of samples read from both chips, from that same time... Look at 48 page of [Cypress CY7C68013A-56LTXC (FX2LP)](http://www.cypress.com/?docID=45142#page=48) "Slave FIFO Asynchronous Write" 
## Contents 
\- [1 Hardware](XZL_Studio_DX.html#Hardware) \- [2 Pin mapping](XZL_Studio_DX.html#Pin_mapping) \- [2.1 First FX2LP pin mappings](XZL_Studio_DX.html#First_FX2LP_pin_mappings) \- [2.2 Second FX2LP pin mappings](XZL_Studio_DX.html#Second_FX2LP_pin_mappings) \- [3 Photos](XZL_Studio_DX.html#Photos) \- [4 Protocol](XZL_Studio_DX.html#Protocol) \- [5 Resources](XZL_Studio_DX.html#Resources) 
## Hardware \- **Main chip**: 2x [Cypress CY7C68013A-56LTXC (FX2LP)](http://www.cypress.com/?docID=45142) \- **Analog-to-Digital converter**: 2x [Texas Instruments TLC5510I (SO 24pin package)](http://www.ti.com/lit/ds/symlink/tlc5510.pdf) \- **I2C EEPROM**: ATMLH136 24C02C M Y, place for second EEPROM chip [reference](http://ww1.microchip.com/downloads/en/DeviceDoc/21202J.pdf). \- **USB 2.0 Hub**: [SMSC USB2512A (QFN 36-pin package)](http://www.mouser.com/catalog/specsheets/2512adb.pdf) \- **Low-dropout voltage regulator**: [Advanced Monolithic Systems AMS1117-3.3](http://www.advanced-monolithic.com/pdf/ds1117.pdf) \- **CMOS Voltage Converter**: 2x [7660 AIBAZ V01828A](https://www.ti.com/lit/ds/symlink/lmc7660.pdf) \- **Crystal**: 24MHz \- ... Two jumpers: \- **P1** jumper - WRITE PROTECT, Connects WP EEPROM pin \\[7\\] to Vcc. If pin is closed, Write Protection is enabled. \- **P3** jumper - EEPROM CONNECTION, connects SDA EEPROM pin \\[5\\] to SDA pins on both CY7C68013A (if open there is no connection) Extra info, It looks that place for second eeprom is designed as backup memory. If P4 is closed, and P3 is open, then only spare memory is connected. ## Pin mapping Needed for use (I don't know how to remap pins yet) Current PIN meaning - instead of that what is printed on device (for OpenTraceLab 0.8) | | | |------|-----| | 4 | 15 | | 5 | 14 | | 6 | 13 | | 7 | 8 | | 3 | 9 | | 2 | 10 | | 1 | 11 | | 0 | 12 | | TRIG | GND | | 5V | GND | ### First FX2LP pin mappings Responsible for all digital inputs (0-15) and TRIG. Now it works with latest software version, but channels numbers are scrambled: | | | | | |-----|--------------|---------------------------------------------|---------------------------------------| | \\# | Pin | Destination | Remark | | | FD4 | 0 | digital input | | | FD5 | 1 | digital input | | | FD6 | 2 | digital input | | | FD7 | 3 | digital input | | | FD3 | 4 | digital input | | | FD2 | 5 | digital input | | | FD1 | 6 | digital input | | | FD0 | 7 | digital input | | | FD15 | 8 | digital input | | | FD14 | 9 | digital input | | | FD13 | a | digital input | | | FD8 | b | digital input | | | FD9 | c | digital input | | | FD10 | d | digital input | | | FD11 | e | digital input | | | FD12 | f | digital input | | 36 | CTL0/FLAGA | TRIG | socket pin | | 37 | CTL1/\\*FLAGB | ADC \\[1,2\\] CLK + RDY1/SLWR on second FX2LP | signal for both ADC and secondary FX2 | | 21 | Reserved | GND | | ### Second FX2LP pin mappings Connected to both ADCs FX2LP pin mappings | | | | | |-----------|-------------------|---------------------------------------|---------------------------------------------------------------| | \\# | Pin | Destination | Remark | | 9 | RDY1/SLWR | CL1 on first FXLP and ADC \\[1,2\\] CLK | input: ADC_clock, signal to start read data | | 25-32 | FD0-FD7 | ADC CH1, D1-D8 | ADC_data for channel 1 | | 42-56,1-3 | FD8-FD15 | ADC CH2, D1-D8 | ADC_data for channel 2 | | 45 | PA5/FIFOADR1 | GND | gnd ? to check | | 47 | PA7/\\*FLAGD/SLCS# | GND | gnd ? to check? **probably can be used do distinguish chips** | *TODO* - check rest of the pins EEPROM - connected to both (!) CY7C68013A processors | | | | | |-----|--------|-----------|------------| | \\# | EEPROM | Processor | | | | SDA | SDA | via jumper | | | SCL | SCL | | ## Photos \- 
[![\1](../../assets/hardware/general/\2)](./File:XZL_Studio-DX_front.jpg.html)
Device, top
\- 
[![\1](../../assets/hardware/general/\2)](./File:XZL_Studio-DX_connectors.jpg.html)
Device, connectors
\- 
[![\1](../../assets/hardware/general/\2)](./File:XZL_Studio-DX_usb.jpg.html)
Device, usb
\- 
[![\1](../../assets/hardware/general/\2)](./File:XZL_Studio-DX_pcb_up.jpg.html)
PCB, top
\- 
[![\1](../../assets/hardware/general/\2)](./File:XZL_Studio-DX_pcb_down.jpg.html)
PCB, bottom
## Protocol Since we use the open-source [fx2lafw](Fx2lafw.html "Fx2lafw") firmware for this device, we don't need to know the protocol. ## Resources TODO. 
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=XZL_Studio_DX&oldid=13848](https://OpenTraceLab.org/w/index.php?title=XZL_Studio_DX&oldid=13848)" 
[Categories](specialcategories-specialcategories.md): \- [Device](./Category:Device.html "Category:Device") \- [Logic analyzer](./Category:Logic_analyzer.html "Category:Logic analyzer") \- [Oscilloscope](./Category:Oscilloscope.html "Category:Oscilloscope") \- [Mixed-signal oscilloscope](./Category:Mixed-signal_oscilloscope.html "Category:Mixed-signal oscilloscope") \- [Supported](./Category:Supported.html "Category:Supported")

## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
