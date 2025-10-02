---
title: Rigol DM3068
---

# Rigol DM3068

<div class="infobox" markdown>

![Rigol DM3068](./img/Rigol_DM3068_back.jpg){ .infobox-image }

### Rigol DM3068

| | |
|---|---|
| **Status** | planned |
| **Counts** | 2200000 |
| **IEC 61010-1** | CAT I (1000V) / CAT II (300V) |
| **Connectivity** | LXI-C (Ethernet), USB, RS232, and GPIB |
| **Measurements** | TODO |
| **Features** | TODO |
| **Website** | [rigolna.com](http://www.rigolna.com/products/digital-multimeters/dm3000/dm3068/) |

</div>

The **Rigol DM3068** is a 2200000 counts, CAT I (1000V) / CAT II (300V) bench digital multimeter with LXI-C (Ethernet), USB, RS232, and GPIB connectivity.

See [Rigol DM3068/Info](https://sigrok.org/wiki/Rigol_DM3068/Info) for more details (such as **lsusb -vvv** output) about the device.

## Hardware

TODO.

## Photos

<div class="photo-grid" markdown>

[![Rigol Dm3068 Back](./img/Rigol_DM3068_back.jpg)](./img/Rigol_DM3068_back.jpg "Rigol Dm3068 Back"){ .glightbox data-gallery="rigol-dm3068" }
<span class="caption">Rigol Dm3068 Back</span>

[![Rigol Dm3068 Front](./img/Rigol_DM3068_front.jpg)](./img/Rigol_DM3068_front.png "Rigol Dm3068 Front"){ .glightbox data-gallery="rigol-dm3068" }
<span class="caption">Rigol Dm3068 Front</span>

[![Rigol Dm3068 Front](./img/Rigol_DM3068_front.jpg)](./img/Rigol_DM3068_front.jpg "Rigol Dm3068 Front"){ .glightbox data-gallery="rigol-dm3068" }
<span class="caption">Rigol Dm3068 Front</span>

</div>
## Protocol

TODO.

The user manual claims:

```
 Support the command sets of RIGOL DM3068, Agilent 34401A (including some extensions) and Fluke 45.

```

Which suggests that the DM3068 might already work with either the fluke-45 driver, or the scpi-dmm driver (after adding the Rigol device's *IDN? response to the set of supported models perhaps). Another option is to add native DM3068 support to the scpi-dmm driver.

## Resources
- [DM3068 Datasheet](http://beyondmeasure.rigoltech.com/acton/attachment/1579/f-0020/0/-/-/-/-/file.pdf)

