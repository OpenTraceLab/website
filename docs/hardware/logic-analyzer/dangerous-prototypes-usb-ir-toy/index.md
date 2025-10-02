---
title: Dangerous Prototypes USB IR Toy
---

# Dangerous Prototypes USB IR Toy

<div class="infobox" markdown>

![Dangerous Prototypes USB IR Toy](./img/Dangerous_prototypes_irtoy_bottom.jpg){ .infobox-image }

### Dangerous Prototypes USB IR Toy

| | |
|---|---|
| **Status** | supported |
| **Source code** | [openbench-logic-sniffer](https://github.com/OpenTraceLab/OpenTraceCapture/tree/main/src/hardware/openbench-logic-sniffer) |
| **Channels** | 1 |
| **Samplerate** | 10kHz |
| **Samplerate (state)** | — |
| **Triggers** | automatically triggers upon IR signal |
| **Min/max voltage** | N/A |
| **Memory** | 1024 bytes |
| **Compression** | none |
| **Website** | [dangerousprototypes.com](http://dangerousprototypes.com/docs/USB_Infrared_Toy) |

</div>

The **Dangerous Prototypes USB IR Toy** is a USB-based, 1-channel logic analyzer with a 10kHz sampling rate.

The hardware design is available under a Creative Commons (CC-BY-SA) license.

See [Dangerous Prototypes USB IR Toy/Info](https://sigrok.org/wiki/Dangerous_Prototypes_USB_IR_Toy/Info) for more details (such as **lsusb -v** output) about the device.

## Hardware
- **8-bit microcontroller with integrated USB Full-Speed support**: [Microchip PIC18F2550-I/SO](http://www.microchip.com/wwwproducts/Devices.aspx?dDocName=en010280) ([datasheet](http://ww1.microchip.com/downloads/en/DeviceDoc/39632e.pdf))
- 20MHz crystal
- IR transmitter (LED): Vishay TSAL7400
- IR receiver / demodulator: Vishay TSOP38238
- IR frequency detector: Fairchild QSE159

## Photos

<div class="photo-grid" markdown>

[![Dangerous Prototypes Irtoy Bottom](./img/Dangerous_prototypes_irtoy_bottom.jpg)](./img/Dangerous_prototypes_irtoy_bottom.jpg "Dangerous Prototypes Irtoy Bottom"){ .glightbox data-gallery="dangerous-prototypes-usb-ir-toy" }
<span class="caption">Dangerous Prototypes Irtoy Bottom</span>

[![Dangerous Prototypes Irtoy Mugshot](./img/Dangerous_prototypes_irtoy_mugshot.jpg)](./img/Dangerous_prototypes_irtoy_mugshot.png "Dangerous Prototypes Irtoy Mugshot"){ .glightbox data-gallery="dangerous-prototypes-usb-ir-toy" }
<span class="caption">Dangerous Prototypes Irtoy Mugshot</span>

[![Dangerous Prototypes Irtoy Top](./img/Dangerous_prototypes_irtoy_top.jpg)](./img/Dangerous_prototypes_irtoy_top.jpg "Dangerous Prototypes Irtoy Top"){ .glightbox data-gallery="dangerous-prototypes-usb-ir-toy" }
<span class="caption">Dangerous Prototypes Irtoy Top</span>

</div>
## Protocol

The USB IR Toy uses the [extended SUMP protocol](http://dangerousprototypes.com/docs/The_Logic_Sniffer%27s_extended_SUMP_protocol), as used by the [Openbench Logic Sniffer](https://sigrok.org/wiki/Openbench_Logic_Sniffer) driver. It is thus supported in sigrok out of the box.

## Resources
- [USB Infrared Toy](http://dangerousprototypes.com/docs/USB_Infrared_Toy) (main wiki page)
- [USB Infrared Toy forum](http://dangerousprototypes.com/forum/viewforum.php?f=29)

