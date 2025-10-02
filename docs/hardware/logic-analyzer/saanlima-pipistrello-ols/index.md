---
title: Saanlima Pipistrello OLS
---

# Saanlima Pipistrello OLS

<div class="infobox" markdown>

![Saanlima Pipistrello OLS](./img/Saanlima_Pipistrello-OLS.png){ .infobox-image }

### Saanlima Pipistrello OLS

| | |
|---|---|
| **Status** | supported |
| **Source code** | [pipistrello-ols](https://github.com/OpenTraceLab/OpenTraceCapture/tree/main/src/hardware/pipistrello-ols) |
| **Channels** | 32 |
| **Samplerate** | 0-100MHz |
| **Samplerate (state)** | — |
| **Triggers** | value, rising/falling edge |
| **Min/max voltage** | 0V — 5V |
| **Memory** | 64MiB |
| **Compression** | yes |
| **Website** | [saanlima.com](http://pipistrello.saanlima.com/index.php?title=Welcome_to_Pipistrello) |

</div>

The **Saanlima Pipistrello** is an FPGA development board with many on-board peripherals and pin headers compatible with the [Papilio](http://www.gadgetfactory.net/papilio/) series of boards. It has USB connectivity to a host PC, and, by adding the [Saanlima buffer wing](http://saanlima.com/store/index.php?route=product/product&product_id=55), can be used as a replacement for the [Openbench Logic Sniffer](https://sigrok.org/wiki/Openbench_Logic_Sniffer) (OLS).

The FPGA firmware for the OLS has been ported for the Pipistrello, and can thus use the full 64MiB memory to store samples. It also has triggers on rising/falling edges as an extra feature. 

All design source for the Pipistrello, including schematics and Eagle board files, are available under the [CC-BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.

See [Saanlima Pipistrello OLS/Info](https://sigrok.org/wiki/Saanlima_Pipistrello_OLS/Info) for more details (such as **lsusb -v** output) about the device.

## Hardware

**Pipistrello 2.0 board**

- [Xilinx Spartan-6 LX45](http://www.xilinx.com/support/documentation/data_sheets/ds160.pdf) FPGA
- [Micron N25Q128A13ESE40G](http://www.micron.com/-/media/documents/products/data%20sheet/nor%20flash/serial%20nor/n25q/n25q_128mb_3v_65nm.pdf) 16MiB Flash
- [Micron MT46H32M16LFBF-5](http://www.micron.com/-/media/documents/products/data%20sheet/dram/mobile%20dram/low-power%20dram/lpddr/60-series/t67m_512mb_mobile_lpddr_sdram.pdf) 64MiB DRAM
- [FTDI FT2232H](http://www.ftdichip.com/Support/Documents/DataSheets/ICs/DS_FT2232H.pdf) USB interface

**Buffer wing**

- 2 x [NXP 74LVC16245A](http://www.nxp.com/documents/data_sheet/74LVC_LVCH16245A.pdf) 16-bit 5V-tolerant transceivers
## Protocol

The protocol used is the same as the [OLS protocol](https://sigrok.org/wiki/Openbench_Logic_Sniffer#Protocol), with the addition of commands for edge triggers. See the source code for details.

The Pipistrello needs to be manually flashed with a FPGA bitstream to work with sigrok. These bitstreams can be downloaded from [the Pipistrello wiki](http://pipistrello.saanlima.com/index.php?title=Pipistrello_as_Logic_Analyzer) and the source code is available (see [bug #1021](https://sigrok.org/bugzilla/show_bug.cgi?id=1021) about possible automation for for this).

**Important**: The Pipistrello OLS driver [only supports using the FIFO mode bitstream](http://forum.gadgetfactory.net/index.php?/topic/1864-fpga-as-usb-pia/&do=findComment&comment=18847) and the FTDI chip has been switched to FIFO mode. If using the UART mode bitstream, use the [Openbench Logic Sniffer](https://sigrok.org/wiki/Openbench_Logic_Sniffer) driver **instead** (see [bug #1020](https://sigrok.org/bugzilla/show_bug.cgi?id=1020) about automated detection for this).

## Photos

<div class="photo-grid" markdown>

[![Saanlima Pipistrello Ols](./img/Saanlima_Pipistrello-OLS.png)](./img/Saanlima_Pipistrello-OLS.png "Saanlima Pipistrello Ols"){ .glightbox data-gallery="saanlima-pipistrello-ols" }
<span class="caption">Saanlima Pipistrello Ols</span>

[![Saanlima Pipistrello](./img/Saanlima_Pipistrello.jpg)](./img/Saanlima_Pipistrello.jpg "Saanlima Pipistrello"){ .glightbox data-gallery="saanlima-pipistrello-ols" }
<span class="caption">Saanlima Pipistrello</span>

[![Saanlima Pipistrello Buffer Wing](./img/Saanlima_Pipistrello_buffer_wing.jpg)](./img/Saanlima_Pipistrello_buffer_wing.jpg "Saanlima Pipistrello Buffer Wing"){ .glightbox data-gallery="saanlima-pipistrello-ols" }
<span class="caption">Saanlima Pipistrello Buffer Wing</span>

</div>
## Resources
- [Saanlima Pipistrello](http://pipistrello.saanlima.com/index.php?title=Welcome_to_Pipistrello)
- [Pipistrello support forum](http://saanlima.com/forum/viewforum.php?f=3&sid=d8f2eaf446327493dd36a7132da1cc52)

