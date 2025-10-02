---
title: Agilent U12xxx series
---

# Agilent U12xxx series

<div class="infobox" markdown>

### Agilent U12xxx series

| | |
|---|---|

</div>

The Agilent U12xxx series are handheld digital multimeters, ranging from inexpensive all-purpose meters to industrial meters.

| Model | Counts | Supported |
|---|---|---|
| U1231A | 6000 | Yes |
| [U1232A](https://sigrok.org/wiki/Agilent_U1232A) | 6000 | Yes |
| U1233A | 6000 | Yes |
| U1241A / U1241B | 10000 | Yes |
| U1241C | 10000 | Yes |
| U1242A / U1242B | 10000 | Yes |
| [U1242C](https://sigrok.org/wiki/Keysight_U1242C) | 10000 | Yes |
| U1251A / U1251B | 50000 | Yes |
| U1252A / U1252B | 50000 | Yes |
| U1253A / U1253B | 50000 | Yes |
| U1271A | 30000 | Yes |
| [U1272A](https://sigrok.org/wiki/Agilent_U1272A) | 30000 | Yes |
| U1273A | 30000 | Yes |
| U1273AX | 30000 | Yes |
| U1281A | 60000 | Yes |
| U1282A | 60000 | Yes |

Is your model not supported yet? Get in touch! We need people to help us test other models in this series, and getting a new model supported is generally quick & easy.










































## Connection

All models communicate via an optically isolated serial connection, usually at 9600 bps, 8 bits, no parity, and 1 stop bit (9600/8n1). Some models allow the user to change the serial parameters (e.g. the U1272A supports 9600/19200 baud, 7/8bits, parity odd/even/none).

Connecting to the devices can be done either via USB ([U1173A cable](https://sigrok.org/wiki/Device_cables#Agilent_U1173A) or [U1173B cable](https://sigrok.org/wiki/Device_cables#Agilent_U1173B)) or Bluetooth ([U1177A interface](https://sigrok.org/wiki/Device_cables#Agilent_U1177A)).

## Protocol

All models in this series use generally the same protocol, with only minor differences between models – and none within the same range.

The meters will respond to commands, which consist of a short ASCII string followed by either LF or CR+LF. The meter will either send no response at all, some ASCII text followed by CR+LF, or `*E` followed by CR+LF if the command given was invalid.

Some events (such as turning the rotary switch) will cause spontaneous transmissions of event notifiers. These consist of a `*` character, a single character and CR+LF.

### *IDN?

Sending the command `*IDN?` causes the device to return a comma-separated four-field string, compatible with the identical GPIB command. The four fields are vendor name, model name, serial number and version:

```
Agilent Technologies,U1232A,MY52020136,V1.00
Agilent Technologies,U1253B,MY5*xxxxxxx*,V2.26
Agilent Technologies,U1272A,MY5*xxxxxxx*,V2.04
Keysight Technologies,U1242C,MY5*xxxxxxx*,V1.20
Keysight Technologies,U1282A,MY5*xxxxxxx*,V1.03

```
### *RST

Sending the command `*RST` causes the device to reset. The response is an asterisk followed by the current dial position, for example `*1` indicates the first position.

### SYST:BATT?

The command `SYST:BATT?` returns a value indicating the device's battery level. The value is in a different format depending on the model series:

The U123xx, U124xC, U127xx and U128xx models return a percentage value, like this:

```
36%

```

The U124xx and U125xx models return a value like this:

```
+1.04200000E+02

```
### SYST:BEEP

The command `SYST:BEEP` or `SYST:BEEP TONE` makes the multimeter emit a beep.

### SYST:BLIT

The commands `SYST:BLIT 1` and `SYST:BLIT 0` turn the screen backlight on and off. There is no response. The backlight timer will still run and turn the backlight back off again if it is enabled.

The U127x devices don't seem to support this command.

### FETC?

The `FETC?` command returns the current measured value, as a floating point ASCII string, as in the following examples:

```
+9.25000000E-03
+0.00000000E+00
-1.01140000E+00
-9.10200000E-01

```

The sign characters are always present, and the value is always in normalized scientific format. This applies even when in a mode that uses integer numbers, 11 would be transmitted as `+1.10000000E+01`. If no valid measurement is available, i.e. the display shows "OL" or "-OL", the transmitted value is either `+9.90000000E+37` and `-9.90000000E+37` respectively.

For models with dual display, the `FETC? @2` command returns the current value from the secondary display, in the same format.

### CONF:

The `CONF:` commands can be used to change modes and ranges on the multimeter. It is not to be confused with the `CONF?` query described below.

For a given rotary switch position, only those CONF: commands work that switch to modes that can be reached by pressing the range or shift buttons.

#### U123xx models
| Command | Rotary Switch Setting | Meaning |
|---|---|---|
| `CONF:VOLT:AC` | Any voltage mode | Switch to Volts AC mode with autoranging |
| `CONF:VOLT:DC` | Any voltage mode | Switch to Volts DC mode with autoranging |
| `CONF:VOLT:AC 600` | Any voltage mode | Switch to Volts AC mode and 600V range. Valid ranges are: 600, 60, 6, 0.6 |
| `CONF:VOLT:AC 600` | Any voltage mode | Switch to Volts AC mode and 600V range. Valid ranges are: 600, 60, 6, 0.6 |
| `CONF:CURR:AC` | Any current mode | Switch to AC current measurement mode with autoranging |
| `CONF:CURR:DC` | Any current mode | Switch to DC current measurement mode with autoranging |
| `CONF:CURR:AC 60u` | Any current mode | Switch to AC current measurement mode and 60uA range. Valid ranges are 10, 6 for A mode, and 600u, 60u for uA mode. |
| `CONF:CURR:DC 60u` | Any current mode | Switch to DC current measurement mode and 60uA range. Valid ranges are 10, 6 for A mode, and 600u, 60u for uA mode. |
| `CONF:FREQ` | VZlow, AC voltage or any current mode | Switch to frequency measurement mode. No manual ranges are available. |
| `CONF:CONT` | Resistance | Switch to continuity mode. |
| `CONF:RES` | Resistance | Switch to resistance mode with autoranging. |
| `CONF:RES 6M` | Resistance | Switch to resistance mode and 6MΩ range. Valid ranges are 60M, 6M, 600k, 60k 6k, 600 |
| `CONF:CAP` | Capacitance | Switch to capacitance mode with autoranging. |
| `CONF:CAP 1000n` | Capacitance | Switch to capacitance mode and 1000nF range. Valid ranges are: 10m, 1000u, 100u, 10u, 1000n |

#### U124xx/U125xx models

Same as above for the U123xx, except for different ranges.

### CONF?

The `CONF?` command queries the device's current measurement configuration.

#### U123xx models

This can be either one, two or three comma-separated fields. The number of fields depends on the first field's value, but the second field always denotes the measurement mode's range and resolution, and the third field is the current type (AC or DC). For example, this indicates AC voltage in the 600mV range:

```
V,0,AC

```
| Mode | Resolution | Current | Meaning |
|---|---|---|---|
| V | y | y | **Volts** |
|  | 0 |  | Range 600mV, resolution 0.1mV |
|  | 1 |  | Range 6V, resolution 1mV |
|  | 2 |  | Range 60V, resolution 0.01V |
|  | 3 |  | Range 600V, resolution 0.1V |
| MV | y | y | **Millivolts** |
|  | 1 |  | Range 600mV, resolution 0.1mV |
| A | y | y | **Ampere** |
|  | 0 |  | Range 6A, resolution 1mA |
|  | 1 |  | Range 10A, resolution 0.01A |
| UA | y | y | **Microampere** |
|  | 0 |  | Range 60μA, resolution 0.01μA |
|  | 1 |  | Range 600μA, resolution 0.1μA |
| FREQ | y | y | **AC frequency** |
|  | 0 |  | Range 99.9 Hz, resolution 0.01 Hz |
|  | 1 |  | Range 999.9 Hz, resolution 0.1 Hz |
|  | 2 |  | Range 9.999 kHz, resolution 1 Hz |
|  | 3 |  | Range 99.99 kHz, resolution 10 Hz |
|  | 4 |  | Range 200 kHz, resolution 100 Hz |
| RES | y | n | **Resistance** |
|  | 0 |  | Range 600Ω, resolution 0.1Ω |
|  | 1 |  | Range 6kΩ, resolution 0.001kΩ |
|  | 2 |  | Range 60kΩ, resolution 0.01kΩ |
|  | 3 |  | Range 600kΩ, resolution 0.1kΩ |
|  | 4 |  | Range 6MΩ, resolution 0.001MΩ |
|  | 5 |  | Range 60MΩ, resolution 0.01MΩ |
| CAP | y | n | **Capacitance** |
|  | 0 |  | Range 1000nF, resolution 1nF |
|  | 1 |  | Range 10μF, resolution 0.01μF |
|  | 2 |  | Range 100μF, resolution 0.1μF |
|  | 3 |  | Range 1000μF, resolution 1μF |
|  | 4 |  | Range 10mF, resolution 0.01mF |
| DIOD | n | n | **Diode** |

#### U124xx and U125xx models

The output consists of a quoted string with the meter's mode, followed by a space, two values, separated by a comma, denoting the current range, and the value of one count. The mode may optionally include a colon followed by a code denoting a submode relevant to that major mode.
For example, AC voltage mode with 1000mV range on a 10000-count U1241B would be given as:

```
"VOLT:AC +1.000000E+00,+1.000000E-04"

```
| Mode | Meaning |
|---|---|
| `VOLT` | DC voltage |
| `VOLT:AC` | AC voltage |
| `CURR` | DC current |
| `CURR:AC` | AC current |
| `FREQ` | Frequency counter |
| `DIOD` | Diode check. No range values are given. |
| `CONT` | Continuity. No range values are given. |
| `RES` | Resistance |
| `CAP` | Capacitance |
| `SCOU` | Switch counter. No range values are given. |
| `CPER:0-20mA` | Current loop, 0-20mA setting |
| `CPER:4-20mA` | Current loop, 4-20mA setting |
| `T1:K` or `T2:K` | Temperature on T1 or T2, submode can be K or J, denoting the thermocouple type. Instead of range values, `CEL` or `FAR` is given, denoting the measurement is in degrees Celsius or Fahrenheit. The full response might thus be: `"T1:K CEL"`. |

#### U124xC

The output is very similar to the U124xx and U125xx models with a few differences and additions.

| Mode | Meaning |
|---|---|
| `VOLT` | DC voltage |
| `VOLT:AC` | AC voltage |
| `VOLT:HRAT` | Harmonic Ratio |
| `CURR` | DC current |
| `CURR:AC` | AC current |
| `FREQ` `FREQ:AC` | Frequency |
| `DIOD` | Diode check. No range values are given. |
| `CONT` | Continuity |
| `RES` | Resistance |
| `CAP` | Capacitance |
| `CPER:0-20mA` | Current loop, 0-20mA setting |
| `CPER:4-20mA` | Current loop, 4-20mA setting |
| `TEMP` | Internal temperature. No range values are given. |
| `TEMP:K` | Temperature, submode can be K or J, denoting the thermocouple type. Instead of range values, `CEL` or `FAR` is given, denoting the measurement is in degrees Celsius or Fahrenheit. The full response might thus be: `"TEMP:K CEL"`. |
| `NCV` | Vsense (Non-contact Voltage). Instead of range values, `HI` or `LO` is given, denoting High sensivity or Low sensivity. The full response might thus be: `"NCV HI"`. |

#### U128xx

The output is very similar to the U124xC model with a few additions.

| Mode | Meaning |
|---|---|
| `VOLT` | DC voltage |
| `VOLT:AC` | AC voltage |
| `VOLT:ACDC` | AC+DC voltage |
| `CURR` | DC current |
| `CURR:AC` | AC current |
| `CURR:ACDC` | AC+DC current |
| `FREQ` `FREQ:AC` | Frequency |
| `PULS:PWID` `PULS:PWID:AC` | Pulse width |
| `PULS:PDUT` | Duty cycle. No range values are given. |
| `FC1` | Frequency counter (0.5 Hz to 10 MHz) |
| `FC100` | Frequency counter (1 MHz to 100 MHz) |
| `DIOD` | Diode check. No range values are given. |
| `CONT` | Continuity |
| `RES` | Resistance |
| `COND` | Conductance |
| `CAP` | Capacitance |
| `CPER:0-20mA` | Current loop, 0-20mA setting |
| `CPER:4-20mA` | Current loop, 4-20mA setting |
| `TEMP` | Internal temperature. No range values are given. |
| `TEMP:K` | Temperature, submode can be K or J, denoting the thermocouple type. Instead of range values, `CEL` or `FAR` is given, denoting the measurement is in degrees Celsius or Fahrenheit. The full response might thus be: `"TEMP:K CEL"`. |
| `SQU` | Square wave output. No range values are given. |
| `NCV` | Vsense (Non-contact Voltage). Instead of range values, `HIGH` or `LOW` is given, denoting High sensivity or Low sensivity. The full response might thus be: `"NCV HIGH"`. |

### STAT?

The `STAT?` command is used to query the current state of the device. The response is a quoted 21-byte string, like this:

```
"000000000110L00000000"

```
#### U123xx models
| Byte | Value | Meaning |
|---|---|---|
| 1 |  | **Max/min/avg mode** |
|  | 0 | Off |
|  | 1 | On |
| 2 |  | **Relative measurement**. The last value returned from FETC? before this mode was enabled denotes the stored reference value. |
|  | 0 | Off |
|  | 1 | On |
| 3 |  | **Trig hold-log** |
|  | 0 | Off |
|  | 1 | On |
| 4 |  | **Auto hold-log** |
|  | 0 | Off |
|  | 1 | On |
| 5 |  | **LED flashlight** |
|  | 0 | Off |
|  | 1 | On |
| 6 |  | **LCD backlight** |
|  | 0 | Off |
|  | 1 | On |
| 7 |  | **Smoothing** |
|  | 0 | Off |
|  | 1 | On |
| 8 |  | **Temp/aux mode**. When on and rotary switch is in position 5 (capacitance), CONF? returns `MV,1,DC`, but the value returned from FETC? instead denotes the temperature, in the unit (F or C) according to the meter's configuration. |
|  | 0 | Off |
|  | 1 | On |
| 9 |  | *Unknown (always 0)* |
| 10 |  | **Beep frequency** |
|  | 0 | 4.2kHz |
|  | 1 | 3.8kHz (default) |
|  | 2 | 3.4kHz |
|  | 3 | 3.2kHz |
|  | 4 | Off |
| 11 |  | **Auto power-off** (APO) |
|  | 0 | Off |
|  | 1 | On |
| 12 |  | *Unknown (always 0)* |
| 13 |  | *Unknown (always L)* |
| 14-15 |  | *Unknown (always 0)* |
| 16 |  | **Rotary switch position** |
|  | 0 | V/Zlow |
|  | 1 | Voltage AC |
|  | 2 | Voltage DC |
|  | 3 | Resistance |
|  | 4 | Diode |
|  | 5 | Capacitance |
|  | 6 | Current |
|  | 7 | Microcurrent |
| 17 |  | **Continuity mode**. When enabled, the value returned from FETC? is either NAN (no continuity) or any real value to denote continuity. |
|  | 0 | Off |
|  | 1 | On |
| 18 |  | *Unknown (always 0)* |
| 19 |  | **Battery low indicator** |
|  | 0 | Battery OK |
|  | 1 | Battery low |
| 20-21 |  | *Unknown (always 0)* |

#### U124xx models
| Byte | Value | Meaning |
|---|---|---|
| 1 |  | **Max/min/avg mode** |
|  | 0 | Off |
|  | 1 | On |
| 2 |  | **Relative measurement**. The last value returned from FETC? before this mode was enabled denotes the stored reference value. |
|  | 0 | Off |
|  | 1 | On |
| 3 |  | *Unknown* |
| 4 |  | *Unknown* |
| 5 |  | *Unknown* |
| 6 |  | **Current loop mode** |
|  | 0 | 0-20mA mode |
|  | 1 | 4-20mA mode |
| 7 |  | *Unknown (always I)* |
| 8 |  | **Hold mode**. |
|  | 0 | Off |
|  | 1 | On |
| 9 |  | *Unknown* |
| 10 |  | **Beep frequency** |
|  | 0 | Off (no beeps) |
|  | C | 300Hz |
|  | F | 600Hz |
|  | 1 | 1200Hz |
|  | 2 | 2400Hz |
| 11 |  | **Auto power-off** (APO) |
|  | 0 | Off |
|  | 1 | On |
| 12 |  | **LCD backlight** |
|  | 0 | Off |
|  | 1 | On |
| 13 |  | *Unknown (always L)* |
| 14 |  | *Unknown* |
| 15 |  | *Unknown* |
| 16 |  | **Rotary switch position** |
|  | 0 | Voltage |
|  | 1 | Diode |
|  | 2 | Resistance |
|  | 3 | Capacitance |
|  | 4 | uA |
|  | 5 | mA |
|  | 6 | A |
|  | 7 | Temperature |
| 17 |  | *Unknown* |
| 18 |  | *Unknown (always 1)* |
| 19 |  | *Unknown* |
| 20 |  | **Switch counter mode** |
|  | 0 | increase count on rising flank (initially low) |
|  | 1 | increase count on falling flank (initially high) |
| 21 |  | **Auto range** |
|  | 0 | Off |
|  | 1 | On |

#### U124xC models
| Byte | Value | Meaning |
|---|---|---|
| 1 |  | **Max/min/avg/maxminavg mode** |
|  | 0 | Off |
|  | 1 | On |
| 2 |  | **Relative measurement**. The last value returned from FETC? before this mode was enabled denotes the stored reference value. |
|  | 0 | Off |
|  | 1 | On |
| 3 |  | **Flashlight** |
|  | 0 | Off |
|  | 1 | On |
| 4 |  | **Probe socket connexion alert** |
|  | 0 | Off |
|  | 1 | On |
| 5 |  | *Unknown* |
| 6 |  | *Unknown* |
| 7 |  | **Smooth mode** |
|  | 0 | Off |
|  | 1 | On |
| 8 |  | **Trigger Hold** |
|  | 0 | Off |
|  | 1 | On |
| 9 |  | **0°C Temperature compensation** |
|  | 0 | Off |
|  | 1 | On |
| 10 |  | **Beep frequency** |
|  | 0 | Off (no beeps) |
|  | 1 | 3200 Hz |
|  | 2 | 3268 Hz |
|  | 3 | 3339 Hz |
|  | 4 | 3413 Hz |
|  | 5 | 3491 Hz |
|  | 6 | 4572 Hz |
|  | 7 | 3657 Hz |
|  | 8 | 3746 Hz |
|  | 9 | 3840 Hz |
|  | A | 3938 Hz |
|  | B | 4042 Hz |
|  | C | 4151 Hz |
|  | D | 4267 Hz |
| 11 |  | **Auto power-off status** |
|  | 0 | Off |
|  | 1 | On |
| 12 |  | **Auto Hold** |
|  | 0 | Off |
|  | 1 | On |
| 13 |  | **Meter mode** |
|  | L | Normal |
|  | C | Calibration |
| 14 |  | *Unknown* |
| 15 |  | *Reserved* |
| 16 |  | **Rotary switch position** |
|  | 0 | Zlow Voltage AC / DC (V) |
|  | 1 | Voltage AC (V) / H% |
|  | 2 | Voltage DC (V) |
|  | 3 | Resistance / continuity |
|  | 4 | Diode / capacitance |
|  | 5 | Current DC / AC (µA/mA) |
|  | 6 | Current DC / AC (A) |
|  | 7 | Temperature |
| 17 |  | **Battery type** |
|  | 0 | Primary |
|  | 1 | Secondary (rechargeable) |
| 18 |  | **Battery low or Current percent** |
|  | 0 | Off |
|  | 1 | Battery low or 4-20 mA mode |
|  | 2 | 0-20 mA mode and not Battery low |
| 19 |  | *Unknown* |
| 20 |  | *Unknown* |
| 21 |  | **DC filter (LPF)** |
|  | 0 | Off |
|  | 1 | On |

#### U125xx models
| Byte | Value | Meaning |
|---|---|---|
| 1 |  | **Max/min/avg mode** |
|  | 0 | Off |
|  | 1 | On |
| 2 |  | **Relative measurement**. The last value returned from FETC? before this mode was enabled denotes the stored reference value. |
|  | 0 | Off |
|  | 1 | On |
| 3 |  | **dB mode** |
|  | 0 | Off |
|  | m | dBm |
|  | V | dBV |
| 4 |  | *Unknown* |
| 5 |  | **Peak hold mode** |
|  | 0 | Off |
|  | 1 | On |
| 6 |  | **Current percent** |
|  | 0 | 0-20mA |
|  | 1 | 4-20mA |
| 7 |  | *Triggerhold I/B&#160;?* |
| 8 |  | **Triggered hold mode**. |
|  | 0 | Off |
|  | 1 | On |
| 9 |  | *Zero temperature compensation?* |
| 10 |  | *Beep selection&#160;?* |
| 11 |  | **Auto power-off** (APO) |
|  | 0 | Off |
|  | 1 | On |
| 12 |  | **LCD backlight** |
|  | 0 | Off |
|  | 1 | On |
| 13 |  | *Unknown (always L)* |
| 14 |  | *Unknown (always 0)* |
| 15 |  | *Unknown* |
| 16 |  | *Rotary position&#160;?* |
| 17 |  | *Output status active/standby&#160;?* |
| 18 |  | *Unknown* |
| 19 |  | **Battery low indicator** |
|  | 0 | Battery OK |
|  | 1 | Battery low |
| 20 |  | **Frequency counter prescaler** |
|  | 0 | No prescaling |
|  | 1 | Divide by 100 |
| 21 |  | **Auto range** |
|  | 0 | Manual range |
|  | 1 | Auto range |

#### U127xx models
| Byte | Value | Meaning |
|---|---|---|
| 1 |  | **Max/min/avg/maxminavg mode** |
|  | 0 | Off |
|  | 1 | On |
| 2 |  | **Relative measurement**. The last value returned from FETC? before this mode was enabled denotes the stored reference value. |
|  | 0 | Off |
|  | 1 | On |
| 3 |  | *Unknown* |
| 4 |  | *Unknown* |
| 5 |  | *Unknown* |
| 6 |  | *Unknown* |
| 7 |  | *Unknown* |
| 8 |  | *Unknown* |
| 9 |  | *Unknown* |
| 10 |  | **Beep frequency** |
|  | 0 | Off (no beeps) |
|  | 1 | 3200Hz |
|  | 2 | 3491Hz |
|  | 3 | 3840Hz |
|  | 4 | 4267Hz |
| 11 |  | *Unknown* |
| 12 |  | *Unknown* |
| 13 |  | *Unknown (always L)* |
| 14 |  | *Unknown* |
| 15 |  | *Unknown* |
| 16 |  | **Rotary switch position** |
|  | 0 | Zlow, V AC/DC |
|  | 1 | *N/A (this is the "OFF" position)* |
|  | 2 | Voltage AC (V) / LPF |
|  | 3 | Voltage AC (mV) / LPF |
|  | 4 | Voltage DC / AC (V) |
|  | 5 | Voltage DC / AC (mV) |
|  | 6 | Resistance / "smart resistance" / continuity |
|  | 7 | Diode / Auto |
|  | 8 | Capacitance / temperature |
|  | 9 | Current DC / AC (mA/A) |
|  | A | Current DC / AC (µA)**Note:** This is "A" in the "STAT?" reply, but "*10" in the event notifiers (see below). |
| 17 |  | **Continuity mode**. When enabled, the value returned from FETC? is either NAN (no continuity) or any real value to denote continuity. |
|  | 0 | Off |
|  | 1 | On |
| 18 |  | **Smart Ohm mode** ("O'Comp" icon active on the display). |
|  | 0 | Off |
|  | 1 | On |
| 19 |  | *Unknown* |
| 20 |  | **LPF** |
|  | 0 | Off |
|  | 1 | On |
| 21 |  | **DC filter** |
|  | 0 | Off |
|  | 1 | On |

#### U128xx models
| Byte | Value | Meaning |
|---|---|---|
| 1 |  | **Max/min/avg/maxminavg mode** |
|  | 0 | Off |
|  | 1 | On |
| 2 |  | **Relative measurement**. The last value returned from FETC? before this mode was enabled denotes the stored reference value. |
|  | 0 | Off |
|  | 1 | On |
| 3 |  | **dB function** |
|  | 0 | Off |
|  | M | dBm |
|  | V | dBV |
| 4 |  | **Probe socket connexion alert** |
|  | 0 | Off |
|  | 1 | On |
| 5 |  | **Peak-hold** |
|  | 0 | Off |
|  | 1 | On |
| 6 |  | **Current percent** |
|  | 0 | Off |
|  | 1 | 4-20 mA |
|  | 2 | 0-20 mA |
| 7 |  | **Pulse width and duty cycle trigger level** |
|  | 0 | Negative |
|  | 1 | Positive |
| 8 |  | **Trigger Hold** |
|  | 0 | Off |
|  | 1 | On |
| 9 |  | **0°C Temperature compensation** |
|  | 0 | Off |
|  | 1 | On |
| 10 |  | **Beep frequency** |
|  | 0 | Off (no beeps) |
|  | 1 | 3200 Hz |
|  | 2 | 3268 Hz |
|  | 3 | 3339 Hz |
|  | 4 | 3413 Hz |
|  | 5 | 3491 Hz |
|  | 6 | 4572 Hz |
|  | 7 | 3657 Hz |
|  | 8 | 3746 Hz |
|  | 9 | 3840 Hz |
|  | A | 3938 Hz |
|  | B | 4042 Hz |
|  | C | 4151 Hz |
|  | D | 4267 Hz |
| 11 |  | **Auto power-off status** |
|  | 0 | Off |
|  | 1 | On |
| 12 |  | **Auto Hold** |
|  | 0 | Off |
|  | 1 | On |
| 13 |  | **Meter mode** |
|  | L | Normal |
|  | C | Calibration |
| 14 |  | **Voltage alert** |
|  | 0 | Off |
|  | 1 | On |
| 15 |  | *Reserved* |
| 16 |  | **Rotary switch position** |
|  | 0 | Voltage AC (V) / LPF |
|  | 1 | Voltage AC (mV) / LPF |
|  | 2 | Voltage DC / AC (V) |
|  | 3 | Voltage DC / AC (mV) |
|  | 4 | Resistance / continuity / conductance |
|  | 5 | Diode / frequency counter |
|  | 6 | Capacitance / temperature |
|  | 7 | Current DC / AC (µA/mA) |
|  | 8 | Current DC / AC (A) |
|  | 9 | Square wave output |
| 17 |  | **Battery type** |
|  | 0 | Primary |
|  | 1 | Secondary (rechargeable) |
| 18 |  | **Battery low** |
|  | 0 | Off |
|  | 1 | On |
| 19 |  | **Resolution** |
|  | 0 | 5 digits |
|  | 1 | 4 digits |
| 20 |  | **LPF** |
|  | 0 | Off |
|  | 1 | On |
| 21 |  | **DC filter** |
|  | 0 | Off |
|  | 1 | On |

### LOG:

Different commands can be used to retrieve the content of the different log memories from the multimeter. Those commands allow to retrieve log entries one by one, specifying the index of the entry to retrieve each time. When the index is greater than the index of the last logged value, the multimeter will return an error (`*E`). The actual commands depends on the model.

The response is presented as a quoted string whose length depends on the model.

Note that each log entry is also emitted by the multimeter whenever a new value is captured to the log.

#### U123xx models

The valid commands to retrieve log entries are yet to be determined.

Log entries are 15 characters long. Here is an example of log entry:

```
"050000210000200"

```

Note that the position of the decimal point is not explicitly given, it must be discerned from the range.

| Byte | Value | Meaning |
|---|---|---|
| 1 |  | *Unknown (always 0)* |
| 2 |  | **Function** |
|  | 0 | AUX |
|  | 1 | Voltage |
|  | 2 | Microcurrent |
|  | 4 | Current |
|  | 5 | Resistance or continuity |
|  | 6 | Diode |
|  | 8 | Capacitance |
|  | 9 | Frequency |
| 3 |  | *Unknown (always 0)* |
| 4 |  | **First (most significant) digit of measurement** |
| 5 |  | **Second digit of measurement** |
| 6 |  | **Third digit of measurement** |
| 7 |  | **Fourth (least significant) digit of measurement** |
| 8 |  | **Mode bits** (several can be set at once) |
|  | 1 | Autoranging is enabled |
|  | 2 | Value is negative |
| 9 |  | **Mode bits** (several can be set at once) |
|  | 1 | DC |
|  | 2 | AC |
|  | 4 | Overload |
| 10 |  | **Range**, values are the same as with `CONF?` |
| 11 |  | *Unknown (always 0)* |
| 12 |  | **Temperature unit (probably)** |
|  | 0 | not in temperature mode |
|  | 1 | degrees Fahrenheit (not confirmed, need to check) |
|  | 2 | degrees Celsius |
| 13 |  | **Mode bits** (several can be set at once) |
|  | 1 | Relative mode is enabled |
|  | 2 | Trig Hold-Log mode is enabled |
|  | 4 | Auto Hold-Log mode is enabled |
| 14 |  | **Capacitance/AUX mode** |
|  | 0 | Capacitance |
|  | 1 | AUX temperature (mV setting in menu is off) |
|  | 2 | AUX mV (mV setting in menu is on) |
| 15 |  | *Unknown (always 0)* |

#### U124xC models

The valid commands to retrieve log entries are:

```
LOG:HAND <index>
LOG:TRIG <index>
LOG:AUTO <index>
LOG:EXPO <index>

```

Log entries are 14 characters long. Here is an example of log entry:

```
"01000241100100"

```

Note that the position of the decimal point is not explicitly given, it must be discerned from the active function and exponent.

| Byte | Value | Meaning |
|---|---|---|
| 1-2 |  | **Function** |
|  | 0 | Millivoltage |
|  | 1 | Voltage (averaging sense if Alternative unit flag and AC mode) |
|  | 2 | Microcurrent (averaging sense if Alternative unit flag and AC mode) |
|  | 3 | Current (averaging sense if Alternative unit flag and AC mode) |
|  | 4 | Resistance (Continuity if Alternative unit flag) |
|  | 5 | Diode |
|  | 6 | Temperature in °C (or °F if Alternative unit flag) |
|  | 7 | Capacitance |
|  | 8 | Frequency |
|  | 9 | Harmonic ratio |
|  | 10 | %Scale of 4-20 mA (or 0-20 mA if Alternative unit flag) |
| 3 |  | **First (most significant) digit of measurement** |
| 4 |  | **Second digit of measurement** |
| 5 |  | **Third digit of measurement** |
| 6 |  | **Fourth digit of measurement** |
| 7 |  | **Fifth (least significant) digit of measurement** |
| 8 |  | **Mode bits** (several can be set at once) |
|  | 1 | Autoranging is enabled |
|  | 2 | Value is negative |
| 9 |  | **Mode bits** (several can be set at once) |
|  | 1 | DC |
|  | 2 | AC |
|  | 4 | Overload |
| 10 |  | **Exponent** |
| 11 |  | **Mode bits (several can be set at once)** |
|  | 1 | Alternate unit flag |
|  | 2 | Thermocouple type (0 = K, 1 = J) |
|  | 4 | Zero temperature compensation |
| 12 |  | **Hold mode** |
|  | 1 | Trig-Hold mode |
|  | 3 | Auto-Hold mode |
|  | 4 | Relative mode is enabled (can be combined with *-Hold mode) |
| 13 |  | **Mode bits** (several can be set at once) |
|  | 1 | Average |
|  | 2 | Min |
|  | 4 | Max |
| 14 |  | **Data logging option** |
|  | 0 | Manual Log (Hand) |
|  | 1 | Interval Log (Auto) |
|  | 2 | Event Log (Trig) |
|  | 3 | Export Log (Hold button) |

Default exponent to be applied to the value for the different functions, in addition to the Exponent field.

| Exponent | Function |
|---|---|
| 10e-5 | Millivoltage |
| 10e-4 | Voltage |
| 10e-7 | Microcurrent |
| 10e-3 | Current |
| 10e-2 | Resistance / Continuity |
| 10e-3 | Diode |
| 10e-1 | Temperature (both °C and °F) |
| 10e-10 | Capacitance |
| 10e-2 | Frequency |
| 10e-2 | Harmonic ratio |
| 10e-2 | %Scale of 4-20 mA / 0-20 mA |

#### U125xx models

The valid commands to retrieve log entries are:

```
LOG? H<index>
LOG? A<index>

```

Note that <index> must be exactly 3 digits

Log entries are 13 characters long. Here is an example of log entry:

```
"0522041404000"

```

Note that the position of the decimal point is not explicitly given, it must be discerned from the active function and exponent.

| Byte | Value | Meaning |
|---|---|---|
| 1-2 |  | **Function** |
|  | 0 | Millivoltage |
|  | 1 | Voltage |
|  | 2 | *Unknown* |
|  | 3 | Current |
|  | 4 | *Unknown* |
|  | 5 | Resistance (Continuity if Alternative unit flag&#160;?, Conductance if Locked / Manual ranging) |
|  | 6 | Diode |
|  | 7 | Temperature in °C (or °F if Alternative unit flag) |
|  | 8 | Capacitance |
|  | 9 | Frequency |
|  | 10 | Duty cycle |
|  | 11 | Pulse width |
|  | 12 | *Unknown* |
|  | 13 | dBm (or dBV if Alternative unit flag) |
|  | 14 | %Scale of 4-20 mA (or 0-20 mA if Alternative unit flag) |
| 3 |  | **First (most significant) digit of measurement** |
| 4 |  | **Second digit of measurement** |
| 5 |  | **Third digit of measurement** |
| 6 |  | **Fourth digit of measurement** |
| 7 |  | **Fifth (least significant) digit of measurement** |
| 8 |  | **Mode bits** (several can be set at once) |
|  | 1 | Locked&#160;? Manual ranging is enabled&#160;? |
|  | 2 | Value is negative |
| 9 |  | **Mode bits** (several can be set at once) |
|  | 1 | DC |
|  | 2 | AC |
|  | 4 | Overload |
| 10 |  | **Exponent** |
| 11 |  | **Mode bits (several can be set at once)** |
|  | 1 | Alternate unit flag |
|  | 2 | Thermocouple type (0 = K, 1 = J) |
|  | 4 | Environment temperature compensation&#160;? |
| 12 |  | **Hold mode** |
|  | 1 | Trig-Hold mode&#160;? |
|  | 2 | Peak-Hold mode&#160;? |
|  | 3 | Auto-hold mode&#160;? |
|  | 4 | Relative mode is enabled (can be combined with *-Hold mode) |
| 13 |  | **Mode bits** (several can be set at once) |
|  | 1 | Average |
|  | 2 | Min |
|  | 4 | Max |
|  | 8 | "press"&#160;? |

Default exponent to be applied to the value for the different functions, in addition to the Exponent field.

| Exponent | Function |
|---|---|
| 10-7 | Millivoltage |
| 10-5 | Voltage |
| 10-7 | Current |
| 10-3 | Resistance / Continuity |
| 10-19 | Conductance |
| 10-5 | Diode |
| 10-2 | Temperature |
| 10-13 | Capacitance |
| 10-3 | Frequency |
| 10-5 | Duty cycle |
| 10-5 | Pulse width |
| 10-3 | dBm / dBV |
| 10-3 | %Scale of 4-20 mA / 0-20 mA |

#### U128xx models

The valid commands to retrieve log entries are:

```
LOG:HAND <index>
LOG:TRIG <index>
LOG:AUTO <index>
LOG:EXPO <index>

```

Log entries are 14 characters long. Here is an example of log entry:

```
"04235201470002"

```

Note that the position of the decimal point is not explicitly given, it must be discerned from the active function and exponent.

| Byte | Value | Meaning |
|---|---|---|
| 1-2 |  | **Function** |
|  | 0 | Millivoltage |
|  | 1 | Voltage |
|  | 2 | Microcurrent |
|  | 3 | Current |
|  | 4 | Resistance (Continuity if Alternative unit flag) |
|  | 5 | Diode |
|  | 6 | Temperature in °C (or °F if Alternative unit flag) |
|  | 7 | Capacitance |
|  | 8 | Frequency |
|  | 9 | Duty cycle (positive pulse, or negative if Alternative unit flag) |
|  | 10 | Pulse width (positive pulse, or negative if Alternative unit flag) |
|  | 11 | dBm (or dBV if Alternative unit flag) |
|  | 12 | %Scale of 4-20 mA (or 0-20 mA if Alternative unit flag) |
|  | 13 | Conductance |
| 3 |  | **First (most significant) digit of measurement** |
| 4 |  | **Second digit of measurement** |
| 5 |  | **Third digit of measurement** |
| 6 |  | **Fourth digit of measurement** |
| 7 |  | **Fifth (least significant) digit of measurement** |
| 8 |  | **Mode bits** (several can be set at once) |
|  | 1 | Autoranging is enabled |
|  | 2 | Value is negative |
| 9 |  | **Mode bits** (several can be set at once) |
|  | 1 | DC |
|  | 2 | AC |
|  | 4 | Overload |
| 10 |  | **Exponent** |
| 11 |  | **Mode bits (several can be set at once)** |
|  | 1 | Alternate unit flag |
|  | 2 | Thermocouple type (0 = K, 1 = J) |
|  | 4 | Zero temperature compensation |
| 12 |  | **Hold mode** |
|  | 1 | Trig-Hold mode |
|  | 2 | Peak-Hold mode |
|  | 3 | Auto-hold mode |
|  | 4 | Relative mode is enabled (can be combined with *-Hold mode) |
| 13 |  | **Mode bits** (several can be set at once) |
|  | 1 | Average |
|  | 2 | Min |
|  | 4 | Max |
| 14 |  | **Data logging option** |
|  | 0 | Manual Log (Hand) |
|  | 1 | Event Log (Trig) |
|  | 2 | Interval Log (Auto) |
|  | 3 | Export Log (Hold button) |

Default exponent to be applied to the value for the different functions, in addition to the Exponent field.

| Exponent | Function |
|---|---|
| 10-6 | Millivoltage |
| 10-4 | Voltage |
| 10-9 | Microcurrent |
| 10-4 | Current |
| 10-3 | Resistance / Continuity |
| 10-4 | Diode |
| 10-1 | Temperature °C |
| 10-2 | Temperature °F |
| 10-12 | Capacitance |
| 10-3 | Frequency |
| 10-3 | Duty cycle |
| 10-6 | Pulse width |
| 10-3 | dBm / dBV |
| 10-2 | %Scale of 4-20 mA / 0-20 mA |
| 10-11 | Conductance |

### Event Notifiers
| String | Meaning |
|---|---|
| `*0` through `*7` | Rotary switch position has changed. `*0` denotes the most counter-clockwise position (excluding the OFF position), then the value is increased by one for each step in the rotary switch's range. On the U127xx models the codes range from `*0` through `*10`. |
| `*B` | Battery voltage dropped to "battery empty" level. |
| `*E` | Invalid command. |
| `*I` | Probes are connected to the wrong sockets for this mode, "Cerr" is shown on display (not supported on U123xx; it *is* supported on U124xC, U127xx and U128xx). |
| `*L` | A button was pressed (not supported on U123xx, U124xC, U127xx and U128xx). This notifier is only sent once after a command, even if the user presses several buttons. |

## Resources
- [Series overview](http://www.keysight.com/en/pc-1000004008%3Aepsg%3Apgr/handheld-digital-multimeter-clamp-and-calibrator-meters)
- [Documentation](http://www.keysight.com/main/facet.jspx?c=181653.i.1&to=80029.k.0)

