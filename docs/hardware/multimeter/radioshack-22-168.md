# Radioshack 22 168

| | | |:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:| | [![\1](../../assets/hardware/general/\2)](./File:Rs_22_168_angle.png.html) | | | Status | supported | | Source code | [serial-dmm](http://github.com/OpenTraceLab/?p=OpenTraceCapture.git;a=tree;f=src/hardware/serial-dmm) | | Counts | 2000 | | IEC 61010-1 | Unspecified | | Connectivity | RS232 | | Measurements | voltage, current, resistance, capacitance, continuity, diode, logic, frequency, hFE | | Features | data hold, min/max, 10 reading memory | | Website | [radioshack.com](http://support.radioshack.com/productinfo/DocumentResults.asp?sku_id=22-168&Name=Meters%20and%20Scopes&Reuse=N) | **RadioShack 22-168** The **RadioShack 22-168** is a 2000 counts handheld digital multimeter with RS-232 connectivity. 
## Contents 
\- [1 Hardware](RadioShack_22-168.html#Hardware) \- [2 Photos](RadioShack_22-168.html#Photos) \- [3 Protocol](RadioShack_22-168.html#Protocol) \- [4 Resources](RadioShack_22-168.html#Resources) 
## Hardware \- **3 1/2 digit ADC with bandgap reference**: [Maxim MAX130CPL](http://www.maxim-ic.com/datasheet/index.mvp/id/1288) ([datasheet](http://datasheets.maxim-ic.com/en/ds/MAX130-MAX131.pdf)) (marking: "Maxim MAX130CPL 0138-3 C10039") \- **CPU**: Metex KS57C2016 (Samsung KS57C2016 4-bit microcontroller with custom Metex firmware) (marking: "Metex 93D3 KS57C2016-02 410") \- **?**: Metex 9005 (marking has ST logo: "Metex 9005 MET7ACS 92A32792BA") \- **Crystal**: 4.1856MHz crystal \- **555 timer**: [Intersil ICM7555CBA](http://www.intersil.com/content/intersil/en/products/timing-and-digital/counters-time-base-ics/counter-time-base-ics/ICM7555.html) ([datasheet](http://www.intersil.com/content/dam/Intersil/documents/fn28/fn2867.pdf)) (marking: "H 7555 CBA L405") \- **Quad analog switch/quad multiplexer**: [Motorola 14066B](http://www.onsemi.com/PowerSolutions/product.do?id=MC14066B) ([datasheet](http://www.onsemi.com/pub/Collateral/MC14066B-D.PDF)) (marking: "14066B XAC334") \- **Quad 2-input NAND gate**: GD4011BD \- **Optoisolator**: Lite-ON LTV-817 \- **Unidentified ICs**: Two ICs, which appear to be SSOP8 packages are hidden behind black goo. The purpose of the goo is unknown. ## Photos \- 
[![\1](../../assets/hardware/general/\2)](./File:Rs_22_168_angle.png.html)
Device, angle
\- 
[![\1](../../assets/hardware/general/\2)](./File:Rs_22_168_mugshot.png.html)
Mugshot
\- 
[![\1](../../assets/hardware/general/\2)](./File:Rs_22_168_back.jpg.html)
Device, back
\- 
[![\1](../../assets/hardware/general/\2)](./File:Rs_22_168_metex_stand.jpg.html)
"Metex" logo on the stand
\- 
[![\1](../../assets/hardware/general/\2)](./File:Rs_22_168_batt_comp.jpg.html)
Battery compartment
\- 
[![\1](../../assets/hardware/general/\2)](./File:Rs_22_168_batt_cover.jpg.html)
Battery cover
\- 
[![\1](../../assets/hardware/general/\2)](./File:Rs_22_168_opened_mooning.jpg.html)
Opened up
\- 
[![\1](../../assets/hardware/general/\2)](./File:Rs_22_168_spare_fuse.jpg.html)
Spare fuse
\- 
[![\1](../../assets/hardware/general/\2)](./File:Rs_22_168_inside_mooning.jpg.html)
Front cover, PCB still mounted
\- 
[![\1](../../assets/hardware/general/\2)](./File:Rs_22_168_cover_front.jpg.html)
Front cover
\- 
[![\1](../../assets/hardware/general/\2)](./File:Rs_22_168_cover_back.jpg.html)
Rear cover
\- 
[![\1](../../assets/hardware/general/\2)](./File:Rs_22_168_bare_dmm.jpg.html)
Bare electronics
\- 
[![\1](../../assets/hardware/general/\2)](./File:Rs_22_168_sandwiched_pcb.jpg.html)
Range-switch sandwiched between PCBs
\- 
[![\1](../../assets/hardware/general/\2)](./File:Rs_22_168_rangeswitch.jpg.html)
Range-switch
\- 
[![\1](../../assets/hardware/general/\2)](./File:Rs_22_168_pcb_main_front.jpg.html)
Main PCB, front
\- 
[![\1](../../assets/hardware/general/\2)](./File:Rs_22_168_pcb_second_top.jpg.html)
Secondary PCB, front
\- 
[![\1](../../assets/hardware/general/\2)](./File:Rs_22_168_pcb_second_bottom.jpg.html)
Secondary PCB, back
\- 
[![\1](../../assets/hardware/general/\2)](./File:Rs_22_168_pcb_main_front_light.jpg.html)
Main PCB, front, illuminated
\- 
[![\1](../../assets/hardware/general/\2)](./File:Rs_22_168_pcb_main_back_light.jpg.html)
Main PCB, back, illuminated
\- 
[![\1](../../assets/hardware/general/\2)](./File:Rs_22_168_pcb_top_light.jpg.html)
Secondary PCB, front, illuminated
\- 
[![\1](../../assets/hardware/general/\2)](./File:Rs_22_168_pcb_2_bottom_light.jpg.html)
Secondary PCB, back, illuminated
\- 
[![\1](../../assets/hardware/general/\2)](./File:Rs_22_168_hidden_components.jpg.html)
Unidentified components protected by black coating
\- 
[![\1](../../assets/hardware/general/\2)](./File:Rs_22_168_ics5.jpg.html)
Metex KS57C2016 CPU
\- 
[![\1](../../assets/hardware/general/\2)](./File:Rs_22_168_mosc.jpg.html)
4.1856 MHz crystal
\- 
[![\1](../../assets/hardware/general/\2)](./File:Rs_22_168_ics3.jpg.html)
MAX130CPL ADC
\- 
[![\1](../../assets/hardware/general/\2)](./File:Rs_22_168_ics4.jpg.html)
Metex 9005 7ACS (ST Micro logo)
\- 
[![\1](../../assets/hardware/general/\2)](./File:Rs_22_168_ics1.jpg.html)
MC14066B Quad Analog Switch/Quad Multiplexer (left) and GD4011BD quad 2-input NAND gate (right)
\- 
[![\1](../../assets/hardware/general/\2)](./File:Rs_22_168_ics2.jpg.html)
555 Timer
\- 
[![\1](../../assets/hardware/general/\2)](./File:Rs_22_168_optoisolation.jpg.html)
RS-232 optoisolation
\- 
[![\1](../../assets/hardware/general/\2)](./File:Rs_22_168_lcd.jpg.html)
LCD display
\- 
[![\1](../../assets/hardware/general/\2)](./File:Rs_22_168_lcd_back.jpg.html)
LCD display, back
\- 
[![\1](../../assets/hardware/general/\2)](./File:Rs_22_168_rs232_interface_port.jpg.html)
RS-232 interface port
\- 
[![\1](../../assets/hardware/general/\2)](./File:Rs_22_168_cable_mated.jpg.html)
RS-232 cable, mated
**Cable:** See [Device_cables#Metex_5-pin_RS232_cable](Device_cables.html#Metex_5-pin_RS232_cable "Device cables"). ## Protocol See [Multimeter_ICs#Metex_14-byte_ASCII](Multimeter_ICs.html#Metex_14-byte_ASCII "Multimeter ICs"). ## Resources \- [Vendor software](https://www.radioshack.com/search/softwareResults.jsp?kw=22-168) \- [Software download](http://www.radioshack.com/graphics/uc/rsk/Support/SoftwareDownload/2200168.exe) \- [linuxtoys.org: Radio Shack DMM with RS-232](http://www.linuxtoys.org/dvm/dvm.html)
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=RadioShack_22-168&oldid=6055](https://OpenTraceLab.org/w/index.php?title=RadioShack_22-168&oldid=6055)" 
[Categories](specialcategories-specialcategories.md): \- [Device](./Category:Device.html "Category:Device") \- [Multimeter](./Category:Multimeter.html "Category:Multimeter") \- [Supported](./Category:Supported.html "Category:Supported")

## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
