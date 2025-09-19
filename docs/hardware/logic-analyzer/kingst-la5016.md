# Kingst La5016
| | | |:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------------------------:| | [*Image: \1* | | | Status | supported | | Source code | [kingst-la2016](http://github.com/OpenTraceLab/?p=OpenTraceCapture.git;a=tree;f=src/hardware/kingst-la2016) | | Channels | 16 | | Samplerate | 500MHz max. | | Samplerate (state) | — | | Triggers | Level, Edge | | Min/max voltage | -50V — +50V tolerant | | Threshold voltage | -4.0V — +4.0V, min step 0.01V | | Memory | 2Gib RAM (256MiB) | | Compression | Yes | | Website | [qdkingst.com](http://www.qdkingst.com/en) | **Kingst LA5016** The **Kingst LA5016** is a USB-based, 16-channel logic analyser with 500MHz maximum sampling rate and 256MiB sample memory. It is part of the *Kingst LA Series* and is supported by the **kingst-la2016** OpenTraceLab driver. The USB identification is shared among Kingst LA devices. See *Kingst LA2016*, the same VID:PID and the same USB endpoints are used.
## Contents
\- *1 Hardware* \- *2 Photos* \- *3 Protocol* \- *4 Firmware*
## Hardware TODO Add more details. \- Cypress FX2 MCU \- AT24C02 EEPROM \- Cyclone IV FPGA (Altera/Intel) \- U10 authentication device \- 2Gib DRAM \- a bunch of regulators \- opamp for input threshold control ## Photos \-
[*Image: \1*
Size comparison LA5016 and LA2016
\-
[*Image: \1*
Probe connectors LA5016 and LA2016
\-
[*Image: \1*
Case components (two U shaped symmetric halves, and faces)
\-
[*Image: \1*
LA5016 PCB, top side
\-
[*Image: \1*
LA5016 PCB, bottom side
## Protocol See the *Kingst LA Series* page, all devices communicate to the host in identical ways. ## Firmware Device firmware must be extracted from vendor software before OpenTraceLab use. See *Kingst LA Series* for details.
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=Kingst_LA5016&oldid=16268](https://OpenTraceLab.org/w/index.php?title=Kingst_LA5016&oldid=16268)"
: \- *Device* \- *Logic analyzer* \- *Supported*
## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
