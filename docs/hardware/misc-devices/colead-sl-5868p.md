# Colead Sl 5868P

| | | |:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:| | [![\1](../../assets/hardware/general/\2)](./File:Colead_SL-5868P.png.html) | | | Status | supported | | Source code | [colead-slm](http://github.com/OpenTraceLab/?p=OpenTraceCapture.git;a=tree;f=src/hardware/colead-slm) | | Connectivity | [RS232](Device_cables.html#Colead_SL-5868P_cables "Device cables") | | Frequency range | 31.5Hz - 8kHz | | Measurement range (A) | 30dB - 130dB | | Resolution | 0.1dB | | Accuracy (94dB@1kHz) | 1dB | | Frequency weighting | A, C, Flat | | Time weighting | F, S | | Standards | IEC 651 Type 2, ANSI 1.4 Type 2 | | Website | [coleadmeter.com](http://www.coleadmeter.com/view3.asp?goodsname=Multifunctional%20Sound%20Level%20Meter%20SL-5868P&id2=226) | **Colead SL-5868P** The **Colead SL5868P** is a sound level meter with RS232 connectivity. It has live (Lp), equivalent continuous (Leq), and threshold-based (Ln) measurement modes. It can also trigger alarm conditions based on a configured level, and drive a relay accordingly. It is rebranded under many names, but appears to generally have the SL-5868P model designation. It's available for under \$100. 
## Contents 
\- [1 Hardware](Colead_SL-5868P.html#Hardware) \- [2 Photos](Colead_SL-5868P.html#Photos) \- [3 Protocol](Colead_SL-5868P.html#Protocol) \- [3.1 Commands](Colead_SL-5868P.html#Commands) \- [3.2 Data structure](Colead_SL-5868P.html#Data_structure) 
## Hardware \- [Nuvoton W78E052D](http://www.nuvoton.com/NuvotonMOSS/Community/ProductInfo.aspx?tp_GUID=4119224f-5a2b-4861-a2aa-4e7895c6a532) 8-bit microcontroller \- [Holtek HT1621B](http://www.holtek.com/english/docum/consumer/1621.htm) LCD driver \- 6MHz clock ## Photos \- 
[![\1](../../assets/hardware/general/\2)](./File:Colead_SL-5868P.jpg.html)
Device, front
\- 
[![\1](../../assets/hardware/general/\2)](./File:Colead_SL-5868P_back.jpg.html)
Device, back
\- 
[![\1](../../assets/hardware/general/\2)](./File:Colead_SL-5868P_side.jpg.html)
Device, side
\- 
[![\1](../../assets/hardware/general/\2)](./File:Colead_SL-5868P_PCB_front.jpg.html)
PCB, front
\- 
[![\1](../../assets/hardware/general/\2)](./File:Colead_SL-5868P_PCB_back.jpg.html)
PCB, back
\- 
[![\1](../../assets/hardware/general/\2)](./File:Colead_SL-5868P_PCB_detail_1.jpg.html)
Detail 1
\- 
[![\1](../../assets/hardware/general/\2)](./File:Colead_SL-5868P_PCB_detail_2.jpg.html)
Detail 2
\- 
[![\1](../../assets/hardware/general/\2)](./File:Colead_SL-5868P_PCB_unmarked.jpg.html)
Unmarked chip
## Protocol The serial port is set to 2400bps, 8 bits, no parity, 1 stop bit (2400/8n1). The meter sends two measurements per second. When a new measurement is ready, the device sends `0x10`. The PC responds with `0x20`, which causes the device to transmit a 10-byte structure containing configuration and measurement. When the user presses the `Read` key on the keypad, the device sends all its stored measurements out via the serial port. This is preceded by two bogus measurement records as a marker, where all the digits are set to `0x0a` and byte 2 contains `0x09` in the first record, and `0x08` in the second record. The stored measurement records then follow; the entire sequence is typically repeated twice, including the marker. When the user switches back to live measurement mode, another two bogus measurement records are sent. To mark the return to live mode, the second bogus record this time contains `0x07`. All following records are then live. ### Commands | | | | |----------|---------------|-------------------| | Command | Direction | Description | | **0x10** | Device -\> PC | Measurement ready | | **0x20** | PC -\> Device | Send measurement | ### Data structure | | | | |------|-------|-----------------------------------------------------------------------------------------------------------------------| | Byte | Value | Description | | 0 | | *Always 0x08* | | 1 | | *Always 0x04* | | 2 | | **Configuration. The low nibble has the following meaning:** | | | 0000 | Lp, Weighting A, Fast | | | 0001 | Lp, Weighting A, Slow | | | 0010 | Lp, Weighting C, Fast | | | 0011 | Lp, Weighting C, Slow | | | 0100 | Lp, Flat, Fast | | | 0101 | Lp, Flat, Slow | | | 0110 | Ln, Weighting A, Fast | | | 0111 | Ln, Weighting A, Slow | | | 1000 | Leq, Weighting A, Fast (10-second mean) | | | 1001 | Leq, Weighting A, Fast (mean over minutes) | | | 1010 | Leq, Weighting A, Slow (10-second mean) | | | 1011 | Leq, Weighting A, Slow (mean over minutes) | | | 1100 | Internal calibration mode, Fast | | | 1101 | Internal calibration mode, Slow | | | 1110 | *Unused* | | | 1111 | *Unused* | | | | **The high nibble has the following meaning:** | | | 0001 | Normal measurement | | | 0010 | Max hold mode | | 3-7 | | **BCD-encoded value, one byte per digit 0x00-0x09. 0x0a means ignored digit. The last digit represents the decimal.** | | 8 | | **Measurement status** | | | 0 | Invalid | | | 1 | Valid | | 9 | | **Checksum: sum of bytes 0-8** | 
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=Colead_SL-5868P&oldid=6617](https://OpenTraceLab.org/w/index.php?title=Colead_SL-5868P&oldid=6617)" 
[Categories](specialcategories-specialcategories.md): \- [Device](./Category:Device.html "Category:Device") \- [Sound level meter](./Category:Sound_level_meter.html "Category:Sound level meter") \- [Supported](./Category:Supported.html "Category:Supported")

## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
