# Sainsmart Dds120

| | | |:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------------------------------:| | [![\1](../../assets/hardware/general/\2)](./File:Dds120_mugshot.png.html) | | | Status | supported | | Source code | [hantek-6xxx](http://github.com/OpenTraceLab/?p=OpenTraceCapture.git;a=tree;f=src/hardware/hantek-6xxx) | | Channels | 2 | | Samplerate | 50MHz | | Analog bandwidth | 20MHz | | Vertical resolution | 8bit | | Triggers | none (SW-only) | | Input impedance | 1MΩ‖25pF | | Memory | none | | Display | none | | Connectivity | USB | | Website | [sainsmart.com](http://www.sainsmart.com/sainsmart-dds-120-20m-50m-s-virtual-oscilloscope-silver.html) | **SainSmart DDS120** The **SainSmart DDS120** is a USB-based, 2-channel oscilloscope with an analog bandwidth of 20MS/s and 50MS/s sampling rate. This device appears to be a rebadge of the [Rocktech BM102](Rocktech_BM102.html "Rocktech BM102") (or vice versa). The [lsusb](SainSmart_DDS120/Info.html "SainSmart DDS120/Info") is exactly the same, the PCB is exactly the same (both have a "656517" and "102LJT1402" silkscreen), and the components used appear to be the same as well. The device was apparently [created by someone named "buudai"](https://translate.google.de/translate?sl=auto&tl=en&js=y&prev=_t&hl=en&ie=UTF-8&u=https%3A%2F%2Fweb.archive.org%2Fweb%2F20140520231246%2Fhttp%3A%2F%2Fbbs.21ic.com%2Ficview-350047-1-1.html&edit-text=&act=url) in 2012 (also reflected in the [lsusb](SainSmart_DDS120/Info.html "SainSmart DDS120/Info") and in the former [buudai.com](https://web.archive.org/web/20130403082149/http://www.buudai.com/) website). See [SainSmart DDS120/Info](SainSmart_DDS120/Info.html "SainSmart DDS120/Info") for more details (such as **lsusb -v** output) about the device. 
## Contents 
\- [1 Hardware](SainSmart_DDS120.html#Hardware) \- [2 Photos](SainSmart_DDS120.html#Photos) \- [3 Protocol](SainSmart_DDS120.html#Protocol) \- [4 Firmware](SainSmart_DDS120.html#Firmware) \- [5 Resources](SainSmart_DDS120.html#Resources) 
## Hardware \- **USB**: [Cypress CY7C68013A-100AXC](http://www.cypress.com/documentation/datasheets/cy7c68013a-cy7c68014a-cy7c68015a-cy7c68016a-ez-usb-fx2lp-usb) (FX2LP) ([datasheet](http://www.cypress.com/file/138911/download)) \- **64-kbyte I²C EEPROM**: [Microchip 24LC64I](http://www.microchip.com/wwwproducts/Devices.aspx?dDocName=en010831) ([datasheet](http://ww1.microchip.com/downloads/en/DeviceDoc/21189f.pdf)) \- **Crystal**: 24MHz \- **145 MHz FastFET Opamps**: [AD8065ART-R2](http://www.analog.com/en/products/amplifiers/operational-amplifiers/jfet-input-amplifiers/ad8065.html#product-overview): ([datasheet](http://www.analog.com/static/imported-files/data_sheets/AD8065_8066.pdf)) **Or in newer hardware:** \- **Dual 8bit, 100MSPS ADC**: [MXTronix MXT2088](https://translate.google.com/translate?hl=en&sl=zh-CN&tl=en&u=http%3A%2F%2Fwww.mxtronics.com%2Fn107%2Fn124%2Fn181%2Fn184%2Fc692%2Fcontent.html) ([datasheet](http://www.mxtronics.com/n107/n124/n181/n184/c692/attr/2630.pdf)) \- **145 MHz FastFET Opamps**: [AD8065](http://www.analog.com/en/products/amplifiers/operational-amplifiers/jfet-input-amplifiers/ad8065.html#product-overview): ([datasheet](http://www.analog.com/static/imported-files/data_sheets/AD8065_8066.pdf)) \- 4x **CMOS differential 4-channel analog mux/demux with logic-level conversion**: [Texas Instruments CD4052B(M)](http://www.ti.com/product/cd4052b/description) ([datasheet](http://www.ti.com/lit/gpn/cd4052b)) ## Photos **Teardown 1**: \- 
[![\1](../../assets/hardware/general/\2)](./File:Dds120_mugshot.png.html)
Device, top
\- 
[![\1](../../assets/hardware/general/\2)](./File:DDS120_Top_20141024_0540p.jpg.html)
PCB, front
\- 
[![\1](../../assets/hardware/general/\2)](./File:Sainsmart_dds120_front_1.jpg.html)
PCB, front
\- 
[![\1](../../assets/hardware/general/\2)](./File:Sainsmart_dds120_front_2.jpg.html)
PCB, front
\- 
[![\1](../../assets/hardware/general/\2)](./File:Sainsmart_dds120_front_3.jpg.html)
PCB, front
\- 
[![\1](../../assets/hardware/general/\2)](./File:Sainsmart_dds120_front_4.jpg.html)
PCB, front
\- 
[![\1](../../assets/hardware/general/\2)](./File:Sainsmart_dds120_front_5.jpg.html)
PCB, front
\- 
[![\1](../../assets/hardware/general/\2)](./File:Sainsmart_dds120_back_1.jpg.html)
PCB, back
\- 
[![\1](../../assets/hardware/general/\2)](./File:Sainsmart_dds120_back_2.jpg.html)
PCB, back
\- 
[![\1](../../assets/hardware/general/\2)](./File:Sainsmart_dds120_box_1.jpg.html)
Box
\- 
[![\1](../../assets/hardware/general/\2)](./File:Sainsmart_dds120_box_2.jpg.html)
Box
\- 
[![\1](../../assets/hardware/general/\2)](./File:Sainsmart_dds120_box_3.jpg.html)
Box
**Teardown 2 (purchased 03/2016)**: \- 
[![\1](../../assets/hardware/general/\2)](./File:Saintsmart_dds120_sticker.jpg.html)
Sticker
\- 
[![\1](../../assets/hardware/general/\2)](./File:Saintsmart_dds120_package_contents.jpg.html)
Package contents
\- 
[![\1](../../assets/hardware/general/\2)](./File:Saintsmart_dds120_device_top.jpg.html)
Device, top
\- 
[![\1](../../assets/hardware/general/\2)](./File:Saintsmart_dds120_device_bottom.jpg.html)
Device, bottom
\- 
[![\1](../../assets/hardware/general/\2)](./File:Saintsmart_dds120_usb.jpg.html)
USB
\- 
[![\1](../../assets/hardware/general/\2)](./File:Saintsmart_dds120_connectors.jpg.html)
Connectors
\- 
[![\1](../../assets/hardware/general/\2)](./File:Saintsmart_dds120_pcb_top.jpg.html)
PCB, top
\- 
[![\1](../../assets/hardware/general/\2)](./File:Saintsmart_dds120_pcb_bottom.jpg.html)
PCB, bottom
\- 
[![\1](../../assets/hardware/general/\2)](./File:Saintsmart_dds120_mxt2088.jpg.html)
MXTronix MXT2088
\- 
[![\1](../../assets/hardware/general/\2)](./File:Saintsmart_dds120_fx2.jpg.html)
Cypress FX2
\- 
[![\1](../../assets/hardware/general/\2)](./File:Saintsmart_dds120_microchip_24lc64i.jpg.html)
Microchip 24LC64I
\- 
[![\1](../../assets/hardware/general/\2)](./File:Saintsmart_dds120_ti_cd4052bm.jpg.html)
TI CD4052BM
\- 
[![\1](../../assets/hardware/general/\2)](./File:Saintsmart_dds120_ams1117-3.3.jpg.html)
AMS1117-3.3
\- 
[![\1](../../assets/hardware/general/\2)](./File:Saintsmart_dds120_nais_210eh_347.jpg.html)
Unknown IC
## Protocol We use an open-source firmware for this device (i.e., not the vendor firmware/protocol), hence we do not need to know the vendor protocol. There is some [historic vendor firmware/protocol info](SainSmart_DDS120/Info.html#Vendor_firmware "SainSmart DDS120/Info") for those interested, though. ## Firmware In order to use this device, the [OpenTraceLab-firmware-fx2lafw](Fx2lafw.html "Fx2lafw") (\>= 0.1.4) firmware is required. The firmware was originally written by Jochen Hoenicke (see [README](http://github.com/OpenTraceLab/?p=OpenTraceLab-firmware-fx2lafw.git;a=blob;f=README) for details), thanks a lot! **Note**: The firmware is **not** flashed into the device permanently! You only need to make it available in the usual place where [OpenTraceCapture](OpenTraceCapture.html "OpenTraceCapture") looks for firmware files, it will be used automatically (and "uploaded" to the Cypress FX2's SRAM every time you attach the device to a USB port). **Note**: On Windows, you will have to [assign the WinUSB driver via Zadig](Windows.html#Device_specific_USB_driver "Windows") **twice**: the first time for the initial USB VID/PID the device has when attaching it via USB (04b4:602a or 04b5:602a, depending on which vendor driver is currently being used by the device), and a second time after the firmware has been uploaded to the device and the device has "renumerated" with a different VID/PID pair (1d50:608e). See [this section](SainSmart_DDS120/Info.html#Open-source_firmware_details "SainSmart DDS120/Info") for technical details about the firmware/hardware. ## Resources \- [EEVBlog forum thread](http://www.eevblog.com/forum/testgear/sainsmart-dds120-usb-oscilloscope-\(buudai-bm102\)/) \- [Detailed description of the hardware](http://www.360customs.de/en/2014/10/usb-oszilloskop-sainsmart-dds120-2-kanal-20mhz-50msps-buudairocktech-bm102/) \- [Vendor product page](http://www.sainsmart.com/sainsmart-dds-120-20m-50m-s-virtual-oscilloscope-silver.html) \- [Vendor software download links](https://www.eevblog.com/forum/testgear/saintsmart-dds120-software-download/msg818124/#msg818124)
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=SainSmart_DDS120&oldid=13748](https://OpenTraceLab.org/w/index.php?title=SainSmart_DDS120&oldid=13748)" 
[Categories](specialcategories-specialcategories.md): \- [Device](./Category:Device.html "Category:Device") \- [Oscilloscope](./Category:Oscilloscope.html "Category:Oscilloscope") \- [Supported](./Category:Supported.html "Category:Supported")

## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
