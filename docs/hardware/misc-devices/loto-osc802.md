# Loto Osc802

| | | |:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------------------------------------:| | [![\1](../../assets/hardware/general/\2)](./File:Loto_OSC802.jpg.html) | | | Status | planned | | Channels | 1 | | Samplerate | 1ch @ 80MHz | | Analog bandwidth | 20MHz | | Triggers | Hardware | | Memory | 64K/channel | | Connectivity | USB | | Website | [rockemb.com](http://www.rockemb.com/index.php?m=content&c=index&a=show&catid=96&id=105) | **Loto OSC802** The **Loto OSC802** is a USB-based, 2-channel oscilloscope with an analog bandwidth of 20MHz and 80MS/s sampling rate. See [Loto OSC802/Info](https://OpenTraceLab.org/w/index.php?title=Loto_OSC802/Info&action=edit&redlink=1 "Loto OSC802/Info \(page does not exist\)") for more details (such as **lsusb -v** output) about the device. See [Loto OSCxxx series](Loto_OSCxxx_series.html "Loto OSCxxx series") for information common to all devices in this series. 
## Contents 
\- [1 Hardware](Loto_OSC802.html#Hardware) \- [2 Photos](Loto_OSC802.html#Photos) \- [3 Protocol](Loto_OSC802.html#Protocol) \- [4 Resources](Loto_OSC802.html#Resources) 
## Hardware \- **Main chip**: [Altera MAX II EPM240](https://www.intel.com/content/www/us/en/products/programmable/cpld/max-ii.html) ([pin info](https://www.intel.com/content/dam/www/programmable/us/en/pdfs/literature/dp/max2/epm240.pdf) [device handbook](https://www.intel.com/content/dam/www/programmable/us/en/pdfs/literature/hb/max2/max2_mii5v1.pdf)) \- **8-Bit, 80 MSPS Dual A/D Converter**: Analog Devices AD9288 ([datasheet](https://www.analog.com/media/en/technical-documentation/data-sheets/ad9288.pdf)) \- **Main oscillator**: 80MHz 80.000 YX NH \- **USB**: Cypress CY7C68013A-100AXC (FX2LP) \- **64K x 16 high-speed CMOS static RAM**: 2x [ISSI IS61LV6416-8TI](http://www.issi.com/products-asynchronous-sram.htm) ([datasheet](http://www.issi.com/WW/pdf/61LV6416_L.pdf)) \- **I2C EEPROM**: Microchip 24LC02BI (for the USB VID/PID of the Cypress FX2LP) \- **Main power supply**: [TESLA A0505S-1W-DC isolation power chip 5V](https://www.chinahao.com/product/559725327304/) **Input stage (per channel):** \- **Analog Multiplexer/Demultiplexer**: [CD4052](http://www.ti.com/lit/ds/symlink/cd4051b.pdf) ## Photos \- 
[![\1](../../assets/hardware/general/\2)](./File:Loto_OSC802_01.jpg.html)
Inside
\- 
[![\1](../../assets/hardware/general/\2)](./File:Loto_OSC802_02.jpg.html)
Core part
\- 
[![\1](../../assets/hardware/general/\2)](./File:Loto_OSC802_03.jpg.html)
Back
\- 
[![\1](../../assets/hardware/general/\2)](./File:Loto_OSC802_04.jpg.html)
Communication part
## Protocol See [Loto OSCxxx series#Protocol](Loto_OSCxxx_series.html#Protocol "Loto OSCxxx series"). ## Resources \- [Brochure](http://www.rockemb.com/uploadfile/2019/0220/20190220114957785.pdf) \- [Vendor website](http://www.rockemb.com/index.php?m=content&c=index&a=show&catid=96&id=105)
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=Loto_OSC802&oldid=14678](https://OpenTraceLab.org/w/index.php?title=Loto_OSC802&oldid=14678)" 
[Categories](specialcategories-specialcategories.md): \- [Device](./Category:Device.html "Category:Device") \- [Oscilloscope](./Category:Oscilloscope.html "Category:Oscilloscope") \- [Planned](./Category:Planned.html "Category:Planned")

## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
