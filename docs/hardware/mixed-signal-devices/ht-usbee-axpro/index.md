---
title: HT USBee-AxPro
---

# HT USBee-AxPro

<div class="infobox" markdown>

![HT USBee-AxPro](./img/Ht_usbee_axpro_v5_mugshot.png){ .infobox-image }

### HT USBee-AxPro

| | |
|---|---|
| **Status** | supported |
| **Source code** | [fx2lafw](https://github.com/OpenTraceLab/OpenTraceCapture/tree/main/src/hardware/fx2lafw) |
| **Channels** | 8 + 1 |
| **Samplerate** | 8ch @ 24MHz, 8+1ch @ 12MHz |
| **Samplerate (state)** | — |
| **Triggers** | none (SW-only) |
| **Min/max voltage** | Digital: -1V — +6VAnalog: ±10V (±20V max) |
| **Threshold voltage** | Fixed: VIH=1.6V, VIL=1.4V |
| **Memory** | none |
| **Compression** | none |
| **Price range** | $35 - $45 |
| **Website** | [aliexpress.com](http://de.aliexpress.com/item/New-3-in-1-Tool-Oscilloscope-Logic-Analyzer-ALTERA-Saleae8-USBEE-AX-PRO-Altera-USB-Blaster/32236912930.html) |

</div>

The **HT USBee-AxPro** is a USB-based, 8-channel logic analyzer with up to 24MHz sampling rate, with 1 additional analog channel (3MHz analog bandwidth).

It is able to switch between USBee AX-Pro, Salea Logic and Altera USB blaster mode via a button. When pressing the button the USB VID/PID changes.

It is a clone of the [CWAV USBee AX-Pro](/w/index.php?title=CWAV_USBee_AX-Pro&action=edit&redlink=1).

In sigrok, we use the open-source [fx2lafw](https://sigrok.org/wiki/Fx2lafw) firmware for this logic analyzer.

See [HT USBee-AxPro/Info](https://sigrok.org/wiki/HT_USBee-AxPro/Info) for some more details (such as **lsusb -v** output) on the device.

## Hardware

**HT2013 V5.00**:

- **Main chip**: [Cypress CY7C68013A-56SSOP (FX2LP)](http://www.cypress.com/?docID=45142)
- **64Kbit I²C EEPROM**: [Microchip 24LC641](http://ww1.microchip.com/downloads/en/DeviceDoc/21189f.pdf)
- **2Kbit I²C EEPROM**: [Microchip 24LC02B](http://ww1.microchip.com/downloads/en/DeviceDoc/21709c.pdf)
- **Auxiliary 8051 chip**: [ST STM8S003F3](http://www.st.com/web/en/resource/technical/document/datasheet/DM00024550.pdf) (used for handling the button)
- **Supply voltage regulator**: Advanced Monolithic Systems AMS1117-3.3
- **Analog-to-digital converter**: [Texas Instruments TLC5510I](http://www.ti.com/lit/ds/symlink/tlc5510.pdf)
- **Analog input amplifiers**: [Analog Devices AD8065](http://www.analog.com/static/imported-files/data_sheets/AD8065_8066.pdf) (SMD marking "HRA")
- **Analog amplifiers negative supply**: [Intersil ICL7660 (7660 AIBAZ V120428A)](http://www.intersil.com/content/dam/Intersil/documents/icl7/icl7660.pdf)
- **Crystal**: 24MHz
### FX2LP pin mappings
| # | Pin | Destination | Remark |
|---|---|---|---|
|  | CTL2 | ADC_CLK | ADC clock |
|  | PD0..7 | ADC_D1..8 | ADC data output |

### Analog frontend

**Schematics**:

[](./img/Ht-usbee-axpro_analog_schematics.svg)

**Notes**:

- Some devices have R2 = 66.5Ω (instead of 66.5kΩ), this basically limits the range to -3.3V — +3.3V.
- TLC5510 is used with ~3.3V "reference" from LDO output which is both out of the allowed range and is a major source of inaccuracy.
- Some devices (probably those that do not have U5 populated) produce bogus min and max spikes when measuring certain voltages, this can probably be remedied by adding small (on the order of 10s pF) capacitance to U5 Vcc and GND pins or to the ADC CLK line.

**HT_V6.0**:

- ...
### Pin mappings

The FX2 CTL2 and PD0..7 pins are mapped exactly like the **HT2013 V5.00** version. The TLC5510I OE# pin is tied to GND.

## Photos

<div class="photo-grid" markdown>

[![Ht Usbee Axpro V5 Mugshot](./img/Ht_usbee_axpro_v5_mugshot.png)](./img/Ht_usbee_axpro_v5_mugshot.png "Ht Usbee Axpro V5 Mugshot"){ .glightbox data-gallery="ht-usbee-axpro" }
<span class="caption">Ht Usbee Axpro V5 Mugshot</span>

[![Ht Usbee Axpro V5 Intersil Icl7660](./img/Ht_usbee_axpro_v5_intersil_icl7660.jpg)](./img/Ht_usbee_axpro_v5_intersil_icl7660.jpg "Ht Usbee Axpro V5 Intersil Icl7660"){ .glightbox data-gallery="ht-usbee-axpro" }
<span class="caption">Ht Usbee Axpro V5 Intersil Icl7660</span>

[![Ht Usbee Axpro V5 Device Bottom](./img/Ht_usbee_axpro_v5_device_bottom.jpg)](./img/Ht_usbee_axpro_v5_device_bottom.jpg "Ht Usbee Axpro V5 Device Bottom"){ .glightbox data-gallery="ht-usbee-axpro" }
<span class="caption">Ht Usbee Axpro V5 Device Bottom</span>

[![Ht Usbee Axpro Connector](./img/Ht_usbee_axpro_connector.jpg)](./img/Ht_usbee_axpro_connector.jpg "Ht Usbee Axpro Connector"){ .glightbox data-gallery="ht-usbee-axpro" }
<span class="caption">Ht Usbee Axpro Connector</span>

[![Ht Usbee Backside](./img/Ht-usbee_backside.jpg)](./img/Ht-usbee_backside.jpg "Ht Usbee Backside"){ .glightbox data-gallery="ht-usbee-axpro" }
<span class="caption">Ht Usbee Backside</span>

[![Ht Usbee Axpro V5 Ams1117 3.3](./img/Ht_usbee_axpro_v5_ams1117-3.3.jpg)](./img/Ht_usbee_axpro_v5_ams1117-3.3.jpg "Ht Usbee Axpro V5 Ams1117 3.3"){ .glightbox data-gallery="ht-usbee-axpro" }
<span class="caption">Ht Usbee Axpro V5 Ams1117 3.3</span>

[![Ht Usbee Axpro 24mhz Crystal](./img/Ht_usbee_axpro_24mhz_crystal.jpg)](./img/Ht_usbee_axpro_24mhz_crystal.jpg "Ht Usbee Axpro 24mhz Crystal"){ .glightbox data-gallery="ht-usbee-axpro" }
<span class="caption">Ht Usbee Axpro 24mhz Crystal</span>

[![7660](./img/7660.jpg)](./img/7660.jpg "7660"){ .glightbox data-gallery="ht-usbee-axpro" }
<span class="caption">7660</span>

[![Ht Usbee Axpro Package](./img/Ht-usbee-axpro_package.jpg)](./img/Ht-usbee-axpro_package.jpg "Ht Usbee Axpro Package"){ .glightbox data-gallery="ht-usbee-axpro" }
<span class="caption">Ht Usbee Axpro Package</span>

[![Ht Usbee Axpro V5 Pcb Bottom](./img/Ht_usbee_axpro_v5_pcb_bottom.jpg)](./img/Ht_usbee_axpro_v5_pcb_bottom.jpg "Ht Usbee Axpro V5 Pcb Bottom"){ .glightbox data-gallery="ht-usbee-axpro" }
<span class="caption">Ht Usbee Axpro V5 Pcb Bottom</span>

[![Ht Usbee Axpro V5 Usb](./img/Ht_usbee_axpro_v5_usb.jpg)](./img/Ht_usbee_axpro_v5_usb.jpg "Ht Usbee Axpro V5 Usb"){ .glightbox data-gallery="ht-usbee-axpro" }
<span class="caption">Ht Usbee Axpro V5 Usb</span>

[![Ht Usbee Axpro Cypress Fx2](./img/Ht_usbee_axpro_cypress_fx2.jpg)](./img/Ht_usbee_axpro_cypress_fx2.jpg "Ht Usbee Axpro Cypress Fx2"){ .glightbox data-gallery="ht-usbee-axpro" }
<span class="caption">Ht Usbee Axpro Cypress Fx2</span>

[![24lc64](./img/24LC64.jpg)](./img/24LC64.jpg "24lc64"){ .glightbox data-gallery="ht-usbee-axpro" }
<span class="caption">24lc64</span>

[![Ht Usbee Axpro Pcb Bottom](./img/Ht_usbee_axpro_pcb_bottom.jpg)](./img/Ht_usbee_axpro_pcb_bottom.jpg "Ht Usbee Axpro Pcb Bottom"){ .glightbox data-gallery="ht-usbee-axpro" }
<span class="caption">Ht Usbee Axpro Pcb Bottom</span>

[![Ht Usbee Device](./img/Ht-usbee_device.jpg)](./img/Ht-usbee_device.jpg "Ht Usbee Device"){ .glightbox data-gallery="ht-usbee-axpro" }
<span class="caption">Ht Usbee Device</span>

[![Ht Usbee Axpro V5 St Stm8s003f3](./img/Ht_usbee_axpro_v5_st_stm8s003f3.jpg)](./img/Ht_usbee_axpro_v5_st_stm8s003f3.jpg "Ht Usbee Axpro V5 St Stm8s003f3"){ .glightbox data-gallery="ht-usbee-axpro" }
<span class="caption">Ht Usbee Axpro V5 St Stm8s003f3</span>

[![Ht Usbee Axpro V5 Ti Tlc5510i](./img/Ht_usbee_axpro_v5_ti_tlc5510i.jpg)](./img/Ht_usbee_axpro_v5_ti_tlc5510i.jpg "Ht Usbee Axpro V5 Ti Tlc5510i"){ .glightbox data-gallery="ht-usbee-axpro" }
<span class="caption">Ht Usbee Axpro V5 Ti Tlc5510i</span>

[![Expansion Board](./img/Expansion_board.jpg)](./img/Expansion_board.jpg "Expansion Board"){ .glightbox data-gallery="ht-usbee-axpro" }
<span class="caption">Expansion Board</span>

[![Ht Usbee Axpro No Siggen Case](./img/Ht-usbee-axpro_no_siggen_case.jpg)](./img/Ht-usbee-axpro_no_siggen_case.jpg "Ht Usbee Axpro No Siggen Case"){ .glightbox data-gallery="ht-usbee-axpro" }
<span class="caption">Ht Usbee Axpro No Siggen Case</span>

[![Ht Usbee Axpro V5 Microchip 24lc02bi](./img/Ht_usbee_axpro_v5_microchip_24lc02bi.jpg)](./img/Ht_usbee_axpro_v5_microchip_24lc02bi.jpg "Ht Usbee Axpro V5 Microchip 24lc02bi"){ .glightbox data-gallery="ht-usbee-axpro" }
<span class="caption">Ht Usbee Axpro V5 Microchip 24lc02bi</span>

[![Probe Adaptor](./img/Probe_adaptor.jpg)](./img/Probe_adaptor.jpg "Probe Adaptor"){ .glightbox data-gallery="ht-usbee-axpro" }
<span class="caption">Probe Adaptor</span>

[![Ht Usbee Axpro V5 Analog Connector Bottom](./img/Ht_usbee_axpro_v5_analog_connector_bottom.jpg)](./img/Ht_usbee_axpro_v5_analog_connector_bottom.jpg "Ht Usbee Axpro V5 Analog Connector Bottom"){ .glightbox data-gallery="ht-usbee-axpro" }
<span class="caption">Ht Usbee Axpro V5 Analog Connector Bottom</span>

[![Tlc5510i](./img/TLC5510I.jpg)](./img/TLC5510I.jpg "Tlc5510i"){ .glightbox data-gallery="ht-usbee-axpro" }
<span class="caption">Tlc5510i</span>

[![Fx2](./img/FX2.jpg)](./img/FX2.jpg "Fx2"){ .glightbox data-gallery="ht-usbee-axpro" }
<span class="caption">Fx2</span>

[![Ht Usbee Axpro Intersil Icl7660s](./img/Ht_usbee_axpro_intersil_icl7660s.jpg)](./img/Ht_usbee_axpro_intersil_icl7660s.jpg "Ht Usbee Axpro Intersil Icl7660s"){ .glightbox data-gallery="ht-usbee-axpro" }
<span class="caption">Ht Usbee Axpro Intersil Icl7660s</span>

[![Ht Usbee Axpro V5 Button Conn](./img/Ht_usbee_axpro_v5_button_conn.jpg)](./img/Ht_usbee_axpro_v5_button_conn.jpg "Ht Usbee Axpro V5 Button Conn"){ .glightbox data-gallery="ht-usbee-axpro" }
<span class="caption">Ht Usbee Axpro V5 Button Conn</span>

[![Ht Usbee Axpro V5 Device Top](./img/Ht_usbee_axpro_v5_device_top.jpg)](./img/Ht_usbee_axpro_v5_device_top.jpg "Ht Usbee Axpro V5 Device Top"){ .glightbox data-gallery="ht-usbee-axpro" }
<span class="caption">Ht Usbee Axpro V5 Device Top</span>

[![Ht Usbee Axpro Pcb Top](./img/Ht_usbee_axpro_pcb_top.jpg)](./img/Ht_usbee_axpro_pcb_top.jpg "Ht Usbee Axpro Pcb Top"){ .glightbox data-gallery="ht-usbee-axpro" }
<span class="caption">Ht Usbee Axpro Pcb Top</span>

[![Ht Usbee Axpro V5 Pcb Top](./img/Ht_usbee_axpro_v5_pcb_top.jpg)](./img/Ht_usbee_axpro_v5_pcb_top.jpg "Ht Usbee Axpro V5 Pcb Top"){ .glightbox data-gallery="ht-usbee-axpro" }
<span class="caption">Ht Usbee Axpro V5 Pcb Top</span>

[![Stm8 1](./img/STM8_1.jpg)](./img/STM8_1.jpg "Stm8 1"){ .glightbox data-gallery="ht-usbee-axpro" }
<span class="caption">Stm8 1</span>

[![Ht Usbee Axpro Analog Adapter Top](./img/Ht_usbee_axpro_analog_adapter_top.jpg)](./img/Ht_usbee_axpro_analog_adapter_top.jpg "Ht Usbee Axpro Analog Adapter Top"){ .glightbox data-gallery="ht-usbee-axpro" }
<span class="caption">Ht Usbee Axpro Analog Adapter Top</span>

[![Ht Usbee Axpro Device Bottom](./img/Ht_usbee_axpro_device_bottom.jpg)](./img/Ht_usbee_axpro_device_bottom.jpg "Ht Usbee Axpro Device Bottom"){ .glightbox data-gallery="ht-usbee-axpro" }
<span class="caption">Ht Usbee Axpro Device Bottom</span>

[![Ht Usbee Axpro Package Contents](./img/Ht_usbee_axpro_package_contents.jpg)](./img/Ht_usbee_axpro_package_contents.jpg "Ht Usbee Axpro Package Contents"){ .glightbox data-gallery="ht-usbee-axpro" }
<span class="caption">Ht Usbee Axpro Package Contents</span>

[![Ht Usbee Pcb](./img/Ht-usbee_pcb.jpg)](./img/Ht-usbee_pcb.jpg "Ht Usbee Pcb"){ .glightbox data-gallery="ht-usbee-axpro" }
<span class="caption">Ht Usbee Pcb</span>

[![Ht Usbee Axpro V5 Microchip 24lc64i](./img/Ht_usbee_axpro_v5_microchip_24lc64i.jpg)](./img/Ht_usbee_axpro_v5_microchip_24lc64i.jpg "Ht Usbee Axpro V5 Microchip 24lc64i"){ .glightbox data-gallery="ht-usbee-axpro" }
<span class="caption">Ht Usbee Axpro V5 Microchip 24lc64i</span>

[![Ht Usbee Axpro No Siggen Pcb](./img/Ht-usbee-axpro_no_siggen_pcb.jpg)](./img/Ht-usbee-axpro_no_siggen_pcb.jpg "Ht Usbee Axpro No Siggen Pcb"){ .glightbox data-gallery="ht-usbee-axpro" }
<span class="caption">Ht Usbee Axpro No Siggen Pcb</span>

[![Ht Usbee Pcb Front](./img/Ht-usbee_pcb_front.jpg)](./img/Ht-usbee_pcb_front.jpg "Ht Usbee Pcb Front"){ .glightbox data-gallery="ht-usbee-axpro" }
<span class="caption">Ht Usbee Pcb Front</span>

[![Ht Usbee Axpro Device Top](./img/Ht_usbee_axpro_device_top.jpg)](./img/Ht_usbee_axpro_device_top.jpg "Ht Usbee Axpro Device Top"){ .glightbox data-gallery="ht-usbee-axpro" }
<span class="caption">Ht Usbee Axpro Device Top</span>

[![Ht Usbee Axpro Ams1117 3.3](./img/Ht_usbee_axpro_ams1117-3.3.jpg)](./img/Ht_usbee_axpro_ams1117-3.3.jpg "Ht Usbee Axpro Ams1117 3.3"){ .glightbox data-gallery="ht-usbee-axpro" }
<span class="caption">Ht Usbee Axpro Ams1117 3.3</span>

[![Ams1117](./img/AMS1117.jpg)](./img/AMS1117.jpg "Ams1117"){ .glightbox data-gallery="ht-usbee-axpro" }
<span class="caption">Ams1117</span>

[![Ht Usbee Case Front](./img/Ht-usbee_case_front.jpg)](./img/Ht-usbee_case_front.jpg "Ht Usbee Case Front"){ .glightbox data-gallery="ht-usbee-axpro" }
<span class="caption">Ht Usbee Case Front</span>

[![Ht Usbee Axpro Analog Adapter Bottom](./img/Ht_usbee_axpro_analog_adapter_bottom.jpg)](./img/Ht_usbee_axpro_analog_adapter_bottom.jpg "Ht Usbee Axpro Analog Adapter Bottom"){ .glightbox data-gallery="ht-usbee-axpro" }
<span class="caption">Ht Usbee Axpro Analog Adapter Bottom</span>

[![Pcb3](./img/PCB3.jpg)](./img/PCB3.jpg "Pcb3"){ .glightbox data-gallery="ht-usbee-axpro" }
<span class="caption">Pcb3</span>

[![Ht Usbee Axpro Microchip 24lc02b](./img/Ht_usbee_axpro_microchip_24lc02b.jpg)](./img/Ht_usbee_axpro_microchip_24lc02b.jpg "Ht Usbee Axpro Microchip 24lc02b"){ .glightbox data-gallery="ht-usbee-axpro" }
<span class="caption">Ht Usbee Axpro Microchip 24lc02b</span>

[![Ht Usbee Axpro Usb](./img/Ht_usbee_axpro_usb.jpg)](./img/Ht_usbee_axpro_usb.jpg "Ht Usbee Axpro Usb"){ .glightbox data-gallery="ht-usbee-axpro" }
<span class="caption">Ht Usbee Axpro Usb</span>

[![Ht Usbee Axpro Tlc5510i](./img/Ht_usbee_axpro_tlc5510i.jpg)](./img/Ht_usbee_axpro_tlc5510i.jpg "Ht Usbee Axpro Tlc5510i"){ .glightbox data-gallery="ht-usbee-axpro" }
<span class="caption">Ht Usbee Axpro Tlc5510i</span>

[![Ht Usbee Axpro Hra](./img/Ht_usbee_axpro_hra.jpg)](./img/Ht_usbee_axpro_hra.jpg "Ht Usbee Axpro Hra"){ .glightbox data-gallery="ht-usbee-axpro" }
<span class="caption">Ht Usbee Axpro Hra</span>

[![Sm8 2](./img/SM8_2.jpg)](./img/SM8_2.jpg "Sm8 2"){ .glightbox data-gallery="ht-usbee-axpro" }
<span class="caption">Sm8 2</span>

[![24lc02b](./img/24LC02B.jpg)](./img/24LC02B.jpg "24lc02b"){ .glightbox data-gallery="ht-usbee-axpro" }
<span class="caption">24lc02b</span>

[![Ht Usbee Axpro V5 Cypress Fx2](./img/Ht_usbee_axpro_v5_cypress_fx2.jpg)](./img/Ht_usbee_axpro_v5_cypress_fx2.jpg "Ht Usbee Axpro V5 Cypress Fx2"){ .glightbox data-gallery="ht-usbee-axpro" }
<span class="caption">Ht Usbee Axpro V5 Cypress Fx2</span>

[![Ht Usbee Axpro V5 Analog Connector Top](./img/Ht_usbee_axpro_v5_analog_connector_top.jpg)](./img/Ht_usbee_axpro_v5_analog_connector_top.jpg "Ht Usbee Axpro V5 Analog Connector Top"){ .glightbox data-gallery="ht-usbee-axpro" }
<span class="caption">Ht Usbee Axpro V5 Analog Connector Top</span>

[![Ht Usbee Axpro V5 Connector](./img/Ht_usbee_axpro_v5_connector.jpg)](./img/Ht_usbee_axpro_v5_connector.jpg "Ht Usbee Axpro V5 Connector"){ .glightbox data-gallery="ht-usbee-axpro" }
<span class="caption">Ht Usbee Axpro V5 Connector</span>

[![Ht Usbee Axpro V5 Package Contents](./img/Ht_usbee_axpro_v5_package_contents.jpg)](./img/Ht_usbee_axpro_v5_package_contents.jpg "Ht Usbee Axpro V5 Package Contents"){ .glightbox data-gallery="ht-usbee-axpro" }
<span class="caption">Ht Usbee Axpro V5 Package Contents</span>

</div>
## Protocol

Since we use the open-source [fx2lafw](https://sigrok.org/wiki/Fx2lafw) firmware for this device, we don't need to know the protocol.

## Resources
- [epanorama.net: HT-USBee AxPro review](http://www.epanorama.net/newepa/2014/06/17/ht-usbee-axpro-review/)
- [Itead: Saleae8 / USBEE AX PRO / Altera Combination: Logic Analyzer](https://www.itead.cc/saleae8-usbee-ax-pro-altera-combination-logic-analyzer.html)

