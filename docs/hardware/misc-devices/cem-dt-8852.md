# Cem Dt 8852
| | | |:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------------------:| | [*Image: \1* | | | Status | supported | | Source code | [cem-dt-885x](http://github.com/OpenTraceLab/?p=OpenTraceCapture.git;a=tree;f=src/hardware/cem-dt-885x) | | Connectivity | USB | | Frequency range | 31.5Hz - 8kHz | | Measurement range (A) | 30dB - 130dB | | Resolution | 0.1dB | | Accuracy (94dB@1kHz) | 1.4dB | | Frequency weighting | A, C | | Time weighting | F, S | | Standards | IEC 61672-1 Class 2 | | Website | *cem-instruments.com* | **CEM DT-8852** The **CEM DT-8852** is an IEC 61672-1 class 2 compliant sound level meter with USB connectivity. See *CEM DT-8852/Info* for more details (such as **lsusb -vvv** output) about the device. Some random facts: \- The device only starts logging to USB when the SETUP key is pressed on the keypad. This also disables auto power-off mode. \- Power consumption is 9.5mA at 9V, regardless of USB or recording status; 15mA when the backlight is on. \- The battery low warning starts when the battery delivers less than 7V. \- Sound pressure level measurements are sent to the host at a rate of 20Hz.
## Contents
\- *1 Hardware* \- *2 Photos* \- *3 Protocol* \- *3.1 Commands* \- *3.2 Measurements and settings* \- *3.3 Recorded measurements* \- *3.3.1 Bugs* \- *4 Resources*
## Hardware \- [Holtek HT49R70A](http://www.holtek.com/english/docum/uc/49x70.htm) microcontroller with firmware in OTP flash \- [Silicon Labs CP2102](http://www.silabs.com/products/interface/usbtouart/Pages/usb-to-uart-bridge.aspx) USB-serial interface ## Photos \-
[*Image: \1*
Device, front
\-
[*Image: \1*
Device, back
\-
[*Image: \1*
Device, side
\-
[*Image: \1*
PCB
\-
[*Image: \1*
PCB: keypad and LCD
\-
[*Image: \1*
PCB detail
\-
[*Image: \1*
PCB detail
\-
[*Image: \1*
Microcontroller
\-
[*Image: \1*
CP2102 USB interface chip
\-
[*Image: \1*
Display, all segments on
## Protocol The device communicates at 9600 baud, no parity, 8 data bits, and 1 stop bit (9600/8n1). ### Commands None of the following commands are needed to receive live measurements from the device; see the next section. The commands are always 1 byte, take no parameters, and receive no acknowledgement or reply. Figuring out whether the command was successful or not must be done by watching the continual stream of settings. This is not optional: the device is very unresponsive, and commands nearly always have to be resent. The following commands are supported: | | | |-------|-------------------------------------------------| | Token | Description | | 0x33 | Power down the device. | | 0x55 | Toggle measurement recording on/off. | | 0x11 | Toggle Max/Min/normal mode. | | 0x77 | Toggle Fast/Slow time weighting | | 0x88 | Toggle measurement range. | | 0x99 | Toggle dBA/dBC frequency weighting. | | 0xac | Request transfer of stored measurement records. | ### Measurements and settings Current settings and measurements are continually streamed over the serial bus, without any prompting from the PC. Data is encapsulated in packets of between two and five bytes. The packets are structured as follows: | | | | | | |:----:|:-----:|:----:|:---:|:---:| | 1 | 2 | 3 | 4 | 5 | | 0xa5 | Token | Data | | | The number of data bytes depend on the token. These are the tokens: | | | | |-------|------|------------------------------------------------------------------| | Token | Data | Description | | 0x02 | 0 | Time weighting Fast | | 0x03 | 0 | Time weighting Slow | | 0x04 | 0 | Max hold mode | | 0x05 | 0 | Min hold mode | | 0x06 | 3 | Current time in BCD; first nibble unknown | | 0x07 | 0 | Current measurement is over measurement range high threshold | | 0x08 | 0 | Current measurement is under measurement range low threshold | | 0x09 | 0 | Memory store is full | | 0x0a | 0 | Device is currently recording to memory | | 0x0b | 1 | Last measurement sent with 0x0d was shown on display readout | | 0x0c | 0 | Last measurement sent with 0x0d was shown in bargraph on display | | 0x0d | 2 | Current measurement, multiplied by 10, in BCD | | 0x0e | 0 | Live measurements mode (not max/min hold) | | 0x0f | 0 | Battery is low | | 0x11 | 0 | Current measurement is within the current measurement range | | 0x19 | 0 | Memory store is not full | | 0x1a | 0 | Device is not recording to memory | | 0x1b | 1 | Frequency weighting dBA | | 0x1c | 1 | Frequency weighting dBC | | 0x1f | 0 | Battery is OK | | 0x30 | 0 | Measurement range 30-80 dB | | 0x40 | 0 | Measurement range 30-130 dB (auto) | | 0x4b | 0 | Measurement range 50-100 dB | | 0x4c | 0 | Measurement range 80-130 dB | ### Recorded measurements After the host has requested the recorded measurement log, a packet will be inserted into the regular output stream. Instead of 0xa5, this packet begins with 0xbb: | | | | |:----:|:------:|:---:| | 1 | 2 | 3 | | 0xbb | Length | | The length field is big-endian encoded, with an offset of 100. A length field of `0x0064` thus indicates no stored samples. This is followed by a series of records, where the first byte (token) indicates the content to follow: | | | |:-----:|:-------------------------------------------------------------------------------------------:| | Token | Description | | 0xaa | Measurements in this record use dBA frequency weighting. Metadata follows. | | 0xcc | Measurements in this record use dBC frequency weighting. Metadata follows. | | 0xac | Measurements follow, until the next token. Encoding is BCD times 10, as in the live stream. | | 0xdd | End of recorded measurement dump. | The metadata following 0xaa and 0xcc denotes the date and time this record was started, and the sampling rate. It is encoded in 7 bytes: | | | |:----:|:-------------------------------------------------------:| | Byte | Description | | 0 | Last two digits of year (BCD) | | 1 | Month (BCD) | | 2 | Day of month (BCD) | | 3 | Hour (BCD) | | 4 | Minutes (BCD) | | 5 | Seconds (BCD) | | 6 | Samplerate, as seconds between measurements (1-59, BCD) | #### Bugs \- A packet indicating memory is empty is not supposed to have any sub-packets: only the 0xbb token, length, and 0xdd to indicate end of transfer. However this always seems to include a 0xaa or 0xcc byte as well: > | | | | | | > |:----:|:----:|:----:|:----:|:----:| > | 1 | 2 | 3 | 4 | 5 | > | 0xbb | 0x00 | 0x64 | 0xaa | 0xdd | \- The length of the memory transfer (as sent after 0xbb) refers to all the data sent afterwards, excepting only 0xac and 0xdd, which are protocol tokens. However: \- The count is always off by one; one byte less is sent than the length indicates. \- The last record's measurement data's last byte is in fact a random extra byte, half of a BCD-encoded SPL value. This is another off-by-one: the byte has to be discarded. The length is thus actually off by two. ## Resources [Partial protocol documentation](http://www.produktinfo.conrad.com/datenblaetter/100000-124999/105031-da-01-en-InterfaceProtocol_VOLTCRAFT_SL_451.pdf)
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=CEM_DT-8852&oldid=9259](https://OpenTraceLab.org/w/index.php?title=CEM_DT-8852&oldid=9259)"
: \- *Device* \- *Sound level meter* \- *Supported*
## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
