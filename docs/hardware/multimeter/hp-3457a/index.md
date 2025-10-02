---
title: HP 3457A
---

# HP 3457A

<div class="infobox" markdown>

![HP 3457A](./img/Hp_3457a_rev6_analog_section_riser_board.jpg){ .infobox-image }

### HP 3457A

| | |
|---|---|
| **Status** | supported |
| **Source code** | [hp-3457a](https://github.com/OpenTraceLab/OpenTraceCapture/tree/main/src/hardware/hp-3457a) |
| **Counts** | 30300000 |
| **IEC 61010-1** | 450V p-p max |
| **Connectivity** | GPIB |
| **Measurements** | voltage, current, resistance, frequency, period |
| **Features** | autorange, readings memory, four-wire resistance |
| **Website** | [keysight.com](http://www.keysight.com/en/pd-3457A%3Aepsg%3Apro-pn-3457A/digital-multimeter) |

</div>

The **Hewlett-Packard 3457A** is a 7.5 digits (30300000 counts) bench digital multimeter with GPIB connectivity.

## Hardware
- **Precision Subsurface Zener Voltage reference**: [Linear Technology LM399](http://cds.linear.com/docs/en/datasheet/199399fc.pdf)
- **Analog board microprocessor**: Intel 8051
- **Digital board microprocessor**: Motorola 6800
## Plug-in cards

The HP 3457A supports one plug-in card in the rear, which replaces the rear terminals. Two cards are supported by the device.

### Rear terminals

The rear terminals provide the same five-terminal measurement capability as the front panel terminals. The rear terminal block can be replaced by one of the following relay multiplexer cards.

### 44491A Armature Relay Multiplexer

This card supports 10 input channels. The last two channels are dedicated to current measurements while the other wight can be configured for either two-terminal measurements, or four-wire resistance measurements.

- 8 - voltage, 2-wire resistance channels
- 4 - four-wire resistance channels
- 2 - current channels
### 44492A Reed Relay Multiplexer

This card supports 10 channels, multiplexable to the voltage inputs. It supports voltage, two-wire resistance and frequency measurements.

## sigrok quirks
### Driver design goals and quirks

The driver is designed for accuracy and precision rather than throughput. As a result, it does not use the DMM's FIFO memory, but instead focuses on getting maximum precision from each measurement. When the integration time is set to 10 or 100 powerline cycles, the driver will automatically read the HIRES register, and add the result to the reading to get 7.5 digit measurements. This is handled transparently.

Only one measurement unit is supported, irrespective of the number of channels provided by expansion cards. This means that all channels will measure the same quantity.  Changing measurement type between channels is not supported. Another side-effect is that if a given channel does not support the current measurement quantity, the DMM will produce a measurement with open terminals.

Only the front or rear terminals, or expansion card may be selected at any given time. This is because certain firmware revisions do not like switching back and forth too fast between terminals.

Switching between channels is achieved using the scan-advance feature, using the SLIST and SADV commands. This method seems to work best on all tested hardware and firmware revisions of the 3457A. Manual channel switching generates a "Trig too fast" error that is only correctable with an upgrade of the primary processor board.

### Connecting and configuring the DMM

The HP3457A can only be accessed via GPIB. On linux, it will most likely be accessed with libgpib. The **conn** parameter will then be of the form "libgpib/<device_name>", where device_name is the **name** entry be specified in a gpib.conf device section.

The device supports a configurable ADC integration time based on the number of powerline cycles. This can be specified by using the **nplc** key. Since there is no way to query the measurement quantity, it should be specified before starting an acquisition, else the unit will not be reported. This is done via the **measured_quantity** key.

For example, to read two voltage samples from libgpib device hp3457a, with 10 powerline cycles integration time:

```
sigrok-cli --driver=hp-3457a:conn=libgpib/hp3457a \
  --samples 2 \
  --config "measured_quantity=voltage:nplc=10"

```

## Photos

<div class="photo-grid" markdown>

[![Hp 3457a Rev6 Analog Section Riser Board](./img/Hp_3457a_rev6_analog_section_riser_board.jpg)](./img/Hp_3457a_rev6_analog_section_riser_board.jpg "Hp 3457a Rev6 Analog Section Riser Board"){ .glightbox data-gallery="hp-3457a" }
<span class="caption">Hp 3457a Rev6 Analog Section Riser Board</span>

[![Hp 3457a Rev6 Relay Flyback Diodes](./img/Hp_3457a_rev6_relay_flyback_diodes.jpg)](./img/Hp_3457a_rev6_relay_flyback_diodes.jpg "Hp 3457a Rev6 Relay Flyback Diodes"){ .glightbox data-gallery="hp-3457a" }
<span class="caption">Hp 3457a Rev6 Relay Flyback Diodes</span>

[![Hp 3457a Rev6 Voltage Reference Board](./img/Hp_3457a_rev6_voltage_reference_board.jpg)](./img/Hp_3457a_rev6_voltage_reference_board.jpg "Hp 3457a Rev6 Voltage Reference Board"){ .glightbox data-gallery="hp-3457a" }
<span class="caption">Hp 3457a Rev6 Voltage Reference Board</span>

[![Hp 3457a Rev6 Lithium Nvram Battery](./img/Hp_3457a_rev6_lithium_nvram_battery.jpg)](./img/Hp_3457a_rev6_lithium_nvram_battery.jpg "Hp 3457a Rev6 Lithium Nvram Battery"){ .glightbox data-gallery="hp-3457a" }
<span class="caption">Hp 3457a Rev6 Lithium Nvram Battery</span>

[![Hp 3457a Rev6 Analog Section Overview](./img/Hp_3457a_rev6_analog_section_overview.jpg)](./img/Hp_3457a_rev6_analog_section_overview.jpg "Hp 3457a Rev6 Analog Section Overview"){ .glightbox data-gallery="hp-3457a" }
<span class="caption">Hp 3457a Rev6 Analog Section Overview</span>

[![Hp 3457a Rev6 Mains Input And Transformer](./img/Hp_3457a_rev6_mains_input_and_transformer.jpg)](./img/Hp_3457a_rev6_mains_input_and_transformer.jpg "Hp 3457a Rev6 Mains Input And Transformer"){ .glightbox data-gallery="hp-3457a" }
<span class="caption">Hp 3457a Rev6 Mains Input And Transformer</span>

[![Hp 3457a Sigrok Teaser](./img/HP_3457a_sigrok_teaser.jpg)](./img/HP_3457a_sigrok_teaser.png "Hp 3457a Sigrok Teaser"){ .glightbox data-gallery="hp-3457a" }
<span class="caption">Hp 3457a Sigrok Teaser</span>

[![Hp 3457a Rev6 Analog Section Relays](./img/Hp_3457a_rev6_analog_section_relays.jpg)](./img/Hp_3457a_rev6_analog_section_relays.jpg "Hp 3457a Rev6 Analog Section Relays"){ .glightbox data-gallery="hp-3457a" }
<span class="caption">Hp 3457a Rev6 Analog Section Relays</span>

[![Hp 3457a Rev6 Top Cover Removed](./img/Hp_3457a_rev6_top_cover_removed.jpg)](./img/Hp_3457a_rev6_top_cover_removed.jpg "Hp 3457a Rev6 Top Cover Removed"){ .glightbox data-gallery="hp-3457a" }
<span class="caption">Hp 3457a Rev6 Top Cover Removed</span>

</div>
#### Hardware Revision 6

		- 
			[](./img/Hp_3457a_rev6_top_cover_removed.jpg)

Device with the top cover removed. The analog section is hidden under two metal shields

		- 
			[](./img/Hp_3457a_rev6_analog_section_overview.jpg)

Overview of the analog section

		- 
			[](./img/Hp_3457a_rev6_analog_section_riser_board.jpg)

Analog section, riser board

		- 
			[](./img/Hp_3457a_rev6_voltage_reference_board.jpg)

Voltage reference board

		- 
			[](./img/Hp_3457a_rev6_analog_section_relays.jpg)

Analog section, relays

		- 
			[](./img/Hp_3457a_rev6_relay_flyback_diodes.jpg)

Flyback diodes for the relays are nicely lined up

		- 
			[](./img/Hp_3457a_rev6_mains_input_and_transformer.jpg)

Mains input and transformer

		- 
			[](./img/Hp_3457a_rev6_lithium_nvram_battery.jpg)

Digital section, lithium NVRAM baterry

More TODO.

Also see [EEVBlog's teardown pictures](https://www.flickr.com/photos/eevblog/sets/72157632803534496/).

## Resources
- [EEVBlog teardown of the 3457A](https://www.eevblog.com/2013/02/20/eevblog-426-hp-3457a-multimeter-teardown/)

