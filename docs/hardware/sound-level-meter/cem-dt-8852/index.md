---
title: CEM DT-8852
---

# CEM DT-8852

<div class="infobox" markdown>

![CEM DT-8852](./img/CEM_DT-8852_back.jpg){ .infobox-image }

### CEM DT-8852

| | |
|---|---|
| **Status** | supported |
| **Source code** | [cem-dt-885x](https://github.com/OpenTraceLab/OpenTraceCapture/tree/main/src/hardware/cem-dt-885x) |
| **Connectivity** | USB |
| **Frequency range** | 31.5Hz - 8kHz |
| **Measurement range (A)** | 30dB - 130dB |
| **Resolution** | 0.1dB |
| **Accuracy (94dB@1kHz)** | 1.4dB |
| **Frequency weighting** | A, C |
| **Time weighting** | F, S |
| **Standards** | IEC 61672-1 Class 2 |
| **Website** | [cem-instruments.com](http://www.cem-instruments.com/en/pro/pro-385.html) |

</div>

The **CEM DT-8852** is an IEC 61672-1 class 2 compliant sound level meter with USB connectivity.

See [CEM DT-8852/Info](https://sigrok.org/wiki/CEM_DT-8852/Info) for more details (such as **lsusb -vvv** output) about the device.

Some random facts:

- The device only starts logging to USB when the SETUP key is pressed on the keypad. This also disables auto power-off mode.
- Power consumption is 9.5mA at 9V, regardless of USB or recording status; 15mA when the backlight is on.
- The battery low warning starts when the battery delivers less than 7V.
- Sound pressure level measurements are sent to the host at a rate of 20Hz.

## Hardware
- [Holtek HT49R70A](http://www.holtek.com/english/docum/uc/49x70.htm) microcontroller with firmware in OTP flash
- [Silicon Labs CP2102](http://www.silabs.com/products/interface/usbtouart/Pages/usb-to-uart-bridge.aspx) USB-serial interface

## Photos

<div class="photo-grid" markdown>

[![Cem Dt 8852 Back](./img/CEM_DT-8852_back.jpg)](./img/CEM_DT-8852_back.jpg "Cem Dt 8852 Back"){ .glightbox data-gallery="cem-dt-8852" }
<span class="caption">Cem Dt 8852 Back</span>

[![Cem Dt 8852 Side](./img/CEM_DT-8852_side.jpg)](./img/CEM_DT-8852_side.jpg "Cem Dt 8852 Side"){ .glightbox data-gallery="cem-dt-8852" }
<span class="caption">Cem Dt 8852 Side</span>

[![Cem Dt 8852](./img/CEM_DT-8852.jpg)](./img/CEM_DT-8852.png "Cem Dt 8852"){ .glightbox data-gallery="cem-dt-8852" }
<span class="caption">Cem Dt 8852</span>

[![Cem Dt 8852 Pcb Back Middle](./img/CEM_DT-8852_PCB_back_middle.jpg)](./img/CEM_DT-8852_PCB_back_middle.jpg "Cem Dt 8852 Pcb Back Middle"){ .glightbox data-gallery="cem-dt-8852" }
<span class="caption">Cem Dt 8852 Pcb Back Middle</span>

[![Cem Dt 8852 Mcu](./img/CEM_DT-8852_MCU.jpg)](./img/CEM_DT-8852_MCU.jpg "Cem Dt 8852 Mcu"){ .glightbox data-gallery="cem-dt-8852" }
<span class="caption">Cem Dt 8852 Mcu</span>

[![Cem Dt 8852 Pcb Front](./img/CEM_DT-8852_PCB_front.jpg)](./img/CEM_DT-8852_PCB_front.jpg "Cem Dt 8852 Pcb Front"){ .glightbox data-gallery="cem-dt-8852" }
<span class="caption">Cem Dt 8852 Pcb Front</span>

[![Cem Dt 8852 Pcb Back](./img/CEM_DT-8852_PCB_back.jpg)](./img/CEM_DT-8852_PCB_back.jpg "Cem Dt 8852 Pcb Back"){ .glightbox data-gallery="cem-dt-8852" }
<span class="caption">Cem Dt 8852 Pcb Back</span>

[![Cem Dt 8852 Cp2102](./img/CEM_DT-8852_CP2102.jpg)](./img/CEM_DT-8852_CP2102.jpg "Cem Dt 8852 Cp2102"){ .glightbox data-gallery="cem-dt-8852" }
<span class="caption">Cem Dt 8852 Cp2102</span>

[![Cem Dt 8852 Display Segments](./img/CEM_DT-8852_display_segments.jpg)](./img/CEM_DT-8852_display_segments.jpg "Cem Dt 8852 Display Segments"){ .glightbox data-gallery="cem-dt-8852" }
<span class="caption">Cem Dt 8852 Display Segments</span>

[![Cem Dt 8852 Pcb Back Bottom](./img/CEM_DT-8852_PCB_back_bottom.jpg)](./img/CEM_DT-8852_PCB_back_bottom.jpg "Cem Dt 8852 Pcb Back Bottom"){ .glightbox data-gallery="cem-dt-8852" }
<span class="caption">Cem Dt 8852 Pcb Back Bottom</span>

</div>
## Protocol

The device communicates at 9600 baud, no parity, 8 data bits, and 1 stop bit (9600/8n1).

### Commands

None of the following commands are needed to receive live measurements from the device; see the next section.

The commands are always 1 byte, take no parameters, and receive no acknowledgement or reply. Figuring out whether the command was successful or not must be done by watching the continual stream of settings. This is not optional: the device is very unresponsive, and commands nearly always have to be resent.

The following commands are supported:

| Token | Description |
|---|---|
| 0x33 | Power down the device. |
| 0x55 | Toggle measurement recording on/off. |
| 0x11 | Toggle Max/Min/normal mode. |
| 0x77 | Toggle Fast/Slow time weighting |
| 0x88 | Toggle measurement range. |
| 0x99 | Toggle dBA/dBC frequency weighting. |
| 0xac | Request transfer of stored measurement records. |

### Measurements and settings

Current settings and measurements are continually streamed over the serial bus, without any prompting from the PC. Data is encapsulated in packets of between two and five bytes. The packets are structured as follows:

| 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|
| 0xa5 | Token | Data |

The number of data bytes depend on the token. These are the tokens:

| Token | Data | Description |
|---|---|---|
| 0x02 | 0 | Time weighting Fast |
| 0x03 | 0 | Time weighting Slow |
| 0x04 | 0 | Max hold mode |
| 0x05 | 0 | Min hold mode |
| 0x06 | 3 | Current time in BCD; first nibble unknown |
| 0x07 | 0 | Current measurement is over measurement range high threshold |
| 0x08 | 0 | Current measurement is under measurement range low threshold |
| 0x09 | 0 | Memory store is full |
| 0x0a | 0 | Device is currently recording to memory |
| 0x0b | 1 | Last measurement sent with 0x0d was shown on display readout |
| 0x0c | 0 | Last measurement sent with 0x0d was shown in bargraph on display |
| 0x0d | 2 | Current measurement, multiplied by 10, in BCD |
| 0x0e | 0 | Live measurements mode (not max/min hold) |
| 0x0f | 0 | Battery is low |
| 0x11 | 0 | Current measurement is within the current measurement range |
| 0x19 | 0 | Memory store is not full |
| 0x1a | 0 | Device is not recording to memory |
| 0x1b | 1 | Frequency weighting dBA |
| 0x1c | 1 | Frequency weighting dBC |
| 0x1f | 0 | Battery is OK |
| 0x30 | 0 | Measurement range 30-80 dB |
| 0x40 | 0 | Measurement range 30-130 dB (auto) |
| 0x4b | 0 | Measurement range 50-100 dB |
| 0x4c | 0 | Measurement range 80-130 dB |

### Recorded measurements

After the host has requested the recorded measurement log, a packet will be inserted into the regular output stream. Instead of 0xa5, this packet begins with 0xbb:

| 1 | 2 | 3 |
|---|---|---|
| 0xbb | Length |

The length field is big-endian encoded, with an offset of 100. A length field of `0x0064` thus indicates no stored samples.

This is followed by a series of records, where the first byte (token) indicates the content to follow:

| Token | Description |
|---|---|
| 0xaa | Measurements in this record use dBA frequency weighting. Metadata follows. |
| 0xcc | Measurements in this record use dBC frequency weighting. Metadata follows. |
| 0xac | Measurements follow, until the next token. Encoding is BCD times 10, as in the live stream. |
| 0xdd | End of recorded measurement dump. |

The metadata following 0xaa and 0xcc denotes the date and time this record was started, and the sampling rate. It is encoded in 7 bytes:

| Byte | Description |
|---|---|
| 0 | Last two digits of year (BCD) |
| 1 | Month (BCD) |
| 2 | Day of month (BCD) |
| 3 | Hour (BCD) |
| 4 | Minutes (BCD) |
| 5 | Seconds (BCD) |
| 6 | Samplerate, as seconds between measurements (1-59, BCD) |

#### Bugs
- A packet indicating memory is empty is not supposed to have any sub-packets: only the 0xbb token, length, and 0xdd to indicate end of transfer. However this always seems to include a 0xaa or 0xcc byte as well:

| 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|
| 0xbb | 0x00 | 0x64 | 0xaa | 0xdd |

- The length of the memory transfer (as sent after 0xbb) refers to all the data sent afterwards, excepting only 0xac and 0xdd, which are protocol tokens. However:
The count is always off by one; one byte less is sent than the length indicates.
- The last record's measurement data's last byte is in fact a random extra byte, half of a BCD-encoded SPL value. This is another off-by-one: the byte has to be discarded.

The length is thus actually off by two.

## Resources

[Partial protocol documentation](http://www.produktinfo.conrad.com/datenblaetter/100000-124999/105031-da-01-en-InterfaceProtocol_VOLTCRAFT_SL_451.pdf)

