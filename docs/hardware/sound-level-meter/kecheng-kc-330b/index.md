---
title: Kecheng KC-330B
---

# Kecheng KC-330B

<div class="infobox" markdown>

![Kecheng KC-330B](./img/Kecheng_KC-330B.png){ .infobox-image }

### Kecheng KC-330B

| | |
|---|---|
| **Status** | supported |
| **Source code** | [kecheng-kc-330b](https://github.com/OpenTraceLab/OpenTraceCapture/tree/main/src/hardware/kecheng-kc-330b) |
| **Connectivity** | USB |
| **Measurement range (A)** | 30dB - 130dB |
| **Resolution** | 0.1dB |
| **Accuracy (94dB@1kHz)** | 1.5dB |
| **Frequency weighting** | A, C |
| **Time weighting** | F, S |

</div>

The **Kecheng KC-330B** is a sound level meter and data logger with USB connectivity.

See [Kecheng KC-330B/Info](https://sigrok.org/wiki/Kecheng_KC-330B/Info) for more details (such as **lsusb -vvv** output) about the device.

## Hardware
- [Silicon Labs F320](http://www.silabs.com/Support%20Documents/TechnicalDocs/C8051F32x.pdf) 8-bit MCU with USB interface
- 2 X [SG Micro SGM8522](http://www.sg-micro.com/f/productparticular.aspx?pid=60) dual rail-to-rail op-amp, SGM8524 quad rail-to-rail op-amp
- [Microchip 24LC512](http://www.microchip.com/wwwproducts/Devices.aspx?dDocName=en010828) 64KB EEPROM
- [Texas Instruments CD4053M](http://www.ti.com/product/cd4053b) triple 2-channel multiplexer

## Photos

<div class="photo-grid" markdown>

[![Kecheng Kc 330b](./img/Kecheng_KC-330B.png)](./img/Kecheng_KC-330B.png "Kecheng Kc 330b"){ .glightbox data-gallery="kecheng-kc-330b" }
<span class="caption">Kecheng Kc 330b</span>

[![Kecheng Kc 330b Pcb Lcd Top](./img/Kecheng_KC-330B_PCB_LCD_top.jpg)](./img/Kecheng_KC-330B_PCB_LCD_top.jpg "Kecheng Kc 330b Pcb Lcd Top"){ .glightbox data-gallery="kecheng-kc-330b" }
<span class="caption">Kecheng Kc 330b Pcb Lcd Top</span>

[![Kecheng Kc 330b F320](./img/Kecheng_KC-330B_F320.jpg)](./img/Kecheng_KC-330B_F320.jpg "Kecheng Kc 330b F320"){ .glightbox data-gallery="kecheng-kc-330b" }
<span class="caption">Kecheng Kc 330b F320</span>

[![Kecheng Kc 330b Pcb Top](./img/Kecheng_KC-330B_PCB_top.jpg)](./img/Kecheng_KC-330B_PCB_top.jpg "Kecheng Kc 330b Pcb Top"){ .glightbox data-gallery="kecheng-kc-330b" }
<span class="caption">Kecheng Kc 330b Pcb Top</span>

[![Kecheng Kc 330b Pcb Top Detail](./img/Kecheng_KC-330B_PCB_top_detail.jpg)](./img/Kecheng_KC-330B_PCB_top_detail.jpg "Kecheng Kc 330b Pcb Top Detail"){ .glightbox data-gallery="kecheng-kc-330b" }
<span class="caption">Kecheng Kc 330b Pcb Top Detail</span>

[![Kecheng Kc 330b Back](./img/Kecheng_KC-330B_back.png)](./img/Kecheng_KC-330B_back.png "Kecheng Kc 330b Back"){ .glightbox data-gallery="kecheng-kc-330b" }
<span class="caption">Kecheng Kc 330b Back</span>

[![Kecheng Kc 330b Pcb Bottom](./img/Kecheng_KC-330B_PCB_bottom.jpg)](./img/Kecheng_KC-330B_PCB_bottom.jpg "Kecheng Kc 330b Pcb Bottom"){ .glightbox data-gallery="kecheng-kc-330b" }
<span class="caption">Kecheng Kc 330b Pcb Bottom</span>

</div>
## Protocol

The host sends commands to the device via endpoint 2, and receives responses via endpoint 1. A command consists of a single byte, with the MSB (bit 7) cleared, followed by any arguments to the command. The response from the device consists of at least one byte: the command, with the MSB set.

| Command | Response | Description |
|---|---|---|
| 0x01 | 0x81 | **Configure device**, 6 bytes payload: |
|  |  |  | 1 | Sample interval 0-6, representing 125ms, 500ms, 1s, 2s, 5s, 10s, 60s respectively. |
|  | 2 | Alarm low threshold |
|  | 3 | Alarm high threshold |
|  | 4 | Time weighting: 0=Fast, 1=Slow |
|  | 5 | Frequency weighting: 0=dBA, 1=dBC |
|  | 6 | Data source: 0=memory, 1=real time |

0x02

0x82

**Identify**, response payload is length byte + device model (ASCII)

0x03

0x83

**Set date and time**, 6 bytes payload:

|  | 1 | Last two digits of year, e.g. 0x0d for 2013 |
|---|---|---|
|  | 2 | Month, 1-12 |
|  | 3 | Day of month, 1-31 |
|  | 4 | Hours |
|  | 5 | Minutes |
|  | 6 | Seconds |

0x04

**Check device status**

0x84

Device is activated, i.e. logging to memory or live to PC ("log" on the display).

0xa4

Device is deactivated ("con" or "---" on the display).

0x05

0x85

**Get stored measurement info**, response has 8 bytes payload:

|  | 1-6 | Configuration settings of acquired data, same format as 0x01 command (except 0x11...) |
|---|---|---|
|  | 7-8 | Big-endian integer representing the number of stored measurements (32000 is the maximum). |

0x06

0x86

**Get stored start date/time**. Response has 6 bytes payload, same format as 0x03 command.

0x07

0x87

**Get stored measurements**, 3 bytes payload:

|  | 1-2 | Big-endian integer representing the sample offset, in blocks of 63 samples. |
|---|---|---|
|  | 3 | Number of samples to send. This is always the maximum, 0x3f, until the last chunk. |

0x08

0x88

**Get live measurement**, response has 2 bytes payload: big-endian integer representing the dB value X 10

