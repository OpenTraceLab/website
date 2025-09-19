# Sainsmart Dds120
| | | |:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------------------------------:| | [*Image: \1* | | | Status | supported | | Source code | [hantek-6xxx](http://github.com/OpenTraceLab/?p=OpenTraceCapture.git;a=tree;f=src/hardware/hantek-6xxx) | | Channels | 2 | | Samplerate | 50MHz | | Analog bandwidth | 20MHz | | Vertical resolution | 8bit | | Triggers | none (SW-only) | | Input impedance | 1MΩ‖25pF | | Memory | none | | Display | none | | Connectivity | USB | | Website | *sainsmart.com* | **SainSmart DDS120** The **SainSmart DDS120** is a USB-based, 2-channel oscilloscope with an analog bandwidth of 20MS/s and 50MS/s sampling rate. This device appears to be a rebadge of the *Rocktech BM102* (or vice versa). The *lsusb* is exactly the same, the PCB is exactly the same (both have a "656517" and "102LJT1402" silkscreen), and the components used appear to be the same as well. The device was apparently *created by someone named "buudai"* in 2012 (also reflected in the *lsusb* and in the former [buudai.com](https://web.archive.org/web/20130403082149/http://www.buudai.com/) website). See *SainSmart DDS120/Info* for more details (such as **lsusb -v** output) about the device.
## Contents
\- *1 Hardware* \- *2 Photos* \- *3 Protocol* \- *4 Firmware* \- *5 Resources*
## Hardware \- **USB**: [Cypress CY7C68013A-100AXC](http://www.cypress.com/documentation/datasheets/cy7c68013a-cy7c68014a-cy7c68015a-cy7c68016a-ez-usb-fx2lp-usb) (FX2LP) ([datasheet](http://www.cypress.com/file/138911/download)) \- **64-kbyte I²C EEPROM**: [Microchip 24LC64I](http://www.microchip.com/wwwproducts/Devices.aspx?dDocName=en010831) ([datasheet](http://ww1.microchip.com/downloads/en/DeviceDoc/21189f.pdf)) \- **Crystal**: 24MHz \- **145 MHz FastFET Opamps**: *AD8065ART-R2*: ([datasheet](http://www.analog.com/static/imported-files/data_sheets/AD8065_8066.pdf)) **Or in newer hardware:** \- **Dual 8bit, 100MSPS ADC**: *MXTronix MXT2088* ([datasheet](http://www.mxtronics.com/n107/n124/n181/n184/c692/attr/2630.pdf)) \- **145 MHz FastFET Opamps**: *AD8065*: ([datasheet](http://www.analog.com/static/imported-files/data_sheets/AD8065_8066.pdf)) \- 4x **CMOS differential 4-channel analog mux/demux with logic-level conversion**: [Texas Instruments CD4052B(M)](http://www.ti.com/product/cd4052b/description) ([datasheet](http://www.ti.com/lit/gpn/cd4052b)) ## Photos **Teardown 1**: \-
[*Image: \1*
Device, top
\-
[*Image: \1*
PCB, front
\-
[*Image: \1*
PCB, front
\-
[*Image: \1*
PCB, front
\-
[*Image: \1*
PCB, front
\-
[*Image: \1*
PCB, front
\-
[*Image: \1*
PCB, front
\-
[*Image: \1*
PCB, back
\-
[*Image: \1*
PCB, back
\-
[*Image: \1*
Box
\-
[*Image: \1*
Box
\-
[*Image: \1*
Box
**Teardown 2 (purchased 03/2016)**: \-
[*Image: \1*
Sticker
\-
[*Image: \1*
Package contents
\-
[*Image: \1*
Device, top
\-
[*Image: \1*
Device, bottom
\-
[*Image: \1*
USB
\-
[*Image: \1*
Connectors
\-
[*Image: \1*
PCB, top
\-
[*Image: \1*
PCB, bottom
\-
[*Image: \1*
MXTronix MXT2088
\-
[*Image: \1*
Cypress FX2
\-
[*Image: \1*
Microchip 24LC64I
\-
[*Image: \1*
TI CD4052BM
\-
[*Image: \1*
AMS1117-3.3
\-
[*Image: \1*
Unknown IC
## Protocol We use an open-source firmware for this device (i.e., not the vendor firmware/protocol), hence we do not need to know the vendor protocol. There is some *historic vendor firmware/protocol info* for those interested, though. ## Firmware In order to use this device, the *OpenTraceLab-firmware-fx2lafw* (\>= 0.1.4) firmware is required. The firmware was originally written by Jochen Hoenicke (see [README](http://github.com/OpenTraceLab/?p=OpenTraceLab-firmware-fx2lafw.git;a=blob;f=README) for details), thanks a lot! **Note**: The firmware is **not** flashed into the device permanently! You only need to make it available in the usual place where *OpenTraceCapture* looks for firmware files, it will be used automatically (and "uploaded" to the Cypress FX2's SRAM every time you attach the device to a USB port). **Note**: On Windows, you will have to *assign the WinUSB driver via Zadig* **twice**: the first time for the initial USB VID/PID the device has when attaching it via USB (04b4:602a or 04b5:602a, depending on which vendor driver is currently being used by the device), and a second time after the firmware has been uploaded to the device and the device has "renumerated" with a different VID/PID pair (1d50:608e). See *this section* for technical details about the firmware/hardware. ## Resources \- [EEVBlog forum thread](http://www.eevblog.com/forum/testgear/sainsmart-dds120-usb-oscilloscope-\(buudai-bm102\)/) \- [Detailed description of the hardware](http://www.360customs.de/en/2014/10/usb-oszilloskop-sainsmart-dds120-2-kanal-20mhz-50msps-buudairocktech-bm102/) \- *Vendor product page* \- [Vendor software download links](https://www.eevblog.com/forum/testgear/saintsmart-dds120-software-download/msg818124/#msg818124)
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=SainSmart_DDS120&oldid=13748](https://OpenTraceLab.org/w/index.php?title=SainSmart_DDS120&oldid=13748)"
: \- *Device* \- *Oscilloscope* \- *Supported*
## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
