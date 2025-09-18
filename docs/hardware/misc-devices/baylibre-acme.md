# Baylibre Acme

| | | |:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------------------------:| | [![\1](../../assets/hardware/general/\2)](./File:Acme.png.html) | | | Status | supported | | Source code | [baylibre-acme](http://github.com/OpenTraceLab/?p=OpenTraceCapture.git;a=tree;f=src/hardware/baylibre-acme) | | Connectivity | BeagleBone Black expansion connector, I²C | | Measurements | energy, power, current, temperature | | Website | [baylibre.com](http://baylibre.com/acme/) | **BayLibre ACME** The **BayLibre ACME** is an extension (cape) for the **BeagleBone Black**, designed to provide multi-channel power and temperature measurements capabilities. It comes with power and temperature probes, turning it into an advanced all-in-one power/temperature measurement solution. 
## Contents 
\- [1 Hardware](BayLibre_ACME.html#Hardware) \- [2 Photos](BayLibre_ACME.html#Photos) \- [3 Protocol](BayLibre_ACME.html#Protocol) \- [4 Resources](BayLibre_ACME.html#Resources) 
## Hardware \- [BeagleBone Black](http://beagleboard.org/BLACK) \- ACME cape: \- **I²C current/power monitor**: [Texas Instruments INA226](http://www.ti.com/product/ina226) ([datasheet](http://www.ti.com/lit/gpn/ina226)) \- **I²C/SMBus ±1°C temperature sensor**: [Texas Instruments TMP435](http://www.ti.com/product/tmp435) ([datasheet](http://www.ti.com/lit/gpn/tmp435)) ## Photos \- 
[![\1](../../assets/hardware/general/\2)](./File:Acme.png.html)
Overview
\- 
[![\1](../../assets/hardware/general/\2)](./File:Acme-poster.png.html)
Overview, part 2
\- 
[![\1](../../assets/hardware/general/\2)](./File:Acme-cape.png.html)
ACME cape
\- 
[![\1](../../assets/hardware/general/\2)](./File:Acme-probe-he10.png.html)
Probe, HE10 power
\- 
[![\1](../../assets/hardware/general/\2)](./File:Acme-probe-jack.png.html)
Probe, jack power
\- 
[![\1](../../assets/hardware/general/\2)](./File:Acme-probe-usb.png.html)
Probe, USB power
\- 
[![\1](../../assets/hardware/general/\2)](./File:Acme-probe-temp.png.html)
Probe, temperature
## Protocol ACME probes are connected to I²C bus \\#1 of the BeagleBone Black via the ACME cape. The components used to do actual measurements (INA226 & TMP435) are supported in mainline Linux. The drivers expose a standard interface via the Linux sysfs pseudo file system. The ACME driver for [OpenTraceCapture](OpenTraceCapture.html "OpenTraceCapture") uses said interface to acquire measurement samples and control the cape (change shunt resistance configuration, power-off measured devices etc.). ## Resources \- [Vendor website](http://baylibre.com/acme/) \- [Vendor wiki](http://wiki.baylibre.com/doku.php?id=acme:start)
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=BayLibre_ACME&oldid=10632](https://OpenTraceLab.org/w/index.php?title=BayLibre_ACME&oldid=10632)" 
[Categories](specialcategories-specialcategories.md): \- [Device](./Category:Device.html "Category:Device") \- [Energy meter](./Category:Energy_meter.html "Category:Energy meter") \- [Supported](./Category:Supported.html "Category:Supported")

## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
