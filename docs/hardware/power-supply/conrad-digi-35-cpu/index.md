---
title: Conrad DIGI 35 CPU
---

# Conrad DIGI 35 CPU

<div class="infobox" markdown>

![Conrad DIGI 35 CPU](./img/Conrad_digi_35_cpu_6.jpg){ .infobox-image }

### Conrad DIGI 35 CPU

| | |
|---|---|
| **Status** | supported |
| **Source code** | [conrad-digi-35-cpu](https://github.com/OpenTraceLab/OpenTraceCapture/tree/main/src/hardware/conrad-digi-35-cpu) |
| **Channels** | 1 |
| **Voltage/current (CH1)** | 0-35V / 0-2.55A |
| **Connectivity** | RS232 |
| **Features** | settable values, interval and timed power-off functionality |

</div>

The **Conrad DIGI 35 CPU** is a one-channel, digitally-controlled laboratory power supply with RS-232 connectivity. It came onto the market in 1992.

## Hardware
### ICs
- Motorola 68HC05C4 (CPU)
- DAC-0802L (2x)
- LM-336 Voltage Reference
- ...
### RS-232 interface

The RS-232 interface is equipped with a DB-9 socket in DTE configuration. It only receives data, but does not send any and uses no handshake lines.

Communication parameters 8n1, 9600 (power-on default), 4800, 2400 and 300 baud are supported.

To convert it to a more common DCE configuration, unplug and open the device and solder the RxD line from pin 2 of the DB-9 socket to pin 3.

## Photos

<div class="photo-grid" markdown>

[![Conrad Digi 35 Cpu 6](./img/Conrad_digi_35_cpu_6.jpg)](./img/Conrad_digi_35_cpu_6.jpg "Conrad Digi 35 Cpu 6"){ .glightbox data-gallery="conrad-digi-35-cpu" }
<span class="caption">Conrad Digi 35 Cpu 6</span>

[![Conrad Digi 35 Cpu 3](./img/Conrad_digi_35_cpu_3.jpg)](./img/Conrad_digi_35_cpu_3.jpg "Conrad Digi 35 Cpu 3"){ .glightbox data-gallery="conrad-digi-35-cpu" }
<span class="caption">Conrad Digi 35 Cpu 3</span>

[![Conrad Digi 35 Cpu 1](./img/Conrad_digi_35_cpu_1.jpg)](./img/Conrad_digi_35_cpu_1.jpg "Conrad Digi 35 Cpu 1"){ .glightbox data-gallery="conrad-digi-35-cpu" }
<span class="caption">Conrad Digi 35 Cpu 1</span>

[![Conrad Digi 35 Cpu 14](./img/Conrad_digi_35_cpu_14.jpg)](./img/Conrad_digi_35_cpu_14.jpg "Conrad Digi 35 Cpu 14"){ .glightbox data-gallery="conrad-digi-35-cpu" }
<span class="caption">Conrad Digi 35 Cpu 14</span>

[![Conrad Digi 35 Cpu 2](./img/Conrad_digi_35_cpu_2.jpg)](./img/Conrad_digi_35_cpu_2.jpg "Conrad Digi 35 Cpu 2"){ .glightbox data-gallery="conrad-digi-35-cpu" }
<span class="caption">Conrad Digi 35 Cpu 2</span>

[![Conrad Digi 35 Cpu Logo](./img/Conrad_digi_35_cpu_logo.jpg)](./img/Conrad_digi_35_cpu_logo.png "Conrad Digi 35 Cpu Logo"){ .glightbox data-gallery="conrad-digi-35-cpu" }
<span class="caption">Conrad Digi 35 Cpu Logo</span>

[![Conrad Digi 35 Cpu 5](./img/Conrad_digi_35_cpu_5.jpg)](./img/Conrad_digi_35_cpu_5.jpg "Conrad Digi 35 Cpu 5"){ .glightbox data-gallery="conrad-digi-35-cpu" }
<span class="caption">Conrad Digi 35 Cpu 5</span>

[![Conrad Digi 35 Cpu 7](./img/Conrad_digi_35_cpu_7.jpg)](./img/Conrad_digi_35_cpu_7.jpg "Conrad Digi 35 Cpu 7"){ .glightbox data-gallery="conrad-digi-35-cpu" }
<span class="caption">Conrad Digi 35 Cpu 7</span>

</div>
## Protocol

ASCII based.

| Vxxx <CR> | Set voltage to xx.x V or set special function. |
|---|---|
| Cxxx <CR> | Set current to x.xx A. |
| L <CR> | Lock keyboard. |
| E <CR> | Enable keyboard. |
| U <CR> | Increase voltage by 100 mV |
| D <CR> | Decrease voltage by 100 mV |

Special functions:

| 4xx | ??? Undocumented. Can be entered without error, but unknown meaning, if any. |
|---|---|
| 5xx | Set interval 01-99 seconds. The output is switched on and off in the interval. Use with care because of wear of relay! Set to 00 to disable. |
| 6xx | Set countdown to 01-99 hours. After countdown has expired, the output is disabled. Set to 00 to disable. |
| 7xx | Set countdown 01-99 minutes. Can be combined with 6xx. Set to 00 to disable. |
| 800 | Set baud rate to 300. |
| 801 | Set baud rate to 2400. |
| 802 | Set baud rate to 4800. |
| 803 | Set baud rate to 9600 (power-on default). |
| 900 | Set current mode to overcurrent protection (reaching current limit disables output). |
| 901 | Set current mode to constant current (reaching current limit lowers voltage; power-on default). |
| 902 | Lock keyboard (unlock via RS-232). |

Please note that there seems to be no way to enable the output by software.

## Manual operation
### Status on power-up

Voltage and current are set to 0. Both voltage and current must be set separately (see below) before the power supply puts out any power.

### Setting voltage (or special function)

U → <digit1> <digit2> <digit3> → U 

Output is disabled while setting. LED *CONST V* is on when output is enabled.

When output is enabled, the voltage can be increased or decreased in steps of 100 mV with the *UP/DOWN* button.

### Setting current

I → <digit1> <digit2> <digit3> → I 

Output is disabled while setting. Display shows set value after third digit.

## Remote operation

The sigrok driver for this device is named *conrad-digi-35-cpu*.

This device seems to be only partly remote controllable. Especially it seems not to be possible to enable the output remotely (if this is wrong, e.g. if you have the original software and it can remote control the output with it, please contact [Matthias](https://sigrok.org/wiki/User:Matthias_Heidbrink)). After the output has been enabled manually, voltage and current can be changed remotely.

Because the user can change the device settings at any time and the driver cannot query the device for the current state, the parameters can be set only, but not read.

| Function | Parameters | Comment |
|---|---|---|
| SR_CONF_VOLTAGE_TARGET | Double 0-35.0 |  |
| SR_CONF_CURRENT_LIMIT | Double 0-2.55 |  |
| SR_CONF_OVER_CURRENT_PROTECTION_ENABLED | Boolean on/off | When enabled, the device switches off the output when max. current is reached.When disabled, the device is in constant current mode and lowers the voltage when target current is reached. |

## Resources
- [Manual](http://www2.produktinfo.conrad.com/datenblaetter/500000-524999/512982-an-02-de-Programmierbares_Netzteil_DIGI_35_CPU.pdf) (German)
## See also
- [Programmable power supply](https://sigrok.org/wiki/Programmable_power_supply)
- [Power supply comparison](https://sigrok.org/wiki/Power_supply_comparison)

