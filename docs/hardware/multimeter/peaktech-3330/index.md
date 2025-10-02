---
title: PeakTech 3330
---

# PeakTech 3330

<div class="infobox" markdown>

![PeakTech 3330](./img/P3330_front_holster.jpg){ .infobox-image }

### PeakTech 3330

| | |
|---|---|
| **Status** | supported |
| **Source code** | [serial-dmm](https://github.com/OpenTraceLab/OpenTraceCapture/tree/main/src/hardware/serial-dmm) |
| **Counts** | 4000 |
| **IEC 61010-1** | CAT III (1000V) |
| **Connectivity** | USB and RS232 cables |
| **Measurements** | voltage, current, resistance, capacitance, frequency, duty cycle, diode, continuity, temperature |
| **Features** | autorange, data hold, relative, backlight, display prompts |
| **Website** | [peaktech.de](http://www.peaktech.de/productdetail/kategorie/auslaufmodelle-nur-solange-der-vorrat-reicht/produkt/p-3330.html) |

</div>

The **PeakTech 3330** is a 4000 counts, CAT III (1000V) handheld digital multimeter with RS232 or USB connectivity.

In addition to the usual features, the display presents the internal temperature, and has extra indicators and prompts (disconnect power from the circuit under test for passive measurement functions, which jacks to connect the probes to depending on the selected function, when a fuse is blown).

See [PeakTech 3330/Info](https://sigrok.org/wiki/PeakTech_3330/Info) for more details (such as **lsusb -v** output) about the device.

## Hardware

**Multimeter**:

- **Multimeter IC**: [Fortune Semiconductor FS9721_LP3](https://sigrok.org/wiki/Multimeter_ICs#Fortune_Semiconductor_FS9721_LP3)
- **Crystal**: 4MHz (markings: "4.000")
- **Fuse**: 20A/500V (markings: HUKE R015 / RT14 RT18 / RT19)
- **Fuse**: 500mA/250V (glass)

The U1 chip is labelled FS9711_LP3, but works flawlessly with all existing routines for FS9721. Only a TX LED is fitted in the DMM.

The fuses do NOT match the CAT III 1000V rating which is claimed on the front cover and in the paper!

There are two PCBs, with the input circuitry and range switch stacked on top of the PCB which holds the DMM chip. The top PCB is labelled "DT-9932B-3" in copper.  The bottom PCB has "DT-9932B-7" as well as "2004.12.11.v.7" silk screen labels. The PCBs are connected by means of several soldered ribbon cables.

There is a COB ("U2") on pads with a QFP44 footprint. The chip is close to a big brown THT capacitor (sample'n'hold?), though the meter does not claim TRMS capabilities. Only few pins are connected, it's unlikely to be a display controller.

**RS232/USB cables**:

- The DMM comes with both RS232 as well as USB cables.
- The USB cable contains a CP2102 chip.
- Both cables only have an RX LED.

## Photos

<div class="photo-grid" markdown>

[![P3330 Front Holster](./img/P3330_front_holster.jpg)](./img/P3330_front_holster.png "P3330 Front Holster"){ .glightbox data-gallery="peaktech-3330" }
<span class="caption">P3330 Front Holster</span>

[![P3330 Pcb Input](./img/P3330_pcb_input.jpg)](./img/P3330_pcb_input.png "P3330 Pcb Input"){ .glightbox data-gallery="peaktech-3330" }
<span class="caption">P3330 Pcb Input</span>

[![P3330 Lcd Backlight](./img/P3330_lcd_backlight.jpg)](./img/P3330_lcd_backlight.png "P3330 Lcd Backlight"){ .glightbox data-gallery="peaktech-3330" }
<span class="caption">P3330 Lcd Backlight</span>

[![P3330 Pcb Dmmchip Closeup](./img/P3330_pcb_dmmchip_closeup.jpg)](./img/P3330_pcb_dmmchip_closeup.png "P3330 Pcb Dmmchip Closeup"){ .glightbox data-gallery="peaktech-3330" }
<span class="caption">P3330 Pcb Dmmchip Closeup</span>

[![P3330 Serial Cables](./img/P3330_serial_cables.jpg)](./img/P3330_serial_cables.png "P3330 Serial Cables"){ .glightbox data-gallery="peaktech-3330" }
<span class="caption">P3330 Serial Cables</span>

[![P3330 Device Back](./img/P3330_device_back.jpg)](./img/P3330_device_back.png "P3330 Device Back"){ .glightbox data-gallery="peaktech-3330" }
<span class="caption">P3330 Device Back</span>

[![P3330 Range Labels](./img/P3330_range_labels.jpg)](./img/P3330_range_labels.png "P3330 Range Labels"){ .glightbox data-gallery="peaktech-3330" }
<span class="caption">P3330 Range Labels</span>

[![P3330 Device Front](./img/P3330_device_front.jpg)](./img/P3330_device_front.png "P3330 Device Front"){ .glightbox data-gallery="peaktech-3330" }
<span class="caption">P3330 Device Front</span>

[![P3330 Lcd Indicator](./img/P3330_lcd_indicator.jpg)](./img/P3330_lcd_indicator.png "P3330 Lcd Indicator"){ .glightbox data-gallery="peaktech-3330" }
<span class="caption">P3330 Lcd Indicator</span>

[![P3330 Pcb Dmmchip](./img/P3330_pcb_dmmchip.jpg)](./img/P3330_pcb_dmmchip.png "P3330 Pcb Dmmchip"){ .glightbox data-gallery="peaktech-3330" }
<span class="caption">P3330 Pcb Dmmchip</span>

[![Peaktech 3330 Mugshot](./img/Peaktech_3330_mugshot.jpg)](./img/Peaktech_3330_mugshot.png "Peaktech 3330 Mugshot"){ .glightbox data-gallery="peaktech-3330" }
<span class="caption">Peaktech 3330 Mugshot</span>

[![P3330 Pcb Twoboard](./img/P3330_pcb_twoboard.jpg)](./img/P3330_pcb_twoboard.png "P3330 Pcb Twoboard"){ .glightbox data-gallery="peaktech-3330" }
<span class="caption">P3330 Pcb Twoboard</span>

</div>
## Protocol

See [Multimeter_ICs#Fortune_Semiconductor_FS9721_LP3](https://sigrok.org/wiki/Multimeter_ICs#Fortune_Semiconductor_FS9721_LP3) for the DMM IC protocol.

Serial communication is controlled by the yellow "RS232" button.

## Resources
- [Product page](http://www.peaktech.de/productdetail/kategorie/auslaufmodelle-nur-solange-der-vorrat-reicht/produkt/p-3330.html) (it's in the vendor's "discontinued" section, has been removed from the website in the meantime)

