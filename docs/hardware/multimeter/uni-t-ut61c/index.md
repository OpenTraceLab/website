---
title: UNI-T UT61C
---

# UNI-T UT61C

<div class="infobox" markdown>

![UNI-T UT61C](./img/Uni-t_ut61c_mugshot.png){ .infobox-image }

### UNI-T UT61C

| | |
|---|---|
| **Status** | supported |
| **Source code** | [uni-t-dmm](https://github.com/OpenTraceLab/OpenTraceCapture/tree/main/src/hardware/uni-t-dmm) |
| **Counts** | 6000 |
| **IEC 61010-1** | CAT II (600V) / CAT III (300V) |
| **Connectivity** | [RS232](https://sigrok.org/wiki/Device_cables#UNI-T_UT-D02) / [USB](https://sigrok.org/wiki/Device_cables#UNI-T_UT-D04) |
| **Measurements** | voltage, current, resistance, capacitance, frequency, duty cycle, diode, continuity, temperature |
| **Features** | autorange, data hold, min/max, rel, bargraph, backlight |
| **Website** | [uni-trend.com](http://www.uni-trend.com/UT61C.html) |

</div>

The **UNI-T UT61C** is a 6000 counts, CAT II (600V) / CAT III (300V) handheld digital multimeter with RS232 or USB connectivity.

See [UNI-T UT61C/Info](https://sigrok.org/wiki/UNI-T_UT61C/Info) for more details (such as **lsusb -v** output) about the device.

## Hardware

**Multimeter**:

- **Multimeter IC**: [Fortune Semiconductor FS9922-DMM4](https://sigrok.org/wiki/Multimeter_ICs#Fortune_Semiconductor_FS9922-DMM4) ([datasheet](http://www.ic-fortune.com/upload/Download/FS9922-DMM4-DS-11_EN.pdf))
- **Crystal**: 4MHz (markings: "3.999")
- **Fuses**: 10A/240V and 1A/240V (HRV fuses)

**RS232 cable**:

See [Device cables#UNI-T_UT-D02](https://sigrok.org/wiki/Device_cables#UNI-T_UT-D02).

**USB cable**:

See [Device cables#UNI-T_UT-D04](https://sigrok.org/wiki/Device_cables#UNI-T_UT-D04).

## Photos

<div class="photo-grid" markdown>

[![Uni T Ut61c Mugshot](./img/Uni-t_ut61c_mugshot.png)](./img/Uni-t_ut61c_mugshot.png "Uni T Ut61c Mugshot"){ .glightbox data-gallery="uni-t-ut61c" }
<span class="caption">Uni T Ut61c Mugshot</span>

</div>
## Usage

The DMM does not transmit samples after power up.
You need to long-press the `REL Δ` button to activate the remote measurement.
This also deactivates the auto power-off function of the device.

The following [sigrok-cli](https://sigrok.org/wiki/Sigrok-cli) command can be used to receive five measured values from a device connected via USB (note that the USB VID/PID after the **`conn`** option needs to be changed depending on the exact USB adapter cable used):

```
$ sigrok-cli --driver=uni-t-ut61c:conn=1a86.e008 -O analog --samples 5

```

If your meter has a serial (RS-232) cable connected to a USB-to-serial adapter, a different driver is used. Example for ttyUSB0:

```
$ sigrok-cli --driver=uni-t-ut61c-ser:conn=/dev/ttyUSB0 -O analog --samples 5

```

Same example for COM1 (Windows), please note the special syntax for specifying the COM port:

```
C:\> sigrok-cli --driver=uni-t-ut61c-ser:conn=\\.\COM1 -O analog --samples 5

```

**`--samples <n>`** stops acquisition after the specified number of measurements, while **`--continuous`** does not stop.  Type just **sigrok-cli** by itself for a summary of options. 
More information on drivers can be found in the [README.devices](http://sigrok.org/gitweb/?p=libsigrok.git;a=blob;f=README.devices) file of the [libsigrok](https://sigrok.org/wiki/Libsigrok) source tree.

## Protocol

See [Multimeter_ICs#Fortune_Semiconductor_FS9922-DMM4](https://sigrok.org/wiki/Multimeter_ICs#Fortune_Semiconductor_FS9922-DMM4) for the DMM IC protocol. Depending on the cable, additional transport-specific decoding is needed, though.

## Resources
- [Manual](http://www.uni-trend.com/manual2/UT61English.pdf)
- [Vendor software](http://www.uni-trend.com/Web%20site/DMM%20Software/UT61C%20setup.exe)

