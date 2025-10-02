---
title: Arduino
---

# Arduino

<div class="infobox" markdown>

![Arduino](./img/Arduino_Uno-R3.jpg){ .infobox-image }

### Arduino

| | |
|---|---|
| **Status** | in progress |
| **Source code** | [ols](https://github.com/OpenTraceLab/OpenTraceCapture/tree/main/src/hardware/ols) |
| **Channels** | 6 |
| **Samplerate** | 4MHz |
| **Samplerate (state)** | — |
| **Triggers** | none (SW-only) |
| **Min/max voltage** | -0.5V — 5.5V |
| **Threshold voltage** | Fixed: VIH=3.0V—5V, VIL=0V—1.5V |
| **Memory** | ATmega168:  532 (or lower), ATmega328:  1024 (or lower), ATmega2560: 7168 (or lower) |
| **Compression** | RLE |
| **Price range** | $1 - $35 |
| **Website** | [github.com/gillham/logic_analyzer](https://github.com/gillham/logic_analyzer) |

</div>

**NOTE** The sigrok project does not support "the Arduino" as a specific device. Instead one of the Arduino sketches implements the [ SUMP protocol](https://sigrok.org/wiki/SUMP_compatibles) which allows to use the Arduino with the **ols** device driver. Which means that this page is about the **AGLA** project, not the Arduino.

## Older, mostly obsolete information below

SUMP protocol implementation for Arduino. Basic functionality is present, but we need someone to fix the details to make things nice and usefull.

**TODO**  (gsi) This page feels a little out of place. The sigrok project doesn't support "the Arduino" as a capture device. It's just that the AGLA project happens to implement the SUMP protocol on some Arduino board, which then makes it accessible to the OLS driver in a generic fashion. This page should reflect these facts, be renamed to AGLA, perhaps move to the SUMP section as yet another compatible.

## Hardware
- **Main chip**: Atmel ATmega168/328/2560
- **Input pins**: With optional internal pullups (currently has to be modified at compile-time)
- **Input protection**: While Arduino is relatively rugged device, keep in mind it relies solely on internal protection of ATmega chips, so without additional protection it will not handle heavy abuse, overvoltage, etc...
- **3.3V and 5V output**: 3.3V, 5V
- **16MHz crystal**: 16.000

## Photos

<div class="photo-grid" markdown>

[![Arduino Uno R3](./img/Arduino_Uno-R3.jpg)](./img/Arduino_Uno-R3.jpg "Arduino Uno R3"){ .glightbox data-gallery="arduino" }
<span class="caption">Arduino Uno R3</span>

[![Arduino Nano](./img/Arduino_Nano.jpg)](./img/Arduino_Nano.jpg "Arduino Nano"){ .glightbox data-gallery="arduino" }
<span class="caption">Arduino Nano</span>

</div>
## Protocol
- This uses the extended SUMP protocol as implemented by sigrok in ols driver.
[https://sigrok.org/wiki/Openbench_Logic_Sniffer](https://sigrok.org/wiki/Openbench_Logic_Sniffer)
- [http://dangerousprototypes.com/docs/The_Logic_Sniffer%27s_extended_SUMP_protocol](http://dangerousprototypes.com/docs/The_Logic_Sniffer%27s_extended_SUMP_protocol)
## Problems

Everything looks almost fine, device loads in pulseview, but there are still some cosmetic issues left to tackle:

- **Buffer is currently sent or parsed backwards (time goes from right to left/zero)!!!** (not sure if problem lays in arduino code or sigrok)
- RLE (=continuous capture) is not properly implemented in sigrok/ols driver, therefore capture length is limited by device memory
- Maximum supported samplerate is reported by device and received by sigrok, but not reflected in pulseview GUI
- Triggering is still a work in progress, but generally works for samples below 1MHz. over 1MHz works for a basic busy wait trigger that doesn't store until after the trigger fires.

**TODO** (gsi) I understand that **RLE** is about compression, not streaming. The RLE feature may extend the capacity to store more samples, but still remains in buffered mode and is limited by physical memory, and may add more constraints on supported sample rates when not done in hardware.

## Oportunities

**TODO** (gsi) See the above general comment, this page is about AGLA and not generic Arduino support as an all singing and all dancing device. All of mixed signal and output pins and generator mode and pin feature configuration are outside of the SUMP protocol spec. Any of hardware pin control or board specific indicators are strictly internal to the firmware and unrelated to the PC side.

- Arduino has couple of ADC enabled pins. ADC is not very fast, but i guess we can add some basic analog input capabilities for low samplerate modes. (1kHz analog sampling should be more than doable). [[1]](https://github.com/gillham/logic_analyzer/issues/49)
- Add way to enable/disable input pullups through sigrok and pulseview GUI [[2]](https://github.com/gillham/logic_analyzer/issues/47)
- Configure arduino PWM on some unused pin to work as clock and calibration source [[3]](https://github.com/gillham/logic_analyzer/issues/48)
- Add way to control output pins or provide signal generator controlled by pulseview GUI
- Signal if we are currently capturing using some unused pin (= sync multiple analyzers together using triggers!) [[4]](https://github.com/gillham/logic_analyzer/issues/50)
## FTDI-LA (alternative approach)

**TODO** (gsi) Does a discussion of FTDI as a logic analyzer belong to the AGLA device page, just because some Arduino boards happen to use FTDI for serial communication to the MCU? Would not think so.

Note that some older arduino designs and arduino clones feature FTDI usb-serial chip, which might be used as logic analyzer as well using [FTDI-LA](https://sigrok.org/wiki/FTDI-LA). **This has nothing to do with OLS driver described on this page and i mention it just for completeness.** Both Arduino/SUMP and FTDI-LA approaches have some pitfalls, so you might prefer one or the another.

Also note that Arduino boards wire FTDI to ATmega chips and that might cause you some troubles. If atmega pins connected to FTDI are configured as outputs or pullups, it can mess up the measurements or even damage the ATmega (given you apply voltage to it). So make sure you know what are you doing. In best case scenario you have arduino board with DIP socket, which allows you to remove atmega completely from board when you use it with FTDI-LA driver.

## Resources
- [Github page of the project](https://github.com/gillham/logic_analyzer)
- [Github issue concerning sigrok support](https://github.com/gillham/logic_analyzer/issues/38)
- [Similar project for STM32 boards](https://github.com/ddrown/stm32-sump)
- [Similar project for ESP32 boards](https://github.com/Ebiroll/esp32_sigrok)

