---
title: 128axc-based USBee AX-Pro clone
---

# 128axc-based USBee AX-Pro clone

<div class="infobox" markdown>

![128axc-based USBee AX-Pro clone](./img/128axc-usbee-axpro-clone-Nxp-input-buffer.jpg){ .infobox-image }

### 128axc-based USBee AX-Pro clone

| | |
|---|---|
| **Status** | supported |
| **Source code** | [fx2lafw](https://github.com/OpenTraceLab/OpenTraceCapture/tree/main/src/hardware/fx2lafw) |
| **Channels** | 8 |
| **Samplerate** | 24MHz |
| **Samplerate (state)** | — |
| **Triggers** | none (SW-only) |
| **Min/max voltage** | -0.5V — 5.25V (absolute max rating) |
| **Threshold voltage** | Fixed: VIH=2.0V—5.25V, VIL=-0.5V—0.8V |
| **Memory** | none |
| **Compression** | none |
| **Website** | none |

</div>

The **128axc-based USBee AX-Pro clone** is a USB-based logic analyzer with 8-channel and up to 24MHz sample-rate.

It is yet another Cypress FX2 based logic analyzer. This one reports on USB as 08a9:0014 which is [CWAV USBee AX-Pro](/w/index.php?title=CWAV_USBee_AX-Pro&action=edit&redlink=1), but contrary to the original (or other clones such as [HT_USBee-AxPro](https://sigrok.org/wiki/HT_USBee-AxPro)), it has no Analog input.

In sigrok, we use the open-source [fx2lafw](https://sigrok.org/wiki/Fx2lafw) firmware for this logic analyzer.

See [128axc-based USBee AX-Pro clone/Info](https://sigrok.org/wiki/128axc-based_USBee_AX-Pro_clone/Info) for more details (such as **lsusb -v** output) about the device.

## Hardware
- **Main chip**: [Cypress CY7C68013A-128AXC (FX2)](http://www.cypress.com/part/cy7c68013a-128axc)
- **Input buffer**: NXP HC245
- **2kByte I²C EEPROM**: Atmel A24C02BN
- **Voltage regulator**: AMS 117
- **24MHz crystal**: RJH24.000
- No DAC is present, no Analog entry possible.

## Photos

<div class="photo-grid" markdown>

[![128axc Usbee Axpro Clone Nxp Input Buffer](./img/128axc-usbee-axpro-clone-Nxp-input-buffer.jpg)](./img/128axc-usbee-axpro-clone-Nxp-input-buffer.jpg "128axc Usbee Axpro Clone Nxp Input Buffer"){ .glightbox data-gallery="128axc-based-usbee-ax-pro-clone" }
<span class="caption">128axc Usbee Axpro Clone Nxp Input Buffer</span>

[![128axc Usbee Axpro Clone Front](./img/128axc-usbee-axpro-clone-Front.jpg)](./img/128axc-usbee-axpro-clone-Front.jpg "128axc Usbee Axpro Clone Front"){ .glightbox data-gallery="128axc-based-usbee-ax-pro-clone" }
<span class="caption">128axc Usbee Axpro Clone Front</span>

[![128axc Usbee Axpro Clone Overview](./img/128axc-usbee-axpro-clone-Overview.jpg)](./img/128axc-usbee-axpro-clone-Overview.jpg "128axc Usbee Axpro Clone Overview"){ .glightbox data-gallery="128axc-based-usbee-ax-pro-clone" }
<span class="caption">128axc Usbee Axpro Clone Overview</span>

[![128axc Usbee Axpro Clone Back Cypress](./img/128axc-usbee-axpro-clone-Back-cypress.jpg)](./img/128axc-usbee-axpro-clone-Back-cypress.jpg "128axc Usbee Axpro Clone Back Cypress"){ .glightbox data-gallery="128axc-based-usbee-ax-pro-clone" }
<span class="caption">128axc Usbee Axpro Clone Back Cypress</span>

</div>
## Protocol

Since we use the open-source [fx2lafw](https://sigrok.org/wiki/Fx2lafw) firmware for this device, we don't need to know the protocol.

## Resources
- [Banggood seller](https://www.banggood.com/USB-Logic-Analyzer-24M-8CH-Microcontroller-ARM-FPGA-Debug-Tool-p-1177821.html)

