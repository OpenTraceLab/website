---
title: Voltcraft VC-890
---

# Voltcraft VC-890

<div class="infobox" markdown>

![Voltcraft VC-890](./img/Voltcraft_vc890_temperature_probe_2.jpg){ .infobox-image }

### Voltcraft VC-890

| | |
|---|---|
| **Status** | planned |
| **Source code** | [serial-dmm](https://github.com/OpenTraceLab/OpenTraceCapture/tree/main/src/hardware/serial-dmm) |
| **Counts** | 60000 |
| **IEC 61010-1** | CAT III (1000V) / CAT IV (600V) |
| **Connectivity** | USB/serial |
| **Website** | [conrad.com](http://www.conrad.com/ce/en/product/124600/Handheld-multimeter-digital-VOLTCRAFT-VC890-OLED-Calibrated-to-Manufacturers-standards-no-certificate-OLED-display) |

</div>

The **Voltcraft VC-890** is a 60000 counts, CAT III (1000V) / CAT IV (600V) handheld digital multimeter with USB connectivity.

See [Voltcraft VC-890/Info](https://sigrok.org/wiki/Voltcraft_VC-890/Info) for more details (such as **lsusb -v** output) about the device.

## Hardware

**Multimeter**:

- ES51997P chipset
- EFM32 MCU (used as display controller)
- OLED, pixel graphics, large primary display and bar graph, lots of indicators, secondary display

**USB cable:**

- CP2110 USB to UART bridge (USB HID, supported by conn=hid/cp2110 specs)

## Photos

<div class="photo-grid" markdown>

[![Voltcraft Vc890 Temperature Probe 2](./img/Voltcraft_vc890_temperature_probe_2.jpg)](./img/Voltcraft_vc890_temperature_probe_2.jpg "Voltcraft Vc890 Temperature Probe 2"){ .glightbox data-gallery="voltcraft-vc-890" }
<span class="caption">Voltcraft Vc890 Temperature Probe 2</span>

[![Voltcraft Vc890 Device Front](./img/Voltcraft_vc890_device_front.jpg)](./img/Voltcraft_vc890_device_front.jpg "Voltcraft Vc890 Device Front"){ .glightbox data-gallery="voltcraft-vc-890" }
<span class="caption">Voltcraft Vc890 Device Front</span>

[![Voltcraft Vc890 Package Box](./img/Voltcraft_vc890_package_box.jpg)](./img/Voltcraft_vc890_package_box.jpg "Voltcraft Vc890 Package Box"){ .glightbox data-gallery="voltcraft-vc-890" }
<span class="caption">Voltcraft Vc890 Package Box</span>

[![Voltcraft Vc890 Device Lcd](./img/Voltcraft_vc890_device_lcd.jpg)](./img/Voltcraft_vc890_device_lcd.jpg "Voltcraft Vc890 Device Lcd"){ .glightbox data-gallery="voltcraft-vc-890" }
<span class="caption">Voltcraft Vc890 Device Lcd</span>

[![Voltcraft Vc890 Device Battery](./img/Voltcraft_vc890_device_battery.jpg)](./img/Voltcraft_vc890_device_battery.jpg "Voltcraft Vc890 Device Battery"){ .glightbox data-gallery="voltcraft-vc-890" }
<span class="caption">Voltcraft Vc890 Device Battery</span>

[![Voltcraft Vc890 Mugshot](./img/Voltcraft_vc890_mugshot.png)](./img/Voltcraft_vc890_mugshot.png "Voltcraft Vc890 Mugshot"){ .glightbox data-gallery="voltcraft-vc-890" }
<span class="caption">Voltcraft Vc890 Mugshot</span>

[![Voltcraft Vc890 Device Back](./img/Voltcraft_vc890_device_back.jpg)](./img/Voltcraft_vc890_device_back.jpg "Voltcraft Vc890 Device Back"){ .glightbox data-gallery="voltcraft-vc-890" }
<span class="caption">Voltcraft Vc890 Device Back</span>

[![Voltcraft Vc890 Package Content](./img/Voltcraft_vc890_package_content.jpg)](./img/Voltcraft_vc890_package_content.jpg "Voltcraft Vc890 Package Content"){ .glightbox data-gallery="voltcraft-vc-890" }
<span class="caption">Voltcraft Vc890 Package Content</span>

[![Voltcraft Vc890 Usb Cable 1](./img/Voltcraft_vc890_usb_cable_1.jpg)](./img/Voltcraft_vc890_usb_cable_1.jpg "Voltcraft Vc890 Usb Cable 1"){ .glightbox data-gallery="voltcraft-vc-890" }
<span class="caption">Voltcraft Vc890 Usb Cable 1</span>

[![Voltcraft Vc890 Temperature Probe 1](./img/Voltcraft_vc890_temperature_probe_1.jpg)](./img/Voltcraft_vc890_temperature_probe_1.jpg "Voltcraft Vc890 Temperature Probe 1"){ .glightbox data-gallery="voltcraft-vc-890" }
<span class="caption">Voltcraft Vc890 Temperature Probe 1</span>

[![Voltcraft Vc890 Usb Cable 2](./img/Voltcraft_vc890_usb_cable_2.jpg)](./img/Voltcraft_vc890_usb_cable_2.jpg "Voltcraft Vc890 Usb Cable 2"){ .glightbox data-gallery="voltcraft-vc-890" }
<span class="caption">Voltcraft Vc890 Usb Cable 2</span>

</div>
## Protocol
## Resources
- [Manual](http://www.produktinfo.conrad.com/datenblaetter/100000-124999/124600-an-01-ml-VOLTCRAFT_VC890_OLED_DMM_de_en_fr_nl.pdf)
- [Protocol documentation (the meter)](http://www.produktinfo.conrad.com/datenblaetter/100000-124999/124600-in-01-en-Schnittstellen_VOLTCRAFT_VC_890_OLED_DMM.pdf)
- [ES51997P spec (DMM analog front end)](http://www.cyrustek.com.tw/spec/ES51997.pdf)
- [Vendor software](http://www.produktinfo.conrad.com/datenblaetter/100000-124999/124600-up-01-ml-VOLTSOFT_SETUP_V_2_00_de_en_fr.zip)
- [review and teardown video](http://www.youtube.com/watch?v=DT2MU32la2c)

