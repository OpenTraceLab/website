---
title: VKTECH saleae clone
---

# VKTECH saleae clone

<div class="infobox" markdown>

![VKTECH saleae clone](./img/VKTECH_PCB_front.jpg){ .infobox-image }

### VKTECH saleae clone

| | |
|---|---|
| **Status** | supported |
| **Source code** | [fx2lafw](https://github.com/OpenTraceLab/OpenTraceCapture/tree/main/src/hardware/fx2lafw) |
| **Channels** | 8 |
| **Samplerate** | 24MHz |
| **Samplerate (state)** | — |
| **Triggers** | none (SW-only) |
| **Min/max voltage** | max. 5.25V |
| **Threshold voltage** | Fixed: VIH=1.4V, VIL=0.8V |
| **Memory** | none |
| **Compression** | none |
| **Price range** | $5 - $10 |
| **Website** | [[1]](http://xxxx) |

</div>

The **VKTECH** is a fairly standard Cypress FX2 based 8 channel 24 MHz logic analyzer, it is most similar to the [ARMFLY_Mini-Logic](https://sigrok.org/wiki/ARMFLY_Mini-Logic) and [MCU123_USBee_AX_Pro_clone](https://sigrok.org/wiki/MCU123_USBee_AX_Pro_clone) devices, though has differences from both of them (SMD LEDs, QFN package unlike MCU123, transceiver IC unlike ARMFLY).

sigrok uses the open-source [fx2lafw](https://sigrok.org/wiki/Fx2lafw) firmware for this logic analyzer.

The device uses USB\VID_0925&PID_3881 so is indistinguishable from a [Saleae_Logic](https://sigrok.org/wiki/Saleae_Logic) device

Mine was purchased from [AliExpress](https://aliexpress.com/item/24MHz-8-Channel-Logic-Analyzer/32814170174.html) and arrived in 6 days.

## Hardware
- **Main chip**: Cypress CY7C68013A-56LTXC (FX2LP in QFN package)
- **Transceiver** NXP LVC245A
- **3.3V voltage regulator**: 6206A  1711/33
- **I²C EEPROM**: ATMHK218  24C02N
- **Crystal**: 24MHz

## Photos

<div class="photo-grid" markdown>

[![Vktech Pcb Front](./img/VKTECH_PCB_front.jpg)](./img/VKTECH_PCB_front.jpg "Vktech Pcb Front"){ .glightbox data-gallery="vktech-saleae-clone" }
<span class="caption">Vktech Pcb Front</span>

[![Vktech Pcb Rear](./img/VKTECH_PCB_rear.jpg)](./img/VKTECH_PCB_rear.jpg "Vktech Pcb Rear"){ .glightbox data-gallery="vktech-saleae-clone" }
<span class="caption">Vktech Pcb Rear</span>

[![Vktech Connected](./img/VKTECH_connected.jpg)](./img/VKTECH_connected.jpg "Vktech Connected"){ .glightbox data-gallery="vktech-saleae-clone" }
<span class="caption">Vktech Connected</span>

[![Vktech Case](./img/VKTECH_case.jpg)](./img/VKTECH_case.jpg "Vktech Case"){ .glightbox data-gallery="vktech-saleae-clone" }
<span class="caption">Vktech Case</span>

[![Vktech Thumb](./img/VKTECH_thumb.jpg)](./img/VKTECH_thumb.jpg "Vktech Thumb"){ .glightbox data-gallery="vktech-saleae-clone" }
<span class="caption">Vktech Thumb</span>

</div>
## Links

[neko.ne.jp/~freewing](http://www.neko.ne.jp/~freewing/hardware/usb_logic_analyzer_cy7c68013a_clone)

