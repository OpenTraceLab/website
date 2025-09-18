# Gossen Metrawatt Metrahit 18S

| | | |:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------------------------:| | [![\1](../../assets/hardware/general/\2)](./File:Gossen_Metrawatt_Metrahit_18S_small.png.html) | | | Status | supported | | Source code | [gmc-mh-1x-2x](http://github.com/OpenTraceLab/?p=OpenTraceCapture.git;a=tree;f=src/hardware/gmc-mh-1x-2x) | | Counts | 31000 | | IEC 61010-1 | CAT III 1000 V, CAT IV 600 V | | Connectivity | Infrared (RS232) | | Measurements | voltage, current, resistance, capacitance, temperature, diode, continuity | | Features | autorange, data hold, bargraph | **[Gossen Metrawatt](Gossen_Metrawatt.html "Gossen Metrawatt") Metrahit 18S** The **[Gossen Metrawatt](Gossen_Metrawatt.html "Gossen Metrawatt") Metrahit 18S** is a 31000 counts handheld digital multimeter with IR (RS232) connectivity. ## Hardware \- **Battery**: *9 V IEC 6 F 22* or *IEC 6 LR 61* or corresponding rechargeable battery \- **Fuse**: \- Current 300 mA: FF (UR) 1,6 A/500G; 6,3x32 mm \- Current 3A, 10A: \- Siba Ultrarapid 16A/600 V≈ 10mm x 38 mm \- Littlefuse KLK 15A/600 V≈ 13/32” / 1 1/2” \- Bussmann KLK 15A/600 V≈ 13/32” / 1 1/2”  \- TODO. ## Photos \- 
[![\1](../../assets/hardware/general/\2)](./File:Metrahit_18S_1.jpg.html)
Package
\- 
[![\1](../../assets/hardware/general/\2)](./File:Metrahit_18S_2.jpg.html)
Inside
\- 
[![\1](../../assets/hardware/general/\2)](./File:Metrahit_18S_4.jpg.html)
Display
\- 
[![\1](../../assets/hardware/general/\2)](./File:Metrahit_18S_3.jpg.html)
IR Interface
## Measurement functions and ranges Measurement function | Range | Resolution | Accuracy | OpenTraceLab result | Remarks  
---|---|---|---|---|---  
V= | 300 mV | 10 μV | ±(0.05% + 3) | mq V, unit V, mqflags DC | Input Impendance >10 GΩ  
3 V | 100 μV | ±(0.05% + 3) | " |   
30 V | 1 mV | " |   
300 V | 10 mV | " |   
1000 V | 100 mV | " |   
V≈ | 300 mV | 10 µV | ±(0.5% + 30) (> 500 Digit)) | mq V, unit V, mqflags AC,RMS |   
3 V | 100 μV | ±(0.5% + 30) (> 300 Digit) | " |   
30 V | 1 mV | " |   
300 V | 10 mV | " |   
1000 V | 100 mV | " |   
V≃ | 300 mV | 10 μV | ±(0.5% + 30) (> 500 Digit)) | mq V, unit V, mqflags AC,DC,RMS |   
3 V | 100 μV | ±(0.5% + 30) (> 300 Digit) | " |   
30 V | 1 mV | " |   
300 V | 10 mV | " |   
1000 V | 100 mV | " |   
V db≈ | -48 - 63 dB | 0.01 dB |  | mq V, unit V, mqflags AC,RMS | Actually 5 ranges.  
V db≈ rel | -48 - 63 dB | 0.01 dB |  | mq V, unit V, mqflags AC,RMS | Actually 5 ranges. To activate, press yellow button in dB mode, then do second measurement. Cannot be distinguished from non-rel measurement remotely.  
A= |  300.00 µA | 100 nA |  | mq Curr., unit A, mqflags DC |   
3.0000 mA | 1 µA |  | " |   
30.000 mA | 1 µA |  | " |   
300.00 mA | 10 µA |  | " |   
3.0000 A | 100 µA |  | " |   
10.000 A | 1 mA |  | " |   
A≃ |  300.00 µA | 100 nA |  | mq Curr., unit A, mqflags AC,DC,RMS |   
3.0000 mA | 1 µA |  | " |   
30.000 mA | 1 µA |  | " |   
300.00 mA | 10 µA |  | " |   
3.0000 A | 100 µA |  | " |   
10.000 A | 1 mA |  | " |   
Ω | 300.00 Ω | 10 mΩ |  | mq Res., unit Ω, mqflags - |   
3.0000 kΩ | 100 mΩ |  | " |   
30.000 kΩ | 1 Ω |  | " |   
300.00 kΩ | 10 Ω |  | " |   
3.0000 MΩ | 100 Ω |  | " |   
30.000 MΩ | 1 kΩ |  | " |   
Diode/Cont. | 3.0000 V– | 1 mV |  | mq V, unit V, mqflags DC,DIODE | Diode and cont. are identical on this device, just without beeper for diode.  
Cap. F | 3.000 nF | 1 pF |  | mq Cap., unit F, mqflags - |   
30.00 nF | 10 pF |  | " |   
300.0 nF | 100 pF |  | " |   
3.000 µF | 1 nF |  | " |   
30.00 µF | 10 nF |  | " |   
300.0 µF | 100 nF | ±(5.0% + 6) | " |   
3.000 mF | 1 µF | " |   
10.00 mF | 10 µF | " |   
Hz≃ | 300.00 Hz | 0.01 Hz | ±(0.1% + 3) | mq Freq., unit Hz, mqflags AC,DC |   
3.0000 kHz | 0.1 Hz | " |   
30.000 kHz | 1 Hz | " |   
100.000 kHz | 10 Hz | " |   
°C | Pt100 –200.0 - +100.0 °C | 0.1 °C | 2 Kelvin + 5 | mq Temp., unit °C, mqflags - |   
Pt100 +100.0 - +800.0 °C | ±(1.0% + 5) | " |   
Pt1000 –100.0 - +100.0 °C | 2 Kelvin + 5 | " |   
Pt1000 +100.0 - +800.0 °C | ±(1.0% + 5) | " |   
Event count |  |  |  | mq V, unit V, mqflags AC,RMS,REL | Counts events >= 2500 digits that last >=2s with a break >=2s. To activate, switch to voltage ACDC, press yellow button twice. Press up to 4 times to cycle parameters, press long to stop. See manual. Not useful remotely because the current measurement value is sent, not the counter.  
Stop Watch |  |  |  | (Time data) | To activate, select a 3V-1000V range manually, press yellow button, press AUTO for start/stop, DATA for reset. Delivers only invalid data ("Overflow") via IR on [ Matthias'](https://OpenTraceLab.org/wiki/User:Matthias_Heidbrink "User:Matthias Heidbrink") device.  
Data Hold |  |  |  | mqflags += HOLD | Disabled while IR interface is active on [ Matthias'](https://OpenTraceLab.org/wiki/User:Matthias_Heidbrink "User:Matthias Heidbrink") device.  
MIN |  |  |  | mqflags += MIN | Influences only display, via IR flag is set, but actual current value is delivered.  
MAX |  |  |  | mqflags += MAX | Influences only display, via IR flag is set, but actual current value is delivered.  
The column "OpenTraceLab result" contains in short form what the driver generates for the resp. data type. 
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=Gossen_Metrawatt_Metrahit_18S&oldid=11921](https://OpenTraceLab.org/w/index.php?title=Gossen_Metrawatt_Metrahit_18S&oldid=11921)" 
[Categories](specialcategories-specialcategories.md): \- [Device](./Category:Device.html "Category:Device") \- [Multimeter](./Category:Multimeter.html "Category:Multimeter") \- [Supported](./Category:Supported.html "Category:Supported")

## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
