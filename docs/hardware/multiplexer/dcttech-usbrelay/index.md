---
title: dcttech usbrelay
---

# dcttech usbrelay

<div class="infobox" markdown>

![dcttech usbrelay](./img/Dcttech-usbrelay2-top.jpg){ .infobox-image }

### dcttech usbrelay

| | |
|---|---|
| **Status** | supported |
| **Source code** | [dcttech-usbrelay](https://github.com/OpenTraceLab/OpenTraceCapture/tree/main/src/hardware/dcttech-usbrelay) |
| **Channels** | up to 8 |
| **Ratings** | 10A 250VAC / 10A 30VDC |
| **Connectivity** | USB HID |

</div>

The **dcttech.com USBRelay<n>** is a USB relay card with up to 8 relays
(models with 1, 2, 4, or 8 relays exist). The firmware is based on V-USB
and presents itself as USB HID to the PC (so that no driver installation
is required on Windows).

See [ Info](https://sigrok.org/wiki/Dcttech_usbrelay/Info) for USB details.

## Photos

<div class="photo-grid" markdown>

[![Dcttech Usbrelay2 Top](./img/Dcttech-usbrelay2-top.jpg)](./img/Dcttech-usbrelay2-top.png "Dcttech Usbrelay2 Top"){ .glightbox data-gallery="dcttech-usbrelay" }
<span class="caption">Dcttech Usbrelay2 Top</span>

[![Dcttech Usbrelay Mugshot](./img/Dcttech_usbrelay_mugshot.jpg)](./img/Dcttech_usbrelay_mugshot.png "Dcttech Usbrelay Mugshot"){ .glightbox data-gallery="dcttech-usbrelay" }
<span class="caption">Dcttech Usbrelay Mugshot</span>

[![Dcttech Usbrelay4 Bot](./img/Dcttech-usbrelay4-bot.jpg)](./img/Dcttech-usbrelay4-bot.png "Dcttech Usbrelay4 Bot"){ .glightbox data-gallery="dcttech-usbrelay" }
<span class="caption">Dcttech Usbrelay4 Bot</span>

[![Dcttech Usbrelay Diy](./img/Dcttech-usbrelay-diy.jpg)](./img/Dcttech-usbrelay-diy.png "Dcttech Usbrelay Diy"){ .glightbox data-gallery="dcttech-usbrelay" }
<span class="caption">Dcttech Usbrelay Diy</span>

[![Dcttech Usbrelay4 Top](./img/Dcttech-usbrelay4-top.jpg)](./img/Dcttech-usbrelay4-top.png "Dcttech Usbrelay4 Top"){ .glightbox data-gallery="dcttech-usbrelay" }
<span class="caption">Dcttech Usbrelay4 Top</span>

[![Dcttech Usbrelay2 Bot](./img/Dcttech-usbrelay2-bot.jpg)](./img/Dcttech-usbrelay2-bot.png "Dcttech Usbrelay2 Bot"){ .glightbox data-gallery="dcttech-usbrelay" }
<span class="caption">Dcttech Usbrelay2 Bot</span>

</div>
## Example use

Detect the device and display its properties.

```
 $ **sigrok-cli -d dcttech-usbrelay --scan**
 The following devices were found:
 dcttech-usbrelay:conn=/dev/hidraw2 - www.dcttech.com USBRelay4 [S/N: 12345]

``````
 $ **sigrok-cli -d dcttech-usbrelay --show**
 Driver functions:
     Multiplexer
 Scan options:
     conn
 dcttech-usbrelay:conn=/dev/hidraw2 - www.dcttech.com USBRelay4 [S/N: 12345]
 Channel groups:
     R1: channel
     R2: channel
     R3: channel
     R4: channel
 Supported configuration options across all channel groups:
     conn: /dev/hidraw2 (current)
     enabled: on, off

```

Display the relay state.

```
 $ **sigrok-cli -d dcttech-usbrelay --get channel_group=R1:enabled --get channel_group=R2:enabled --get channel_group=R3:enabled --get channel_group=R4:enabled**
 true
 false
 false
 true

```

Manipulate the state of relays.

```
 $ **sigrok-cli -d dcttech-usbrelay --config channel_group=R1:enabled=off --config channel_group=R2:enabled=on --set**

```

## Resources
- [V-USB project page](https://www.obdev.at/products/vusb), software bitbanging USB for AVR controllers that don't have native USB hardware support
- [product description](http://vusb.wikidot.com/project:driver-less-usb-relays-hid-interface) and [source code repo](https://github.com/pavel-a/usb-relay-hid) of a private project that is not related to the vendor, implements OpenSource   libraries and CLI and GUI applications to control these cards

