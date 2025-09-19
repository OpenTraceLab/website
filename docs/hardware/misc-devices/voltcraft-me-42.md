# Voltcraft Me 42
| | | |:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------:| | [*Image: \1* | | | Status | supported | | Source code | [serial-dmm](http://github.com/OpenTraceLab/?p=OpenTraceCapture.git;a=tree;f=src/hardware/serial-dmm) | | Counts | 4000 | | IEC 61010-1 | CAT II (750 V AC/1000 V DC) | | Connectivity | RS-232 (DB9) | | Measurements | voltage, current, resistance, diode, continuity | | Features | autorange, hold, bargraph | | Website | [conrad.de](http://www.conrad.de/ce/de/product/123294/VOLTCRAFT-VC820-DMM/SHOP_AREA_17622&promotionareaSearchDetail=005) | **Voltcraft ME-42** The **Voltcraft ME-42** is a 4000 counts, CAT II (750/1000V) handheld digital multimeter with RS232 connectivity. It is an OEM version of the Metex ME-42. The device was sold by *Conrad Elektronik* as article 120130 starting from 1999 and is not available any more.
## Contents
\- *1 Hardware* \- *2 Photos* \- *3 Protocol* \- *4 Model family* \- *5 Resources* \- *6 Measurement functions and ranges*
## Hardware **Multimeter**: \- TODO  \- **Fuses**: 800mA/250V 5x20mm and 15A/250V 6x30mm (superfast, ceramic fuses) \- **Battery**: 9V NEDA 1604 or 6F22 \- One [source](http://mysite.verizon.net/tomhunter/experime/meter.htm) reported a very low battery life. **RS232 cable:** \- Standard RS-232 cable with DB9 (M) plug. \- During tests run by *Matthias*, this device did not work with several *USB to serial converters* (tested MosChip, Prolific, FTDI chipsets), only on a real "RS-232" port. ## Photos **Multimeter**: \-
[*Image: \1*
Front
\-
[*Image: \1*
Back
\-
[*Image: \1*
Inside, with shielding
\-
[*Image: \1*
Back of board, without shielding
\-
[*Image: \1*
Board and power button removed
\-
[*Image: \1*
RS-232 interface and cover
## Protocol See *Multimeter_ICs#Metex_14-byte_ASCII* for the DMM IC protocol. ## Model family It seems that this device belongs to a family of several similiar devices and OEM models.  Metex | Conrad | PeakTech | Radio Shack | RMS | Frequency | Transistor | Logic | Temp | Cap. | Remarks
---|---|---|---|---|---|---|---|---|---|---
Metex ME-11 | - | ? | *RadioShack 22-805* | ? | ? | ? | ? | ? | ? | Amps manual range; seems to be similiar to ME-42
*Metex ME-21* | - | ? | ? | - | ● | - | ● | - | - | Manual Range
Metex ME-22 | Voltcraft ME-22 | ? | ? | ? | ● | ● | ● | ● | ? | Manual Range
Metex ME-22 RMS | Voltcraft ME-22 RMS | ? | ? | ● | ● | ● | ● | ● | ? | Manual Range
*Metex ME-31* | - | *PeakTech 3410* | ? | ? | ? | ● | ? | ● | ? |
Metex ME-32 | Voltcraft ME-32 | ? | ? | - | - | ● | - | ● | ● | Amps manual range
Metex ME-42 | **Voltcraft ME-42** | ? | ? | - | - | - | - | - | - | Amps manual range
## Resources \- [Manual DE, single pages](http://www.produktinfo.conrad.com/datenblaetter/100000-124999/120130-an-01-de-Digitalmultimeter_ME_42.pdf) \- [Manual DE/GB/F/NL](http://www.produktinfo.conrad.com/datenblaetter/100000-124999/120130-an-01-ml-Digitalmultimeter_ME_42_de_en_fr_nl.pdf) ## Measurement functions and ranges | | | | | | | |----------------------|----------|------------|-------------|--------------------------------|-------------------------| | Measurement function | Range | Resolution | Accuracy | OpenTraceLab result | Remarks | | V= | 400.0 mV | 100 μV | ±(0.5% + 3) | mq V, unit V, mqflags DC | " | | | 4.000 V | 1 mV | | " | | | | 40.00 V | 10 mV | | " | | | | 400.0 V | 100 mV | | " | | | | 1000 V | 1 V | | " | | | V≈ | 400.0 mV | 100 μV | ±(1.0% + 5) | mq V, unit V, mqflags AC | 40 Hz - 100 Hz | | | 4.000 V | 1 mV | | " | 40 Hz - 400 Hz | | | 40.00 V | 10 mV | | " | " | | | 400.0 V | 100 mV | | " | " | | | 750 V | 1 V | | " | " | | A= | 4.000 mA | 1 µA | ±(0.8% + 3) | mq Curr., unit A, mqflags DC | | | | 400.0 mA | 100 µA | ±(1.2% + 3) | " | | | | 20.00 A | 10 mA | ±(2.0% + 5) | " | | | A≈ | 4.000 mA | 10 µA | ±(1.0% + 5) | mq Curr., unit A, mqflags AC | | | | 400.0 mA | 100 µA | ±(1.5% + 5) | " | | | | 20.00 A | 10 mA | ±(3.0% + 5) | " | | | Ω | 400.0 Ω | 100 mΩ | | mq Res., unit Ω, mqflags - | Continuity beep \< 50 Ω | | | 4.000 kΩ | 1 Ω | | " | | | | 40.00 kΩ | 10 Ω | | " | | | | 400.0 kΩ | 100 Ω | | " | | | | 4.000 MΩ | 1 kΩ | | " | | | | 40.00 MΩ | 10 kΩ | | " | | | Diode | 2.000 V– | 1 mV | | mq V, unit V, mqflags DC,DIODE | Max. 1.5 mA | | Data Hold | | | | \\- | | The column "OpenTraceLab result" contains in short form what the driver generates for the resp. data type. The device seems to be extremely slow when the RS-232 interface is enabled and often takes up to about 10 seconds to detect a changed value or switch to another range. During this time a previous value keeps being sent. When changing to a new range automatically or manually, the device might send the old value scaled to the new range for a short time. This behaviour is caused by the device, not by OpenTraceLab! It improves slightly in manual range.
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=Voltcraft_ME-42&oldid=15063](https://OpenTraceLab.org/w/index.php?title=Voltcraft_ME-42&oldid=15063)"
: \- *Device* \- *Multimeter* \- *Supported*
## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
