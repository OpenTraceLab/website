# Hantek 4032L

| | | |:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------------------------:| | [![\1](../../assets/hardware/general/\2)](./File:Hantek_4032l_mugshot.png.html) | | | Status | supported | | Source code | [hantek-4032l](http://github.com/OpenTraceLab/?p=OpenTraceCapture.git;a=tree;f=src/hardware/hantek-4032l) | | Channels | 32 | | Samplerate | 400MHz | | Samplerate (state) | ? | | Triggers | edge, bus value range, pattern, pattern duration, combined | | Min/max voltage | -6V — +60V input, -6V — +6V threshold | | Memory | 2Gbit (64M samples x 32) | | Compression | — | | Website | [hantek.com](http://www.hantek.com/en/ProductDetail_16_14.html) | **Hantek 4032L** The [Hantek 4032L](http://www.hantek.com/en/ProductDetail_16_14.html) is a USB-based, 32-channel logic analyzer with up to 400MHz sampling rate and 2Gbit DDR2 memory. See [Hantek 4032L/Info](Hantek_4032L/Info.html "Hantek 4032L/Info") for more details (such as **lsusb -v** output) on the device. 
## Contents 
\- [1 Hardware](Hantek_4032L.html#Hardware) \- [2 Photos](Hantek_4032L.html#Photos) \- [3 Protocol](Hantek_4032L.html#Protocol) \- [3.1 Vendor requests](Hantek_4032L.html#Vendor_requests) \- [3.2 Command/Parameters packet](Hantek_4032L.html#Command/Parameters_packet) \- [3.2.1 Commands and responses](Hantek_4032L.html#Commands_and_responses) \- [3.3 Acquisition session flow](Hantek_4032L.html#Acquisition_session_flow) \- [4 Hardware features support status](Hantek_4032L.html#Hardware_features_support_status) 
## Hardware \- Xilinx Spartan-6 XC6SLX16 CSG324 DIV1225 (FPGA, 14579 logic cells, 2 DDR1/2/3 memory controllers, BGA324) \- Cypress FX2LP CY7C68013A-100AXC (USB 2.0 HS controller, TQFP100) \- 2x Micron MT47H64M16HR-25E:H (1Gbit DDR2 SDRAM, BGA) \- TI TPS51116 (DDR memory power controller) \- Unknown I2C EEPROM (marking removed, contains FX2 firmware) \- MXIC MX25L4005 (4Mbit SPI flash, marking removed, contains FPGA bitstream) \- DAC122S085CIMM (marking removed, input Vref generators) ## Photos **Teardown 1**: \- 
[![\1](../../assets/hardware/general/\2)](./File:Hantek_4032l_package.jpg.html)
Package
\- 
[![\1](../../assets/hardware/general/\2)](./File:Hantek_4032l_package_contents.jpg.html)
Package contents
\- 
[![\1](../../assets/hardware/general/\2)](./File:Hantek_4032l_device_top.jpg.html)
Device, top
\- 
[![\1](../../assets/hardware/general/\2)](./File:Hantek_4032l_device_bottom.jpg.html)
Device, bottom
\- 
[![\1](../../assets/hardware/general/\2)](./File:Hantek_4032l_usb_connector.jpg.html)
USB connector
\- 
[![\1](../../assets/hardware/general/\2)](./File:Hantek_4032l_probe_connector.jpg.html)
Probe connector
\- 
[![\1](../../assets/hardware/general/\2)](./File:Hantek_4032l_pcb_top.jpg.html)
PCB, top
\- 
[![\1](../../assets/hardware/general/\2)](./File:Hantek_4032l_pcb_bottom.jpg.html)
PCB, bottom
\- 
[![\1](../../assets/hardware/general/\2)](./File:Hantek_4032l_xilinx_xc6slx16.jpg.html)
Xilinx XC6SLX16
\- 
[![\1](../../assets/hardware/general/\2)](./File:Hantek_4032l_cypress_fx2.jpg.html)
Cypress FX2
\- 
[![\1](../../assets/hardware/general/\2)](./File:Hantek_4032l_micron_ddr2_sdram2.jpg.html)
DDR2 SDRAM
\- 
[![\1](../../assets/hardware/general/\2)](./File:Hantek_4032l_micron_ddr2_sdram1.jpg.html)
DDR2 SDRAM
\- 
[![\1](../../assets/hardware/general/\2)](./File:Hantek_4032l_tps51116.jpg.html)
TI TPS51116
\- 
[![\1](../../assets/hardware/general/\2)](./File:Hantek_4032l_ti_tps54286.jpg.html)
TI TPS54286
\- 
[![\1](../../assets/hardware/general/\2)](./File:Hantek_4032l_spi_flash_chip.jpg.html)
SPI flash
\- 
[![\1](../../assets/hardware/general/\2)](./File:Hantek_4032l_mornsun_a0512s-1wr2.jpg.html)
Mornsun A0512S-1WR2
\- 
[![\1](../../assets/hardware/general/\2)](./File:Hantek_4032l_50mhz_crystal.jpg.html)
50MHz crystal
\- 
[![\1](../../assets/hardware/general/\2)](./File:Hantek_4032l_unknown_chips1.jpg.html)
Unknown chips
\- 
[![\1](../../assets/hardware/general/\2)](./File:Hantek_4032l_unknown_chips2.jpg.html)
Unknown chips
\- 
[![\1](../../assets/hardware/general/\2)](./File:Hantek_4032l_unknown_chips3.jpg.html)
Unknown chips
**Teardown 2**: \- 
[![\1](../../assets/hardware/general/\2)](./File:Hantek4032L_BoxSideView.png.html)
Device, top
\- 
[![\1](../../assets/hardware/general/\2)](./File:Hantek4032L_BoxIso.png.html)
Device, with probes
\- 
[![\1](../../assets/hardware/general/\2)](./File:Hantek4032L_BoxPortSide.png.html)
Probe port side
\- 
[![\1](../../assets/hardware/general/\2)](./File:Hantek4032L_BoxUsbSide.png.html)
PC USB port side
\- 
[![\1](../../assets/hardware/general/\2)](./File:Hantek4032L_PcbTop.png.html)
PCB, top
\- 
[![\1](../../assets/hardware/general/\2)](./File:Hantek4032L_PcbBottom.png.html)
PCB, bottom
## Protocol \- Vendor request is used to reset the engine and flush the buffers \- Endpoint 2 is used for host-to-device command/parameters transfers \- Endpoint 6 is used for device-to-host status/data transfers X denotes "any value" in the following description ### Vendor requests \- bRequest=0xB3, wValue=X, wIndex=X, wLength=0x0A, data={ 0x0F, 0x03, 0x03, 0x03, X, X, X, X, X, X } - restart the engine (reset FPGA, reset FIFOs) \- bRequest=0xD0, wValue=X, wIndex=X, wLength=0x00 - disable communication (set FIFO reset), not used \- bRequest=0xD1, wValue=X, wIndex=X, wLength=0x00 - enable communication (clear FIFO reset), not used ### Command/Parameters packet struct CmdParamsPacket byte Magic[2]={ 0x7F, 0x01 } byte SampleRate 0x22 - 400MS/s 0x23 - 320MS/s 0x20 - 200MS/s 0x21 - 160MS/s 0x00 - 100MS/s 0x08 - 80MS/s 0x01 - 50MS/s 0x09 - 40MS/s 0x02 - 25MS/s 0x0A - 20MS/s 0x03 - 12.5MS/s 0x0B - 10MS/s 0x04 - 6.25MS/s 0x0C - 5MS/s 0x10 - 4MS/s 0x05 - 3.125MS/s 0x0D - 2.5MS/s 0x11 - 2MS/s 0x06 - 1.5625MS/s 0x0E - 1.25MS/s 0x12 - 1MS/s 0x07 - 781.25KS/s 0x0F - 625KS/s 0x13 - 500KS/s 0x14 - 250KS/s 0x15 - 125KS/s 0x16 - 62.5KS/s 0x17 - 31.25KS/s 0x18 - 16KS/s 0x19 - 8KS/s 0x1A - 4KS/s 0x1B - 2KS/s 0x1C - 1KS/s 0x24 - posedge CLKA 0x25 - posedge CLKB 0x28 - negedge CLKA 0x29 - negedge CLKB 0x26 - DDR CLKA 0x27 - DDR CLKB byte TrigFlags bit 0 - enable trigger 1 (main) bit 1 - enable trigger 2 (advanced) bit 2 - trigger logic, 0 - T1 or T2, 1 - T1 and T2 bit 3 - unknown USBXI sync trigger config, default: 1 bit 4 - unknown USBXI sync trigger config, default: 0 bit 7 - unknown USBXI "check mode", default: 0 word PwmA - channel A Vref PWM value, pseudocode: -6V < ThresholdVoltage < +6V Vref = 1.8-ThresholdVoltage if Vref>10.0 Vref = 10.0 if Vref<-5.0 Vref = -5.0 pwm = ToInt((Vref + 5.0) / 15.0 * 4096.0) if pwm>4095 pwm = 4095 word PwmB - channel B Vref PWM value byte UsbxiData - unknown USBXI parameter, default: 00 byte unused: 00 dword SampleDepth - sample depth in bits per channel, 2k-64M, must be multiple of 512 dword PretriggerDepth - pretrigger buffer depth in bits, must be < SampleDepth struct Trig Trig1 - trigger 1 config, see below struct Trig Trig2 - trigger 2 config, see below byte Command[2] - command, see Commands and responses below struct Trig dword Flags - trigger types selection: bit 4:0 - edge trigger signal, 0-31 -> A0-B15 bit 6:5 - edge to trigger on: 00 - rise 01 - fall 10 - rise or fall 11 - edge trigger disabled bit 7 - unused bit 9:8 - data range trigger type: 00 - data=RangeMax trigger 01 - data=RangeMin or data=RangeMax trigger 10 - dataRangeMax trigger 11 - RangeMinTimeMax trigger 11 - TimeMin masked_value=00000101 (bits 6,1,0 are combined and zero-extended) #### Commands and responses { 0x1A, 0x2B } - configure and start capture, all parameters are used Response: none { 0x3A, 0x4B } - get status, parameters are defaults Response: dword Magic=0x2B1A037F - drop rx data until this) dword CurrentDataValue - A0-B15 current state snapshot dword CaptureStatus - 0-not finished, 1-?, 2-done, data is ready dword UsbxiData - unknown USBXI data dword DevVersion - FPGA firmware version dword DummyData[251] - pad to 1024 bytes { 0x5A, 0x6B } - get captured data, parameters are defaults Response: dword Magic=0x2B1A027F - drop rx data until this dword CaptureData[SampleDepth] - capture data dword EndMarker=0x4D3C037F - drop rx data after this till end of 512 byte packet { 0x9A, 0xAB } - unknown USBXI "eraser data" cmd, parameters are defaults Response: none { 0xBA, 0xCB } - unknown USBXI "set sync trig output" cmd, parameters are defaults Response: none ### Acquisition session flow \- Send restart vendor request (0xB3) \- Send { 0x1A, 0x2B } type packet to configure and start capture \- Poll with { 0x3A, 0x4B } until CaptureStatus=2 (optionally blink bus indicators according to CurrentDataValue during poll) \- Get capture data with { 0x5A, 0x6B } ## Hardware features support status \+ Buffered mode acquisition \+ Sample depth selection \+ Pretrigger depth selection \+ Internal clocking (timing mode) \+ External clocking (state mode) with edge (rising/falling/both) and clock channel (ACLK/BCLK) selection \+ Logic voltage threshold selection (independent for Axx and Bxx channel groups, possible to analyze dual standard circuits) \+ Unconditional trigger \+ Trigger on signal edge (rising/falling/any) \+ Trigger on bus pattern match \- Trigger on bus value within/out of range \- Trigger on bus pattern condition (match/within/out of range) repeating for N consecutive samples where N is equal/within range/out of range \- Trigger on bus pattern condition at specific signal edge \- Trigger on any of the above conditions combined with pattern match on the previous/current/next sample \- Use two trigger units in AND/OR combination \- External trigger input/output signals 
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=Hantek_4032L&oldid=14464](https://OpenTraceLab.org/w/index.php?title=Hantek_4032L&oldid=14464)" 
[Categories](specialcategories-specialcategories.md): \- [Device](./Category:Device.html "Category:Device") \- [Logic analyzer](./Category:Logic_analyzer.html "Category:Logic analyzer") \- [Supported](./Category:Supported.html "Category:Supported")

## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
