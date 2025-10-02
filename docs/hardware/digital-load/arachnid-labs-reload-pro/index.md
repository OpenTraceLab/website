---
title: Arachnid Labs Reload Pro
---

# Arachnid Labs Reload Pro

<div class="infobox" markdown>

![Arachnid Labs Reload Pro](./img/Arachnid_Labs_ReLoad_Pro_-_Mugshot.png){ .infobox-image }

### Arachnid Labs Reload Pro

| | |
|---|---|
| **Status** | supported |
| **Source code** | [arachnid-labs-re-load-pro](https://github.com/OpenTraceLab/OpenTraceCapture/tree/main/src/hardware/arachnid-labs-re-load-pro) |
| **Channels** | 1 |
| **Voltage/current (CH1)** | 25W (50W with fan kit) / 0-6A / 0-60V |
| **Connectivity** | USB |
| **Features** | DC constant current load |
| **Website** | [arachnidlabs.com](http://www.arachnidlabs.com/reload-pro) |

</div>

The **Arachnid Labs Re:load Pro** is a programmable DC electronic load (25W, or 50W with fan kit, 0~6A, 0~60V) with serial connectivity over USB.

See [Arachnid Labs Reload Pro/Info](https://sigrok.org/wiki/Arachnid_Labs_Reload_Pro/Info) for more details (such as **lsusb -v** output) about the device.

## Hardware
- **Cypress PSoC 4200 series microcontroller**: [Cypress CY8C4245PVI-482](http://www.cypress.com/part/cy8c4245pvi-482) ([datasheet](http://www.cypress.com/file/138656/download))
- **Pass transistor**: [Infineon BTS141](https://www.infineon.com/cms/en/product/power/smart-low-side-and-high-side-switches/automotive-smart-low-side-switch-hitfet/BTS141/productType.html?productType=db3a30443a06def4013ab74184b1278c) ([datasheet](https://www.infineon.com/dgdl/Infineon-BTS141-DS-v01_00-EN.pdf?fileId=5546d46259d9a4bf015a84e19f937577))
- **Optional fan kit**

## Photos

<div class="photo-grid" markdown>

[![Arachnid Labs Reload Pro Mugshot](./img/Arachnid_Labs_ReLoad_Pro_-_Mugshot.png)](./img/Arachnid_Labs_ReLoad_Pro_-_Mugshot.png "Arachnid Labs Reload Pro Mugshot"){ .glightbox data-gallery="arachnid-labs-reload-pro" }
<span class="caption">Arachnid Labs Reload Pro Mugshot</span>

[![Arachnid Labs Reload Pro Pcb Top 1](./img/Arachnid_Labs_ReLoad_Pro_-_PCB_Top_1.jpg)](./img/Arachnid_Labs_ReLoad_Pro_-_PCB_Top_1.jpg "Arachnid Labs Reload Pro Pcb Top 1"){ .glightbox data-gallery="arachnid-labs-reload-pro" }
<span class="caption">Arachnid Labs Reload Pro Pcb Top 1</span>

[![Arachnid Labs Reload Pro Back Fan Kit](./img/Arachnid_Labs_ReLoad_Pro_-_Back_Fan_Kit.jpg)](./img/Arachnid_Labs_ReLoad_Pro_-_Back_Fan_Kit.jpg "Arachnid Labs Reload Pro Back Fan Kit"){ .glightbox data-gallery="arachnid-labs-reload-pro" }
<span class="caption">Arachnid Labs Reload Pro Back Fan Kit</span>

[![Arachnid Labs Reload Pro Pcb Top 2](./img/Arachnid_Labs_ReLoad_Pro_-_PCB_Top_2.jpg)](./img/Arachnid_Labs_ReLoad_Pro_-_PCB_Top_2.jpg "Arachnid Labs Reload Pro Pcb Top 2"){ .glightbox data-gallery="arachnid-labs-reload-pro" }
<span class="caption">Arachnid Labs Reload Pro Pcb Top 2</span>

[![Arachnid Labs Reload Pro Pcb Bottom](./img/Arachnid_Labs_ReLoad_Pro_-_PCB_Bottom.jpg)](./img/Arachnid_Labs_ReLoad_Pro_-_PCB_Bottom.jpg "Arachnid Labs Reload Pro Pcb Bottom"){ .glightbox data-gallery="arachnid-labs-reload-pro" }
<span class="caption">Arachnid Labs Reload Pro Pcb Bottom</span>

[![Arachnid Labs Reload Pro Top](./img/Arachnid_Labs_ReLoad_Pro_-_Top.jpg)](./img/Arachnid_Labs_ReLoad_Pro_-_Top.jpg "Arachnid Labs Reload Pro Top"){ .glightbox data-gallery="arachnid-labs-reload-pro" }
<span class="caption">Arachnid Labs Reload Pro Top</span>

[![Arachnid Labs Reload Pro Front](./img/Arachnid_Labs_ReLoad_Pro_-_Front.jpg)](./img/Arachnid_Labs_ReLoad_Pro_-_Front.jpg "Arachnid Labs Reload Pro Front"){ .glightbox data-gallery="arachnid-labs-reload-pro" }
<span class="caption">Arachnid Labs Reload Pro Front</span>

</div>
## Protocol

See [protocol documentation](http://www.arachnidlabs.com/reload-pro/usb-interface).

## Resources
- [Manual](https://github.com/arachnidlabs/reload-pro/raw/master/User%20Manual.pdf)
- [GitHub with PCB and firmware](https://github.com/arachnidlabs/reload-pro/)
- [Fan kit](http://www.arachnidlabs.com/reload-pro/fan-kit)

