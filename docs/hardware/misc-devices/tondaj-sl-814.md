# Tondaj Sl 814

| | | |:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:| | [![\1](../../assets/hardware/general/\2)](./File:Tondaj_sl-814.png.html) | | | Status | supported | | Source code | [tondaj-sl-814](http://github.com/OpenTraceLab/?p=OpenTraceCapture.git;a=tree;f=src/hardware/tondaj-sl-814) | | Connectivity | [USB/serial](Device_cables.html#Tondaj_SL-814_cable "Device cables") | | Frequency range | 31.5Hz - 8.5kHz | | Measurement range (A) | 40dB - 130dB | | Resolution | 0.1dB | | Accuracy (94dB@1kHz) | 2dB | | Frequency weighting | A, C | | Time weighting | F, S | | Website | [tondaj.cn](http://www.tondaj.cn/ce040_Eng/productshow.asp?id=43&mnid=1039&classname=DIGITAL%20SOUND%20LEVEL%20METER&uppage=/ce040_Eng/product.asp) | **Tondaj SL-814** The **Tondaj SL-814** (also referred to as **TDJ SL814** sometimes) is a sound level meter with USB connectivity. It is available from many different vendors, partly under different names or as noname "sound level meter", e.g. on [aliexpress.com](http://www.aliexpress.com/wholesale?SearchText=sl-814&catId=0), [amazon.com](http://www.amazon.com/s/ref=nb_sb_noss_2/182-8135276-7469311?url=search-alias%3Daps&field-keywords=sl-814) (from resellers such as Neewer, Skque, Generic, HDE, BestDealUSA, and many others). The device has an auto-poweroff feature which leads to a power-off after 5 minutes. There is no known way to prevent this from happening when running off of batteries. When connected via USB, the device stays powered on. As soon as the connection is removed though, the 5 minute timer for poweroff starts. See [Tondaj SL-814/Info](Tondaj_SL-814/Info.html "Tondaj SL-814/Info") for more details (such as **lsusb -vvv** output) about the device. 
## Contents 
\- [1 Hardware](Tondaj_SL-814.html#Hardware) \- [2 Photos](Tondaj_SL-814.html#Photos) \- [3 Protocol](Tondaj_SL-814.html#Protocol) \- [3.1 Commands / replies](Tondaj_SL-814.html#Commands_/_replies) \- [3.2 Data reply](Tondaj_SL-814.html#Data_reply) \- [3.3 Notes](Tondaj_SL-814.html#Notes) \- [4 Python script](Tondaj_SL-814.html#Python_script) \- [5 Resources](Tondaj_SL-814.html#Resources) 
## Hardware **Device**: \- **Main CPU**: [Atmel ATmega8/L](http://www.atmel.com/devices/ATMEGA8.aspx) (marking: "Atmel ATmega8L 8AU 1113D"), ([datasheet](http://www.atmel.com/Images/doc2486.pdf)) \- **8MHz crystal**: 8.00ECSXR \- **?**: 324 GZ15129 \- **5V (100mA) low-dropout voltage regulator**: [Holtek HT7550-1#](http://www.holtek.com/english/docum/consumer/75xx_1.htm) ([datasheet](http://www.holtek.com/pdf/consumer/ht75xx_1v200.pdf)) \- **Trim potentiometer**: Bochen 3296 **USB cable**: \- See [Device_cables#Tondaj_SL-814_cable](Device_cables.html#Tondaj_SL-814_cable "Device cables"). ## Photos **Device**: \- 
[![\1](../../assets/hardware/general/\2)](./File:Tondaj_sl-814_package.jpg.html)
\- 
[![\1](../../assets/hardware/general/\2)](./File:Tondaj_sl-814_package_contents.jpg.html)
\- 
[![\1](../../assets/hardware/general/\2)](./File:Tondaj_sl-814_device_front.jpg.html)
\- 
[![\1](../../assets/hardware/general/\2)](./File:Tondaj_sl-814_device_back.jpg.html)
\- 
[![\1](../../assets/hardware/general/\2)](./File:Tondaj_sl-814_device_front_nofoam.jpg.html)
\- 
[![\1](../../assets/hardware/general/\2)](./File:Tondaj_sl-814_probe_tip.jpg.html)
\- 
[![\1](../../assets/hardware/general/\2)](./File:Tondaj_sl-814_prolific_usb_cable.jpg.html)
\- 
[![\1](../../assets/hardware/general/\2)](./File:Tondaj_sl-814_lcd_segments.jpg.html)
\- 
[![\1](../../assets/hardware/general/\2)](./File:Tondaj_sl-814_jacks.jpg.html)
\- 
[![\1](../../assets/hardware/general/\2)](./File:Tondaj_sl-814_decapitated.jpg.html)
\- 
[![\1](../../assets/hardware/general/\2)](./File:Tondaj_sl-814_device_open.jpg.html)
\- 
[![\1](../../assets/hardware/general/\2)](./File:Tondaj_sl-814_cover.jpg.html)
\- 
[![\1](../../assets/hardware/general/\2)](./File:Tondaj_sl-814_pcb_top.jpg.html)
\- 
[![\1](../../assets/hardware/general/\2)](./File:Tondaj_sl-814_pcb_bottom.jpg.html)
\- 
[![\1](../../assets/hardware/general/\2)](./File:Tondaj_sl-814_bochen.jpg.html)
\- 
[![\1](../../assets/hardware/general/\2)](./File:Tondaj_sl-814_connectors.jpg.html)
\- 
[![\1](../../assets/hardware/general/\2)](./File:Tondaj_sl-814_atmega8l.jpg.html)
\- 
[![\1](../../assets/hardware/general/\2)](./File:Tondaj_sl-814_crystal.jpg.html)
\- 
[![\1](../../assets/hardware/general/\2)](./File:Tondaj_sl-814_gz15129.jpg.html)
\- 
[![\1](../../assets/hardware/general/\2)](./File:Tondaj_sl-814_gz15129_2.jpg.html)
\- 
[![\1](../../assets/hardware/general/\2)](./File:Tondaj_sl-814_holtek_7550.jpg.html)
\- 
[![\1](../../assets/hardware/general/\2)](./File:Tondaj_sl-814_holtek_ht1621b.jpg.html)
\- 
[![\1](../../assets/hardware/general/\2)](./File:Tondaj_sl-814_nxp_hef4053bt.jpg.html)
\- 
[![\1](../../assets/hardware/general/\2)](./File:Tondaj_sl-814_ti_tl062c.jpg.html)
**USB cable**: See [Device_cables#Tondaj_SL-814_cable](Device_cables.html#Tondaj_SL-814_cable "Device cables"). ## Protocol The device has a mini-USB connector for PC connectivity. It ships with a Prolific USB-to-serial cable (i.e. the PL2303 Prolific chip is *inside the cable*) which can be attached to that connector. The pinout of the USB side of the cable [appears to be a little unusual](https://www.amazon.com/review/R3DGCOYM03S2WJ): 1-NC, 2-TX, 3-RX, 4-GND, 5-GND (green/white swapped, red disconnected). The device accepts a simple command-based protocol over the (virtual) serial port, using a baudrate of **9600 baud**, with **8e1** settings (8 data bits, even parity, one stop bit). ### Commands / replies Commands and replies can consist of multiple bytes, and always end with **0x0d**. | | | | | |-----------------|--------------------|-----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | Name | Command | Reply | Comments | | Init | 0x10 0x04 0x0d | 0x05 0x0d | It's unclear what exactly this command does, likely some kind of initialization. Data transfers also seem to work fine when it is omitted. According to the scheme below in the "Send key" case it might be a "key press", but there doesn't seem to be any visible or noticeable effect at all. E.g. it does *not* reset any of the settings (A/C, fast/slow, and so on) to their defaults. | | Send key | 0x10 **0xKK** 0x0d | **0xKK+1** 0x0d | This command has the same effect as if a certain key/button on the SL-814 had been pressed. The known value encodings for the key (**0xKK**) are: **0x20** = up arrow key, **0x30** = down arrow key, **0x40** = A/C key, **0x50** = fast/slow key. There doesn't seem to be a key code for the "MAX" button or the power button. Thanks to Chris Hoogenboom for the info about this command. | | Get measurement | 0x30 **0xZZ** 0x0d | *0xAA 0xBB* **0xZZ+1** 0x0d | For a given command with **0xZZ** value (0-255), the device returns **0xZZ + 1** as part of the reply (a simple "sequence number" mechanism which is apparently meant for the host as error-checking mechanism). | ### Data reply The first two bytes of the reply to the "get measurement" command (*0xAA 0xBB*) have the following format: | | | | |------|-----|----------------------------------------------------------| | Byte | Bit | Value | | 0 | | | | | 7 | *A/C measurement type*. 0: **A**, 1: **C**. | | | 6 | *Unknown/unused*. | | | 5-4 | *Level*. 00: **40**, 01: **60**, 10: **80**, 11: **100** | | | 3 | *Slow/Fast measurement mode*. 0: **Fast**, 1: **Slow**. | | | 2-0 | *Value\\[10..8\\]*. | | 1 | | | | | 7-0 | *Value\\[7..0\\]*. | The actual measurement value seems to span 11 bits, and is encoded in BCD format. Example: If *Value\\[10..0\\]* is **436** (decimal), the corresponding measurement value is **43.6 dB**. ### Notes The "MAX" mode on the device (which always keeps showing the highest measured value since the "MAX" button was pressed) only affects the value shown on the display. The values returned via USB upon the "get measurement" command, always show the current value, not the "MAX" one shown on the display. ## Python script Here's a quick Python script for getting the values out of the Tondaj SL-814.  #!/usr/bin/python3 # Tondaj SL-814 sound level meter Python script # Copyright (C) 2012 Uwe Hermann  # Released under the terms of the GNU GPL, version 2 or later. import time import serial s = serial.Serial('/dev/ttyUSB0', baudrate=9600, parity=serial.PARITY_EVEN) while 1: # Query s.write(bytes([0x30, 0x01, 0x0d])) result = s.read(4) print('%02x %02x %02x %02x' % tuple(result), end=' - ') # A/C ac = (result[0] & (1 << 7)) >> 7 print('A' if ac == 0 else 'C', end=', ') # Slow/Fast sl = (result[0] & (1 << 3)) >> 3 print('Fast' if sl == 0 else 'Slow', end=', ') # Level factor = (result[0] & ((1 << 5) | (1 << 4))) >> 4 print('Level: %d' % (40 + (int(bin(factor), 2) * 20)), end=', ') # Value val = ((result[0] & 0x7) << 8) | result[1] tmp_str = '%d' % val val_str = tmp_str[:-1] + '.' + tmp_str[-1:] print(val_str + ' dB') time.sleep(0.5) s.close()  **Example output:**  09 af 02 0d - A, Slow, Level: 40, 43.1 dB 09 b9 02 0d - A, Slow, Level: 40, 44.1 dB 09 e9 02 0d - A, Slow, Level: 40, 48.9 dB 89 cb 02 0d - C, Slow, Level: 40, 45.9 dB 89 eb 02 0d - C, Slow, Level: 40, 49.1 dB 8a 6c 02 0d - C, Slow, Level: 40, 62.0 dB 82 99 02 0d - C, Fast, Level: 40, 66.5 dB 82 3c 02 0d - C, Fast, Level: 40, 57.2 dB 82 72 02 0d - C, Fast, Level: 40, 62.6 dB 92 85 02 0d - C, Fast, Level: 60, 64.5 dB 93 05 02 0d - C, Fast, Level: 60, 77.3 dB 92 68 02 0d - C, Fast, Level: 60, 61.6 dB a3 93 02 0d - C, Fast, Level: 80, 91.5 dB a3 93 02 0d - C, Fast, Level: 80, 91.5 dB a3 93 02 0d - C, Fast, Level: 80, 91.5 dB b3 f2 02 0d - C, Fast, Level: 100, 101.0 dB b3 f2 02 0d - C, Fast, Level: 100, 101.0 dB b3 f2 02 0d - C, Fast, Level: 100, 101.0 dB  ## Resources \- [Many Amazon reviews of the SL-814](http://www.amazon.com/USB-Digital-Sound-Level-Meter/product-reviews/B005JX2EZ2/ref=cm_cr_dp_see_all_btm?ie=UTF8&showViewpoints=1&sortBy=bySubmissionDateDescending) \- [Even more Amazon reviews of the SL-814](http://www.amazon.com/Digital-Sound-Frequency-Levels-Musicians/product-reviews/B005511F9Y/ref=cm_cr_pr_top_link_1?ie=UTF8&showViewpoints=0) \- Reviews mentioning the OpenTraceLab support and/or teardown: "[Forget the USB part...](http://www.amazon.com/review/R1VC2CMBK9LHWJ/ref=cm_cr_dp_title?ie=UTF8&ASIN=B005JX2EZ2&nodeID=1055398&store=home-garden)", "[Works Fine For Me](http://www.amazon.com/review/R3DGCOYM03S2WJ/ref=cm_cr_rdp_perm)" 
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=Tondaj_SL-814&oldid=11954](https://OpenTraceLab.org/w/index.php?title=Tondaj_SL-814&oldid=11954)" 
[Categories](specialcategories-specialcategories.md): \- [Device](./Category:Device.html "Category:Device") \- [Sound level meter](./Category:Sound_level_meter.html "Category:Sound level meter") \- [Supported](./Category:Supported.html "Category:Supported")

## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
