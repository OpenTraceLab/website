---
title: ZKETECH EBD-USB
---

# ZKETECH EBD-USB

<div class="infobox" markdown>

![ZKETECH EBD-USB](./img/Ztetech-ebd-usb_2B.png){ .infobox-image }

### ZKETECH EBD-USB

| | |
|---|---|
| **Status** | supported |
| **Source code** | [zketech-ebd-usb](https://github.com/OpenTraceLab/OpenTraceCapture/tree/main/src/hardware/zketech-ebd-usb) |
| **Channels** | 1 |
| **Voltage/current (CH1)** | 35W / 0-4A / 0-21V |
| **Connectivity** | USB/serial |
| **Features** | DC constant current load |
| **Website** | [zketech.com](http://www.zketech.com) |

</div>

The **ZKETECH EBD-USB+** is a programmable DC electronic load (0~4A, 0~21V) with serial connectivity over USB.

The electronic load can only be used together with a computer, because it has no external controls.

Currently only the "plus" version is supported. Contact us for support if you own a "non-plus" version (25W / 13.5V).

See [ZKETECH EBD-USB/Info](https://sigrok.org/wiki/ZKETECH_EBD-USB/Info) for more details (such as **lsusb -v** output) about the device.

## Hardware
- **Power MOSFET**: [Infineon IRLZ44N](https://www.infineon.com/cms/de/product/power/mosfet/20v-300v-n-channel-power-mosfet/40v-75v-n-channel-power-mosfet/irlz44n/) ([datasheet](https://www.infineon.com/dgdl/irlz44npbf.pdf?fileId=5546d462533600a40153567217c32725))
## Protocol

Messages are exchanged between host and devices:

- they start with 0xfa
- they end with 0xf8
- these two bytes values can't be used in the rest of the message (the maximum value is 240)
- the second byte encodes the message type
- all two-byte values are in base 240 (e.g. 01 0a = 250)
- the second last byte is a XOR checksum of the message (excluding first and last byte).

The communication is prone to byte loss on both directions.
Always verify the message length, checksum, and don't send the bytes too fast.
Resend messages until the one expected next is received.
Sometimes it doesn't send any messages anymore and doesn't react to sent messages.
Then the only way to reset the device is to re-plug it.

Messages:

- `fa 05 00 00 00 00 00 00 05 f8`
direction: host to device
- description: start measurements
- `fa 06 00 00 00 00 00 00 06 f8`
direction: host to device
- description: stop measurements
- `fa 01 00 64 00 0a 00 00 6f f8`
direction: host to device
- description: start load
- content:
`00 64`: current limit in 0.001 A
- `00 0a`: cutoff voltage in 0.01 V
- `00 00`: time limit in minutes
- note: the time limit is not enforced on the device. the device will report the minutes passed, and the host needs to stop the load
- `fa 02 00 00 00 00 00 00 02 f8`
direction: host to device
- description: toggle load on/off
- `fa 07 00 64 00 0a 00 00 69 f8`
direction: host to device
- description: update load
- content:
`00 64`: current limit in 0.001 A
- `00 0a`: cutoff voltage in 0.01 V
- `00 00`: time limit in minutes
- note: the time limit is not enforced on the device. the device will report the minutes passed, and the host needs to stop the load
- `fa 04 00 14 c8 00 00 00 d8 f8`
direction: host to device
- description: calibrate
- content:
`00`: 0x00 = low voltage, 0x01 = high voltage, 0x02 = low current, 0x03 = high current
- `14 c8`: voltage in 0.001 V or current in 0.0001 A
- `fa 00 00 00 14 c5 07 a9 07 ad 00 64 00 0a 00 00 1a a1 f8`
direction: device to host
- description: measurement, without load
- content:
`00 00`: current in 0.0001 A
- `14 c5`: voltage in 0.001 V
- `07 a9`: voltage of D+ 0.001 V
- `07 ad`: voltage of D- 0.001 V
- `00 64`: current limit in 0.001 A
- `00 0a`: cutoff voltage in 0.01 V
- `00 00`: time limit in minutes
- `1a`: device (0x1a = EBD-USB+)
- `fa 0a 00 00 14 c5 07 a9 07 ad 00 64 00 0a 00 00 1a ab f8`
direction: device to host
- description: measurement, with load
- content: same as measurement, without load
- `fa 0a 00 0a 00 00 00 00 00 f8`
direction: device to host
- description: load timer
- content:
`00 0a`: time minutes passed since load start
- `fa 64 00 00 00 00 01 3b 00 e7 01 50 09 6f 10 a0 1a 24 f8`
direction: device to host
- description: device measurement, without load
- content:
`00 00`: current in 0.0001 A
- `00 00`: voltage in 0.001 V
- `01 3b`: voltage of D+ 0.001 V
- `00 e7`: voltage of D- 0.001 V
- `01 50`: version in 0.01
- `09 6f`: unknown (seems constant)
- `10 a0`: unknown (seems constant)
- `1a`: device (0x1a = EBD-USB+)
- `fa 6e 08 52 14 67 07 95 07 9c 01 50 09 6f 10 a0 1a d3 f8`
direction: device to host
- description: device measurement, with load
- content: same as device measurement, without load

## Photos

<div class="photo-grid" markdown>

[![Ztetech Ebd Usb 2b](./img/Ztetech-ebd-usb_2B.png)](./img/Ztetech-ebd-usb_2B.png "Ztetech Ebd Usb 2b"){ .glightbox data-gallery="zketech-ebd-usb" }
<span class="caption">Ztetech Ebd Usb 2b</span>

[![Zketech Ebd Usb 2b Left](./img/Zketech-ebd-usb_2B_left.jpg)](./img/Zketech-ebd-usb_2B_left.jpg "Zketech Ebd Usb 2b Left"){ .glightbox data-gallery="zketech-ebd-usb" }
<span class="caption">Zketech Ebd Usb 2b Left</span>

[![Zketech Ebd Usb 2b Bottom](./img/Zketech-ebd-usb_2B_bottom.jpg)](./img/Zketech-ebd-usb_2B_bottom.jpg "Zketech Ebd Usb 2b Bottom"){ .glightbox data-gallery="zketech-ebd-usb" }
<span class="caption">Zketech Ebd Usb 2b Bottom</span>

[![Zketech Ebd Usb 2b Top](./img/Zketech-ebd-usb_2B_top.jpg)](./img/Zketech-ebd-usb_2B_top.jpg "Zketech Ebd Usb 2b Top"){ .glightbox data-gallery="zketech-ebd-usb" }
<span class="caption">Zketech Ebd Usb 2b Top</span>

</div>
## Resources
- [Vendor software](http://www.zketech.com/nd.jsp?id=15#_np=101_304)

