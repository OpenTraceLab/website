---
title: Victor 70C
---

# Victor 70C

<div class="infobox" markdown>

![Victor 70C](./img/Victor_70C_LCD.jpg){ .infobox-image }

### Victor 70C

| | |
|---|---|
| **Status** | supported |
| **Source code** | [serial-dmm](https://github.com/OpenTraceLab/OpenTraceCapture/tree/main/src/hardware/serial-dmm) |
| **Counts** | 6000 |
| **IEC 61010-1** | CAT II |
| **Connectivity** | USB (standard cable) |
| **Measurements** | voltage, current, resistance, continuity, diode, capacitance, frequency, temperature |
| **Features** | max/min, data hold, relative, backlight |
| **Website** | [china-victor.com](http://www.china-victor.com/english/en/product_data.aspx?ClassID=168&amp;ID=121) |

</div>

The **Victor 70C** is a 6000 counts, CAT II handheld digital multimeter with USB connectivity.

It is also sold as the [EZA EZ-735](http://github.com/mvneves/victor70c#victor70c-software-for-linux).

See [Victor 70C/Info](https://sigrok.org/wiki/Victor_70C/Info) for more details (such as **lsusb -v** output) about the device.

## Hardware
- [Fortune Semiconductor FS9922-DMM4](http://www.ic-fortune.com/upload/Download/FS9922-DMM4-DS-11_EN.pdf) multimeter chip
- [NXP HEF4066BT](http://datasheet.octopart.com/HEF4066BT-Philips-datasheet-87533.pdf) quadruple bilateral switches
- [Microchip TC7660E](http://datasheet.octopart.com/TC7660EOA-Microchip-datasheet-1009.pdf) charge pump DC-to-DC voltage converter
- [Texas Instruments 27L2C](http://datasheet.octopart.com/TLC27L2CP-Texas-Instruments-datasheet-151061.pdf) precision dual op-amp
- Unknown USB interface chip (HID)

Note: the USB/HID chip is *in the multimeter* (not in the USB cable/connector) for this device. The device is connected to the PC using a standard USB cable (without any internal logic/chip).

## Photos

<div class="photo-grid" markdown>

[![Victor 70c Lcd](./img/Victor_70C_LCD.jpg)](./img/Victor_70C_LCD.jpg "Victor 70c Lcd"){ .glightbox data-gallery="victor-70c" }
<span class="caption">Victor 70c Lcd</span>

[![Victor 70c](./img/Victor_70C.jpg)](./img/Victor_70C.jpg "Victor 70c"){ .glightbox data-gallery="victor-70c" }
<span class="caption">Victor 70c</span>

[![Victor 70c Tc7660e](./img/Victor_70C_TC7660E.jpg)](./img/Victor_70C_TC7660E.jpg "Victor 70c Tc7660e"){ .glightbox data-gallery="victor-70c" }
<span class="caption">Victor 70c Tc7660e</span>

[![Victor 70c 27l2c](./img/Victor_70C_27L2C.jpg)](./img/Victor_70C_27L2C.jpg "Victor 70c 27l2c"){ .glightbox data-gallery="victor-70c" }
<span class="caption">Victor 70c 27l2c</span>

[![Victor 70c Hef4066bt](./img/Victor_70C_HEF4066BT.jpg)](./img/Victor_70C_HEF4066BT.jpg "Victor 70c Hef4066bt"){ .glightbox data-gallery="victor-70c" }
<span class="caption">Victor 70c Hef4066bt</span>

[![Victor 70c](./img/Victor_70C.png)](./img/Victor_70C.png "Victor 70c"){ .glightbox data-gallery="victor-70c" }
<span class="caption">Victor 70c</span>

[![Victor 70c Pcb Top](./img/Victor_70C_PCB_top.jpg)](./img/Victor_70C_PCB_top.jpg "Victor 70c Pcb Top"){ .glightbox data-gallery="victor-70c" }
<span class="caption">Victor 70c Pcb Top</span>

[![Victor 70c Lcd Controller](./img/Victor_70C_LCD_controller.jpg)](./img/Victor_70C_LCD_controller.jpg "Victor 70c Lcd Controller"){ .glightbox data-gallery="victor-70c" }
<span class="caption">Victor 70c Lcd Controller</span>

[![Victor 70c Pcb Bottom](./img/Victor_70C_PCB_bottom.jpg)](./img/Victor_70C_PCB_bottom.jpg "Victor 70c Pcb Bottom"){ .glightbox data-gallery="victor-70c" }
<span class="caption">Victor 70c Pcb Bottom</span>

</div>
## Protocol

See [Victor protocol](https://sigrok.org/wiki/Victor_protocol).

## Resources
- [RoastLogger: Input Devices](https://web.archive.org/web/20160527152655/http://homepage.ntlworld.com/green_bean/coffee/roastlogger/dmmdetails.html) (Victor Victor 86B/86C support)
- [Dave Ansell Science Communication: Victor 86C multimeter USB encoding for linux](http://www.daveansell.co.uk/?q=node/44) (PHP)
- [victor86b-usb-interface: USB interface for Victor 86B Digital Multimeter using HIDAPI](https://web.archive.org/web/20170104171210/https://code.google.com/archive/p/victor86b-usb-interface/) (see also [here](http://www.codeproject.com/Articles/310547/USB-Digital-Multimeter-Driver-using-HIDAPI))
- [Github: victor70c](https://github.com/mvneves/victor70c) (HIDAPI)
- [Random review / photos](http://translate.google.com/translate?hl=de&sl=zh-CN&tl=en&u=http%3A%2F%2Fmytes.blog.163.com%2Fblog%2Fstatic%2F24568310201163010029970%2F)

