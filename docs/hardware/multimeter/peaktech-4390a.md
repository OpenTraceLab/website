# Peaktech 4390A

| | | |:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------------------------------------:| | [![\1](../../assets/hardware/general/\2)](./File:Peaktech_4390a_metex_m-3860m_mugshot.png.html) | | | Status | supported | | Source code | [serial-dmm](http://github.com/OpenTraceLab/?p=OpenTraceCapture.git;a=tree;f=src/hardware/serial-dmm) | | Counts | 4000 | | IEC 61010-1 | — | | Connectivity | RS232 | | Measurements | voltage, current, frequency, hFE, logic, continuity, diode, resistance, temperature, capacitance, power | | Features | true-rms, signal-out, 3 sub-displays, backlight, bargraph, auto hold, data hold, range hold, min/max, relative offset, comparision, 10 reading memory | **PeakTech 4390A** The **PeakTech 4390A** is a 4000 counts handheld digital multimeter with RS232 connectivity. This is a rebadged [Metex M-3860M](https://web.archive.org/web/20090221062027/http://imetex.com:80/html/product/product_model_detail.asp?idx=27) multimeter. **Note:** This is **not** the same device as the [PeakTech 4390](PeakTech_4390.html "PeakTech 4390"), despite the very similar name. 
## Contents 
\- [1 Hardware](PeakTech_4390A.html#Hardware) \- [2 Photos](PeakTech_4390A.html#Photos) \- [3 Protocol](PeakTech_4390A.html#Protocol) \- [4 Resources](PeakTech_4390A.html#Resources) 
## Hardware **Main ICs**: \- **Multimeter IC**: Metex 00M38M03 (markings: METEX / 00M38M03 / 663 / 0411KK002) \- **A/D Converter**: [Maxim MAX134 3 3/4 Digit DMM Circuit](https://www.maximintegrated.com/en/products/analog/data-converters/analog-to-digital-converters/MAX134.html) ([datasheet](https://datasheets.maximintegrated.com/en/ds/MAX133-MAX134.pdf)) \- **True RMS Converter**: [Analog Devices AD737](http://www.analog.com/en/products/linear-products/rms-to-dc-converters/ad737.html) ([datasheet](http://www.analog.com/media/en/technical-documentation/data-sheets/AD737.pdf)) \- **Power Metering IC**: [Sames SA9102CSA](http://www.sames.co.za/energy-metering-legacy/) ([datasheet](http://www.sames.co.za/wp-content/uploads/pdf/legacy/SA9102C.pdf)) \- **Voltage Reference 1.2V**: ICL8069 ([datasheet](https://www.intersil.com/content/dam/Intersil/documents/icl8/icl8069.pdf)) (markings: CC / 8069 / G301AC) \- **LCD Controller**: Epson S1D12708F00A1 (markings: EPSON JAPAN / S1D12708F00A1 / F04202336) **Miscellaneous ICs**: \- **Serial EEPROM**: Atmel AT93C46 ([datasheet](http://www.atmel.com/Images/doc5140.pdf)) (markings: ATMEL 348 / 93C46) \- **Optocoupler for RS232**: 2x [Lite-On 817B](http://optoelectronics.liteon.com/en-global/Led/LED-Component/Detail/651/0/LTV-817%20Series) ([datasheet](http://optoelectronics.liteon.com/upload/download/DS-70-96-0013/LTV-8X4%20series%20201509.pdf)) (markings: L0419 / 817B / Y) \- **OpAmp**: 2x 2904 ([datasheet](http://www.njr.com/semicon/PDF/NJM2904_E.pdf)) (markings: 2904 / 4169B / JRC) \- **Low Offset Voltage OpAmp**: OP-07 ([datasheet](http://www.njr.com/semicon/PDF/NJMOP-07_E.pdf)) (markings: OP-07 / 4051B / JRC) \- **OpAmp**: NJM062/TL062 ([datasheet](http://www.njr.com/semicon/PDF/NJM062_NJM064_E.pdf)) (markings: 062 / 3138B / JRC) \- **Quad 2-Input NAND Gate**: ON Semi 74HC00A ([datasheet](https://www.onsemi.com/pub/Collateral/MC74HC00A-D.PDF)) (markings: HC00A / ON PBK340) \- **Quad Multiplexer**: ON Semi 14066B ([datasheet](https://www.onsemi.com/pub/Collateral/MC14066B-D.PDF)) (markings: 14066B / ON PPM426) \- **555 Timer**: Intersil ICM7555 ([datasheet](https://www.intersil.com/content/dam/Intersil/documents/icm7/icm7555-56.pdf)) (markings: i 7555 / IBA / L044FCL) \- **Quad 2-Input NAND Schmitt Trigger**: 74HC132D ([datasheet](https://assets.nexperia.com/documents/data-sheet/74HC_HCT132.pdf)) \- **Dual Decade Ripple Counter**: 74HC390D ([datasheet](https://assets.nexperia.com/documents/data-sheet/74HC_HCT390.pdf)) **Fuses**: \- 250V, 15A (N65) \- 250V, 800mA ## Photos **Multimeter**: \- 
[![\1](../../assets/hardware/general/\2)](./File:Peaktech_4390a_metex_m-3860m_top.jpg.html)
Device, top
\- 
[![\1](../../assets/hardware/general/\2)](./File:Peaktech_4390a_metex_m-3860m_bottom.jpg.html)
Device, bottom
\- 
[![\1](../../assets/hardware/general/\2)](./File:Peaktech_4390A_Metex_M-3860M_-_Shielding.jpg.html)
Big PCB, shielding
\- 
[![\1](../../assets/hardware/general/\2)](./File:Peaktech_4390A_Metex_M-3860M_-_PCB_Bottom.jpg.html)
Big PCB, bottom
\- 
[![\1](../../assets/hardware/general/\2)](./File:Peaktech_4390A_Metex_M-3860M_-_PCB_Top_1.jpg.html)
PCB sandwich, top
\- 
[![\1](../../assets/hardware/general/\2)](./File:Peaktech_4390A_Metex_M-3860M_-_PCB_Top_2.jpg.html)
PCB sandwich, top
\- 
[![\1](../../assets/hardware/general/\2)](./File:Peaktech_4390A_Metex_M-3860M_-_PCB_Big_Top_Full.jpg.html)
Big PCB, top
\- 
[![\1](../../assets/hardware/general/\2)](./File:Peaktech_4390A_Metex_M-3860M_-_PCB_Big_Top_Detail.jpg.html)
Big PCB, top detail
\- 
[![\1](../../assets/hardware/general/\2)](./File:Peaktech_4390A_Metex_M-3860M_-_PCB_Small_Bottom.jpg.html)
Small PCB, bottom
\- 
[![\1](../../assets/hardware/general/\2)](./File:Peaktech_4390A_Metex_M-3860M_-_PCB_Small_Top.jpg.html)
Small PCB, top
\- 
[![\1](../../assets/hardware/general/\2)](./File:Peaktech_4390a_metex_m-3860m_power_adapter.jpg.html)
Power adapter
**RS232 cable:** \- 
[![\1](../../assets/hardware/general/\2)](./File:Peaktech_4390A_Metex_M-3860M_-_Serial_Cable.jpg.html)
Serial cable
See [Device_cables#Metex_5-pin_RS232_cable](Device_cables.html#Metex_5-pin_RS232_cable "Device cables") (Version 2). ## Protocol See [Multimeter_ICs#Metex_14-byte_ASCII](Multimeter_ICs.html#Metex_14-byte_ASCII "Multimeter ICs"). The device sends 4 \\* 14 bytes. The first 14 bytes represents the main display and then the three sub displays from left to right (left, middle, right). ## Resources \- [Conrad: Metex M-3860M manual](http://www2.produktinfo.conrad.de/datenblaetter/100000-124999/121371-an-01-en-Digitalmultimeter_M_3860_M.pdf)
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=PeakTech_4390A&oldid=12856](https://OpenTraceLab.org/w/index.php?title=PeakTech_4390A&oldid=12856)" 
[Categories](specialcategories-specialcategories.md): \- [Device](./Category:Device.html "Category:Device") \- [Multimeter](./Category:Multimeter.html "Category:Multimeter") \- [Supported](./Category:Supported.html "Category:Supported")

## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
