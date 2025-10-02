---
title: Agilent 34401A
---

# Agilent 34401A

<div class="infobox" markdown>

![Agilent 34401A](./img/Agilent_34401A_-_front.jpg){ .infobox-image }

### Agilent 34401A

| | |
|---|---|
| **Status** | supported |
| **Source code** | [scpi-dmm](https://github.com/OpenTraceLab/OpenTraceCapture/tree/main/src/hardware/scpi-dmm) |
| **IEC 61010-1** | CAT II (300V) |
| **Connectivity** | GPIB, RS232 |
| **Measurements** | voltage, current, 2- and 4-wire resistance, diode, continuity, frequency, period |
| **Features** | autorange, true RMS, data hold, relative |
| **Website** | [keysight.com](https://www.keysight.com/en/pd-1000001295%3Aepsg%3Apro-pn-34401A/digital-multimeter-6-digit) |

</div>

The **HP 34401A** / **Agilent 34401A** is a 6.5 digits CAT II (300V) bench multimeter.

## Photos

<div class="photo-grid" markdown>

[![Agilent 34401a Front](./img/Agilent_34401A_-_front.jpg)](./img/Agilent_34401A_-_front.png "Agilent 34401a Front"){ .glightbox data-gallery="agilent-34401a" }
<span class="caption">Agilent 34401a Front</span>

[![Agilent 34401a Back](./img/Agilent_34401A_-_back.jpg)](./img/Agilent_34401A_-_back.png "Agilent 34401a Back"){ .glightbox data-gallery="agilent-34401a" }
<span class="caption">Agilent 34401a Back</span>

</div>
## Example use

Depending on your type of connection you have to can either use the [ RS232 connection parameter](https://sigrok.org/wiki/Connection_parameters#RS232_.2F_Virtual_Com_Port) or the [ GPIB connection parameter](https://sigrok.org/wiki/Connection_parameters#Linux-GPIB). Examples:

```
 **--driver=scpi-dmm:conn=/dev/ttyUSB0**

```

or

```
 **--driver=scpi-dmm:conn=libgpib/hp34401a**

```

Check the capabilities of the meter's driver, and current state of settings:

```
 $ **sigrok-cli -d scpi-dmm:conn=/dev/ttyUSB0 --show**

```

Get or set the meter's current function:

```
 $ **sigrok-cli -d scpi-dmm:conn=/dev/ttyUSB0 --get measured_quantity**
 $ **sigrok-cli -d scpi-dmm:conn=/dev/ttyUSB0 -c measured_quantity=voltage/dc --set**

```

Acquire measurement data, in the current mode or in another specified mode:

```
 $ **sigrok-cli -d scpi-dmm:conn=/dev/ttyUSB0 --continuous**
 $ **sigrok-cli -d scpi-dmm:conn=/dev/ttyUSB0 --time 10s**
 $ **sigrok-cli -d scpi-dmm:conn=/dev/ttyUSB0 --samples 10 -c measured_quantity=current/dc**

```
## Resources
- [Datasheet](https://www.keysight.com/de/de/assets/7018-06774/data-sheets/5968-0162.pdf)
- [User's guide](https://www.keysight.com/us/en/assets/9018-01063/user-manuals/9018-01063.pdf)
- [User's guide errata](https://www.keysight.com/us/en/assets/9018-02040/user-manuals/9018-02040.pdf)
- [Service guide](https://www.keysight.com/us/en/assets/9018-05613/service-manuals/9018-05613.pdf)

