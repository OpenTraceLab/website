# Noname Xl Logic16 100M
**Noname XL-LOGIC16-100M** [*Image: \1* |
---|---
Status | in progress
Source code | [saleae-logic16](http://github.com/OpenTraceLab/?p=OpenTraceCapture.git;a=tree;f=src/hardware/saleae-logic16)
Channels | 3/6/9/16
Samplerate | 100/50/32/16MHz
Samplerate (state) | —
Triggers | none (SW-only)
Min/max voltage | -0.9V — 6V
Threshold voltage | configurable:
for 1.8V to 3.6V systems: VIH=1.4V, VIL=0.7V
for 5V systems: VIH=3.6V, VIL=1.4V
Memory | none
Compression | yes
Price range | $30 - $35
Website | *aliexpress.com*
**Noname XL-LOGIC16-100M** The **Noname XL-LOGIC16-100M** is a USB-based, 16-channel logic analyzer with up to 100MHz sampling rate. It is labelled and sold as a *Saleae Logic16* clone, and comes with "modified" Saleae Logic software on a CD-ROM. See *Noname XL-LOGIC16-100M/Info* for more details (such as **lsusb -v** output) about the device.
## Contents
\- *1 Variants in same case* \- *2 Hardware* \- *3 Photos* \- *4 Firmware* \- *5 Protocol* \- *6 Resources*
## Variants in same case The 2015-1-8 version of the *Mcupro_Logic16_clone* comes in the same case as this device. Unlike this device, the mcupro version works with OpenTraceLab! ## Hardware A single Phillips head screw holds the case together. Most notable are the complete lack of test points or programming headers! There are some unpopulated resistor/capacitor pairs on the backside. \- **FPGA**: *Xilinx Spartan-3A XC3S200A*, 200K gates ([datasheeet](http://www.xilinx.com/support/documentation/data_sheets/ds529.pdf)) \- **USB interface chip**: [Cypress CY7C68013A-56PVXC (FX2LP)](http://www.cypress.com/?mpn=CY7C68013A-56PVXC) ([datasheet](http://www.cypress.com/?docID=34060)) \- **I2C EEPROM**: 2Kbit [Atmel 24C02B](http://www.atmel.com/devices/AT24C02B.aspx) (markings: "ATMEL317 24C02BN SU27 D") ([datasheet](http://www.atmel.com/Images/doc5126.pdf)) \- **16-Bit 2.5V to 3.3V/3.3V to 5V level shifting transceiver with 3-state outputs**: [TI SN74ALVC164245](http://www.ti.com/product/SN74ALVC164245) ([datasheet](http://www.ti.com/lit/gpn/sn74alvc164245)) \- **3.3V voltage regulator**: *Advanced Monolithic Systems AMS1117-3.3* ([datasheet](http://ams-semitech.com/attachments/File/AMS1117_20120314.pdf), [older datasheet](http://www.advanced-monolithic.com/pdf/ds1117.pdf)) \- **1.2V voltage regulator**: *Advanced Monolithic Systems AMS1117-1.2* ([datasheet](http://ams-semitech.com/attachments/File/AMS1117_20120314.pdf), [older datasheet](http://www.advanced-monolithic.com/pdf/ds1117.pdf)) \- **Crystal:** 24.000 Three LEDs (USB/green, COM/blue, and RUN/red) are on the board. ## Photos \-
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
\-
[*Image: \1*
\-
[*Image: \1*
**Photos from another unit:** \-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
**Photos from yet another unit (with JTAG and other resistor values):** \-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
**Photos from yet another unit (with black case):** \-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
## Firmware You can use the [OpenTraceLab-fwextract-saleae-logic16](http://github.com/OpenTraceLab/?p=OpenTraceLab-util.git;a=tree;f=firmware/saleae-logic16) tool to extract (from the "Logic" Linux binary) the FX2 firmware and the FPGA bitstreams, exactly *as for a real Saleae Logic16*. Note, the md5sum of the FX2 firmware is identical to the original Saleae firmware, but the FPGA bitstreams are different. Attempting to connect to this device with the "modified" FPGA bitstream, which \\_works\\_ with the vendor supplied "modified" Logic software fails to load in OpenTraceLab, with a FPGA version mismatch. The FX2 firmware loads successfully, at least in as much as the LED blinks a heartbeat pattern as expected. Update: July 4, 2015: marcus_c has written some open source fpga bitstream for spartan based logic16s, and \\_this\\_ bitstream does work with this device. However, at this time, binaries are not available. See [[1]](https://github.com/zeldin/logic16_bitstream) for the source. Update: September 3, 2015 blight has an alternative open source fpga bitstream. It also works. See [[2]](https://github.com/gregani/la16fw) for both source and binaries ## Protocol See *Saleae Logic16#Protocol*. ## Resources \- Random aliexpress.com vendors: *vendor1*, *vendor2*
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=Noname_XL-LOGIC16-100M&oldid=14397](https://OpenTraceLab.org/w/index.php?title=Noname_XL-LOGIC16-100M&oldid=14397)"
: \- *Device* \- *Logic analyzer* \- *In progress*
## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
