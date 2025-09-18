# Rigol Ds2072

| | | |:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------------:| | [![\1](../../assets/hardware/general/\2)](./File:Rigol-ds2072_mugshot.png.html) | | | Status | supported | | Source code | [rigol-ds](http://github.com/OpenTraceLab/?p=OpenTraceCapture.git;a=tree;f=src/hardware/rigol-ds) | | Channels | 2 | | Samplerate | 2GSa/s (1ch), 1GSa/s (2ch) | | Analog bandwidth | 70MHz (upgradable up to 300 MHz) | | Vertical resolution | 8bits | | Triggers | edge, pulse, runt, windows, nth edge, slope, video, pattern, delay, timeout, duration, setup/hold, RS232/UART, I²C, SPI, CAN, USB | | Input impedance | 1MΩ‖16pF 300V RMS CAT I | | Memory | 56Mpts (mode/ch-dependent) | | Display | 8" 800x480, 160K colors | | Connectivity | USB host/device, ethernet, trigger out, pass/fail out | | Features | math: +, —, x, /, FFT, vertical sensitivity: 500µV/div - 10V/div | | Website | [rigolna.com](http://www.rigolna.com/products/digital-oscilloscopes/ds2000/ds2072/) | **Rigol DS2072** The [Rigol DS2072](http://www.rigolna.com/products/digital-oscilloscopes/ds2000/ds2072/) is a USB-based, 2-channel oscilloscope with an analog bandwidth of 70MHz and 2GS/s sampling rate. See [Rigol DS2072/Info](Rigol_DS2072/Info.html "Rigol DS2072/Info") for more details (such as **lsusb -v** output) about the device. See [Rigol DS2000 series](Rigol_DS2000_series.html "Rigol DS2000 series") for information common to all devices in this series. ## Photos \- 
[![\1](../../assets/hardware/general/\2)](./File:Rigol_DS2072_front.jpg.html)
Device, front
\- 
[![\1](../../assets/hardware/general/\2)](./File:Rigol_DS2072_back.jpg.html)
Device, back
\- 
[![\1](../../assets/hardware/general/\2)](./File:Rigol_DS2072_left.jpg.html)
Connectors on left side
\- 
[![\1](../../assets/hardware/general/\2)](./File:Rigol_DS2072_right.jpg.html)
Device, right side
\- 
[![\1](../../assets/hardware/general/\2)](./File:Rigol_DS2072_waveform.jpg.html)
Device showing a waveform
## Protocol Example of using SCPI over LAN: OpenTraceCLI -d rigol-ds:conn=tcp-raw/192.168.3.16/5555 -l 5 --scan OpenTraceCLI -d rigol-ds:conn=tcp-raw/192.168.3.16/5555 --frames 1 -O analog ## More Info
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=Rigol_DS2072&oldid=9902](https://OpenTraceLab.org/w/index.php?title=Rigol_DS2072&oldid=9902)" 
[Categories](specialcategories-specialcategories.md): \- [Device](./Category:Device.html "Category:Device") \- [Oscilloscope](./Category:Oscilloscope.html "Category:Oscilloscope") \- [Supported](./Category:Supported.html "Category:Supported")

## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
