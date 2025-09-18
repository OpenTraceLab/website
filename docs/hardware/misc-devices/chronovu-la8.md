# Chronovu La8

| | | |:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------------------:| | [![\1](../../assets/hardware/general/\2)](./File:Chronovu_la8_front.png.html) | | | Status | supported | | Source code | [chronovu-la](http://github.com/OpenTraceLab/?p=OpenTraceCapture.git;a=tree;f=src/hardware/chronovu-la) | | Channels | 8 | | Samplerate | 100MHz | | Samplerate (state) | — | | Triggers | high, low, dont-care | | Min/max voltage | -0.5 — 5V | | Threshold voltage | Fixed: VIH=2V—5V, VIL=0V—0.8V | | Memory | 8Mbyte (SDRAM) | | Compression | none | | Website | [chronovu.com](http://www.chronovu.com/) | **ChronoVu LA8** The **ChronoVu LA8** is a USB-based 8-channel logic analyzer with up to 100MHz sampling rate. See [ChronoVu LA16](ChronoVu_LA16.html "ChronoVu LA16") for the 16 channel version. It features a Xilinx CPLD for sampling, 8MByte of built-in SDRAM to store the samples, and can trigger on low or high states of any combination of probes. After the 8MByte sample buffer is full, the data is transferred to the host via an FTDI FT245RL chip. See [ChronoVu LA8/Info](ChronoVu_LA8/Info.html "ChronoVu LA8/Info") for more details (such as **lsusb -v** output) about the device. *Many thanks to the vendor ([ChronoVu](http://www.chronovu.com/)) for freely providing information on the protocol used to communicate with the device. This helped us implement the OpenTraceCapture hardware driver more quickly. We're happy to see more open-source friendly vendors support OpenTraceLab!* 
## Contents 
\- [1 Hardware](ChronoVu_LA8.html#Hardware) \- [2 Photos](ChronoVu_LA8.html#Photos) \- [3 Usage](ChronoVu_LA8.html#Usage) \- [4 Protocol](ChronoVu_LA8.html#Protocol) \- [4.1 Starting an acquisition](ChronoVu_LA8.html#Starting_an_acquisition) \- [4.2 Demangling data](ChronoVu_LA8.html#Demangling_data) \- [4.3 Stopping an acquisition](ChronoVu_LA8.html#Stopping_an_acquisition) \- [4.4 Triggers](ChronoVu_LA8.html#Triggers) \- [4.5 Sampling](ChronoVu_LA8.html#Sampling) \- [5 TODO](ChronoVu_LA8.html#TODO) \- [6 Resources](ChronoVu_LA8.html#Resources) 
## Hardware \- Xilinx XC2C256 CoolRunner-II CPLD \- Micron MT48LC4M16A2 SDRAM (8 MByte) \- FTDI FT245RL \- Level shifter: [Texas Instruments SN74LVTH244A](http://www.ti.com/product/sn74lvth244a), marking: LXH244A, [datasheet](http://www.ti.com/lit/gpn/sn74lvth244a) \- PT70151 ## Photos \- 
[![\1](../../assets/hardware/general/\2)](./File:Chronovu_la8_device.jpg.html)
Device with probes
\- 
[![\1](../../assets/hardware/general/\2)](./File:Chronovu_la8_front.jpg.html)
Device, front
\- 
[![\1](../../assets/hardware/general/\2)](./File:Chronovu_la8_back.jpg.html)
Device, back
\- 
[![\1](../../assets/hardware/general/\2)](./File:Chronovu_la8_usb.jpg.html)
USB and LEDs
\- 
[![\1](../../assets/hardware/general/\2)](./File:Chronovu_la8_probes.jpg.html)
Probe connector
\- 
[![\1](../../assets/hardware/general/\2)](./File:Chronovu_la8_pcb_front.jpg.html)
PCB, front
\- 
[![\1](../../assets/hardware/general/\2)](./File:Chronovu_la8_pcb_back.jpg.html)
PCB, back
\- 
[![\1](../../assets/hardware/general/\2)](./File:Chronovu_la8_xilinx.jpg.html)
Xilinx CPLD
\- 
[![\1](../../assets/hardware/general/\2)](./File:Chronovu_la8_sdram_mt48lc4m16a2.jpg.html)
SDRAM chip
\- 
[![\1](../../assets/hardware/general/\2)](./File:Chronovu_la8_ftdi_ft245rl.jpg.html)
FTDI chip
\- 
[![\1](../../assets/hardware/general/\2)](./File:Chronovu_la8_lxh244a.jpg.html)
LXH244A
\- 
[![\1](../../assets/hardware/general/\2)](./File:Chronovu_la8_pt70151.jpg.html)
PT70151
\- 
[![\1](../../assets/hardware/general/\2)](./File:Chronovu_la8_wires.jpg.html)
Custom wire
See also [this flickr set](http://www.flickr.com/photos/uwehermann/sets/72157626537516956/) for more photos of the device. ## Usage The default samplerate is 100MHz (which results in a sampling time of 0.084s). In order to get 8MB of samples (max.) at 100MHz in binary format use: $ OpenTraceCLI --driver chronovu-la8 --output-format binary --output-file samples.dat \ \--samples 8m To select another sampling rate use this syntax: $ OpenTraceCLI --driver chronovu-la8 --config samplerate=1mhz \ \--output-format binary --output-file samples.dat --samples 8m In order to save the data in the file format which the ChronoVu LA8 software can read (usually using the **.kdt** file extension): $ OpenTraceCLI --driver chronovu-la8 --config samplerate=1mhz \ \--output-format chronovu-la8 --output-file samples.kdt --samples 8m ## Protocol The ChronoVu LA8 is a USB-based device and presents itself as an FTDI device with vendor ID / device ID of **0403:6001** (see also [the full lsusb](ChronoVu_LA8/Info.html "ChronoVu LA8/Info")). Newer versions of the device use the VID/PID **0403:8867**. Talking to the device is thus done using libftdi's **ftdi_read()** and **ftdi_write()** functions. ### Starting an acquisition The data acquisition is started by sending 4 specific bytes to the device via **ftdi_write()**. This configures the sampling and trigger setup and initiates the acquisition. | | | | |------|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | Byte | Value | Comment | | 0 | divcount | This byte must contain the **divcount** value which determines the samplerate/sampletime/sampleperiod (see below). | | 1 | 0xff | This byte must always be 0xff. | | 2 | Trigger pattern | This byte contains the **trigger pattern** (MSB = channel 7, LSB = channel 0). A 1 bit matches a high signal, 0 matches a low signal on a probe. Only low/high triggers (but not e.g. rising/falling) are supported. | | 3 | Trigger mask | This byte contains the **trigger mask** (MSB = channel 7, LSB = channel 0). A 1 bit means "must match trigger pattern", 0 means "don't care". | After these bytes have been sent you need to wait a certain minimal amount of time, then grab the 8MByte buffer data from the LA8 using **ftdi_read()**. ### Demangling data However, the data received from the device is not directly usable as it is "mangled" a bit due to internal hardware reasons. So it's required to de-mangle the data first, in order to get it into the final format, i.e., one byte per sample, MSB is the value of channel 7, LSB is the value of channel 0. ### Stopping an acquisition TODO ### Triggers TODO ### Sampling The device has an 8MByte buffer (SDRAM) which is always filled completely with samples. Using the **divcount** divider value (valid range: 0x00 - 0xfe) samplerates between 100MHz and 392.15kHz can be selected. Depending on the samplerate different total sampling times (from 0.084s up to 21.391s) can be achieved. The formula for the sample period (not to be confused with the samplerate) is: sample period = (divcount + 1) * 10ns The following table shows a small part of the valid divcount values and resulting sample periods, samplerates, and sampling times. | | | | | |---------|---------------|------------|---------------| | Divider | Sample period | Samplerate | Sampling time | | 0x00 | 10ns | 100MHz | 0.084s | | 0x01 | 20ns | 50MHz | 0.168s | | ... | ... | ... | ... | | 0xfd | 2540ns | 393.7kHz | 21.307s | | 0xfe | 2550ns | 392.156kHz | 21.391s | ## TODO \- Test trigger support, might work already. \- Finish input and output file format support for the ChronoVu LA8 software for interoperability. \- Trigger support and some smaller fixes are pending. \- For sampling of less than 8MByte of data, padding is needed. \- For less than 8 probes, padding is needed too. \- Implement --time support, currently only --samples works correctly. \- Check if the 8MByte 'final_buf' buffer can be replaced by a static 4kB buffer (if data is sent in 4kB chunks). ## Resources \- [Manual](http://www.chronovu.com/downloads/ReadMeFile%20LA8-4.00.pdf) \- [Vendor FAQ](http://www.chronovu.com/help/docs/faq/) \- [Vendor software](http://www.chronovu.com/download/)
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=ChronoVu_LA8&oldid=13498](https://OpenTraceLab.org/w/index.php?title=ChronoVu_LA8&oldid=13498)" 
[Categories](specialcategories-specialcategories.md): \- [Device](./Category:Device.html "Category:Device") \- [Logic analyzer](./Category:Logic_analyzer.html "Category:Logic analyzer") \- [Supported](./Category:Supported.html "Category:Supported")

## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
