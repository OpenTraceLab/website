# Loto Oscxxx Series
| | | |:----------------------|------------------------------------------------------------------------------------------------------------------------------------------------| | Status | planned | | Channels | 2 analog (all models) + trigger | | Samplerate | 50-200 MSa/s (by channel in dual channel) | | Samplerate (eq. time) | 0.2-1 GSa/s (dual channel combined or single channel) | | Analog bandwidth | 20-50 MHz (depending on model) | | Vertical resolution | 8bits | | Triggers | edge, pulse width, slope, video, alternate | | Input impedance | 1MΩ‖25pF±5pF | | Memory | 64Kpts (by channel, 128K total) | | Connectivity | USB host and device | | Features | math: + / — / x / FFT / Digital decoder | | Website | [rockemb.com](http://www.rockemb.com/index.php?m=content&c=index&a=lists&catid=96) | **Loto OSCxxx series** The **Loto OSCxxx series** are compact and portable digital storage oscilloscopes, produced by Rocktech.
## Contents
\- *1 Devices* \- *2 Protocol* \- *2.1 OSC802* \- *3 Resources*
## Devices | | | | | | |-----------------------------------------------|-----------------|--------------------------|---------------|------------------------------| | Model | Bandwidth (MHz) | Sample Rate (MS/s by ch) | USB VID/PID | Notes | | Loto OSCH02 | 100 | 250 | 0x8312:0x8a2a | Rel. 2020 (250MSa just CH-A) | | Loto OSC2002 | 50 | 200 | 0x8312:0x8801 | 2018-2019 edition | | Loto OSCA02 | 35 | 100 | 0x8312:0x8a02 | | | *Loto OSC802* | 25 | 80 | 0x8312:0x8312 | | | Loto OSC482 | 20 | 50 | 0x8102:0x8102 | | | Loto BM102 | 20 | 50 | 0x8102:0x8102 | out of production | | Loto OSCE02 | 50 | 200 | 0x8312:0x8101 | | ## Protocol ### OSC802 Commands sent via Control Transfer to EP0. Samples buffer available on Bulk EP. List of commands (provisional):  Request Type | Request | Value | Index | Data | Description
---|---|---|---|---|---
0x80 | 0x33 | 0x00 | 0x00 | 1 byte | _Start acquisition._
0x80 | 0x50 | 0x00 | 0x00 | 1 byte | _Check if acquisition buffer is ready. Write 0x21 in the data byte if ready._
0x80 | 0x94 | value | 0x00 | 1 byte | _Set sampling rate with value[0-3] and AC/DC for Channel 1 with value[4]._ _Rate values: 80MSa/s (B0000), 10MSa/s (B1000), 625KSa/s (B1100)_ _value[4] = 1 - > DC coupling, value[4] = 0 -> AC coupling_
0x80 | 0x22 0x23 0x24 | value | 0x00 | 1 byte | _Set Channel 1 and Channel 2 voltage. Set AC/DC for Channel 2._
0x80 | 0xE7 | value | 0x00 | 1 byte | _Enable (value=1) or disable (value=0) hardware trigger on Channel 1._
0x80 | 0xC5 | value | 0x00 | 1 byte | _Set trigger slope up (value=1) or down (value=0)._
0x80 | 0x16 | value | 0x00 | 1 byte | _Set trigger level (value=0-255)._
## Resources \- [Vendor website](http://www.rockemb.com/index.php?m=content&c=index&a=lists&catid=96) \- [Forum](http://bbs.lotoins.com/)
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=Loto_OSCxxx_series&oldid=15205](https://OpenTraceLab.org/w/index.php?title=Loto_OSCxxx_series&oldid=15205)"
: \- *Device* \- *Oscilloscope* \- *Planned*
## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
