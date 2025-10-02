---
title: Rigol DG1000z Series
---

# Rigol DG1000z Series

<div class="infobox" markdown>

![Rigol DG1000z Series](./img/Dg1000z_series.jpg){ .infobox-image }

### Rigol DG1000z Series

| | |
|---|---|
| **Status** | supported |
| **Source code** | [rigol-dg](https://github.com/OpenTraceLab/OpenTraceCapture/tree/main/src/hardware/rigol-dg) |
| **Frequency (sine)** | 25-60MHz |
| **Frequency (square)** | 25MHz |
| **Frequency (other)** | 15-25MHz (pulse), 500-1000KHz (ramp) |
| **Frequency (user)** | 10-20MHz |
| **Waveforms** | sine, square, ramp, pulse, harmonic, noise, arbitrary waveform |
| **Waveform memory** | 2-8Mpts (16Mpts option) |
| **Modulation** | AM, FM, PM, DSB-AM, FSK, ASK, PWM |
| **Connectivity** | USBTMC, LAN |
| **Website** | [rigolna.com](https://www.rigolna.com/products/waveform-generators/dg1000z/) |

</div>

Rigol DG1000Z Series Arbitrary Waveform Generators are 2 channel, 25-60MHz signal generators with up to 16Mpts waveform memory. 

## Devices

Hardware on all these models is identical, only difference is in software/firmware. 

| Model | Channels | Max Frequency (Sine) | Max Frequency (Square) | Arbitrary Waveform Length | Frequency Counter |
|---|---|---|---|---|---|
| DG1022Z | 2 | 25 MHz | 25 MHz | 2 Mpts * | Y |
| DG1032Z | 2 | 30 MHz | 25 MHz | 8 Mpts * | Y |
| DG1062Z | 2 | 60 MHz | 25 MHz | 8 Mpts * | Y |

- ) 16 Mpts waveform memory is (software) option.
## Hardware

**Digital**:

TODO

**Analog**:

TODO

## Photos

<div class="photo-grid" markdown>

[![Dg1000z Series](./img/Dg1000z_series.jpg)](./img/Dg1000z_series.png "Dg1000z Series"){ .glightbox data-gallery="rigol-dg1000z-series" }
<span class="caption">Dg1000z Series</span>

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
- [DG1000Z Datasheet](http://beyondmeasure.rigoltech.com/acton/attachment/1579/f-033c/0/-/-/-/-/file.pdf)
- [DG1000Z Specifications](http://beyondmeasure.rigoltech.com/acton/attachment/1579/f-044f/0/-/-/-/-/file.pdf)
- [DG1000Z User's Guide](http://beyondmeasure.rigoltech.com/acton/attachment/1579/f-0450/0/-/-/-/-/file.pdf)
- [DG100Z Programming Guide](http://beyondmeasure.rigoltech.com/acton/attachment/1579/f-0493/1/-/-/-/-/DG1000Z%20Programming%20Guide.pdf)

