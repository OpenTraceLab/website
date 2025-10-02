---
title: RadioShack 22-168
---

# RadioShack 22-168

<div class="infobox" markdown>

![RadioShack 22-168](./img/Rs_22_168_sandwiched_pcb.jpg){ .infobox-image }

### RadioShack 22-168

| | |
|---|---|
| **Status** | supported |
| **Source code** | [serial-dmm](https://github.com/OpenTraceLab/OpenTraceCapture/tree/main/src/hardware/serial-dmm) |
| **Counts** | 2000 |
| **IEC 61010-1** | Unspecified |
| **Connectivity** | RS232 |
| **Measurements** | voltage, current, resistance, capacitance, continuity, diode, logic, frequency, hFE |
| **Features** | data hold, min/max, 10 reading memory |
| **Website** | [radioshack.com](http://support.radioshack.com/productinfo/DocumentResults.asp?sku_id=22-168&amp;Name=Meters%20and%20Scopes&amp;Reuse=N) |

</div>

The **RadioShack 22-168** is a 2000 counts handheld digital multimeter with RS-232 connectivity.

## Hardware
- **3 1/2 digit ADC with bandgap reference**: [Maxim MAX130CPL](http://www.maxim-ic.com/datasheet/index.mvp/id/1288) ([datasheet](http://datasheets.maxim-ic.com/en/ds/MAX130-MAX131.pdf)) (marking: "Maxim MAX130CPL 0138-3 C10039")
- **CPU**: Metex KS57C2016 (Samsung KS57C2016 4-bit microcontroller with custom Metex firmware) (marking: "Metex 93D3 KS57C2016-02 410")
- **?**: Metex 9005 (marking has ST logo: "Metex 9005 MET7ACS 92A32792BA")
- **Crystal**: 4.1856MHz crystal
- **555 timer**:  [Intersil ICM7555CBA](http://www.intersil.com/content/intersil/en/products/timing-and-digital/counters-time-base-ics/counter-time-base-ics/ICM7555.html) ([datasheet](http://www.intersil.com/content/dam/Intersil/documents/fn28/fn2867.pdf)) (marking: "H 7555 CBA L405")
- **Quad analog switch/quad multiplexer**: [Motorola 14066B](http://www.onsemi.com/PowerSolutions/product.do?id=MC14066B) ([datasheet](http://www.onsemi.com/pub/Collateral/MC14066B-D.PDF)) (marking: "14066B XAC334")
- **Quad 2-input NAND gate**: GD4011BD
- **Optoisolator**: Lite-ON LTV-817
- **Unidentified ICs**:  Two ICs, which appear to be SSOP8 packages are hidden behind black goo. The purpose of the goo is unknown.

## Photos

<div class="photo-grid" markdown>

[![Rs 22 168 Sandwiched Pcb](./img/Rs_22_168_sandwiched_pcb.jpg)](./img/Rs_22_168_sandwiched_pcb.jpg "Rs 22 168 Sandwiched Pcb"){ .glightbox data-gallery="radioshack-22-168" }
<span class="caption">Rs 22 168 Sandwiched Pcb</span>

[![Rs 22 168 Ics4](./img/Rs_22_168_ics4.jpg)](./img/Rs_22_168_ics4.jpg "Rs 22 168 Ics4"){ .glightbox data-gallery="radioshack-22-168" }
<span class="caption">Rs 22 168 Ics4</span>

[![Rs 22 168 Ics1](./img/Rs_22_168_ics1.jpg)](./img/Rs_22_168_ics1.jpg "Rs 22 168 Ics1"){ .glightbox data-gallery="radioshack-22-168" }
<span class="caption">Rs 22 168 Ics1</span>

[![Rs 22 168 Optoisolation](./img/Rs_22_168_optoisolation.jpg)](./img/Rs_22_168_optoisolation.jpg "Rs 22 168 Optoisolation"){ .glightbox data-gallery="radioshack-22-168" }
<span class="caption">Rs 22 168 Optoisolation</span>

[![Rs 22 168 Bare Dmm](./img/Rs_22_168_bare_dmm.jpg)](./img/Rs_22_168_bare_dmm.jpg "Rs 22 168 Bare Dmm"){ .glightbox data-gallery="radioshack-22-168" }
<span class="caption">Rs 22 168 Bare Dmm</span>

[![Rs 22 168 Pcb Second Top](./img/Rs_22_168_pcb_second_top.jpg)](./img/Rs_22_168_pcb_second_top.jpg "Rs 22 168 Pcb Second Top"){ .glightbox data-gallery="radioshack-22-168" }
<span class="caption">Rs 22 168 Pcb Second Top</span>

[![Rs 22 168 Rs232 Interface Port](./img/Rs_22_168_rs232_interface_port.jpg)](./img/Rs_22_168_rs232_interface_port.jpg "Rs 22 168 Rs232 Interface Port"){ .glightbox data-gallery="radioshack-22-168" }
<span class="caption">Rs 22 168 Rs232 Interface Port</span>

[![Rs 22 168 Cover Front](./img/Rs_22_168_cover_front.jpg)](./img/Rs_22_168_cover_front.jpg "Rs 22 168 Cover Front"){ .glightbox data-gallery="radioshack-22-168" }
<span class="caption">Rs 22 168 Cover Front</span>

[![Rs 22 168 Batt Cover](./img/Rs_22_168_batt_cover.jpg)](./img/Rs_22_168_batt_cover.jpg "Rs 22 168 Batt Cover"){ .glightbox data-gallery="radioshack-22-168" }
<span class="caption">Rs 22 168 Batt Cover</span>

[![Rs 22 168 Cover Back](./img/Rs_22_168_cover_back.jpg)](./img/Rs_22_168_cover_back.jpg "Rs 22 168 Cover Back"){ .glightbox data-gallery="radioshack-22-168" }
<span class="caption">Rs 22 168 Cover Back</span>

[![Rs 22 168 Metex Stand](./img/Rs_22_168_metex_stand.jpg)](./img/Rs_22_168_metex_stand.jpg "Rs 22 168 Metex Stand"){ .glightbox data-gallery="radioshack-22-168" }
<span class="caption">Rs 22 168 Metex Stand</span>

[![Rs 22 168 Lcd](./img/Rs_22_168_lcd.jpg)](./img/Rs_22_168_lcd.jpg "Rs 22 168 Lcd"){ .glightbox data-gallery="radioshack-22-168" }
<span class="caption">Rs 22 168 Lcd</span>

[![Rs 22 168 Spare Fuse](./img/Rs_22_168_spare_fuse.jpg)](./img/Rs_22_168_spare_fuse.jpg "Rs 22 168 Spare Fuse"){ .glightbox data-gallery="radioshack-22-168" }
<span class="caption">Rs 22 168 Spare Fuse</span>

[![Rs 22 168 Pcb Second Bottom](./img/Rs_22_168_pcb_second_bottom.jpg)](./img/Rs_22_168_pcb_second_bottom.jpg "Rs 22 168 Pcb Second Bottom"){ .glightbox data-gallery="radioshack-22-168" }
<span class="caption">Rs 22 168 Pcb Second Bottom</span>

[![Rs 22 168 Pcb Main Front](./img/Rs_22_168_pcb_main_front.jpg)](./img/Rs_22_168_pcb_main_front.jpg "Rs 22 168 Pcb Main Front"){ .glightbox data-gallery="radioshack-22-168" }
<span class="caption">Rs 22 168 Pcb Main Front</span>

[![Rs 22 168 Ics2](./img/Rs_22_168_ics2.jpg)](./img/Rs_22_168_ics2.jpg "Rs 22 168 Ics2"){ .glightbox data-gallery="radioshack-22-168" }
<span class="caption">Rs 22 168 Ics2</span>

[![Rs 22 168 Cable Mated](./img/Rs_22_168_cable_mated.jpg)](./img/Rs_22_168_cable_mated.jpg "Rs 22 168 Cable Mated"){ .glightbox data-gallery="radioshack-22-168" }
<span class="caption">Rs 22 168 Cable Mated</span>

[![Rs 22 168 Angle](./img/Rs_22_168_angle.jpg)](./img/Rs_22_168_angle.png "Rs 22 168 Angle"){ .glightbox data-gallery="radioshack-22-168" }
<span class="caption">Rs 22 168 Angle</span>

[![Rs 22 168 Hidden Components](./img/Rs_22_168_hidden_components.jpg)](./img/Rs_22_168_hidden_components.jpg "Rs 22 168 Hidden Components"){ .glightbox data-gallery="radioshack-22-168" }
<span class="caption">Rs 22 168 Hidden Components</span>

[![Rs 22 168 Pcb Main Front Light](./img/Rs_22_168_pcb_main_front_light.jpg)](./img/Rs_22_168_pcb_main_front_light.jpg "Rs 22 168 Pcb Main Front Light"){ .glightbox data-gallery="radioshack-22-168" }
<span class="caption">Rs 22 168 Pcb Main Front Light</span>

[![Rs 22 168 Inside Mooning](./img/Rs_22_168_inside_mooning.jpg)](./img/Rs_22_168_inside_mooning.jpg "Rs 22 168 Inside Mooning"){ .glightbox data-gallery="radioshack-22-168" }
<span class="caption">Rs 22 168 Inside Mooning</span>

[![Rs 22 168 Ics5](./img/Rs_22_168_ics5.jpg)](./img/Rs_22_168_ics5.jpg "Rs 22 168 Ics5"){ .glightbox data-gallery="radioshack-22-168" }
<span class="caption">Rs 22 168 Ics5</span>

[![Rs 22 168 Pcb 2 Bottom Light](./img/Rs_22_168_pcb_2_bottom_light.jpg)](./img/Rs_22_168_pcb_2_bottom_light.jpg "Rs 22 168 Pcb 2 Bottom Light"){ .glightbox data-gallery="radioshack-22-168" }
<span class="caption">Rs 22 168 Pcb 2 Bottom Light</span>

[![Rs 22 168 Pcb Main Back Light](./img/Rs_22_168_pcb_main_back_light.jpg)](./img/Rs_22_168_pcb_main_back_light.jpg "Rs 22 168 Pcb Main Back Light"){ .glightbox data-gallery="radioshack-22-168" }
<span class="caption">Rs 22 168 Pcb Main Back Light</span>

[![Rs 22 168 Mosc](./img/Rs_22_168_mosc.jpg)](./img/Rs_22_168_mosc.jpg "Rs 22 168 Mosc"){ .glightbox data-gallery="radioshack-22-168" }
<span class="caption">Rs 22 168 Mosc</span>

[![Rs 22 168 Mugshot](./img/Rs_22_168_mugshot.jpg)](./img/Rs_22_168_mugshot.png "Rs 22 168 Mugshot"){ .glightbox data-gallery="radioshack-22-168" }
<span class="caption">Rs 22 168 Mugshot</span>

[![Rs 22 168 Rangeswitch](./img/Rs_22_168_rangeswitch.jpg)](./img/Rs_22_168_rangeswitch.jpg "Rs 22 168 Rangeswitch"){ .glightbox data-gallery="radioshack-22-168" }
<span class="caption">Rs 22 168 Rangeswitch</span>

[![Rs 22 168 Batt Comp](./img/Rs_22_168_batt_comp.jpg)](./img/Rs_22_168_batt_comp.jpg "Rs 22 168 Batt Comp"){ .glightbox data-gallery="radioshack-22-168" }
<span class="caption">Rs 22 168 Batt Comp</span>

[![Rs 22 168 Opened Mooning](./img/Rs_22_168_opened_mooning.jpg)](./img/Rs_22_168_opened_mooning.jpg "Rs 22 168 Opened Mooning"){ .glightbox data-gallery="radioshack-22-168" }
<span class="caption">Rs 22 168 Opened Mooning</span>

[![Rs 22 168 Pcb Top Light](./img/Rs_22_168_pcb_top_light.jpg)](./img/Rs_22_168_pcb_top_light.jpg "Rs 22 168 Pcb Top Light"){ .glightbox data-gallery="radioshack-22-168" }
<span class="caption">Rs 22 168 Pcb Top Light</span>

[![Rs 22 168 Ics3](./img/Rs_22_168_ics3.jpg)](./img/Rs_22_168_ics3.jpg "Rs 22 168 Ics3"){ .glightbox data-gallery="radioshack-22-168" }
<span class="caption">Rs 22 168 Ics3</span>

[![Rs 22 168 Lcd Back](./img/Rs_22_168_lcd_back.jpg)](./img/Rs_22_168_lcd_back.jpg "Rs 22 168 Lcd Back"){ .glightbox data-gallery="radioshack-22-168" }
<span class="caption">Rs 22 168 Lcd Back</span>

[![Rs 22 168 Back](./img/Rs_22_168_back.jpg)](./img/Rs_22_168_back.jpg "Rs 22 168 Back"){ .glightbox data-gallery="radioshack-22-168" }
<span class="caption">Rs 22 168 Back</span>

</div>
## Protocol

See [Multimeter_ICs#Metex_14-byte_ASCII](https://sigrok.org/wiki/Multimeter_ICs#Metex_14-byte_ASCII).

## Resources
- [Vendor software](https://www.radioshack.com/search/softwareResults.jsp?kw=22-168)
- [Software download](http://www.radioshack.com/graphics/uc/rsk/Support/SoftwareDownload/2200168.exe)
- [linuxtoys.org: Radio Shack DMM with RS-232](http://www.linuxtoys.org/dvm/dvm.html)

