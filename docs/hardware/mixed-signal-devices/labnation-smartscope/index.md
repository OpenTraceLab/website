---
title: LabNation SmartScope
---

# LabNation SmartScope

<div class="infobox" markdown>

![LabNation SmartScope](./img/Lab_nation_smartscope_pcb_top.jpg){ .infobox-image }

### LabNation SmartScope

| | |
|---|---|
| **Status** | planned |
| **Channels** | 8 |
| **Samplerate** | 100MHz |
| **Samplerate (state)** | — |
| **Triggers** | low, high, rising, falling, edge |
| **Min/max voltage** | ? |
| **Threshold voltage** | Fixed: VIL=0.8V, VIH=2.0V |
| **Memory** | 4Msamples (8MByte SDRAM) |
| **Compression** | ? |
| **Website** | [lab-nation.com](https://www.lab-nation.com) |

</div>

The **LabNation SmartScope** is a USB-based mixed-signal oscilloscope (100 MS/s, 45MHz bandwidth), 8-channel logic analyzer (100MHz), arbitrary waveform generator / function generator.

See [LabNation SmartScope/Info](https://sigrok.org/wiki/LabNation_SmartScope/Info) for some more details (such as **lsusb -v** output) on the device.

## Hardware
- **FPGA (3840 logic cells)**: [Xilinx XC6SXL4](http://www.xilinx.com/products/silicon-devices/fpga/spartan-6/lx.html) ([datasheet](http://www.xilinx.com/support/documentation/data_sheets/ds160.pdf))
- **64Mbit SDRAM**: [Alliance Memory AS4C4M16S](http://www.alliancememory.com/datasheets/AS4C4M16S.asp) ([datasheet](http://www.alliancememory.com/pdf/dram/64M-AS4C4M16S.pdf))
- **Dual-channel, 8-bit, 100Msps ADC**: [Maxim MAX19506](http://www.maximintegrated.com/en/products/analog/data-converters/analog-to-digital-converters/MAX19506.html) ([datasheet](http://datasheets.maximintegrated.com/en/ds/MAX19506.pdf))
- **8-bit microcontroller with full-speed USB**: [Microchip PIC18F14K50](http://www.microchip.com/wwwproducts/Devices.aspx?dDocName=en533924) ([datasheet](http://ww1.microchip.com/downloads/en/DeviceDoc/41350E.pdf))
- **Single-pole normally-closed SOP OptoMOS relay**: [Ixys CPC1125N](http://www.ixysic.com/Products/SSRFormB.htm) ([datasheet](http://www.ixysic.com/home/pdfs.nsf/www/CPC1125N.pdf/$file/CPC1125N.pdf))
- **250MHz, rail-to-rail I/O, CMOS dual opamp**: [Texas Instruments OPA2354](http://www.ti.com/product/opa2354) ([datasheet](http://www.ti.com/lit/gpn/opa2354))
- **Quad buffer/line driver with 3-state outputs**: [Diodes Incorporated 74LVC126A](http://diodes.com/catalog/standard_logic_189/74lvc126a.html) ([datasheet](http://diodes.com/datasheets/74LVC126A.pdf))
- 0480000 OCP1332 1725
- 4x CGA4V
- S03A

## Photos

<div class="photo-grid" markdown>

[![Lab Nation Smartscope Pcb Top](./img/Lab_nation_smartscope_pcb_top.jpg)](./img/Lab_nation_smartscope_pcb_top.jpg "Lab Nation Smartscope Pcb Top"){ .glightbox data-gallery="labnation-smartscope" }
<span class="caption">Lab Nation Smartscope Pcb Top</span>

[![Lab Nation Smartscope Pcb Analog Frontend](./img/Lab_nation_smartscope_pcb_analog_frontend.jpg)](./img/Lab_nation_smartscope_pcb_analog_frontend.jpg "Lab Nation Smartscope Pcb Analog Frontend"){ .glightbox data-gallery="labnation-smartscope" }
<span class="caption">Lab Nation Smartscope Pcb Analog Frontend</span>

[![Lab Nation Smartscope Mugshot](./img/Lab_nation_smartscope_mugshot.jpg)](./img/Lab_nation_smartscope_mugshot.png "Lab Nation Smartscope Mugshot"){ .glightbox data-gallery="labnation-smartscope" }
<span class="caption">Lab Nation Smartscope Mugshot</span>

[![Lab Nation Smartscope Device Top](./img/Lab_nation_smartscope_device_top.jpg)](./img/Lab_nation_smartscope_device_top.jpg "Lab Nation Smartscope Device Top"){ .glightbox data-gallery="labnation-smartscope" }
<span class="caption">Lab Nation Smartscope Device Top</span>

[![Lab Nation Smartscope Xilinx Spartan6 Xc6slx4](./img/Lab_nation_smartscope_xilinx_spartan6_xc6slx4.jpg)](./img/Lab_nation_smartscope_xilinx_spartan6_xc6slx4.jpg "Lab Nation Smartscope Xilinx Spartan6 Xc6slx4"){ .glightbox data-gallery="labnation-smartscope" }
<span class="caption">Lab Nation Smartscope Xilinx Spartan6 Xc6slx4</span>

[![Lab Nation Smartscope Cpc1125n](./img/Lab_nation_smartscope_cpc1125n.jpg)](./img/Lab_nation_smartscope_cpc1125n.jpg "Lab Nation Smartscope Cpc1125n"){ .glightbox data-gallery="labnation-smartscope" }
<span class="caption">Lab Nation Smartscope Cpc1125n</span>

[![Lab Nation Smartscope Device Probe Connector](./img/Lab_nation_smartscope_device_probe_connector.jpg)](./img/Lab_nation_smartscope_device_probe_connector.jpg "Lab Nation Smartscope Device Probe Connector"){ .glightbox data-gallery="labnation-smartscope" }
<span class="caption">Lab Nation Smartscope Device Probe Connector</span>

[![Lab Nation Smartscope P6060](./img/Lab_nation_smartscope_p6060.jpg)](./img/Lab_nation_smartscope_p6060.jpg "Lab Nation Smartscope P6060"){ .glightbox data-gallery="labnation-smartscope" }
<span class="caption">Lab Nation Smartscope P6060</span>

[![Lab Nation Smartscope Cables Probes](./img/Lab_nation_smartscope_cables_probes.jpg)](./img/Lab_nation_smartscope_cables_probes.jpg "Lab Nation Smartscope Cables Probes"){ .glightbox data-gallery="labnation-smartscope" }
<span class="caption">Lab Nation Smartscope Cables Probes</span>

[![Lab Nation Smartscope Package Bottom](./img/Lab_nation_smartscope_package_bottom.jpg)](./img/Lab_nation_smartscope_package_bottom.jpg "Lab Nation Smartscope Package Bottom"){ .glightbox data-gallery="labnation-smartscope" }
<span class="caption">Lab Nation Smartscope Package Bottom</span>

[![Lab Nation Smartscope 74lvc126a](./img/Lab_nation_smartscope_74lvc126a.jpg)](./img/Lab_nation_smartscope_74lvc126a.jpg "Lab Nation Smartscope 74lvc126a"){ .glightbox data-gallery="labnation-smartscope" }
<span class="caption">Lab Nation Smartscope 74lvc126a</span>

[![Lab Nation Smartscope Pcb Bottom](./img/Lab_nation_smartscope_pcb_bottom.jpg)](./img/Lab_nation_smartscope_pcb_bottom.jpg "Lab Nation Smartscope Pcb Bottom"){ .glightbox data-gallery="labnation-smartscope" }
<span class="caption">Lab Nation Smartscope Pcb Bottom</span>

[![Lab Nation Smartscope Package Contents](./img/Lab_nation_smartscope_package_contents.jpg)](./img/Lab_nation_smartscope_package_contents.jpg "Lab Nation Smartscope Package Contents"){ .glightbox data-gallery="labnation-smartscope" }
<span class="caption">Lab Nation Smartscope Package Contents</span>

[![Lab Nation Smartscope Package Top](./img/Lab_nation_smartscope_package_top.jpg)](./img/Lab_nation_smartscope_package_top.jpg "Lab Nation Smartscope Package Top"){ .glightbox data-gallery="labnation-smartscope" }
<span class="caption">Lab Nation Smartscope Package Top</span>

[![Lab Nation Smartscope Device Bottom](./img/Lab_nation_smartscope_device_bottom.jpg)](./img/Lab_nation_smartscope_device_bottom.jpg "Lab Nation Smartscope Device Bottom"){ .glightbox data-gallery="labnation-smartscope" }
<span class="caption">Lab Nation Smartscope Device Bottom</span>

[![Lab Nation Smartscope Microchip Pic 18lf14k50 I Ss](./img/Lab_nation_smartscope_microchip_pic_18lf14k50-i-ss.jpg)](./img/Lab_nation_smartscope_microchip_pic_18lf14k50-i-ss.jpg "Lab Nation Smartscope Microchip Pic 18lf14k50 I Ss"){ .glightbox data-gallery="labnation-smartscope" }
<span class="caption">Lab Nation Smartscope Microchip Pic 18lf14k50 I Ss</span>

[![Lab Nation Smartscope Oaci 45rc](./img/Lab_nation_smartscope_oaci_45rc.jpg)](./img/Lab_nation_smartscope_oaci_45rc.jpg "Lab Nation Smartscope Oaci 45rc"){ .glightbox data-gallery="labnation-smartscope" }
<span class="caption">Lab Nation Smartscope Oaci 45rc</span>

[![Lab Nation Smartscope Maxim Max19506](./img/Lab_nation_smartscope_maxim_max19506.jpg)](./img/Lab_nation_smartscope_maxim_max19506.jpg "Lab Nation Smartscope Maxim Max19506"){ .glightbox data-gallery="labnation-smartscope" }
<span class="caption">Lab Nation Smartscope Maxim Max19506</span>

[![Lab Nation Smartscope Alliance As4c4m16s 7tcntr](./img/Lab_nation_smartscope_alliance_as4c4m16s-7tcntr.jpg)](./img/Lab_nation_smartscope_alliance_as4c4m16s-7tcntr.jpg "Lab Nation Smartscope Alliance As4c4m16s 7tcntr"){ .glightbox data-gallery="labnation-smartscope" }
<span class="caption">Lab Nation Smartscope Alliance As4c4m16s 7tcntr</span>

[![Lab Nation Smartscope Device Connector](./img/Lab_nation_smartscope_device_connector.jpg)](./img/Lab_nation_smartscope_device_connector.jpg "Lab Nation Smartscope Device Connector"){ .glightbox data-gallery="labnation-smartscope" }
<span class="caption">Lab Nation Smartscope Device Connector</span>

</div>
## Protocol
## Progress

Detection and bitstream loading implemented in libsigrok driver.  Scope init and acquisition WIP in python test code.
See [https://github.com/karlp/libsigrok/tree/devel/labnation](https://github.com/karlp/libsigrok/tree/devel/labnation)

## Resources
- [Vendor software](https://www.lab-nation.com/download)

