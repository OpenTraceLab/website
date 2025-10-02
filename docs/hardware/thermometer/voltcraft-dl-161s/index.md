---
title: Voltcraft DL-161S
---

# Voltcraft DL-161S

<div class="infobox" markdown>

![Voltcraft DL-161S](./img/Voltcraft_DL-161S.png){ .infobox-image }

### Voltcraft DL-161S

| | |
|---|---|
| **Status** | planned |
| **Connectivity** | USB |
| **Frequency range** | 31.5Hz - 8kHz |
| **Measurement range (A)** | 30dB - 130dB |
| **Accuracy (94dB@1kHz)** | 1.4dB |
| **Frequency weighting** | A, C |
| **Time weighting** | F, S |
| **Standards** | IEC 61672-1 Class 2 |
| **Website** | [Voltcraft](http://www.conrad.de/ce/de/product/105054/VOLTCRAFT-DL-161S-USB-Schallpegel-Datenlogger-315-Hz-8-kHz-30-bis-130-dB-Schallpegel-Messgeraet-Laerm-Messgeraet) |

</div>

The **Voltcraft DL-161S** is a sound level meter with USB connectivity.

See [Voltcraft DL-161S/Info](https://sigrok.org/wiki/Voltcraft_DL-161S/Info) for more details (such as **lsusb -vvv** output) about the device.

This is a rebadged [CEM DT-173](http://www.cem-instruments.com/en/pro/pro-290.html).

## Hardware

TODO

## Photos

<div class="photo-grid" markdown>

[![Voltcraft Dl 161s](./img/Voltcraft_DL-161S.png)](./img/Voltcraft_DL-161S.png "Voltcraft Dl 161s"){ .glightbox data-gallery="voltcraft-dl-161s" }
<span class="caption">Voltcraft Dl 161s</span>

</div>
## Protocol

The host sends commands and receives responses via a virtual serial port, with USB bulk endpoint 2 as a backend. A command consists of a single byte followed by any arguments to the command.

| Command | Response | Description |
|---|---|---|
| 0x0c | 0xff | **Calibrate device**, 2 bytes payload: |
|  | 1 | Calibration value, as a signed integer between -10 and 10, where 1 represents 0.1 dB |
|  | 2 | *Unused (0x00)* |
| 0x0e | 0xff | **Configure device** |
|  |  |  | 1-2 | Length of data to follow, as a little-endian integer. |
|  | 3 | "REC" LED flash interval, in seconds: 0=none, 10, 20, 30. |
|  | 4 | Bitfield representing the following flags:

7 | Activation: 0=immediate, 1=manual |
| 6-5 | *Unused* |
| 4 | 0=store measurements, 1=real-time |
| 3 | Frequency weighting: 0=dBC, 1=dBA |
| 2 | Time weighting: 0=Slow, 1=Fast |
| 1-0 | *Unused* |

5

Sample interval 1-7, representing 50ms, 500ms, 1s, 2s, 5s, 10s, 60s respectively.

6

Last two digits of year, e.g. 0x0d for 2013

7

Month, 1-12

8

Day of month, 1-31

9

Hours

10

Minutes

11

Seconds

12-14

Number of samples to acquire, as a big-endian integer.

15

Alarm low threshold

16

Alarm high threshold

0x0d

0xff

**Get stored measurement count**, 2 bytes payload:

1-2

*Always 0x0000?*

Response has 3 byte payload, representing the number of bytes used in sample memory as a little-endian integer. Each sample uses two bytes.

0x0f

**Get stored measurements**, 2 bytes payload is offset into buffer (*as pages? page size?*)

|  | 1 |  |
|---|---|---|
|  | 2 | Sample rate 1-7, as above. |
|  | 3 |  |
|  | 4 |  |
|  | 5 |  |
|  | 6 |  |
|  |  |  |
|  |  |  |

## Resources
- [Device manual](http://www.produktinfo.conrad.com/datenblaetter/100000-124999/105054-an-01-ml-DL_161S_SCHALLP_DATENLOGGER_de_en_fr_nl.pdf)

