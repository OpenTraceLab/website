---
title: BayLibre ACME
---

# BayLibre ACME

<div class="infobox" markdown>

![BayLibre ACME](./img/Acme-probe-temp.png){ .infobox-image }

### BayLibre ACME

| | |
|---|---|
| **Status** | supported |
| **Source code** | [baylibre-acme](https://github.com/OpenTraceLab/OpenTraceCapture/tree/main/src/hardware/baylibre-acme) |
| **Connectivity** | BeagleBone Black expansion connector, I²C |
| **Measurements** | energy, power, current, temperature |
| **Website** | [baylibre.com](http://baylibre.com/acme/) |

</div>

The **BayLibre ACME** is an extension (cape) for the **BeagleBone Black**, designed to provide multi-channel power and temperature measurements capabilities.

It comes with power and temperature probes, turning it into an advanced all-in-one power/temperature measurement solution.

## Hardware
- [BeagleBone Black](http://beagleboard.org/BLACK)
- ACME cape:
**I²C current/power monitor**: [Texas Instruments INA226](http://www.ti.com/product/ina226) ([datasheet](http://www.ti.com/lit/gpn/ina226))
- **I²C/SMBus ±1°C temperature sensor**: [Texas Instruments TMP435](http://www.ti.com/product/tmp435) ([datasheet](http://www.ti.com/lit/gpn/tmp435))

## Photos

<div class="photo-grid" markdown>

[![Acme Probe Temp](./img/Acme-probe-temp.png)](./img/Acme-probe-temp.png "Acme Probe Temp"){ .glightbox data-gallery="baylibre-acme" }
<span class="caption">Acme Probe Temp</span>

[![Acme](./img/Acme.png)](./img/Acme.png "Acme"){ .glightbox data-gallery="baylibre-acme" }
<span class="caption">Acme</span>

[![Acme Poster](./img/Acme-poster.png)](./img/Acme-poster.png "Acme Poster"){ .glightbox data-gallery="baylibre-acme" }
<span class="caption">Acme Poster</span>

[![Acme Probe He10](./img/Acme-probe-he10.png)](./img/Acme-probe-he10.png "Acme Probe He10"){ .glightbox data-gallery="baylibre-acme" }
<span class="caption">Acme Probe He10</span>

[![Acme Probe Usb](./img/Acme-probe-usb.png)](./img/Acme-probe-usb.png "Acme Probe Usb"){ .glightbox data-gallery="baylibre-acme" }
<span class="caption">Acme Probe Usb</span>

[![Acme Cape](./img/Acme-cape.png)](./img/Acme-cape.png "Acme Cape"){ .glightbox data-gallery="baylibre-acme" }
<span class="caption">Acme Cape</span>

[![Acme Probe Jack](./img/Acme-probe-jack.png)](./img/Acme-probe-jack.png "Acme Probe Jack"){ .glightbox data-gallery="baylibre-acme" }
<span class="caption">Acme Probe Jack</span>

</div>
## Protocol

ACME probes are connected to I²C bus #1 of the BeagleBone Black via the ACME cape.

The components used to do actual measurements (INA226 & TMP435) are supported in mainline Linux. The drivers expose a standard interface via the Linux sysfs pseudo file system.

The ACME driver for [libsigrok](https://sigrok.org/wiki/Libsigrok) uses said interface to acquire measurement samples and control the cape (change shunt resistance configuration, power-off measured devices etc.).

## Resources
- [Vendor website](http://baylibre.com/acme/)
- [Vendor wiki](http://wiki.baylibre.com/doku.php?id=acme:start)

