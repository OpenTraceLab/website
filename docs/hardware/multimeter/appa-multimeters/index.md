---
title: APPA Multimeters
---

# APPA Multimeters

<div class="infobox" markdown>

### APPA Multimeters

| | |
|---|---|
| **Status** | in progress |
| **Source code** | [appa-dmm](https://github.com/OpenTraceLab/OpenTraceCapture/tree/main/src/hardware/appa-dmm) |
| **Connectivity** | Infrared (USB), Bluetooth LE |
| **Website** | [appatech.com](http://www.appatech.com/en/product.html) |

</div>

Hand multimeters, bench versameters, current clamps and lcr meters with optical serial (USB) and BLE interface supported by the "**appa-dmm**" driver.

The driver supporting these APPA-based devices ("appa-dmm" in sigrok) has been created and will be included in mainline sigrok once it passes acception (see developement repository [github.com/Cymaphore/libsigrok branch appa-dmm](https://github.com/Cymaphore/libsigrok)).


















# Supported Series
| Series | Type | Optical RS232/USB | Bluetooth LE | Comments |
|---|---|---|---|---|
| [APPA 100 Series](https://sigrok.org/wiki/APPA_100_Series) | Handheld Multimeter | X |  | experimental |
| [APPA 150B Series](https://sigrok.org/wiki/APPA_150B_Series) | Clamp Multimeter |  | X |  |
| [APPA 170 Series](https://sigrok.org/wiki/APPA_170_Series) | Clamp Multimeter |  | X |  |
| [APPA 200 Series](https://sigrok.org/wiki/APPA_200_Series) | Bench Multimeter | X | X* |  |
| [APPA 300 Series](https://sigrok.org/wiki/APPA_300_Series) | Handheld Multimeter | X |  | experimental |
| [APPA 500 Series](https://sigrok.org/wiki/APPA_500_Series) | Handheld Multimeter | X | X* |  |
| [APPA 700 Series](https://sigrok.org/wiki/APPA_700_Series) | Handheld LCR Meters | X |  | maybe limited support, unknown |
| [APPA A Series](https://sigrok.org/wiki/APPA_A_Series) | Clamp Multimeter |  | X |  |
| [APPA S Series](https://sigrok.org/wiki/APPA_S_Series) | Handheld Multimeter |  | X |  |
| [APPA sFlex Series](https://sigrok.org/wiki/APPA_sFlex_Series) | Clamp Multimeter |  | X |  |

Note: * BLE-Support on individual models

# Features
## Device detection and identification

The driver automatically detects the device and its capabilities on connection. If a specific feature, for example data logging, is not supported by a specific device, it is for compatibility reasons visible in the driver but will return an empty result. Data acquisition can happen continuous or limited by time, sample count or frame count.

If the model supports it, vendor and model information as well as the serial number are read from the device and can be accessed in sigrok. In case this fails, sigrok will report the device under its OEM designation.

## Data sources
### Live (display readings)

This data source provides the display readings of a device. If a reading is currently unavailable or disabled, inf or OL are reported. This is also the case for the Secondary Display for devices that don't have this feature.

Live readings usually contain all the information available via the APPA protocol that can be mapped to corresponding sigrok-values. If a meaning can not be mapped, it is ignored. Display text is decoded and will result in a warning-message containing the text. Menu operations are decoded as well and will also result in warning-messages. The driver is prepared to incorporate these message into sigrok-readings, in case sigrok ever supports this.

Error messages from the device (Probe-Errors, Fuse-Errors, etc.) are reported using error messages.

The sample rate of the readings depends on the connectivity used. By default, data as acquired from the device at 10 Hz and the polling is aligned with the clock of the host machine. If the connection method (for example BLE on some devices) doesn't permit that rate, it is lowered and the polling timer will not be aligned with the host to still allow the highest possible data rate. The actual sample rate of the acquired readings depends on the capabilities of the device and the function in question.

### MEM (hold / auto-hold memory)

Some of the models have an internal memory for single display readings based on auto hold or manual save features. These are individual records not related to each other without any sample rate. This data can be acquired / downloaded from the device using sigrok.

The primary channel holds the reading, the secondary channel holds the ID of the record as stored in the device. The data can be exported as CSV-File using sigrok-cli.

### LOG (data logging memory)

Many of the models have an internal memory to perform standalone data logging at a configurable sample rate. This data can be acquired / downloaded from the device using sigrok.

The primary channel holds the reading, the secondary channel holds the ID of the record as stored in the device. The sample interval is obtained from the device, but it depends upon the sigrok-client to actually interpret it. The data can be exported as CSV-File using sigrok-cli.

## Connectivity
- Optical serial (USB cable, for example [IC-300U](https://sigrok.org/wiki/Device_cables#APPA_IC-300U))
- Optical serial (RS232 cable, for example [IC-300](https://sigrok.org/wiki/Device_cables#APPA_IC-300))
- Bluetooth LE

The available connection method depends on the individual model.

# Examples: Establish data connection between sigrok and MM 12 (APPA 506B)

**Important:** Driver is not (yet) part of mainline sigrok - see [this repository in github](https://github.com/Cymaphore/libsigrok) if you want to use it already.

## Serial/USB

Assuming the meter is turned on, plugged in and the usb-serial driver is loadad and up (should happen automatically). /dev/ttyUSB0 is used as an example.

List devices, if unsure what the serial port is:

```
 # sigrok-cli --list-serial
 /dev/ttyUSB0  CP2102 USB to UART Bridge Controller - 2020y000231

```

Scan for MM 12 with USB/Serial connection:

```
 $ sigrok-cli -d benning-dmm:conn=/dev/ttyUSB0 --scan

```

Show readings from connected meter:

```
 $ sigrok-cli -d benning-dmm:conn=/dev/ttyUSB0 --continuous

```

Open in SmuView:

```
 $ smuview --driver benning-dmm:conn=/dev/ttyUSB0

```
## Bluetooth LE

Assuming the meter is turned on and bluetooth activated on the meter and the PC. Important: Your Bluetooth-Controller must support BLE.

Scan for BLE devices:

```
 # sudo sigrok-cli --list-serial
 bt/appa-dmm/18-7A-93-BF-47-62   BENNING MM12 (BLE)

```

If your OS / UI supports it, you can also use the Bluetooth scanning capability from the system tray and pick the MAC address from the details there.

"18:7A:93:BF:47:62" acts as an example for the device address you will find. For sigrok the ":" must be replaced by "-" for now. That device address is used for the following examples, just replace it by the address of your own meter.

The full connection string then would look like this, as seen in the scanning result: bt/appa-dmm/18-7A-93-BF-47-62

Scan for MM 12 with BLE connection:

```
 $ sigrok-cli -d benning-dmm:conn=bt/appa-dmm/18-7A-93-BF-47-62 --scan

```

Show readings from connected meter:

```
 $ sigrok-cli -d benning-dmm:conn=bt/appa-dmm/18-7A-93-BF-47-62 --continuous

```

Open in SmuView:

```
 $ smuview --driver benning-dmm:conn=bt/appa-dmm/18-7A-93-BF-47-62

```

