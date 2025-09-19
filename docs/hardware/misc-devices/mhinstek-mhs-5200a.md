# Mhinstek Mhs 5200A
| | | |:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:| | [*Image: \1* | | | Status | in progress | | Frequency (user) | 0.01Hz-6MHz/12MHz/20MHz/25Hz | | Waveforms | sine/square/triangle/sawtooth/arbitrary, TTL rect | | Amplitude | 20 V (open)/10 V (50 Ohm) (adjustable) | | Connectivity | USB/serial | | Website | *mhinstek.com* | **MHINSTEK MHS-5200A** The **MHINSTEK MHS-5200A** (-06M/12M/20M/25M) is a dual-channel, standalone function generator. It can be controlled with the push-buttons and the rotary encoder on the front panel, or via a USB interface. Amplitude and offset voltage can be controlled programmatically. Device also supports different measurements via 'Ext. In' or 'TTL' channels. It can measure: frequency, counter, pulse width, period and duty cycle.
## Contents
\- *1 Hardware (Q3 2016 model)*) \- *2 Photos* \- *3 Connection* \- *4 Protocol* \- *5 Resources*
## Hardware (Q3 2016 model) \- FPGA: Lattice MACH XO2 1200HC TQFP-100 \- Clock: unknown \- STM8S005K6 8-bit MCU with 32 Kbytes Flash, 16 MHz CPU, integrated 128 byte EEPROM *STM8S005K6 product page* \- Output stage: \- R2R-ladder 12bit DAC \- Signal/DC-offset sum: AD8017 Op-Amp \- Variable gain amplifier: AD603A \- Power amplifier: AD812A \- Output switch relais: 0db/-20db/off \- 24LC512 I²C EEPROM, 512Kb (64K x 8) for arbitrary waveform data \- 74AHC14D hex inverting schmitt trigger According to the specs, the hardware should run at 200MS/s, but measurement shows it only runs at ~175MS/s. ## Photos \-
[*Image: \1*
Device, front
\-
[*Image: \1*
Device, front
\-
[*Image: \1*
PCB, top
\-
[*Image: \1*
PCB, analog circuitry
\-
[*Image: \1*
PCB, bottom
\-
[*Image: \1*
2015 version PCB, with CH340
## Connection The generator has an internal PL2303 USB-to-serial converter. The VID/PID is 067b:2303. Communication parameters are 57600 bps, 8N1. The earlier 2015 version (firmware 4.22) has CH340 chip for USB-to serial converter, so the VID/PID is 1a86:7523, while rest of the components and functions remain unchanged. ## Protocol The generator uses a plain text protocol for communication. Each command (*set* or *read*) starts with ':' and has to be terminated with a newline, ASCII code 0x0a (but CRLF, i.e. 0x0d 0x0a, is also accepted). *Set* commands are acknowledged with an 'ok' response, *read* commands echo the request followed by the parameter value. ## Resources \- [analogzoo.com: MHS-5200A Teardown and Review](http://www.analogzoo.com/2015/08/mhs-5200a-teardown-and-review/) \- [eevblog.com: MHS-5200A Serial Protocol Reverse Engineered](http://www.eevblog.com/forum/testgear/mhs-5200a-serial-protocol-reverse-engineered/) \- [Google docs: MHS5200A Protocol](https://docs.google.com/document/d/1HbLQ4u87RJkD3Ktyw7k9U7Zh5BPNzbrhMlszNGdXiiY/edit)
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=MHINSTEK_MHS-5200A&oldid=16023](https://OpenTraceLab.org/w/index.php?title=MHINSTEK_MHS-5200A&oldid=16023)"
## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
