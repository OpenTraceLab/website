---
title: Agilent 34405A
---

# Agilent 34405A

<div class="infobox" markdown>

![Agilent 34405A](./img/Agilent_34405A.png){ .infobox-image }

### Agilent 34405A

| | |
|---|---|
| **Status** | supported |
| **Source code** | [scpi-dmm](https://github.com/OpenTraceLab/OpenTraceCapture/tree/main/src/hardware/scpi-dmm) |
| **Counts** | 120000 |
| **IEC 61010-1** | CAT II (300V) / CAT I (1000VDC) |
| **Connectivity** | USB (USBTMC) |
| **Measurements** | voltage, current, resistance, capacitance, frequency, temperature, diode, continuity |
| **Features** | autorange, true RMS, data hold, relative |
| **Website** | [keysight.com](http://www.keysight.com/en/pd-686884-pn-34405A/digital-multimeter-5-digit) |

</div>

The **Agilent 34405A** is a 120000 count CAT II (300V) / CAT I (1000VDC) bench multimeter with USB ([USBTMC](https://sigrok.org/wiki/USBTMC)) connectivity.

See [Agilent 34405A/Info](https://sigrok.org/wiki/Agilent_34405A/Info) for USB profile information.

## Photos

<div class="photo-grid" markdown>

[![Agilent 34405a](./img/Agilent_34405A.png)](./img/Agilent_34405A.png "Agilent 34405a"){ .glightbox data-gallery="agilent-34405a" }
<span class="caption">Agilent 34405a</span>

[![Agilent 34405a Back](./img/Agilent_34405A_back.png)](./img/Agilent_34405A_back.png "Agilent 34405a Back"){ .glightbox data-gallery="agilent-34405a" }
<span class="caption">Agilent 34405a Back</span>

</div>
## Example use

Scan for connected devices:

```
 $ **sigrok-cli -d scpi-dmm --scan**

```

If other supported models or multiple devices of the same type are connected:

```
 $ **lsusb**
 $ **sigrok-cli -d scpi-dmm:conn=0957.0618 --scan**
 $ **sigrok-cli -d scpi-dmm:conn=3.15 --scan**

```

Check the capabilities of the meter's driver, and current state of settings:

```
 $ **sigrok-cli -d scpi-dmm --show**

```

Get or set the meter's current function:

```
 $ **sigrok-cli -d scpi-dmm --get measured_quantity**
 $ **sigrok-cli -d scpi-dmm -c measured_quantity=voltage/dc --set**

```

Get and set the range:

```
 $ **sigrok-cli -d scpi-dmm --get range**
 $ **sigrok-cli -d scpi-dmm -c range=auto --set**
 $ **sigrok-cli -d scpi-dmm -c range=5e+3 --set**
 $ **sigrok-cli -d scpi-dmm -c range=10e-6 --set**

```

Acquire measurement data, in the current mode or in another specified mode:

```
 $ **sigrok-cli -d scpi-dmm --continuous**
 $ **sigrok-cli -d scpi-dmm --time 10s**
 $ **sigrok-cli -d scpi-dmm --samples 10 -c measured_quantity=current/dc**

```
## Resources
- [Datasheet](http://literature.cdn.keysight.com/litweb/pdf/5989-4906EN.pdf)
- [User’s and Service Guide](http://cp.literature.agilent.com/litweb/pdf/34405-91000.pdf)

