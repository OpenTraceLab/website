# Fpgalafw
**This is a preliminary design** **fpgalafw** is a proposal for a project to implement a universal logic analyser firmware for use as a firmware for commercial logic analysers that we wish to support, on FPGA development boards and for use as an in-circuit, or even in-FPGA debugging tool.
## Contents
\- *1 Benefits* \- *2 Goals* \- *3 Previous Projects* \- *4 Status* \- *5 Components* \- *6 Project Folder Structure* \- *7 Firmware Packaging* \- *8 Firmware Build Environment* \- *9 Protocol*
## Benefits \- Would simplify the implementation of OpenTraceCapture. \- Reduced repetition. \- Advanced triggering becomes hard when every manufacturer has a different trigger model. We can implement one to cover a variety of devices. \- Unlock previously unsupported device features. If a feature is added to one LA, it is added to all. \- Would enable support for more analysers such as the *RockyLogic Ant8*, the *RockyLogic Ant18e*, the *ChronoVu LA8* etc. ## Goals \- 100% open-source Verilog implementation (written from scratch or based off of other open-source projects). \- Portable Verilog implementation that works (as much as possible) in a generic way. \- Should work across all common FPGA/CPLD families from various vendors, including Xilinx, Altera, Microsemi/Actel, Lattice, etc. \- Should work for any suitable FPGA/CPLD based logic analyzer board (existing devices or future ones than can be built specifically for use with this project), and any suitable CPLD/FPGA eval boards. \- This means that the use of vendor-/family-specific constructs are discouraged in the "core" of the code. There might be optional per-device or per-vendor constructs that are not portable, but those should be moved outside the "core" so that as much functionality as possible works for any device. ## Previous Projects There are various pre-existing open source firmware projects that can be drawn upon: \- 2004 - [eebit](http://www.freepcb.com/eebit/) \- 2006 - [SUMP](http://www.sump.org/projects/analyzer/) (written in VHDL) \- 2008 - [openVeriFLA](http://opencores.org/project,openverifla) \- 2009 - [miniLA](http://minila.sourceforge.net/index.php) \- 2009 - [LeKernel's Logic Analyser](http://lekernel.net/blog/2009/01/usb-logic-analyzer/) \- 2010 - [BitHound](http://www.bastli.ethz.ch/index.php?page=BitHoundEn) (Derived from SUMP but with Ethernet interface) \- 2011 - [OpenBench Logic Sniffer](http://dangerousprototypes.com/docs/Open_Bench_Logic_Sniffer) (Derived from SUMP, ported to Verilog) \- [Demon Core Verilog Source Code SVN](http://gadgetforge.gadgetfactory.net/gf/project/butterflylogic/scmsvn/?action=browse&path=%2Ftrunk%2FVerilog_Core%2F) ## Status Some intitial work has been done, but the project is not really started yet. The current best branches are \- Joel Holdsworth's work on the demon core: <https://github.com/jhol/butterflylogic> \- Iztok Jeras's work on the demone core: <https://github.com/jeras/butterflylogic> ## Components fpgalafw will not work as a monolithic single firmware. Rather it is a library/framework of components that can be assembled together depending on the capabilities of the device, and the mode of operation.
Host Interface |
  * [Cypress FX2](http://www.cypress.com/?id=193)
  * [FTDI FT245](http://www.ftdichip.com/Products/ICs/FT245BM.htm) USB Fifo
  * RS232 (SUMP)
  * Ethernet
  * USB-MCU
  * JTAG - for ChipScope-like in-circuit use cases.
  * PCIe?
  * Parallel Port?
  * Cypress FX3?
---
Storage |
  * Internal Block-RAM (BRAM)
  * External DRAM
  * External SDRAM (DDR2, DDR3)
  * Burst RAM
  * Internal Soft-RAM? (Shift Registers)
  * Streaming Pass-through
---
Data Packer |
  * N-probes to M-data Lines Muxer
  * RLE Encoder
  * RLE + Golomb/Huffman/... Encoder?
---
Indicator LEDs |
  * None
  * Tri-colour
  * Multiple LEDs
---
Operating Modes |
  * Storage Sampling
    * Asynchronous Mode
    * Externally Clocked Synchronous (State Analysis) Mode
  * Continuous Sampling
  * Pulse Counter
  * Time-to-digital Conversion
  * Signal Generation
---
Triggering |
  * External
  * Simple (Edge/Level)
  * Time Delayed
  * Advanced Triggers (the Demon Core replicates the behaviour of the HP16550)
---
## Project Folder Structure Proposed project folder structure... \- / \- README \- NEWS \- Makefile \- /boards \- /openbench-logic-sniffer \- /nexys2 \- /papilio ... \- /rtl \- /verilog \- /host-interface \- /cypress-fx2 \- /software \- /firmware \- /sump \- /firmware \- .... \- /storage \- /ddr2 \- /firmware \- /bram \- /firmware \- /tools \- \\# Scripts etc in here \- /sw \- \\# Embedded sofware here ## Firmware Packaging Each device class will be given a firmware package that the driver can load. This package will be ZIP-file containing multiple firmware .bit files for the different permutations of modes and options that can be selected on this device. It is undesirable to have a single universal hardware file for each device, because multiple features will compete for use the limited number of logic units and internal storage. The firmware package will contain a text index file that indicates the capabilities of the device, its Bus ID, and a list of the firmware files available. ## Firmware Build Environment The firmware will be built using a GNU Make driven build environment, which will be compatible with Altera, Xilinx, Microsemi/Actel, Lattice tools, and FreeHDL etc. ## Protocol We will implement a common command protocol, common among all the host interfaces. (With the possible exception of SUMP if we plan to support that).
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=Fpgalafw&oldid=7791](https://OpenTraceLab.org/w/index.php?title=Fpgalafw&oldid=7791)"
## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
