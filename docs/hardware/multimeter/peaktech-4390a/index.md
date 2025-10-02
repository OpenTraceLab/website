---
title: PeakTech 4390A
---

# PeakTech 4390A

<div class="infobox" markdown>

![PeakTech 4390A](./img/Peaktech_4390a_metex_m-3860m_mugshot.png){ .infobox-image }

### PeakTech 4390A

| | |
|---|---|
| **Status** | supported |
| **Source code** | [serial-dmm](https://github.com/OpenTraceLab/OpenTraceCapture/tree/main/src/hardware/serial-dmm) |
| **Counts** | 4000 |
| **IEC 61010-1** | — |
| **Connectivity** | RS232 |
| **Measurements** | voltage, current, frequency, hFE, logic, continuity, diode, resistance, temperature, capacitance, power |
| **Features** | true-rms, signal-out, 3 sub-displays, backlight, bargraph, auto hold, data hold, range hold, min/max, relative offset, comparision, 10 reading memory |

</div>

The **PeakTech 4390A** is a 4000 counts handheld digital multimeter with RS232 connectivity.

This is a rebadged [Metex M-3860M](https://web.archive.org/web/20090221062027/http://imetex.com:80/html/product/product_model_detail.asp?idx=27) multimeter.

**Note:** This is **not** the same device as the [PeakTech 4390](https://sigrok.org/wiki/PeakTech_4390), despite the very similar name.

## Hardware

**Main ICs**:

- **Multimeter IC**: Metex 00M38M03 (markings: METEX / 00M38M03 / 663 / 0411KK002)
- **A/D Converter**: [Maxim MAX134 3 3/4 Digit DMM Circuit](https://www.maximintegrated.com/en/products/analog/data-converters/analog-to-digital-converters/MAX134.html) ([datasheet](https://datasheets.maximintegrated.com/en/ds/MAX133-MAX134.pdf))
- **True RMS Converter**: [Analog Devices AD737](http://www.analog.com/en/products/linear-products/rms-to-dc-converters/ad737.html) ([datasheet](http://www.analog.com/media/en/technical-documentation/data-sheets/AD737.pdf))
- **Power Metering IC**: [Sames SA9102CSA](http://www.sames.co.za/energy-metering-legacy/) ([datasheet](http://www.sames.co.za/wp-content/uploads/pdf/legacy/SA9102C.pdf))
- **Voltage Reference 1.2V**: ICL8069 ([datasheet](https://www.intersil.com/content/dam/Intersil/documents/icl8/icl8069.pdf)) (markings: CC / 8069 / G301AC)
- **LCD Controller**: Epson S1D12708F00A1 (markings: EPSON JAPAN / S1D12708F00A1 / F04202336)

**Miscellaneous ICs**:

- **Serial EEPROM**: Atmel AT93C46 ([datasheet](http://www.atmel.com/Images/doc5140.pdf)) (markings: ATMEL 348 / 93C46)
- **Optocoupler for RS232**: 2x [Lite-On 817B](http://optoelectronics.liteon.com/en-global/Led/LED-Component/Detail/651/0/LTV-817%20Series) ([datasheet](http://optoelectronics.liteon.com/upload/download/DS-70-96-0013/LTV-8X4%20series%20201509.pdf)) (markings: L0419 / 817B / Y)
- **OpAmp**: 2x 2904 ([datasheet](http://www.njr.com/semicon/PDF/NJM2904_E.pdf)) (markings: 2904 / 4169B / JRC)
- **Low Offset Voltage OpAmp**: OP-07 ([datasheet](http://www.njr.com/semicon/PDF/NJMOP-07_E.pdf)) (markings: OP-07 / 4051B / JRC)
- **OpAmp**: NJM062/TL062 ([datasheet](http://www.njr.com/semicon/PDF/NJM062_NJM064_E.pdf)) (markings: 062 / 3138B / JRC)
- **Quad 2-Input NAND Gate**: ON Semi 74HC00A ([datasheet](https://www.onsemi.com/pub/Collateral/MC74HC00A-D.PDF)) (markings: HC00A / ON PBK340)
- **Quad Multiplexer**: ON Semi 14066B ([datasheet](https://www.onsemi.com/pub/Collateral/MC14066B-D.PDF)) (markings: 14066B / ON PPM426)
- **555 Timer**: Intersil ICM7555 ([datasheet](https://www.intersil.com/content/dam/Intersil/documents/icm7/icm7555-56.pdf)) (markings: i 7555 / IBA / L044FCL)
- **Quad 2-Input NAND Schmitt Trigger**: 74HC132D ([datasheet](https://assets.nexperia.com/documents/data-sheet/74HC_HCT132.pdf))
- **Dual Decade Ripple Counter**: 74HC390D ([datasheet](https://assets.nexperia.com/documents/data-sheet/74HC_HCT390.pdf))

**Fuses**:

- 250V, 15A (N65)
- 250V, 800mA

## Photos

<div class="photo-grid" markdown>

[![Peaktech 4390a Metex M 3860m Mugshot](./img/Peaktech_4390a_metex_m-3860m_mugshot.png)](./img/Peaktech_4390a_metex_m-3860m_mugshot.png "Peaktech 4390a Metex M 3860m Mugshot"){ .glightbox data-gallery="peaktech-4390a" }
<span class="caption">Peaktech 4390a Metex M 3860m Mugshot</span>

[![Peaktech 4390a Metex M 3860m Pcb Small Bottom](./img/Peaktech_4390A_Metex_M-3860M_-_PCB_Small_Bottom.jpg)](./img/Peaktech_4390A_Metex_M-3860M_-_PCB_Small_Bottom.jpg "Peaktech 4390a Metex M 3860m Pcb Small Bottom"){ .glightbox data-gallery="peaktech-4390a" }
<span class="caption">Peaktech 4390a Metex M 3860m Pcb Small Bottom</span>

[![Peaktech 4390a Metex M 3860m Pcb Bottom](./img/Peaktech_4390A_Metex_M-3860M_-_PCB_Bottom.jpg)](./img/Peaktech_4390A_Metex_M-3860M_-_PCB_Bottom.jpg "Peaktech 4390a Metex M 3860m Pcb Bottom"){ .glightbox data-gallery="peaktech-4390a" }
<span class="caption">Peaktech 4390a Metex M 3860m Pcb Bottom</span>

[![Peaktech 4390a Metex M 3860m Pcb Small Top](./img/Peaktech_4390A_Metex_M-3860M_-_PCB_Small_Top.jpg)](./img/Peaktech_4390A_Metex_M-3860M_-_PCB_Small_Top.jpg "Peaktech 4390a Metex M 3860m Pcb Small Top"){ .glightbox data-gallery="peaktech-4390a" }
<span class="caption">Peaktech 4390a Metex M 3860m Pcb Small Top</span>

[![Peaktech 4390a Metex M 3860m Power Adapter](./img/Peaktech_4390a_metex_m-3860m_power_adapter.jpg)](./img/Peaktech_4390a_metex_m-3860m_power_adapter.jpg "Peaktech 4390a Metex M 3860m Power Adapter"){ .glightbox data-gallery="peaktech-4390a" }
<span class="caption">Peaktech 4390a Metex M 3860m Power Adapter</span>

[![Peaktech 4390a Metex M 3860m Serial Cable](./img/Peaktech_4390A_Metex_M-3860M_-_Serial_Cable.jpg)](./img/Peaktech_4390A_Metex_M-3860M_-_Serial_Cable.jpg "Peaktech 4390a Metex M 3860m Serial Cable"){ .glightbox data-gallery="peaktech-4390a" }
<span class="caption">Peaktech 4390a Metex M 3860m Serial Cable</span>

[![Peaktech 4390a Metex M 3860m Pcb Top 2](./img/Peaktech_4390A_Metex_M-3860M_-_PCB_Top_2.jpg)](./img/Peaktech_4390A_Metex_M-3860M_-_PCB_Top_2.jpg "Peaktech 4390a Metex M 3860m Pcb Top 2"){ .glightbox data-gallery="peaktech-4390a" }
<span class="caption">Peaktech 4390a Metex M 3860m Pcb Top 2</span>

[![Peaktech 4390a Metex M 3860m Pcb Top 1](./img/Peaktech_4390A_Metex_M-3860M_-_PCB_Top_1.jpg)](./img/Peaktech_4390A_Metex_M-3860M_-_PCB_Top_1.jpg "Peaktech 4390a Metex M 3860m Pcb Top 1"){ .glightbox data-gallery="peaktech-4390a" }
<span class="caption">Peaktech 4390a Metex M 3860m Pcb Top 1</span>

[![Peaktech 4390a Metex M 3860m Pcb Big Top Detail](./img/Peaktech_4390A_Metex_M-3860M_-_PCB_Big_Top_Detail.jpg)](./img/Peaktech_4390A_Metex_M-3860M_-_PCB_Big_Top_Detail.jpg "Peaktech 4390a Metex M 3860m Pcb Big Top Detail"){ .glightbox data-gallery="peaktech-4390a" }
<span class="caption">Peaktech 4390a Metex M 3860m Pcb Big Top Detail</span>

[![Peaktech 4390a Metex M 3860m Bottom](./img/Peaktech_4390a_metex_m-3860m_bottom.jpg)](./img/Peaktech_4390a_metex_m-3860m_bottom.jpg "Peaktech 4390a Metex M 3860m Bottom"){ .glightbox data-gallery="peaktech-4390a" }
<span class="caption">Peaktech 4390a Metex M 3860m Bottom</span>

[![Peaktech 4390a Metex M 3860m Pcb Big Top Full](./img/Peaktech_4390A_Metex_M-3860M_-_PCB_Big_Top_Full.jpg)](./img/Peaktech_4390A_Metex_M-3860M_-_PCB_Big_Top_Full.jpg "Peaktech 4390a Metex M 3860m Pcb Big Top Full"){ .glightbox data-gallery="peaktech-4390a" }
<span class="caption">Peaktech 4390a Metex M 3860m Pcb Big Top Full</span>

[![Peaktech 4390a Metex M 3860m Top](./img/Peaktech_4390a_metex_m-3860m_top.jpg)](./img/Peaktech_4390a_metex_m-3860m_top.jpg "Peaktech 4390a Metex M 3860m Top"){ .glightbox data-gallery="peaktech-4390a" }
<span class="caption">Peaktech 4390a Metex M 3860m Top</span>

[![Peaktech 4390a Metex M 3860m Shielding](./img/Peaktech_4390A_Metex_M-3860M_-_Shielding.jpg)](./img/Peaktech_4390A_Metex_M-3860M_-_Shielding.jpg "Peaktech 4390a Metex M 3860m Shielding"){ .glightbox data-gallery="peaktech-4390a" }
<span class="caption">Peaktech 4390a Metex M 3860m Shielding</span>

</div>
## Protocol

See [Multimeter_ICs#Metex_14-byte_ASCII](https://sigrok.org/wiki/Multimeter_ICs#Metex_14-byte_ASCII).

The device sends 4 * 14 bytes. The first 14 bytes represents the main display and then the three sub displays from left to right (left, middle, right).

## Resources
- [Conrad: Metex M-3860M manual](http://www2.produktinfo.conrad.de/datenblaetter/100000-124999/121371-an-01-en-Digitalmultimeter_M_3860_M.pdf)

