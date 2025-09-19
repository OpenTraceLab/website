# Va Va18B
| | | |:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------------------:| | [*Image: \1* | | | Status | supported | | Source code | [serial-dmm](http://github.com/OpenTraceLab/?p=OpenTraceCapture.git;a=tree;f=src/hardware/serial-dmm) | | Counts | 6000 | | IEC 61010-1 | CAT II (1000V) | | Connectivity | *USB/serial* | | Measurements | voltage, resistance, continuity, diode, capacitance, frequency, current, temperature, duty cycle | | Features | min/max, data hold, relative, backlight | | Website | [mastech.com](http://www.mastech.com.cn/html/en/products-va18b.htm) | **V&A; VA18B** The **V&A; VA18B** is a 6000 counts, CAT II (1000V) handheld digital multimeter with USB connectivity. See *V&A; VA18B/Info* for more details (such as **lsusb -v** output) about the device. Note: The company V&A; ("[SHANGHAI YIHUA V&A INSTRUMENT CO., LTD, known as Mastech Shanghai](http://www.mastech.com.cn/html/en/about-us.htm)") has apparently been part of (or related to) [MASTECH](http://www.p-mastech.com) in the past, and also sells some multimeter models that have been sold by MASTECH in the past.[1](http://www.eevblog.com/forum/product-reviews-photos-and-discussion/product-review-dmm-latest-va-mastech-va18b/msg128081/#msg128081)
## Contents
\- *1 Model overview* \- *2 Hardware* \- *3 Photos* \- *4 Protocol* \- *5 Resources*
## Model overview It seems there have been at least two different revisions of the multimeter (or at least of the PC-Link cable). The older one used a Sunplus SPCP825 USB-to-serial chip (see [here](http://www.mikrocontroller.net/topic/160215#2032176), [here](http://multimeter.schewe.com/), or also check the drivers from *here*), the newer revisions use a Prolific PL2303HX chip. Both should work fine with OpenTraceLab, as long as the respective driver creates a "virtual COM port" / serial port device OpenTraceLab can connect to. | | | | | | |-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|-----------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | Device | Rebranded? | PC interface chip | Vendor software | Comments | | [V&A VA18B](http://www.mastech.com.cn/html/en/products-va18b.htm) (old) | no | Sunplus SPCP825 | "PC-LINK" | Manual: [VA18B.pdf](http://www.mastech.com.cn/down/VA18B.pdf) | | [V&A VA18B](http://www.mastech.com.cn/html/en/products-va18b.htm) (new) | no | Prolific PL2303HX | "PC-LINK" | Manual: [VA18B.pdf](http://www.mastech.com.cn/down/VA18B.pdf). PCB silk screen: "VA18B 20070302". | | [Amarad Hellas Electronic VA18B](http://www.amarad.gr/full_product.php?prod_id=1114026193) | yes (VA18B) | ? | ? | See also [this photo](http://www.eevblog.com/forum/product-reviews-photos-and-discussion/product-review-dmm-latest-va-mastech-va18b/?action=dlattach;attach=15446;image). PCB silk screen: "VA18B 20070302". | | [Velleman DVM1200](http://www.velleman.eu/products/view/?id=372236) | yes (VA18B) | ? | "PC-LINK" | — | | [Maxwell MX-25328](http://www.maxwell-digital.com/index.php?tld=en&page=product&d1=new&d2=multimeters&c=04_25328) | [yes](http://www.eevblog.com/forum/product-reviews-photos-and-discussion/product-review-dmm-latest-va-mastech-va18b/msg115180/#msg115180) (VA18B) | ? | "Maxwell Universal Program" | Maxwell wrote [their own PC software](http://www.maxwell-digital.com/index.php?tld=en&page=product&d1=new&d2=multimeters&c=04_25328), apparently (works fine with the VA18B if you select "25328" as device in the software). | | *PeakTech P3375* | likely (VA18B) | ? | ? | Very likely a rebranded V&A; VA18B ([1](https://www.buerklin.com/default.asp?event=ShowArtikel%2821K535%29&l=e&jump=ArtNr_21K535&ajaxLoad=true), [2](http://www.avelmak.sk/index.php?lm=620&pg=det&article=35074), [3](http://www.ebay.de/itm/Digital-Multimeter-Peaktech-P3375-/320835015683?pt=Mess_Pr%C3%BCftechnik&hash=item4ab341d403)). | ## Hardware **Multimeter**: \- **Main chip:** Unknown, it's very likely a bare die under the black blob (see photos). The pads suggest it's a 100pin device. \- **Display glass**: "O LIT051476 LDH" (left), "090504 LDTP11781H" (right) \- **Precision, very low power, CMOS dual opamp:**: 27L2C U85T CN58 \- **100 mA Low Power LDO (3.0V)**: [Holtek HT7530-1](http://www.holtek.com/english/docum/consumer/75xx_1.htm) \- **Crystal**: 4MHz \- **Fuses**: 750mA/600V (5x20mm), 10A/600V (6x30mm) **USB cable**: \- See *Device cables#V.26A_VA4000*. ## Photos **Multimeter:** \-
[*Image: \1*
Package, front
\-
[*Image: \1*
Package, back
\-
[*Image: \1*
Package, contents
\-
[*Image: \1*
Device, front
\-
[*Image: \1*
Device, back
\-
[*Image: \1*
Device, open 1
\-
[*Image: \1*
Device, open 2
\-
[*Image: \1*
PCB, front
\-
[*Image: \1*
PCB, front, 1
\-
[*Image: \1*
PCB, front, 2
\-
[*Image: \1*
PCB, front, 3
\-
[*Image: \1*
PCB, back
\-
[*Image: \1*
27L2C
\-
[*Image: \1*
7350-1
\-
[*Image: \1*
Crystal
\-
[*Image: \1*
LCD
**USB cable:** See *Device cables#V.26A_VA4000*. ## Protocol 14-byte LCD segments over USB-2-serial (Prolific PL2303HX chip, 2400 baud, 8n1), see various links below. The DMM IC used in this multimeter is very likely a Fortune Semiconductor FS9721_LP3, see *Multimeter_ICs#Fortune_Semiconductor_FS9721_LP3* for the protocol. The transmission of the 14-byte chunks happens roughly every 300ms (measured using a logic analyzer at 24MHz samplerate, on the receiver IR diode on the USB cable and the RX pin of the PL2303HX). Sometimes it's 300.15ms, then 325.16ms, then 300.15ms, then 325.16ms again, and so on. This timing seems to be quite consistent. However, only exactly 8 of these 14-byte chunks are spaced at 300ms. Every 9th chunk of 14 bytes will then be 600ms apart, for (yet) unknown reasons. This is not due to the IR transmission, the same effect can be verified when measuring the respective timing on the multimeter itself (before the data gets sent via IR). To enable output to the PC on the multimeter you have to keep the **Hz/DUTY** key pressed while powering on the device. However, it will auto-poweroff after roughly 1 hour, even in this mode. To avoid that, press both the **Hz/DUTY** and the **SELECT** key during power-up (see [manual](http://www.mastech.com.cn/down/VA18B.pdf), page 9, section 2.3.1). ## Resources \- Protocol descriptions: [[1]](http://www.dh2faa.de/va18b.html), [[2]](http://www.gomatlab.de/datenuebertragung-va-18b-multimeter-t873.html), [[3]](http://multimeter.schewe.com/) \- [EEVblog forums: Product review: DMM latest V&A Mastech VA18B](http://www.eevblog.com/forum/product-reviews-photos-and-discussion/product-review-dmm-latest-va-mastech-va18b/) \- Other teardowns: [1](http://www.eevblog.com/forum/product-reviews-photos-and-discussion/product-review-dmm-latest-va-mastech-va18b/msg65513/#msg65513), [2](http://www.eevblog.com/forum/product-reviews-photos-and-discussion/product-review-dmm-latest-va-mastech-va18b/msg65679/#msg65679), [3](http://www.eevblog.com/forum/product-reviews-photos-and-discussion/product-review-dmm-latest-va-mastech-va18b/msg65698/#msg65698) (VA18B, but the PCB silkscreen says "[VA17B 20060413](http://www.eevblog.com/forum/product-reviews-photos-and-discussion/product-review-dmm-latest-va-mastech-va18b/?action=dlattach;attach=15597;image)")
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=V%26A_VA18B&oldid=8094](https://OpenTraceLab.org/w/index.php?title=V%26A_VA18B&oldid=8094)"
: \- *Device* \- *Multimeter* \- *Supported*
## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
