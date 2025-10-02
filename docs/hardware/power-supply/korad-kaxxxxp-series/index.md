---
title: Korad KAxxxxP series
---

# Korad KAxxxxP series

<div class="infobox" markdown>

![Korad KAxxxxP series](./img/Velleman_ps3005d_mugshot.png){ .infobox-image }

### Korad KAxxxxP series

| | |
|---|---|
| **Status** | supported |
| **Source code** | [korad-kaxxxxp](https://github.com/OpenTraceLab/OpenTraceCapture/tree/main/src/hardware/korad-kaxxxxp) |
| **Channels** | 1 |
| **Voltage/current (CH1)** | various |
| **Connectivity** | USB/serial, RS232 |
| **Features** | programmable presets, over voltage protection, over current protection, output on/off |
| **Website** | [koradtechnology.com](http://koradtechnology.com) |

</div>

The **Korad KAxxxxP** series are 1 channel switch-mode programmable power supplies with both USB/serial and RS232 connectivity.

The devices are also sold as rebranded versions by e.g. Velleman, Tenma/Farnell, Stamos, or RND.

## Devices
| Device | OEM/Rebranded | Voltage range | Current range | Power |
|---|---|---|---|---|
| [Korad KA3003P](http://www.koradtechnology.com/product/14.html) | [Tenma 72-2535](http://uk.farnell.com/tenma/72-2535/power-supply-1ch-30v-3a-prog/dp/2445411) | 0-30 V | 0-3 A | 90 W |
| [Korad KA3005P](https://sigrok.org/wiki/Korad_KA3005P) | [Velleman PS3005D](https://sigrok.org/wiki/Velleman_PS3005D), [Velleman LABPS3005D](https://sigrok.org/wiki/Velleman_LABPS3005D), [Tenma 72-2540](http://uk.farnell.com/tenma/72-2540/power-supply-1ch-30v-5a-prog/dp/2445412), [RND 320-KA3005P](https://www.distrelec.de/en/bench-top-power-supply-30-programmable-rnd-lab-rnd-320-ka3005p/p/30061864) | 0-30 V | 0-5 A | 150 W |
| [Korad KD3005P](http://www.koradtechnology.com/product/16.html) | — | 0-30 V | 0-5 A | 150 W |
| [Korad KA3010P](http://www.koradtechnology.com/product/14.html) | — | 0-30 V | 0-10 A | 300 W |
| [Korad KA6002P](http://www.koradtechnology.com/product/14.html) | [Tenma 72-2545](http://uk.farnell.com/tenma/72-2545/power-supply-1ch-60v-2a-prog/dp/2445413) | 0-60 V | 0-2 A | 120 W |
| [Korad KA6003P](http://www.koradtechnology.com/product/14.html) | [Tenma 72-2550](http://uk.farnell.com/tenma/72-2550/power-supply-1ch-60v-3a-prog/dp/2445414) | 0-60 V | 0-3 A | 180 W |
| [Korad KA6005P](http://www.koradtechnology.com/product/14.html) | — | 0-60 V | 0-5 A | 300 W |
| [Korad KD6005P](http://www.koradtechnology.com/product/16.html) | — | 0-60 V | 0-5 A | 300 W |
| [Stamos S-LS-31](http://www.stamos-welding.com/mains-adapter-s-ls-31) | — | 0-30 V | 0-5 A | 250 W |

**Note:** The libsigrok [korad-kaxxxxp](http://sigrok.org/gitweb/?p=libsigrok.git;a=tree;f=src/hardware/korad-kaxxxxp) driver needs to know about the device's ID (the response to the ***IDN?** command, see below). If you have a device which is not yet [listed in the driver](https://sigrok.org/gitweb/?p=libsigrok.git;a=blob;f=src/hardware/korad-kaxxxxp/api.c#l58), please let us know.

**Note:** Some versions of the Velleman PS3005D appear to use the [Atten PPS3000 series](https://sigrok.org/wiki/Atten_PPS3000_series) protocol instead of the Korad protocol described below.

## Protocol

The protocol is serial (actual RS232 and serial-over-USB is supported by the devices), 9600/8N1, (almost fully) ASCII based. No line termination, CRC or checksum characters are used. The PC sends a request string which the power supply then responds to.

During a PC connection, the front control buttons and the scrollwheel are blocked.

| Request | Example output | Remarks |
|---|---|---|
| *IDN? | KORADKA3005PV2.0 | Request identification from device. See also the [full list of recognized IDs in libsigrok](https://sigrok.org/gitweb/?p=libsigrok.git;a=blob;f=src/hardware/korad-kaxxxxp/api.c) in the models[] array. |
| STATUS? | (byte) | Request the actual status. The output is a single byte with the actual status encoded in bits. At least the Velleman PS3005D V2.0 is a bit buggy here. The only reliable bits are: 0x40 (Output mode: 1:on, 0:off), 0x20 (OVP and/or OCP mode: 1:on, 0:off) and 0x01 (CV/CC mode: 1:CV, 0:CC). |
| VSET1? | 12.34 | Request the voltage as set by the user. |
| VSET1:12.34 | (none) | Set the maximum output voltage. |
| VOUT1? | 12.34 | Request the actual voltage output. |
| ISET1? | 0.125 | Request the current as set by the user. See notes below for a firmware bug related to this command. |
| ISET1:0.125 | (none) | Set the maximum output current. |
| IOUT1? | 0.125 | Request the actual output current. |
| OUT1 | (none) | Enable the power output. |
| OUT0 | (none) | Disable the power output. |
| OVP1 | (none) | Enable the "Over Voltage Protection", the PS will switch off the output when the voltage rises above the actual level. |
| OVP0 | (none) | Disable the "Over Voltage Protection". |
| OCP1 | (none) | Enable the "Over Current Protection", the PS will switch off the output when the current rises above the actual level. |
| OCP0 | (none) | Disable the "Over Current Protection". |
| TRACK0 | (none) | Set multichannel mode, 0 independent, 1 series, 2 parallel (from Velleman protocol v1.3 documentation). |
| RCL1 | (none) | Recalls voltage and current limits from memory, 1 to 5 (from Velleman protocol v2.0 documentation). |
| SAV1 | (none) | Saves voltage and current limits to memory, 1 to 5 (from Velleman protocol v2.0 documentation). |

**Remarks**:

- The digit 1 in the V... and I... requests indicates the values are meant for channel one. In future (or "higher"?) models this may be two for a second channel and so on.
- Voltage ("00.00" to "31.00" V) and current ("0.000" to "5.100" A) output values have a fixed length with fixed dot position. The values won't become negative.
- ISET1? replies with a sixth byte on many models (all?) which is the sixth character from *IDN? reply if *IDN? was queried before (during same power cycle). This byte is read and discarded by sigrok. As reported by [Jordi Castells / kxtells](https://github.com/kxtells/tenma-serial/issues/2) this behaviour seems to happen only on protocol version 2.0, but not in 2.1.
## Resources
- [Korad digital control DC power supplies (KAxxxxD)](http://koradtechnology.com/en/cp2-1.html)
- [Korad programmable DC power supplies (KAxxxxP)](http://koradtechnology.com/en/cp3-1.html)
- [Korad digital control DC electronic loads](http://koradtechnology.com/en/cp4-1.html)
- [Korad programmable DC electronic loads](http://koradtechnology.com/en/cp5-1.html)
- [Korad encoder control DC power supplies (KDxxxxP)](http://koradtechnology.com/en/Products.html)

## Photos

<div class="photo-grid" markdown>

[![Velleman Ps3005d Mugshot](./img/Velleman_ps3005d_mugshot.png)](./img/Velleman_ps3005d_mugshot.png "Velleman Ps3005d Mugshot"){ .glightbox data-gallery="korad-kaxxxxp-series" }
<span class="caption">Velleman Ps3005d Mugshot</span>

</div>
