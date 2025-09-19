# Siglent Sdg1010
| | | |:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------------------------------------:| | [*Image: \1* | | | Status | planned | | Frequency (sine) | 10MHz | | Frequency (square) | 10MHz | | Frequency (other) | 5MHz (pulse), 300KHz (ramp) | | Frequency (user) | 5MHz | | Waveforms | sine, square, pulse, ramp, noise, user | | Waveform memory | 16000 points | | Modulation | AM, FM, PM, DSB-AM, FSK, ASK, PWM | | Connectivity | USBTMC | | Website | [siglent.com](http://siglent.com/en/product/detail3.aspx?id=100000001526838&nodecode=119008003) | **Siglent SDG1010** The Siglent SDG1010 is a 10MHz function generator with USB connectivity. See *Siglent SDG1010/Info* for more details (such as **lsusb -vvv** output) about the device.
## Contents
\- *1 Hardware* \- *2 Photos* \- *2.1 Device* \- *2.2 Teardown* \- *2.3 Digital parts* \- *2.4 Analog parts* \- *2.5 Display / frontpanel* \- *2.6 Power supply* \- *3 Protocol* \- *4 Resources*
## Hardware **Digital**: \- **...**: XILINX SPARTAN-6 XC6SLX9 (marking: "XILINX SPARTAN-6 XC6SLX9 FTG256BIV1201 D4339091A 2C TAIWAN") \- **...**: ISP13628D (marking: "ISP13628D 78535 8W D78132F") \- **...**: Lattice MachXO LCMXO640C (marking: "Lattice MachXO LCMXO640C 3TN144C A211CC25") \- **...**: Analog Devices ADSP-BF531 (markings: "Analog Devices ADSP-BF531 SBSTZ400 2310414.1 0.6 \\#1208 Blackfin") \- **...**: Advanced Monolithic Systems AMS1117 (marking: "AMS1117 1125") \- **...**: Hynix H57V1262GTR (marking: "Hynix H57V1262GTR-75C 209S N8FT1265Q2") \- **...**: Spansion S29GL064N90TFIO4 (markings: "Spansion S29GL064N90TFIO4 124FF491 H (C)06 SPANSION") \- and lots more... **Analog**: \- **14 bit, 165Msps digital to analog converter**: [Burr-Brown DAC904E](http://web.archive.org/web/20000418160235/http://www.burr-brown.com/cgi-bin/WebObjects/BurrBrown.woa/wa/displayProductFolder?productName=DAC904) (marking: "BB DAC904E 03C9JNK"), ([datasheet](http://www.datasheetcatalog.com/datasheets_pdf/D/A/C/9/DAC904.shtml)) \- Burr-Brown was acquired by Texas Instruments in 2000. New TI URLs: [DAC904 product page](http://www.ti.com/product/dac904), [TI datasheet](http://www.ti.com/lit/gpn/dac904). \- **16 bit, high speed, low noise, voltage output, digital to analog converter** : [Texas Instruments DAC8580](http://www.ti.com/product/dac8580) (marking: "D8580I 09T A97S"), ([datasheet](http://www.ti.com/lit/gpn/dac8580)) \- **Fixed 49.9 ohm impedance output**. The real output voltage of the device is not necessarily the same as the indicated output voltage of the device because there is a 50 ohm resistor in series with the output. This is done so that the user can have adequate transmission line termination on a 50 ohm coaxial cable, as well as being a rudimentary short circuit protection mechanism. You can set in software the impedance of the load you are driving so that the displayed voltage settings match the voltage present in the load. In earlier firmware versions, there were High-Z and 50 ohm impedances available. In more recent firmware versions (which?) the user can select any impedance from 50 ohm to 1k ohm and high-Z. Note that this only affect the displayed value. The internal output impedance is still 50 ohms, and there is still a voltage drop across that resistor, a voltage drop.  Ch1 can output up to 20V peak to peak (it goes from -10V to +10V), Ch2 can only go up to 6V pk-pk. Both have the fixed 49.9 ohm impedance, but because of the higher voltage output, Ch1 uses an array of 4 resistors, as seen on the images below. **Display/frontpanel**: \- ... **Power supply**: \- ... ## Photos ### Device \-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
### Teardown \-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
### Digital parts \-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
### Analog parts \-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
### Display / frontpanel \-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
### Power supply \-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
\-
[*Image: \1*
## Protocol There are two possible PC connectivity methods that can be selected in the SDG1010 menu, which have different USB VID/PID pairs: \- "Raw USB" (this is what the vendor PC software uses): **f4ed:ee37** \- "USBTMC": **f4ed:ee3a** Additionally, there are apparently *GPIB* and Ethernet options, but those are not available in the "standard" device. It's unclear if/where devices with those options can be bought, maybe only the rebranded LeCroy devices have them (?) TODO: Details. USBRAW connectivity is not possible on a Windows 8 platform, because of driver signature enforcement ([details](http://www.eevblog.com/forum/testgear/the-sdg1000-and-sdg800-thread/msg579096/#msg579096)). Additionally, there are no drivers provided by Siglent for platforms other than Windows. Obviously, USBTMC is the method to use for universal communication with this device. See the [SDG1000 programming manual](https://www.box.com/s/e18ab37cfc290838d50d) for a protocol description. A much better written manual is available for the LeCroy WaveStation series, which are rebadged Siglent generators. This manual is available on LeCroy's website, [here](http://cdn.teledynelecroy.com/files/manuals/wsta_scpi_manual_reva.pdf). ## Resources \- [EEVblog forums: Siglent SDG1025 Arbitrary/function generator under some tests](http://www.eevblog.com/forum/product-reviews-photos-and-discussion/siglent-sdg1025-arbitraryfunction-generator-under-some-tests/) (also has teardown photos) \- [EEVblog forums: Help choosing an ARB: New Siglent SDG1020 vs Used Fluke 281 / Wavetek 39A](http://www.eevblog.com/forum/product-reviews-photos-and-discussion/new-siglent-sdg1020-vs-used-fluke-281-wavetek-39a/) \- [EEVblog Forums: Siglent SDG1000 series thread, with a collection of resources including documentation, known issues, solutions and specifications](http://www.eevblog.com/forum/testgear/the-sdg1000-and-sdg800-thread/)
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=Siglent_SDG1010&oldid=10454](https://OpenTraceLab.org/w/index.php?title=Siglent_SDG1010&oldid=10454)"
: \- *Device* \- *Signal generator* \- *Planned*
## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
