# Bbc Goertz Metrawatt M2110

| | | |:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------------------:| | [![\1](../../assets/hardware/general/\2)](./File:Bbc_gm_m2110_mugshot.png.html) | | | Status | supported | | Source code | [serial-dmm](http://github.com/OpenTraceLab/?p=OpenTraceCapture.git;a=tree;f=src/hardware/serial-dmm) | | Counts | 30000 | | Connectivity | RS232 | | Measurements | voltage, current, resistance, capacitance | | Features | manual range | **BBC Goertz Metrawatt M2110** The **BBC Goertz Metrawatt M2110** is a historic (about 1984) 30000 count bench multimeter with RS232 connectivity. It is possibly the oldest multimeter supported by [OpenTraceCapture](OpenTraceCapture.html "OpenTraceCapture"). A multimeter called **Metravo 5D** from the same manufacturer that seems to be the same model without RS232 port received the *iF design awards* in 1981. The manufacturer is called [Gossen Metrawatt](Gossen_Metrawatt.html "Gossen Metrawatt") today. 
## Contents 
\- [1 Hardware](BBC_Goertz_Metrawatt_M2110.html#Hardware) \- [2 Photos](BBC_Goertz_Metrawatt_M2110.html#Photos) \- [3 Protocol](BBC_Goertz_Metrawatt_M2110.html#Protocol) \- [4 Support in OpenTraceLab](BBC_Goertz_Metrawatt_M2110.html#Support_in_sigrok) \- [5 Resources](BBC_Goertz_Metrawatt_M2110.html#Resources) 
## Hardware **RS232 interface:** \- Baud rates 150/300/600/1200/2400/4800/9600, configurable via rotary switch \- 7 data bits \- No/even/odd parity bit, configurable via DIP switches \- 1 or 2 stop bits, configurable via DIP switch \- Optional CTS handshake, configurable via DIP switch \- Output intervals 0.66 s/10 s/1 min/10 min/1 h/manual/remote controlled, configurable via rotary switch \- Manual output sends value on button *Start/Reset* pressed \- Remote controlled output sends data on CTS set or ENQ sent, configurable via DIP switches \- Max. 1.5 measurements/s **RS232 cable:** \- 25 pin "female" connector \- Null modem cable required (DTE configuration)! ## Photos \- 
[![\1](../../assets/hardware/general/\2)](./File:Bbcg_m2110_1.JPG.html)
Front
\- 
[![\1](../../assets/hardware/general/\2)](./File:Bbcg_m2110_2.JPG.html)
Serial interface config
\- 
[![\1](../../assets/hardware/general/\2)](./File:Bbcg_m2110_3.JPG.html)
Top, right side
\- 
[![\1](../../assets/hardware/general/\2)](./File:Bbcg_m2110_4.JPG.html)
Top, back
\- 
[![\1](../../assets/hardware/general/\2)](./File:Bbcg_m2110_5.JPG.html)
Bottom
\- 
[![\1](../../assets/hardware/general/\2)](./File:Bbcg_m2110_6.JPG.html)
Wire clamps
\- 
[![\1](../../assets/hardware/general/\2)](./File:Bbcg_m2110_7.JPG.html)
Switched on, with measurement leads
## Protocol msg := SDDDDDD | 'OVERRNG' CR LF S := '-' | ' ' D := '0'..'9'|'.'  Unfortunately the device does not send the measured unit. ## Support in OpenTraceLab The device is supported by the driver **bbcgm-m2110** in modes that send data automatically or manually. Polling is not implemented. The device does not send the measured quantity or unit via the serial interface, just the value. The device detection requires a message to be sent by the device within 1s. The default serial port parameters are 1200/7n2. After power on or configuration changes the button *Start/Reset* must be pressed at least once to initiate sending. ## Resources \- Manual (PDF) available from [Gossen Metrawatt](Gossen_Metrawatt.html "Gossen Metrawatt") customer support. \- [_Metravo 5D_ in _iF online exibition_](http://exhibition.ifdesign.de/entrydetails_en.html?beitrag_id=11387)
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=BBC_Goertz_Metrawatt_M2110&oldid=10061](https://OpenTraceLab.org/w/index.php?title=BBC_Goertz_Metrawatt_M2110&oldid=10061)" 
[Categories](specialcategories-specialcategories.md): \- [Device](./Category:Device.html "Category:Device") \- [Multimeter](./Category:Multimeter.html "Category:Multimeter") \- [Supported](./Category:Supported.html "Category:Supported")

## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
