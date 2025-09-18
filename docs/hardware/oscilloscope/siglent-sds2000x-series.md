# Siglent Sds2000X Series

| | | |:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------------------:| | [![\1](../../assets/hardware/general/\2)](./File:Sds2304x-mugshot.png.html) | | | Status | supported | | Source code | [siglent-sds](http://github.com/OpenTraceLab/?p=OpenTraceCapture.git;a=tree;f=src/hardware/siglent-sds) | | Channels | 2-4 analog, 16 digital | | Samplerate | up to 2GSa/s | | Analog bandwidth | 70-300MHz | | Vertical resolution | 8bits | | Triggers | edge, slope, pulse width, window, runt, interval, dropout, pattern, video, serial bus | | Input impedance | 1MΩ‖18pF 400Vp CAT I, 50Ω 5V RMS | | Memory | 140Mpts | | Display | 8" VGA (800x480) | | Connectivity | USB host/device, ethernet, pass/fail, trig out, GPIB (optional) | | Website | [siglent.com](http://www.siglent.com/ens/) | **Siglent SDS2000X series** The **Siglent SDS2000X series** of oscilloscopes supports samplerates of 2GSa/s, up to 4 analog channels with up to 300MHz bandwidth, and up to 16 logic channels with up to 500MSa/s. See [Siglent SDS2000X series/Info](Siglent_SDS2000X_series/Info.html "Siglent SDS2000X series/Info") for more details (such as **lsusb -v** output) about the device. 
## Contents 
\- [1 Hardware](Siglent_SDS2000X_series.html#Hardware) \- [2 Photos](Siglent_SDS2000X_series.html#Photos) \- [3 Protocol](Siglent_SDS2000X_series.html#Protocol) \- [4 Resources](Siglent_SDS2000X_series.html#Resources) 
## Hardware The Siglent SDS2000X series oscilloscopes are capable of sampling up to 2GSa/s 140 Mpts/CH memory for the analog channels. Due to the fact that the 2 channels are shared, if both channels are on the sampling is limited to 1GSa/s and 70 Mpts/CH memory per channel. This is also true with the 4 channel devices. The analog channels have history memory where 80000 frames are stored and can be viewed via the scopes History function. All devices have the logic analyzer and DDS arbitrary waveform generator built-in. Keep in mind that for the logic analyzer and waveform generator an extra software option must be purchased. For the logic analyzer an additional probe device (SPL2016) must also be purchased. The logic analyzer is capable 500 MSa/s with 140 Mpts/CH memory. The older series SDS2000X Logic Analyzer function does not support acquisition of the LA channels over VXI or USB. Due to flash memory program limitations the code for this function does not fit. Its not clear if newer "E" scopes will come functionality for the SDS2000 series scopes. An extra software option to decode serial protocols is also available on all devices. | | | | | |----------|-----------|-----------------|------------------| | Model | Bandwidth | Analog channels | Digital channels | | SDS2304X | 300MHz | 4 | 16 | | SDS2302X | 300MHz | 2 | 16 | | SDS2204X | 200MHz | 4 | 16 | | SDS2202X | 200MHz | 2 | 16 | | SDS2104X | 100MHz | 4 | 16 | | SDS2102X | 100MHz | 2 | 16 | | SDS2074X | 70MHz | 4 | 16 | | SDS2072X | 70MHz | 2 | 16 | ## Photos \- 
[![\1](../../assets/hardware/general/\2)](./File:Sds2304x-front.png.html)
SDS2304X, front view
\- 
[![\1](../../assets/hardware/general/\2)](./File:Sds2000x-connectors.png.html)
SDS2000X, rear connectors
\- 
[![\1](../../assets/hardware/general/\2)](./File:Sds2000x-analog-probe.png.html)
Analog probe (one per channel)
\- 
[![\1](../../assets/hardware/general/\2)](./File:Sds2000x-logic-probe-2.png.html)
Logic probes cable, PCIe to IDC, SPL2016
\- 
[![\1](../../assets/hardware/general/\2)](./File:Sds2000x-logic-probe-1.png.html)
Logic probes, IDC to cable ends, EZ-Hooks
\- 
[![\1](../../assets/hardware/general/\2)](./File:Sds2000x-logic-probe-3.png.html)
Logic probes, IDC boxes, colour codes, 2x GND per 8 channels
## Protocol All devices support USB (USBTMC) and LAN (VXI-11) by default, and are implementing the IEEE488.2 protocol. ## Resources \- [SDS2000X Series Oscilloscopes - Data Sheet](http://www.siglentamerica.com/USA_website_2014/Documents/DataSheet/SDS2000X_Datasheet_DS0102X-E01B.pdf) \- [SIGLENT_Digital Oscilloscopes Remote Control Manual](http://www.siglentamerica.com/USA_website_2014/Documents/Program_Material/SIGLENT_Digital_Oscilloscopes_Remote%20Control%20Manual.pdf)
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=Siglent_SDS2000X_series&oldid=13508](https://OpenTraceLab.org/w/index.php?title=Siglent_SDS2000X_series&oldid=13508)" 
[Categories](specialcategories-specialcategories.md): \- [Device](./Category:Device.html "Category:Device") \- [Logic analyzer](./Category:Logic_analyzer.html "Category:Logic analyzer") \- [Oscilloscope](./Category:Oscilloscope.html "Category:Oscilloscope") \- [Mixed-signal oscilloscope](./Category:Mixed-signal_oscilloscope.html "Category:Mixed-signal oscilloscope") \- [Supported](./Category:Supported.html "Category:Supported")

## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
