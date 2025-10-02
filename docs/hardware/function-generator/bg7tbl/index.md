---
title: BG7TBL
---

# BG7TBL

<div class="infobox" markdown>

![BG7TBL](./img/BG7TBL_pcb_bot.jpg){ .infobox-image }

### BG7TBL

| | |
|---|---|
| **Status** | planned |
| **Frequency (user)** | 138MHz-4.4GHz |
| **Waveforms** | sine (fixed) |
| **Amplitude** | ? V |
| **Connectivity** | USB |

</div>

The BG7TBL USB RF Signal Generator is a PC-based function generator. It has no external controls, requiring a USB connection to a computer.

Software to run this hardware can be found here [http://www.dl4jal.eu/](http://www.dl4jal.eu/).

This device can be bought on ebay for ca $65. Search for "138MHz-4.4GHz". There is a version with the ADF4351 instead that will give you more range (35MHz-4.4GHz).

## Hardware
- Microcontroller: [Atmel Atmega 8L](http://www.atmel.com/Images/Atmel-2486-8-bit-AVR-microcontroller-ATmega8_L_datasheet.pdf)
- Wideband Synthesizer: [ADF4350](http://www.analog.com/media/en/technical-documentation/data-sheets/ADF4350.pdf)
- USB to Serial: [FTDI FT232RL](http://www.ftdichip.com/Support/Documents/DataSheets/ICs/DS_FT232R.pdf)
- Logarithmic Amplifier [AD8307](http://www.analog.com/media/en/technical-documentation/data-sheets/AD8307.pdf)
- Mixer: [IAM 81008](http://www.qsl.net/n9zia/omnitracs/IAM81008.pdf)
- LDO: [AMS1117](http://www.advanced-monolithic.com/pdf/ds1117.pdf)

## Photos

<div class="photo-grid" markdown>

[![Bg7tbl Pcb Bot](./img/BG7TBL_pcb_bot.jpg)](./img/BG7TBL_pcb_bot.jpg "Bg7tbl Pcb Bot"){ .glightbox data-gallery="bg7tbl" }
<span class="caption">Bg7tbl Pcb Bot</span>

[![Bg7tbl Pcb Top](./img/BG7TBL_pcb_top.jpg)](./img/BG7TBL_pcb_top.jpg "Bg7tbl Pcb Top"){ .glightbox data-gallery="bg7tbl" }
<span class="caption">Bg7tbl Pcb Top</span>

[![Bg7tbl Case](./img/BG7TBL_case.jpg)](./img/BG7TBL_case.jpg "Bg7tbl Case"){ .glightbox data-gallery="bg7tbl" }
<span class="caption">Bg7tbl Case</span>

</div>
## Protocol

Baud 57600, 8n1

The protocol is binary serial based.

### Query firmware
- Send 0x8f+"v"

The answer should be in hex:

- 77

Where the returned byte is the firmware version, 0x77 = 119 = 'w'.

```
#!/usr/bin/python                             

import serial

ser = serial.Serial('/dev/ttyUSB0', 57600, timeout=1) # Linux first FTDI
ser.write("\x8f" + "v")
print("version is " + ser.read())

```
### Signal generator
#### Setting frequency

To set a frequency send:

- 0x8f

Then f and then the frequency divided by 10 with leading zeroes. For example this is the payload for 400MHz.

- 400 000 000 / 10
- f040000000
```
#!/usr/bin/python
import sys, serial

ser = serial.Serial('/dev/ttyUSB0', 57600, timeout=1) # Linux first FTDI
# sys.argv[1] is frequency in Herz
cmd = "\x8f" + "f" + '{:09d}'.format(int(sys.argv[1])/10)
ser.write(cmd)

```
### Spectrum analyzer

The protocol is briefly described in the source code here:

[https://github.com/DoYouKnow/BG7TBL_Reader](https://github.com/DoYouKnow/BG7TBL_Reader)

Here is a minimal code for an 'x' sweep (the protocol is described in chapter 6 of [http://www.dl4jal.eu/LinNWT_doc_en.pdf](http://www.dl4jal.eu/LinNWT_doc_en.pdf) ).  The device sends back the expected number of bytes but it seems I have to divide the frequency by 10... (?).

```
#!/usr/bin/python
import sys, serial, struct

start_frequency = 100000000    # FM band
increment       = 20000
steps           = 2000
#
# 'x' sweep (writing the command returns (4 * steps) bytes (what is it, I don't know)
#
cmd = "\x8f" + "x" + '{:09d}{:08d}{:04d}'.format(start_frequency/10, increment, steps)
ser = serial.Serial('/dev/ttyUSB0', 57600, timeout=100) # Linux first FTDI
ser.write(cmd)
rsp = ser.read(4 * steps)
if len(rsp) < (4 * steps):
	sys.stderr.write("Warning&#160;: Did not read enough measures! Try increasing the timeout\n")
	steps = len(rsp)/4    # adapt to the number of measures read
val_tab = struct.unpack_from("<" + "h"*2*steps, rsp) # 2 * steps 'little endian shorts'
for i in range(0, steps):
	print(val_tab[2*i])	# channel A (A and B are interleaved)

```

