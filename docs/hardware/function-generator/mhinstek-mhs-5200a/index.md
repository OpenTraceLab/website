---
title: MHINSTEK MHS-5200A
---

# MHINSTEK MHS-5200A

<div class="infobox" markdown>

![MHINSTEK MHS-5200A](./img/MHINSTEK_MHS-5200A_analog.jpg){ .infobox-image }

### MHINSTEK MHS-5200A

| | |
|---|---|
| **Status** | in progress |
| **Frequency (user)** | 0.01Hz-6MHz/12MHz/20MHz/25Hz |
| **Waveforms** | sine/square/triangle/sawtooth/arbitrary, TTL rect |
| **Amplitude** | 20 V (open)/10 V (50 Ohm) (adjustable) |
| **Connectivity** | USB/serial |
| **Website** | [mhinstek.com](https://translate.googleusercontent.com/translate_c?depth=1&amp;hl=en&amp;ie=UTF8&amp;prev=_t&amp;rurl=translate.google.com&amp;sl=auto&amp;sp=nmt4&amp;tl=en&amp;u=http://www.mhinstek.com/product/html/%3F88.html&amp;xid=17259,1500003,15700002,15700022,15700124,15700149,15700168,15700173,15700186,15700190,15700201&amp;usg=ALkJrhj5uwzXTjOX5J5IsZRbjEe2d8Li_w) |

</div>

The **MHINSTEK MHS-5200A** (-06M/12M/20M/25M) is a dual-channel, standalone function generator. It can be controlled with the push-buttons and the rotary
encoder on the front panel, or via a USB interface.

Amplitude and offset voltage can be controlled programmatically.

Device also supports different measurements via 'Ext. In' or 'TTL' channels. It can measure: frequency, counter, pulse width, period and duty cycle.

## Hardware (Q3 2016 model)
- FPGA: Lattice MACH XO2 1200HC TQFP-100
- Clock: unknown
- STM8S005K6 8-bit MCU with 32 Kbytes Flash, 16 MHz CPU, integrated 128 byte EEPROM [STM8S005K6 product page](http://www.st.com/en/microcontrollers/stm8s005k6.html)
- Output stage:
R2R-ladder 12bit DAC
- Signal/DC-offset sum: AD8017 Op-Amp
- Variable gain amplifier: AD603A
- Power amplifier: AD812A
- Output switch relais: 0db/-20db/off
- 24LC512 I²C EEPROM, 512Kb (64K x 8) for arbitrary waveform data
- 74AHC14D hex inverting schmitt trigger

According to the specs, the hardware should run at 200MS/s, but measurement shows it only runs at ~175MS/s.

## Photos

<div class="photo-grid" markdown>

[![Mhinstek Mhs 5200a Analog](./img/MHINSTEK_MHS-5200A_analog.jpg)](./img/MHINSTEK_MHS-5200A_analog.jpg "Mhinstek Mhs 5200a Analog"){ .glightbox data-gallery="mhinstek-mhs-5200a" }
<span class="caption">Mhinstek Mhs 5200a Analog</span>

[![Mhinstek Mhs 5200a Back](./img/MHINSTEK_MHS-5200A_back.jpg)](./img/MHINSTEK_MHS-5200A_back.jpg "Mhinstek Mhs 5200a Back"){ .glightbox data-gallery="mhinstek-mhs-5200a" }
<span class="caption">Mhinstek Mhs 5200a Back</span>

[![Mhinstek Mhs 5200a Persp](./img/MHINSTEK_MHS-5200A_persp.jpg)](./img/MHINSTEK_MHS-5200A_persp.jpg "Mhinstek Mhs 5200a Persp"){ .glightbox data-gallery="mhinstek-mhs-5200a" }
<span class="caption">Mhinstek Mhs 5200a Persp</span>

[![Mhinstek Mhs 5200a Startscreen2](./img/MHINSTEK_MHS-5200A_startscreen2.jpg)](./img/MHINSTEK_MHS-5200A_startscreen2.jpg "Mhinstek Mhs 5200a Startscreen2"){ .glightbox data-gallery="mhinstek-mhs-5200a" }
<span class="caption">Mhinstek Mhs 5200a Startscreen2</span>

[![Mhinstek Mhs 5200a Base](./img/MHINSTEK_MHS-5200A_base.jpg)](./img/MHINSTEK_MHS-5200A_base.jpg "Mhinstek Mhs 5200a Base"){ .glightbox data-gallery="mhinstek-mhs-5200a" }
<span class="caption">Mhinstek Mhs 5200a Base</span>

[![Mhinstek Mhs 5200a Ch340](./img/MHINSTEK_MHS-5200A_CH340.jpg)](./img/MHINSTEK_MHS-5200A_CH340.jpg "Mhinstek Mhs 5200a Ch340"){ .glightbox data-gallery="mhinstek-mhs-5200a" }
<span class="caption">Mhinstek Mhs 5200a Ch340</span>

[![Mhinstek Mhs 5200a Startscreen1](./img/MHINSTEK_MHS-5200A_startscreen1.jpg)](./img/MHINSTEK_MHS-5200A_startscreen1.jpg "Mhinstek Mhs 5200a Startscreen1"){ .glightbox data-gallery="mhinstek-mhs-5200a" }
<span class="caption">Mhinstek Mhs 5200a Startscreen1</span>

</div>
## Connection

The generator has an internal PL2303 USB-to-serial converter. The VID/PID is 067b:2303. Communication parameters are 57600 bps, 8N1.

The earlier 2015 version (firmware 4.22) has CH340 chip for USB-to serial converter, so the VID/PID is 1a86:7523, while rest of the components and functions remain unchanged.

## Protocol

The generator uses a plain text protocol for communication.

Each command (*set* or *read*) starts with ':' and has to be terminated with a newline, ASCII code 0x0a (but CRLF, i.e. 0x0d 0x0a, is also accepted).

*Set* commands are acknowledged with an 'ok' response, *read* commands echo the request followed by the parameter value.

## Resources
- [analogzoo.com: MHS-5200A Teardown and Review](http://www.analogzoo.com/2015/08/mhs-5200a-teardown-and-review/)
- [eevblog.com: MHS-5200A Serial Protocol Reverse Engineered](http://www.eevblog.com/forum/testgear/mhs-5200a-serial-protocol-reverse-engineered/)
- [Google docs: MHS5200A Protocol](https://docs.google.com/document/d/1HbLQ4u87RJkD3Ktyw7k9U7Zh5BPNzbrhMlszNGdXiiY/edit)

