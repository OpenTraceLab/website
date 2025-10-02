---
title: Brymen BM857
---

# Brymen BM857

<div class="infobox" markdown>

![Brymen BM857](./img/Bm859s-front.jpg){ .infobox-image }

### Brymen BM857

| | |
|---|---|
| **Status** | supported |
| **Source code** | [serial-dmm](https://github.com/OpenTraceLab/OpenTraceCapture/tree/main/src/hardware/serial-dmm) |
| **Counts** | 50000, 500000(DCV), 999999(Hz) |
| **IEC 61010-1** | CAT III (1000V) / CAT IV (600V) |
| **Connectivity** | RS232 |
| **Measurements** | voltage, frequency, diode, resistance, continuity, capacitance, current |
| **Features** | autorange, data hold, crest, backlight, true-rms, dBm (selectable impedance), %4-20mA |
| **Website** | brymen.com [BM857s](http://brymen.com/product-html/PD02BM850s_857s.html) [BM859s](http://brymen.com/product-html/PD02BM850s_859s.html) |

</div>

The **Brymen BM857** is a 50000 counts (500000 DC V), CAT III (1000V) / CAT IV (600V) handheld digital multimeter with RS232 connectivity. The **BM859s** is also supported, it uses the same protocol. Adapter kits ship with IR to RS232 cables, and include RS232 to USB converters.

Higher end models support dual temperature sensors and difference mode, and the reference impedance for dBm measurements can be chosen in a range between 4 and 1200 Ohms.

## Hardware

**Multimeter:**

- **Multimeter IC**: TBD
- **Precision +2.5V Voltage reference**: [Analog Devices REF43](http://www.analog.com/en/special-linear-functions/voltage-references/ref43/products/product.html)
- **True RMS-to-DC converter**: [Analog Devices AD737](http://www.analog.com/en/special-linear-functions/rms-to-dc-converters/ad737/products/product.html)
- **EEPROM(?)**: Chip marked S24C0.
- **Unidentified**: Several 062-JRC chips. These appear to be JFET opamps.
- **Unidentified**: Two QFP64 chips.
- TODO

**Cable:**

- TODO
- See the [ BRUA-85Xa kit](https://sigrok.org/wiki/Device_cables#Brymen_BRUA-85Xa_kit) and the [ BC-85Xa adapter](https://sigrok.org/wiki/Device_cables#Brymen_BC-85Xa)
- See [User_talk:Mrnuke#BM857_PC_Interface_cable](https://sigrok.org/wiki/User_talk:Mrnuke#BM857_PC_Interface_cable)

## Photos

<div class="photo-grid" markdown>

[![Bm859s Front](./img/Bm859s-front.jpg)](./img/Bm859s-front.png "Bm859s Front"){ .glightbox data-gallery="brymen-bm857" }
<span class="caption">Bm859s Front</span>

[![Bm857 Mcu 2blcdc](./img/Bm857_mcu_2Blcdc.jpg)](./img/Bm857_mcu_2Blcdc.jpg "Bm857 Mcu 2blcdc"){ .glightbox data-gallery="brymen-bm857" }
<span class="caption">Bm857 Mcu 2blcdc</span>

[![Bm857 Cable Clips](./img/Bm857_cable_clips.jpg)](./img/Bm857_cable_clips.jpg "Bm857 Cable Clips"){ .glightbox data-gallery="brymen-bm857" }
<span class="caption">Bm857 Cable Clips</span>

[![Brymen Br85x Dmm Hookup Side](./img/Brymen_br85x_dmm_hookup_side.jpg)](./img/Brymen_br85x_dmm_hookup_side.jpg "Brymen Br85x Dmm Hookup Side"){ .glightbox data-gallery="brymen-bm857" }
<span class="caption">Brymen Br85x Dmm Hookup Side</span>

[![Bm857 Cover Front](./img/Bm857_cover_front.jpg)](./img/Bm857_cover_front.jpg "Bm857 Cover Front"){ .glightbox data-gallery="brymen-bm857" }
<span class="caption">Bm857 Cover Front</span>

[![Brymen Br85x Dmm Hookup Angle](./img/Brymen_br85x_dmm_hookup_angle.jpg)](./img/Brymen_br85x_dmm_hookup_angle.jpg "Brymen Br85x Dmm Hookup Angle"){ .glightbox data-gallery="brymen-bm857" }
<span class="caption">Brymen Br85x Dmm Hookup Angle</span>

[![Bm857 Upperpcb Top](./img/Bm857_upperpcb_top.jpg)](./img/Bm857_upperpcb_top.jpg "Bm857 Upperpcb Top"){ .glightbox data-gallery="brymen-bm857" }
<span class="caption">Bm857 Upperpcb Top</span>

[![Bm857 Upperpcb Bottom](./img/Bm857_upperpcb_bottom.jpg)](./img/Bm857_upperpcb_bottom.jpg "Bm857 Upperpcb Bottom"){ .glightbox data-gallery="brymen-bm857" }
<span class="caption">Bm857 Upperpcb Bottom</span>

[![Bm857 Front Noholster](./img/Bm857_front_noholster.jpg)](./img/Bm857_front_noholster.png "Bm857 Front Noholster"){ .glightbox data-gallery="brymen-bm857" }
<span class="caption">Bm857 Front Noholster</span>

[![Bm857 Lowerpcb Top](./img/Bm857_lowerpcb_top.jpg)](./img/Bm857_lowerpcb_top.jpg "Bm857 Lowerpcb Top"){ .glightbox data-gallery="brymen-bm857" }
<span class="caption">Bm857 Lowerpcb Top</span>

[![Bm857 Lcdc](./img/Bm857_lcdc.jpg)](./img/Bm857_lcdc.jpg "Bm857 Lcdc"){ .glightbox data-gallery="brymen-bm857" }
<span class="caption">Bm857 Lcdc</span>

[![Bm857 Ics 2](./img/Bm857_ICs_2.jpg)](./img/Bm857_ICs_2.jpg "Bm857 Ics 2"){ .glightbox data-gallery="brymen-bm857" }
<span class="caption">Bm857 Ics 2</span>

[![Bm857 Box Left](./img/Bm857_box_left.jpg)](./img/Bm857_box_left.png "Bm857 Box Left"){ .glightbox data-gallery="brymen-bm857" }
<span class="caption">Bm857 Box Left</span>

[![Bm857 Cover Back](./img/Bm857_cover_back.jpg)](./img/Bm857_cover_back.jpg "Bm857 Cover Back"){ .glightbox data-gallery="brymen-bm857" }
<span class="caption">Bm857 Cover Back</span>

[![Bm857 Back](./img/Bm857_back.jpg)](./img/Bm857_back.jpg "Bm857 Back"){ .glightbox data-gallery="brymen-bm857" }
<span class="caption">Bm857 Back</span>

[![Bm857 Inside Backside](./img/Bm857_inside_backside.jpg)](./img/Bm857_inside_backside.jpg "Bm857 Inside Backside"){ .glightbox data-gallery="brymen-bm857" }
<span class="caption">Bm857 Inside Backside</span>

[![Bm 857 Mugshot 500000](./img/Bm_857_mugshot_500000.jpg)](./img/Bm_857_mugshot_500000.png "Bm 857 Mugshot 500000"){ .glightbox data-gallery="brymen-bm857" }
<span class="caption">Bm 857 Mugshot 500000</span>

[![Bm857 Hv Slots](./img/Bm857_hv_slots.jpg)](./img/Bm857_hv_slots.jpg "Bm857 Hv Slots"){ .glightbox data-gallery="brymen-bm857" }
<span class="caption">Bm857 Hv Slots</span>

[![Bm857 Input Circuit](./img/Bm857_input_circuit.jpg)](./img/Bm857_input_circuit.jpg "Bm857 Input Circuit"){ .glightbox data-gallery="brymen-bm857" }
<span class="caption">Bm857 Input Circuit</span>

[![Bm857 Mcu 2blcdc 2](./img/Bm857_mcu_2Blcdc_2.jpg)](./img/Bm857_mcu_2Blcdc_2.jpg "Bm857 Mcu 2blcdc 2"){ .glightbox data-gallery="brymen-bm857" }
<span class="caption">Bm857 Mcu 2blcdc 2</span>

[![Bm859s Display Segments](./img/Bm859s-display-segments.jpg)](./img/Bm859s-display-segments.png "Bm859s Display Segments"){ .glightbox data-gallery="brymen-bm857" }
<span class="caption">Bm859s Display Segments</span>

[![Bm857 Back Noholster](./img/Bm857_back_noholster.jpg)](./img/Bm857_back_noholster.jpg "Bm857 Back Noholster"){ .glightbox data-gallery="brymen-bm857" }
<span class="caption">Bm857 Back Noholster</span>

[![Bm857 Lcd Backlit](./img/Bm857_lcd_backlit.jpg)](./img/Bm857_lcd_backlit.jpg "Bm857 Lcd Backlit"){ .glightbox data-gallery="brymen-bm857" }
<span class="caption">Bm857 Lcd Backlit</span>

[![Bm857 Package Contents](./img/Bm857_package_contents.jpg)](./img/Bm857_package_contents.jpg "Bm857 Package Contents"){ .glightbox data-gallery="brymen-bm857" }
<span class="caption">Bm857 Package Contents</span>

[![Bm859s Box Front](./img/Bm859s-box-front.jpg)](./img/Bm859s-box-front.png "Bm859s Box Front"){ .glightbox data-gallery="brymen-bm857" }
<span class="caption">Bm859s Box Front</span>

[![Bm859s Manual](./img/Bm859s-manual.jpg)](./img/Bm859s-manual.png "Bm859s Manual"){ .glightbox data-gallery="brymen-bm857" }
<span class="caption">Bm859s Manual</span>

[![Bm857 Opened](./img/Bm857_opened.jpg)](./img/Bm857_opened.jpg "Bm857 Opened"){ .glightbox data-gallery="brymen-bm857" }
<span class="caption">Bm857 Opened</span>

[![Bm857 Lowerpcb Bottom](./img/Bm857_lowerpcb_bottom.jpg)](./img/Bm857_lowerpcb_bottom.jpg "Bm857 Lowerpcb Bottom"){ .glightbox data-gallery="brymen-bm857" }
<span class="caption">Bm857 Lowerpcb Bottom</span>

[![Bm857 Hv Walls](./img/Bm857_hv_walls.jpg)](./img/Bm857_hv_walls.jpg "Bm857 Hv Walls"){ .glightbox data-gallery="brymen-bm857" }
<span class="caption">Bm857 Hv Walls</span>

[![Brymen Br85x Dmm Hookup All](./img/Brymen_br85x_dmm_hookup_all.jpg)](./img/Brymen_br85x_dmm_hookup_all.jpg "Brymen Br85x Dmm Hookup All"){ .glightbox data-gallery="brymen-bm857" }
<span class="caption">Brymen Br85x Dmm Hookup All</span>

[![Bm859s Front Sleeve](./img/Bm859s-front-sleeve.jpg)](./img/Bm859s-front-sleeve.png "Bm859s Front Sleeve"){ .glightbox data-gallery="brymen-bm857" }
<span class="caption">Bm859s Front Sleeve</span>

[![Bm857 Ics](./img/Bm857_ICs.jpg)](./img/Bm857_ICs.jpg "Bm857 Ics"){ .glightbox data-gallery="brymen-bm857" }
<span class="caption">Bm857 Ics</span>

[![Brymen Br85x Dmm Hookup Top](./img/Brymen_br85x_dmm_hookup_top.jpg)](./img/Brymen_br85x_dmm_hookup_top.jpg "Brymen Br85x Dmm Hookup Top"){ .glightbox data-gallery="brymen-bm857" }
<span class="caption">Brymen Br85x Dmm Hookup Top</span>

</div>
## BM850s series
The BM857s and BM859s meters (the BM850s series) uses the same protocol and works with the [ BC-85Xa adapters](https://sigrok.org/wiki/Device_cables#Brymen_BC-85Xa).

		- 
			[](./img/Bm859s-front-sleeve.png)

BM859s front with sleeve

		- 
			[](./img/Bm859s-front.png)

BM859s front

		- 
			[](./img/Bm859s-manual.png)

BM859s manual

		- 
			[](./img/Bm859s-box-front.png)

BM859s box front

		- 
			[](./img/Bm859s-display-segments.png)

BM859s display segments

## Protocol
Serial communication (genuine COM port), textual presentation of measurement values (floating point, normalized mantissa plus exponent), combined with binary bit fields for current meter's function and thus measured unit, variable length records with control chars in the header/footer (DLE, STX/ETX) around the mode flags and value's text, up to 22 bytes per DMM packet. See resources below for a full description of the protocol.

## Resources- vendor's [BM810/BM830/BM850 page](http://brymen.com/product-html/Products2-2.html) which links to individual 857/859 devices
- vendor's [download area](http://brymen.com/product-html/PD02BM850s_protocolDL.html), [BM850 section](http://brymen.com/product-html/PD02BM850s_protocolDL.html), [BM850s protocol details](http://brymen.com/product-html/images/DownloadList/ProtocolList/BM850-BM850a-BM850s_List/BM850-BM850a-BM850s-500000-count-DMM-protocol-BC85X-BC85Xa.zip) (links have changed in the past, might too in the future)
- BM850/BM850a/BM850s protocol documentation [download area](http://brymen.com/product-html/PD02BM850s_protocolDL.html) and [ZIP with PDF](http://brymen.com/product-html/images/DownloadList/ProtocolList/BM850-BM850a-BM850s_List/BM850-BM850a-BM850s-500000-count-DMM-protocol-BC85X-BC85Xa.zip) (worked as of 2019-06-10, vendor may change that)

