---
title: AZ-Delivery Logic Analyzer
---

# AZ-Delivery Logic Analyzer

<div class="infobox" markdown>

![AZ-Delivery Logic Analyzer](./img/AZ-Delivery_logic_PCB_front.jpg){ .infobox-image }

### AZ-Delivery Logic Analyzer

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
| **Price range** | $5 - $15 |
| **Website** | [[1]](http://xxxx) |

</div>

The **AZ-Delivery Logic Analyzer** is a standard USB Cypress FX2 based 8-channel 24 MHz logic analyzer, which has a strong resemblence to [VKTECH saleae clone](https://sigrok.org/wiki/VKTECH_saleae_clone).

In sigrok, we use the open-source [fx2lafw](https://sigrok.org/wiki/Fx2lafw) firmware for this logic analyzer.

The device uses USB\VID_0925&PID_3881 so is indistinguishable from a [Saleae_Logic](https://sigrok.org/wiki/Saleae_Logic) device

Mine was purchased for roughly 12€ from [Amazon.de](https://amzn.to/3FPKWkb) and it arrived in less than a 24-hour window. 

See [AZDelivery Logic Analyzer/Info](https://sigrok.org/wiki/AZDelivery_Logic_Analyzer/Info) for more details (such as **lsusb -vvv** output) about the device.

## Hardware
- **Main chip**: Cypress CY7C68013A-56LTXC (FX2LP in QFN package)
- **Transceiver** —
- **3.3V voltage regulator**: 662K (XC6206P332MR)
- **I²C EEPROM**: ATMHK101  24C02N
- **Crystal**: 24MHz

## Photos

<div class="photo-grid" markdown>

[![Az Delivery Logic Pcb Front](./img/AZ-Delivery_logic_PCB_front.jpg)](./img/AZ-Delivery_logic_PCB_front.jpg "Az Delivery Logic Pcb Front"){ .glightbox data-gallery="az-delivery-logic-analyzer" }
<span class="caption">Az Delivery Logic Pcb Front</span>

[![Azdelivery Logic Analyzer Closeup Cy7c68013a](./img/Azdelivery_logic_analyzer_closeup_CY7C68013A.jpg)](./img/Azdelivery_logic_analyzer_closeup_CY7C68013A.jpg "Azdelivery Logic Analyzer Closeup Cy7c68013a"){ .glightbox data-gallery="az-delivery-logic-analyzer" }
<span class="caption">Azdelivery Logic Analyzer Closeup Cy7c68013a</span>

[![Az Delivery Logic Pcb Back](./img/AZ-Delivery_logic_PCB_back.jpg)](./img/AZ-Delivery_logic_PCB_back.jpg "Az Delivery Logic Pcb Back"){ .glightbox data-gallery="az-delivery-logic-analyzer" }
<span class="caption">Az Delivery Logic Pcb Back</span>

[![Az Delivery Logic Analyzer](./img/AZ-Delivery_logic_analyzer.jpg)](./img/AZ-Delivery_logic_analyzer.png "Az Delivery Logic Analyzer"){ .glightbox data-gallery="az-delivery-logic-analyzer" }
<span class="caption">Az Delivery Logic Analyzer</span>

[![Az Delivery Logic Package Content](./img/AZ-Delivery_logic_package_content.jpg)](./img/AZ-Delivery_logic_package_content.jpg "Az Delivery Logic Package Content"){ .glightbox data-gallery="az-delivery-logic-analyzer" }
<span class="caption">Az Delivery Logic Package Content</span>

</div>
## Links

[[2]](https://www.amazon.de/AZDelivery-Analyzer-compatible-Arduino-including/dp/B01MUFRHQ2)
[[3]](https://www.az-delivery.de/products/saleae-logic-analyzer)

