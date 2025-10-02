---
title: EDF Teleinfo
---

# EDF Teleinfo

<div class="infobox" markdown>

![EDF Teleinfo](./img/Actaris_a14c5_teleinfo.png){ .infobox-image }

### EDF Teleinfo

| | |
|---|---|
| **Status** | supported |
| **Source code** | [teleinfo](https://github.com/OpenTraceLab/OpenTraceCapture/tree/main/src/hardware/teleinfo) |
| **Connectivity** | RS232 |
| **Measurements** | energy, apparent power, current |

</div>

The **EDF Teleinfo** is a standard describing the client information RS232 output that all main house energy meter must follow in France.

A few manufacturers are selling compliant energy meters, such as Sagem, Landis+Gyr or Actaris.

Those energy meters can read current, apparent power and total consumed energy.

## Photos

<div class="photo-grid" markdown>

[![Actaris A14c5 Teleinfo](./img/Actaris_a14c5_teleinfo.png)](./img/Actaris_a14c5_teleinfo.png "Actaris A14c5 Teleinfo"){ .glightbox data-gallery="edf-teleinfo" }
<span class="caption">Actaris A14c5 Teleinfo</span>

</div>
## Protocol

The device is continuously sending informations on a modulated serial port running at 1200 bauds 7e1.
The signal is ASK modulated on a 50 kHz carrier.

The protocol is detailed in [this document](http://www.planete-domotique.com/notices/ERDF-NOI-CPT_O2E.pdf).

## Resources
- [Demodulateur teleinformation EDF](http://vesta.homelinux.free.fr/site/wiki/demodulateur_teleinformation_edf.html)
- [La téléinformation EDF (Planète Domotique)](http://www.planete-domotique.com/blog/2010/03/30/la-teleinformation-edf/)

