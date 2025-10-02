---
title: Colead SL-5868P
---

# Colead SL-5868P

<div class="infobox" markdown>

![Colead SL-5868P](./img/Colead_SL-5868P.jpg){ .infobox-image }

### Colead SL-5868P

| | |
|---|---|
| **Status** | supported |
| **Source code** | [colead-slm](https://github.com/OpenTraceLab/OpenTraceCapture/tree/main/src/hardware/colead-slm) |
| **Connectivity** | [RS232](https://sigrok.org/wiki/Device_cables#Colead_SL-5868P_cables) |
| **Frequency range** | 31.5Hz - 8kHz |
| **Measurement range (A)** | 30dB - 130dB |
| **Resolution** | 0.1dB |
| **Accuracy (94dB@1kHz)** | 1dB |
| **Frequency weighting** | A, C, Flat |
| **Time weighting** | F, S |
| **Standards** | IEC 651 Type 2, ANSI 1.4 Type 2 |
| **Website** | [coleadmeter.com](http://www.coleadmeter.com/view3.asp?goodsname=Multifunctional%20Sound%20Level%20Meter%20SL-5868P&amp;id2=226) |

</div>

The **Colead SL5868P** is a sound level meter with RS232 connectivity.

It has live (Lp), equivalent continuous (Leq), and threshold-based (Ln) measurement modes. It can also trigger alarm conditions based on a configured level, and drive a relay accordingly.

It is rebranded under many names, but appears to generally have the SL-5868P model designation. It's available for under $100.

## Hardware
- [Nuvoton W78E052D](http://www.nuvoton.com/NuvotonMOSS/Community/ProductInfo.aspx?tp_GUID=4119224f-5a2b-4861-a2aa-4e7895c6a532) 8-bit microcontroller
- [Holtek HT1621B](http://www.holtek.com/english/docum/consumer/1621.htm) LCD driver
- 6MHz clock

## Photos

<div class="photo-grid" markdown>

[![Colead Sl 5868p](./img/Colead_SL-5868P.jpg)](./img/Colead_SL-5868P.jpg "Colead Sl 5868p"){ .glightbox data-gallery="colead-sl-5868p" }
<span class="caption">Colead Sl 5868p</span>

[![Colead Sl 5868p Pcb Front](./img/Colead_SL-5868P_PCB_front.jpg)](./img/Colead_SL-5868P_PCB_front.jpg "Colead Sl 5868p Pcb Front"){ .glightbox data-gallery="colead-sl-5868p" }
<span class="caption">Colead Sl 5868p Pcb Front</span>

[![Colead Sl 5868p Pcb Detail 2](./img/Colead_SL-5868P_PCB_detail_2.jpg)](./img/Colead_SL-5868P_PCB_detail_2.jpg "Colead Sl 5868p Pcb Detail 2"){ .glightbox data-gallery="colead-sl-5868p" }
<span class="caption">Colead Sl 5868p Pcb Detail 2</span>

[![Colead Sl 5868p Pcb Back](./img/Colead_SL-5868P_PCB_back.jpg)](./img/Colead_SL-5868P_PCB_back.jpg "Colead Sl 5868p Pcb Back"){ .glightbox data-gallery="colead-sl-5868p" }
<span class="caption">Colead Sl 5868p Pcb Back</span>

[![Colead Sl 5868p Side](./img/Colead_SL-5868P_side.jpg)](./img/Colead_SL-5868P_side.jpg "Colead Sl 5868p Side"){ .glightbox data-gallery="colead-sl-5868p" }
<span class="caption">Colead Sl 5868p Side</span>

[![Colead Sl 5868p Pcb Unmarked](./img/Colead_SL-5868P_PCB_unmarked.jpg)](./img/Colead_SL-5868P_PCB_unmarked.jpg "Colead Sl 5868p Pcb Unmarked"){ .glightbox data-gallery="colead-sl-5868p" }
<span class="caption">Colead Sl 5868p Pcb Unmarked</span>

[![Colead Sl 5868p Pcb Detail 1](./img/Colead_SL-5868P_PCB_detail_1.jpg)](./img/Colead_SL-5868P_PCB_detail_1.jpg "Colead Sl 5868p Pcb Detail 1"){ .glightbox data-gallery="colead-sl-5868p" }
<span class="caption">Colead Sl 5868p Pcb Detail 1</span>

[![Colead Sl 5868p Back](./img/Colead_SL-5868P_back.jpg)](./img/Colead_SL-5868P_back.jpg "Colead Sl 5868p Back"){ .glightbox data-gallery="colead-sl-5868p" }
<span class="caption">Colead Sl 5868p Back</span>

[![Colead Sl 5868p](./img/Colead_SL-5868P.png)](./img/Colead_SL-5868P.png "Colead Sl 5868p"){ .glightbox data-gallery="colead-sl-5868p" }
<span class="caption">Colead Sl 5868p</span>

</div>
## Protocol

The serial port is set to 2400bps, 8 bits, no parity, 1 stop bit (2400/8n1).

The meter sends two measurements per second. When a new measurement is ready, the device sends `0x10`. The PC responds with `0x20`, which causes the device to transmit a 10-byte structure containing configuration and measurement.

When the user presses the `Read` key on the keypad, the device sends all its stored measurements out via the serial port. This is preceded by two bogus measurement records as a marker, where all the digits are set to `0x0a` and byte 2 contains `0x09` in the first record, and `0x08` in the second record. The stored measurement records then follow; the entire sequence is typically repeated twice, including the marker.

When the user switches back to live measurement mode, another two bogus measurement records are sent. To mark the return to live mode, the second bogus record this time contains `0x07`. All following records are then live.

### Commands
| Command | Direction | Description |
|---|---|---|
| **0x10** | Device -> PC | Measurement ready |
| **0x20** | PC -> Device | Send measurement |

### Data structure
| Byte | Value | Description |
|---|---|---|
| 0 |  | *Always 0x08* |
| 1 |  | *Always 0x04* |
| 2 |  | **Configuration. The low nibble has the following meaning:** |
|  | 0000 | Lp, Weighting A, Fast |
|  | 0001 | Lp, Weighting A, Slow |
|  | 0010 | Lp, Weighting C, Fast |
|  | 0011 | Lp, Weighting C, Slow |
|  | 0100 | Lp, Flat, Fast |
|  | 0101 | Lp, Flat, Slow |
|  | 0110 | Ln, Weighting A, Fast |
|  | 0111 | Ln, Weighting A, Slow |
|  | 1000 | Leq, Weighting A, Fast (10-second mean) |
|  | 1001 | Leq, Weighting A, Fast (mean over minutes) |
|  | 1010 | Leq, Weighting A, Slow (10-second mean) |
|  | 1011 | Leq, Weighting A, Slow (mean over minutes) |
|  | 1100 | Internal calibration mode, Fast |
|  | 1101 | Internal calibration mode, Slow |
|  | 1110 | *Unused* |
|  | 1111 | *Unused* |
|  |  | **The high nibble has the following meaning:** |
|  | 0001 | Normal measurement |
|  | 0010 | Max hold mode |
| 3-7 |  | **BCD-encoded value, one byte per digit 0x00-0x09. 0x0a means ignored digit. The last digit represents the decimal.** |
| 8 |  | **Measurement status** |
|  | 0 | Invalid |
|  | 1 | Valid |
| 9 |  | **Checksum: sum of bytes 0-8** |

