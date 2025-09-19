# Rockylogic Ant8
| | | |:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------:| | [*Image: \1* | | | Status | planned | | Channels | 8 | | Samplerate | 500MHz | | Samplerate (state) | ? | | Triggers | ? | | Min/max voltage | ? | | Memory | ? | | Compression | ? | | Website | *rockylogic.com* | **RockyLogic Ant8** The *RockyLogic Ant8* is a USB-based, 8-channel logic analyzer with up to 500MHz sampling rate. See *RockyLogic_Ant8/Info* for more details (such as **lsusb -v** output) about the device.
## Contents
\- *1 Hardware* \- *2 Photos* \- *3 Protocol* \- *4 DIY Ant8 probe cable* \- *5 Resources*
## Hardware \- Xilinx Spartan-II XC2S30 VQ100AMS0341 (FPGA; 13,824 total distributed RAM bits, 24K total block RAM) \- Xilinx XC9572XL VQ44BMN0345 10C (CPLD; 10ns pin-to-pin logic delays) \- FTDI FT245BM (USB FIFO device) \- IDT ICS501M (clock multiplier) \- Atmel AT93C66 (4kB, three-wire serial EEPROM) \- ON Semiconductor (On) HC00A PGZI (quad 2-input NAND gate) \- National/TI LP2989 (marking: 33AB 2989 IM-2.5) (micropower/low-noise, 500mA ultra low-dropout regulator) \- 20MHz crystal (for the FPGA) ## Photos \-
[*Image: \1*
RockyLogic Ant8
\-
[*Image: \1*
Device with probes
\-
[*Image: \1*
PCB, front
\-
[*Image: \1*
PCB, back
\-
[*Image: \1*
FTDI FT245BM
\-
[*Image: \1*
Atmel 93C66 EEPROM
\-
[*Image: \1*
Xilinx XC2S30
\-
[*Image: \1*
Xilinx XC9572XL
\-
[*Image: \1*
IDT ICS501M
\-
[*Image: \1*
National LP2989
\-
[*Image: \1*
ON HC00A
See also [this flickr set](https://secure.flickr.com/photos/uwehermann/sets/72157628456436719/) for more PCB photos of the device. ## Protocol See *the Ant18e wiki page* for a description of the Ant8/Ant16/Ant18e protocol. ## DIY Ant8 probe cable The Ant8 cable shipped with the device doesn't have the best quality probes/hooks, but you can easily make your own cable where you can attach the better-quality E-Z Hooks. **Requirements:** \- 10-pin colored ribbon cable, such as *this one*. \- The colors match the one shipped with the Ant8 (white, gray, purple, blue, green, yellow, orange, red, brown) if you remove the 10th (black) lead. The brown lead is GND. \- A "SUB-D" connector where you can attach the ribbon cable, such as *this one*. \- 5 female-female jumper wires, such as [these ones](http://www.komputer.de/zen/index.php?main_page=product_info&cPath=31&products_id=77), which we'll cut into two halves to get 10 female connectors (only 9 needed). \- 9 short pieces of heat-shrink tubing. \- 9 E-Z Hook grippers/hooks to attach to the cable. **Photos:** \-
[*Image: \1*
Sub-D connector
\-
[*Image: \1*
Ribbon cable (black lead removed)
\-
[*Image: \1*
Connected cable
\-
[*Image: \1*
Jumper wires
\-
[*Image: \1*
Cut jumper wires
\-
[*Image: \1*
Heat-shrink tubing
\-
[*Image: \1*
Prepared heat-shrink tubing
\-
[*Image: \1*
Soldered jumper-wires
\-
[*Image: \1*
Heated up
\-
[*Image: \1*
Finished cable with E-Z Hooks
See also [this flickr set](https://secure.flickr.com/photos/uwehermann/sets/72157628685898881/) for more photos. ## Resources TODO.
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=RockyLogic_Ant8&oldid=9730](https://OpenTraceLab.org/w/index.php?title=RockyLogic_Ant8&oldid=9730)"
: \- *Device* \- *Logic analyzer* \- *Planned*
## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
