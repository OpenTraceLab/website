# Lascar Electronics El Usb Protocol
[Lascar Electronics](http://www.lascarelectronics.com/) makes a series of devices in the "EL-USB" range. They share the same basic protocol, differing only in small details and log data format related to the device type.
## Contents
\- *1 Communication* \- *2 Protocol* \- *2.1 Commands* \- *2.2 Device configuration structure*
## Communication The Lascar data loggers all use a Silicon labs USB interface chip, which presents just two endpoints: | | | | | |----------|-----------|---------------|-----------------| | Endpoint | Direction | Transfer type | Max packet size | | 2 | IN | Bulk | 64 | | 2 | OUT | Bulk | 64 | ## Protocol ### Commands Bytes | Command
---|---
**0x00 0xff 0xff** | **Load device configuration structure.** A 3-byte header is returned first in which the first byte is 0x02, and the second and third bytes are the length of the configuration structure to follow, as a little-endian integer representing the number of bytes. Different devices in the EL-USB series have differently-sized configuration structures.
**0x01** _0xnn 0xnn_ | **Save device configuration structure.** The second and third bytes are the length of the configuration structure to follow, as a little-endian integer representing the number of bytes. The device responds with a single byte with value 0xff when the configuration has been saved.
**0x03 0xff 0xff** | **Transfer logged data.** A 3-byte header is returned first in which the first byte is 0x02, and the second and third bytes are the length of the logged data to follow, as a little-endian integer representing the number of bytes. The device's entire sample memory is then transferred. The number of stored samples (offset 0x2e in the configuration structure) should be checked before interpreting the data; any remaining data in the transfer should be ignored.
### Device configuration structure Offset | Size | Value
---|---|---
0x00 | 1 | **Device type** | 1,2 | EL-USB-1
---|---
3 | EL-USB-2
4,6 | EL-USB-3
5,7 | EL-USB-4
8 | EL-USB-LITE
9 | EL-USB-CO
10 | EL-USB-TC
11 | EL-USB-CO300
12 | EL-USB-2-LCD
13 | EL-USB-2+
14 | EL-USB-1-PRO
15 | EL-USB-TC-LCD
16 | EL-USB-2-LCD+
17 | EL-USB-5
18 | EL-USB-1-RCG
19 | EL-USB-1-LCD
20 | EL-OEM-3
21 | EL-USB-1-LCD
0x01 | 1 | _Unused_
0x02 | 16 | **NULL-terminated device name** (15 chars max)
0x12 | 1 | **Start time, hour** (0-23)
0x13 | 1 | **Start time, minute** (0-59)
0x14 | 1 | **Start time, second** (0-59)
0x15 | 1 | **Start date, day** (1-31)
0x16 | 1 | **Start date, month** (1-12)
0x17 | 1 | **Start date, year** (year - 2000)
0x18 | 4 | **Seconds remaining until logging starts** (unsigned little-endian)
0x1c | 2 | **Samplerate, as seconds between samples** (unsigned little-endian)
0x1e | 2 | **Number of stored samples** (unsigned little-endian)
0x20 | 1 | **Alarm conditions bitfield** (1=enable)  | EL-USB-2
---
0 | temperature high
1 | temperature low
2 | temperature high hold
3 | temperature low hold
4 | relative humidity high
5 | relative humidity low
6 | relative humidity high hold
7 | relative humidity low hold
0x21 | 1 |  | Bit | Bitfield
---|---
0 |
1 |
2 |
3 |
4 | Logging start (1) or stop
5 |
6 |
7 |
0x22 | 1 | **Temperature alarm high** (value + 40) * 2
0x23 | 1 | **Temperature alarm low** (value + 40) * 2
0x24 | 4 | **Calibration high** (stored as little-endian BINARY32 single-precision float)
0x28 | 4 | **Calibration low** (stored as little-endian BINARY32 single-precision float)
0x2c | 2 | _unknown_ (00 00)
0x2e | 2 | **Device-specific configuration** (16-bit little-endian integer or bitfield)  | EL-USB-1*, EL-USB-2*, EL-USB-LITE, EL-USB-TC*
---
0x0000 | Celcius
0x0001 | Fahrenheit
0x30 | 4 | **Firmware version** (ASCII, not NULL-terminated
0x34 | 2 | **Serial number** (unsigned little-endian)
0x36 | 2 | _unknown_ (00 00)
0x38 | 1 | **Relative humidity alarm high** (value * 2)
0x39 | 1 | **Relative humidity alarm low** (value * 2)
0x3a | 2 | _unknown_ (00 00)
0x3c | 4 | _unknown_ (00 00 00 00)
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=Lascar_Electronics_EL-USB_protocol&oldid=6032](https://OpenTraceLab.org/w/index.php?title=Lascar_Electronics_EL-USB_protocol&oldid=6032)"
## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
