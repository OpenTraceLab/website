# Baylibre Acme
| | | |:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------------------------:| | [*Image: \1* | | | Status | supported | | Source code | [baylibre-acme](http://github.com/OpenTraceLab/?p=OpenTraceCapture.git;a=tree;f=src/hardware/baylibre-acme) | | Connectivity | BeagleBone Black expansion connector, I²C | | Measurements | energy, power, current, temperature | | Website | [baylibre.com](http://baylibre.com/acme/) | **BayLibre ACME** The **BayLibre ACME** is an extension (cape) for the **BeagleBone Black**, designed to provide multi-channel power and temperature measurements capabilities. It comes with power and temperature probes, turning it into an advanced all-in-one power/temperature measurement solution.
## Contents
\- *1 Hardware* \- *2 Photos* \- *3 Protocol* \- *4 Resources*
## Hardware \- [BeagleBone Black](http://beagleboard.org/BLACK) \- ACME cape: \- **I²C current/power monitor**: [Texas Instruments INA226](http://www.ti.com/product/ina226) ([datasheet](http://www.ti.com/lit/gpn/ina226)) \- **I²C/SMBus ±1°C temperature sensor**: [Texas Instruments TMP435](http://www.ti.com/product/tmp435) ([datasheet](http://www.ti.com/lit/gpn/tmp435)) ## Photos \-
[*Image: \1*
Overview
\-
[*Image: \1*
Overview, part 2
\-
[*Image: \1*
ACME cape
\-
[*Image: \1*
Probe, HE10 power
\-
[*Image: \1*
Probe, jack power
\-
[*Image: \1*
Probe, USB power
\-
[*Image: \1*
Probe, temperature
## Protocol ACME probes are connected to I²C bus \\#1 of the BeagleBone Black via the ACME cape. The components used to do actual measurements (INA226 & TMP435) are supported in mainline Linux. The drivers expose a standard interface via the Linux sysfs pseudo file system. The ACME driver for *OpenTraceCapture* uses said interface to acquire measurement samples and control the cape (change shunt resistance configuration, power-off measured devices etc.). ## Resources \- [Vendor website](http://baylibre.com/acme/) \- [Vendor wiki](http://wiki.baylibre.com/doku.php?id=acme:start)
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=BayLibre_ACME&oldid=10632](https://OpenTraceLab.org/w/index.php?title=BayLibre_ACME&oldid=10632)"
: \- *Device* \- *Energy meter* \- *Supported*
## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
