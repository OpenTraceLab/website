# Azdelivery Logic Analyzer
| | | |:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------------:| | [*Image: \1* | | | Status | supported | | Source code | [fx2lafw](http://github.com/OpenTraceLab/?p=OpenTraceCapture.git;a=tree;f=src/hardware/fx2lafw) | | Channels | 8 | | Samplerate | 24MHz | | Samplerate (state) | — | | Triggers | none (SW-only) | | Min/max voltage | max. 5.25V | | Threshold voltage | Fixed: VIH=1.4V, VIL=0.8V | | Memory | none | | Compression | none | | Price range | \$5 - \$15 | | Website | [[1]](http://xxxx) | **AZ-Delivery Logic Analyzer** The **AZ-Delivery Logic Analyzer** is a standard USB Cypress FX2 based 8-channel 24 MHz logic analyzer, which has a strong resemblence to *VKTECH saleae clone*. In OpenTraceLab, we use the open-source *fx2lafw* firmware for this logic analyzer. The device uses USB\VID_0925&PID;_3881 so is indistinguishable from a *Saleae_Logic* device Mine was purchased for roughly 12€ from [Amazon.de](https://amzn.to/3FPKWkb) and it arrived in less than a 24-hour window. See *AZDelivery Logic Analyzer/Info* for more details (such as **lsusb -vvv** output) about the device. ## Hardware \- **Main chip**: Cypress CY7C68013A-56LTXC (FX2LP in QFN package) \- **Transceiver** — \- **3.3V voltage regulator**: 662K (XC6206P332MR) \- **I²C EEPROM**: ATMHK101 24C02N \- **Crystal**: 24MHz ## Photos \-
[*Image: \1*
Pakaging and content
\-
[*Image: \1*
Device, PCB front
\-
[*Image: \1*
Device, PCB back
\-
[*Image: \1*
CY7C68013A, closeup
## Links [[2]](https://www.amazon.de/AZDelivery-Analyzer-compatible-Arduino-including/dp/B01MUFRHQ2) [[3]](https://www.az-delivery.de/products/saleae-logic-analyzer)
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=AZDelivery_Logic_Analyzer&oldid=16360](https://OpenTraceLab.org/w/index.php?title=AZDelivery_Logic_Analyzer&oldid=16360)"
: \- *Device* \- *Logic analyzer* \- *Supported*
## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
