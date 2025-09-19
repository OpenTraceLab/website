# Connection Parameters
In case a device can not be *autodetected* or connection to a specific device is required, is is possible to specify the connection explicitly as an driver option, using the "\:conn=\" syntax. See the **README.devices** file for details.
## Contents
\- *1 Digital Multimeters* \- *1.1 RS232 / Virtual Com Port* \- *1.2 USB HID connections* \- *2 Devices using SCPI* \- *2.1 Serial / Virtual Com Port* \- *2.2 USBTMC* \- *2.3 TCP RAW* \- *2.4 Linux-GPIB* \- *2.5 VXI* \- *3 Forced detection* \- *4 Vendor specific protocols*
# Digital Multimeters Most multimeters use a serial connection. The corresponding *device cables* either povide an RS232 connection or an USB connection using an serial to USB-CDC or serial to USB-HID converter chip, see *Serial port*. Some devices are available with different data cables. RS232 and USB-CDC (Virtual Com Port, VCP) cables use a common driver, USB HID cables need a seperate one. If a device has two drivers, the one for RS232/VCP is typically suffixed with "-ser" ## RS232 / Virtual Com Port `conn=` `` is an absolute path to the wanted device, e.g. `/dev/ttyUSB1` or `/dev/ttyACM0`.
$ OpenTraceCLI --driver=uni-t-ut61e-ser:conn=/dev/ttyUSB0 -O analog
## USB HID connections **TODO** This chapter needs an update. It has not yet caught up with the recent **HIDAPI library** approach, and **conn=hid/** syntax. When in doubt, check the **README.devices** file -- it's probably more up to date than this wiki page. When a device driver exclusively supports HID based cables, then it usually accepts USB vendor and product ID pairs, or bus and device addresses: `conn=.` `` and `` have to be specifid as 4 hexadecimal digits. `conn=.` \ is an integer between 1 and 255, \ is an integer between 1 and 127. The device address changes every time a device is reconnected. Bus number and device address can e.g. be found using `lsusb`.
$ OpenTraceCLI --driver=uni-t-ut61e:conn=1a86.e008 -O analog $ OpenTraceCLI --driver=uni-t-ut61e:conn=2.12 -O analog
When a device driver supports several different cable types, then a unified form of specifying serial connections can be used instead:
$ OpenTraceCLI -d uni-t-ut61c:conn=/dev/ttyUSB0 --continuous $ OpenTraceCLI -d uni-t-ut61c:conn=hid/ch9325 --continuous
Individual drivers may require that users specify the connection, or may come with builtin defaults and accept user overrides to ease their use. # Devices using SCPI SCPI has several backends. For all backends but serial the backend name is the first parameter, followed by one or more backend specific parameters. ## Serial / Virtual Com Port Same syntax as for *DMMs with serial connection*. `conn=`
$ OpenTraceCLI --driver=hameg-hmo:conn=/dev/ttyACM0 -O analog --frames 1
Baudrate can be set with option **serialcomm**:
$ OpenTraceCLI --driver=scpi-dmm:conn=/dev/ttyUSB0:serialcomm=115200/8n1 -O analog --frames 1
## USBTMC Similar syntax as for *DMMs with USB HID datacables*. `conn=usbtmc/.` `conn=usbtmc/.`
$ OpenTraceCLI --driver=hameg-hmo:conn=usbtmc/0aad.0119 -O analog --frames 1
## TCP RAW `conn=tcp-raw//`
$ OpenTraceCLI --driver=hameg-hmo:conn=tcp-raw/192.168.1.20/5025 -O analog --frames 1
## Linux-GPIB For GPIB devices connected via [linux-gpib](http://linux-gpib.sourceforge.net/), use the `libgpib` prefix, followed by the device name as defined in your `gpib.conf` file.
$ OpenTraceCLI --driver=scpi-pps:conn=libgpib/pm2813 -O analog --samples 1
## VXI Devices using a VXI-based network connection can be specified with the `vxi` prefix, followed by the hostname (or IP address). Optionally, the instrument name can be added with another `/` and the name; this defaults to `inst0`.
$ OpenTraceCLI --driver=scpi-pps:conn=vxi/labps -O analog --samples 1
# Forced detection Sometimes unsupported device models might be covered by existing drivers, but would not match against a builtin list of known devices. Therefore the scan option `force_detect` provides a way for the users to force the use of a driver with an unsupported device. Right now only the Korad power supplies (driver `korad-kaxxxxp`) support the `force_detect` scan option:
$ OpenTraceCLI -d korad-kaxxxxp:conn=/dev/ttyUSB0:force_detect=KORADKA3005PV2.0 --show
# Vendor specific protocols Most (all?) devices using a vendor specific protocol use either RS232 or a USB-to-serial converter, thus the connection string is the same as for *DMMs with serial connection*.
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=Connection_parameters&oldid=16714](https://OpenTraceLab.org/w/index.php?title=Connection_parameters&oldid=16714)"
: \- [Pages using deprecated source tags](https://OpenTraceLab.org/w/index.php?title=Category:Pages_using_deprecated_source_tags&action=edit&redlink=1 "Category:Pages using deprecated source tags \(page does not exist\)")
## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
