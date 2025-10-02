---
title: Galvant GPIBUSB
---

# Galvant GPIBUSB

<div class="infobox" markdown>

![Galvant GPIBUSB](./img/GalvantGPIBUSBrev4.JPG){ .infobox-image }

### Galvant GPIBUSB

| | |
|---|---|
| **Status** | not supported |
| **Sigrok driver** | [[1]](http://sigrok.org/gitweb/?p=libsigrok.git;a=tree;f=src/hardware/) |
| **Website** | [galvant.ca](http://www.galvant.ca/#!/store/) |
| **Hardware license** | [CC-BY-SA 3.0](http://creativecommons.org/licenses/by-sa/3.0/) |
| **Project files** | [on Github](https://github.com/Galvant/gpibusb-pcb) |
| **Project program** | [KiCad](http://kicad-pcb.org/) |
| **Layout** | in project files, gerbers |
| **Schematics** | in project files |
| **Firmware source** | [on Github](https://github.com/Galvant/gpibusb-firmware) |
| **Firmware license** | [GNU Affero license](http://www.gnu.org/licenses/agpl.txt) |

</div>

The Galvant GPIBUSB is a USB-based, firmware-implemented GPIB interface.

See [Galvant GPIBUSB/Info](https://sigrok.org/wiki/Galvant_GPIBUSB/Info) for more details (such as **lsusb -v** output) about the device.

## Hardware
- [Microchip PIC18F4250](http://ww1.microchip.com/downloads/en/devicedoc/39631a.pdf) microcontroller
- [FTDI FT230X](http://www.ftdichip.com/Support/Documents/DataSheets/ICs/DS_FT230X.pdf) USB-serial interface chip
- [SN75160B](http://www.ti.com/lit/ds/symlink/sn75160b.pdf) GPIB interface driver
- [SN75162B](http://www.ti.com/lit/ds/slls005b/slls005b.pdf) GPIB interface driver

## Photos

<div class="photo-grid" markdown>

[![Galvantgpibusbrev4](./img/GalvantGPIBUSBrev4.JPG)](./img/GalvantGPIBUSBrev4.JPG "Galvantgpibusbrev4"){ .glightbox data-gallery="galvant-gpibusb" }
<span class="caption">Galvantgpibusbrev4</span>

</div>
## Protocol

It's a custom protocol over a virtual serial port (FTDI FT230X), described in the [manual](https://github.com/Galvant/gpibusb-documentation). An earlier protocol has been supplemented in recent firmware with one that appears to be compatible with the [Prologix GPIB-USB](https://sigrok.org/wiki/Prologix_GPIB-USB)

## Resources
- [Vendor description](http://galvant.ca/shop/gpibusb/)
- [Vendor user documentation sources](https://github.com/Galvant/gpibusb-documentation)
- [hardware resources](https://github.com/Galvant/gpibusb-pcb) OSHW (KiCad) design on github
- [firmware resources](https://github.com/Galvant/gpibusb-firmware) (sources on github, GNU Affero license )

