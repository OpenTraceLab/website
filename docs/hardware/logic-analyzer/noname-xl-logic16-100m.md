# Noname Xl Logic16 100M

**Noname XL-LOGIC16-100M** [![\1](../../assets/hardware/general/\2)](./File:Noname_xl_logic16_100m_mugshot.png.html) |   
---|---  
Status | in progress  
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
Price range | $30 - $35  
Website | [aliexpress.com](http://www.aliexpress.com/item/Free-Shipping-Saleae-24MHz-8Channels-Logic-Analyzer-Fully-Checked-Best-quality-Input-buffered/1731200392.html)  
**Noname XL-LOGIC16-100M** The **Noname XL-LOGIC16-100M** is a USB-based, 16-channel logic analyzer with up to 100MHz sampling rate. It is labelled and sold as a [Saleae Logic16](Saleae_Logic16.html "Saleae Logic16") clone, and comes with "modified" Saleae Logic software on a CD-ROM. See [Noname XL-LOGIC16-100M/Info](Noname_XL-LOGIC16-100M/Info.html "Noname XL-LOGIC16-100M/Info") for more details (such as **lsusb -v** output) about the device. 
## Contents 
\- [1 Variants in same case](Noname_XL-LOGIC16-100M.html#Variants_in_same_case) \- [2 Hardware](Noname_XL-LOGIC16-100M.html#Hardware) \- [3 Photos](Noname_XL-LOGIC16-100M.html#Photos) \- [4 Firmware](Noname_XL-LOGIC16-100M.html#Firmware) \- [5 Protocol](Noname_XL-LOGIC16-100M.html#Protocol) \- [6 Resources](Noname_XL-LOGIC16-100M.html#Resources) 
## Variants in same case The 2015-1-8 version of the [Mcupro_Logic16_clone](Mcupro_Logic16_clone.html "Mcupro Logic16 clone") comes in the same case as this device. Unlike this device, the mcupro version works with OpenTraceLab! ## Hardware A single Phillips head screw holds the case together. Most notable are the complete lack of test points or programming headers! There are some unpopulated resistor/capacitor pairs on the backside. \- **FPGA**: [Xilinx Spartan-3A XC3S200A](http://www.xilinx.com/support/index.html/content/xilinx/en/supportNav/silicon_devices/fpga/spartan-3a.html), 200K gates ([datasheeet](http://www.xilinx.com/support/documentation/data_sheets/ds529.pdf)) \- **USB interface chip**: [Cypress CY7C68013A-56PVXC (FX2LP)](http://www.cypress.com/?mpn=CY7C68013A-56PVXC) ([datasheet](http://www.cypress.com/?docID=34060)) \- **I2C EEPROM**: 2Kbit [Atmel 24C02B](http://www.atmel.com/devices/AT24C02B.aspx) (markings: "ATMEL317 24C02BN SU27 D") ([datasheet](http://www.atmel.com/Images/doc5126.pdf)) \- **16-Bit 2.5V to 3.3V/3.3V to 5V level shifting transceiver with 3-state outputs**: [TI SN74ALVC164245](http://www.ti.com/product/SN74ALVC164245) ([datasheet](http://www.ti.com/lit/gpn/sn74alvc164245)) \- **3.3V voltage regulator**: [Advanced Monolithic Systems AMS1117-3.3](http://www.advanced-monolithic.com/products/voltreg.html#1117) ([datasheet](http://ams-semitech.com/attachments/File/AMS1117_20120314.pdf), [older datasheet](http://www.advanced-monolithic.com/pdf/ds1117.pdf)) \- **1.2V voltage regulator**: [Advanced Monolithic Systems AMS1117-1.2](http://www.advanced-monolithic.com/products/voltreg.html#1117) ([datasheet](http://ams-semitech.com/attachments/File/AMS1117_20120314.pdf), [older datasheet](http://www.advanced-monolithic.com/pdf/ds1117.pdf)) \- **Crystal:** 24.000 Three LEDs (USB/green, COM/blue, and RUN/red) are on the board. ## Photos \- 
[![\1](../../assets/hardware/general/\2)](./File:Noname_xl_logic16_100m_package.jpg.html)
\- 
[![\1](../../assets/hardware/general/\2)](./File:Noname_xl_logic16_100m_device_top.jpg.html)
\- 
[![\1](../../assets/hardware/general/\2)](./File:Noname_xl_logic16_100m_device_bottom.jpg.html)
\- 
[![\1](../../assets/hardware/general/\2)](./File:Noname_xl_logic16_100m_device_usb.jpg.html)
\- 
[![\1](../../assets/hardware/general/\2)](./File:Noname_xl_logic16_100m_device_connector.jpg.html)
\- 
[![\1](../../assets/hardware/general/\2)](./File:Noname_xl_logic16_100m_pcb_top.jpg.html)
\- 
[![\1](../../assets/hardware/general/\2)](./File:Noname_xl_logic16_100m_pcb_bottom.jpg.html)
\- 
[![\1](../../assets/hardware/general/\2)](./File:Noname_xl_logic16_100m_xilinx_spartan_xc3s200a.jpg.html)
\- 
[![\1](../../assets/hardware/general/\2)](./File:Noname_xl_logic16_100m_cypress_fx2lp.jpg.html)
\- 
[![\1](../../assets/hardware/general/\2)](./File:Noname_xl_logic16_100m_ti_alvc164245.jpg.html)
\- 
[![\1](../../assets/hardware/general/\2)](./File:Noname_xl_logic16_100m_atmel_24c02bn.jpg.html)
\- 
[![\1](../../assets/hardware/general/\2)](./File:Noname_xl_logic16_100m_v05.jpg.html)
\- 
[![\1](../../assets/hardware/general/\2)](./File:Noname_xl_logic16_100m_ams1117_33.jpg.html)
\- 
[![\1](../../assets/hardware/general/\2)](./File:Noname_xl_logic16_100m_ams1117_12.jpg.html)
**Photos from another unit:** \- 
[![\1](../../assets/hardware/general/\2)](./File:Xl-logic16-100m-external.jpg.html)
\- 
[![\1](../../assets/hardware/general/\2)](./File:Xl-logic16-100m-pcb-top.jpg.html)
\- 
[![\1](../../assets/hardware/general/\2)](./File:Xl-logic16-100m-pcb-bottom.jpg.html)
**Photos from yet another unit (with JTAG and other resistor values):** \- 
[![\1](../../assets/hardware/general/\2)](./File:Xl-logic16-100m-v2-external.jpg.html)
\- 
[![\1](../../assets/hardware/general/\2)](./File:Xl-logic16-100m-v2-top.jpg.html)
\- 
[![\1](../../assets/hardware/general/\2)](./File:Xl-logic16-100m-v2-bottom.jpg.html)
**Photos from yet another unit (with black case):** \- 
[![\1](../../assets/hardware/general/\2)](./File:Xl_logic16_100m_black_device_top.jpg.html)
\- 
[![\1](../../assets/hardware/general/\2)](./File:Xl_logic16_100m_black_pcb_top.jpg.html)
\- 
[![\1](../../assets/hardware/general/\2)](./File:Xl_logic16_100m_black_pcb_bottom.jpg.html)
## Firmware You can use the [OpenTraceLab-fwextract-saleae-logic16](http://github.com/OpenTraceLab/?p=OpenTraceLab-util.git;a=tree;f=firmware/saleae-logic16) tool to extract (from the "Logic" Linux binary) the FX2 firmware and the FPGA bitstreams, exactly [as for a real Saleae Logic16](Saleae_Logic16.html "Saleae Logic16"). Note, the md5sum of the FX2 firmware is identical to the original Saleae firmware, but the FPGA bitstreams are different. Attempting to connect to this device with the "modified" FPGA bitstream, which \\_works\\_ with the vendor supplied "modified" Logic software fails to load in OpenTraceLab, with a FPGA version mismatch. The FX2 firmware loads successfully, at least in as much as the LED blinks a heartbeat pattern as expected. Update: July 4, 2015: marcus_c has written some open source fpga bitstream for spartan based logic16s, and \\_this\\_ bitstream does work with this device. However, at this time, binaries are not available. See [[1]](https://github.com/zeldin/logic16_bitstream) for the source. Update: September 3, 2015 blight has an alternative open source fpga bitstream. It also works. See [[2]](https://github.com/gregani/la16fw) for both source and binaries ## Protocol See [Saleae Logic16#Protocol](Saleae_Logic16.html#Protocol "Saleae Logic16"). ## Resources \- Random aliexpress.com vendors: [vendor1](http://www.aliexpress.com/item/Free-Shipping-Saleae-24MHz-8Channels-Logic-Analyzer-Fully-Checked-Best-quality-Input-buffered/1731200392.html), [vendor2](http://www.aliexpress.com/item/Saleae-logic16-USB-100MHz-Real-Time-Logic-Analyzers/1856825810.html)
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=Noname_XL-LOGIC16-100M&oldid=14397](https://OpenTraceLab.org/w/index.php?title=Noname_XL-LOGIC16-100M&oldid=14397)" 
[Categories](specialcategories-specialcategories.md): \- [Device](./Category:Device.html "Category:Device") \- [Logic analyzer](./Category:Logic_analyzer.html "Category:Logic analyzer") \- [In progress](./Category:In_progress.html "Category:In progress")

## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
