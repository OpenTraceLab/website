# Gossen Metrawatt Metrahit X Tra

| | | |:-------------|--------------------------------------------------------------------------------------------------------------------------------| | Status | in progress | | Counts | 31000 | | IEC 61010-1 | CAT III 1000 V, CAT IV 600 V | | Connectivity | Infrared (USB) | | Measurements | voltage, current, resistance, capacitance, temperature, frequency, duty cycle, diode, continuity | | Features | autorange, data hold | | Website | [[1]](http://www.gossenmetrawatt.com/english/produkte/metrahitx-tra.htm) | **Gossen Metrawatt Metrahit X-Tra** The **[Gossen Metrawatt](Gossen_Metrawatt.html "Gossen Metrawatt") Metrahit X-Tra** is a 4.5 digit, 12000 counts 1000V CAT III/600 V CAT IV handheld digital multimeter with IR (USB) connectivity. ## Hardware \- **Power supply**: \- Battery: 2x *1,5 V IEC R 6*, *IEC LR 6* or corresponding NiCd rechargeable batteries \- **Fuse**: \- Current: FF (UR) 10 A/1000 V AC/DC (30 kA) 10 mm x 38 mm ## Using the device with OpenTraceLab The device is planned to be supported using a [USB X-Tra interface](Gossen_Metrawatt.html#USB_X-Tra "Gossen Metrawatt") or similar IR to USB interface. ## Measurement functions and ranges Measurement function | Range | Resolution | Accuracy | OpenTraceLab result | Remarks  
---|---|---|---|---|---  
V= | 100 mV | 10 μV | ±(0,09% 3) | mq V, unit V, mqflags DC | with ZERO  
1 V | 100 μV | ±(0,05% 3) |   
10 V | 1 mV | "  
100 V | 10 mV | "  
1000 V | 100 mV | "  
V≈ | 100 mV | 10 µV | ±(1% + 30) (> 300 Digit) | mq V, unit V, mqflags AC,RMS | min. 200 µV  
1 V | 100 μV | ±(0,5% + 30) (> 200 Digit) | " |   
10 V | 1 mV | " |   
100 V | 10 mV | " |   
1000 V | 100 mV | " |   
V≃ | 100 mV | 10 µV | ±(1% + 30) (> 300 Digit) | mq V, unit V, mqflags AC,DC,RMS | min. 200 µV  
1 V | 100 μV | " |   
10 V | 1 mV | " |   
100 V | 10 mV | " |   
1000 V | 100 mV | " |   
A= |  100.00 µA | 10 nA | 0,5% + 3 | mq Curr., unit A, mqflags DC |   
1.0000 mA | 100 nA | " |   
10.000 mA | 1 µA | " |   
100.00 mA | 10 µA | " |   
1.0000 A | 100 µA | 0,9% + 10 | " |   
10.000 A | 1 mA | " |   
A≃ |  100.00 µA | 10 nA | 1,5% + 10 | mq Curr., unit A, mqflags AC,RMS |   
3.0000 mA | 100 nA | " |   
30.000 mA | 1 µA | " |   
300.00 mA | 10 µA | " |   
3.0000 A | 100 µA | " |   
10.000 A | 1 mA | " |   
A≃ |  100.00 µA | 10 nA | 1,5% + 30 | mq Curr., unit A, mqflags AC,DC,RMS |   
3.0000 mA | 100 nA | " |   
30.000 mA | 1 µA | " |   
300.00 mA | 10 µA | " |   
3.0000 A | 100 µA | " |   
10.000 A | 1 mA | " |   
Ω | 100.00 Ω | 10 mΩ | 0,2% + 5 | mq Res., unit Ω, mqflags - |   
1.0000 kΩ | 100 mΩ | " |   
10.000 kΩ | 1 Ω | " |   
100.00 kΩ | 10 Ω | " |   
1.0000 MΩ | 100 Ω | " |   
10.000 MΩ | 1 kΩ | 0,5% + 10 | " |   
40.00 MΩ | 10 kΩ | 2% + 10 | " |   
Ohm/Cont. | 100 Ω | 100 mΩ | 3% + 3% | mq Res., unit Ω, mqflags - | max. 8 V/ca. 1 mA  
Diode | 5,1 V | 1 mV | 0.5% + 3 | mq V, unit V, mqflags DC,DIODE | max. 8 V/ca. 1 mA  
Cap. F | 10.00 nF | 10 pF | 1.0% + 6 | mq Cap., unit F, mqflags - |   
100.0 nF | 100 pF | " |   
1.000 µF | 1 nF | " |   
10.00 µF | 10 nF | " |   
100.0 µF | 100 nF | ±(5.0% + 6) | " |   
1000 µF | 1 µF | " |   
Hz (V) | 100.00 Hz | 0.01 Hz | ±(0.05% + 3) | mq Freq., unit Hz, mqflags AC,DC |   
100.00 kHz | 10 Hz | " |   
100.00 Hz -  
1.0000 MHz | 0.01 Hz - 100 Hz | " | 3 ranges; TTL voltage (5 V) only!  
Hz (A) | 1,0000 kHz | 0.1 Hz | mq Freq., unit Hz, mqflags AC,DC |   
30.00 kHz | 10 Hz | " |   
% | 2,0-98%  
100 Hz - 1 kHz | 0.01 % | ±(0,1%) | mq Duty., unit %, mqflags - |   
5,0-95%  
... - 10 kHz | ±(0,1% per kHz) | " |   
10-90%  
... - 100 kHz | " |   
°C/°F | Pt100  
–200.0 - +850.0 °C | 0.1 °C | ±(0,3% +15) | mq Temp., unit °C/°F, mqflags - | Multimeter switchable between °C and °F.  
Pt1000  
-150.0 - +850.0 °C | " |   
Type K  
-250 - +1372.0 °C | ±(1% + 5K) | " |   
The column *Accuracy* was simplified, see manual for exact specs. The column "OpenTraceLab result" contains in short form what the driver generates for the resp. data type. 
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=Gossen_Metrawatt_Metrahit_X-Tra&oldid=11629](https://OpenTraceLab.org/w/index.php?title=Gossen_Metrawatt_Metrahit_X-Tra&oldid=11629)" 
[Categories](specialcategories-specialcategories.md): \- [Device](./Category:Device.html "Category:Device") \- [Multimeter](./Category:Multimeter.html "Category:Multimeter") \- [Planned](./Category:Planned.html "Category:Planned")

## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
