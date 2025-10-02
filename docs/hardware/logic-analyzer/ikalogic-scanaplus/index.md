---
title: IKALOGIC ScanaPLUS
---

# IKALOGIC ScanaPLUS

<div class="infobox" markdown>

![IKALOGIC ScanaPLUS](./img/Ikalogic_scanaplus_xilinx_xc3s50an.jpg){ .infobox-image }

### IKALOGIC ScanaPLUS

| | |
|---|---|
| **Status** | supported |
| **Source code** | [ikalogic-scanaplus](https://github.com/OpenTraceLab/OpenTraceCapture/tree/main/src/hardware/ikalogic-scanaplus) |
| **Channels** | 9 |
| **Samplerate** | 100MHz |
| **Samplerate (state)** | — |
| **Triggers** | rising, falling, logic level, pulse width |
| **Min/max voltage** | -35V — 35V |
| **Threshold voltage** | configurable per channel-group: 1.2V, 1.5V, 1.8V, 2.8V, 3.3V to 5V |
| **Memory** | — |
| **Compression** | yes |
| **Website** | [ikalogic.com](http://www.ikalogic.com/ikalogic-products/scanaplus-9-channels-100mhz-logic-analyzer/) |

</div>

The **IKALOGIC ScanaPLUS** is a USB-based, 9-channel logic analyzer with up to 100MHz sampling rate.

See [IKALOGIC ScanaPLUS/Info](https://sigrok.org/wiki/IKALOGIC_ScanaPLUS/Info) for more details (such as **lsusb -vvv** output) about the device.

## Hardware
- **FPGA with 1Mbit flash memory**: [Xilinx XC3S50AN](http://www.xilinx.com/support/index.html/content/xilinx/en/supportNav/silicon_devices/fpga/spartan-3an.html) (markings: "Xilinx Spartan XC3S50AN QTG144AGQ1301 D4518897A 4C") ([datasheet](http://www.xilinx.com/support/documentation/data_sheets/ds557.pdf))
- **Hi-speed single-channel USB UART/FIFO**: [FTDI FT232H](http://www.ftdichip.com/Products/ICs/FT232H.htm) (markings: "FTDI D5RHQ.1 FT232HL 1230-B") ([datasheet](http://www.ftdichip.com/Support/Documents/DataSheets/ICs/DS_FT232H.pdf))
- 2x **4-bit dual-supply bus transceiver with configurable voltage translation & 3-state outputs**: [Texas Instruments SN74AVC4T774](http://www.ti.com/product/sn74avc4t774) (markings: "WT774 09K G4 CLS4") ([datasheet](http://www.ti.com/lit/gpn/sn74avc4t774))
- **Low-power dual op-amp**: [ST LM358](http://www.st.com/web/catalog/sense_power/FM123/SC61/SS1378/PF63721) (markings: "358 ET eZ022") ([datasheet](http://www.st.com/st-web-ui/static/active/en/resource/technical/document/datasheet/CD00000464.pdf))
- **2Kbit Microwire EEPROM**: [Microchip 93LC56B](http://www.microchip.com/wwwproducts/Devices.aspx?dDocName=en010906) (markings: "93LC56BI SN e3 1302 PVA") ([datasheet](http://ww1.microchip.com/downloads/en/DeviceDoc/21794G.pdf))
- **Dual 1.8V low-power push-pull output comparator**: [Microchip MCP6562](http://www.microchip.com/wwwproducts/Devices.aspx?dDocName=en539581) (markings: "MCP6562E SN e3 1301 RPH") ([datasheet](http://ww1.microchip.com/downloads/en/DeviceDoc/22139C.pdf))

## Photos

<div class="photo-grid" markdown>

[![Ikalogic Scanaplus Xilinx Xc3s50an](./img/Ikalogic_scanaplus_xilinx_xc3s50an.jpg)](./img/Ikalogic_scanaplus_xilinx_xc3s50an.jpg "Ikalogic Scanaplus Xilinx Xc3s50an"){ .glightbox data-gallery="ikalogic-scanaplus" }
<span class="caption">Ikalogic Scanaplus Xilinx Xc3s50an</span>

[![Ikalogic Scanaplus Package1](./img/Ikalogic_scanaplus_package1.jpg)](./img/Ikalogic_scanaplus_package1.jpg "Ikalogic Scanaplus Package1"){ .glightbox data-gallery="ikalogic-scanaplus" }
<span class="caption">Ikalogic Scanaplus Package1</span>

[![Ikalogic Scanaplus Device Connector](./img/Ikalogic_scanaplus_device_connector.jpg)](./img/Ikalogic_scanaplus_device_connector.jpg "Ikalogic Scanaplus Device Connector"){ .glightbox data-gallery="ikalogic-scanaplus" }
<span class="caption">Ikalogic Scanaplus Device Connector</span>

[![Ikalogic Scanaplus Package2](./img/Ikalogic_scanaplus_package2.jpg)](./img/Ikalogic_scanaplus_package2.jpg "Ikalogic Scanaplus Package2"){ .glightbox data-gallery="ikalogic-scanaplus" }
<span class="caption">Ikalogic Scanaplus Package2</span>

[![Ikalogic Scanaplus Ftdi Ft232hl](./img/Ikalogic_scanaplus_ftdi_ft232hl.jpg)](./img/Ikalogic_scanaplus_ftdi_ft232hl.jpg "Ikalogic Scanaplus Ftdi Ft232hl"){ .glightbox data-gallery="ikalogic-scanaplus" }
<span class="caption">Ikalogic Scanaplus Ftdi Ft232hl</span>

[![Ikalogic Scanaplus Device Open](./img/Ikalogic_scanaplus_device_open.jpg)](./img/Ikalogic_scanaplus_device_open.jpg "Ikalogic Scanaplus Device Open"){ .glightbox data-gallery="ikalogic-scanaplus" }
<span class="caption">Ikalogic Scanaplus Device Open</span>

[![Ikalogic Scanaplus Device Bottom](./img/Ikalogic_scanaplus_device_bottom.jpg)](./img/Ikalogic_scanaplus_device_bottom.jpg "Ikalogic Scanaplus Device Bottom"){ .glightbox data-gallery="ikalogic-scanaplus" }
<span class="caption">Ikalogic Scanaplus Device Bottom</span>

[![Ikalogic Scanaplus Device With Probes](./img/Ikalogic_scanaplus_device_with_probes.jpg)](./img/Ikalogic_scanaplus_device_with_probes.jpg "Ikalogic Scanaplus Device With Probes"){ .glightbox data-gallery="ikalogic-scanaplus" }
<span class="caption">Ikalogic Scanaplus Device With Probes</span>

[![Ikalogic Scanaplus St 358 Ez022](./img/Ikalogic_scanaplus_st_358_ez022.jpg)](./img/Ikalogic_scanaplus_st_358_ez022.jpg "Ikalogic Scanaplus St 358 Ez022"){ .glightbox data-gallery="ikalogic-scanaplus" }
<span class="caption">Ikalogic Scanaplus St 358 Ez022</span>

[![Ikalogic Scanaplus Microchip 93lc56bi](./img/Ikalogic_scanaplus_microchip_93lc56bi.jpg)](./img/Ikalogic_scanaplus_microchip_93lc56bi.jpg "Ikalogic Scanaplus Microchip 93lc56bi"){ .glightbox data-gallery="ikalogic-scanaplus" }
<span class="caption">Ikalogic Scanaplus Microchip 93lc56bi</span>

[![Ikalogic Scanaplus Mcp6562e](./img/Ikalogic_scanaplus_mcp6562e.jpg)](./img/Ikalogic_scanaplus_mcp6562e.jpg "Ikalogic Scanaplus Mcp6562e"){ .glightbox data-gallery="ikalogic-scanaplus" }
<span class="caption">Ikalogic Scanaplus Mcp6562e</span>

[![Ikalogic Scanaplus Ti Wt774 2](./img/Ikalogic_scanaplus_ti_wt774_2.jpg)](./img/Ikalogic_scanaplus_ti_wt774_2.jpg "Ikalogic Scanaplus Ti Wt774 2"){ .glightbox data-gallery="ikalogic-scanaplus" }
<span class="caption">Ikalogic Scanaplus Ti Wt774 2</span>

[![Ikalogic Scanaplus Device Top](./img/Ikalogic_scanaplus_device_top.jpg)](./img/Ikalogic_scanaplus_device_top.jpg "Ikalogic Scanaplus Device Top"){ .glightbox data-gallery="ikalogic-scanaplus" }
<span class="caption">Ikalogic Scanaplus Device Top</span>

[![Ikalogic Scanaplus Ti Wt774 1](./img/Ikalogic_scanaplus_ti_wt774_1.jpg)](./img/Ikalogic_scanaplus_ti_wt774_1.jpg "Ikalogic Scanaplus Ti Wt774 1"){ .glightbox data-gallery="ikalogic-scanaplus" }
<span class="caption">Ikalogic Scanaplus Ti Wt774 1</span>

[![Ikalogic Scanaplus Mugshot](./img/Ikalogic_scanaplus_mugshot.jpg)](./img/Ikalogic_scanaplus_mugshot.png "Ikalogic Scanaplus Mugshot"){ .glightbox data-gallery="ikalogic-scanaplus" }
<span class="caption">Ikalogic Scanaplus Mugshot</span>

[![Ikalogic Scanaplus Device Open2](./img/Ikalogic_scanaplus_device_open2.jpg)](./img/Ikalogic_scanaplus_device_open2.jpg "Ikalogic Scanaplus Device Open2"){ .glightbox data-gallery="ikalogic-scanaplus" }
<span class="caption">Ikalogic Scanaplus Device Open2</span>

[![Ikalogic Scanaplus Package3](./img/Ikalogic_scanaplus_package3.jpg)](./img/Ikalogic_scanaplus_package3.jpg "Ikalogic Scanaplus Package3"){ .glightbox data-gallery="ikalogic-scanaplus" }
<span class="caption">Ikalogic Scanaplus Package3</span>

[![Ikalogic Scanaplus Pcb Top](./img/Ikalogic_scanaplus_pcb_top.jpg)](./img/Ikalogic_scanaplus_pcb_top.jpg "Ikalogic Scanaplus Pcb Top"){ .glightbox data-gallery="ikalogic-scanaplus" }
<span class="caption">Ikalogic Scanaplus Pcb Top</span>

[![Ikalogic Scanaplus Pcb Bottom](./img/Ikalogic_scanaplus_pcb_bottom.jpg)](./img/Ikalogic_scanaplus_pcb_bottom.jpg "Ikalogic Scanaplus Pcb Bottom"){ .glightbox data-gallery="ikalogic-scanaplus" }
<span class="caption">Ikalogic Scanaplus Pcb Bottom</span>

[![Ikalogic Scanaplus Device Usb](./img/Ikalogic_scanaplus_device_usb.jpg)](./img/Ikalogic_scanaplus_device_usb.jpg "Ikalogic Scanaplus Device Usb"){ .glightbox data-gallery="ikalogic-scanaplus" }
<span class="caption">Ikalogic Scanaplus Device Usb</span>

[![Ikalogic Scanaplus Package Contents](./img/Ikalogic_scanaplus_package_contents.jpg)](./img/Ikalogic_scanaplus_package_contents.jpg "Ikalogic Scanaplus Package Contents"){ .glightbox data-gallery="ikalogic-scanaplus" }
<span class="caption">Ikalogic Scanaplus Package Contents</span>

</div>
## Protocol

The IKALOGIC ScanaPLUS **always** acquires samples at 100MHz (on all 9 channels at once), it is [not possible to change that](http://www.ikalogic.com/faq/modify-sampling-rate-scanaplus/). However, the USB traffic is still reduced a bit due to the use of compression.

The highest supported, continuously-applying frequency of the input signal(s) for the ScanaPLUS is [roughly 10MHz](http://www.ikalogic.com/faq/maximum-frequency-captured-scanaplus/) (say, a 10MHz SPI clock). For faster signals the USB bandwidth starts to become too limited and samples will be lost, which is (as far as we know) undetectable for the host software, thus the user can see captured data that is not actually correct. Note that it **is** possible to capture signals faster than 10MHz correctly in some situations, if that data only appears in small bursts (and not continuously).

### FTDI chip init

The ScanaPLUS is connected to the PC via an FTDI FT232H chip (we use libftdi to talk to it) that gets configured to "Sync FIFO" mode by the software, allowing theoretical transfer speeds up to 40 Mbyte/second. The FT232H uses the standard VID/PID of 0403:6014, but has an **iProduct** field that contains the string "SCANAPLUS" so we can reliably say whether a given device with 0403:6014 as VID/PID is a ScanaPLUS or not. The device also has a proper **iSerial**, allowing to even uniquely distinguish two different ScanaPLUS devices connected to the same PC.

During init, the FT232's "interface A" (the only one in this IC) has to be selected and opened. Then, the RX/TX buffers are purged, to eliminate "old" data (if any) from the buffers.

The chip is then put into "Sync FIFO" mode, by first resetting the so-called "bitmode", then setting it to "Sync FIFO" (as per FTDI datasheet).

The FTDI chip latency timer is set to the lowest-possible value of 2ms (the hardware default is 16ms). What this does is that the IC will send data to the host either when the requested amount of bytes is reached (or buffers are full), or when 2ms have passed since the last time bytes were sent to the host, whichever happens first. This has performance/latency advantages (see [AN_107](http://www.ftdichip.com/Support/Documents/AppNotes/AN_107_AdvancedDriverOptions_AN_000073.pdf) section 6.3, [AN232B-04](http://www.ftdichip.com/Support/Documents/AppNotes/AN232B-04_DataLatencyFlow.pdf), and [AN232B-03](http://www.ftdichip.com/Support/Documents/AppNotes/AN232B-03_D2XXDataThroughput.pdf)), but it also [prevents the device from ever being put into USB suspend](http://www.ftdichip.com/Support/FAQs.htm#HwGen2).

Finally, the read data chunk size is set to 64kB.

#### EEPROM

The ScanaPLUS has an I2C EEPROM connected to the FTDI FT232H which contains some parameters the FT232H uses.

Additionally, three bytes in the ["user area" of the EEPROM](http://www.ftdichip.com/Documents/AppNotes/AN_121_FTDI_Device_EEPROM_User_Area_Usage.pdf) are ScanaPLUS-specific. We're referring to them as the "magic bytes", since they seem to be different in each ScanaPLUS device, probably representing some kind of serial number or such. They have to be read from the EEPROM and sent (slightly modified) to the FPGA via a certain method, in order for the sampling to work later. If they're not sent, or the incorrect bytes are sent, the sampling will basically appear to work, but all probe values will be low (0), no matter which signal is actually applied to the probes.

The three bytes are located at [EEPROM index 16 and 17](http://sigrok.org/gitweb/?p=libsigrok.git;a=blob;f=hardware/ikalogic-scanaplus/protocol.c;h=86597850afe2ab0d77e3d5947a6b2a1c1ad1177a;hb=HEAD#l127) (the EEPROM is read in 16-bit units, so those two indices will yield 4 bytes, one of which is irrelevant).

Note: Bit 7 of the three bytes must not be used, apparently. Even though the three bits can be either 0 or 1 (we've seen both in actual ScanaPLUS devices), the device ID as sent to the FPGA has bit 7 of each byte zero'd out. It is unknown whether bit 7 of these bytes has any meaning, whether it's used somewhere, or whether it can be simply ignored.

### Command format

The commands sent to the FPGA (via the FT232H) seem to always consist of two bytes.

The first byte is probably an identifier for the command to execute and seems to always have the high nibble set to 0x8 and/or bit 7 must always be set (?), i.e., possible commands seem to range from 0x80-0x8f. The second byte is then usually the data byte or parameter belonging to the command, and it seems to always have bit 7 cleared (?)

### Initialization

First a 2-byte sequence is sent.

| Byte | Description |
|---|---|
| **0x88** | ? |
| 0x41 | ? |

The following 4-byte sequence probably sets default logic level thresholds for the probes (?)

| Byte | Description |
|---|---|
| **0x89** | ? |
| 0x64 | ? |
| **0x8a** | ? |
| 0x64 | ? |

Then the initial 2-byte sequence is sent again.

| Byte | Description |
|---|---|
| **0x88** | ? |
| 0x41 | ? |

It is followed by an 8-byte sequence.

| Byte | Description |
|---|---|
| **0x8d** | ? |
| 0x01 | ? |
| **0x8d** | ? |
| 0x05 | ? |
| **0x8d** | ? |
| 0x01 | ? |
| **0x8d** | ? |
| 0x02 | ? |

Next, a sequence of 57 chunks of 4 bytes each are transferred in a loop. The 4 bytes are:

| Byte | Description |
|---|---|
| **0x8d** | ? |
| 0x06 | ? |
| **0x8d** | ? |
| 0x02 | ? |

Finally, another 2-byte sequence finished the initialization.

| Byte | Description |
|---|---|
| **0x88** | ? |
| 0x40 | ? |

### Starting an acquisition

An acquisition is started by sending a certain sequence of bytes to the FT232H as follows.

First, 4 bytes are sent which configure the probe group voltage thresholds.

| Byte | Description |
|---|---|
| **0x89** | This is the "set threshold for probes 1-4" command. |
| 0x7f | TODO. |
| **0x8a** | This is the "set threshold for probes 5-9" command. |
| 0x7f | TODO. |

Then, two bytes are sent which configure how probes 5/6 and 7/8 should work.

| Byte | Description |
|---|---|
| **0x88** | This is the "configure probes 5/6 and 7/8" command. |
| ? | TODO. |

Before setting the 3 magic bytes, they are first cleared to 0x00.

| Byte | Description |
|---|---|
| **0x8c** | This is the "set magic byte 1" command. |
| 0x00 | Set the magic byte to 0x00. |
| **0x8e** | This is the "set magic byte 2" command. |
| 0x00 | Set the magic byte to 0x00. |
| **0x8f** | This is the "set magic byte 3" command. |
| 0x00 | Set the magic byte to 0x00. |

Finally, the 3 magic bytes (see above) are set.

| Byte | Description |
|---|---|
| **0x8c** | This is the "set magic byte 1" command. |
| *0xQQ* |  |
| **0x8e** | This is the "set magic byte 2" command. |
| *0xRR* |  |
| **0x8f** | This is the "set magic byte 3" command. |
| *0xSS* |  |

After the acquisition starts, a bunch of samples will be returned as all-zero, no matter which signals are actually present on the probes. This is probably due to the FPGA reconfiguring some of its internal state/config during this time. As far as we know there is apparently no way for the PC-side to know when this "reconfiguration" starts or ends. The FTDI chip will return all-zero "dummy" samples during this time, which is indistinguishable from actual all-zero samples.

We currently simply ignore the first 64kB of data (in the libsigrok driver) after an acquisition starts. Empirical tests have shown that the "reconfigure" time is a lot less than that usually.

### Sample format and compression

After an acquisition has started, compressed samples are streamed to the PC continously.

A compressed chunk consists of two bytes. Bits [7:1] of the high byte encode how many samples this compressed chunk consists of (0-127). Bit 0 of the high byte and bits [7:0] of the low byte encode the states of the 9 probes (high/1 or low/0). Bit 0 of the low byte is the value of probe 1, Bit 7 of the low byte is the value of probe 8, and bit 0 of the high byte is probe 9.

Examples:

- **0xfe 0x00** means "127 sample periods ((0xfe >> 1) = 0x7f = 127) all 9 probes were low (0x00 0x00)".
- **0x30 0x07** means "24 sample periods ((0x30 >> 1) = 0x18 = 24) probes 1,2,3 were high and all others were low (0x00 0x07)".
- **0x31 0x07** means "24 sample periods ((0x31 >> 1) = 0x18 = 24) probes 1,2,3,9 were high and all others were low (0x01 0x07)".

The FPGA will always try to return as many samples as possible in a 2-byte compressed chunk. Let's assume data for 254 sample periods will be gathered. If during this time all probes are of the same value (e.g. low), the returned values will be **0xfe 0x00 0xfe 0x00** (4 bytes). If the probe values are always 0b000101010 during this time (probes 2,4,6 high and all others low), the returned values would be **0xfe 0x2a 0xfe 0x2a** (4 bytes).

However, the more transitions occur duing the sampling time, i.e. the fewer sample values are the same for consecutive sample periods, the more bytes are needed to encode the compressed chunks. For example, if probe 3 is high for 50 periods, low for the next 50 periods, high for 50 periods, low for 50 periods, high for 50 periods, and low for the remaining 4 periods (all other probes low), this would yield **0x64 0x04 0x64 0x00 0x64 0x04 0x64 0x00 0x64 0x04 0x08 0x00** (12 bytes). It is easy to see that with increasing number of transitions (worse, if there are transitions on multiple probes even) the number of bytes required to encode the probe values into compressed chunks will increase dramatically. At some point the limited USB bandwidth (together with potential delays in reading and processing the data in software) will no longer be sufficient to transmit the number of bytes that would be required within a certain amount of time.

This is why the vendor states that for continuous input signals of frequencies higher than [roughly 10MHz](http://www.ikalogic.com/faq/maximum-frequency-captured-scanaplus/) the displayed sample data may no longer be correct in some cases. It **could** be correct for frequencies even higher than 10MHz though, if that 10MHz data is not continuously applied but rather only in short bursts, with pauses between the bursts.

### Triggers

Triggering seems to be a pure software function, the device/protocol doesn't seem to support any hardware-based triggering. Samples are continuously streamed to the PC, which then checks for the trigger conditions in that data "manually" in software.

## Resources
- [Specification](http://www.ikalogic.com/wp-content/uploads/ScanaPLUS_spec_sheet.pdf)
- [Manual](http://www.ikalogic.com/ikalogic-products/scanastudio-2/scanastudio-help-scanaplus-workspace/)
- [Vendor software](http://www.ikalogic.com/ikalogic-products/scanastudio-2/)

