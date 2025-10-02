---
title: RockyLogic Ant18e
---

# RockyLogic Ant18e

<div class="infobox" markdown>

![RockyLogic Ant18e](./img/Ant18e-front2.jpg){ .infobox-image }

### RockyLogic Ant18e

| | |
|---|---|
| **Status** | planned |
| **Channels** | 18 |
| **Samplerate** | 1GHz |
| **Samplerate (state)** | 100MHz |
| **Triggers** | high, low, rising, falling, either, dont-care, counting, duration, multi-stage |
| **Min/max voltage** | 0.8V — 2.5V |
| **Memory** | 8K |
| **Compression** | ? |
| **Website** | [rockylogic.com](http://www.rockylogic.com/products/ant18e.html) |

</div>

The **RockyLogic Ant18e** is a USB-based, 18-channel logic analyzer with up to 1GHz sampling rate.

See [RockyLogic_Ant18e/Info](https://sigrok.org/wiki/RockyLogic_Ant18e/Info) for more details (such as **lsusb -vvv** output) about the device.

## Hardware
- Xilinx XC3S200 (FPGA)
- Xilinx XC9572XL (CPLD)
- FTDI FT245RL (USB FIFO device)
- IDT 501MLF (clock multiplier)
- 25MHz crystal

## Photos

<div class="photo-grid" markdown>

[![Ant18e Front2](./img/Ant18e-front2.jpg)](./img/Ant18e-front2.png "Ant18e Front2"){ .glightbox data-gallery="rockylogic-ant18e" }
<span class="caption">Ant18e Front2</span>

[![Ant18e Closed](./img/Ant18e_closed.jpg)](./img/Ant18e_closed.jpg "Ant18e Closed"){ .glightbox data-gallery="rockylogic-ant18e" }
<span class="caption">Ant18e Closed</span>

[![Ant18e Back2](./img/Ant18e-back2.jpg)](./img/Ant18e-back2.png "Ant18e Back2"){ .glightbox data-gallery="rockylogic-ant18e" }
<span class="caption">Ant18e Back2</span>

[![Rockylogic Ant18e](./img/RockyLogic_Ant18e.jpg)](./img/RockyLogic_Ant18e.png "Rockylogic Ant18e"){ .glightbox data-gallery="rockylogic-ant18e" }
<span class="caption">Rockylogic Ant18e</span>

</div>
## Protocol

The protocol for [Ant8](https://sigrok.org/wiki/RockyLogic_Ant8) / Ant16 / Ant18e seems to be very similar, so this section documents all variants.

Since the device uses an FTDI chip for USB communication with the host, the common endpoint configuration for devices like this is used: endpoint 1 for device-to-host communication, and endpoint 2 for host-to-device.

### FPGA bitstreams

There is one "base" FPGA bitstream which likely implements the "quick sample mode" explained below. This bitstream is (re-)uploaded after every sampling run.

Before a sampling run at a given sampling rate, a special bitstream is uploaded (a different one for each samplerate, it seems).

The size of a bitstream (plus metadata or other info contained in the binary data sent to the device) is **174612 bytes** (Ant18e) or **56138 bytes** (Ant8).

On Ant8, the FTDI chip's D0-D7 (data) pins are connected to the CPLD, and one of the CPLD pins is connected to the PROGRAM# pin of the FPGA. It's thus likely that the data sent from the host is received by the CPLD, which then writes the configuration bitstream into the FPGA via one of multiple possible methods.

The command **0x03** starts a bitstream upload; it is immediately followed by a bitstream of the size relevant to that device.

### Status

The commands **0x02 0x81** and **0x12 0x81** request the current status from the device. The response is a one-byte status code:

**0x02 0x81**: appears to be used in "idle" mode only.

- 0x0e: unknown
- 0x08: unknown
- 0x0b: unknown
- 0x07: unknown

**0x12 0x81**: appears to be used when capturing.

- 0x02:&#160;?
- 0x03: waiting for trigger?
- 0x43: prefill?
- 0x86: (not seen with proper trigger)
- 0xc7: capture ready
### Quick sample mode

This mode lets the host receive the status of all probes immediately. It's used by the original software to animate the "pins" display when a proper acquisition is not running.

The host sends a two-byte command (Ant18e: **0x19 0x92**, Ant8: **0x19 0x88**). The second bytes seems to have bit 7 always set to 1, and (some of) the remaining bits (6..0) encode the number of bytes/probes to get (18 for Ant18e, 8 for Ant8). We expect that the Ant16 uses **0x19 0x90** as command (not verified due to lack of Ant16 hardware).

The host then receives in return a number of bytes (Ant18e: **18 bytes**, Ant8: **8 bytes**) containing the state of all probes. Each byte has the information for one probe, encoded as follows:

- Bits 7-3 (7-4 on Ant8): The probe ID (Ant18e: 0-17, Ant8: 0-7); shift right by 3 bits (on Ant18e), or 4 bits (on Ant8).
- Bit 2: If 1/high, this means a falling edge occured on the respective probe(?)
- Bit 1: If 1/high, this means a rising edge occured on the respective probe(?)
- Bit 0: The state of the respective signal (0: low, 1: high).

Example on Ant8:

- Host sends: 0x19 0x88
- Host receives (for example):
0x00 0x10 0x20 0x30 0x40 0x50 0x60 0x70 (all 8 probes are low)
- 0x00 0x13 0x20 0x30 0x40 0x50 0x60 0x70 (probe 1 went from low to high == rising edge)
- 0x00 0x11 0x20 0x30 0x40 0x50 0x60 0x70 (probe 1 is high, and was high before too)
- 0x00 0x14 0x20 0x30 0x40 0x50 0x60 0x70 (probe 1 went from high to low == falling edge)
- 0x00 0x10 0x20 0x30 0x40 0x50 0x60 0x70 (probe 1 is low, and was low before too)
### Starting a measurement

TODO

### Measurement configuration

TODO: Triggers etc.

### Retrieving samples

The host simply reads all samples from the device. The samples are given in the following format:

Ant8:

- There are exactly 3072 samples per run, each sample consisting of one byte, where bit 0 is the state (low/high) of probe 0, and bit 7 is the state of probe 7.
- There is no compression or "mangling" of the sample data.
### Pseudo-continuous sampling mode

The original software has a mode where it automatically does one sample run after the other. This is achieved by starting an acquisition, right after the previous one has finished. A new bitstream is only uploaded if needed, i.e., if parameters such as sampling rate are changed by the user. Otherwise only some (smaller) command/setup bytes are sent to the device.

Either way there will be data between two consecutive runs that will not be acquired/seen by the user, so this is not a "real" continuous sampling mode.

## Resources

TODO.

