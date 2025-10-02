---
title: TekPower TP4000ZC
---

# TekPower TP4000ZC

<div class="infobox" markdown>

![TekPower TP4000ZC](./img/Tp4000zc_chip.jpg){ .infobox-image }

### TekPower TP4000ZC

| | |
|---|---|
| **Status** | supported |
| **Source code** | [serial-dmm](https://github.com/OpenTraceLab/OpenTraceCapture/tree/main/src/hardware/serial-dmm) |
| **Counts** | 4000 |
| **IEC 61010-1** | CAT II (600V) |
| **Connectivity** | [RS232](https://sigrok.org/wiki/Device_cables#Digitek_DT4000ZC_cable) |
| **Measurements** | voltage, resistance, continuity, diode, capacitance, frequency, temperature, current, duty cycle |
| **Features** | autorange, data hold, relative |
| **Website** | [tekpower.us](http://www.tekpower.us) |

</div>

The **TekPower TP4000ZC** is a 4000 counts, CAT II (600V) handheld digital multimeter with RS232 connectivity.

This multimeter is a rebadged [Digitek DT4000ZC](https://sigrok.org/wiki/Digitek_DT4000ZC).

## Hardware

**Multimeter:**

- **Multimeter IC**: The microcontroller is an unidentifiable plastic blob (based on the communication protocol, probably a [Fortune Semiconductor FS9721_LP3](https://sigrok.org/wiki/Multimeter_ICs#Fortune_Semiconductor_FS9721_LP3))
- LM358 opamp
- HEF4013BT flip-flop
- The RS-232 connector is a standard 3.5m stereo jack, with the ring left unconnected. The transmitter is optically insulated from the rest of the device.

**Cable:**

- See [Device_cables#Digitek_DT4000ZC_cable](https://sigrok.org/wiki/Device_cables#Digitek_DT4000ZC_cable).
- The DB-9 connector has a loopback resistor between the RX and TX pins.

## Photos

<div class="photo-grid" markdown>

[![Tp4000zc Chip](./img/Tp4000zc_chip.jpg)](./img/Tp4000zc_chip.jpg "Tp4000zc Chip"){ .glightbox data-gallery="tekpower-tp4000zc" }
<span class="caption">Tp4000zc Chip</span>

[![Tp4000zc Chip Lm358](./img/Tp4000zc_chip_LM358.jpg)](./img/Tp4000zc_chip_LM358.jpg "Tp4000zc Chip Lm358"){ .glightbox data-gallery="tekpower-tp4000zc" }
<span class="caption">Tp4000zc Chip Lm358</span>

[![Tp4000zc Open Back](./img/Tp4000zc_open_back.jpg)](./img/Tp4000zc_open_back.jpg "Tp4000zc Open Back"){ .glightbox data-gallery="tekpower-tp4000zc" }
<span class="caption">Tp4000zc Open Back</span>

[![Tp4000zc Back](./img/Tp4000zc_back.jpg)](./img/Tp4000zc_back.jpg "Tp4000zc Back"){ .glightbox data-gallery="tekpower-tp4000zc" }
<span class="caption">Tp4000zc Back</span>

[![Tp4000zc Back Nocover](./img/Tp4000zc_back_nocover.jpg)](./img/Tp4000zc_back_nocover.jpg "Tp4000zc Back Nocover"){ .glightbox data-gallery="tekpower-tp4000zc" }
<span class="caption">Tp4000zc Back Nocover</span>

[![Tp4000zc Front Nocover](./img/Tp4000zc_front_nocover.jpg)](./img/Tp4000zc_front_nocover.png "Tp4000zc Front Nocover"){ .glightbox data-gallery="tekpower-tp4000zc" }
<span class="caption">Tp4000zc Front Nocover</span>

[![Tp4000zc 232 Module](./img/Tp4000zc_232_module.jpg)](./img/Tp4000zc_232_module.jpg "Tp4000zc 232 Module"){ .glightbox data-gallery="tekpower-tp4000zc" }
<span class="caption">Tp4000zc 232 Module</span>

[![Tp4000zc Pcb Front](./img/Tp4000zc_pcb_front.jpg)](./img/Tp4000zc_pcb_front.jpg "Tp4000zc Pcb Front"){ .glightbox data-gallery="tekpower-tp4000zc" }
<span class="caption">Tp4000zc Pcb Front</span>

[![Tp4000zc 232 Optoisolation](./img/Tp4000zc_232_optoisolation.jpg)](./img/Tp4000zc_232_optoisolation.jpg "Tp4000zc 232 Optoisolation"){ .glightbox data-gallery="tekpower-tp4000zc" }
<span class="caption">Tp4000zc 232 Optoisolation</span>

[![Tp4000zc 232 Pcb Front](./img/Tp4000zc_232_pcb_front.jpg)](./img/Tp4000zc_232_pcb_front.jpg "Tp4000zc 232 Pcb Front"){ .glightbox data-gallery="tekpower-tp4000zc" }
<span class="caption">Tp4000zc 232 Pcb Front</span>

[![Tp4000zc 232 Pcb Back](./img/Tp4000zc_232_pcb_back.jpg)](./img/Tp4000zc_232_pcb_back.jpg "Tp4000zc 232 Pcb Back"){ .glightbox data-gallery="tekpower-tp4000zc" }
<span class="caption">Tp4000zc 232 Pcb Back</span>

[![Tp4000zc Batt](./img/Tp4000zc_batt.jpg)](./img/Tp4000zc_batt.jpg "Tp4000zc Batt"){ .glightbox data-gallery="tekpower-tp4000zc" }
<span class="caption">Tp4000zc Batt</span>

[![Tp4000zc Contents](./img/Tp4000zc_contents.jpg)](./img/Tp4000zc_contents.jpg "Tp4000zc Contents"){ .glightbox data-gallery="tekpower-tp4000zc" }
<span class="caption">Tp4000zc Contents</span>

[![Tp4000zc Angle](./img/Tp4000zc_angle.jpg)](./img/Tp4000zc_angle.png "Tp4000zc Angle"){ .glightbox data-gallery="tekpower-tp4000zc" }
<span class="caption">Tp4000zc Angle</span>

[![Tp4000zc Pcb Back](./img/Tp4000zc_pcb_back.jpg)](./img/Tp4000zc_pcb_back.jpg "Tp4000zc Pcb Back"){ .glightbox data-gallery="tekpower-tp4000zc" }
<span class="caption">Tp4000zc Pcb Back</span>

[![Tp4000zc Front](./img/Tp4000zc_front.jpg)](./img/Tp4000zc_front.png "Tp4000zc Front"){ .glightbox data-gallery="tekpower-tp4000zc" }
<span class="caption">Tp4000zc Front</span>

[![Tp4000zc Chip Hef4013bt](./img/Tp4000zc_chip_HEF4013BT.jpg)](./img/Tp4000zc_chip_HEF4013BT.jpg "Tp4000zc Chip Hef4013bt"){ .glightbox data-gallery="tekpower-tp4000zc" }
<span class="caption">Tp4000zc Chip Hef4013bt</span>

[![Tp4000zc Open Front](./img/Tp4000zc_open_front.jpg)](./img/Tp4000zc_open_front.jpg "Tp4000zc Open Front"){ .glightbox data-gallery="tekpower-tp4000zc" }
<span class="caption">Tp4000zc Open Front</span>

[![Tp4000zc Open Front Noboard](./img/Tp4000zc_open_front_noboard.jpg)](./img/Tp4000zc_open_front_noboard.jpg "Tp4000zc Open Front Noboard"){ .glightbox data-gallery="tekpower-tp4000zc" }
<span class="caption">Tp4000zc Open Front Noboard</span>

</div>
## Protocol

See [Multimeter_ICs#Fortune_Semiconductor_FS9721_LP3](https://sigrok.org/wiki/Multimeter_ICs#Fortune_Semiconductor_FS9721_LP3).

User bit 2 is used to indicate temperature measurement in degrees Celsius.

## Resources
- [Video review of TP4000ZC (Part 1/2)](http://www.youtube.com/watch?v=kXzAD74C5As)
- [Video review of TP4000ZC (Part 2/2)](http://www.youtube.com/watch?v=7pbRLom7bNc)
- [TP4000ZC serial protocol](http://www.multimeterwarehouse.com/TP4000ZC/TP4000ZC_serial_protocol.pdf)
- [multimeterwarehouse.com: TP4000ZC](http://www.multimeterwarehouse.com/TP4000ZC.htm)
- [multimeterreviews.com: TekPower TP4000ZC (PC RS232 Interface)](http://www.multimeterreviews.com/tekpower-tp4000zc-pc-based-rs232-interaced-auto-ranging-digital/)
- [mjlorton.com: T4D 22 TekPower TP4000ZC](http://mjlorton.com/forum/index.php?topic=103.0)

