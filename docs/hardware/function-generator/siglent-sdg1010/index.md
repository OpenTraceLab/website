---
title: Siglent SDG1010
---

# Siglent SDG1010

<div class="infobox" markdown>

![Siglent SDG1010](./img/Siglent_sdg1010_analog_ad_ocmp_ti_13eep3k_5166isz.jpg){ .infobox-image }

### Siglent SDG1010

| | |
|---|---|
| **Status** | planned |
| **Frequency (sine)** | 10MHz |
| **Frequency (square)** | 10MHz |
| **Frequency (other)** | 5MHz (pulse), 300KHz (ramp) |
| **Frequency (user)** | 5MHz |
| **Waveforms** | sine, square, pulse, ramp, noise, user |
| **Waveform memory** | 16000 points |
| **Modulation** | AM, FM, PM, DSB-AM, FSK, ASK, PWM |
| **Connectivity** | USBTMC |
| **Website** | [siglent.com](http://siglent.com/en/product/detail3.aspx?id=100000001526838&amp;nodecode=119008003) |

</div>

The Siglent SDG1010 is a 10MHz function generator with USB connectivity.

See [Siglent SDG1010/Info](https://sigrok.org/wiki/Siglent_SDG1010/Info) for more details (such as **lsusb -vvv** output) about the device.

## Hardware

**Digital**:

- **...**: XILINX SPARTAN-6 XC6SLX9 (marking: "XILINX SPARTAN-6 XC6SLX9 FTG256BIV1201 D4339091A 2C TAIWAN")
- **...**: ISP13628D (marking: "ISP13628D 78535 8W D78132F")
- **...**: Lattice MachXO LCMXO640C (marking: "Lattice MachXO LCMXO640C 3TN144C A211CC25")
- **...**: Analog Devices ADSP-BF531 (markings: "Analog Devices ADSP-BF531 SBSTZ400 2310414.1 0.6 #1208 Blackfin")
- **...**: Advanced Monolithic Systems AMS1117 (marking: "AMS1117 1125")
- **...**: Hynix H57V1262GTR (marking: "Hynix H57V1262GTR-75C 209S N8FT1265Q2")
- **...**: Spansion S29GL064N90TFIO4 (markings: "Spansion S29GL064N90TFIO4 124FF491 H (C)06 SPANSION")
- and lots more...

**Analog**:

- **14 bit, 165Msps digital to analog converter**: [Burr-Brown DAC904E](http://web.archive.org/web/20000418160235/http://www.burr-brown.com/cgi-bin/WebObjects/BurrBrown.woa/wa/displayProductFolder?productName=DAC904) (marking: "BB DAC904E 03C9JNK"), ([datasheet](http://www.datasheetcatalog.com/datasheets_pdf/D/A/C/9/DAC904.shtml))
Burr-Brown was acquired by Texas Instruments in 2000. New TI URLs: [DAC904 product page](http://www.ti.com/product/dac904), [TI datasheet](http://www.ti.com/lit/gpn/dac904).
- **16 bit, high speed, low noise, voltage output, digital to analog converter **: [Texas Instruments DAC8580](http://www.ti.com/product/dac8580) (marking: "D8580I 09T A97S"), ([datasheet](http://www.ti.com/lit/gpn/dac8580))
- **Fixed 49.9 ohm impedance output**. The real output voltage of the device is not necessarily the same as the indicated output voltage of the device because there is a 50 ohm resistor in series with the output. This is done so that the user can have adequate transmission line termination on a 50 ohm coaxial cable, as well as being a rudimentary short circuit protection mechanism. You can set in software the impedance of the load you are driving so that the displayed voltage settings match the voltage present in the load. In earlier firmware versions, there were High-Z and 50 ohm impedances available. In more recent firmware versions (which?) the user can select any impedance from 50 ohm to 1k ohm and high-Z. Note that this only affect the displayed value. The internal output impedance is still 50 ohms, and there is still a voltage drop across that resistor, a voltage drop.
```
Ch1 can output up to 20V peak to peak (it goes from -10V to +10V), Ch2 can only go up to 6V pk-pk. Both have the fixed 49.9 ohm impedance, but because of the higher voltage output, Ch1 uses an array of 4 resistors, as seen on the images below. 

```

**Display/frontpanel**:

- ...

**Power supply**:

- ...

## Photos

<div class="photo-grid" markdown>

[![Siglent Sdg1010 Analog Ad Ocmp Ti 13eep3k 5166isz](./img/Siglent_sdg1010_analog_ad_ocmp_ti_13eep3k_5166isz.jpg)](./img/Siglent_sdg1010_analog_ad_ocmp_ti_13eep3k_5166isz.jpg "Siglent Sdg1010 Analog Ad Ocmp Ti 13eep3k 5166isz"){ .glightbox data-gallery="siglent-sdg1010" }
<span class="caption">Siglent Sdg1010 Analog Ad Ocmp Ti 13eep3k 5166isz</span>

[![Siglent Sdg1010 Backpanel Pcb](./img/Siglent_sdg1010_backpanel_pcb.jpg)](./img/Siglent_sdg1010_backpanel_pcb.jpg "Siglent Sdg1010 Backpanel Pcb"){ .glightbox data-gallery="siglent-sdg1010" }
<span class="caption">Siglent Sdg1010 Backpanel Pcb</span>

[![Siglent Sdg1010 Analog Ft B3g4a 5z](./img/Siglent_sdg1010_analog_ft_b3g4a_5z.jpg)](./img/Siglent_sdg1010_analog_ft_b3g4a_5z.jpg "Siglent Sdg1010 Analog Ft B3g4a 5z"){ .glightbox data-gallery="siglent-sdg1010" }
<span class="caption">Siglent Sdg1010 Analog Ft B3g4a 5z</span>

[![Siglent Sdg1010 Cpld Conn Fpgarun](./img/Siglent_sdg1010_cpld_conn_fpgarun.jpg)](./img/Siglent_sdg1010_cpld_conn_fpgarun.jpg "Siglent Sdg1010 Cpld Conn Fpgarun"){ .glightbox data-gallery="siglent-sdg1010" }
<span class="caption">Siglent Sdg1010 Cpld Conn Fpgarun</span>

[![Siglent Sdg1010 Pcb Bottom](./img/Siglent_sdg1010_pcb_bottom.jpg)](./img/Siglent_sdg1010_pcb_bottom.jpg "Siglent Sdg1010 Pcb Bottom"){ .glightbox data-gallery="siglent-sdg1010" }
<span class="caption">Siglent Sdg1010 Pcb Bottom</span>

[![Siglent Sdg1010 Analog 5166isz 3](./img/Siglent_sdg1010_analog_5166isz_3.jpg)](./img/Siglent_sdg1010_analog_5166isz_3.jpg "Siglent Sdg1010 Analog 5166isz 3"){ .glightbox data-gallery="siglent-sdg1010" }
<span class="caption">Siglent Sdg1010 Analog 5166isz 3</span>

[![Siglent Sdg1010 Screenshot](./img/Siglent_sdg1010_screenshot.jpg)](./img/Siglent_sdg1010_screenshot.jpg "Siglent Sdg1010 Screenshot"){ .glightbox data-gallery="siglent-sdg1010" }
<span class="caption">Siglent Sdg1010 Screenshot</span>

[![Siglent Sdg1010 Analog Pcb Topright](./img/Siglent_sdg1010_analog_pcb_topright.jpg)](./img/Siglent_sdg1010_analog_pcb_topright.jpg "Siglent Sdg1010 Analog Pcb Topright"){ .glightbox data-gallery="siglent-sdg1010" }
<span class="caption">Siglent Sdg1010 Analog Pcb Topright</span>

[![Siglent Sdg1010 Powersupply Ti Tl431ac](./img/Siglent_sdg1010_powersupply_ti_tl431ac.jpg)](./img/Siglent_sdg1010_powersupply_ti_tl431ac.jpg "Siglent Sdg1010 Powersupply Ti Tl431ac"){ .glightbox data-gallery="siglent-sdg1010" }
<span class="caption">Siglent Sdg1010 Powersupply Ti Tl431ac</span>

[![Siglent Sdg1010 Display Frontpanel Top](./img/Siglent_sdg1010_display_frontpanel_top.jpg)](./img/Siglent_sdg1010_display_frontpanel_top.jpg "Siglent Sdg1010 Display Frontpanel Top"){ .glightbox data-gallery="siglent-sdg1010" }
<span class="caption">Siglent Sdg1010 Display Frontpanel Top</span>

[![Siglent Sdg1010 Ao4405](./img/Siglent_sdg1010_ao4405.jpg)](./img/Siglent_sdg1010_ao4405.jpg "Siglent Sdg1010 Ao4405"){ .glightbox data-gallery="siglent-sdg1010" }
<span class="caption">Siglent Sdg1010 Ao4405</span>

[![Siglent Sdg1010 Analog Mic2941a](./img/Siglent_sdg1010_analog_mic2941a.jpg)](./img/Siglent_sdg1010_analog_mic2941a.jpg "Siglent Sdg1010 Analog Mic2941a"){ .glightbox data-gallery="siglent-sdg1010" }
<span class="caption">Siglent Sdg1010 Analog Mic2941a</span>

[![Siglent Sdg1010 Analog Ti 16z](./img/Siglent_sdg1010_analog_ti_16z.jpg)](./img/Siglent_sdg1010_analog_ti_16z.jpg "Siglent Sdg1010 Analog Ti 16z"){ .glightbox data-gallery="siglent-sdg1010" }
<span class="caption">Siglent Sdg1010 Analog Ti 16z</span>

[![Siglent Sdg1010 Analog Bnc](./img/Siglent_sdg1010_analog_bnc.jpg)](./img/Siglent_sdg1010_analog_bnc.jpg "Siglent Sdg1010 Analog Bnc"){ .glightbox data-gallery="siglent-sdg1010" }
<span class="caption">Siglent Sdg1010 Analog Bnc</span>

[![Siglent Sdg1010 Ti Ha04](./img/Siglent_sdg1010_ti_ha04.jpg)](./img/Siglent_sdg1010_ti_ha04.jpg "Siglent Sdg1010 Ti Ha04"){ .glightbox data-gallery="siglent-sdg1010" }
<span class="caption">Siglent Sdg1010 Ti Ha04</span>

[![Siglent Sdg1010 Device Powersupply Removed](./img/Siglent_sdg1010_device_powersupply_removed.jpg)](./img/Siglent_sdg1010_device_powersupply_removed.jpg "Siglent Sdg1010 Device Powersupply Removed"){ .glightbox data-gallery="siglent-sdg1010" }
<span class="caption">Siglent Sdg1010 Device Powersupply Removed</span>

[![Siglent Sdg1010 Device Backpanel Removed](./img/Siglent_sdg1010_device_backpanel_removed.jpg)](./img/Siglent_sdg1010_device_backpanel_removed.jpg "Siglent Sdg1010 Device Backpanel Removed"){ .glightbox data-gallery="siglent-sdg1010" }
<span class="caption">Siglent Sdg1010 Device Backpanel Removed</span>

[![Siglent Sdg1010 Device Open Bottom](./img/Siglent_sdg1010_device_open_bottom.jpg)](./img/Siglent_sdg1010_device_open_bottom.jpg "Siglent Sdg1010 Device Open Bottom"){ .glightbox data-gallery="siglent-sdg1010" }
<span class="caption">Siglent Sdg1010 Device Open Bottom</span>

[![Siglent Sdg1010 Display Frontpanel Keys](./img/Siglent_sdg1010_display_frontpanel_keys.jpg)](./img/Siglent_sdg1010_display_frontpanel_keys.jpg "Siglent Sdg1010 Display Frontpanel Keys"){ .glightbox data-gallery="siglent-sdg1010" }
<span class="caption">Siglent Sdg1010 Display Frontpanel Keys</span>

[![Siglent Sdg1010 Analog Pcb Topleft](./img/Siglent_sdg1010_analog_pcb_topleft.jpg)](./img/Siglent_sdg1010_analog_pcb_topleft.jpg "Siglent Sdg1010 Analog Pcb Topleft"){ .glightbox data-gallery="siglent-sdg1010" }
<span class="caption">Siglent Sdg1010 Analog Pcb Topleft</span>

[![Siglent Sdg1010 Beeper](./img/Siglent_sdg1010_beeper.jpg)](./img/Siglent_sdg1010_beeper.jpg "Siglent Sdg1010 Beeper"){ .glightbox data-gallery="siglent-sdg1010" }
<span class="caption">Siglent Sdg1010 Beeper</span>

[![Siglent Sdg1010 Version Info](./img/Siglent_sdg1010_version_info.jpg)](./img/Siglent_sdg1010_version_info.jpg "Siglent Sdg1010 Version Info"){ .glightbox data-gallery="siglent-sdg1010" }
<span class="caption">Siglent Sdg1010 Version Info</span>

[![Siglent Sdg1010 Ti Lc244a](./img/Siglent_sdg1010_ti_lc244a.jpg)](./img/Siglent_sdg1010_ti_lc244a.jpg "Siglent Sdg1010 Ti Lc244a"){ .glightbox data-gallery="siglent-sdg1010" }
<span class="caption">Siglent Sdg1010 Ti Lc244a</span>

[![Siglent Sdg1010 Display Frontpanel Bottom](./img/Siglent_sdg1010_display_frontpanel_bottom.jpg)](./img/Siglent_sdg1010_display_frontpanel_bottom.jpg "Siglent Sdg1010 Display Frontpanel Bottom"){ .glightbox data-gallery="siglent-sdg1010" }
<span class="caption">Siglent Sdg1010 Display Frontpanel Bottom</span>

[![Siglent Sdg1010 Spansion S29gl064n90tfio4](./img/Siglent_sdg1010_spansion_s29gl064n90tfio4.jpg)](./img/Siglent_sdg1010_spansion_s29gl064n90tfio4.jpg "Siglent Sdg1010 Spansion S29gl064n90tfio4"){ .glightbox data-gallery="siglent-sdg1010" }
<span class="caption">Siglent Sdg1010 Spansion S29gl064n90tfio4</span>

[![Siglent Sdg1010 Device Backplastic Removed](./img/Siglent_sdg1010_device_backplastic_removed.jpg)](./img/Siglent_sdg1010_device_backplastic_removed.jpg "Siglent Sdg1010 Device Backplastic Removed"){ .glightbox data-gallery="siglent-sdg1010" }
<span class="caption">Siglent Sdg1010 Device Backplastic Removed</span>

[![Siglent Sdg1010 Analog Ti D85801](./img/Siglent_sdg1010_analog_ti_d85801.jpg)](./img/Siglent_sdg1010_analog_ti_d85801.jpg "Siglent Sdg1010 Analog Ti D85801"){ .glightbox data-gallery="siglent-sdg1010" }
<span class="caption">Siglent Sdg1010 Analog Ti D85801</span>

[![Siglent Sdg1010 Analog I 28210 2](./img/Siglent_sdg1010_analog_i_28210_2.jpg)](./img/Siglent_sdg1010_analog_i_28210_2.jpg "Siglent Sdg1010 Analog I 28210 2"){ .glightbox data-gallery="siglent-sdg1010" }
<span class="caption">Siglent Sdg1010 Analog I 28210 2</span>

[![Siglent Sdg1010 Analog On 7905ct](./img/Siglent_sdg1010_analog_on_7905ct.jpg)](./img/Siglent_sdg1010_analog_on_7905ct.jpg "Siglent Sdg1010 Analog On 7905ct"){ .glightbox data-gallery="siglent-sdg1010" }
<span class="caption">Siglent Sdg1010 Analog On 7905ct</span>

[![Siglent Sdg1010 Device Open Top](./img/Siglent_sdg1010_device_open_top.jpg)](./img/Siglent_sdg1010_device_open_top.jpg "Siglent Sdg1010 Device Open Top"){ .glightbox data-gallery="siglent-sdg1010" }
<span class="caption">Siglent Sdg1010 Device Open Top</span>

[![Siglent Sdg1010 Fpga Jtag](./img/Siglent_sdg1010_fpga_jtag.jpg)](./img/Siglent_sdg1010_fpga_jtag.jpg "Siglent Sdg1010 Fpga Jtag"){ .glightbox data-gallery="siglent-sdg1010" }
<span class="caption">Siglent Sdg1010 Fpga Jtag</span>

[![Siglent Sdg1010 Dsp Jtag Uart](./img/Siglent_sdg1010_dsp_jtag_uart.jpg)](./img/Siglent_sdg1010_dsp_jtag_uart.jpg "Siglent Sdg1010 Dsp Jtag Uart"){ .glightbox data-gallery="siglent-sdg1010" }
<span class="caption">Siglent Sdg1010 Dsp Jtag Uart</span>

[![Siglent Sdg1010 Analog Ti Tl072c I 28210](./img/Siglent_sdg1010_analog_ti_tl072c_i_28210.jpg)](./img/Siglent_sdg1010_analog_ti_tl072c_i_28210.jpg "Siglent Sdg1010 Analog Ti Tl072c I 28210"){ .glightbox data-gallery="siglent-sdg1010" }
<span class="caption">Siglent Sdg1010 Analog Ti Tl072c I 28210</span>

[![Siglent Sdg1010 Analog Cosmo Y214s](./img/Siglent_sdg1010_analog_cosmo_y214s.jpg)](./img/Siglent_sdg1010_analog_cosmo_y214s.jpg "Siglent Sdg1010 Analog Cosmo Y214s"){ .glightbox data-gallery="siglent-sdg1010" }
<span class="caption">Siglent Sdg1010 Analog Cosmo Y214s</span>

[![Siglent Sdg1010 Package Contents](./img/Siglent_sdg1010_package_contents.jpg)](./img/Siglent_sdg1010_package_contents.jpg "Siglent Sdg1010 Package Contents"){ .glightbox data-gallery="siglent-sdg1010" }
<span class="caption">Siglent Sdg1010 Package Contents</span>

[![Siglent Sdg1010 Analog 5166isz 5](./img/Siglent_sdg1010_analog_5166isz_5.jpg)](./img/Siglent_sdg1010_analog_5166isz_5.jpg "Siglent Sdg1010 Analog 5166isz 5"){ .glightbox data-gallery="siglent-sdg1010" }
<span class="caption">Siglent Sdg1010 Analog 5166isz 5</span>

[![Siglent Sdg1010 Pcb Version](./img/Siglent_sdg1010_pcb_version.jpg)](./img/Siglent_sdg1010_pcb_version.jpg "Siglent Sdg1010 Pcb Version"){ .glightbox data-gallery="siglent-sdg1010" }
<span class="caption">Siglent Sdg1010 Pcb Version</span>

[![Siglent Sdg1010 Backpanel Top](./img/Siglent_sdg1010_backpanel_top.jpg)](./img/Siglent_sdg1010_backpanel_top.jpg "Siglent Sdg1010 Backpanel Top"){ .glightbox data-gallery="siglent-sdg1010" }
<span class="caption">Siglent Sdg1010 Backpanel Top</span>

[![Siglent Sdg1010 Crystal Shx25000](./img/Siglent_sdg1010_crystal_shx25000.jpg)](./img/Siglent_sdg1010_crystal_shx25000.jpg "Siglent Sdg1010 Crystal Shx25000"){ .glightbox data-gallery="siglent-sdg1010" }
<span class="caption">Siglent Sdg1010 Crystal Shx25000</span>

[![Siglent Sdg1010 Display Frontpanel Removed](./img/Siglent_sdg1010_display_frontpanel_removed.jpg)](./img/Siglent_sdg1010_display_frontpanel_removed.jpg "Siglent Sdg1010 Display Frontpanel Removed"){ .glightbox data-gallery="siglent-sdg1010" }
<span class="caption">Siglent Sdg1010 Display Frontpanel Removed</span>

[![Siglent Sdg1010 Display Frontpanel Usb Top](./img/Siglent_sdg1010_display_frontpanel_usb_top.jpg)](./img/Siglent_sdg1010_display_frontpanel_usb_top.jpg "Siglent Sdg1010 Display Frontpanel Usb Top"){ .glightbox data-gallery="siglent-sdg1010" }
<span class="caption">Siglent Sdg1010 Display Frontpanel Usb Top</span>

[![Siglent Sdg1010 Analog I 28210 1](./img/Siglent_sdg1010_analog_i_28210_1.jpg)](./img/Siglent_sdg1010_analog_i_28210_1.jpg "Siglent Sdg1010 Analog I 28210 1"){ .glightbox data-gallery="siglent-sdg1010" }
<span class="caption">Siglent Sdg1010 Analog I 28210 1</span>

[![Siglent Sdg1010 Display Frontpanel Hc393](./img/Siglent_sdg1010_display_frontpanel_hc393.jpg)](./img/Siglent_sdg1010_display_frontpanel_hc393.jpg "Siglent Sdg1010 Display Frontpanel Hc393"){ .glightbox data-gallery="siglent-sdg1010" }
<span class="caption">Siglent Sdg1010 Display Frontpanel Hc393</span>

[![Siglent Sdg1010 Analog 5166isz 1](./img/Siglent_sdg1010_analog_5166isz_1.jpg)](./img/Siglent_sdg1010_analog_5166isz_1.jpg "Siglent Sdg1010 Analog 5166isz 1"){ .glightbox data-gallery="siglent-sdg1010" }
<span class="caption">Siglent Sdg1010 Analog 5166isz 1</span>

[![Siglent Sdg1010 Powersupply Rubycon Cap1](./img/Siglent_sdg1010_powersupply_rubycon_cap1.jpg)](./img/Siglent_sdg1010_powersupply_rubycon_cap1.jpg "Siglent Sdg1010 Powersupply Rubycon Cap1"){ .glightbox data-gallery="siglent-sdg1010" }
<span class="caption">Siglent Sdg1010 Powersupply Rubycon Cap1</span>

[![Siglent Sdg1010 Dsprun](./img/Siglent_sdg1010_dsprun.jpg)](./img/Siglent_sdg1010_dsprun.jpg "Siglent Sdg1010 Dsprun"){ .glightbox data-gallery="siglent-sdg1010" }
<span class="caption">Siglent Sdg1010 Dsprun</span>

[![Siglent Sdg1010 Device Top](./img/Siglent_sdg1010_device_top.jpg)](./img/Siglent_sdg1010_device_top.jpg "Siglent Sdg1010 Device Top"){ .glightbox data-gallery="siglent-sdg1010" }
<span class="caption">Siglent Sdg1010 Device Top</span>

[![Siglent Sdg1010 Hynix H57v1262gtr](./img/Siglent_sdg1010_hynix_h57v1262gtr.jpg)](./img/Siglent_sdg1010_hynix_h57v1262gtr.jpg "Siglent Sdg1010 Hynix H57v1262gtr"){ .glightbox data-gallery="siglent-sdg1010" }
<span class="caption">Siglent Sdg1010 Hynix H57v1262gtr</span>

[![Siglent Sdg1010 Xilinx Spartan6 Xc6slx9](./img/Siglent_sdg1010_xilinx_spartan6_xc6slx9.jpg)](./img/Siglent_sdg1010_xilinx_spartan6_xc6slx9.jpg "Siglent Sdg1010 Xilinx Spartan6 Xc6slx9"){ .glightbox data-gallery="siglent-sdg1010" }
<span class="caption">Siglent Sdg1010 Xilinx Spartan6 Xc6slx9</span>

[![Siglent Sdg1010 Analog Ti Tl072c Nxp 74hc4051d I 28210](./img/Siglent_sdg1010_analog_ti_tl072c_nxp_74hc4051d_i_28210.jpg)](./img/Siglent_sdg1010_analog_ti_tl072c_nxp_74hc4051d_i_28210.jpg "Siglent Sdg1010 Analog Ti Tl072c Nxp 74hc4051d I 28210"){ .glightbox data-gallery="siglent-sdg1010" }
<span class="caption">Siglent Sdg1010 Analog Ti Tl072c Nxp 74hc4051d I 28210</span>

[![Siglent Sdg1010 Powersupply Pcb Version](./img/Siglent_sdg1010_powersupply_pcb_version.jpg)](./img/Siglent_sdg1010_powersupply_pcb_version.jpg "Siglent Sdg1010 Powersupply Pcb Version"){ .glightbox data-gallery="siglent-sdg1010" }
<span class="caption">Siglent Sdg1010 Powersupply Pcb Version</span>

[![Siglent Sdg1010 Display Frontpanel Hc595](./img/Siglent_sdg1010_display_frontpanel_hc595.jpg)](./img/Siglent_sdg1010_display_frontpanel_hc595.jpg "Siglent Sdg1010 Display Frontpanel Hc595"){ .glightbox data-gallery="siglent-sdg1010" }
<span class="caption">Siglent Sdg1010 Display Frontpanel Hc595</span>

[![Siglent Sdg1010 Start Screen](./img/Siglent_sdg1010_start_screen.jpg)](./img/Siglent_sdg1010_start_screen.jpg "Siglent Sdg1010 Start Screen"){ .glightbox data-gallery="siglent-sdg1010" }
<span class="caption">Siglent Sdg1010 Start Screen</span>

[![Siglent Sdg1010 Powersupply 28 8003 00r](./img/Siglent_sdg1010_powersupply_28-8003-00r.jpg)](./img/Siglent_sdg1010_powersupply_28-8003-00r.jpg "Siglent Sdg1010 Powersupply 28 8003 00r"){ .glightbox data-gallery="siglent-sdg1010" }
<span class="caption">Siglent Sdg1010 Powersupply 28 8003 00r</span>

[![Siglent Sdg1010 Powersupply Heatsink](./img/Siglent_sdg1010_powersupply_heatsink.jpg)](./img/Siglent_sdg1010_powersupply_heatsink.jpg "Siglent Sdg1010 Powersupply Heatsink"){ .glightbox data-gallery="siglent-sdg1010" }
<span class="caption">Siglent Sdg1010 Powersupply Heatsink</span>

[![Siglent Sdg1010 Powersupply Powerbutton](./img/Siglent_sdg1010_powersupply_powerbutton.jpg)](./img/Siglent_sdg1010_powersupply_powerbutton.jpg "Siglent Sdg1010 Powersupply Powerbutton"){ .glightbox data-gallery="siglent-sdg1010" }
<span class="caption">Siglent Sdg1010 Powersupply Powerbutton</span>

[![Siglent Sdg1010 Display Back](./img/Siglent_sdg1010_display_back.jpg)](./img/Siglent_sdg1010_display_back.jpg "Siglent Sdg1010 Display Back"){ .glightbox data-gallery="siglent-sdg1010" }
<span class="caption">Siglent Sdg1010 Display Back</span>

[![Siglent Sdg1010 Powersupply Sharp Pc817](./img/Siglent_sdg1010_powersupply_sharp_pc817.jpg)](./img/Siglent_sdg1010_powersupply_sharp_pc817.jpg "Siglent Sdg1010 Powersupply Sharp Pc817"){ .glightbox data-gallery="siglent-sdg1010" }
<span class="caption">Siglent Sdg1010 Powersupply Sharp Pc817</span>

[![Siglent Sdg1010 Powersupply Rubycon Cap2](./img/Siglent_sdg1010_powersupply_rubycon_cap2.jpg)](./img/Siglent_sdg1010_powersupply_rubycon_cap2.jpg "Siglent Sdg1010 Powersupply Rubycon Cap2"){ .glightbox data-gallery="siglent-sdg1010" }
<span class="caption">Siglent Sdg1010 Powersupply Rubycon Cap2</span>

[![Siglent Sdg1010 Analog I 28210 3](./img/Siglent_sdg1010_analog_i_28210_3.jpg)](./img/Siglent_sdg1010_analog_i_28210_3.jpg "Siglent Sdg1010 Analog I 28210 3"){ .glightbox data-gallery="siglent-sdg1010" }
<span class="caption">Siglent Sdg1010 Analog I 28210 3</span>

[![Siglent Sdg1010 Backpanel Connectors](./img/Siglent_sdg1010_backpanel_connectors.jpg)](./img/Siglent_sdg1010_backpanel_connectors.jpg "Siglent Sdg1010 Backpanel Connectors"){ .glightbox data-gallery="siglent-sdg1010" }
<span class="caption">Siglent Sdg1010 Backpanel Connectors</span>

[![Siglent Sdg1010 Backpanel Bottom](./img/Siglent_sdg1010_backpanel_bottom.jpg)](./img/Siglent_sdg1010_backpanel_bottom.jpg "Siglent Sdg1010 Backpanel Bottom"){ .glightbox data-gallery="siglent-sdg1010" }
<span class="caption">Siglent Sdg1010 Backpanel Bottom</span>

[![Siglent Sdg1010 Display Frontpanel Pcb1](./img/Siglent_sdg1010_display_frontpanel_pcb1.jpg)](./img/Siglent_sdg1010_display_frontpanel_pcb1.jpg "Siglent Sdg1010 Display Frontpanel Pcb1"){ .glightbox data-gallery="siglent-sdg1010" }
<span class="caption">Siglent Sdg1010 Display Frontpanel Pcb1</span>

[![Siglent Sdg1010 Analog Hc595](./img/Siglent_sdg1010_analog_hc595.jpg)](./img/Siglent_sdg1010_analog_hc595.jpg "Siglent Sdg1010 Analog Hc595"){ .glightbox data-gallery="siglent-sdg1010" }
<span class="caption">Siglent Sdg1010 Analog Hc595</span>

[![Siglent Sdg1010 Display Frontpanel Hc595 2](./img/Siglent_sdg1010_display_frontpanel_hc595_2.jpg)](./img/Siglent_sdg1010_display_frontpanel_hc595_2.jpg "Siglent Sdg1010 Display Frontpanel Hc595 2"){ .glightbox data-gallery="siglent-sdg1010" }
<span class="caption">Siglent Sdg1010 Display Frontpanel Hc595 2</span>

[![Siglent Sdg1010 Analog Devices Adsp Bf531](./img/Siglent_sdg1010_analog_devices_adsp_bf531.jpg)](./img/Siglent_sdg1010_analog_devices_adsp_bf531.jpg "Siglent Sdg1010 Analog Devices Adsp Bf531"){ .glightbox data-gallery="siglent-sdg1010" }
<span class="caption">Siglent Sdg1010 Analog Devices Adsp Bf531</span>

[![Siglent Sdg1010 Analog Pcb Bottomright](./img/Siglent_sdg1010_analog_pcb_bottomright.jpg)](./img/Siglent_sdg1010_analog_pcb_bottomright.jpg "Siglent Sdg1010 Analog Pcb Bottomright"){ .glightbox data-gallery="siglent-sdg1010" }
<span class="caption">Siglent Sdg1010 Analog Pcb Bottomright</span>

[![Siglent Sdg1010 Analog Bb Dac904e](./img/Siglent_sdg1010_analog_bb_dac904e.jpg)](./img/Siglent_sdg1010_analog_bb_dac904e.jpg "Siglent Sdg1010 Analog Bb Dac904e"){ .glightbox data-gallery="siglent-sdg1010" }
<span class="caption">Siglent Sdg1010 Analog Bb Dac904e</span>

[![Siglent Sdg1010 Powersupply Various Chips](./img/Siglent_sdg1010_powersupply_various_chips.jpg)](./img/Siglent_sdg1010_powersupply_various_chips.jpg "Siglent Sdg1010 Powersupply Various Chips"){ .glightbox data-gallery="siglent-sdg1010" }
<span class="caption">Siglent Sdg1010 Powersupply Various Chips</span>

[![Siglent Sdg1010 Analog Ti 13eep3k](./img/Siglent_sdg1010_analog_ti_13eep3k.jpg)](./img/Siglent_sdg1010_analog_ti_13eep3k.jpg "Siglent Sdg1010 Analog Ti 13eep3k"){ .glightbox data-gallery="siglent-sdg1010" }
<span class="caption">Siglent Sdg1010 Analog Ti 13eep3k</span>

[![Siglent Sdg1010 Display Connector](./img/Siglent_sdg1010_display_connector.jpg)](./img/Siglent_sdg1010_display_connector.jpg "Siglent Sdg1010 Display Connector"){ .glightbox data-gallery="siglent-sdg1010" }
<span class="caption">Siglent Sdg1010 Display Connector</span>

[![Siglent Sdg1010 Device Display Frontpanel Removed](./img/Siglent_sdg1010_device_display_frontpanel_removed.jpg)](./img/Siglent_sdg1010_device_display_frontpanel_removed.jpg "Siglent Sdg1010 Device Display Frontpanel Removed"){ .glightbox data-gallery="siglent-sdg1010" }
<span class="caption">Siglent Sdg1010 Device Display Frontpanel Removed</span>

[![Siglent Sdg1010 Ams1117](./img/Siglent_sdg1010_ams1117.jpg)](./img/Siglent_sdg1010_ams1117.jpg "Siglent Sdg1010 Ams1117"){ .glightbox data-gallery="siglent-sdg1010" }
<span class="caption">Siglent Sdg1010 Ams1117</span>

[![Siglent Sdg1010 Device Front 8116](./img/Siglent_sdg1010_device_front_8116.jpg)](./img/Siglent_sdg1010_device_front_8116.jpg "Siglent Sdg1010 Device Front 8116"){ .glightbox data-gallery="siglent-sdg1010" }
<span class="caption">Siglent Sdg1010 Device Front 8116</span>

[![Siglent Sdg1010 Display Frontpanel Empty](./img/Siglent_sdg1010_display_frontpanel_empty.jpg)](./img/Siglent_sdg1010_display_frontpanel_empty.jpg "Siglent Sdg1010 Display Frontpanel Empty"){ .glightbox data-gallery="siglent-sdg1010" }
<span class="caption">Siglent Sdg1010 Display Frontpanel Empty</span>

[![Siglent Sdg1010 Analog On A34 Ti 17h](./img/Siglent_sdg1010_analog_on_a34_ti_17h.jpg)](./img/Siglent_sdg1010_analog_on_a34_ti_17h.jpg "Siglent Sdg1010 Analog On A34 Ti 17h"){ .glightbox data-gallery="siglent-sdg1010" }
<span class="caption">Siglent Sdg1010 Analog On A34 Ti 17h</span>

[![Siglent Sdg1010 Display Frontpanel 74hc4051d](./img/Siglent_sdg1010_display_frontpanel_74hc4051d.jpg)](./img/Siglent_sdg1010_display_frontpanel_74hc4051d.jpg "Siglent Sdg1010 Display Frontpanel 74hc4051d"){ .glightbox data-gallery="siglent-sdg1010" }
<span class="caption">Siglent Sdg1010 Display Frontpanel 74hc4051d</span>

[![Siglent Sdg1010 Analog Lgaa](./img/Siglent_sdg1010_analog_lgaa.jpg)](./img/Siglent_sdg1010_analog_lgaa.jpg "Siglent Sdg1010 Analog Lgaa"){ .glightbox data-gallery="siglent-sdg1010" }
<span class="caption">Siglent Sdg1010 Analog Lgaa</span>

[![Siglent Sdg1010 Powersupply Coil](./img/Siglent_sdg1010_powersupply_coil.jpg)](./img/Siglent_sdg1010_powersupply_coil.jpg "Siglent Sdg1010 Powersupply Coil"){ .glightbox data-gallery="siglent-sdg1010" }
<span class="caption">Siglent Sdg1010 Powersupply Coil</span>

[![Siglent Sdg1010 Device Mainpcb Removed](./img/Siglent_sdg1010_device_mainpcb_removed.jpg)](./img/Siglent_sdg1010_device_mainpcb_removed.jpg "Siglent Sdg1010 Device Mainpcb Removed"){ .glightbox data-gallery="siglent-sdg1010" }
<span class="caption">Siglent Sdg1010 Device Mainpcb Removed</span>

[![Siglent Sdg1010 Display Frontpanel Usb Bottom](./img/Siglent_sdg1010_display_frontpanel_usb_bottom.jpg)](./img/Siglent_sdg1010_display_frontpanel_usb_bottom.jpg "Siglent Sdg1010 Display Frontpanel Usb Bottom"){ .glightbox data-gallery="siglent-sdg1010" }
<span class="caption">Siglent Sdg1010 Display Frontpanel Usb Bottom</span>

[![Siglent Sdg1010 Powersupply Nxp Tea1610t](./img/Siglent_sdg1010_powersupply_nxp_tea1610t.jpg)](./img/Siglent_sdg1010_powersupply_nxp_tea1610t.jpg "Siglent Sdg1010 Powersupply Nxp Tea1610t"){ .glightbox data-gallery="siglent-sdg1010" }
<span class="caption">Siglent Sdg1010 Powersupply Nxp Tea1610t</span>

[![Siglent Sdg1010 Isp13628d](./img/Siglent_sdg1010_isp13628d.jpg)](./img/Siglent_sdg1010_isp13628d.jpg "Siglent Sdg1010 Isp13628d"){ .glightbox data-gallery="siglent-sdg1010" }
<span class="caption">Siglent Sdg1010 Isp13628d</span>

[![Siglent Sdg1010 Ahc14](./img/Siglent_sdg1010_ahc14.jpg)](./img/Siglent_sdg1010_ahc14.jpg "Siglent Sdg1010 Ahc14"){ .glightbox data-gallery="siglent-sdg1010" }
<span class="caption">Siglent Sdg1010 Ahc14</span>

[![Siglent Sdg1010 Device Bottom](./img/Siglent_sdg1010_device_bottom.jpg)](./img/Siglent_sdg1010_device_bottom.jpg "Siglent Sdg1010 Device Bottom"){ .glightbox data-gallery="siglent-sdg1010" }
<span class="caption">Siglent Sdg1010 Device Bottom</span>

[![Siglent Sdg1010 Ti Hb125](./img/Siglent_sdg1010_ti_hb125.jpg)](./img/Siglent_sdg1010_ti_hb125.jpg "Siglent Sdg1010 Ti Hb125"){ .glightbox data-gallery="siglent-sdg1010" }
<span class="caption">Siglent Sdg1010 Ti Hb125</span>

[![Siglent Sdg1010 Analog 5166isz 2](./img/Siglent_sdg1010_analog_5166isz_2.jpg)](./img/Siglent_sdg1010_analog_5166isz_2.jpg "Siglent Sdg1010 Analog 5166isz 2"){ .glightbox data-gallery="siglent-sdg1010" }
<span class="caption">Siglent Sdg1010 Analog 5166isz 2</span>

[![Siglent Sdg1010 Powersupply Nt1795nl](./img/Siglent_sdg1010_powersupply_nt1795nl.jpg)](./img/Siglent_sdg1010_powersupply_nt1795nl.jpg "Siglent Sdg1010 Powersupply Nt1795nl"){ .glightbox data-gallery="siglent-sdg1010" }
<span class="caption">Siglent Sdg1010 Powersupply Nt1795nl</span>

[![Siglent Sdg1010 Analog Aub 1738](./img/Siglent_sdg1010_analog_aub_1738.jpg)](./img/Siglent_sdg1010_analog_aub_1738.jpg "Siglent Sdg1010 Analog Aub 1738"){ .glightbox data-gallery="siglent-sdg1010" }
<span class="caption">Siglent Sdg1010 Analog Aub 1738</span>

[![Siglent Sdg1010 Analog Pcb Bottomleft](./img/Siglent_sdg1010_analog_pcb_bottomleft.jpg)](./img/Siglent_sdg1010_analog_pcb_bottomleft.jpg "Siglent Sdg1010 Analog Pcb Bottomleft"){ .glightbox data-gallery="siglent-sdg1010" }
<span class="caption">Siglent Sdg1010 Analog Pcb Bottomleft</span>

[![Siglent Sdg1010 Backpanel Open](./img/Siglent_sdg1010_backpanel_open.jpg)](./img/Siglent_sdg1010_backpanel_open.jpg "Siglent Sdg1010 Backpanel Open"){ .glightbox data-gallery="siglent-sdg1010" }
<span class="caption">Siglent Sdg1010 Backpanel Open</span>

[![Siglent Sdg1010 Lattice Machxo Lcmxo640c](./img/Siglent_sdg1010_lattice_machxo_lcmxo640c.jpg)](./img/Siglent_sdg1010_lattice_machxo_lcmxo640c.jpg "Siglent Sdg1010 Lattice Machxo Lcmxo640c"){ .glightbox data-gallery="siglent-sdg1010" }
<span class="caption">Siglent Sdg1010 Lattice Machxo Lcmxo640c</span>

[![Siglent Sdg1010 Analog 5166isz 4](./img/Siglent_sdg1010_analog_5166isz_4.jpg)](./img/Siglent_sdg1010_analog_5166isz_4.jpg "Siglent Sdg1010 Analog 5166isz 4"){ .glightbox data-gallery="siglent-sdg1010" }
<span class="caption">Siglent Sdg1010 Analog 5166isz 4</span>

[![Siglent Sdg1010 Powersupply Pcb Bottom](./img/Siglent_sdg1010_powersupply_pcb_bottom.jpg)](./img/Siglent_sdg1010_powersupply_pcb_bottom.jpg "Siglent Sdg1010 Powersupply Pcb Bottom"){ .glightbox data-gallery="siglent-sdg1010" }
<span class="caption">Siglent Sdg1010 Powersupply Pcb Bottom</span>

[![Siglent Sdg1010 Powersupply Pcb Top](./img/Siglent_sdg1010_powersupply_pcb_top.jpg)](./img/Siglent_sdg1010_powersupply_pcb_top.jpg "Siglent Sdg1010 Powersupply Pcb Top"){ .glightbox data-gallery="siglent-sdg1010" }
<span class="caption">Siglent Sdg1010 Powersupply Pcb Top</span>

[![Siglent Sdg1010 Handle](./img/Siglent_sdg1010_handle.jpg)](./img/Siglent_sdg1010_handle.jpg "Siglent Sdg1010 Handle"){ .glightbox data-gallery="siglent-sdg1010" }
<span class="caption">Siglent Sdg1010 Handle</span>

[![Siglent Sdg1010 Analog On 7915ct](./img/Siglent_sdg1010_analog_on_7915ct.jpg)](./img/Siglent_sdg1010_analog_on_7915ct.jpg "Siglent Sdg1010 Analog On 7915ct"){ .glightbox data-gallery="siglent-sdg1010" }
<span class="caption">Siglent Sdg1010 Analog On 7915ct</span>

[![Siglent Sdg1010 Wab X1c](./img/Siglent_sdg1010_wab_x1c.jpg)](./img/Siglent_sdg1010_wab_x1c.jpg "Siglent Sdg1010 Wab X1c"){ .glightbox data-gallery="siglent-sdg1010" }
<span class="caption">Siglent Sdg1010 Wab X1c</span>

[![Siglent Sdg1010 Display Frontpanel Pcb2](./img/Siglent_sdg1010_display_frontpanel_pcb2.jpg)](./img/Siglent_sdg1010_display_frontpanel_pcb2.jpg "Siglent Sdg1010 Display Frontpanel Pcb2"){ .glightbox data-gallery="siglent-sdg1010" }
<span class="caption">Siglent Sdg1010 Display Frontpanel Pcb2</span>

[![Siglent Sdg1010 Analog Mic29302wu](./img/Siglent_sdg1010_analog_mic29302wu.jpg)](./img/Siglent_sdg1010_analog_mic29302wu.jpg "Siglent Sdg1010 Analog Mic29302wu"){ .glightbox data-gallery="siglent-sdg1010" }
<span class="caption">Siglent Sdg1010 Analog Mic29302wu</span>

[![Siglent Sdg1010 Powersupply Fuse](./img/Siglent_sdg1010_powersupply_fuse.jpg)](./img/Siglent_sdg1010_powersupply_fuse.jpg "Siglent Sdg1010 Powersupply Fuse"){ .glightbox data-gallery="siglent-sdg1010" }
<span class="caption">Siglent Sdg1010 Powersupply Fuse</span>

[![Siglent Sdg1010 Pcb Top](./img/Siglent_sdg1010_pcb_top.jpg)](./img/Siglent_sdg1010_pcb_top.jpg "Siglent Sdg1010 Pcb Top"){ .glightbox data-gallery="siglent-sdg1010" }
<span class="caption">Siglent Sdg1010 Pcb Top</span>

</div>
### Device

		- 
			[](./img/Siglent_sdg1010_package_contents.jpg)

		- 
			[](./img/Siglent_sdg1010_device_front_8116.jpg)

		- 
			[](./img/Siglent_sdg1010_start_screen.jpg)

		- 
			[](./img/Siglent_sdg1010_screenshot.jpg)

		- 
			[](./img/Siglent_sdg1010_version_info.jpg)

### Teardown

		- 
			[](./img/Siglent_sdg1010_device_top.jpg)

		- 
			[](./img/Siglent_sdg1010_device_bottom.jpg)

		- 
			[](./img/Siglent_sdg1010_device_backplastic_removed.jpg)

		- 
			[](./img/Siglent_sdg1010_handle.jpg)

		- 
			[](./img/Siglent_sdg1010_device_open_top.jpg)

		- 
			[](./img/Siglent_sdg1010_device_open_bottom.jpg)

		- 
			[](./img/Siglent_sdg1010_device_backpanel_removed.jpg)

		- 
			[](./img/Siglent_sdg1010_backpanel_open.jpg)

		- 
			[](./img/Siglent_sdg1010_backpanel_connectors.jpg)

		- 
			[](./img/Siglent_sdg1010_backpanel_pcb.jpg)

		- 
			[](./img/Siglent_sdg1010_backpanel_top.jpg)

		- 
			[](./img/Siglent_sdg1010_backpanel_bottom.jpg)

		- 
			[](./img/Siglent_sdg1010_device_mainpcb_removed.jpg)

		- 
			[](./img/Siglent_sdg1010_device_powersupply_removed.jpg)

		- 
			[](./img/Siglent_sdg1010_device_display_frontpanel_removed.jpg)

### Digital parts

		- 
			[](./img/Siglent_sdg1010_pcb_top.jpg)

		- 
			[](./img/Siglent_sdg1010_pcb_bottom.jpg)

		- 
			[](./img/Siglent_sdg1010_analog_devices_adsp_bf531.jpg)

		- 
			[](./img/Siglent_sdg1010_xilinx_spartan6_xc6slx9.jpg)

		- 
			[](./img/Siglent_sdg1010_lattice_machxo_lcmxo640c.jpg)

		- 
			[](./img/Siglent_sdg1010_spansion_s29gl064n90tfio4.jpg)

		- 
			[](./img/Siglent_sdg1010_hynix_h57v1262gtr.jpg)

		- 
			[](./img/Siglent_sdg1010_isp13628d.jpg)

		- 
			[](./img/Siglent_sdg1010_dsp_jtag_uart.jpg)

		- 
			[](./img/Siglent_sdg1010_fpga_jtag.jpg)

		- 
			[](./img/Siglent_sdg1010_cpld_conn_fpgarun.jpg)

		- 
			[](./img/Siglent_sdg1010_dsprun.jpg)

		- 
			[](./img/Siglent_sdg1010_ams1117.jpg)

		- 
			[](./img/Siglent_sdg1010_ahc14.jpg)

		- 
			[](./img/Siglent_sdg1010_ao4405.jpg)

		- 
			[](./img/Siglent_sdg1010_ti_ha04.jpg)

		- 
			[](./img/Siglent_sdg1010_ti_hb125.jpg)

		- 
			[](./img/Siglent_sdg1010_ti_lc244a.jpg)

		- 
			[](./img/Siglent_sdg1010_wab_x1c.jpg)

		- 
			[](./img/Siglent_sdg1010_beeper.jpg)

		- 
			[](./img/Siglent_sdg1010_crystal_shx25000.jpg)

		- 
			[](./img/Siglent_sdg1010_pcb_version.jpg)

### Analog parts

		- 
			[](./img/Siglent_sdg1010_analog_bnc.jpg)

		- 
			[](./img/Siglent_sdg1010_analog_pcb_topleft.jpg)

		- 
			[](./img/Siglent_sdg1010_analog_pcb_topright.jpg)

		- 
			[](./img/Siglent_sdg1010_analog_pcb_bottomleft.jpg)

		- 
			[](./img/Siglent_sdg1010_analog_pcb_bottomright.jpg)

		- 
			[](./img/Siglent_sdg1010_analog_bb_dac904e.jpg)

		- 
			[](./img/Siglent_sdg1010_analog_5166isz_1.jpg)

		- 
			[](./img/Siglent_sdg1010_analog_5166isz_2.jpg)

		- 
			[](./img/Siglent_sdg1010_analog_5166isz_3.jpg)

		- 
			[](./img/Siglent_sdg1010_analog_5166isz_4.jpg)

		- 
			[](./img/Siglent_sdg1010_analog_5166isz_5.jpg)

		- 
			[](./img/Siglent_sdg1010_analog_ad_ocmp_ti_13eep3k_5166isz.jpg)

		- 
			[](./img/Siglent_sdg1010_analog_aub_1738.jpg)

		- 
			[](./img/Siglent_sdg1010_analog_cosmo_y214s.jpg)

		- 
			[](./img/Siglent_sdg1010_analog_ft_b3g4a_5z.jpg)

		- 
			[](./img/Siglent_sdg1010_analog_hc595.jpg)

		- 
			[](./img/Siglent_sdg1010_analog_i_28210_1.jpg)

		- 
			[](./img/Siglent_sdg1010_analog_i_28210_2.jpg)

		- 
			[](./img/Siglent_sdg1010_analog_i_28210_3.jpg)

		- 
			[](./img/Siglent_sdg1010_analog_lgaa.jpg)

		- 
			[](./img/Siglent_sdg1010_analog_mic2941a.jpg)

		- 
			[](./img/Siglent_sdg1010_analog_mic29302wu.jpg)

		- 
			[](./img/Siglent_sdg1010_analog_on_7905ct.jpg)

		- 
			[](./img/Siglent_sdg1010_analog_on_7915ct.jpg)

		- 
			[](./img/Siglent_sdg1010_analog_on_a34_ti_17h.jpg)

		- 
			[](./img/Siglent_sdg1010_analog_ti_13eep3k.jpg)

		- 
			[](./img/Siglent_sdg1010_analog_ti_d85801.jpg)

		- 
			[](./img/Siglent_sdg1010_analog_ti_16z.jpg)

		- 
			[](./img/Siglent_sdg1010_analog_ti_tl072c_i_28210.jpg)

		- 
			[](./img/Siglent_sdg1010_analog_ti_tl072c_nxp_74hc4051d_i_28210.jpg)

### Display / frontpanel

		- 
			[](./img/Siglent_sdg1010_display_frontpanel_top.jpg)

		- 
			[](./img/Siglent_sdg1010_display_frontpanel_bottom.jpg)

		- 
			[](./img/Siglent_sdg1010_display_frontpanel_pcb1.jpg)

		- 
			[](./img/Siglent_sdg1010_display_frontpanel_pcb2.jpg)

		- 
			[](./img/Siglent_sdg1010_display_frontpanel_removed.jpg)

		- 
			[](./img/Siglent_sdg1010_display_connector.jpg)

		- 
			[](./img/Siglent_sdg1010_display_back.jpg)

		- 
			[](./img/Siglent_sdg1010_display_frontpanel_keys.jpg)

		- 
			[](./img/Siglent_sdg1010_display_frontpanel_empty.jpg)

		- 
			[](./img/Siglent_sdg1010_display_frontpanel_74hc4051d.jpg)

		- 
			[](./img/Siglent_sdg1010_display_frontpanel_hc393.jpg)

		- 
			[](./img/Siglent_sdg1010_display_frontpanel_hc595.jpg)

		- 
			[](./img/Siglent_sdg1010_display_frontpanel_hc595_2.jpg)

		- 
			[](./img/Siglent_sdg1010_display_frontpanel_usb_top.jpg)

		- 
			[](./img/Siglent_sdg1010_display_frontpanel_usb_bottom.jpg)

### Power supply

		- 
			[](./img/Siglent_sdg1010_powersupply_pcb_top.jpg)

		- 
			[](./img/Siglent_sdg1010_powersupply_pcb_bottom.jpg)

		- 
			[](./img/Siglent_sdg1010_powersupply_pcb_version.jpg)

		- 
			[](./img/Siglent_sdg1010_powersupply_nxp_tea1610t.jpg)

		- 
			[](./img/Siglent_sdg1010_powersupply_sharp_pc817.jpg)

		- 
			[](./img/Siglent_sdg1010_powersupply_ti_tl431ac.jpg)

		- 
			[](./img/Siglent_sdg1010_powersupply_various_chips.jpg)

		- 
			[](./img/Siglent_sdg1010_powersupply_powerbutton.jpg)

		- 
			[](./img/Siglent_sdg1010_powersupply_fuse.jpg)

		- 
			[](./img/Siglent_sdg1010_powersupply_rubycon_cap1.jpg)

		- 
			[](./img/Siglent_sdg1010_powersupply_rubycon_cap2.jpg)

		- 
			[](./img/Siglent_sdg1010_powersupply_coil.jpg)

		- 
			[](./img/Siglent_sdg1010_powersupply_heatsink.jpg)

		- 
			[](./img/Siglent_sdg1010_powersupply_28-8003-00r.jpg)

		- 
			[](./img/Siglent_sdg1010_powersupply_nt1795nl.jpg)

## Protocol

There are two possible PC connectivity methods that can be selected in the SDG1010 menu, which have different USB VID/PID pairs:

- "Raw USB" (this is what the vendor PC software uses): **f4ed:ee37**
- "USBTMC": **f4ed:ee3a**

Additionally, there are apparently [GPIB](https://sigrok.org/wiki/GPIB) and Ethernet options, but those are not available in the "standard" device. It's unclear if/where devices with those options can be bought, maybe only the rebranded LeCroy devices have them (?)

TODO: Details.
USBRAW connectivity is not possible on a Windows 8 platform, because of driver signature enforcement ([details](http://www.eevblog.com/forum/testgear/the-sdg1000-and-sdg800-thread/msg579096/#msg579096)). Additionally, there are no drivers provided by Siglent for platforms other than Windows. Obviously, USBTMC is the method to use for universal communication with this device.

See the [SDG1000 programming manual](https://www.box.com/s/e18ab37cfc290838d50d) for a protocol description.

A much better written manual is available for the LeCroy WaveStation series, which are rebadged Siglent generators. This manual is available on LeCroy's website, [here](http://cdn.teledynelecroy.com/files/manuals/wsta_scpi_manual_reva.pdf).

## Resources
- [EEVblog forums: Siglent SDG1025 Arbitrary/function generator under some tests](http://www.eevblog.com/forum/product-reviews-photos-and-discussion/siglent-sdg1025-arbitraryfunction-generator-under-some-tests/) (also has teardown photos)
- [EEVblog forums: Help choosing an ARB: New Siglent SDG1020 vs Used Fluke 281 / Wavetek 39A](http://www.eevblog.com/forum/product-reviews-photos-and-discussion/new-siglent-sdg1020-vs-used-fluke-281-wavetek-39a/)
- [EEVblog Forums: Siglent SDG1000 series thread, with a collection of resources including documentation, known issues, solutions and specifications](http://www.eevblog.com/forum/testgear/the-sdg1000-and-sdg800-thread/)

