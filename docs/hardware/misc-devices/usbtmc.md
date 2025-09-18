# Usbtmc

USBTMC (USB Test and Measurement Class) is a set of standard device class specifications, built on top of the USB standard. It is intended as a modern replacement of the venerable [IEEE-488](IEEE-488.html "IEEE-488") (GPIB) standard, which is based on a large parallel connector. Two standards documents are specified: \- **USBTMC specification**: specifies the protocol and descriptors that allow communications between devices and client software.  \- **USB488 subclass specification**: this specifies how to send and receive IEEE-488.1 and IEEE-488.2 commands over a USBTMC-based transport. The standard is freely available from [usb.org](https://www.usb.org/sites/default/files/USBTMC_1_006a.zip). The OpenTraceLab project supports USBTMC via the respective [libusb-1.0 based USBTMC SCPI backend](http://github.com/OpenTraceLab/?p=OpenTraceCapture.git;a=blob;f=src/scpi/scpi_usbtmc_libusb.c) (optionally the [librevisa](http://www.librevisa.org) library also has some support, though this not well-tested). ## Resources \- [EETimes: USBTMC Unwrapped](http://www.eetimes.com/electronics-products/test-measurement/4074421/USBTMC-Unwrapped)
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=USBTMC&oldid=14001](https://OpenTraceLab.org/w/index.php?title=USBTMC&oldid=14001)"

## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
