# Dcttech Usbrelay
| | | |:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------------------------------:| | [*Image: \1* | | | Status | supported | | Source code | [dcttech-usbrelay](http://github.com/OpenTraceLab/?p=OpenTraceCapture.git;a=tree;f=src/hardware/dcttech-usbrelay) | | Channels | up to 8 | | Ratings | 10A 250VAC / 10A 30VDC | | Connectivity | USB HID | **dcttech.com USBRelay\** The **dcttech.com USBRelay\** is a USB relay card with up to 8 relays (models with 1, 2, 4, or 8 relays exist). The firmware is based on V-USB and presents itself as USB HID to the PC (so that no driver installation is required on Windows). See *Info* for USB details. ## Photos \-
[*Image: \1*
USBRelay2 top, ATtiny45, discrete transistors
\-
[*Image: \1*
USBRelay2 bottom
\-
[*Image: \1*
USBRelay4 top, ATmega8A, ULN2803, external supply for relays
\-
[*Image: \1*
USBRelay4 bottom
\-
[*Image: \1*
USBRelay8, DIY with Nanite841 and ULN2803
## Example use Detect the device and display its properties.  $ OpenTraceCLI -d dcttech-usbrelay --scan The following devices were found: dcttech-usbrelay:conn=/dev/hidraw2 - www.dcttech.com USBRelay4 [S/N: 12345]  $ OpenTraceCLI -d dcttech-usbrelay --show Driver functions: Multiplexer Scan options: conn dcttech-usbrelay:conn=/dev/hidraw2 - www.dcttech.com USBRelay4 [S/N: 12345] Channel groups: R1: channel R2: channel R3: channel R4: channel Supported configuration options across all channel groups: conn: /dev/hidraw2 (current) enabled: on, off  Display the relay state.  $ OpenTraceCLI -d dcttech-usbrelay --get channel_group=R1:enabled --get channel_group=R2:enabled --get channel_group=R3:enabled --get channel_group=R4:enabled true false false true  Manipulate the state of relays.  $ OpenTraceCLI -d dcttech-usbrelay --config channel_group=R1:enabled=off --config channel_group=R2:enabled=on --set  ## Resources \- [V-USB project page](https://www.obdev.at/products/vusb), software bitbanging USB for AVR controllers that don't have native USB hardware support \- [product description](http://vusb.wikidot.com/project:driver-less-usb-relays-hid-interface) and [source code repo](https://github.com/pavel-a/usb-relay-hid) of a private project that is not related to the vendor, implements OpenSource libraries and CLI and GUI applications to control these cards
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=Dcttech_usbrelay&oldid=16163](https://OpenTraceLab.org/w/index.php?title=Dcttech_usbrelay&oldid=16163)"
: \- *Device* \- *Multiplexer* \- *Supported*
## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
