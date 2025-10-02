---
title: Rigol DG800 Series
---

# Rigol DG800 Series

<div class="infobox" markdown>

![Rigol DG800 Series](./img/Rigol_DG811_frontpanel.png){ .infobox-image }

### Rigol DG800 Series

| | |
|---|---|
| **Status** | supported |
| **Source code** | [rigol-dg](https://github.com/OpenTraceLab/OpenTraceCapture/tree/main/src/hardware/rigol-dg) |
| **Frequency (sine)** | 10-35MHz |
| **Frequency (square)** | 5-10MHz |
| **Frequency (other)** | 5-10MHz (pulse), 200-1000KHz (ramp) |
| **Frequency (user)** | 5-10MHz |
| **Waveforms** | sine, square, ramp, pulse, harmonic, noise, arbitrary waveform |
| **Waveform memory** | 2 Mpts (8 Mpts option) |
| **Modulation** | AM, FM, PM, DSB-AM, FSK, ASK, PWM |
| **Connectivity** | USBTMC |
| **Website** | [rigolna.com](https://www.rigolna.com/products/waveform-generators/dg800/) |

</div>

Rigol DG800 Series Arbitrary Waveform Generators are 1-2 channel, 10-36MHz high-resolution (16bit) signal generators with up to 8 Mpts waveform memory. 
Thanks to fan-less design, these units are completely silent.

These units appear to me using same hardware (just different color chassis) and firmware 
as [ Rigol DG900 Series](https://sigrok.org/wiki/Rigol_DG900_Series) signal generators.

Notable limitation when compared to Rigol DG1000z series is that Frequency Counter cannot be used simultaneously with second channel (CH2) is active.
This only affects the 2 channel units (DG812, DG822, DG832).

## Devices

Hardware on all these models is identical, only difference is in software/firmware. 

| Model | Channels | Max Frequency (Sine) | Max Frequency (Square) | Arbitrary Waveform Length | Frequency Counter |
|---|---|---|---|---|---|
| DG811 | 1 | 10 MHz | 5 MHz | 2 Mpts | Y |
| DG812 | 2 | 10 MHz | 5 MHz | 2 Mpts | Y |
| DG821 | 1 | 25 MHz | 10 MHz | 2 Mpts | Y |
| DG822 | 2 | 25 MHz | 10 MHz | 2 Mpts | Y |
| DG831 | 1 | 35 MHz | 10 MHz | 2 Mpts | Y |
| DG832 | 2 | 35 MHz | 10 MHz | 2 Mpts | Y |

- ) Waveform memory can be upgraded to 8 Mbpts via software license.
## Hardware

**Digital**:

TODO

**Analog**:

TODO

## Photos

<div class="photo-grid" markdown>

[![Rigol Dg811 Frontpanel](./img/Rigol_DG811_frontpanel.png)](./img/Rigol_DG811_frontpanel.png "Rigol Dg811 Frontpanel"){ .glightbox data-gallery="rigol-dg800-series" }
<span class="caption">Rigol Dg811 Frontpanel</span>

</div>
## Protocol

TODO

## Example use

Depending on your type of connection you have to can either use the [ USBTMC connection parameter](https://sigrok.org/wiki/Connection_parameters#USBTMC) or the [ TCP/IP connection parameter](https://sigrok.org/wiki/Connection_parameters#TCP_RAW). Examples:

```
 **-d rigol-dg**

```

(usually no parameters are needed when connecting via USB)

When connecting over TCP/IP need to specify ip address and port:

```
 **-d rigol-dg:conn=tcp-raw/192.168.42.42/5555**

```

Check the capabilities of the meter's driver, and current state of settings:

```
 $ **sigrok-cli -d rigol-dg --show**

```

Check the capabilities specific to a channel (1 or 2):

```
 $ **sigrok-cli -d rigol-dg -g 1 --show**

```

Enable or disable channel output (first channel):

```
 $ **sigrok-cli -d rigol-dg -g 1 --set --config enabled=true**
 $ **sigrok-cli -d rigol-dg -g 1 --set --config enabled=false**

```

Get or set the waveform function (second channel):

```
 $ **sigrok-cli -d rigol-dg -g 2 --get pattern**
 $ **sigrok-cli -d rigol-dg -g 2 --set --config pattern=square**

```

Get or set the output signal frequency:

```
 $ **sigrok-cli -d rigol-dg -g 1 --get output_frequency**
 $ **sigrok-cli -d rigol-dg -g 1 --set --config output_frequency=20000**

```

Get or set the output signal amplitude:

```
 $ **sigrok-cli -d rigol-dg -g 1 --get amplitude**
 $ **sigrok-cli -d rigol-dg -g 1 --set --config amplitude=3.3**

```

Get or set the output signal offset:

```
 $ **sigrok-cli -d rigol-dg -g 1 --get offset**
 $ **sigrok-cli -d rigol-dg -g 1 --set --config offset=1.0**

```

Get or set the output signal phase:

```
 $ **sigrok-cli -d rigol-dg -g 1 --get phase**
 $ **sigrok-cli -d rigol-dg -g 1 --set --config phase=90.0**

```

Get or set the output signal duty cycle:

```
 $ **sigrok-cli -d rigol-dg -g 1 --get output_duty_cycle**
 $ **sigrok-cli -d rigol-dg -g 1 --set --config output_duty_cycle=25.0**

```

Acquire measurement data (frequency counter output):

```
 $ **sigrok-cli -d rigol-dg --continuous**
 $ **sigrok-cli -d rigol-dg --time 10s**
 $ **sigrok-cli -d rigol-dg --samples 10**

```
## Resources
- [DG800 Datasheet](https://beyondmeasure.rigoltech.com/acton/attachment/1579/f-08a0/1/-/-/-/-/DG800%20Datasheet.pdf)
- [DG800 User's Guide](https://beyondmeasure.rigoltech.com/acton/attachment/1579/f-08a5/0/-/-/-/-/DG800_UserGuide_EN.pdf)
- [DG800 Programming Guide](https://beyondmeasure.rigoltech.com/acton/attachment/1579/f-08a6/0/-/-/-/-/DG800_ProgrammingGuide_EN.pdf)

