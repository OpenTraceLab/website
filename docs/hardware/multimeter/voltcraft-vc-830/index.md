---
title: Voltcraft VC-830
---

# Voltcraft VC-830

<div class="infobox" markdown>

![Voltcraft VC-830](./img/Voltcraft_vc830_device_top.jpg){ .infobox-image }

### Voltcraft VC-830

| | |
|---|---|
| **Status** | supported |
| **Source code** | [serial-dmm](https://github.com/OpenTraceLab/OpenTraceCapture/tree/main/src/hardware/serial-dmm) |
| **Counts** | 6000 |
| **IEC 61010-1** | CAT III (1000V) / CAT IV (600V) |
| **Connectivity** | [RS232](https://sigrok.org/wiki/Device_cables#UNI-T_UT-D02) / [USB](https://sigrok.org/wiki/Device_cables#UNI-T_UT-D04) |
| **Measurements** | voltage, resistance, diode, continuity, capacitance, frequency, duty cycle, current |
| **Features** | autorange, hold, relative, test-lead-detection (TLD), backlight |
| **Website** | [conrad.de](http://www.conrad.de/ce/de/product/124601/VOLTCRAFT-VC830-Digital-Multimeter-m-Messleitungen-VC800-Serie-6000-Counts-CAT-IV-600-V) |

</div>

The **Voltcraft VC-830** is a 6000 counts, CAT III (1000V) / CAT IV (600V) handheld digital multimeter with RS232 or USB connectivity.

## Hardware

**Multimeter**:

- Fortune Semiconductor FS9922-DMM4
- ...

**RS232 cable:**

- See [Device cables#UNI-T_UT-D02](https://sigrok.org/wiki/Device_cables#UNI-T_UT-D02).

**USB cable:**

- See [Device cables#UNI-T_UT-D04](https://sigrok.org/wiki/Device_cables#UNI-T_UT-D04).

## Photos

<div class="photo-grid" markdown>

[![Voltcraft Vc830 Device Top](./img/Voltcraft_vc830_device_top.jpg)](./img/Voltcraft_vc830_device_top.jpg "Voltcraft Vc830 Device Top"){ .glightbox data-gallery="voltcraft-vc-830" }
<span class="caption">Voltcraft Vc830 Device Top</span>

[![Voltcraft Vc830](./img/Voltcraft_vc830.png)](./img/Voltcraft_vc830.png "Voltcraft Vc830"){ .glightbox data-gallery="voltcraft-vc-830" }
<span class="caption">Voltcraft Vc830</span>

[![Voltcraft Vc830 Battery](./img/Voltcraft_vc830_battery.jpg)](./img/Voltcraft_vc830_battery.jpg "Voltcraft Vc830 Battery"){ .glightbox data-gallery="voltcraft-vc-830" }
<span class="caption">Voltcraft Vc830 Battery</span>

[![Voltcraft Vc830 Ir](./img/Voltcraft_vc830_ir.jpg)](./img/Voltcraft_vc830_ir.jpg "Voltcraft Vc830 Ir"){ .glightbox data-gallery="voltcraft-vc-830" }
<span class="caption">Voltcraft Vc830 Ir</span>

[![Voltcraft Vc830 Lcd](./img/Voltcraft_vc830_lcd.jpg)](./img/Voltcraft_vc830_lcd.jpg "Voltcraft Vc830 Lcd"){ .glightbox data-gallery="voltcraft-vc-830" }
<span class="caption">Voltcraft Vc830 Lcd</span>

[![Voltcraft Vc830 Device Bottom](./img/Voltcraft_vc830_device_bottom.jpg)](./img/Voltcraft_vc830_device_bottom.jpg "Voltcraft Vc830 Device Bottom"){ .glightbox data-gallery="voltcraft-vc-830" }
<span class="caption">Voltcraft Vc830 Device Bottom</span>

</div>
## Protocol

See [Multimeter_ICs#Fortune_Semiconductor_FS9922-DMM4](https://sigrok.org/wiki/Multimeter_ICs#Fortune_Semiconductor_FS9922-DMM4).

A [short protocol description is also available from Voltcraft/Conrad](http://www.produktinfo.conrad.com/datenblaetter/100000-124999/124601-in-01-en-RS232_com_protocol_VC_850.pdf).

This DMM is wired up a bit differently than "normal" for the diode mode, see below. The **MEA5** to **MEA1** bits are inputs of the FS9922-DMM4 chip, controlled by the position of the mode selection wheel on the DMM.

| Mode (selection wheel) | MEA5 | MEA4 | MEA3 | MEA2 | MEA1 | Mode (FS9922-DMM4 datasheet) |
|---|---|---|---|---|---|---|
| Voltage AC | 1 | 0 | 1 | 1 | 0 | AC V (6.000V ~ 6000V) |
| Voltage DC | 1 | 1 | 0 | 1 | 0 | DC V (600.0mV ~ 6000V) |
| Capacitance | 1 | 0 | 0 | 1 | 1 | Capacitance |
| Resistance / continuity | 0 | 1 | 1 | 0 | 0 | Ohm / beeper |
| Diode | 0 | 1 | 1 | 0 | 1 | ADP (6.000) |
| Frequency / duty cycle | 1 | 0 | 1 | 0 | 0 | Hz / Duty |
| DC / AC current (µA) | 1 | 1 | 0 | 1 | 1 | DC / AC µA (600.0µA / 6000µA) |
| DC / AC current (mA) | 1 | 1 | 1 | 0 | 1 | DC / AC mA (60.00mA / 600.0mA) |
| DC / AC current (10A) | 1 | 1 | 1 | 1 | 0 | DC / AC A (6.000A / 60.00A) |

When the mode selection wheel is turned to "diode" setting, the FS9922-DMM4 chip will not be put into one of its known "diode" modes ("Diode/Beeper", "Ohm/Diode/Beeper/cap.", or "Ohm/Beeper/Diode") but instead it will use the "ADP (6.000)" setting. This will light up COM4/SEG22 on the LCD (which is a "diode" symbol on this DMM) and in the PC protocol the "z1" user-defined bit will be set (but **not** the "voltage" and/or "diode" bits, as one would expect). Thus, some [special handling](http://sigrok.org/gitweb/?p=libsigrok.git;a=commitdiff;h=e52bb9be8351b8c4f960d998a62dfbd05b8fa637) is needed in order to properly parse the diode mode setting.

See the [Fortune Semiconductor FS9922-DMM4](http://www.ic-fortune.com/upload/Download/FS9922-DMM4-DS-11_EN.pdf) datasheet page 11 ("Measuring Modes Select") and 12 ("ADP Input/User-Defined Symbols and Confirmation of Decimal Locations") for details.

## Resources
- [Manual](http://www.produktinfo.conrad.com/datenblaetter/100000-124999/124601-an-01-ml-VOLTCRAFT_VC830_DMM_de_en_fr_nl.pdf)
- [Vendor software](http://www.produktinfo.conrad.com/datenblaetter/100000-124999/124601-up-01-en-Win7_32_64_Bit_VC830_VC850_V4_2_6.zip)

