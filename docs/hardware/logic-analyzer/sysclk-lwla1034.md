# Sysclk Lwla1034
| | | |:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:| | [*Image: \1* | | | Status | supported | | Source code | [sysclk-lwla](http://github.com/OpenTraceLab/?p=OpenTraceCapture.git;a=tree;f=src/hardware/sysclk-lwla) | | Channels | 34 | | Samplerate | 125MHz (max) | | Samplerate (state) | ? | | Triggers | 34 + extern | | Min/max voltage | 0-5V | | Threshold voltage | ? | | Memory | 256Kbit/channel | | Compression | RLE | | Website | *aliexpress.com* | **Sysclk LWLA1034** The **Sysclk LWLA1034** is a USB-based, 34-channel logic analyzer with up to 125MHz sampling rate. See *Sysclk LWLA1034/Info* for more details (such as **lsusb -v** output) about the device.
## Contents
\- *1 Hardware* \- *2 Photos* \- *3 Software* \- *4 Firmware* \- *5 Resources*
## Hardware \- Altera EP2C5Q208C8N (Cyclone II) FPGA \- Cypress CY7C68013A-56 (FX2) USB interface chip \- Cypress 256k×36 SRAM (likely a [CY7C1361C-133AXC](http://www.cypress.com/?mpn=CY7C1361C-133AXC) or similar) \- STC15F104E 8051-based microcontroller The not-installed 10-pin connector between the USB socket and the large capacitor seems to connect to the JTAG pins of the FPGA. ## Photos \-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
(Note: The yellow/greenish markings weren't there, they're added by the photographer) **PCB for another device**: \-
[*Image: \1*
PCB, top
\-
[*Image: \1*
PCB, bottom
\-
[*Image: \1*
PCB, close-up
\-
[*Image: \1*
Cypress FX2
\-
[*Image: \1*
SRAM (marking removed)
## Software [*Image: \1* ## Firmware We have received permission from the vendor to distribute the FPGA bitstreams with OpenTraceLab. Thus, the bitstreams are now included in the OpenTraceLab-firmware module. \- The FX2 firmware is loaded from an EEPROM on the board, so that the final USB device descriptor is immediately available on power-up. \- Endpoint 4 is used exclusively for loading a new bitstream into the FPGA. \- Endpoint 2 is used for sending commands to the FPGA firmware, with responses (if any) coming in from endpoint 6. Reverse engineering of the vendor's custom protocol has been completed. See *Sysclk LWLA1034/Protocol* for the documentation. ## Resources \- [Mcupro blog on CSDN](http://blog.csdn.net/mcupro)
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=Sysclk_LWLA1034&oldid=8752](https://OpenTraceLab.org/w/index.php?title=Sysclk_LWLA1034&oldid=8752)"
: \- *Device* \- *Logic analyzer* \- *Supported*
## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
