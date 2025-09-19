# Sysclk Lwla1016
| | | |:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------------------:| | [*Image: \1* | | | Status | supported | | Source code | [sysclk-lwla](http://github.com/OpenTraceLab/?p=OpenTraceCapture.git;a=tree;f=src/hardware/sysclk-lwla) | | Channels | 16/8 | | Samplerate | 100/200/250 MHz | | Samplerate (state) | ? | | Triggers | only in 100MHz mode | | Min/max voltage | ? | | Threshold voltage | ? | | Memory | 512Kbit/channel, or 256Kbit/channel with RLE | | Compression | optional RLE | | Website | [taobao.com](http://item.taobao.com/item.htm?id=12821371102) | **Sysclk LWLA1016** The **Sysclk LWLA1016** is a USB-based, 16-channel logic analyzer with up to 100MHz sampling rate, or up to 250MHz with 8 channels. Note that OpenTraceLab supports only the 100 MHz mode with 16 channels. Supporting the 200/250 MHz 8 channel modes is not worth the effort, since the device does not support triggers in these modes. A non-streaming device without triggers is pretty much useless for any real world application. See *Sysclk LWLA1016/Info* for more details (such as **lsusb -v** output) about the device.
## Contents
\- *1 Hardware* \- *2 Photos* \- *3 Protocol* \- *4 Firmware* \- *5 Resources*
## Hardware TODO. ## Photos \-
[*Image: \1*
Device, front
\-
[*Image: \1*
Device, back
\-
[*Image: \1*
Device, open
\-
[*Image: \1*
PCB, top
\-
[*Image: \1*
PCB, bottom
\-
[*Image: \1*
Cypress FX2
\-
[*Image: \1*
ISSI 1
\-
[*Image: \1*
ISSI 2
\-
[*Image: \1*
ATMLH105
\-
[*Image: \1*
STC
\-
[*Image: \1*
LDOs
\-
[*Image: \1*
Input stage
\-
[*Image: \1*
Crystal
## Protocol Reverse engineering of the vendor's custom protocol is complete. See *Sysclk LWLA1016/Protocol* for the findings gathered. ## Firmware In order to use this device you'll have to place the correct firmware files into a directory where *OpenTraceCapture* is looking for them. See *Firmware#Where_to_put_the_firmware_files* for the OS-specific details. For the LWLA1016 we provide a [script](http://github.com/OpenTraceLab/?p=OpenTraceLab-util.git;a=tree;f=firmware/sysclk-lwla), which can extract them from the vendor software. First you'll need to install the (Windows) vendor software and grab a copy of its installation directory, e.g. **C:\Program Files\LWLA1016** (or similar, depends on where you installed). Then:  $ git clone git://OpenTraceLab.org/OpenTraceLab-util $ cd OpenTraceLab-util/firmware/sysclk-lwla $ ./OpenTraceLab-fwextract-sysclk-lwla1016 LWLA1016 [...] $ md5sum *.rbf 9ea144768afdd3092712075c23eadca4 sysclk-lwla1016-100.rbf 339d71ee799d3d3dbdcbcf1a00aa9f33 sysclk-lwla1016-100-ts.rbf 77fe7158ee53dcbed3bf390ee753594f sysclk-lwla1016-200.rbf e5246f3c1b9e3a34b570af9d50e02cbf sysclk-lwla1016-200-ts.rbf d9f587c9f53d0706f25658bc5580e4f7 sysclk-lwla1016-250.rbf 9d8c284bdbcfbad88aab9c2a79eb783d sysclk-lwla1016-250-ts.rbf  Finally, copy all the extracted **\\*.rbf** files to the *directory where OpenTraceCapture will look for them*. ## Resources TODO.
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=Sysclk_LWLA1016&oldid=11885](https://OpenTraceLab.org/w/index.php?title=Sysclk_LWLA1016&oldid=11885)"
: \- *Device* \- *Logic analyzer* \- *Supported*
## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
