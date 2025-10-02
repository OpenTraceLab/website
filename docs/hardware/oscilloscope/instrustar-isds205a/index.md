---
title: Instrustar_ISDS205A
---

# Instrustar_ISDS205A

<div class="infobox" markdown>

![Instrustar_ISDS205A](./img/Instrustar-IDS205A_PCBback.jpg){ .infobox-image }

### Instrustar_ISDS205A

| | |
|---|---|
| **Status** | in progress |
| **Channels** | 2 |
| **Samplerate** | 48MHz |
| **Analog bandwidth** | 20MHz |
| **Vertical resolution** | 8bit |
| **Triggers** | none (SW-only) |
| **Input impedance** | 1MΩ‖25pF |
| **Memory** | none |
| **Display** | none |
| **Connectivity** | USB |
| **Website** | [instrustar.com](http://english.instrustar.com/product_detail.asp?nid=1556) |

</div>

The **Instrustar ISDS205A** is a USB-based, 2-channel oscilloscope with an analog bandwidth of 20MS/s and 48MS/s sampling rate.
Compared to products similar for boxing and price level it could be considered an enhanced version of FX2 oscilloscope, not in the boxing which appear to use worse materials, but in the hardware which allow a wider input range (from 0.09mVp to 6Vp) and an hardware AC/DC selector.

See [Instrustar ISDS205A/Info](https://sigrok.org/wiki/Instrustar_ISDS205A/Info) for more details (such as **lsusb -v** output) on the device. 

## Hardware
- Cypress FX2LP CY7C68013AC (USB 2.0 HS controller)
- Analog Devices AD9288 (ADC)
- Microchip 24LC64I (64K I²C EEPROM)
- (2)NXP 74HC4051 (8-Channel Analog Mux)
- NXP 74HC595D (8bit Shift Register (Serial-in to Serial or Parallel-out))  ([datasheet](https://assets.nexperia.com/documents/data_sheet/74HC_HCT595.pdf))
- Oscillator GZX24.000 (24MHz crystal)
- (4) Huike (Shenzhen) HK23F-DC5V-SHG (Reed switch)

**Cypress FX2 pinout:**

| PD5 | 1- | &#160;&#160;O | -56 | PD4 |
|---|---|---|---|---|
| PD6 | 2- | -55 | PD3 |
| PD7 | 3- | -54 | PD2 |
| GND | 4- | -53 | PD1 |
| CLKOUT | 5- | -52 | PD0 |
| VCC | 6- | -51 | *WAKEUP |
| GND | 7- | -50 | VCC |
| RDY0/*SLRD | 8- | -49 | RESET# |
| RDY1/*SLWR | 9- | -48 | GND |
| AVCC | 10- | -47 | PA7 |
| (24MHz crystal) XTALOUT | 11- | -46 | PA6 (74HC595D, SHCP) |
| (24MHz crystal) XTALIN | 12- | -45 | PA5 (74HC595D, STCP) |
| AGND | 13- | -44 | PA4 (74HC595D, DS) |
| AVCC | 14- | -43 | PA3 |
| (USB D+) DPLUS | 15- | -42 | PA2 |
| (USB D-) DMINUS | 16- | -41 | PA1 |
| AGND | 17- | -40 | PA0 (1kHz scope cal pin) |
| VCC | 18- | -39 | VCC |
| GND | 19- | -38 | CTL2 |
| (CTL0, AD9288 ENCA/B) *IFCLK | 20- | -37 | CTL1 |
| RESERVED | 21- | -36 | CTL0 (IFCLK, AD9288 ENCA/B) |
| (EEPROM SCL) SCL | 22- | -35 | GND |
| (EEPROM SDA) SDA | 23- | -34 | VCC |
| VCC | 24- | -33 | GND |
| PB0 | 25- | -32 | PB7 |
| PB1 | 26- | -31 | PB6 |
| PB2 | 27- | -30 | PB5 |
| PB3 | 28- | -29 | PB4 |

**NXP 74HC595D pinout**:

| (upper 74HC4051D, S0) Q1 | 1- | &#160;&#160;O | -16 | VCC |
|---|---|---|---|---|
| (lower 74HC4051D, S0) Q2 | 2- | -15 | Q0 (upper 74HC4051D, S1) |
| (lower 74HC4051D, S1) Q3 | 3- | -14 | DS (FX2 PA4) |
| CH2 low voltage relay Q4 | 4- | -13 | OE# (GND) |
| CH2 AC/DC relay Q5 | 5- | -12 | STCP (FX2 PA5) |
| CH1 low voltage relay Q6 | 6- | -11 | SHCP (FX2 PA6) |
| CH1 AC/DC relay Q7 | 7- | -10 | MR# (VCC) |
| GND | 8- | -9 | Q7S |

**NXP 74HC4051D (upper/lower, CH1/CH2) pinout**:

| Y4 | 1- | &#160;&#160;O | -16 | VCC |
|---|---|---|---|---|
| Y6 | 2- | -15 | Y2 |
| Z | 3- | -14 | Y1 |
| Y7 | 4- | -13 | Y0 |
| Y5 | 5- | -12 | Y3 |
| (GND) E# | 6- | -11 | S0 (NXP 74HC595D, Q1) |
| VEE | 7- | -10 | S1 (NXP 74HC595D, Q0) |
| GND | 8- | -9 | S2 (GND) |

| Y4 | 1- | &#160;&#160;O | -16 | VCC |
|---|---|---|---|---|
| Y6 | 2- | -15 | Y2 |
| Z | 3- | -14 | Y1 |
| Y7 | 4- | -13 | Y0 |
| Y5 | 5- | -12 | Y3 |
| (GND) E# | 6- | -11 | S0 (NXP 74HC595D, Q2) |
| VEE | 7- | -10 | S1 (NXP 74HC595D, Q3) |
| GND | 8- | -9 | S2 (GND) |

**Microchip 24LC64I pinout**:

| (VCC) A0 | 1- | &#160;&#160;O | -8 | VCC |
|---|---|---|---|---|
| (GND) A1 | 2- | -7 | WP (GND) |
| (GND) A2 | 3- | -6 | SCL (FX2 SCL) |
| VSS | 4- | -5 | SDA (FX2 SDA) |

**Analog Devices ADS9288 pinout**:

| AD9288 pins | Description |
|---|---|
| S1, S2 | S1=VCC, S2=GND. "Normal operation, data align disabled". |
| DFS | Tied to GND. Data format select = "offset binary" (not "twos complement"). |
| AINA, AINB | Analog input channels. |
| D0A-D7A | Connected to FX2 PB0-PB7. |
| D0B-D7B | Connected to FX2 PD0-PD7. |

## Firmware

**Note**: The firmware is flashed into the device permanently.

### EEPROM layout

The device has a 8KB I²C EEPROM with the following layout:

```
c2 47 05 31 21 00 00 04 XX XX XX XX XX XX .. ..

```

Description:

| Bytes | Description |
|---|---|
| 0 | **0xc2**: FX2 "c2 load" mode, i.e. VID/PID/DID are loaded from EEPROM as the firmware. |
| 1-2 | **0x0547**: USB vendor ID (VID before firmware renumerate). |
| 3-4 | **0x2131**: USB product ID (PID before firmware renumerate). |
| 5-6 | **0x0000**: USB device ID (DID  before firmware renumerate). |
| 7 | **0x04**: FX2 configuration byte (see FX2 TRM for details). |
| 8-1917h | Firmware. |
| 1918h -1fffh | All-0xff. |

## Photos

<div class="photo-grid" markdown>

[![Instrustar Ids205a Pcbback](./img/Instrustar-IDS205A_PCBback.jpg)](./img/Instrustar-IDS205A_PCBback.jpg "Instrustar Ids205a Pcbback"){ .glightbox data-gallery="instrustar_isds205a" }
<span class="caption">Instrustar Ids205a Pcbback</span>

[![Instrustar Ids205a Pcbfront](./img/Instrustar-IDS205A_PCBfront.jpg)](./img/Instrustar-IDS205A_PCBfront.jpg "Instrustar Ids205a Pcbfront"){ .glightbox data-gallery="instrustar_isds205a" }
<span class="caption">Instrustar Ids205a Pcbfront</span>

[![Instrustar Ids205a Ic2](./img/Instrustar-IDS205A_IC2.jpg)](./img/Instrustar-IDS205A_IC2.jpg "Instrustar Ids205a Ic2"){ .glightbox data-gallery="instrustar_isds205a" }
<span class="caption">Instrustar Ids205a Ic2</span>

[![Instrustar Ids205a Casefront](./img/Instrustar-IDS205A_CaseFront.jpg)](./img/Instrustar-IDS205A_CaseFront.jpg "Instrustar Ids205a Casefront"){ .glightbox data-gallery="instrustar_isds205a" }
<span class="caption">Instrustar Ids205a Casefront</span>

[![Instrustar Ids205a Ic3](./img/Instrustar-IDS205A_IC3.jpg)](./img/Instrustar-IDS205A_IC3.jpg "Instrustar Ids205a Ic3"){ .glightbox data-gallery="instrustar_isds205a" }
<span class="caption">Instrustar Ids205a Ic3</span>

[![Instrustar Ids205a Caseback](./img/Instrustar-IDS205A_CaseBack.jpg)](./img/Instrustar-IDS205A_CaseBack.jpg "Instrustar Ids205a Caseback"){ .glightbox data-gallery="instrustar_isds205a" }
<span class="caption">Instrustar Ids205a Caseback</span>

[![Instrustar Ids205a Ic1](./img/Instrustar-IDS205A_IC1.jpg)](./img/Instrustar-IDS205A_IC1.jpg "Instrustar Ids205a Ic1"){ .glightbox data-gallery="instrustar_isds205a" }
<span class="caption">Instrustar Ids205a Ic1</span>

</div>
## Resources
- [Aliexpress page](http://www.aliexpress.com/item/ISDS205A-Virtual-PC-USB-oscilloscope-2CH-20-MHz-48MSa-s-FFT-analyzer-Data-Logger/32374001270.html)
- [User Guide](http://instrustar.com/upload/user%20guide/ISDS205%20User%20Guide.pdf)
- [SDK 2.6](http://instrustar.com/instrustar_com/upload/software/SDK%202.6.zip)

