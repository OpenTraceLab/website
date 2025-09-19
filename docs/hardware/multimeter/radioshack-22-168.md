# Radioshack 22 168
| | | |:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:| | [*Image: \1* | | | Status | supported | | Source code | [serial-dmm](http://github.com/OpenTraceLab/?p=OpenTraceCapture.git;a=tree;f=src/hardware/serial-dmm) | | Counts | 2000 | | IEC 61010-1 | Unspecified | | Connectivity | RS232 | | Measurements | voltage, current, resistance, capacitance, continuity, diode, logic, frequency, hFE | | Features | data hold, min/max, 10 reading memory | | Website | [radioshack.com](http://support.radioshack.com/productinfo/DocumentResults.asp?sku_id=22-168&Name=Meters%20and%20Scopes&Reuse=N) | **RadioShack 22-168** The **RadioShack 22-168** is a 2000 counts handheld digital multimeter with RS-232 connectivity.
## Contents
\- *1 Hardware* \- *2 Photos* \- *3 Protocol* \- *4 Resources*
## Hardware \- **3 1/2 digit ADC with bandgap reference**: [Maxim MAX130CPL](http://www.maxim-ic.com/datasheet/index.mvp/id/1288) ([datasheet](http://datasheets.maxim-ic.com/en/ds/MAX130-MAX131.pdf)) (marking: "Maxim MAX130CPL 0138-3 C10039") \- **CPU**: Metex KS57C2016 (Samsung KS57C2016 4-bit microcontroller with custom Metex firmware) (marking: "Metex 93D3 KS57C2016-02 410") \- **?**: Metex 9005 (marking has ST logo: "Metex 9005 MET7ACS 92A32792BA") \- **Crystal**: 4.1856MHz crystal \- **555 timer**: *Intersil ICM7555CBA* ([datasheet](http://www.intersil.com/content/dam/Intersil/documents/fn28/fn2867.pdf)) (marking: "H 7555 CBA L405") \- **Quad analog switch/quad multiplexer**: [Motorola 14066B](http://www.onsemi.com/PowerSolutions/product.do?id=MC14066B) ([datasheet](http://www.onsemi.com/pub/Collateral/MC14066B-D.PDF)) (marking: "14066B XAC334") \- **Quad 2-input NAND gate**: GD4011BD \- **Optoisolator**: Lite-ON LTV-817 \- **Unidentified ICs**: Two ICs, which appear to be SSOP8 packages are hidden behind black goo. The purpose of the goo is unknown. ## Photos \-
[*Image: \1*
Device, angle
\-
[*Image: \1*
Mugshot
\-
[*Image: \1*
Device, back
\-
[*Image: \1*
"Metex" logo on the stand
\-
[*Image: \1*
Battery compartment
\-
[*Image: \1*
Battery cover
\-
[*Image: \1*
Opened up
\-
[*Image: \1*
Spare fuse
\-
[*Image: \1*
Front cover, PCB still mounted
\-
[*Image: \1*
Front cover
\-
[*Image: \1*
Rear cover
\-
[*Image: \1*
Bare electronics
\-
[*Image: \1*
Range-switch sandwiched between PCBs
\-
[*Image: \1*
Range-switch
\-
[*Image: \1*
Main PCB, front
\-
[*Image: \1*
Secondary PCB, front
\-
[*Image: \1*
Secondary PCB, back
\-
[*Image: \1*
Main PCB, front, illuminated
\-
[*Image: \1*
Main PCB, back, illuminated
\-
[*Image: \1*
Secondary PCB, front, illuminated
\-
[*Image: \1*
Secondary PCB, back, illuminated
\-
[*Image: \1*
Unidentified components protected by black coating
\-
[*Image: \1*
Metex KS57C2016 CPU
\-
[*Image: \1*
4.1856 MHz crystal
\-
[*Image: \1*
MAX130CPL ADC
\-
[*Image: \1*
Metex 9005 7ACS (ST Micro logo)
\-
[*Image: \1*
MC14066B Quad Analog Switch/Quad Multiplexer (left) and GD4011BD quad 2-input NAND gate (right)
\-
[*Image: \1*
555 Timer
\-
[*Image: \1*
RS-232 optoisolation
\-
[*Image: \1*
LCD display
\-
[*Image: \1*
LCD display, back
\-
[*Image: \1*
RS-232 interface port
\-
[*Image: \1*
RS-232 cable, mated
**Cable:** See *Device_cables#Metex_5-pin_RS232_cable*. ## Protocol See *Multimeter_ICs#Metex_14-byte_ASCII*. ## Resources \- [Vendor software](https://www.radioshack.com/search/softwareResults.jsp?kw=22-168) \- [Software download](http://www.radioshack.com/graphics/uc/rsk/Support/SoftwareDownload/2200168.exe) \- *linuxtoys.org: Radio Shack DMM with RS-232*
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=RadioShack_22-168&oldid=6055](https://OpenTraceLab.org/w/index.php?title=RadioShack_22-168&oldid=6055)"
: \- *Device* \- *Multimeter* \- *Supported*
## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
