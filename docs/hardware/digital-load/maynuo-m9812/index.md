---
title: Maynuo M9812
---

# Maynuo M9812

<div class="infobox" markdown>

![Maynuo M9812](./img/Maynuo_m9812_mugshot.png){ .infobox-image }

### Maynuo M9812

| | |
|---|---|
| **Status** | supported |
| **Source code** | [maynuo-m97](https://github.com/OpenTraceLab/OpenTraceCapture/tree/main/src/hardware/maynuo-m97) |
| **Channels** | 1 |
| **Voltage/current (CH1)** | 300W / 0-30A / 0-150V |
| **Connectivity** | RS232 |
| **Features** | DC electronic load only |
| **Website** | [maynuo.com](http://www.maynuo.com/english/pro.asp?tid=98) |

</div>

The **Maynuo M9812** is a programmable DC electronic load (300W 0~30A 0~150V) with serial connectivity (Modbus RTU).

See [Maynuo M97 series](https://sigrok.org/wiki/Maynuo_M97_series) for information common to all devices in this series.

## Hardware

Digital control:

- **8-bit MCU with 64 KBytes Flash**: [Silicon Labs C8051F340](http://www.silabs.com/products/mcu/8-bit/c8051f32x-f34x/Pages/c8051f32x-f34x.aspx) ([datasheet](http://www.silabs.com/Support%20Documents/TechnicalDocs/C8051F34x.pdf))
- **64 Kbits I²C serial EEPROM**: [Microchip 24LC64](http://www.microchip.com/wwwproducts/Devices.aspx?dDocName=en010831) ([datasheet](http://ww1.microchip.com/downloads/en/DeviceDoc/21189T.pdf))

Precision analog:

- **16 bits ADC**: [TI ADS8327](http://www.ti.com/product/ads8327) ([datasheet](http://www.ti.com/lit/ds/symlink/ads8327.pdf))
- **16 bits DAC**: [BB DAC8831](http://www.ti.com/product/dac8831) ([datasheet](http://www.ti.com/lit/ds/symlink/dac8831.pdf))
- **Precision voltage reference (2.5 V)**: [TI REF5025](http://www.ti.com/product/ref5025) ([datasheet](http://www.ti.com/lit/ds/symlink/ref5025.pdf))
- **Ultralow Offset Voltage Operational Amplifier**: 4x [OP07](http://www.analog.com/en/products/amplifiers/operational-amplifiers/high-voltage-amplifiers-greaterthanequalto-12v/op07.html) ([datasheet](http://www.analog.com/media/en/technical-documentation/data-sheets/OP07.pdf))
- **Low Noise, Precision Operational Amplifier**: 5x [OP27](http://www.analog.com/en/products/amplifiers/operational-amplifiers/high-voltage-amplifiers-greaterthanequalto-12v/op27.html) ([datasheet](http://www.analog.com/media/en/technical-documentation/data-sheets/OP27.pdf))

Output stage:

- **Power MOSFET**: 8x [IRFP250N](http://www.irf.com/part/_/A~IRFP250N) ([datasheet](http://www.irf.com/product-info/datasheets/data/irfp250n.pdf))
- **General purpose JFET quad operational amplifiers**: 2x [ST TL084](http://www.st.com/web/catalog/sense_power/FM123/SC61/SS1378/PF65359) ([datasheet](http://www.st.com/web/en/resource/technical/document/datasheet/CD00000493.pdf))
- **General purpose JFET dual operational amplifiers**: [ST TL082](http://www.st.com/web/en/catalog/sense_power/FM1965/SC1942/PF65358) ([datasheet](http://www.st.com/st-web-ui/static/active/en/resource/technical/document/datasheet/CD00000492.pdf))

Temperature control:

- **NPN Transistor**: [TIP41C](https://www.fairchildsemi.com/products/discretes/bipolar-transistors/high-power-bjts/TIP41C.html) ([datasheet](https://www.fairchildsemi.com/datasheets/TI/TIP41C.pdf))
- **Quadruple Operational Amplifiers**: [LM324](http://www.ti.com/product/lm324) ([datasheet](http://www.ti.com/lit/ds/symlink/lm324.pdf))

Power supply:

- **5 V Regulator**: [MC7805](http://www.onsemi.com/PowerSolutions/product.do?id=MC7805) ([datasheet](http://www.onsemi.com/pub_link/Collateral/MC7800-D.PDF))
- **12 V Regulator**: [MC7812](http://www.onsemi.com/PowerSolutions/product.do?id=MC7812) ([datasheet](http://www.onsemi.com/pub_link/Collateral/MC7800-D.PDF))
- **-12 V Regulator**: [MC7912](http://www.onsemi.com/PowerSolutions/product.do?id=MC7912) ([datasheet](http://www.onsemi.com/pub_link/Collateral/MC7800-D.PDF))

Miscelaneous:

- **Dual 4-input NAND gate**: [NXP 74HC20D](http://www.nxp.com/products/logic/gates/nand_gates/74HC20D.html) ([datasheet](http://www.nxp.com/documents/data_sheet/74HC_HCT20.pdf))
- **Power MOSFET**: [IRF540](http://www.irf.com/part/_/A~IRF540N) ([datasheet](http://www.irf.com/product-info/datasheets/data/irf540npbf.pdf))

VFD controller + panel:

- **VFD driver**: [Princeton Technology Corp. PT6314](http://www.princeton.com.tw/en-us/products/displaydriveric/charactervfddrivercontrolleric.aspx) ([datasheet](http://www.princeton.com.tw/Portals/0/Product/PT6314.pdf))
- **8-Bit Serial-In, Parallel-Out Shift Register**: [Faichild 74VHC164](https://www.fairchildsemi.com/products/logic/flip-flops-latches-registers/registers/74VHC164.html) ([datasheet](https://www.fairchildsemi.com/datasheets/74/74VHC164.pdf))
- **Dual Amplifiers Operational**: [TI LM358](http://www.ti.com/product/LM358) ([datasheet](http://www.ti.com/lit/ds/symlink/lm358.pdf))

## Photos

<div class="photo-grid" markdown>

[![Maynuo M9812 Mugshot](./img/Maynuo_m9812_mugshot.png)](./img/Maynuo_m9812_mugshot.png "Maynuo M9812 Mugshot"){ .glightbox data-gallery="maynuo-m9812" }
<span class="caption">Maynuo M9812 Mugshot</span>

</div>
## Resources
- [Manual (including protocol)](http://www.maynuo.com/downloadfile/2009102937213561.pdf)

