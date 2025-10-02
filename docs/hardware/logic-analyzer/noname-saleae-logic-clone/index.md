---
title: Noname Saleae Logic clone
---

# Noname Saleae Logic clone

<div class="infobox" markdown>

![Noname Saleae Logic clone](./img/LogicAnalyzer2.jpg){ .infobox-image }

### Noname Saleae Logic clone

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

The **Noname Saleae Logic clone** is USB-based logic analyzer with 8-channel and up to 24MHz sample-rate.

It is a clone of the [Saleae Logic](https://sigrok.org/wiki/Saleae_Logic).

In sigrok, we use the open-source [fx2lafw](https://sigrok.org/wiki/Fx2lafw) firmware for this logic analyzer.

See [Noname Saleae Logic clone/Info](/w/index.php?title=Noname_Saleae_Logic_clone/Info&action=edit&redlink=1) for more details (such as **lsusb -v** output) about the device.

## Hardware
- **Main chip**: Cypress CY7C68013A-56LTXC (FX2)
- **Input buffer**: NXP 74LVC245A (markings: "NXP LVC245A KX44549 TXD613F")
- **32kByte I²C EEPROM**: Atmel AT24C256 (markings: "ATML H612 02DM B A2C9JF")
- **Voltage regulator**: Torex Semiconductor XC6206 (markings: "6206A 1625/33")
- **24MHz crystal**: K24.000

## Photos

<div class="photo-grid" markdown>

[![Logicanalyzer2](./img/LogicAnalyzer2.jpg)](./img/LogicAnalyzer2.jpg "Logicanalyzer2"){ .glightbox data-gallery="noname-saleae-logic-clone" }
<span class="caption">Logicanalyzer2</span>

[![Logicanalyzer5](./img/LogicAnalyzer5.jpg)](./img/LogicAnalyzer5.jpg "Logicanalyzer5"){ .glightbox data-gallery="noname-saleae-logic-clone" }
<span class="caption">Logicanalyzer5</span>

[![Logicanalyzer1](./img/LogicAnalyzer1.jpg)](./img/LogicAnalyzer1.jpg "Logicanalyzer1"){ .glightbox data-gallery="noname-saleae-logic-clone" }
<span class="caption">Logicanalyzer1</span>

[![Logicanalyzer3](./img/LogicAnalyzer3.jpg)](./img/LogicAnalyzer3.jpg "Logicanalyzer3"){ .glightbox data-gallery="noname-saleae-logic-clone" }
<span class="caption">Logicanalyzer3</span>

[![Noname Saleae Logic Clone Mugshot](./img/Noname_saleae_logic_clone_mugshot.jpg)](./img/Noname_saleae_logic_clone_mugshot.png "Noname Saleae Logic Clone Mugshot"){ .glightbox data-gallery="noname-saleae-logic-clone" }
<span class="caption">Noname Saleae Logic Clone Mugshot</span>

[![Logicanalyzerbox](./img/LogicAnalyzerBox.jpg)](./img/LogicAnalyzerBox.jpg "Logicanalyzerbox"){ .glightbox data-gallery="noname-saleae-logic-clone" }
<span class="caption">Logicanalyzerbox</span>

[![Logicanalyzer4](./img/LogicAnalyzer4.jpg)](./img/LogicAnalyzer4.jpg "Logicanalyzer4"){ .glightbox data-gallery="noname-saleae-logic-clone" }
<span class="caption">Logicanalyzer4</span>

</div>
## Protocol

Since we use the open-source [fx2lafw](https://sigrok.org/wiki/Fx2lafw) firmware for this device, we don't need to know the protocol.

## Resources
- [Ebay seller](http://www.ebay.de/itm/USB-Logic-Analyzer-8-Kanal-24MHz-I2C-SPI-JTAG-CAN-LIN-UART-e02/122164455000)

