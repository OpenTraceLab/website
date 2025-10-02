---
title: Victor 86C
---

# Victor 86C

<div class="infobox" markdown>

![Victor 86C](./img/Victor_86c_device_front.jpg){ .infobox-image }

### Victor 86C

| | |
|---|---|
| **Status** | supported |
| **Source code** | [serial-dmm](https://github.com/OpenTraceLab/OpenTraceCapture/tree/main/src/hardware/serial-dmm) |
| **Counts** | 4000 |
| **IEC 61010-1** | CAT III (1000V)1 |
| **Connectivity** | [USB](https://sigrok.org/wiki/Device_cables#Victor_86C_USB_cable) |
| **Measurements** | voltage, resistance, continuity, diode, capacitance, frequency, temperature, current, duty cycle |
| **Features** | autorange, data hold, min/max, relative |
| **Website** | [china-victor.com](http://www.china-victor.com/english/en/product_data.aspx?ClassID=168&amp;ID=126) |

</div>

The **Victor 86C** is a 4000 counts, CAT III (1000V)1 handheld digital multimeter with USB connectivity.

See [Victor 86C/Info](https://sigrok.org/wiki/Victor_86C/Info) for more details (such as **lsusb -vvv** output) about the device.

1 CAT III according to the markings on the probes, which doesn't have to mean anything. No explicit "CAT" mention in the manual, it seems (1000V max. is listed, though).

## Hardware

**Multimeter**:

- TODO.

**USB cable**:

- See [Device cables#Victor_86C_USB_cable](https://sigrok.org/wiki/Device_cables#Victor_86C_USB_cable).

## Photos

<div class="photo-grid" markdown>

[![Victor 86c Device Front](./img/Victor_86c_device_front.jpg)](./img/Victor_86c_device_front.png "Victor 86c Device Front"){ .glightbox data-gallery="victor-86c" }
<span class="caption">Victor 86c Device Front</span>

</div>
## Protocol

See [Victor protocol](https://sigrok.org/wiki/Victor_protocol).

## Resources
- [RoastLogger: Input Devices](http://homepage.ntlworld.com/green_bean/coffee/roastlogger/dmmdetails.html) (Victor Victor 86B/86C support)
- [Dave Ansell Science Communication: Victor 86C multimeter USB encoding for linux](http://www.daveansell.co.uk/?q=node/44) (PHP)
- [victor86b-usb-interface: USB interface for Victor 86B Digital Multimeter using HIDAPI](https://code.google.com/p/victor86b-usb-interface/) (see also [here](http://www.codeproject.com/Articles/310547/USB-Digital-Multimeter-Driver-using-HIDAPI))
- [Sparkfun: Victor 70C](https://www.sparkfun.com/products/10892) ([manual](http://dlnmh9ip6v2uc.cloudfront.net/datasheets/Tools/601e-070c-000a.pdf), [software](http://dlnmh9ip6v2uc.cloudfront.net/datasheets/Tools/setup_70c_multi.rar))
- [Github: victor70c](https://github.com/mvneves/victor70c) (HIDAPI)
- [Random review / photos](http://translate.google.com/translate?hl=de&sl=zh-CN&tl=en&u=http%3A%2F%2Fmytes.blog.163.com%2Fblog%2Fstatic%2F24568310201163010029970%2F)

