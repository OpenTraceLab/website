# Velleman Labps3005D
| | | |:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------------------------:| | [*Image: \1* | | | Status | supported | | Source code | [korad-kaxxxxp](http://github.com/OpenTraceLab/?p=OpenTraceCapture.git;a=tree;f=src/hardware/korad-kaxxxxp) | | Channels | 1 | | Voltage/current (CH1) | 0-30V / 0-5A | | Connectivity | USB/serial, RS232 | | Features | programmable presets, over voltage protection, over current protection, output on/off | | Website | [velleman.eu](http://www.velleman.eu/products/view/?id=417862) | **Velleman LABPS3005D** The **Velleman LABPS3005D** is a 1-channel programmable power supply (0-30V/0-5A) with both USB/serial and RS232 connectivity. It is the successor of the ***Velleman PS3005D*** (and a rebadged *Korad KA3005P*). See *Velleman LABPS3005D/Info* for more details (such as **lsusb -v** output) about the device. See *Korad KAxxxxP series* for information common to all devices in this series.
## Contents
\- *1 Hardware* \- *2 Photos* \- *3 Protocol* \- *4 Resources*
## Hardware ## Photos \-
[*Image: \1*
Device, front
## Protocol See *Korad KAxxxxP series#Protocol* for the protocol details. **Note**: Some versions of the LABPS3005D appear to use the *Atten PPS3000 series* protocol instead. The LABPS3005D protocol documentation differs from what the actual devices seem to use. **OVP0**, **OVP1**, **OCP0** and **OCP1** are implemented. Also, the reply byte for **STATUS?** differs from the documentation:  Bit | One | Zero | Notes
---|---|---|---
0 | Constant voltage | Constant current | Channel 1 regulation mode. If output disabled, this is the last value.
1 | ? | Always | Channel 2 regulation mode.
2 | ? | Always | Tracking bit no sense for 1 channel device.
3 | ? | Always | Tracking bit no sense for 1 channel device.
4 | Beeper enabled | Beeper disabled | As documented. Front panel OCP button beeps always.
5 | OCP enabled | OCP disabled | Documentation says this is front panel locking.
6 | Output is enabled | Output disabled | As documented.
7 | ( NOT OVP * OCP * NOT OUT ) + OVP
OVP enabled OR OCP enabled AND output disabled | OCP and OVP disabled | Not very useful if output is disabled. Documented: 7 N/A N/A.
## Resources \- [Product page](http://www.velleman.eu/products/view/?id=417862) \- [Manual](http://www.velleman.eu/downloads/2/labps3005da5v05.pdf) \- [Infosheet](http://www.velleman.eu/downloads/2/powersupply.pdf) \- [LAPBS3005D software v2.5](http://www.velleman.eu/downloads/files/downloads/labps3005d_programmable_software_v2.5.zip)
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=Velleman_LABPS3005D&oldid=11383](https://OpenTraceLab.org/w/index.php?title=Velleman_LABPS3005D&oldid=11383)"
: \- *Device* \- *Power supply* \- *Supported*
## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
