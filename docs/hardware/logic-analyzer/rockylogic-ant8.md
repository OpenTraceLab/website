# Rockylogic Ant8

| | | |:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------:| | [![\1](../../assets/hardware/general/\2)](./File:Rockylogic_ant8.png.html) | | | Status | planned | | Channels | 8 | | Samplerate | 500MHz | | Samplerate (state) | ? | | Triggers | ? | | Min/max voltage | ? | | Memory | ? | | Compression | ? | | Website | [rockylogic.com](http://www.rockylogic.com/products/ant8.html) | **RockyLogic Ant8** The [RockyLogic Ant8](http://www.rockylogic.com/products/ant8.html) is a USB-based, 8-channel logic analyzer with up to 500MHz sampling rate. See [RockyLogic_Ant8/Info](RockyLogic_Ant8/Info.html "RockyLogic Ant8/Info") for more details (such as **lsusb -v** output) about the device. 
## Contents 
\- [1 Hardware](RockyLogic_Ant8.html#Hardware) \- [2 Photos](RockyLogic_Ant8.html#Photos) \- [3 Protocol](RockyLogic_Ant8.html#Protocol) \- [4 DIY Ant8 probe cable](RockyLogic_Ant8.html#DIY_Ant8_probe_cable) \- [5 Resources](RockyLogic_Ant8.html#Resources) 
## Hardware \- Xilinx Spartan-II XC2S30 VQ100AMS0341 (FPGA; 13,824 total distributed RAM bits, 24K total block RAM) \- Xilinx XC9572XL VQ44BMN0345 10C (CPLD; 10ns pin-to-pin logic delays) \- FTDI FT245BM (USB FIFO device) \- IDT ICS501M (clock multiplier) \- Atmel AT93C66 (4kB, three-wire serial EEPROM) \- ON Semiconductor (On) HC00A PGZI (quad 2-input NAND gate) \- National/TI LP2989 (marking: 33AB 2989 IM-2.5) (micropower/low-noise, 500mA ultra low-dropout regulator) \- 20MHz crystal (for the FPGA) ## Photos \- 
[![\1](../../assets/hardware/general/\2)](./File:Rockylogic_ant8_device.jpg.html)
RockyLogic Ant8
\- 
[![\1](../../assets/hardware/general/\2)](./File:Rockylogic_ant8_device_with_probes.jpg.html)
Device with probes
\- 
[![\1](../../assets/hardware/general/\2)](./File:Rockylogic_ant8_pcb_front.jpg.html)
PCB, front
\- 
[![\1](../../assets/hardware/general/\2)](./File:Rockylogic_ant8_pcb_back.jpg.html)
PCB, back
\- 
[![\1](../../assets/hardware/general/\2)](./File:Rockylogic_ant8_ftdi_ft245bm.jpg.html)
FTDI FT245BM
\- 
[![\1](../../assets/hardware/general/\2)](./File:Rockylogic_ant8_atmel_93c66_eeprom.jpg.html)
Atmel 93C66 EEPROM
\- 
[![\1](../../assets/hardware/general/\2)](./File:Rockylogic_ant8_xilinx_spartan_xc2s30_fpga.jpg.html)
Xilinx XC2S30
\- 
[![\1](../../assets/hardware/general/\2)](./File:Rockylogic_ant8_xilinx_xc9572xl_cpld.jpg.html)
Xilinx XC9572XL
\- 
[![\1](../../assets/hardware/general/\2)](./File:Rockylogic_ant8_idt_ics501m.jpg.html)
IDT ICS501M
\- 
[![\1](../../assets/hardware/general/\2)](./File:Rockylogic_ant8_national_lp2989_im2_5.jpg.html)
National LP2989
\- 
[![\1](../../assets/hardware/general/\2)](./File:Rockylogic_ant8_on_hc00a_pgzi.jpg.html)
ON HC00A
See also [this flickr set](https://secure.flickr.com/photos/uwehermann/sets/72157628456436719/) for more PCB photos of the device. ## Protocol See [the Ant18e wiki page](RockyLogic_Ant18e.html#Protocol "RockyLogic Ant18e") for a description of the Ant8/Ant16/Ant18e protocol. ## DIY Ant8 probe cable The Ant8 cable shipped with the device doesn't have the best quality probes/hooks, but you can easily make your own cable where you can attach the better-quality E-Z Hooks. **Requirements:** \- 10-pin colored ribbon cable, such as [this one](http://www.reichelt.de/Flachbandkabel/AWG-28-10F-3M/index.html?;ACTION=3;LA=2;ARTICLE=47668;GROUPID=3328;artnr=AWG+28-10F+3M). \- The colors match the one shipped with the Ant8 (white, gray, purple, blue, green, yellow, orange, red, brown) if you remove the 10th (black) lead. The brown lead is GND. \- A "SUB-D" connector where you can attach the ribbon cable, such as [this one](http://www.reichelt.de/SUB-D-Flachbandverbinder/D-SUB-BU-09FB/index.html?;ACTION=3;LA=2;ARTICLE=6951;GROUPID=3204;artnr=D-SUB+BU+09FB). \- 5 female-female jumper wires, such as [these ones](http://www.komputer.de/zen/index.php?main_page=product_info&cPath=31&products_id=77), which we'll cut into two halves to get 10 female connectors (only 9 needed). \- 9 short pieces of heat-shrink tubing. \- 9 E-Z Hook grippers/hooks to attach to the cable. **Photos:** \- 
[![\1](../../assets/hardware/general/\2)](./File:Diy_rockylogic_ant8_cable_connector.jpg.html)
Sub-D connector
\- 
[![\1](../../assets/hardware/general/\2)](./File:Diy_rockylogic_ant8_cable_ribbon_cable.jpg.html)
Ribbon cable (black lead removed)
\- 
[![\1](../../assets/hardware/general/\2)](./File:Diy_rockylogic_ant8_cable_cable_connected.jpg.html)
Connected cable
\- 
[![\1](../../assets/hardware/general/\2)](./File:Diy_rockylogic_ant8_cable_jumper_wires.jpg.html)
Jumper wires
\- 
[![\1](../../assets/hardware/general/\2)](./File:Diy_rockylogic_ant8_cable_jumper_wires_cut.jpg.html)
Cut jumper wires
\- 
[![\1](../../assets/hardware/general/\2)](./File:Diy_rockylogic_ant8_cable_heat_shrink_tubing.jpg.html)
Heat-shrink tubing
\- 
[![\1](../../assets/hardware/general/\2)](./File:Diy_rockylogic_ant8_cable_prepare_heatshrink_tubing.jpg.html)
Prepared heat-shrink tubing
\- 
[![\1](../../assets/hardware/general/\2)](./File:Diy_rockylogic_ant8_cable_solder_jumper_wires.jpg.html)
Soldered jumper-wires
\- 
[![\1](../../assets/hardware/general/\2)](./File:Diy_rockylogic_ant8_cable_heated_up.jpg.html)
Heated up
\- 
[![\1](../../assets/hardware/general/\2)](./File:Diy_rockylogic_ant8_cable_finished_with_ezhooks.jpg.html)
Finished cable with E-Z Hooks
See also [this flickr set](https://secure.flickr.com/photos/uwehermann/sets/72157628685898881/) for more photos. ## Resources TODO. 
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=RockyLogic_Ant8&oldid=9730](https://OpenTraceLab.org/w/index.php?title=RockyLogic_Ant8&oldid=9730)" 
[Categories](specialcategories-specialcategories.md): \- [Device](./Category:Device.html "Category:Device") \- [Logic analyzer](./Category:Logic_analyzer.html "Category:Logic analyzer") \- [Planned](./Category:Planned.html "Category:Planned")

## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
