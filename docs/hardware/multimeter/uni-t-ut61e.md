# Uni T Ut61E
| | | |:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------:| | [*Image: \1* | | | Status | supported | | Counts | 22,000 | | IEC 61010-1 | CAT II (600 V) / CAT III (300 V) | | Connectivity | *RS232* / *USB* | | Measurements | voltage, current, resistance, capacitance, frequency, duty cycle, diode, continuity | | Features | autorange, true-rms, data hold, min/max, relative, bargraph, backlight | | Website | *uni-trend.com* | **UNI-T UT61E** The **UNI-T UT61E** is a 22,000 counts, CAT II (600 V) / CAT III (300 V) handheld digital multimeter with RS-232 or USB connectivity. See *UNI-T UT61E/Info* for more details (such as **lsusb -vvv** output) about the device. The more recent [UT61+/UT161 series](https://www.uni-trend.com/meters/html/product/NewProducts/UT61%20161%20Series/) is different from the previous UT61 series, and is **not** supported, until their protocol is known and a driver for them becomes available.
## Contents
\- *1 Hardware* \- *2 Photos* \- *3 Protocol* \- *4 Usage* \- *5 Resources*
## Hardware \- *Cyrustek ES51922* multimeter chip (ES51922A actually, as per various photos: [1](http://i492.photobucket.com/albums/rr283/DarkShadower/IMAG0005.jpg), [2](http://www.eevblog.com/forum/product-reviews-photos-and-discussion/uni-t-ut61e-multimeter-teardown-photos/?action=dlattach;attach=19985;image;PHPSESSID=14790b9893bed7edb7d8c0505b195ed8), [3](http://img848.imageshack.us/img848/3784/dscf0150w.jpg), [4](http://we.easyelectronics.ru/uploads/images/00/05/21/2011/11/18/553300.jpg)) ## Photos **Older version:** \-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
**Newer version:** \-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
## Protocol See *Cyrustek ES51922* for the DMM IC protocol. Depending on the cable, additional decoding is needed, though. Different cables are available to communicate to the DMM: regular serial cables which provide a COM port, and USB HID based cables where applications are required to handle a proprietary protocol of running serial communication on top of HID requests. See the **Device cables** page for details; the same cables can be used with many different DMM models. Depending on the specific cable in use, either a device driver ending in **-ser** or not ending in **-ser** must be used. See README.devices for details. The message *"HID feature report error: LIBUSB_ERROR_PIPE"* results from using the USB HID driver with a USB-to-serial cable. In this case, try using --driver=**uni-t-ut61e-ser** The transmission of the measurement data cannot be disabled. The respective Cyrustek ES51922 pin (111, **RS232**) is tied to GND (i.e. transmission is always enabled) on this multimeter.[[1]](http://www.steffenvogel.de/2011/01/25/inner-workings-of-uni-trend-ut61e-digital-multimeter/) ## Usage The following *OpenTraceCLI* command can be used to receive five measured values from a device connected via USB (note that the USB VID/PID after the **`conn`** option needs to be changed depending on the exact USB adapter cable used):
$ OpenTraceCLI --driver=uni-t-ut61e:conn=1a86.e008 -O analog --samples 5
If your meter has a serial (RS-232) cable connected to a USB-to-serial adapter, a different driver is used. Example for ttyUSB0:
$ OpenTraceCLI --driver=uni-t-ut61e-ser:conn=/dev/ttyUSB0 -O analog --samples 5
Same example for COM1 (Windows), please note the special syntax for specifying the COM port:
C:\> OpenTraceCLI --driver=uni-t-ut61e-ser:conn=\\\\.\COM1 -O analog --samples 5
**`--samples `** stops acquisition after the specified number of measurements, while **`--continuous`** does not stop. Type just **OpenTraceCLI** by itself for a summary of options. More information on drivers can be found in the [README.devices](http://github.com/OpenTraceLab/?p=OpenTraceCapture.git;a=blob;f=README.devices) file of the *OpenTraceCapture* source tree. ## Resources \- [Manual](http://www.uni-trend.com/manual2/UT61English.pdf) \- [Vendor software](http://www.uni-trend.com/Web%20site/DMM%20Software/UT61E_setup%20v2.00.exe) \- [Henrik Haftmann: DMM.exe etc.](http://www-user.tu-chemnitz.de/~heha/hs_freeware/UNI-T/) (Windows software for various UNI-T DMMs, and lots of device/protocol info) \- [Henrik Haftmann: Hoitek HE2325U info](http://www-user.tu-chemnitz.de/~heha/bastelecke/Rund%20um%20den%20PC/hid-ser.en.htm) \- [Henrik Haftmann: UT61E log and protocol docs](http://www-user.tu-chemnitz.de/~heha/hs_freeware/UNI-T/UT61E.LOG) \- [diyftw.de: Uni-Trend UT61E (UT-D04 linux treiber)](http://diyftw.de/wiki/doku.php?id=projekte:ut61e) (device info, Linux software using HIDAPI: [ut61e-linux-sw-0.02.tar.gz](http://diyftw.de/wiki/lib/exe/fetch.php?media=projekte:ut61e-linux-sw-0.02.tar.gz)) \- [Steffen Vogel: UNI-TREND UT61E Digital Multimeter](http://www.steffenvogel.de/2009/11/29/uni-trend-ut61e-digital-multimeter/) (device info, Linux software for serial port: [dmmut61e-0.01.tar.gz](http://static.steffenvogel.de/wp-content/uploads/2009/11/dmmut61e-0.01.tar.gz)) \- [Multimeter data parsing utility](https://bitbucket.org/kuzavas/dmm_es51922) complete implementation written in Python \- [Steffen Vogel: Inner workings of UNI-TREND UT61E Digital Multimeter](http://www.steffenvogel.de/2011/01/25/inner-workings-of-uni-trend-ut61e-digital-multimeter/) (teardown) \- *erste.de: UT61 - USB Multimeter unter Linux auslesen* (info on the Hoitek HE2325U (clone?) and how suspend/resume fixes some issues with it) \- *easyelectronics.ru: Refinement of a file multimeter UT61E* \- [flodins.info: Multimeter UNI-T UT61E](http://translate.google.de/translate?sl=pl&tl=en&u=http%3A%2F%2Fflodins.info%2Fmoim-zdaniem%2F81-multimetr-uni-t-ut61e) \- [UNI-T UT61E schematics: ut61e sch.pdf](http://www.eevblog.com/forum/product-reviews-photos-and-discussion/uni-t-ut61e-multimeter-teardown-photos/?action=dlattach;attach=20302;PHPSESSID=14790b9893bed7edb7d8c0505b195ed8) \- Teardowns: [1](http://www.eevblog.com/forum/product-reviews-photos-and-discussion/uni-t-ut61e-multimeter-teardown-photos/msg45069/#msg45069), [2](http://www.eevblog.com/forum/product-reviews-photos-and-discussion/uni-t-ut61e-multimeter-teardown-photos/msg113968/#msg113968), [3](http://www.eevblog.com/forum/product-reviews-photos-and-discussion/uni-t-ut61e-multimeter-teardown-photos/msg86347/#msg86347), [4](http://www.eevblog.com/forum/product-reviews-photos-and-discussion/uni-t-ut61e-multimeter-teardown-photos/msg86378/#msg86378), [5](http://www.eevblog.com/forum/product-reviews-photos-and-discussion/uni-t-ut61e-multimeter-teardown-photos/msg86802/#msg86802), [6](http://www.eevblog.com/forum/product-reviews-photos-and-discussion/uni-t-ut61e-multimeter-teardown-photos/msg82784/#msg82784)
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=UNI-T_UT61E&oldid=16071](https://OpenTraceLab.org/w/index.php?title=UNI-T_UT61E&oldid=16071)"
: \- [Pages using deprecated source tags](https://OpenTraceLab.org/w/index.php?title=Category:Pages_using_deprecated_source_tags&action=edit&redlink=1 "Category:Pages using deprecated source tags \(page does not exist\)") \- *Device* \- *Multimeter* \- *Supported*
## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
