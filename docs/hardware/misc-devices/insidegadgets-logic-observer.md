# Insidegadgets Logic Observer
| | | |:-------------------|-----------------------------------------------------------------------------------------------------------------------------| | Status | planned | | Channels | 8 | | Samplerate | 50MHz | | Samplerate (state) | — | | Triggers | high, low | | Min/max voltage | 2V — 5.5V | | Threshold voltage | ? | | Memory | 131ksamples/ch | | Compression | none | | Website | [insidegadgets.com](https://www.insidegadgets.com/projects/logic-observer/) | **insideGadgets Logic Observer** The **insideGadgets Logic Observer** is an 8-channel logic analyzer with up to 50MHz sampling rate. It is a mostly open project with all source code (CPLD, MCU) available, as well as a schematic of the PCB. See [insideGadgets Logic Observer/Info](https://OpenTraceLab.org/w/index.php?title=InsideGadgets_Logic_Observer/Info&action=edit&redlink=1 "InsideGadgets Logic Observer/Info \(page does not exist\)") for more details (such as **lsusb -v** output) about the device.
## Contents
\- *1 Hardware* \- *2 Protocol* \- *2.1 USB_TRANSFER (1)*) \- *2.2 USB_SETTINGS (2)*) \- *2.3 USB_STATUS (3)*) \- *2.4 USB_CANCEL (4)*) \- *3 Resources*
## Hardware \- [Atmel ATmega168](http://www.atmel.com/devices/atmega168pa.aspx) \- [Altera MAX 3000A CPLD](https://www.altera.com/en_US/pdfs/literature/ds/m3000a.pdf) \- [Cypress 1 Mbit SRAM](http://www.cypress.com/documentation/datasheets/cy7c1018dv33-cy7c1019dv33-1-mbit-128-k-8-static-ram) ## Protocol The device is controlled entirely via USB control messages. The command is encoded in the **request** value of the control message; **value** and **index** are unused. The following requests are defined: ### USB_TRANSFER (1) This tells the device to transfer the samples captured in memory to the host. This is called multiple times; the buffer memory is transferred 254 bytes at a time, with the address increasing automatically. The address is reset when a capture is started or settings are updated. ### USB_SETTINGS (2) Send new settings to the device. The settings consist of the following eight bytes sent along with the control request:  Byte | Description
---|---
0 | Bitmask of the channels to trigger on. All channels marked according to the trigger level must match before a trigger is considered to have fired.
1 | Level to trigger on (0 or 1).
2 | Delay after trigger, in milliseconds.
3 | Trigger count: number of times the trigger must fire before the capture starts.
4 | Sample rate, as follows:  | Value | Sample rate
---|---
80 | 50 MS/S
0 | 10 MS/S
1 | 5 MS/S
3 | 2.5 MS/S
9 | 1 MS/S
19 | 500 KS/S
39 | 250 KS/S
99 | 100 KS/S
5 | Number of samples to capture
6 | Start capture flag: a capture is started if this is not 0.
7 | Always 0.
### USB_STATUS (3) Returns a 2-byte status field. The first byte indicates whether capturing has finished (1) or not (0). The second byte is always 0. ### USB_CANCEL (4) This cancels a capture in progress. ## Resources \- [Manual](https://www.insidegadgets.com/wp-content/uploads/2015/03/Logic_Observer_v1.0_Manual_Rev2.pdf) \- [CPLD/MCU source code](https://www.insidegadgets.com/wp-content/uploads/2015/03/Logic_Observer_v1.0_Rev2.zip)
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=InsideGadgets_Logic_Observer&oldid=10939](https://OpenTraceLab.org/w/index.php?title=InsideGadgets_Logic_Observer&oldid=10939)"
: \- *Device* \- *Logic analyzer* \- *Planned*
## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
