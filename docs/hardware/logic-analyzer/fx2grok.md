# Fx2Grok

The **fx2grok** family consists of four devices (fx2grok-flat, fx2grok-tiny, fx2grok-bga, fx2grok-wide) of **very small**, Open Hardware FX2-based logic analyzers. The schematics and layouts are done from scratch in [KiCad](http://kicad-pcb.org), and are released under the [CC-BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license. Using the open-source [fx2lafw](Fx2lafw.html "Fx2lafw") firmware (and OpenTraceLab, of course) you can use these devices as 8-channel (or 16-channel, for the fx2grok-wide) logic analyzers. 
## Contents 
\- [1 Device comparison](Fx2grok.html#Device_comparison) \- [2 What is NOT the goal?](Fx2grok.html#What_is_NOT_the_goal?) \- [3 Download](Fx2grok.html#Download) \- [4 fx2grok-tiny](Fx2grok.html#fx2grok-tiny) \- [4.1 Status](Fx2grok.html#Status) \- [4.2 Photos](Fx2grok.html#Photos) \- [4.2.1 Schematics, PCB layout, 3D preview](Fx2grok.html#Schematics,_PCB_layout,_3D_preview) \- [4.2.2 Cable and connector variants](Fx2grok.html#Cable_and_connector_variants) \- [4.2.3 Housing](Fx2grok.html#Housing) \- [4.2.4 Assembly](Fx2grok.html#Assembly) \- [4.3 Bill of materials](Fx2grok.html#Bill_of_materials) \- [4.4 Random notes](Fx2grok.html#Random_notes) \- [5 fx2grok-flat](Fx2grok.html#fx2grok-flat) \- [5.1 Status](Fx2grok.html#Status_2) \- [5.2 Photos](Fx2grok.html#Photos_2) \- [5.2.1 Schematics, PCB layout, 3D preview](Fx2grok.html#Schematics,_PCB_layout,_3D_preview_2) \- [6 Resources](Fx2grok.html#Resources) 
# Device comparison **Note**: Most of this is work in progress and might change at any time!  Item | fx2grok-flat | fx2grok-tiny | fx2grok-bga | fxgrok-wide  
---|---|---|---|---  
**Goals** 2 | 
  * Small
  * [Open Hardware](https://en.wikipedia.org/wiki/Open-source_hardware)
  * Convenient and reliable to use in practice
| 
  * Even smaller
  * [Open Hardware](https://en.wikipedia.org/wiki/Open-source_hardware)
  * "Just for fun" project, doesn't have to be practical
  * Sacrifices a lot of things for reduced size
| 
  * Smallest-possible
  * [Open Hardware](https://en.wikipedia.org/wiki/Open-source_hardware)
  * "Just for fun" project, doesn't have to be practical
  * Sacrifices even more things for reduced size
| 
  * Small, but 16 channels
  * [Open Hardware](https://en.wikipedia.org/wiki/Open-source_hardware)
  * Reliable and convenient, with a few more channels
**Author** | Piotr Esden-Tempski | Uwe Hermann | Uwe Hermann | Ryan "Izzy" Bales, based off of Piotr Esden-Tempski's fx2grok-flat  
**Status** | in progress | finished | WIP | WIP  
**Hardware license** | CC-BY-SA 4.0 | CC-BY-SA 4.0 1 | CC-BY-SA 4.0 | CC-BY-SA 4.0  
**Size** | 33 mm x 16 mm | 11 mm x 11 mm | tbd | tbd  
**Logic channels** | 8 + CLK & TRIG | 8 | tbd | 16  
**Layout specs** | 
  * One sided load 4 layer PCB/layout
  * 0.15 mm trace/space
  * 0.3 mm drill & 0.1 mm annular ring
| 
  * Double-sided 2-layer PCB/layout
  * Components soldered on both sides
  * 0.8 mm PCB thickness
  * 5 mil traces, 6 mil trace clearance
  * 8 mil via drill hole diameter, 5 mil annular ring
| tbd | tbd  
**Cypress FX2** | Cypress CY7C68013A-56LTXC, QFN, 8 mm x 8 mm | Cypress CY7C68013A-56LTXC, QFN, 8 mm x 8 mm | Cypress CY7C68013A-56BAXC, BGA, 5 mm x 5 mm | Cypress CY7C68013A-56LTXC, QFN, 8 mm x 8 mm  
**Input protection** | 3 x IP425x-4-TTL EMI/ESD filters on all probes + 100k pull-ups, 1x USBLC6-2 for USB | None whatsoever | None whatsoever | 100Ω on each probe, 4x DSILC6-4 for all probes, 1x USBLC6-2 for USB  
**24 MHz crytal** | ABM8 | 4-SMD, 300μW, 2 mm x 1.6 mm | tbd | tbd  
**USB connector** | USB Micro-B SMD | USB Micro-B SMD | tbd | USB Micro-B SMD  
**Probe connector** | 2x6 1.27 mm PCB-edge connector | 2x5 1.27 mm PCB-edge connector | tbd | 2x 2x5 1.27 mm PCB-edge connectors  
**EEPROM** | Yes, OpenTraceLab fx2lafw (8-channel) VID/PID 1d50:608c | None, default Cypress VID/PID 04b4:8613 | None, default Cypress VID/PID 04b4:8613 | Yes, OpenTraceLab fx2lafw (16-channel) VIP/PID 1d50:608d  
**Passives** | Mostly 0402, some 0603 & 0.4 mm pitch DFN | Only 0402 | tbd | Mostly 0402, some 0603  
**LED** | 1x 0603 LED on PA1 | 1x 0402 LED on PA1 | tbd | 1x 0603 LED on PA1  
1 The obsolete/nonworking fx2grok-tiny 0.1 was licensed CC-BY-SA 3.0, since version 0.2 the license is CC-BY-SA 4.0. 2 Optional goal: Make a tiny 3D-printed enclosure, and/or an "enclosure" using resin ([example](http://createdigitalmusic.com/files/stories/2006/august2006/resin_leds.jpg)) with the device (including probes) ideally looking similar to the OpenTraceLab logo in the end.  # What is NOT the goal? As you may know, there are [tons of FX2-based logic analyzers](Fx2lafw.html#Hardware_overview "Fx2lafw") (and tons of clones) already. There's not much use in creating yet another "standard" device. The goal of these projects is thus **NOT** necessarily to make a **better** device, or to make a **cheaper** device, or anything like that. The main goals are to to make them **Open Hardware** and to have them be **as tiny as possible** (they're mostly "just for fun" projects, especially the fx2grok-tiny and fx2grok-bga variants). # Download The schematics, PCB layout and Gerber files are available from the [fx2grok](https://github.com/OpenTraceLab/?p=fx2grok.git;a=summary) Git repository: $ git clone git://OpenTraceLab.org/fx2grok # fx2grok-tiny ## Status fx2grok-tiny 0.2 has been tested and is known to work. The first PCB version (fx2grok-tiny 0.1) is **not** working and thus obsolete. ## Photos ### Schematics, PCB layout, 3D preview **fx2grok-tiny 0.2**: \- 
[![\1](../../assets/hardware/general/\2)](./File:Fx2grok-tiny-0.2-kicad-schematics.svg.html)
Schematics
\- 
[![\1](../../assets/hardware/general/\2)](./File:Fx2grok-tiny-0.2-kicad-layout.png.html)
PCB layout
\- 
[![\1](../../assets/hardware/general/\2)](./File:Fx2grok-tiny-0.2-kicad-3d-top.png.html)
3D preview, top
\- 
[![\1](../../assets/hardware/general/\2)](./File:Fx2grok-tiny-0.2-kicad-3d-bottom.png.html)
3D preview, bottom
\- 
[![\1](../../assets/hardware/general/\2)](./File:Fx2grok-tiny-0.2-pinout.jpg.html)
Connector pinout
### Cable and connector variants **Samtec SFSD-05-28-H-10.00-SR + TFM-105-01-L-D**: \- 
[![\1](../../assets/hardware/general/\2)](./File:Fx2grok_samtec_cable_orig.jpg.html)
Samtec SFSD-05-28-H-10.00-SR
\- 
[![\1](../../assets/hardware/general/\2)](./File:Fx2grok_samtec_cable_conn.jpg.html)
Connector with notch
\- 
[![\1](../../assets/hardware/general/\2)](./File:Fx2grok_samtec_cable_crimp_parts.jpg.html)
Crimp parts
\- 
[![\1](../../assets/hardware/general/\2)](./File:Fx2grok_samtec_cable_crimp.jpg.html)
Crimp
\- 
[![\1](../../assets/hardware/general/\2)](./File:Fx2grok_0_2_crimp_tool.jpg.html)
Crimp tool
\- 
[![\1](../../assets/hardware/general/\2)](./File:Fx2grok_samtec_cable_finished.jpg.html)
Finished cable
\- 
[![\1](../../assets/hardware/general/\2)](./File:Fx2grok_samtec_cable_with_probes.jpg.html)
Cable with probes
\- 
[![\1](../../assets/hardware/general/\2)](./File:Fx2grok_0_2_crimp_heatshrink_tube1.jpg.html)
Heatshrink tube variant
\- 
[![\1](../../assets/hardware/general/\2)](./File:Fx2grok_0_2_crimp_heatshrink_tube2.jpg.html)
Heatshrink tube variant
\- 
[![\1](../../assets/hardware/general/\2)](./File:Fx2grok_0_2_cable_heatshrink_tube.jpg.html)
Heatshrink tube variant
\- 
[![\1](../../assets/hardware/general/\2)](./File:Fx2grok_0_2_device_heatshrink_tube_cable.jpg.html)
Heatshrink tube cable
\- 
[![\1](../../assets/hardware/general/\2)](./File:Fx2grok_samtec_cable_tfm.jpg.html)
Samtec TFM-105-01-L-D
\- 
[![\1](../../assets/hardware/general/\2)](./File:Fx2grok_samtec_cable_tfm2.jpg.html)
Samtec TFM-105-01-L-D
\- 
[![\1](../../assets/hardware/general/\2)](./File:Fx2grok_samtec_cable_connected.jpg.html)
Cable connected
\- 
[![\1](../../assets/hardware/general/\2)](./File:Fx2grok_samtec_cable_pinheader.jpg.html)
Cable + pinheader
**Hand-soldered ribbon cable**: \- 
[![\1](../../assets/hardware/general/\2)](./File:Fx2grok_ribbon_cable_orig.jpg.html)
Ribbon cable
\- 
[![\1](../../assets/hardware/general/\2)](./File:Fx2grok_ribbon_cable_wires.jpg.html)
Individual wires
\- 
[![\1](../../assets/hardware/general/\2)](./File:Fx2grok_ribbon_cable_soldered.jpg.html)
Soldered connector
\- 
[![\1](../../assets/hardware/general/\2)](./File:Fx2grok_ribbon_cable_conn_kapton.jpg.html)
Kapton tape
\- 
[![\1](../../assets/hardware/general/\2)](./File:Fx2grok_ribbon_cable_finished.jpg.html)
Finished cable
\- 
[![\1](../../assets/hardware/general/\2)](./File:Fx2grok_ribbon_cable_comparison.jpg.html)
Cable comparison
### Housing \- 
[![\1](../../assets/hardware/general/\2)](./File:Fx2grok_0_2_device_heatshrink_tube.jpg.html)
Heatshrink tube
\- 
[![\1](../../assets/hardware/general/\2)](./File:Fx2grok_0_2_device_heatshrink_tube_led.jpg.html)
Heatshrink tube, LED
### Assembly The current set of red PCBs was manufactured by [firstpcb.com](https://firstpcb.com/), solder stencils are manufactured by [oshstencils.com](https://www.oshstencils.com). You can use other PCB manufacturers of course, but don't forget that the PCB thickness must be 0.8mm (otherwise the probe connector won't fit) and that your PCB manufacturer must support all other specs (see table above). The device can be assembled without too much hassle even though all parts are 0402 or otherwise very tiny. \- Apply solderpaste with the stencil to one PCB side. \- Place the parts with a pair of tweezers on the solderpaste (steady hands help, but no microscope is required). \- Solder the parts (a Puhui T-962A oven was used in this case; it should also be doable with a hot air gun/station or a modified pizza oven, though). \- Put some kapton tape on the soldered parts to prevent them from falling off while soldering the other PCB side in the oven. \- Apply solderpaste with the stencil to the other PCB side, place the parts, solder in the oven again. \- As a last step, manually solder (soldering iron) the 5x2 pins edge connector.  \- 
[![\1](../../assets/hardware/general/\2)](./File:Fx2grok_0_2_pcb_panel.jpg.html)
PCB panel
\- 
[![\1](../../assets/hardware/general/\2)](./File:Fx2grok_0_2_pcbs.jpg.html)
PCBs
\- 
[![\1](../../assets/hardware/general/\2)](./File:Fx2grok_0_2_pcb_top.jpg.html)
PCB, top
\- 
[![\1](../../assets/hardware/general/\2)](./File:Fx2grok_0_2_pcb_bottom.jpg.html)
PCB, bottom
\- 
[![\1](../../assets/hardware/general/\2)](./File:Fx2grok_0_2_stencil_top.jpg.html)
Stencil, top
\- 
[![\1](../../assets/hardware/general/\2)](./File:Fx2grok_0_2_stencil_bottom.jpg.html)
Stencil, bottom
\- 
[![\1](../../assets/hardware/general/\2)](./File:Fx2grok_0_2_solderpaste.jpg.html)
Solderpaste
\- 
[![\1](../../assets/hardware/general/\2)](./File:Fx2grok_0_2_pcb_top_populated.jpg.html)
PCB, top, populated
\- 
[![\1](../../assets/hardware/general/\2)](./File:Fx2grok_0_2_pcb_bottom_populated.jpg.html)
PCB, bottom, populated
\- 
[![\1](../../assets/hardware/general/\2)](./File:Fx2grok-tiny-0.2-solderprofile.jpg.html)
Example solderprofile
\- 
[![\1](../../assets/hardware/general/\2)](./File:Fx2grok_0_2_device_top.jpg.html)
Device, top
\- 
[![\1](../../assets/hardware/general/\2)](./File:Fx2grok_0_2_device_bottom.jpg.html)
Device, bottom
\- 
[![\1](../../assets/hardware/general/\2)](./File:Fx2grok_0_2_device_and_cable.jpg.html)
Device and cable
\- 
[![\1](../../assets/hardware/general/\2)](./File:Fx2grok_0_2_size_comparison.jpg.html)
Size comparison
## Bill of materials **Note:** All prices are for single quantities, most parts get a lot cheaper if you buy higher quantities.  Qty | Device | Footprint | Size | Value | Refdes | Digikey | Mouser | Comments  
---|---|---|---|---|---|---|---|---  
Required parts  
1 | Cypress CY7C68013A-56LTXC | QFN-56 | 8 mm x 8 mm | — | IC1 | [10.05€](https://www.digikey.de/product-detail/en/cypress-semiconductor-corp/CY7C68013A-56LTXC/428-2933-ND/2096128?cur=EUR&lang=en) | [10.30€](http://www.mouser.de/search/ProductDetail.aspx?R=0virtualkey0virtualkeyCY7C68013A-56LTXC) | Main chip. Alternatives: 
  * [Future Electronics: 6.55€](http://de.futureelectronics.com/de/technologies/semiconductors/microcontrollers/8-bit/Seiten/6482053-CY7C68013A-56LTXC.aspx)
  * [eBay: 4.07€](http://www.ebay.de/itm/1-PCS-CY7C68013A-56LFXC-QFN56-CY7C68013A-56-EZ-USB-FX2LP-USB-Microcontroller-/371990499413)
  * [Aliexpress: 1.52€](https://www.aliexpress.com/item/10PCS-Free-shipping-CY7C68013A-CY7C68013A-56LFXC-CYPRESS-NEW/32758119152.html) (10 pcs lot, 15.16€ total)
1 | Amphenol FCI 10118192-0001LF | custom | 9.8 mm x 5.6 mm | — | U1 | [0.38€](https://www.digikey.de/product-detail/en/amphenol-fci/10118192-0001LF/609-4613-1-ND/2785378) | [0.35€](http://www.mouser.de/ProductDetail/FCI-Amphenol/10118192-0001LF/?qs=%2fha2pyFadujgPm4iVaIQmAH7IEAODLQazmlVAs%2fyYaruZkWE0oGmeA%3d%3d) | USB Micro-B SMD connector  
1 | Murata XRCGB24M000FAN00R0 | custom | 2 mm x 1.6 mm | 24 MHz | Y1 | [0.29€](https://www.digikey.de/product-detail/en/murata-electronics-north-america/XRCGB24M000FAN00R0/490-16962-1-ND/7595843) | [0.46€](http://www.mouser.de/ProductDetail/Murata/XRCGB24M000FAN00R0/?qs=%2fha2pyFaduhVXszias80rJExv6kKRiz8I6J1KIwVm7ZBhPSw4cO1NxDYBb%252bWztLR) | 24MHz crystal, ±25ppm, 6pF, 150 Ohms, max. 300μW drive level, 4-SMD, no lead  
1 | Micrel MIC5504-3.3YM5-TR | SOT-23-5 | 2.9 mm x 1.6 mm | 3.3 V | U2 | [0.10€](https://www.digikey.de/product-detail/en/microchip-technology/MIC5504-3.3YM5-TR/576-4764-1-ND/4864028) | [0.10€](http://www.mouser.de/ProductDetail/Microchip/MIC5504-33YM5-TR/?qs=%2fha2pyFadujyBzUvhx7nCVHVS1wEK1ahUM91xHyBxIk%3d) | 3.3 V LDO, max. 300mA  
4 | Yageo RC0402JR-072R7L | 0402 | 0.25 mm x 0.125 mm | 2.7 kΩ | R2, R3, R4, R5 | [0.08€](https://www.digikey.de/product-detail/en/yageo/RC0402JR-072K7L/311-2.7KJRCT-ND/729385) | [0.08€](http://www.mouser.de/ProductDetail/Yageo/RC0402JR-072K7L/?qs=%2fha2pyFadugNN0LzwXn2qKv1NucjI%2fazrntxBF%2f%2fhLo7g%252bIVZPpP%2fw%3d%3d) | Resistor  
1 | Samsung RC1005J104CS | 0402 | 0.25 mm x 0.125 mm | 100 kΩ | R1 | [0.08€](https://www.digikey.de/product-detail/en/samsung-electro-mechanics-america-inc/RC1005J104CS/1276-4424-1-ND/3967396) | — | Resistor  
8 | Samsung CL05A104KP5NNNC | 0402 | 0.25 mm x 0.125 mm | 100 nF | C2, C5, C7, C8, C10-C13 | [0.08€](https://www.digikey.de/product-detail/en/samsung-electro-mechanics-america-inc/CL05A104KP5NNNC/1276-1022-1-ND/3889108) | — | Ceramic capacitor  
3 | Taiyo Yuden JMK105BJ105KV-F | 0402 | 0.25 mm x 0.125 mm | 1 µF | C1, C14, C16 | [0.08€](https://www.digikey.de/product-detail/en/taiyo-yuden/JMK105BJ105KV-F/587-1231-1-ND/931008) | [0.10€](http://www.mouser.de/ProductDetail/Taiyo-Yuden/JMK105BJ105KV-F/?qs=%2fha2pyFaduhVfLicOtMYHog0miohobAaExAZufXB%2f%252bdY5R%252bltkZq0w%3d%3d) | Ceramic capacitor  
2 | Murata GRM155R61A225KE95D | 0402 | 0.25 mm x 0.125 mm | 2.2 µF | C3, C6 | [0.08€](https://www.digikey.de/product-detail/en/murata-electronics-north-america/GRM155R61A225KE95D/490-10451-1-ND/5026361) | [0.08€](http://www.mouser.de/ProductDetail/Murata/GRM155R61A225KE95D/?qs=%2fha2pyFadugsr51Fgcs3VEkc4xRHZwzRUbwbh2dpjzoRDOGgmOp%2fmzl%252bsz3xq7eG) | Ceramic capacitor  
2 | Samsung CL05C120JB5NNNC | 0402 | 0.25 mm x 0.125 mm | 12 pF | C4, C9 | [0.08 ](https://www.digikey.de/product-detail/en/samsung-electro-mechanics-america-inc/CL05C120JB5NNNC/1276-1178-1-ND/3889264) | — | Ceramic capacitor  
1 | Vishay VLMB1500-GS08 | 0402 | 0.25 mm x 0.125 mm | — | D1 | [0.34€](https://www.digikey.de/product-detail/en/vishay-semiconductor-opto-division/VLMB1500-GS08/VLMB1500-GS08CT-ND/3504671) | [0.51€](http://www.mouser.de/ProductDetail/Vishay/VLMB1500-GS08/?qs=%2fha2pyFaduhN70pSEFaWb7ncGFJYKJC0keOOL0VlVLSzC7zQ0fA2Ng%3d%3d) | LED. When using other LED colors, you might also want a lower value for R5.  
Optional parts / variants  
1 | Amphenol FCI 20021111-00010T4LF | custom | — | — | P1/P2 | [0.53€](https://www.digikey.de/product-detail/en/20021111-00010T4LF/609-3712-ND/2209072) | [0.55€](http://www.mouser.de/ProductDetail/FCI/20021111-00010T4LF/?qs=%2fha2pyFadug5qLbZ9z2ci%2fTjUM7AITCGO1cafk55nZhEq%252b0iFQt31y%2f99h8z8QRG) | 5x2 through-hole pin header (1.27 mm pitch), could soldered to the PCB (5 pins per side)  
1 | Amphenol FCI 20021311-00010T4LF | custom | — | — | — | [0.68€](https://www.digikey.de/product-detail/en/20021311-00010T4LF/609-3754-ND/2209079) | [0.69€](http://www.mouser.de/ProductDetail/FCI/20021311-00010T4LF/?qs=%2fha2pyFaduhY7txd7xCZHyqlTMKSj7DOXT7F8SKnNS3QPZpSMC9CyD3j5oh5%2fHMK) | 5x2 connector/receptacle (1.27 mm pitch), could be used for soldering the probe cable/wires  
1 | Samtec TFM-105-01-L-D | custom | — | — | P1/P2 | [0.53€](https://www.digikey.de/product-detail/en/samtec-inc/TFM-105-01-L-D/SAM9148-ND/6613860) | — | 5x2 through-hole pin header (1.27 mm pitch) with a notch, soldered to the PCB (5 pins per side), match for the Samtec SFSD-05-28-H-10.00-SR cable below  
1 | Samtec SFSD-05-28-H-10.00-SR | custom | — | — | — | [4.77€](https://www.digikey.de/product-detail/en/samtec-inc/SFSD-05-28-H-10.00-SR/SAM8668-ND/1785919) | — | Potential probe cable, needs some crimping  
**Note**: C15 is missing and there is a C16, which is correct. C15 was removed and the numbering wasn't reset. ## Random notes \- No, you cannot order assembled fx2grok-tiny devices or the bare PCBs anywhere, this is a pure hobby project. You can, however, make your own devices. Everything is Open Hardware, Open Source, and documented. \- The fx2grok-tiny device sacrifices a lot of things in order to make it as tiny as possible: \- There's no input protection whatsoever on the probes, not even a simple resistor. This means (among other things) you'll see random garbage on unconnected probes (which can be avoided by explicitly attaching them to a GND, though). \- There's no protection circuitry whatsoever on the USB side either. \- The device has no EEPROM, so it'll enumerate with the default Cypress USB VID/PID of 04b4:8613. OpenTraceCapture/fx2fwla currently assume all such devices are plain FX2 eval boards with all 16 channels accessible. However, fx2grok-tiny only has 8 channels on the connector, so until we have a nicer permanent fix for this, you have to either limit your samplerate to 12MHz (you cannot use 16MHz or 24MHz), or you can patch the OpenTraceCapture fx2lafw driver to treat devices with a VID/PID of 04b4:8613 as 8-channel devices (instead of 16-channel devices):  diff --git a/src/hardware/fx2lafw/api.c b/src/hardware/fx2lafw/api.c index 34c5bc41..1634635a 100644 \--- a/src/hardware/fx2lafw/api.c +++ b/src/hardware/fx2lafw/api.c @@ -70,7 +70,7 @@ static const struct fx2lafw_profile supported_fx2[] = { */ { 0x04B4, 0x8613, "Cypress", "FX2", NULL, "fx2lafw-cypress-fx2.fw", \- DEV_CAPS_16BIT, NULL, NULL }, \+ 0, NULL, NULL },  \- Many of the recommendations from the Cypress FX2 datasheets and guides are ignored on the fx2grok-tiny (mostly in order to be able to make it smaller, sometimes also a bit simpler). While this seems to work fine regardless (for now), you shouldn't be too surprised if there are issues eventually. \- Unused pins should be tied to GND as per vendor (this is not done, though). \- The recommended crystal should have 12 pF (5 percent tolerance) load capacitors, we're using a crystal that wants 6 pF as per datasheet. \- The recommended crystal should have 500 µW drive level, we're using one with 300 µW. \- Cypress recommends a 4 layer PCB (we use a 2 layer PCB) and various other PCB layout / solderability related things that we're ignoring. \- The solderpaste is a big solid area under the FX2 device, it would be a bit nicer to have that part be a checkerboard pattern (but it seems to work well enough like this, too). \- etc. etc. \- The Gerber files intentionally don't include silkscreen (not really needed, might be too tiny anyway, sometimes might increase PCB manufacturing costs). However, the silkscreen is "abused" in the KiCad files to generate nice 3D previews (see above) that can be helpful when assembling the device. \- The fx2grok-tiny device currently has a blue LED with a 2k7 resistor (R5), which is sufficiently bright. If you want to use other LED colors you might also want to use a lower resistor value to increase brightness. # fx2grok-flat ## Status fx2grok-flat 0.2 has been tested and is known to work, but is not yet the final version. Additional improvements will be implemented in version 0.3. ## Photos ### Schematics, PCB layout, 3D preview **fx2grok-flat 0.2**: \- 
[![\1](../../assets/hardware/general/\2)](./File:FX2Grok-flat-v0-2-3d-top.jpg.html)
3D preview, top
\- 
[![\1](../../assets/hardware/general/\2)](./File:FX2Grok-flat-v0-2-3d-bottom.jpg.html)
3D preview, bottom
# Resources \- [Cypress FX2 overview page](http://www.cypress.com/products/ez-usb-fx2lp) \- [CY7C68013A, CY7C68014A, CY7C68015A, CY7C68016A datasheet](http://www.cypress.com/documentation/datasheets/cy7c68013a-cy7c68014a-cy7c68015a-cy7c68016a-ez-usb-fx2lp-usb) ([PDF](http://www.cypress.com/file/138911/download)) \- [EZ-USB Technical Reference Manual (TRM)](http://www.cypress.com/documentation/technical-reference-manuals/ez-usb-technical-reference-manual) ([PDF](http://www.cypress.com/file/126446/download)) \- [AN15456 - Guide to a Successful EZ-USB FX2LP Hardware Design](http://www.cypress.com/documentation/application-notes/an15456-guide-successful-ez-usb-fx2lp-hardware-design) ([PDF](http://www.cypress.com/file/135006/download)) \- esden's [series of videos](https://www.youtube.com/playlist?list=PLOF903IIpqjOwHIjT7VFqbxBhEHG8v5__) on the fx2grok-flat design (schematics, PCB, with background information and almost a KiCad tutorial) \- esden's [GitHub repository](https://github.com/esden/fx2grok/) with the KiCad project files for the fx2grok-flat (in the "flat" branch) \- Ryan's [GitHub repository](https://github.com/izzy84075/fx2grok) with the KiCad project files for the fx2grok-wide (in the "wide" branch) 
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=Fx2grok&oldid=13036](https://OpenTraceLab.org/w/index.php?title=Fx2grok&oldid=13036)"

## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
