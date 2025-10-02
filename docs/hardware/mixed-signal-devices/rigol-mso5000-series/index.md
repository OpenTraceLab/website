---
title: Rigol MSO5000 Series
---

# Rigol MSO5000 Series

<div class="infobox" markdown>

![Rigol MSO5000 Series](./img/Sigrok_logo_no_text_transparent_512.png){ .infobox-image }

### Rigol MSO5000 Series

| | |
|---|---|
| **Status** | in progress |
| **Source code** | [rigol-ds](https://github.com/OpenTraceLab/OpenTraceCapture/tree/main/src/hardware/rigol-ds) |
| **Samplerate** | up to 8GSa/s |
| **Analog bandwidth** | 70-350MHz (depending on model) |
| **Vertical resolution** | 8bits |
| **Triggers** | edge, pulse, runt, window, nth edge, slope, video, pattern, delay, timeout, duration, setup/hold, protocol (optional: RS232/UART, I²C, SPI, CAN, FlexRay, LIN, I2S, MIL-STD-1553) |
| **Input impedance** | 1MΩ‖17pF 300V RMS CAT I |
| **Memory** | 100Mpts (mode/ch-dependent), Option 200Mpts |
| **Display** | 9" 1024x800 |
| **Connectivity** | USB host/device, ethernet (LXI), HDMI, trigger out, pass/fail out |
| **Features** | math: +, —, x, /, FFT, A&amp;&amp;B, A |
| **Website** | [rigolna.com](https://www.rigolna.com/products/digital-oscilloscopes/MSO5000/) |

</div>

The [Rigol MSO5000 Series](https://www.rigolna.com/products/digital-oscilloscopes/MSO5000/) are 2-/4-channel oscilloscopes with an analog bandwidth of 70-350MHz and up to 8GS/s sampling rate.

## Devices
| Model | Analog channels | Bandwidth | Digital channels |
|---|---|---|---|
| MSO5072 | 2 | 70MHz | 16 |
| MSO5074 | 4 | 70MHz | 16 |
| MSO5102 | 2 | 100MHz | 16 |
| MSO5104 | 4 | 100MHz | 16 |
| MSO5204 | 4 | 200MHz | 16 |
| MSO5354 | 4 | 350MHz | 16 |

## Protocol

The device uses [USBTMC](https://sigrok.org/wiki/USBTMC) or LXI via its Ethernet port for communication with a host PC. The protocol is based on [SCPI](https://sigrok.org/wiki/IEEE-488) commands.

## Resources

[User Manual](https://beyondmeasure.rigoltech.com/acton/attachment/1579/f-0905/0/-/-/-/-/MSO5_users_guide.pdf)

[Programming Guide](https://beyondmeasure.rigoltech.com/acton/attachment/1579/f-0906/0/-/-/-/-/MSO5_programming_guide.pdf)

## Example use

Depending on your type of connection you have to can either use the [ USBTMC connection parameter](https://sigrok.org/wiki/Connection_parameters#USBTMC) or the [ VXI connection parameter](https://sigrok.org/wiki/Connection_parameters#VXI). Examples:

When connecting over TCP/IP need to specify ip address and port:

```
 **-d rigol-ds:conn=vxi/192.168.42.42**

```
```
 **sigrok-cli -d rigol-ds:conn=vxi/192.168.1.250 --config data_source=Live -o live.sr -O srzip --frames=1**

```

See [Rigol-ds data source](https://sigrok.org/wiki/Rigol-ds_data_source) for more information on data source.

## Digital channels

The MSO500 Series has dedicated memory for digital channels, which is smaller in size than the analog memory.
To have the same capturing time, the digital sampling rate is lower than the analog sampling rate.

Note: The support is not in mainline, yet. See [| PR#95](https://github.com/sigrokproject/libsigrok/pull/95)

## Signal generator (option)

The optional signal gnerator can be used with the rigol-dg driver.
For usage see [ Rigol DG800 Series](https://sigrok.org/wiki/Rigol_DG800_Series)

Suported waveforms

| Waveform | min frequency | max. frequency |
|---|---|---|
| Sine | 100mHz | 25MHz |
| Square | 100mHz | 15MHz |
| Ramp | 100mHz | 100kHz |
| Pulse | 100mHz | 1MHz |
| Arb | 100mHz | 10MHz |
| Noise | - | - |
| DC | - | - |
| Sinc | 100mHz | 1MHz |
| ExpRise | 100mHz | 1MHz |
| ExpFall | 100mHz | 1MHz |
| ECG | 100mHz | 1MHz |
| Gauss | 100mHz | 1MHz |
| Lorentz | 100mHz | 1MHz |
| Haversin | 100mHz | 1MHz |

Signal generator [PR#96](https://github.com/sigrokproject/libsigrok/pull/96)  [has been merged 2024-09-28](https://sigrok.org/gitaction/libsigrok.git/8da5cfc..70cdf23)

## Photos

<div class="photo-grid" markdown>

[![Sigrok Logo No Text Transparent 512](./img/Sigrok_logo_no_text_transparent_512.png)](./img/Sigrok_logo_no_text_transparent_512.png "Sigrok Logo No Text Transparent 512"){ .glightbox data-gallery="rigol-mso5000-series" }
<span class="caption">Sigrok Logo No Text Transparent 512</span>

</div>
