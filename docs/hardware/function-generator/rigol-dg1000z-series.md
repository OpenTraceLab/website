# Rigol Dg1000Z Series

| | | |:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------------:| | [![\1](../../assets/hardware/general/\2)](./File:Dg1000z_series.png.html) | | | Status | supported | | Source code | [rigol-dg](http://github.com/OpenTraceLab/?p=OpenTraceCapture.git;a=tree;f=src/hardware/rigol-dg) | | Frequency (sine) | 25-60MHz | | Frequency (square) | 25MHz | | Frequency (other) | 15-25MHz (pulse), 500-1000KHz (ramp) | | Frequency (user) | 10-20MHz | | Waveforms | sine, square, ramp, pulse, harmonic, noise, arbitrary waveform | | Waveform memory | 2-8Mpts (16Mpts option) | | Modulation | AM, FM, PM, DSB-AM, FSK, ASK, PWM | | Connectivity | USBTMC, LAN | | Website | [rigolna.com](https://www.rigolna.com/products/waveform-generators/dg1000z/) | **Rigol DG1000z Series** Rigol DG1000Z Series Arbitrary Waveform Generators are 2 channel, 25-60MHz signal generators with up to 16Mpts waveform memory. 
## Contents 
\- [1 Devices](Rigol_DG1000z_Series.html#Devices) \- [2 Hardware](Rigol_DG1000z_Series.html#Hardware) \- [3 Photos](Rigol_DG1000z_Series.html#Photos) \- [4 Protocol](Rigol_DG1000z_Series.html#Protocol) \- [5 Example use](Rigol_DG1000z_Series.html#Example_use) \- [6 Resources](Rigol_DG1000z_Series.html#Resources) 
## Devices Hardware on all these models is identical, only difference is in software/firmware. | | | | | | | |---------|----------|----------------------|------------------------|---------------------------|-------------------| | Model | Channels | Max Frequency (Sine) | Max Frequency (Square) | Arbitrary Waveform Length | Frequency Counter | | DG1022Z | 2 | 25 MHz | 25 MHz | 2 Mpts \\* | Y | | DG1032Z | 2 | 30 MHz | 25 MHz | 8 Mpts \\* | Y | | DG1062Z | 2 | 60 MHz | 25 MHz | 8 Mpts \\* | Y | \- ) 16 Mpts waveform memory is (software) option. ## Hardware **Digital**: TODO **Analog**: TODO ## Photos \- 
[![\1](../../assets/hardware/general/\2)](./File:Dg1000z_series.png.html)
Front Panel
\- 
[![\1](../../assets/hardware/general/\2)](./File:Dg1022z-01.jpeg.html)
Main PCB
\- 
[![\1](../../assets/hardware/general/\2)](./File:Dg1022z-02.jpeg.html)
Main PCB: front
\- 
[![\1](../../assets/hardware/general/\2)](./File:Dg1022z-03.jpeg.html)
Main PCB: front connectors
\- 
[![\1](../../assets/hardware/general/\2)](./File:Dg1022z-04.jpeg.html)
Main PCB: CPU
\- 
[![\1](../../assets/hardware/general/\2)](./File:Dg1022z-05.jpeg.html)
Main PCB: rear connectors
\- 
[![\1](../../assets/hardware/general/\2)](./File:Dg1022z-fan.jpeg.html)
Case Fan
## Protocol TODO ## Example use Depending on your type of connection you have to can either use the [USBTMC connection parameter](Connection_parameters.html#USBTMC "Connection parameters") or the [TCP/IP connection parameter](Connection_parameters.html#TCP_RAW "Connection parameters"). Examples: -d rigol-dg (usually no parameters are needed when connecting via USB) When connecting over TCP/IP need to specify ip address and port: -d rigol-dg:conn=tcp-raw/192.168.42.42/5555 Check the capabilities of the meter's driver, and current state of settings: $ OpenTraceCLI -d rigol-dg --show Check the capabilities specific to a channel (1 or 2): $ OpenTraceCLI -d rigol-dg -g 1 --show Enable or disable channel output (first channel): $ OpenTraceCLI -d rigol-dg -g 1 --set --config enabled=true $ OpenTraceCLI -d rigol-dg -g 1 --set --config enabled=false Get or set the waveform function (second channel): $ OpenTraceCLI -d rigol-dg -g 2 --get pattern $ OpenTraceCLI -d rigol-dg -g 2 --set --config pattern=square Get or set the output signal frequency: $ OpenTraceCLI -d rigol-dg -g 1 --get output_frequency $ OpenTraceCLI -d rigol-dg -g 1 --set --config output_frequency=20000 Get or set the output signal amplitude: $ OpenTraceCLI -d rigol-dg -g 1 --get amplitude $ OpenTraceCLI -d rigol-dg -g 1 --set --config amplitude=3.3 Get or set the output signal offset: $ OpenTraceCLI -d rigol-dg -g 1 --get offset $ OpenTraceCLI -d rigol-dg -g 1 --set --config offset=1.0 Get or set the output signal phase: $ OpenTraceCLI -d rigol-dg -g 1 --get phase $ OpenTraceCLI -d rigol-dg -g 1 --set --config phase=90.0 Get or set the output signal duty cycle: $ OpenTraceCLI -d rigol-dg -g 1 --get output_duty_cycle $ OpenTraceCLI -d rigol-dg -g 1 --set --config output_duty_cycle=25.0 Acquire measurement data (frequency counter output): $ OpenTraceCLI -d rigol-dg --continuous $ OpenTraceCLI -d rigol-dg --time 10s $ OpenTraceCLI -d rigol-dg --samples 10 ## Resources \- [DG1000Z Datasheet](http://beyondmeasure.rigoltech.com/acton/attachment/1579/f-033c/0/-/-/-/-/file.pdf) \- [DG1000Z Specifications](http://beyondmeasure.rigoltech.com/acton/attachment/1579/f-044f/0/-/-/-/-/file.pdf) \- [DG1000Z User's Guide](http://beyondmeasure.rigoltech.com/acton/attachment/1579/f-0450/0/-/-/-/-/file.pdf) \- [DG100Z Programming Guide](http://beyondmeasure.rigoltech.com/acton/attachment/1579/f-0493/1/-/-/-/-/DG1000Z%20Programming%20Guide.pdf)
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=Rigol_DG1000z_Series&oldid=16245](https://OpenTraceLab.org/w/index.php?title=Rigol_DG1000z_Series&oldid=16245)" 
[Categories](specialcategories-specialcategories.md): \- [Device](./Category:Device.html "Category:Device") \- [Signal generator](./Category:Signal_generator.html "Category:Signal generator") \- [Supported](./Category:Supported.html "Category:Supported")

## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
