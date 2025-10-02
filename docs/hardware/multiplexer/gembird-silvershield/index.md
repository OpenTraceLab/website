---
title: Gembird silvershield
---

# Gembird silvershield

<div class="infobox" markdown>

![Gembird silvershield](./img/Gembird-silvershield-controller-top.jpg){ .infobox-image }

### Gembird silvershield

| | |
|---|---|
| **Status** | planned |
| **Channels** | up to 4 |
| **Ratings** | 230V 10A |
| **Connectivity** | USB HID |

</div>

The **Gembird Silvershield PM** (also referred to as **SIS-PM**) is a USB controlled power outlet with surge protection, up to 4 of the outlets are USB controlled. The firmware presents itself as USB HID to the PC (so that no driver installation is required on Windows).

See [ Info](https://sigrok.org/wiki/Gembird_silvershield/Info) for USB details.

## Photos

<div class="photo-grid" markdown>

[![Gembird Silvershield Controller Top](./img/Gembird-silvershield-controller-top.jpg)](./img/Gembird-silvershield-controller-top.png "Gembird Silvershield Controller Top"){ .glightbox data-gallery="gembird-silvershield" }
<span class="caption">Gembird Silvershield Controller Top</span>

[![Gembird Silvershield Inside](./img/Gembird-silvershield-inside.jpg)](./img/Gembird-silvershield-inside.png "Gembird Silvershield Inside"){ .glightbox data-gallery="gembird-silvershield" }
<span class="caption">Gembird Silvershield Inside</span>

[![Gembird Silvershield Inside Zoom](./img/Gembird-silvershield-inside-zoom.jpg)](./img/Gembird-silvershield-inside-zoom.png "Gembird Silvershield Inside Zoom"){ .glightbox data-gallery="gembird-silvershield" }
<span class="caption">Gembird Silvershield Inside Zoom</span>

[![Gembird Silvershield Front](./img/Gembird-silvershield-front.jpg)](./img/Gembird-silvershield-front.png "Gembird Silvershield Front"){ .glightbox data-gallery="gembird-silvershield" }
<span class="caption">Gembird Silvershield Front</span>

[![Gembird Silvershield Controller Bottom](./img/Gembird-silvershield-controller-bottom.jpg)](./img/Gembird-silvershield-controller-bottom.png "Gembird Silvershield Controller Bottom"){ .glightbox data-gallery="gembird-silvershield" }
<span class="caption">Gembird Silvershield Controller Bottom</span>

[![Gembird Silvershield Label](./img/Gembird-silvershield-label.jpg)](./img/Gembird-silvershield-label.png "Gembird Silvershield Label"){ .glightbox data-gallery="gembird-silvershield" }
<span class="caption">Gembird Silvershield Label</span>

</div>
## Hardware
- Cypress CY7C63723 controller, USB1 low speed
- 6MHz crystal
- 24c02 EEPROM (device supports schedules)
- 7805 regulator, diodes for alternative USB or barrel jack supply
- discrete relay controlling transistors, flyback diodes, opto couplers (4N35) per relay, indicators
## Resources
- [SIS-PM Control for Linux](http://sispmctl.sf.net)
- [sispy](https://github.com/EricSeynaeve/sispy) and especially [SIS-PM_API.txt](https://github.com/EricSeynaeve/sispy/blob/master/SIS-PM_API.txt) the HID report notes

