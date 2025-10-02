---
title: Voltcraft 18220
---

# Voltcraft 18220

<div class="infobox" markdown>

### Voltcraft 18220

| | |
|---|---|
| **Status** | planned |
| **Channels** | 1 |
| **Voltage/current (CH1)** | 0-40V / 0-5A |
| **Connectivity** | RS232 |
| **Features** | settable values, settable output. |

</div>

**Please note: This page is a work in progress, more to come.**

The Conrad *Voltcraft 18220* is a one-channel digitally-controlled laboratory power supply with RS-232 connectivity. It came onto the market in about 1996.
It was sold by Conrad Elektronik as article 512923.















## Hardware
- Output protection against reverse current: Max. 1 A!
## Photos

## Protocol

ASCII based.

## Manual Operation
### Status on power up

The output is disabled. Voltage and current are set to the value on previous power-off. A small negative (!) voltage can be measured while output is off.  

### Output Control
- On: Keep button *VOLT/AMPERE* pressed, press ▲.
- Off: Keep button *VOLT/AMPERE* pressed, press ▼.
### Voltage Control
- If LED *Volt* is not on, press button *VOLT/AMPERE*.
- Press ▲ to increase voltage by 50 mV.
- Press ▼ to decrease voltage by 50 mV.
### Current Control
- If LED *AMPERE* is not on, press button *VOLT/AMPERE*.
- Press ▲ to increase current limit by 100 mA.
- Press ▼ to decrease current limit by 100 mA.
- To display current current limit, shorten output externally.
## Remote Operation

The sigrok driver for this device will be named *voltcraft-18220*.

## Resources
- Manual (German) available from [Conrad Elektronik](http://www.conrad.de) via customer support.
- [http://software.freepage.de/hmueller/pilot/SNT/](http://software.freepage.de/hmueller/pilot/SNT/) Control software for PalmPilot
## See also
- [Programmable power supply](https://sigrok.org/wiki/Programmable_power_supply)
- [Power supply comparison](https://sigrok.org/wiki/Power_supply_comparison)

