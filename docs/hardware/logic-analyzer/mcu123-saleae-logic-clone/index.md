---
title: MCU123 Saleae Logic clone
---

# MCU123 Saleae Logic clone

<div class="infobox" markdown>

![MCU123 Saleae Logic clone](./img/Mcu123_saleae_logic_clone_top.jpg){ .infobox-image }

### MCU123 Saleae Logic clone

| | |
|---|---|
| **Status** | supported |
| **Source code** | [fx2lafw](https://github.com/OpenTraceLab/OpenTraceCapture/tree/main/src/hardware/fx2lafw) |
| **Channels** | 8 |
| **Samplerate** | 24MHz |
| **Samplerate (state)** | — |
| **Triggers** | none (SW-only) |
| **Min/max voltage** | -0.5V — 5.25V |
| **Threshold voltage** | Fixed: VIH=2.0V—5.25V, VIL=-0.5V—0.8V |
| **Memory** | none |
| **Compression** | none |
| **Price range** | $5 - $10 |
| **Website** | [mcu123.com](http://translate.google.de/translate?sl=zh-CN&amp;tl=en&amp;js=n&amp;prev=_t&amp;hl=de&amp;ie=UTF-8&amp;eotf=1&amp;u=http%3A%2F%2Fwww.mcu123.com%2Fwww%2Fprodshow.asp%3FProdId%3DNO054&amp;act=url) |

</div>

The **MCU123 Saleae Logic clone** is a USB-based, 8-channel logic analyzer with up to 24MHz sampling rate.

It is a clone of the [Saleae Logic](https://sigrok.org/wiki/Saleae_Logic). It's also *very* similar to the [MCU123 USBee AX Pro clone](https://sigrok.org/wiki/MCU123_USBee_AX_Pro_clone) minus the different USB vendor/device IDs.

In sigrok, we use the open-source [fx2lafw](https://sigrok.org/wiki/Fx2lafw) firmware for this logic analyzer.

See [MCU123 Saleae Logic clone/Info](https://sigrok.org/wiki/MCU123_Saleae_Logic_clone/Info) for more detailed information on the device.

## Hardware
- **Main chip**: Cypress CY7C68013-56PVC (FX2)
- **Input buffer**: NXP 74HC245 (markings: "NXP HC245 2A7K508 UnD2 18E")
- **256-byte I2C EEPROM**: Atmel AT24C02 (markings: "ATMEL211 24C02N SU27 D")
- **3.3V low-dropout voltage regulator**: Advanced Monolithic Systems AMS1117-3.3 (markings: "AMS1117 3.3 HT240E")
- **24MHz crystal**: 24.000

## Photos

<div class="photo-grid" markdown>

[![Mcu123 Saleae Logic Clone Top](./img/Mcu123_saleae_logic_clone_top.jpg)](./img/Mcu123_saleae_logic_clone_top.jpg "Mcu123 Saleae Logic Clone Top"){ .glightbox data-gallery="mcu123-saleae-logic-clone" }
<span class="caption">Mcu123 Saleae Logic Clone Top</span>

[![Mcu123 Saleae Logic Clone Eeprom](./img/Mcu123_saleae_logic_clone_eeprom.jpg)](./img/Mcu123_saleae_logic_clone_eeprom.jpg "Mcu123 Saleae Logic Clone Eeprom"){ .glightbox data-gallery="mcu123-saleae-logic-clone" }
<span class="caption">Mcu123 Saleae Logic Clone Eeprom</span>

[![Mcu123 Saleae Logic Clone Package Contents](./img/Mcu123_saleae_logic_clone_package_contents.jpg)](./img/Mcu123_saleae_logic_clone_package_contents.jpg "Mcu123 Saleae Logic Clone Package Contents"){ .glightbox data-gallery="mcu123-saleae-logic-clone" }
<span class="caption">Mcu123 Saleae Logic Clone Package Contents</span>

[![Mcu123 Saleae Logic Clone Bottom](./img/Mcu123_saleae_logic_clone_bottom.jpg)](./img/Mcu123_saleae_logic_clone_bottom.jpg "Mcu123 Saleae Logic Clone Bottom"){ .glightbox data-gallery="mcu123-saleae-logic-clone" }
<span class="caption">Mcu123 Saleae Logic Clone Bottom</span>

[![Mcu123 Saleae Logic Clone Pcb Bottom](./img/Mcu123_saleae_logic_clone_pcb_bottom.jpg)](./img/Mcu123_saleae_logic_clone_pcb_bottom.jpg "Mcu123 Saleae Logic Clone Pcb Bottom"){ .glightbox data-gallery="mcu123-saleae-logic-clone" }
<span class="caption">Mcu123 Saleae Logic Clone Pcb Bottom</span>

[![Mcu123 Saleae Logic Clone Pcb Top](./img/Mcu123_saleae_logic_clone_pcb_top.jpg)](./img/Mcu123_saleae_logic_clone_pcb_top.jpg "Mcu123 Saleae Logic Clone Pcb Top"){ .glightbox data-gallery="mcu123-saleae-logic-clone" }
<span class="caption">Mcu123 Saleae Logic Clone Pcb Top</span>

[![Mcu123 Saleae Logic Clone](./img/Mcu123_saleae_logic_clone.png)](./img/Mcu123_saleae_logic_clone.png "Mcu123 Saleae Logic Clone"){ .glightbox data-gallery="mcu123-saleae-logic-clone" }
<span class="caption">Mcu123 Saleae Logic Clone</span>

</div>
## Protocol

Since we use the open-source [fx2lafw](https://sigrok.org/wiki/Fx2lafw) firmware for this device, we don't need to know the protocol.

## Resources
- [Random aliexpress.com vendor](http://www.aliexpress.com/item/USB-Saleae-24M-8CH-Saleae-24MHz-8Channel-Logic-Analyzer-saleae-24M-8CH-Latest-support-1-1/737326718.html) (there are many)
- [Random Taobao vendor](http://translate.google.com/translate?act=url&hl=de&ie=UTF8&prev=_t&rurl=translate.google.com&sl=zh-CN&tl=en&u=http://item.taobao.com/item.htm%3Fid%3D15872520745) (there are many)
- [hotmcu.com shop](http://www.hotmcu.com/saleae-24mhz-8channel-logic-analyzer-p-28.html)

