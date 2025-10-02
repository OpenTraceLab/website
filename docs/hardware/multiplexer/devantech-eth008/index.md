---
title: Devantech ETH008
---

# Devantech ETH008

<div class="infobox" markdown>

![Devantech ETH008](./img/Devantech-eth008b-mugshot.jpg){ .infobox-image }

### Devantech ETH008

| | |
|---|---|
| **Status** | supported |
| **Source code** | [devantech-eth008](https://github.com/OpenTraceLab/OpenTraceCapture/tree/main/src/hardware/devantech-eth008) |
| **Channels** | 2..20 |
| **Ratings** | 16A 250VAC / 16A 24VDC |
| **Connectivity** | Ethernet/Wifi, TCP |
| **Website** | [robot-electronics.co.uk](https://www.robot-electronics.co.uk/eth008b.html) |

</div>

The **Devantech ETH008** is an Ethernet attached relay card with 8 relays, and was used to initially create the sigrok driver.
Models with 2 up to 20 relays exist, as do Wifi models. Some models 
additionally provide digital input and analog input, as well as digital outputs where users decide whether to attach a relay or use the channel as a data line. The different models' protocols are 
similar enough to the ETH008 model, and it is assumed that all product features of Ethernet cards are accessible. 
Some models' operation has yet to get verified.

The firmware supports several ways of communication: interactive web forms,
HTTP GET requests, binary packets over TCP, text lines over TCP.
The sigrok driver uses binary payloads for simplicity and for maximum compatibility
across firmware versions. Password protection for TCP sockets is currently not supported.

There are several models in the series of cards, with differing degrees of support.
It is assumed that WLAN capable models share the same communication protocol as Ethernet devices.
USB CDC (virtual COM port) models are not supported by this sigrok driver, their protocol differs dramatically.
Neither are Modbus attached cards supported.

| Device name | DO | DI | AI | supported | comment |
|---|---|---|---|---|---|
| ETH002 | 2 | — | — | untested | — |
| ETH008 | 8 | — | — | tested | — |
| ETH484 | 12 | 8 | 4 | tested | — |
| ETH8020 | 20 | 8 | 8 | untested | — |
| ETH1610 | 10 | 16 | 16 | tested | — |
| WIFI002 | 2 | — | — | untested | — |
| WIFI008 | 8 | — | — | untested | — |
| WIFI484 | 12 | 8 | 4 | untested | — |
| WIFI8020 | 20 | 8 | 8 | untested | — |

Many thanks to devantech and robot electronics. 
The [robot-electronics.co.uk shop](https://www.robot-electronics.co.uk/) holds extensive documentation and example source code which is linked from their product pages. 
The card vendor provides MIT licensed Python code to control many cards. The robot-electronics.co.uk support kindly made several devices available via remote network access, to help during the creation and extension of the sigrok driver.

## Hardware
- PIC32MZ microcontroller, S25F32 SPI flash
- SMSC Ethernet chip, Fast Ethernet (100Mbps)
- Rohm BD9703 switching regulator, 2.1mm barrel jack
- Hongfa HF115FD relays, screw terminals with common and NC and NO
- discrete transistors and LED indicators per relay channel
- power LED and RJ45 indicators

Nominal supply for the relay card is 12V. The Rohm regulator accepts 8V..35V.
The HF115 relay may accept 24V, too. But the PIC measures the card's supply
by means of a voltage divider, which most probably constrains the acceptable
range of supply voltages for the card.

Voltage and current capability of the relay heavily depends on AC/DC kinds
and the types of load. Rating is much lower for DC and for inductive loads.
See the card vendor's **relay power rating** discussion and relay datasheet.

## Photos

<div class="photo-grid" markdown>

[![Devantech Eth008b Mugshot](./img/Devantech-eth008b-mugshot.jpg)](./img/Devantech-eth008b-mugshot.png "Devantech Eth008b Mugshot"){ .glightbox data-gallery="devantech-eth008" }
<span class="caption">Devantech Eth008b Mugshot</span>

</div>

