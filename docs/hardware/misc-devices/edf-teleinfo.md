# Edf Teleinfo

| | | |:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------------:| | [![\1](../../assets/hardware/general/\2)](./File:Actaris_a14c5_teleinfo.png.html) | | | Status | supported | | Source code | [teleinfo](http://github.com/OpenTraceLab/?p=OpenTraceCapture.git;a=tree;f=src/hardware/teleinfo) | | Connectivity | RS232 | | Measurements | energy, apparent power, current | **EDF Teleinfo** The **EDF Teleinfo** is a standard describing the client information RS232 output that all main house energy meter must follow in France. A few manufacturers are selling compliant energy meters, such as Sagem, Landis+Gyr or Actaris. Those energy meters can read current, apparent power and total consumed energy. ## Photos \- 
[![\1](../../assets/hardware/general/\2)](./File:Actaris_a14c5_teleinfo.jpeg.html)
## Protocol The device is continuously sending informations on a modulated serial port running at 1200 bauds 7e1. The signal is ASK modulated on a 50 kHz carrier. The protocol is detailed in [this document](http://www.planete-domotique.com/notices/ERDF-NOI-CPT_O2E.pdf). ## Resources \- [Demodulateur teleinformation EDF](http://vesta.homelinux.free.fr/site/wiki/demodulateur_teleinformation_edf.html) \- [La téléinformation EDF (Planète Domotique)](http://www.planete-domotique.com/blog/2010/03/30/la-teleinformation-edf/)
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=EDF_Teleinfo&oldid=7429](https://OpenTraceLab.org/w/index.php?title=EDF_Teleinfo&oldid=7429)" 
[Categories](specialcategories-specialcategories.md): \- [Device](./Category:Device.html "Category:Device") \- [Energy meter](./Category:Energy_meter.html "Category:Energy meter") \- [Supported](./Category:Supported.html "Category:Supported")

## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
