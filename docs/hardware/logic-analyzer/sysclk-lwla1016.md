# Sysclk Lwla1016

| | | |:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------------------:| | [![\1](../../assets/hardware/general/\2)](./File:Sysclk_lwla1016.png.html) | | | Status | supported | | Source code | [sysclk-lwla](http://github.com/OpenTraceLab/?p=OpenTraceCapture.git;a=tree;f=src/hardware/sysclk-lwla) | | Channels | 16/8 | | Samplerate | 100/200/250 MHz | | Samplerate (state) | ? | | Triggers | only in 100MHz mode | | Min/max voltage | ? | | Threshold voltage | ? | | Memory | 512Kbit/channel, or 256Kbit/channel with RLE | | Compression | optional RLE | | Website | [taobao.com](http://item.taobao.com/item.htm?id=12821371102) | **Sysclk LWLA1016** The **Sysclk LWLA1016** is a USB-based, 16-channel logic analyzer with up to 100MHz sampling rate, or up to 250MHz with 8 channels. Note that OpenTraceLab supports only the 100 MHz mode with 16 channels. Supporting the 200/250 MHz 8 channel modes is not worth the effort, since the device does not support triggers in these modes. A non-streaming device without triggers is pretty much useless for any real world application. See [Sysclk LWLA1016/Info](Sysclk_LWLA1016/Info.html "Sysclk LWLA1016/Info") for more details (such as **lsusb -v** output) about the device. 
## Contents 
\- [1 Hardware](Sysclk_LWLA1016.html#Hardware) \- [2 Photos](Sysclk_LWLA1016.html#Photos) \- [3 Protocol](Sysclk_LWLA1016.html#Protocol) \- [4 Firmware](Sysclk_LWLA1016.html#Firmware) \- [5 Resources](Sysclk_LWLA1016.html#Resources) 
## Hardware TODO. ## Photos \- 
[![\1](../../assets/hardware/general/\2)](./File:Sysclk_lwla1016_front.jpg.html)
Device, front
\- 
[![\1](../../assets/hardware/general/\2)](./File:Sysclk_lwla1016_device_back.jpg.html)
Device, back
\- 
[![\1](../../assets/hardware/general/\2)](./File:Sysclk_lwla1016_device_open.jpg.html)
Device, open
\- 
[![\1](../../assets/hardware/general/\2)](./File:Sysclk_lwla1016_pcb_top.jpg.html)
PCB, top
\- 
[![\1](../../assets/hardware/general/\2)](./File:Sysclk_lwla1016_pcb_bottom.jpg.html)
PCB, bottom
\- 
[![\1](../../assets/hardware/general/\2)](./File:Sysclk_lwla1016_pcb_cypress_fx2.jpg.html)
Cypress FX2
\- 
[![\1](../../assets/hardware/general/\2)](./File:Sysclk_lwla1016_pcb_issi_1.jpg.html)
ISSI 1
\- 
[![\1](../../assets/hardware/general/\2)](./File:Sysclk_lwla1016_pcb_issi2.jpg.html)
ISSI 2
\- 
[![\1](../../assets/hardware/general/\2)](./File:Sysclk_lwla1016_pcb_atmlh105.jpg.html)
ATMLH105
\- 
[![\1](../../assets/hardware/general/\2)](./File:Sysclk_lwla1016_stc_15f104e.jpg.html)
STC
\- 
[![\1](../../assets/hardware/general/\2)](./File:Sysclk_lwla1016_pcb_ldo.jpg.html)
LDOs
\- 
[![\1](../../assets/hardware/general/\2)](./File:Sysclk_lwla1016_pcb_input.jpg.html)
Input stage
\- 
[![\1](../../assets/hardware/general/\2)](./File:Sysclk_lwla1016_pcb_crystal.jpg.html)
Crystal
## Protocol Reverse engineering of the vendor's custom protocol is complete. See [Sysclk LWLA1016/Protocol](Sysclk_LWLA1016/Protocol.html "Sysclk LWLA1016/Protocol") for the findings gathered. ## Firmware In order to use this device you'll have to place the correct firmware files into a directory where [OpenTraceCapture](OpenTraceCapture.html "OpenTraceCapture") is looking for them. See [Firmware#Where_to_put_the_firmware_files](Firmware.html#Where_to_put_the_firmware_files "Firmware") for the OS-specific details. For the LWLA1016 we provide a [script](http://github.com/OpenTraceLab/?p=OpenTraceLab-util.git;a=tree;f=firmware/sysclk-lwla), which can extract them from the vendor software. First you'll need to install the (Windows) vendor software and grab a copy of its installation directory, e.g. **C:\Program Files\LWLA1016** (or similar, depends on where you installed). Then:  $ git clone git://OpenTraceLab.org/OpenTraceLab-util $ cd OpenTraceLab-util/firmware/sysclk-lwla $ ./OpenTraceLab-fwextract-sysclk-lwla1016 LWLA1016 [...] $ md5sum *.rbf 9ea144768afdd3092712075c23eadca4 sysclk-lwla1016-100.rbf 339d71ee799d3d3dbdcbcf1a00aa9f33 sysclk-lwla1016-100-ts.rbf 77fe7158ee53dcbed3bf390ee753594f sysclk-lwla1016-200.rbf e5246f3c1b9e3a34b570af9d50e02cbf sysclk-lwla1016-200-ts.rbf d9f587c9f53d0706f25658bc5580e4f7 sysclk-lwla1016-250.rbf 9d8c284bdbcfbad88aab9c2a79eb783d sysclk-lwla1016-250-ts.rbf  Finally, copy all the extracted **\\*.rbf** files to the [directory where OpenTraceCapture will look for them](Firmware.html#Where_to_put_the_firmware_files "Firmware"). ## Resources TODO. 
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=Sysclk_LWLA1016&oldid=11885](https://OpenTraceLab.org/w/index.php?title=Sysclk_LWLA1016&oldid=11885)" 
[Categories](specialcategories-specialcategories.md): \- [Device](./Category:Device.html "Category:Device") \- [Logic analyzer](./Category:Logic_analyzer.html "Category:Logic analyzer") \- [Supported](./Category:Supported.html "Category:Supported")

## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
