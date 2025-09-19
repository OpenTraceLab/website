# Motech Lps 300 Series
| | | |:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------------------------:| | [*Image: \1* | | | Status | supported | | Source code | [motech-lps-30x](http://github.com/OpenTraceLab/?p=OpenTraceCapture.git;a=tree;f=src/hardware/motech-lps-30x) | | Channels | 1/3 | | Voltage/current (CH1) | 0-30 V / 0-3 A, model-dependant | | Voltage/current (CH2) | 0-30 V / 0-3 A, model-dependant | | Voltage/current (CH3) | 3.3/5 V / 0-3 A, model-dependant | | Connectivity | RS232 | | Features | output on/off, calibration | | Website | [power.motech.com.tw](http://power.motech.com.tw/) | **Motech LPS-300 series** The ***Motech* LPS-300** series of programmable power supplies consists of five 1-channel or 3-channel devices with optional RS232 connectivity. The devices were also sold as **Amrel LPS-301** to **LPS-305** by **American Reliance** and partly under further brands, e.g. the **LPS-305** as **Tecpel TPS-3025**.
## Contents
\- *1 Specifications* \- *2 Protocol* \- *3 Commands* \- *4 Resources*
## Specifications The models differ only in the number of available channels, maximum voltage and maximum current output: | | | | | | |-------------------------------------------------|--------------|----------|---------------------------------|---------------| | Model | Power output | Channels | Voltage/current | OpenTraceLab status | | *LPS-301* | 30 W | 1 | 30 V/1 A or 15 V/2 A | Supported | | LPS-302 | 60 W | 1 | 30 V/2 A or 15 V/4 A | Planned | | LPS-303 | 90 W | 1 | 30 V/3 A | Planned | | LPS-304 | 70 W | 3 | ±30 V/1 A or ±15 V/2 A; 5 V/2 A | Planned | | LPS-305 | 165 W | 3 | ±30 V/2.5 A; 3.3 or 5 V/3 A | Planned | The three-channel versions have the two main channels wired together for symmetric power supply, but the voltages can be set independantly, if desired. They can be set on or off only together. The *planned* models are prepared in the driver *motech-lps-30x* and can be implemented easily as soon as devices for testing get available. These specifications are common to all models: | | | | |:-------------------------|:---------------------|:-------------| | 30 V channels | | | | | **Voltage** | **Current** | | Programming resolution | 10 mV | 1 mA | | Programming accuracy | 0.05% + 20 mV | 0.15% + 5 mA | | Readback accuracy | 0.1% + 20 mV | 0.2% + 5 mA | | Ripple (10 Hz to 20 MHz) | 1 mV rms / 10 mV p-p | 10 mA rms | | Load regulation | 0.001% + 1mV | 0.01% + 1mA | These specifications apply only to models having a 3.3V/5V output: | | | | |:-----------------------|:------------------|:------------| | 3.3/5 V channel | | | | | **Voltage** | **Current** | | Ripple (10Hz to 20MHz) | 2 mVrms / 10mVp-p | 10mArms | | Load regulation | 0.001% + 1mV | 0.01% + 1mA | The devices can be calibrated easily requiring nothing but a multimeter of sufficient precision. ## Protocol The communication with the device is via an optional RS-232 port (Option 02). The port parameters are 2400 Baud, 8n1. All commands are plain ASCII. All commands are terminated by \r, \n or \r\n. Another command sent before reception of the reply (usually *OK*) will be ignored. It seems that trailing digits for numerical parameters can be omitted.  Command | Reply | Description
---|---|---
BEEP(0|1|2|3) | OK | Beeper function 0: disable; 1: enable; 2: force alarm (beeper test) 3: end force alarm.
CALI(0|1|2) | ? | Calibration 0=end; 1=begin; 2=input parameter
**There seem to be no plausibility checks and the description is incomplete. Messing around with the calibration is strictly discouraged and can cause odd behaviour!**
HELP | (see right) OK | Output list of commands (several lines)
IOUT(n) | d.dddd OK | Current readback
ISET(n) d.dddd | OK | Set output current
LOWA(0|1) | OK | CC output compensated 0=off; 1=on (what does this setting do?)
MODEL | \r\nLPS-␣␣␣␣ OK | Get model number (reply contains spaces instead of model no in FW 1.17, seems to be a bug)
OUT(0|1) | OK | Disable/enable output. OUT without a parameter seems to disable it.
STATUS | <decimal> OK | Working status, bitwise encoding.
Bit 0, channel 1 mode: 0: CV 1: CC.
Bit 1, channel 2 mode: 0: CV 1: CC.
Bit 3,2, tracking: 00: independant; 10: to channel 1; 11: to channel 2.
Bit 4, digital output 3: 0: off; 1: on.
Bit 5, digital output voltage: 0: 5 V; 1: 3.3 V.
Bit 6, output 1/2: off; 1: on.
Bit 7, output 3: 0: ok; 1: overloaded.
Bit 8, Fan: 0: off/low; 1: on/high
Bit 9, beeper: 0: disabled; 1: enabled. Corresponds to BEEP0/1.
Bit 10, CC output compensated: 0: off; 1: on
TRACK(0|1|2) | OK | Tracking 0=independant; 1=from channel 1; 2=from channel 2. Tracking seems to mean that channels 1 and 2 are synchronous on multi-channel models.
VDD(0|3|5) | OK | Set ("digital") output 3 0=off; 1=3.3 V; 5=5 V
VERSION | \r\nVer-1.17␣\r\n OK | Get version number.
**Bug: Seems not to work while the output is active on LPS-301 1.17, no reply!**
VOUT(1|2) | dd.ddd OK | Voltage readback
VSET(1|2) dd.ddd | OK | Set output voltage. Entering more than 3 post-dot digits will overwrite starting from the left!
The specified resolution is 10 mV. However, the actual resolution seems to be slightly higher, possibly due to rounding during decimal to binary conversion or depending on calibration.
* | \r\nERROR\r\n OK | Error (invalid command).
OK means \r\nOK\r\n. ## Commands | | | | | |----------------------------|---------|---------------------|------------------------------------------------------------------------------------------------------------------------------| | Function | Target | Parameters | Comment | | SR_CONF_OUTPUT_CHANNEL | Device | Track1 \| Track2 | In tracking mode the other main channel seems to follow the tracked channel. | | SR_CONF_OUTPUT_VOLTAGE | Channel | Double 0-30.0 | Get: Query output voltage. Updated only if sampling is active! Channel 3 allows only 5 V or 3.3 and 5 V, depending on model! | | SR_CONF_OUTPUT_VOLTAGE_MAX | Channel | Double 0-30.0 | Get: Get max. possible voltage. Set: Set output voltage. Channel 3 allows only 5 V or 3.3 and 5 V, depending on model! | | SR_CONF_OUTPUT_CURRENT | Channel | Double 0.005-x.xxxx | Get: Query output current. Updated only if sampling is active! Channel 1 and 2 only, channel 3 is fixed! | | SR_CONF_OUTPUT_CURRENT_MAX | Channel | Double 0.005-x.xxxx | Get: Get max. possible current. Set: Set output current. Channel 1 and 2 only, channel 3 is fixed! | | SR_CONF_OUTPUT_ENABLED | Channel | Boolean on/off | Switch output on or off. Channels 1 and 2 are connected, accessing one will also set the other one. | Additionally sampling commands are possible. ## Resources \- [LPS-301 - LPS-304 User Manual](http://www.prz.rzeszow.pl/kpe/materialy/astadler/DAQWWW/Manuals/LPS304%20Instruction%20Manual.pdf) \- [LPS-305 User Manual](http://www.motech.com.tw/tw/doc/instrument/LPS%20305%20user%20manual.pdf) ([Amrel version](http://www.programmablepower.com/products/amrel/LPS/LPS305%20Manual.pdf)) \- [Datasheet](http://www.transcat.com/PDF/wiz.pdf)
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=Motech_LPS-300_series&oldid=10166](https://OpenTraceLab.org/w/index.php?title=Motech_LPS-300_series&oldid=10166)"
: \- *Power supply* \- *Supported*
## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
