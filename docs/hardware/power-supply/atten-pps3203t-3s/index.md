---
title: Atten PPS3203T-3S
---

# Atten PPS3203T-3S

<div class="infobox" markdown>

![Atten PPS3203T-3S](./img/Atten_PPS3203T-3S.jpg){ .infobox-image }

### Atten PPS3203T-3S

| | |
|---|---|
| **Status** | supported |
| **Source code** | [atten-pps3xxx](https://github.com/OpenTraceLab/OpenTraceCapture/tree/main/src/hardware/atten-pps3xxx) |
| **Channels** | 3 |
| **Voltage/current (CH1)** | 0-32V / 0-3A |
| **Voltage/current (CH2)** | 0-32V / 0-3A |
| **Voltage/current (CH3)** | 0-6V / 0-3A |
| **Connectivity** | USB-serial, RS232 |
| **Website** | [atten.eu](http://www.atten.eu/atten-pps3203t-3s-programmable-power-supply.html) |

</div>

The **Atten PPS3203T-3S** is a 3-channel programmable power supply with USB-serial and RS232 connectivity.

See [Atten PPS3203T-3S/Info](https://sigrok.org/wiki/Atten_PPS3203T-3S/Info) for more details (such as **lsusb -v** output) about the device.

This device is also sold as the [Tenma 72-8795](http://www.newark.com/tenma/72-8795/programmable-dc-power-supply-32v/dp/32T0685) by Farnell/Newark.

See [Atten PPS3000 series](https://sigrok.org/wiki/Atten_PPS3000_series) for information common to all devices in this series.

## Quick start

The following command will set the voltage on channel #2 to 5.0V, current limit to 0.5A, and then will query the device in continuous mode:

```
$ **sigrok-cli --driver=atten-pps3203:conn=/dev/ttyUSB0 --channel-group=CH2 \**
  **--config "voltage_target=5:current_limit=0.5:enabled=on" --continuous**

```

## Photos

<div class="photo-grid" markdown>

[![Atten Pps3203t 3s](./img/Atten_PPS3203T-3S.jpg)](./img/Atten_PPS3203T-3S.png "Atten Pps3203t 3s"){ .glightbox data-gallery="atten-pps3203t-3s" }
<span class="caption">Atten Pps3203t 3s</span>

[![Atten Pps3203t 3s Back](./img/Atten_PPS3203T-3S_back.jpg)](./img/Atten_PPS3203T-3S_back.jpg "Atten Pps3203t 3s Back"){ .glightbox data-gallery="atten-pps3203t-3s" }
<span class="caption">Atten Pps3203t 3s Back</span>

</div>

