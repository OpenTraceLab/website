---
title: XZL_Studio AX
---

# XZL_Studio AX

<div class="infobox" markdown>

![XZL_Studio AX](./img/Studio_XZL_AX.back.jpg){ .infobox-image }

### XZL_Studio AX

| | |
|---|---|
| **Status** | supported |
| **Source code** | [fx2lafw](https://github.com/OpenTraceLab/OpenTraceCapture/tree/main/src/hardware/fx2lafw) |
| **Channels** | 8 + 1 |
| **Samplerate** | 8ch @ 24MHz, 8+1ch @ 12MHz |
| **Samplerate (state)** | — |
| **Triggers** | 1 independent trigger + (SW-probe 0,1) |
| **Min/max voltage** | Digital: max. 5.5VAnalog: -10V — +10V |
| **Threshold voltage** | Digital: Fixed: VIH=1.4V, VIL=0.8V |
| **Memory** | none |
| **Compression** | none |
| **Price range** | $20 - 35 |
| **Website** | [hotmcu.com](http://www.hotmcu.com/xzl-ax-oscilloscope-and-logic-analyzer-ax-pro-logic-analyzer-p-14.html?cPath=3_26) |

</div>

The **XZL_Studio AX** is a USB-based, 8-channel logic analyzer with up to 24MHz sampling rate, with 1 additional analog channel (theoretically 2, but only one of them can be used at a time; 3MHz analog bandwidth).

It is a clone of the [CWAV USBee AX-Pro](/w/index.php?title=CWAV_USBee_AX-Pro&action=edit&redlink=1).

In sigrok, we use the open-source [fx2lafw](https://sigrok.org/wiki/Fx2lafw) firmware for this logic analyzer.

**Note**: [fx2lafw](https://sigrok.org/wiki/Fx2lafw) currently doesn't support switching between the two possible analog channels, 1ACH (TODO: not verified on hardware) will be used unconditionally.

See [XZL_Studio AX/Info](https://sigrok.org/wiki/XZL_Studio_AX/Info) for some more details (such as **lsusb -v** output) on the device.

## Hardware
- **Main chip**:  Cypress CY7C68013A-56LTXC (FX2LP), U6
- **ADC**: 1x Texas Instruments TLC5510I (SO 24pin package), 8-Bit, 20 MSPS ADC, Single Channel, U10, outputs D1-D8 connected to PD0-PD7, OE# grounded, CLOCK from CTL2 on U6
- **I2C EEPROM**: Atmel 24C02C
- **Low-dropout voltage regulator**: Advanced Monolithic Systems AMS1117-3.3
- **Crystal**: 24MHz
- **Multiplexer**: HCF4051 - Single 8-Channel Analog Multiplexer/Demultiplexer, U12, channel selectors B and C grounded, selector A controlled by PA0 on U6
- **Op Amp**:  LM358 - Single Supply Dual Operational Amplifiers, U15
- ...

## Photos

<div class="photo-grid" markdown>

[![Studio Xzl Ax.back](./img/Studio_XZL_AX.back.jpg)](./img/Studio_XZL_AX.back.jpg "Studio Xzl Ax.back"){ .glightbox data-gallery="xzl_studio-ax" }
<span class="caption">Studio Xzl Ax.back</span>

[![Xzl Studio Ax Mugshot](./img/Xzl_studio_ax_mugshot.jpg)](./img/Xzl_studio_ax_mugshot.png "Xzl Studio Ax Mugshot"){ .glightbox data-gallery="xzl_studio-ax" }
<span class="caption">Xzl Studio Ax Mugshot</span>

</div>
## Protocol

Since we use the open-source [fx2lafw](https://sigrok.org/wiki/Fx2lafw) firmware for this device, we don't need to know the protocol.

## Resources
- [EE Electronics ESLA201A](https://sigrok.org/wiki/EE_Electronics_ESLA201A) - the same circuit (from firmware's point of view). PCB has been copied and altered, same silkscreen labels. No electrolytic caps, no resistive trimmers, larger screw-hole-keepouts, no cap on pin 13 at U10, no U13 (second MAX1044/ICL7660). Has extra button inside the box!

