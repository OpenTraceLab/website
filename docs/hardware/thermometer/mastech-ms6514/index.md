---
title: MASTECH MS6514
---

# MASTECH MS6514

<div class="infobox" markdown>

![MASTECH MS6514](./img/MASTECH_MS6514_PCB_front.jpg){ .infobox-image }

### MASTECH MS6514

| | |
|---|---|
| **Status** | supported |
| **Source code** | [mastech-ms6514](https://github.com/OpenTraceLab/OpenTraceCapture/tree/main/src/hardware/mastech-ms6514) |
| **Connectivity** | USB/serial |
| **Measurements** | temperature |
| **Features** | data hold, min/max/avg |
| **Website** | [mastech-group.com](http://www.mastech-group.com/products.php?cate=106&amp;PNo=89) |

</div>

The **MASTECH MS6514** is a logging thermometer with two thermocouple inputs and USB connectivity. It supports K,J,T,E,R,S,N thermocouple types.

See [MASTECH MS6514/Info](https://sigrok.org/wiki/MASTECH_MS6514/Info) for more details (such as **lsusb -v** output) about the device.

The device sends temperature measurements at approximately 2 Hz to the host.

## Hardware
- TODO
- SiLabs CP2102 USB interface chip

## Photos

<div class="photo-grid" markdown>

[![Mastech Ms6514 Pcb Front](./img/MASTECH_MS6514_PCB_front.jpg)](./img/MASTECH_MS6514_PCB_front.jpg "Mastech Ms6514 Pcb Front"){ .glightbox data-gallery="mastech-ms6514" }
<span class="caption">Mastech Ms6514 Pcb Front</span>

[![Mastech Ms6514 Lcd](./img/MASTECH_MS6514_LCD.jpg)](./img/MASTECH_MS6514_LCD.jpg "Mastech Ms6514 Lcd"){ .glightbox data-gallery="mastech-ms6514" }
<span class="caption">Mastech Ms6514 Lcd</span>

[![Mastech Ms6514 Pcb Back](./img/MASTECH_MS6514_PCB_back.jpg)](./img/MASTECH_MS6514_PCB_back.jpg "Mastech Ms6514 Pcb Back"){ .glightbox data-gallery="mastech-ms6514" }
<span class="caption">Mastech Ms6514 Pcb Back</span>

[![Mastech Ms6514 Connectors](./img/MASTECH_MS6514_connectors.jpg)](./img/MASTECH_MS6514_connectors.jpg "Mastech Ms6514 Connectors"){ .glightbox data-gallery="mastech-ms6514" }
<span class="caption">Mastech Ms6514 Connectors</span>

[![Mastech Ms6514 Pcb Back 2](./img/MASTECH_MS6514_PCB_back_2.jpg)](./img/MASTECH_MS6514_PCB_back_2.jpg "Mastech Ms6514 Pcb Back 2"){ .glightbox data-gallery="mastech-ms6514" }
<span class="caption">Mastech Ms6514 Pcb Back 2</span>

[![Mastech Ms6514 Pcb Back 3](./img/MASTECH_MS6514_PCB_back_3.jpg)](./img/MASTECH_MS6514_PCB_back_3.jpg "Mastech Ms6514 Pcb Back 3"){ .glightbox data-gallery="mastech-ms6514" }
<span class="caption">Mastech Ms6514 Pcb Back 3</span>

[![Mastech Ms6514 Front](./img/MASTECH_MS6514_front.jpg)](./img/MASTECH_MS6514_front.png "Mastech Ms6514 Front"){ .glightbox data-gallery="mastech-ms6514" }
<span class="caption">Mastech Ms6514 Front</span>

[![Mastech Ms6514 Mugshot](./img/MASTECH_MS6514_mugshot.jpg)](./img/MASTECH_MS6514_mugshot.png "Mastech Ms6514 Mugshot"){ .glightbox data-gallery="mastech-ms6514" }
<span class="caption">Mastech Ms6514 Mugshot</span>

</div>
## Protocol

The device communicates with the host via a SiLabs CP2102 USB interface chip. Communication parameters are 9600/8n1. Live data is transmitted as soon as the button Setup/PC-Link is pressed for 3 seconds.

#### Commands
| Byte | Description |
|---|---|
| 0xA1 | Start sending stored data. |

#### Received data
| Byte | Bit | Description |
|---|---|---|
| 0 |  | Always 0x65 |
| 1 |  | Always 0x14 |
| 2 | 0 | 1=READ of stored values, 0=LIVE data |
| 4..3 |  | Index of stored value (0..999) oldest is 0 |
| 6..5 |  | Temperature main display (absolute value without sign) |
| 8..7 |  | Temperature aux display (absolute value without sign) |
| 9 | 5..4 | Mode: 10=SETUP, 11=READ |
| 2..0 | Thermocouple type (1=K, 2=J, 3=T, 4=E, 5=R, 6=S, 7=N) |
| 10 | 6 | Hold  (1=HOLD, 0=not HOLD) |
| 5 | Record active (1=REC, 0=not REC) |
| 1..0 | Unit (1=°C, 2=°F, 3=K) |
| 11 | 7 | Sign temperature main display (1=negative, 0=positive) |
| 6 | Overload temperature main display (1="OL" on LCD) |
| 3 | Factor temperature main display (1 means divide by 10) |
| 1..0 | Function main and aux display (00=T1 on main, T2 on aux; 01=T2 on main, T1 on aux; 10=T1-T2 on main, T1 on aux; 11=T1-T2 on main, T2 on aux) |
| 12 | 7 | Sign temperature aux display (1=negative, 0=positive) |
| 6 | Overload temperature aux display (1="OL" on LCD) |
| 3 | Factor temperature aux display (1 means divide by 10) |
| 1..0 | Function aux display (0=no active, 1=MAX, 2=MIN, 3=AVG). If >0 function defined in byte 11, bit 0-1 is overriden. |
| 13 |  | Hours (hh) |
| 14 |  | Minutes (mm) |
| 15 |  | Seconds (ss) |
| 16 |  | Always 0x0D |
| 17 |  | Always 0x0A |

## Resources
- [Manual](http://www.mastech-group.com/download_s.php?id=173)
- [Vendor software](http://www.mastech-group.com/download_s.php?id=221)

