# Instrustar Isds205X
| | | |:--------------------|-----------------------------------------------------------------------------------------------------------------------------| | Status | planned | | Channels | 2 | | Samplerate | 48MHz | | Analog bandwidth | 20MHz | | Vertical resolution | 8bit | | Triggers | none (SW-only) | | Input impedance | 1MΩ‖25pF | | Memory | none | | Display | none | | Connectivity | USB | | Website | [instrustar.com](http://english.instrustar.com/product_detail.asp?nid=1556) | **Instrustar ISDS205X** The **Instrustar ISDS205X** is a USB-based \- 2-channel oscilloscope with an analog bandwidth of 20MS/s and 48MS/s sampling rate, \- 2-channel "data recorder" (same as oscilloscope, simply storing the analog data), \- 2-channel spectrum analyzer with an analog bandwidth of 20MS/s, \- 1-channel DDS signal generator (sine, square, triangle, up sawtooth, down sawtooth); sine up to 20MHz, rest up to 2MHz, \- 8/16-channel logic analyzer with a max. sampling rate of 24MHz. See *Instrustar ISDS205X/Info* for more details (such as **lsusb -v** output) on the device. ## Hardware **Cypress FX2 pinout:**  | | | | | | |--------------------------------------------------------------------------:|----:|-----|------|-------------------------------------------------------------| | PD5 | 1- | O | -100 | | | PD6 | 2- | | -99 | | | PD7 | 3- | | -98 | | | GND | 4- | | -97 | | | CLKOUT | 5- | | -96 | | | VCC | 6- | | -95 | | | GND | 7- | | -94 | | | RDY0/\\*SLRD | 8- | | -93 | | | RDY1/\\*SLWR | 9- | | -92 | | | AVCC | 10- | | -91 | | | (24MHz crystal) XTALOUT | 11- | | -90 | | | (24MHz crystal) XTALIN | 12- | | -89 | | | AGND | 13- | | -88 | | | AVCC | 14- | | -87 | | | (USB D+) DPLUS | 15- | | -86 | | | (USB D-) DMINUS | 16- | | -85 | | | AGND | 17- | | -84 | | | VCC | 18- | | -83 | | | GND | 19- | | -82 | | | (CTL0, AD9288 ENCA/B) \\*IFCLK | 20- | | -81 | | | RESERVED | 21- | | -80 | | | (EEPROM SCL) SCL | 22- | | -79 | | | (EEPROM SDA) SDA | 23- | | -78 | | | VCC | 24- | | -77 | | | PB0 | 25- | | -76 | | | PB1 | 26- | | -75 | | | PB2 | 27- | | -74 | | | PB3 | 28- | | -73 | | | PB4 | 29- | | -72 | | | PB5 | 30- | | -71 | | | PB6 | 31- | | -70 | | | PB7 | 32- | | -69 | | | GND | 33- | | -68 | | | VCC | 34- | | -67 | | | GND | 35- | | -66 | | | CTL0 (IFCLK, AD9288 ENCA/B) | 36- | | -65 | | | CTL1 | 37- | | -64 | PC7 | | CTL2 | 38- | | -63 | PC6 | | VCC | 39- | | -62 | PC5 | | PA0 (74HC595D, DS) | 40- | | -61 | PC4 | | PA1 (74HC595D, STCP) | 41- | | -60 | PC3 | | PA2 (74HC595D, SHCP) | 42- | | -59 | PC2 | | PA3 (SHCP, Frequency Generator) | 43- | | -58 | PC1 | | PA4 (DS, Frequency Generator) | 44- | | -57 | PC0 (Used as input, unknown) | | PA5 (STCP, Frequency Generator) | 45- | | -56 | PD4 | | PA6 (1kHz scope cal pin) | 46- | | -55 | PD3 | | PA7 (activate analog mode vs digital mode) | 47- | | -54 | PD2 | | GND | 48- | | -53 | PD1 | | RESET# | 49- | | -52 | PD0 | | VCC | 50- | | -51 | \\*WAKEUP |  **NXP 74HC595D pinout**:  | | | | | | |-------------------------------------------------------------:|----:|-----|-----|-----------------------------------------------------------| | (upper 74HC4051D, S0) Q1 | 1- | O | -16 | VCC | | (lower 74HC4051D, S0) Q2 | 2- | | -15 | Q0 (upper 74HC4051D, S1) | | (lower 74HC4051D, S1) Q3 | 3- | | -14 | DS (FX2 PA0) | | Q4 | 4- | | -13 | OE# (GND) | | Q5 | 5- | | -12 | STCP (FX2 PA1) | | Q6 | 6- | | -11 | SHCP (FX2 PA2) | | Q7 | 7- | | -10 | MR# (VCC) | | GND | 8- | | -9 | Q7S |  **NXP 74HC4051D (upper/lower, CH1/CH2) pinout**:  | Y4 | 1- |  O | -16 | VCC
---|---|---|---|---
Y6 | 2- | -15 | Y2
Z | 3- | -14 | Y1
Y7 | 4- | -13 | Y0
Y5 | 5- | -12 | Y3
(GND) E# | 6- | -11 | S0 (NXP 74HC595D, Q1)
VEE | 7- | -10 | S1 (NXP 74HC595D, Q0)
GND | 8- | -9 | S2 (GND)
| Y4 | 1- |  O | -16 | VCC
---|---|---|---|---
Y6 | 2- | -15 | Y2
Z | 3- | -14 | Y1
Y7 | 4- | -13 | Y0
Y5 | 5- | -12 | Y3
(GND) E# | 6- | -11 | S0 (NXP 74HC595D, Q1)
VEE | 7- | -10 | S1 (NXP 74HC595D, Q0)
GND | 8- | -9 | S2 (GND)
**Microchip 24LC02B (top / bottom) pinout**:  | (VCC) A0 | 1- |  O | -8 | VCC
---|---|---|---|---
(GND) A1 | 2- | -7 | WP (GND)
(GND) A2 | 3- | -6 | SCL (FX2 SCL)
VSS | 4- | -5 | SDA (FX2 SDA or NC)
## Photos ## Resources \- [User guide](http://english.instrustar.com/upload/user%20guide/ISDS205%20User%20Guide.pdf)
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=Instrustar_ISDS205X&oldid=14018](https://OpenTraceLab.org/w/index.php?title=Instrustar_ISDS205X&oldid=14018)"
: \- *Device* \- *Oscilloscope* \- *Logic analyzer* \- *Signal generator* \- *Planned*
## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
