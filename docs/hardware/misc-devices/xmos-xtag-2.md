# Xmos Xtag 2
| | | |:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------:| | [*Image: \1* | | | Status | planned | | Channels | ???? | | Samplerate | 50MHz @ 2ch, 16MHz @ 7ch | | Samplerate (state) | ? | | Triggers | ? | | Min/max voltage | ? | | Threshold voltage | ? | | Memory | ? | | Compression | ? | | Website | [xmos.com](http://www.xmos.com/products/xkits/debug) | **XMOS XTAG-2** The **XMOS XTAG-2** is a USB based, ????-channel logic analyzer with up to 50MHz sampling rate. The XTAG-2 is actually a debug/eval board for XMOS ICs, but it can be used as a logic analyzer with a *firmware written by Henk Muller*. See *XMOS XTAG-2/Info* for more details (such as **lsusb -vvv** output) about the device.
## Contents
\- *1 Hardware* \- *2 Photos* \- *3 Protocol* \- *4 Resources*
## Hardware The main chip is an XMOS XS1-L1 [XS1-L01A-LQ64 Datasheet](https://www.xmos.com/en/download/public/XS1-L01A-LQ64-Datasheet%28X1135E%29.pdf). In the above picture, the 7-pin header markings are barely unreadable, but that's the jtag port for the xmos chip. From right to left: TDO, TDI, TCK, TMS, TRST#, RST# and GND. The secondary chip is an [SMSC HS Usb 2.0 transceiver](http://ww1.microchip.com/downloads/en/DeviceDoc/3310.pdf). ## Photos \-
[*Image: \1*
PCB, front
\-
[*Image: \1*
PCB, back
## Protocol TODO. ## Resources \- *XMOS project page of the logic analyzer firmware* \- [sw_logic_analyzer github repo](https://github.com/xcore/sw_logic_analyzer) \- [XTAG-2 quickstart guide](https://www.xmos.com/download/public/XTAG-2-Quick-Start-Guide\(1.1\).pdf) \- [XTAG-2 hardware manual](https://www.xmos.com/download/public/XTAG-2-Hardware-Manual\(1.0\).pdf) \- [XTAG-2 loader (binary)](https://www.xmos.com/download/public/XTAG-2-Loader-%28Binary%29%280.02%29.xe) \- [XTAG-2 design files](http://www.xmos.com/published/xtag-2-design-files)
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=XMOS_XTAG-2&oldid=8217](https://OpenTraceLab.org/w/index.php?title=XMOS_XTAG-2&oldid=8217)"
: \- *Device* \- *Logic analyzer* \- *Planned*
## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
