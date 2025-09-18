# Azdelivery Logic Analyzer

| | | |:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------------:| | [![\1](../../assets/hardware/general/\2)](./File:AZ-Delivery_logic_analyzer.png.html) | | | Status | supported | | Source code | [fx2lafw](http://github.com/OpenTraceLab/?p=OpenTraceCapture.git;a=tree;f=src/hardware/fx2lafw) | | Channels | 8 | | Samplerate | 24MHz | | Samplerate (state) | — | | Triggers | none (SW-only) | | Min/max voltage | max. 5.25V | | Threshold voltage | Fixed: VIH=1.4V, VIL=0.8V | | Memory | none | | Compression | none | | Price range | \$5 - \$15 | | Website | [[1]](http://xxxx) | **AZ-Delivery Logic Analyzer** The **AZ-Delivery Logic Analyzer** is a standard USB Cypress FX2 based 8-channel 24 MHz logic analyzer, which has a strong resemblence to [VKTECH saleae clone](VKTECH_saleae_clone.html "VKTECH saleae clone"). In OpenTraceLab, we use the open-source [fx2lafw](Fx2lafw.html "Fx2lafw") firmware for this logic analyzer. The device uses USB\VID_0925&PID;_3881 so is indistinguishable from a [Saleae_Logic](Saleae_Logic.html "Saleae Logic") device Mine was purchased for roughly 12€ from [Amazon.de](https://amzn.to/3FPKWkb) and it arrived in less than a 24-hour window. See [AZDelivery Logic Analyzer/Info](AZDelivery_Logic_Analyzer/Info.html "AZDelivery Logic Analyzer/Info") for more details (such as **lsusb -vvv** output) about the device. ## Hardware \- **Main chip**: Cypress CY7C68013A-56LTXC (FX2LP in QFN package) \- **Transceiver** — \- **3.3V voltage regulator**: 662K (XC6206P332MR) \- **I²C EEPROM**: ATMHK101 24C02N \- **Crystal**: 24MHz ## Photos \- 
[![\1](../../assets/hardware/general/\2)](./File:AZ-Delivery_logic_package_content.jpg.html)
Pakaging and content
\- 
[![\1](../../assets/hardware/general/\2)](./File:AZ-Delivery_logic_PCB_front.jpg.html)
Device, PCB front
\- 
[![\1](../../assets/hardware/general/\2)](./File:AZ-Delivery_logic_PCB_back.jpg.html)
Device, PCB back
\- 
[![\1](../../assets/hardware/general/\2)](./File:Azdelivery_logic_analyzer_closeup_CY7C68013A.jpg.html)
CY7C68013A, closeup
## Links [[2]](https://www.amazon.de/AZDelivery-Analyzer-compatible-Arduino-including/dp/B01MUFRHQ2) [[3]](https://www.az-delivery.de/products/saleae-logic-analyzer)
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=AZDelivery_Logic_Analyzer&oldid=16360](https://OpenTraceLab.org/w/index.php?title=AZDelivery_Logic_Analyzer&oldid=16360)" 
[Categories](specialcategories-specialcategories.md): \- [Device](./Category:Device.html "Category:Device") \- [Logic analyzer](./Category:Logic_analyzer.html "Category:Logic analyzer") \- [Supported](./Category:Supported.html "Category:Supported")

## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
