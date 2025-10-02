---
title: ATORCH DL24MP-150W Purple
---

# ATORCH DL24MP-150W Purple

<div class="infobox" markdown>

![ATORCH DL24MP-150W Purple](./img/ATORCH_DL24MP-150W_Purple_Master_PCB_Bottom.jpg){ .infobox-image }

### ATORCH DL24MP-150W Purple

| | |
|---|---|
| **Status** | supported |
| **Source code** | [atorch](https://github.com/OpenTraceLab/OpenTraceCapture/tree/main/src/hardware/atorch) |
| **Channels** | 1 |
| **Voltage/current (CH1)** | 150W / 0.2-25A / 2-200V |
| **Connectivity** | serial over Bluetooth, BLE |
| **Features** | modular DC electronic load |
| **Website** | [en.atorch.cn](http://en.atorch.cn/ProDetail.aspx?ProID=12) |

</div>

The **ATORCH DL24MP-150W Purple** is a modular DC electronic load kit with serial connectivity over USB.

## General

The base kit contains a control panel, featuring a color display and 4 buttons, and a master power module, rated for 0.2~25A, 0~200V, max 150W.

Slave modules can be connected, each increasing the maximum power by 150W.

Each power module is cooled by a 8cm fan blowing air through 4 smalls heatsinks ( one per power mosfet )

Operation requires a 12V power supply ( 1A for the base kit, increasing with each add slave module ).

If offers 7 modes of operation&#160;:

- CC&#160;: Constant Current
- CV&#160;: Constant Voltage
- CR&#160;: Constant Resistance
- CP&#160;: Constant Power
- BRT&#160;: Determines the ESR of a battery
- PT&#160;: Determines the maximum power provided by a power supply
- CT&#160;: Determines the resistance of the wiring&#160;?
## Hardware
- **Power MOSFET** x4: [International Rectifier IRFP264N](https://www.irf.com/product-info/datasheets/data/irfp264n.pdf)
- **MCU**&#160;: HC32L170
- **Bluetooth IC**&#160;: Unidentified ( SOIC8, marking BP0Kxxx-28A2)
- **Power meter IC** x2&#160;: [HLW8110](http://www.hiliwi.com/product/49.html). Looks like the 2nd one might be used just as an ADC for the 2 temperature sensors.

The control panel PCB has an unpopulated socket that can be used to connect a rotary encoder and a push button, providing more practical controls.

## Protocol

The device communicates through serial-over-Bluetooth (RFCOMM), appearing under the DL24M_SPP name, and BLE, under the DL24M_BLE name. 
The same protocol is used both on the BLE and Bluetooth link.

See [ATORCH J7-c](https://sigrok.org/wiki/ATORCH_J7-c)

The following measurements are available through that protocol&#160;:

- Actual voltage
- Actual current
- Actual capacity ( in mAh, for battery capacity measurement )
- Actual energy (in Wh)
- External sensor temperature.

## Photos

<div class="photo-grid" markdown>

[![Atorch Dl24mp 150w Purple Master Pcb Bottom](./img/ATORCH_DL24MP-150W_Purple_Master_PCB_Bottom.jpg)](./img/ATORCH_DL24MP-150W_Purple_Master_PCB_Bottom.jpg "Atorch Dl24mp 150w Purple Master Pcb Bottom"){ .glightbox data-gallery="atorch-dl24mp-150w-purple" }
<span class="caption">Atorch Dl24mp 150w Purple Master Pcb Bottom</span>

[![Atorch Dl24mp 150w Purple Panel Pcb Bottom](./img/ATORCH_DL24MP-150W_Purple_Panel_PCB_Bottom.jpg)](./img/ATORCH_DL24MP-150W_Purple_Panel_PCB_Bottom.jpg "Atorch Dl24mp 150w Purple Panel Pcb Bottom"){ .glightbox data-gallery="atorch-dl24mp-150w-purple" }
<span class="caption">Atorch Dl24mp 150w Purple Panel Pcb Bottom</span>

[![Atorch Dl24mp 150w Purple Picture](./img/ATORCH_DL24MP-150W_Purple_Picture.jpg)](./img/ATORCH_DL24MP-150W_Purple_Picture.jpg "Atorch Dl24mp 150w Purple Picture"){ .glightbox data-gallery="atorch-dl24mp-150w-purple" }
<span class="caption">Atorch Dl24mp 150w Purple Picture</span>

[![Atorch Dl24mp 150w Purple Master Pcb Top Control Section](./img/ATORCH_DL24MP-150W_Purple_Master_PCB_Top_Control_Section.jpg)](./img/ATORCH_DL24MP-150W_Purple_Master_PCB_Top_Control_Section.jpg "Atorch Dl24mp 150w Purple Master Pcb Top Control Section"){ .glightbox data-gallery="atorch-dl24mp-150w-purple" }
<span class="caption">Atorch Dl24mp 150w Purple Master Pcb Top Control Section</span>

[![Atorch Dl24mp 150w Purple Panel Pcb Top](./img/ATORCH_DL24MP-150W_Purple_Panel_PCB_Top.jpg)](./img/ATORCH_DL24MP-150W_Purple_Panel_PCB_Top.jpg "Atorch Dl24mp 150w Purple Panel Pcb Top"){ .glightbox data-gallery="atorch-dl24mp-150w-purple" }
<span class="caption">Atorch Dl24mp 150w Purple Panel Pcb Top</span>

</div>

