---
title: RDTech DPS series
---

# RDTech DPS series

<div class="infobox" markdown>

![RDTech DPS series](./img/Rdtech-dps.jpg){ .infobox-image }

### RDTech DPS series

| | |
|---|---|
| **Status** | supported |
| **Source code** | [rdtech-dps](https://github.com/OpenTraceLab/OpenTraceCapture/tree/main/src/hardware/rdtech-dps) |
| **Channels** | 1 |
| **Voltage/current (CH1)** | varies |
| **Connectivity** | serial over USB/Bluetooth |
| **Features** | programmable presets, values, output, over-(voltage,current,power) thresholds. |
| **Website** | [rdtech.aliexpress.com](http://rdtech.aliexpress.com/) |

</div>

**Please note: This page is a work in progress, more to come.**

HangZhou RuiDeng Technologies sells a range of low-cost programmable DC-DC switching PSU modules in either buck or buck/boost configuration. The communication versions are controllable via Modbus over a USB-Serial or Bluetooth connection.

## Hardware
| Model | Topology | Voltage | Current | Max Power |
|---|---|---|---|---|
| DPS3005 | Buck | 0-30V | 0-5A | 160W |
| DPS5005 | Buck | 0-50V | 0-5A | 250W |
| DPH5005 | Buck/Boost | 0-50V | 0-5A | 250W |
| DPS5015 | Buck | 0-50V | 0-15A | 750W |
| DPS5020 | Buck | 0-50V | 0-20A | 1000W |
| DPS8005 | Buck | 0-80V | 0-5.1A | 408W |

## Protocol

Modbus RTU ([Wikipedia](https://en.wikipedia.org/wiki/Modbus#Frame_formats)). Baudrate defaults to 9600 and can be changed by holding V/▲ at power on. The same menu allows configuring the Modbus slave address and the Bluetooth PIN.

External sources exist which combine communication to DPS as well as UM as well as RD devices in a single project. Protocols may be similar enough to make a common driver desirable.

## Manual Operation

The dial is used to change values, pressing the dial in changes the selected digit. Holding in for 3s toggles the keylock.

V/▲ selects the voltage target; holding for 3s selects the M1 preset.

A/▼ selects the current limit; holding for 3s selects the M2 preset.

SET brings up the settings menu; holding for 3s allows selecting any preset from M1-M9 using the dial.

The ON/OFF button switches the output on and off, not the unit itself.

When a preset is selected it is automatically copied into preset M0, which is the active configuration.

Settings menu allows configuring of the over-voltage, over-current and over-power protection thresholds as well as saving to presets M1-M9.
Arrows select option, dial button selects value and digit, SET exits option or menu.

### Status on power up

Can be configured with the S-INI option in the settings menu. Default is off. Selecting a preset will overwrite this value.
The ON/OFF setting in M-PRE determines the output state when the preset is selected. OFF will turn the output off, ON will maintain the current output state.

### Saving a preset

In the settings menu, set M-PRE to desired preset (M1-M9).
Change other options as desired. 
Return to the M-PRE setting (the value must be selected) and hold SET for 3s.
Do not exit the menu before this or the settings will be lost.

## Resources
- [https://www.mediafire.com/folder/3iogirsx1s0vp/DPS_communication_upper_computer](https://www.mediafire.com/folder/3iogirsx1s0vp/DPS_communication_upper_computer) Labview-based control software and protocol documents
- [OpenSource DPS firmware](https://github.com/kanflo/opendps)
- UM/RD/DPS serial device interface tool, [black-fx](https://github.com/Black-FX/rdserialtool) and [rfinnie](https://github.com/rfinnie/rdserialtool) repos
## See also
- [Programmable power supply](https://sigrok.org/wiki/Programmable_power_supply)
- [Power supply comparison](https://sigrok.org/wiki/Power_supply_comparison)

## Photos

<div class="photo-grid" markdown>

[![Rdtech Dps](./img/Rdtech-dps.jpg)](./img/Rdtech-dps.png "Rdtech Dps"){ .glightbox data-gallery="rdtech-dps-series" }
<span class="caption">Rdtech Dps</span>

</div>
