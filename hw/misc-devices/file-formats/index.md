---
title: File formats
---

# File formats

<div class="infobox" markdown>

### File formats

| | |
|---|---|

</div>

[libsigrok](/wiki/Libsigrok) supports a number of different input modules (a.k.a. file formats) and output modules, and has a generic API which allows easily adding more input/output modules.

## Supported input/output formats
| Name | Input | Output | Description |
|---|---|---|---|
| [Analog](/w/index.php?title=File_format:Analog&action=edit&redlink=1) | — | supported | Text output of analog data and types. |
| [ASCII](/w/index.php?title=File_format:Ascii&action=edit&redlink=1) | — | supported | ASCII art. |
| [Binary](/wiki/File_format:Binary) | supported | supported | Raw binary data output without any metadata attached. |
| [Bits](/w/index.php?title=File_format:Bits&action=edit&redlink=1) | — | supported | 0/1 digits. |
| [ChronoVu LA8](/wiki/File_format:Chronovu_la8) | supported | supported | [ChronoVu LA8](/wiki/ChronoVu_LA8) software file format (usually with .kdt file extension). |
| [CSV](/wiki/File_format:Csv) | supported | supported | Comma-separated values (also usable for generating data and config files for gnuplot). |
| [hex](/w/index.php?title=File_format:Hex&action=edit&redlink=1) | — | supported | Hexadecimal digits. |
| [Intronix Logicport LA1034](/w/index.php?title=File_format:Logicport&action=edit&redlink=1) | supported | — | [Intronix Logicport LA1034](/wiki/Intronix_Logicport_LA1034) *.lpf files. |
| [ols](/w/index.php?title=File_format:Ols&action=edit&redlink=1) | — | supported | The file format used by the ["Alternative" Java client](http://www.lxtreme.nl/ols/) for the [Openbench Logic Sniffer](/wiki/Openbench_Logic_Sniffer). |
| [protocoldata](/wiki/File_format:Protocoldata) | supported | — | Re-creates logic trace waveforms from a sequence of data values and optional control instructions. |
| [saleae](/wiki/File_format:Saleae) | supported | — | Files exported by the Saleae Logic application. |
| [srzip](/wiki/File_format:Srzip) | supported | supported | The current (v2) sigrok session file format (*.sr). |
| [STF](/wiki/File_format:Stf) | supported | — | "Sigma Test File". Native format of the Asix Sigma/Omega vendor software. |
| [VCD](/wiki/File_format:Vcd) | supported | supported | The [Value Change Dump](http://en.wikipedia.org/wiki/Value_change_dump) format (can also be visualized in [gtkwave](http://gtkwave.sourceforge.net/), for instance). |
| [WAV](/wiki/File_format:Wav) | supported | supported | The [waveform audio](http://en.wikipedia.org/wiki/WAV) (WAV) file format. |
| [Raw analog](/w/index.php?title=File_format:Raw_analog&action=edit&redlink=1) | supported | — | Analog signals without header (configurable sample size, format, and endianness). |
| [Lauterbach Trace32](/wiki/File_format:Trace32_ad) | supported | — | The Lauterbach Trace32 logic analyzer data file format. |
| [WaveDrom](/wiki/File_format:Wavedrom) | — | supported | Digital timing diagrams in JSON syntax |

The output formats apply only to unprocessed raw data. Data processed by decoders can't be saved into output file by argument, only by redirection of `STDOUT`.

## Supported transform modules
| Name | Description |
|---|---|
| nop | Do nothing. |
| scale | Scale analog values by a specified factor. |
| invert | Invert values. |

## Possible candidates for future input/output formats
| Name | Description |
|---|---|
| Scanalogic | Used by the [IKALOGIC Scanalogic-2](/wiki/IKALOGIC_Scanalogic-2) and [IKALOGIC ScanaPLUS](/wiki/IKALOGIC_ScanaPLUS) logic analyzers. |
| [Rigol ROF](/wiki/File_format:Rigol_rof) | Used by the [Rigol DP800 series](/wiki/Rigol_DP800_series) power supplies. |
| [Rigol RAF](/wiki/File_format:Rigol_raf) | Used by the Rigol DG1000Z, DG4000, and DG5000 series signal generators. See [DG1000Z User Guide](http://www.batronix.com/pdf/Rigol/UserGuide/DG1000Z_UserGuide_EN.pdf) page 2-75, also [this post](http://www.eevblog.com/forum/testgear/rigol-dg4000-series-raf-file-format/msg559443/) at eevblog. |
| [Rigol WFM](/w/index.php?title=File_format:Rigol_wfm&action=edit&redlink=1) | Used by the Rigol DS series oscilloscopes. See [https://github.com/mabl/pyRigolWFM/blob/master/wfm.py](https://github.com/mabl/pyRigolWFM/blob/master/wfm.py) |
| [Rigol WFM4](/wiki/File_format:Rigol_WFM4) | Used by the Rigol DS4000 series oscilloscopes. |
| Vector MDF (v3.3) / ASAM MDF (v4.x) | Automotive industry standard format. Docs can be found [here](http://vector.com/vi_mdf_de.html) and [here](http://vector.com/downloads/mdf_specification.pdf). Validator is [here](http://vector.com/downloads/MDFValidator2.1.8.zip). Some code is [here](https://code.google.com/p/mdfreader/) and [here](http://sourceforge.net/p/mdfdatafile/code/HEAD/tree/). |
| [COMTRADE](http://en.wikipedia.org/wiki/Comtrade) | File format used by devices in power engineering (e.g. protective relays, fault recorders). Can contain digital and analog data with constant or variable sample rate. |
| [PWL](/wiki/File_format:Pwl) | Trivial file format that can be used to define the signal of voltage/current sources in a SPICE simulation. |
| [Tektronix WFM](/wiki/File_format:Tektronix_wfm) | Used by the Tektronix TDS series oscilloscopes. A parser for Matlab can be found [here](http://www.mathworks.com/matlabcentral/fileexchange/5873-tektronix-binary-file-readers/content/wfmread.m). |
| EVCD/IDX/FST/GHW | File formats generated by hardware simulation tools. See the [GtkWave manual](http://gtkwave.sourceforge.net/gtkwave.pdf) for some of them, and conversion utilities. |
| [NI TDMS](https://www.ni.com/hu-hu/support/documentation/supplemental/06/the-ni-tdms-file-format.html) | File formats used by various National Instruments software like LabVIEW or DAQExpress. |
| IMC data format | File formats used by imc GmbH softwares. File format description can be found in the [imc Software Shared Components documentation](https://www.imcdataworks.com/secure-dl/?file=fileadmin/Download-Center/Manuals/imc_FAMOS/imcSharedComponents.pdf). (Registration required.) |

