---
title: Owon P4000 series
---

# Owon P4000 series

<div class="infobox" markdown>

![Owon P4000 series](./img/Owon_P4603.JPG){ .infobox-image }

### Owon P4000 series

| | |
|---|---|
| **Status** | supported |
| **Source code** | [scpi-pps](https://github.com/OpenTraceLab/OpenTraceCapture/tree/main/src/hardware/scpi-pps) |
| **Channels** | 1 |
| **Voltage/current (CH1)** | various |
| **Connectivity** | RS232 |
| **Features** | programmable presets, over voltage protection, over current protection, output on/off |
| **Website** | [owon.com.hk](https://www.owon.com.hk/) |

</div>

The **Owon P4000** series are 1 channel linear power supplies with RS232 connectivity.

The devices are also sold rebranded by Element14 Multicomp as MP710087.

| Device | OEM/Rebranded | Voltage range | Current range | Power |
|---|---|---|---|---|
| [Owon P4305](https://www.owon.com.hk/products_owon_p4000_series_1ch_liner_dc_power_supply) | [MP710086](https://au.element14.com/multicomp-pro/mp710086/dc-power-supply-1ch-30v-5a-150w/dp/322741901) | 0-30 V | 0-5 A | 150 W |
| [Owon P4603](https://www.owon.com.hk/products_owon_p4000_series_1ch_liner_dc_power_supply) | [MP710087](https://au.element14.com/multicomp-pro/mp710087/dc-power-supply-1ch-60v-3a-180w/dp/322742101) | 0-60 V | 0-3 A | 180 W |

## Protocol

The protocol is [SCPI over RS232](https://sigrok.org/wiki/Connection_parameters#Devices_using_SCPI). Manual available [here](http://files.owon.com.cn/software/Application/SP&P_Series_Single_Channel_DC_Power_Supply_Programming_Manual.pdf).

| Request | Example output | Remarks |
|---|---|---|
| *IDN? | OWON,P4603,2037363,FV:V1.6.0 | Get identification number |
| *RST |  | Reset to factory defaults |
| MEAS:VOLT? | 0.000 | Returns voltage present on output, 0.000 if output is turned off. |
| MEAS:CURR? | 0.000 | Returns current on output. |
| MEAS:POW? | 0.000 | Returns power in watts measured on output. |
| OUTP? | 0 or 1 | Query whether output is on. |
| OUTP 0/1 |  | Turn output on/off |
| CURR? | 1.000 | Returns the current limit setting. |
| CURR 1.000 |  | Sets the current limit |
| CURR:LIM? | 1.000 | Returns the overcurrent protection setting. |
| CURR:LIM 1.0 |  | Sets the overcurrent protection setting. |
| VOLT? | 1.000 | Returns the voltage setting. |
| VOLT 1.000 |  | Sets the output voltage |
| VOLT:LIM? | 1.000 | Returns the overvoltage protection setting. |
| VOLT:LIM 1.0 |  | Sets the overvoltage protection setting. |

## Resources
- [Manufacturer documents](https://www.owon.com.hk/products_owon_p4000_series_1ch_liner_dc_power_supply)
- [Teardown and review](https://www.eevblog.com/forum/testgear/inside-the-owon-p4603p4305-linear-psu/)
## See also
- [Programmable power supply](https://sigrok.org/wiki/Programmable_power_supply)
- [Power supply comparison](https://sigrok.org/wiki/Power_supply_comparison)

## Photos

<div class="photo-grid" markdown>

[![Owon P4603](./img/Owon_P4603.JPG)](./img/Owon_P4603.JPG "Owon P4603"){ .glightbox data-gallery="owon-p4000-series" }
<span class="caption">Owon P4603</span>

</div>
