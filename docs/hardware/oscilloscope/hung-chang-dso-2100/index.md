---
title: Hung-Chang DSO-2100
---

# Hung-Chang DSO-2100

<div class="infobox" markdown>

![Hung-Chang DSO-2100](./img/HungChang_DSO2100_PCB_bottom.jpg){ .infobox-image }

### Hung-Chang DSO-2100

| | |
|---|---|
| **Status** | supported |
| **Source code** | [hung-chang-dso-2100](https://github.com/OpenTraceLab/OpenTraceCapture/tree/main/src/hardware/hung-chang-dso-2100) |
| **Channels** | 2 (not simultaneously) |
| **Samplerate** | 100MSa/s |
| **Analog bandwidth** | 30MHz |
| **Vertical resolution** | 8bits |
| **Triggers** | edge, composite video |
| **Input impedance** | 1MΩ‖25pF |
| **Memory** | 10240pts |
| **Display** | none |
| **Connectivity** | parallel port |
| **Features** | vertical sensitivity: 10mV/div - 5V/div |

</div>

The [Hung-Chang DSO-2100](https://web.archive.org/web/20090130044125/http://hcqelectronic.com/osci1/pc.htm) is a 30MHz analog bandwidth 100MS/s parallel port oscilloscope that has been sold under the brand names Protek and Voltcraft. It is not related to the [Hantek DSO-2100USB](https://web.archive.org/web/20131103141209/http://www.hantek.com/en/ProductDetail_133.html) or the [Link Instruments DSO-2100](https://web.archive.org/web/20010803015816/http://www.linkinstruments.com/oscilloscope21.htm) families.

## Hardware
- QuickLogic QL2003 pASIC 2 non-volatile FPGA
- Analog Devices ADSP-2105 microcontroller at 12.5MHz
- 2x ISSI IS61C256AH-10J 32kB SRAM
- 2x Harris (Intersil) HI5714/6CB ADC

The hardware does not allow to sample both channels at the same time as the ADCs are always connected to the same signal. There are a lot of [design flaws](https://web.archive.org/web/20080122084413/http://freenet-homepage.de/kritikus/clicliclic/dso2100h.html) making accurate measurements with this device nearly impossible.

The FPGA handles the low level parallel port protocol so that the microcontroller can interact with the PC using a single byte mailbox in its address space. Samples from SRAM or the ADCs are passed on to the PC by the FPGA without the microcontroller being involved. It also generates the phase shifted sampling clocks from the 50MHz oscillator and increments the SRAM address to take 10240 samples when it detects the correct edge on its trigger input. There is no way to take more samples than that on an event. Most of the 64kB SRAM stays unused.

While the microcontroller is sold as a DSP, its purpose in this device is to handle the state machine that receives the configuration parameters from the PC and to put the FPGA into the requested state. It is also used to copy samples between different regions of the SRAM. Its firmware is ~1000 instructions and can be disassembled using [DEADSP](https://web.archive.org/web/20050901010556/http://www.dce.bg/~vladitx/adsp2181/index.html). It shows that there are indeed no more commands than those listed on the page linked below.

In 2012 it was still possible to request the schematics from [Conrad Electronic](http://www.conrad.com) as it was sold there with the product number 129208 back in 1999. They will send it on an A3 sheet by snail mail. The schematics are of bad quality with barely readable numbers, missing values, missing or wrong units (i.e. 12KF resistors), and blatant errors (op-amps with positive and negative input connected). It also doesn't tell you that some parts have not been populated. The AX1027 resistor array is (P1) - 70Ω - (P2) - 150Ω - (P3) - 75Ω - (P4) - 45Ω - (P5) - 30Ω - (P6).

## Photos

<div class="photo-grid" markdown>

[![Hungchang Dso2100 Pcb Bottom](./img/HungChang_DSO2100_PCB_bottom.jpg)](./img/HungChang_DSO2100_PCB_bottom.jpg "Hungchang Dso2100 Pcb Bottom"){ .glightbox data-gallery="hung-chang-dso-2100" }
<span class="caption">Hungchang Dso2100 Pcb Bottom</span>

[![Hung Chang Dso 2100 Mugshot](./img/Hung_chang_dso_2100_mugshot.png)](./img/Hung_chang_dso_2100_mugshot.png "Hung Chang Dso 2100 Mugshot"){ .glightbox data-gallery="hung-chang-dso-2100" }
<span class="caption">Hung Chang Dso 2100 Mugshot</span>

[![Hungchang Dso2100 Pcb Top](./img/HungChang_DSO2100_PCB_top.jpg)](./img/HungChang_DSO2100_PCB_top.jpg "Hungchang Dso2100 Pcb Top"){ .glightbox data-gallery="hung-chang-dso-2100" }
<span class="caption">Hungchang Dso2100 Pcb Top</span>

[![Hungchang Dso2100 Bottom](./img/HungChang_DSO2100_bottom.jpg)](./img/HungChang_DSO2100_bottom.jpg "Hungchang Dso2100 Bottom"){ .glightbox data-gallery="hung-chang-dso-2100" }
<span class="caption">Hungchang Dso2100 Bottom</span>

[![Hungchang Dso2100](./img/HungChang_DSO2100.jpg)](./img/HungChang_DSO2100.jpg "Hungchang Dso2100"){ .glightbox data-gallery="hung-chang-dso-2100" }
<span class="caption">Hungchang Dso2100</span>

</div>
## Protocol

See [here](https://web.archive.org/web/20090317091949/http://freenet-homepage.de/kritikus/clicliclic/dso2100.html) for more info in the protocol.

## Resources
- [Manual](http://produktinfo.conrad.com/datenblaetter/125000-149999/129208-an-01-en-Digi_Speicheroszilloskop_DSO_2100.pdf)

