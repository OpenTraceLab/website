# Tektronix Tds2024B
| | | |:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------------------------:| | [*Image: \1* | | | Status | in progress | | Channels | 4 | | Samplerate | 2GS/s | | Analog bandwidth | 200MHz | | Vertical resolution | 8bits | | Triggers | edge, pulse width, composite video, alternate | | Display | 5.7" QVGA (320x240) | | Connectivity | USB host/device, GPIB | | Features | [tek.com](http://www.tek.com/oscilloscope/tds1001b-manual/tds1000b-and-tds2000b-series) | **Tektronix TDS2024B** The **Tektronix TDS2024B** is 4 channel oscilloscope with 2GS/s sampling rate, analog bandwidth of 200MHz and USB connectivity (optionally GPIB via the TEK-USB-488 adapter). See *Tektronix TDS2024B/Info* for more details (such as **lsusb -v** output) about the device. See *Tektronix TDS2000B series* for information common to all devices in this series.
## Contents
\- *1 Hardware* \- *2 Photos* \- *3 Usage* \- *4 Protocol* \- *5 Resources*
## Hardware ## Photos \-
[*Image: \1*
Device, front
## Usage Test your device for USB connection with Linux (also works in an VM): \$ **echo \\*IDN? \> /dev/usbtmc1 && cat /dev/usbtmc1** Output should be similar to this: `TEKTRONIX,TDS 2024B,C100044,CF:91.1CT FV:v22.16` ## Protocol See *Tektronix TDS2000B series#Protocol*. ## Resources \- [Tektronix forum: Data logging with TDS2024B](https://forum.tek.com/viewtopic.php?t=131908) \- [Tektronix forum: Save on Trigger example in Python TDS20xx](https://forum.tek.com/viewtopic.php?t=136170) \- [TDS2024B Read Waveform over USBTMC](https://github.com/ymei/USBScope)
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=Tektronix_TDS2024B&oldid=16432](https://OpenTraceLab.org/w/index.php?title=Tektronix_TDS2024B&oldid=16432)"
: \- *Device* \- *Oscilloscope* \- *In progress*
## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
