---
title: AR488
---

# AR488

<div class="infobox" markdown>

![AR488](./img/Ar488-artag-pcb-top.png){ .infobox-image }

### AR488

| | |
|---|---|

</div>

# AR488 GPIB to UART/USB

The [AR488](https://github.com/Twilight-Logic/AR488) is an Arduino-based [ GPIB](https://sigrok.org/wiki/Protocol_decoder:Ieee488) to serial port adapter.  The firmware runs on Uno (and thus Nano), Mega as well as Leonardo boards.  The PC sees a USB or RS-232 attached COM port, transmit data is sent to the device, and the device's response is seen as receive data.  Out-of-band commands prefixed by *++* can control the adapter's behaviour.  The AR488 is accessible to interactive sessions in a terminal program, as well as can serve as a SCPI-over-serial "cable".

With **one device per adapter** (specific GPIB address and communication parameters stored in the **AR488** adapter) **support is transparent**. When the adapter is connected to multiple devices at the same time, then "out-of-band" communication is required (the above mentioned ++ commands), which sigrok does not provide.

## Hardware
- Arduino Uno or Nano (ATmega328P based), or Mega (ATmega2560 based), or Leonardo or Pro Micro (ATmega32U4 based)
- Centronics 24-pin connector

See the AR488-manual.pdf in the firmware source tree for schematics.  Wires run from the Arduino board to the Centronics connector, and driver chips are not involved.  This keeps the component count low, the wiring simple, and the mechanical construction compact (especially with Nano boards which can execute the Uno firmware).  In theory, any bare serially attached ATmega chip would do, but the firmware happens to be written in the Arduino IDE's language (it uses libraries and build support, and won't work outside of the IDE without modifications).

The primary goal of the project is to enable quick access to GPIB attached devices.  Typical use is to have one adapter per device (it's rather low cost, so that's not an issue).  The lack of proper drivers means that the adapter cannot handle a full bus. The limit is said to be somewhere around three or four devices, before signals go out of spec and communication need not work reliably any longer.  For larger setups with many devices, a proper full-blown adapter with appropriate driving capabilities is recommended.

## Photos

<div class="photo-grid" markdown>

[![Ar488 Artag Pcb Top](./img/Ar488-artag-pcb-top.png)](./img/Ar488-artag-pcb-top.png "Ar488 Artag Pcb Top"){ .glightbox data-gallery="ar488" }
<span class="caption">Ar488 Artag Pcb Top</span>

[![Ar488 Artag Pcb Conn](./img/Ar488-artag-pcb-conn.png)](./img/Ar488-artag-pcb-conn.png "Ar488 Artag Pcb Conn"){ .glightbox data-gallery="ar488" }
<span class="caption">Ar488 Artag Pcb Conn</span>

[![Ar488 Diy Sniff Top](./img/Ar488-diy-sniff-top.png)](./img/Ar488-diy-sniff-top.png "Ar488 Diy Sniff Top"){ .glightbox data-gallery="ar488" }
<span class="caption">Ar488 Diy Sniff Top</span>

[![Ar488 Diy Sniff Bot](./img/Ar488-diy-sniff-bot.png)](./img/Ar488-diy-sniff-bot.png "Ar488 Diy Sniff Bot"){ .glightbox data-gallery="ar488" }
<span class="caption">Ar488 Diy Sniff Bot</span>

</div>

