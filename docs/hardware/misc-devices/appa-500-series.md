# Appa 500 Series
| | | |:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------------------------:| | [*Image: \1* | | | Status | in progress | | Source code | [appa-dmm](http://github.com/OpenTraceLab/?p=OpenTraceCapture.git;a=tree;f=src/hardware/appa-dmm) | | IEC 61010-1 | CAT IV (600V) / CAT III (1000V) | | Connectivity | Optical (RS232/USB), Bluetooth LE (depending on model) | | Website | *appatech.com* | **_APPA 500 Series_ APPA 501, 502, 503, 505, 506, 506B, 507 BENNING MM 12 Elma 6600 IDEAL 61-497, 61-498 KPS DMM9000BT ISO-TECH/RS PRO IDM503, IDM505 Sefram 7351, 7352B, 7355, 7357 Voltcraft VC-930, VC-950** The **APPA 500** is a wide range of 6.000 to 100.000 counts, CAT III (1000V) / CAT IV (600V) handheld digital multimeters with optical RS232 / USB connectivity. Model variant 506B also has built-in Bluetooth LE connectivity. *For more information on the OpenTraceLab-integration see: *APPA Multimeters in OpenTraceLab using the appa-dmm driver**  Model | Compatible devices | Optical RS232/USB | Bluetooth LE | Support level | Comments
---|---|---|---|---|---
[APPA 501](http://www.appa.com.ua/product/appa-501) |  | X |  | implemented, untested |
[APPA 502](http://www.appa.com.ua/product/appa-502) |  | X |  | implemented, untested |
*APPA 503* | [CMT 3503](https://www.cosinus.de/?artnr=9998402138)
IDEAL 61-497
ISO-TECH IDM503
*Sefram 7351*
Voltcraft VC-930 | X |  | implemented, untested |
*APPA 505* | IDEAL 61-498
ISO-TECH & [RS PRO IDM505](https://www.rsonline-privat.de/Products/ProductDetail/RS-PRO-IDM505-Digital-Multimeter-1000V-ac-10A-ac-40M-Kat-III-Kat-IV-1241960)
*Sefram 7355*
*Voltcraft VC-950* | X |  | good |
*APPA 506* |  | X |  | good |
*APPA 506B* | *BENNING MM 12*
[KPS DMM9000BT](https://kps-intl.com/na/en/product-list/content/192E036f8140)
*Sefram 7352B* | X | X | good |
*APPA 507* | [CMT 3507](https://www.cosinus.de/?artnr=9998402140)
[Elma 6600](https://elma-instruments.com/products/elma-6600-automation-multimeter.aspx)
[HT Instruments HT8100](https://ht-instruments.de/produkte/multimeter/ht8100/)
*Sefram 7357* | X |  | implemented, untested | Unknown ID
USB cable of APPA 500 Series based meters: *APPA IC-300U* By the datasheet and feature list it seems to be that *208* is the bench version of the 506 handheld meters. Extra features of the 208 compared to the 506: AC 100-240V power supply (but it can still run on batteries), higher frequency measurement range at higher precision (4 MHz), duty cycle measurement and an extra button for display light instead of the automatic light sensor of the 506. *Important:* Some of the older models of the Series 503/505, like the *VC-950*, don't support the new APPA communication protocol with model identification. For these devices you need to manually select the appropriate driver (voltcraft-vc950, appa-500-legacy, etc.) in OpenTraceLab manually.
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=APPA_500_Series&oldid=16322](https://OpenTraceLab.org/w/index.php?title=APPA_500_Series&oldid=16322)"
: \- *Device* \- *Multimeter* \- *Bluetooth* \- *In progress*
## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
