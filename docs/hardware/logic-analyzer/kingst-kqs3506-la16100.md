# Kingst Kqs3506 La16100

**KingST KQS3506-LA16100** [![\1](../../assets/hardware/general/\2)](./File:Kingst_kqs3506_la16100.png.html) |   
---|---  
Status | supported  
Source code | [saleae-logic16](http://github.com/OpenTraceLab/?p=OpenTraceCapture.git;a=tree;f=src/hardware/saleae-logic16)  
Channels | 3/6/9/16  
Samplerate | 100/50/32/16MHz  
Samplerate (state) | —  
Triggers | none (SW-only)  
Min/max voltage | -0.9V — 6V  
Threshold voltage | configurable:  
for 1.8V to 3.6V systems: VIH=1.4V, VIL=0.7V  
for 5V systems: VIH=3.6V, VIL=1.4V  
Memory | none  
Compression | yes  
Website | [taobao.com](http://item.taobao.com/item.htm?id=20369792793)  
**KingST KQS3506-LA16100** The **KingST KQS3506-LA16100** is a USB-based, 16-channel logic analyzer with 100/50/32/16MHz sampling rate (at 3/6/9/16 enabled channels). This is a clone of the [Saleae Logic16](Saleae_Logic16.html "Saleae Logic16"). See [KingST KQS3506-LA16100/Info](KingST_KQS3506-LA16100/Info.html "KingST KQS3506-LA16100/Info") for more details (such as **lsusb -v** output) about the device. 
## Contents 
\- [1 Hardware](KingST_KQS3506-LA16100.html#Hardware) \- [2 Photos](KingST_KQS3506-LA16100.html#Photos) \- [3 Firmware](KingST_KQS3506-LA16100.html#Firmware) \- [4 Protocol](KingST_KQS3506-LA16100.html#Protocol) \- [5 Resources](KingST_KQS3506-LA16100.html#Resources) 
## Hardware \- **FPGA**: [Xilinx Spartan-3A XC3S200A](http://www.xilinx.com/support/index.html/content/xilinx/en/supportNav/silicon_devices/fpga/spartan-3a.html), 200K gates ([datasheet](http://www.xilinx.com/support/documentation/data_sheets/ds529.pdf)) \- **CPLD**: [Altera EPM3032A](http://www.altera.com/literature/lit-m3k.jsp), 600 gates, 32 macrocells ([datasheet](http://www.altera.com/literature/ds/m3000a.pdf), [pinout](http://www.altera.com/literature/dp/max3k/epm3032a.pdf)). \- **USB interface chip**: [Cypress CY7C68013A-56PVXC (FX2LP)](http://www.cypress.com/?mpn=CY7C68013A-56PVXC) ([datasheet](http://www.cypress.com/?docID=34060)) \- **I2C EEPROM**: [Microchip 24LC02B](http://www.microchip.com/wwwproducts/Devices.aspx?dDocName=en010810) ([datasheet](http://ww1.microchip.com/downloads/en/DeviceDoc/21709J.pdf)) \- **3.3V voltage regulator**: [Advanced Monolithic Systems AMS1117-3.3](http://www.advanced-monolithic.com/products/voltreg.html#1117) ([datasheet](http://ams-semitech.com/attachments/File/AMS1117_20120314.pdf), [older datasheet](http://www.advanced-monolithic.com/pdf/ds1117.pdf)) \- **1.2V voltage regulator**: [Advanced Monolithic Systems AMS1117-1.2](http://www.advanced-monolithic.com/products/voltreg.html#1117) ([datasheet](http://ams-semitech.com/attachments/File/AMS1117_20120314.pdf), [older datasheet](http://www.advanced-monolithic.com/pdf/ds1117.pdf)) \- **Crystal**: 24.000 **Pinouts and connections:** **I2C EEPROM:** The Microchip 24LC02B is connected to the Cypress FX2. The **WP** pin of the EEPROM can be jumpered to low or high, in order to write-protect it (or not). The address pins (A0-A2) are all connected to GND, which makes the I2C slave address of the EEPROM 0x50.  | | | | | | |------------------------------------------:|----:|-----|-----|-------------------------------------------------| | (GND) A0 | 1- | O | -8 | VCC (3.3V) | | (GND) A1 | 2- | | -7 | WP (jumper W2) | | (GND) A2 | 3- | | -6 | SCL (FX2 SCL) | | GND | 4- | | -5 | SDA (FX2 SDA) |  **CLPD:** The Altera EPM3032A JTAG pins are available on the **J3** pin header. | | | | | | | | | | | | |------------------------------------------------|------------------------------------------------|-----------------------------------------------------|-----------------------------------------------------------|------------------------------------------------------|------------------------------------------------|-----------------------------------------------------------|-------------------------------------------------|----------------------------------------------------------|-------------------------------------------------|----------------------------------------------------------| | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | | JTAG TDI | I/O (FX2 PA7) | I/O (FX2 PA6) | GND | I/O (FX2 PA5) | I/O (FX2 PA4) | JTAG TMS | I/O (FX2 PA3) | VCC | I/O (FX2 PA2) | GND | | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | | I/O (FX2 PA1) | I/O (FX2 PA0) | I/O (FPGA PROG_B) | I/O (FPGA 94, IO_L05N_0) | GND | VCC | I/O (FPGA 85, IO_L03P_0) | I/O (FX2 CTL2) | I/O (FX2 CTL1) | I/O (FX2 CTL0) | I/O (FPGA 51, DIN/MISO) | | 23 | 24 | 25 | 26 | 27 | 28 | 29 | 30 | 31 | 32 | 33 | | I/O (NC?) | GND | I/O (FPGA 97, IP0) | JTAG TCK | I/O (FPGA 53, CCLK) | I/O (NC?) | VCC | GND | I/O (FPGA 3, IO_L01P_3) | JTAG TDO | I/O (NC?) | | 34 | 35 | 36 | 37 | 38 | 39 | 40 | 41 | 42 | 43 | 44 | | I/O (NC?) | I/O (NC?) | GND | I/O (NC?) | I/O (NC?) | I/O (NC?) | I/O (NC?) | VCC | I/O (NC?) | I/O (NC?) | I/O (NC?) | **JTAG header (CPLD):** The **J3** pin header is a JTAG connector wired to the CPLD (it is **not** additionally wired to the FPGA in a JTAG chain). The pins are (from left to right): | | | | | | | |-----|-----|-----|-----|-----|------| | 1 | 2 | 3 | 4 | 5 | 6 | | TMS | TDI | TCK | TDO | GND | 3.3V | ## Photos **Revision 5.0**: \- 
[![\1](../../assets/hardware/general/\2)](./File:Kingst_kqs3506_la16100_package.jpg.html)
Package
\- 
[![\1](../../assets/hardware/general/\2)](./File:Kingst_kqs3506_la16100_paper.jpg.html)
Paper
\- 
[![\1](../../assets/hardware/general/\2)](./File:Kingst_kqs3506_la16100_device_top.jpg.html)
Device, top
\- 
[![\1](../../assets/hardware/general/\2)](./File:Kingst_kqs3506_la16100_device_bottom.jpg.html)
Device, bottom
\- 
[![\1](../../assets/hardware/general/\2)](./File:Kingst_kqs3506_la16100_device_usb.jpg.html)
Device, USB
\- 
[![\1](../../assets/hardware/general/\2)](./File:Kingst_kqs3506_la16100_device_connector.jpg.html)
Device, connector
\- 
[![\1](../../assets/hardware/general/\2)](./File:Kingst_kqs3506_la16100_pcb_top.jpg.html)
PCB, top
\- 
[![\1](../../assets/hardware/general/\2)](./File:Kingst_kqs3506_la16100_pcb_bottom.jpg.html)
PCB, bottom
\- 
[![\1](../../assets/hardware/general/\2)](./File:Kingst_kqs3506_la16100_xilinx_spartan_xc3s200a.jpg.html)
Xilinx XC3S200A
\- 
[![\1](../../assets/hardware/general/\2)](./File:Kingst_kqs3506_la16100_altera_epm3032a.jpg.html)
Altera EPM3032A
\- 
[![\1](../../assets/hardware/general/\2)](./File:Kingst_kqs3506_la16100_cypress_fx2.jpg.html)
Cypress FX2
\- 
[![\1](../../assets/hardware/general/\2)](./File:Kingst_kqs3506_la16100_at88sc0104_silkscreen.jpg.html)
AT88SC0104 silkscreen
\- 
[![\1](../../assets/hardware/general/\2)](./File:Kingst_kqs3506_la16100_microchip_24lc02b.jpg.html)
Microchip 24LC02B
\- 
[![\1](../../assets/hardware/general/\2)](./File:Kingst_kqs3506_la16100_inputstage_2.jpg.html)
Input stage, 1
\- 
[![\1](../../assets/hardware/general/\2)](./File:Kingst_kqs3506_la16100_input_stage1.jpg.html)
Input stage, 2
\- 
[![\1](../../assets/hardware/general/\2)](./File:Kingst_kqs3506_la16100_ams1117_33.jpg.html)
AMS1117-3.3
\- 
[![\1](../../assets/hardware/general/\2)](./File:Kingst_kqs3506_la16100_ams1117_12.jpg.html)
AMS1117-1.2
**Revision 6.0**: \- 
[![\1](../../assets/hardware/general/\2)](./File:Kingst_kqs3506_la16100_pcb_v6_top.jpg.html)
PCB, top
\- 
[![\1](../../assets/hardware/general/\2)](./File:Kingst_kqs3506_la16100_pcb_v6_bottom.jpg.html)
PCB, bottom
\- 
[![\1](../../assets/hardware/general/\2)](./File:Kingst_kqs3506_la16100_schematic_v6.png.html)
Schematic drawn from PCB
## Firmware See [Saleae_Logic16#Firmware](Saleae_Logic16.html#Firmware "Saleae Logic16"). ## Protocol See [Saleae_Logic16#Protocol](Saleae_Logic16.html#Protocol "Saleae Logic16"). ## Resources \- [kstmcu.taobao.com](http://kstmcu.taobao.com/) \- [kingst.org forum](http://www.kingst.org/forum/index) \- [MCU123 article](http://translate.google.com/translate?sl=zh-CN&tl=en&js=n&prev=_t&hl=de&ie=UTF-8&eotf=1&u=http%3A%2F%2Fwww.mcu123.com%2Fnews%2FArticle%2FPC%2FPCB%2F201210%2F4905.html&act=url)
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=KingST_KQS3506-LA16100&oldid=14186](https://OpenTraceLab.org/w/index.php?title=KingST_KQS3506-LA16100&oldid=14186)" 
[Categories](specialcategories-specialcategories.md): \- [Device](./Category:Device.html "Category:Device") \- [Logic analyzer](./Category:Logic_analyzer.html "Category:Logic analyzer") \- [Supported](./Category:Supported.html "Category:Supported")

## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
