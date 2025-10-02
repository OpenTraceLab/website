---
title: ASIX OMEGA
---

# ASIX OMEGA

<div class="infobox" markdown>

![ASIX OMEGA](./img/ASIX_Omega.png){ .infobox-image }

### ASIX OMEGA

| | |
|---|---|
| **Status** | supported |
| **Source code** | [asix-omega-rtm-cli](https://github.com/OpenTraceLab/OpenTraceCapture/tree/main/src/hardware/asix-omega-rtm-cli) |
| **Channels** | 16 |
| **Samplerate** | 200MHz @ 16ch, 400MHz @ 8ch |
| **Samplerate (state)** | &lt;100MHz |
| **Triggers** | value, edge, duration, sequence, counter, logical ops |
| **Min/max voltage** | -0.3V — 5.5V |
| **Threshold voltage** | Fixed: VIH=2.0V, VIL=0.8V (suitable for TTL, LVTTL, 2.7-5.5V CMOS) |
| **Memory** | 512 megabit |
| **Compression** | "real-time hardware data compression" |
| **Website** | [asix.net](http://www.asix.net/dbg_omega.htm) |

</div>

The **ASIX OMEGA** is the successor of the [ASIX SIGMA](https://sigrok.org/wiki/ASIX_SIGMA) logic analyzer. It is a 16 channel logic analyzer with a samplerate of 200MHz (8 channels at 400MHz), and with 512 Mbit on-board memory. It uses Huffman compression and achieves much better a compression ratio than SIGMA. The hardware supports chaining several OMEGA analyzers with synchronization cables to increase the number of channels.

**IMPORTANT:** The sigrok project currently lacks native support for the device. The sigrok driver uses the vendor software in a specific mode (RTM CLI), thus only part of the feature set is available on those platforms where the vendor software works (Windows x86).

See [ASIX OMEGA/Info](https://sigrok.org/wiki/ASIX_OMEGA/Info) for more details (such as **lsusb -v** output) about the device.

## Hardware
- Xilinx Spartan [XC3S200A](http://www.xilinx.com/support/documentation/data_sheets/ds529.pdf) (FPGA)
- FTDI [FT232HL](http://www.ftdichip.com/Support/Documents/DataSheets/ICs/DS_FT232H.pdf) (USB connectivity)
- SOT23-5 EEPROM for FTDI FT232H
- 2 x NXP [LVC245A](http://www.nxp.com/documents/data_sheet/74LVC_LVCH245A.pdf) (buffer / level shifter)
- [LC125A](http://www.ti.com/lit/ds/scas290q/scas290q.pdf) (buffer / level shifter)
- 2 x [MT48LC16M16A2B4-7E](https://www.micron.com/~/media/documents/products/data-sheet/dram/256mb_sdr.pdf) (DRAM for sample data)
- [ICS570BL](https://www.idt.com/document/dst/570-datasheet) (IDT, "multiplier and zero delay buffer", trigger clock sync?)
- [MF204A](http://www.ti.com/lit/ds/symlink/sn65mlvd204a.pdf) (LVDS line driver)
- multiple regulators, and stuff ...

## Photos

<div class="photo-grid" markdown>

[![Asix Omega](./img/ASIX_Omega.png)](./img/ASIX_Omega.png "Asix Omega"){ .glightbox data-gallery="asix-omega" }
<span class="caption">Asix Omega</span>

[![Omega Bottom](./img/Omega-Bottom.jpg)](./img/Omega-Bottom.jpg "Omega Bottom"){ .glightbox data-gallery="asix-omega" }
<span class="caption">Omega Bottom</span>

[![Omega Top](./img/Omega-Top.jpg)](./img/Omega-Top.jpg "Omega Top"){ .glightbox data-gallery="asix-omega" }
<span class="caption">Omega Top</span>

</div>
## Documentation

TODO

## Example usage

Ideally the sigrok project's asix-sigma driver would also cover Omega devices, but it doesn't. The firmware is not available for distribution, and the protocol information is not publicly available. The asix-sigma driver can detect the Omega devices' presence, but cannot operate them and merely emits a diagnostics message. Models can be told from the serial numbers.

As a quick enabler a separate sigrok driver makes principal operation of Omega devices available by means of the RTM CLI vendor application, which provides a subset of the device's feature set. These are the resulting limitations:

- fixed operation on 16 input signals at a 200MHz samplerate
- hardware triggers are not available
- chains are not available, only a single device can be used
- the vendor software targets Windows (x86), and also executes in wine (when FTDI libs are made available)
- the theoretical 200MHz @ 16ch throughput is constrained by the USB2.0 FTDI FIFO communication, hardware compression helps when input signals are slow or redundant, as does the deep sample memory which smoothes out bursts of activity, but that limitation remains because streaming mode is used

See the **README.devices** document for details on the Asix Omega operation in RTM CLI mode. It outlines the approach, and discusses requirements, configuration, and use.

Optional: Specify the vendor application executable location (needed when 'omegartmcli' is not in PATH).

```
 $ export OMEGARTMCLI="$HOME/.wine/drive_c/progx86/ASIX/SIGMA/omegartmcli.exe"

```

Scan for the device's presence, reflect its properties. Optional: Select one out of multiple connected devices.

```
 $ sigrok-cli -d asix-omega-rtm-cli --scan
 $ sigrok-cli -d asix-omega-rtm-cli --show
 $ sigrok-cli -d asix-omega-rtm-cli:conn=sn=a6030123 --show

```

Capture data for a specified amount of time or a specified amount of samples. Start the GUI for interactive use.

```
 $ sigrok-cli -d asix-omega-rtm-cli -o capture.sr --time 10s
 $ sigrok-cli -d asix-omega-rtm-cli -o capture.sr --samples 100m
 $ pulseview -d asix-omega-rtm-cli &

```

## Firmware

TODO

## Resources
- [vendor's product page](http://www.asix.net/dbg_omega.htm)
- [vendor's download page](https://asix.tech/dbg_omega_en.html) user guide, application notes, vendor software
- [Using ASIX products under Linux](https://asix.tech/support_linux_en.html)

