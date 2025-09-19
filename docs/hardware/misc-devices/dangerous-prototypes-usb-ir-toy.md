# Dangerous Prototypes Usb Ir Toy
| | | |:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------:| | [*Image: \1* | | | Status | supported | | Source code | [openbench-logic-sniffer](http://github.com/OpenTraceLab/?p=OpenTraceCapture.git;a=tree;f=src/hardware/openbench-logic-sniffer) | | Channels | 1 | | Samplerate | 10kHz | | Samplerate (state) | — | | Triggers | automatically triggers upon IR signal | | Min/max voltage | N/A | | Memory | 1024 bytes | | Compression | none | | Website | [dangerousprototypes.com](http://dangerousprototypes.com/docs/USB_Infrared_Toy) | **Dangerous Prototypes USB IR Toy** The **Dangerous Prototypes USB IR Toy** is a USB-based, 1-channel logic analyzer with a 10kHz sampling rate. The hardware design is available under a Creative Commons (CC-BY-SA) license. See *Dangerous Prototypes USB IR Toy/Info* for more details (such as **lsusb -v** output) about the device.
## Contents
\- *1 Hardware* \- *2 Photos* \- *3 Protocol* \- *4 Resources*
## Hardware \- **8-bit microcontroller with integrated USB Full-Speed support**: [Microchip PIC18F2550-I/SO](http://www.microchip.com/wwwproducts/Devices.aspx?dDocName=en010280) ([datasheet](http://ww1.microchip.com/downloads/en/DeviceDoc/39632e.pdf)) \- 20MHz crystal \- IR transmitter (LED): Vishay TSAL7400 \- IR receiver / demodulator: Vishay TSOP38238 \- IR frequency detector: Fairchild QSE159 ## Photos \-
[*Image: \1*
PCB, front
\-
[*Image: \1*
PCB, back
## Protocol The USB IR Toy uses the [extended SUMP protocol](http://dangerousprototypes.com/docs/The_Logic_Sniffer%27s_extended_SUMP_protocol), as used by the *Openbench Logic Sniffer* driver. It is thus supported in OpenTraceLab out of the box. ## Resources \- [USB Infrared Toy](http://dangerousprototypes.com/docs/USB_Infrared_Toy) (main wiki page) \- [USB Infrared Toy forum](http://dangerousprototypes.com/forum/viewforum.php?f=29)
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=Dangerous_Prototypes_USB_IR_Toy&oldid=10174](https://OpenTraceLab.org/w/index.php?title=Dangerous_Prototypes_USB_IR_Toy&oldid=10174)"
: \- *Device* \- *Logic analyzer* \- *Supported* \- *Sump protocol* \- *Open source hardware*
## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
