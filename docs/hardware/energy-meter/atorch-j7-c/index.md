---
title: ATORCH_J7-c
---

# ATORCH_J7-c

<div class="infobox" markdown>

![ATORCH_J7-c](./img/ATORCH_J7-c.jpg){ .infobox-image }

### ATORCH_J7-c

| | |
|---|---|
| **Status** | supported |
| **Source code** | [atorch](https://github.com/OpenTraceLab/OpenTraceCapture/tree/main/src/hardware/atorch) |
| **Connectivity** | serial over Bluetooth, BLE |
| **Measurements** | voltage, current, power, energy, voltage over USB data lines |
| **Features** | measures USB devices; color display |
| **Website** | [en.atorch.cn](http://en.atorch.cn/ProDetail.aspx?ProID=4) |

</div>

The **ATORCH J7-c** is a USB load meter which can measure various properties for USB devices including their voltage, current, power, resistance, capacity, temperature, data line voltage, and charging mode. Communicates to the host by means of serial over bluetooth.

## Hardware

It features the following connectors&#160;: 

- USB-A male ( USB 2.0 only )
- USB-A female ( USB 2.0 only)
- USB-C male
- USB-C female
- USB-microB female

A **CH573F MCU** is responsible for performing all the measurements and managing the user interface.

A small SOIC-8 IC (marking BP0D608-68A2) handles the Bluetooth communication (both RFCOMM and BLE). Might be [AC6328B](https://www.zh-jieli.com/upload/202204/AC63XN-datasheet/AC632N%E8%A7%84%E6%A0%BC%E4%B9%A6/datasheet/AC6328B_Datasheet_V1.0.pdf)

## Pictures

		- 
			[](./img/ATORCH_J7-c_Board_Front.jpg)

Top side of the board

		- 
			[](./img/ATORCH_J7-c_Board_Back.jpg)

Bottom side of the board

## Example use

```
 $ sigrok-cli -d atorch:conn=COM5 --continuous
 $ sigrok-cli -d atorch:conn=bt/ac6328/12-34-56-78-9a-bc --show

```

## Protocol

The device communicates through serial-over-Bluetooth (RFCOMM), appearing under the UC96_SPP name, and BLE, under the UC96_BLE name. 
The same protocol is used both on the BLE and Bluetooth link.

The manufacturer provides an app named "E_Test" for Android and iOS, but no protocol documentation, although it appears that the protocol has been fully reverse-engineered [[1]](https://github.com/syssi/esphome-atorch-dl24/blob/main/docs/protocol-design.md).

The RFCOMM transport uses channel number 2.
The BLE transport can be made to work using the following parameters&#160;: handle_rx = 0x000C, handle_tx = 0x000F, handle_cccd = 0x000D, value_cccd = 0x0001 

## Resources
- vendor software in the [Aliexpress store](http://atorch.aliexpress.com/)
- github syssi esphome-atorch-dl24 [protocol-design](https://github.com/syssi/esphome-atorch-dl24/blob/main/docs/protocol-design.md) text document

## Photos

<div class="photo-grid" markdown>

[![Atorch J7 C](./img/ATORCH_J7-c.jpg)](./img/ATORCH_J7-c.jpg "Atorch J7 C"){ .glightbox data-gallery="atorch_j7-c" }
<span class="caption">Atorch J7 C</span>

[![Atorch J7 C Board Back](./img/ATORCH_J7-c_Board_Back.jpg)](./img/ATORCH_J7-c_Board_Back.jpg "Atorch J7 C Board Back"){ .glightbox data-gallery="atorch_j7-c" }
<span class="caption">Atorch J7 C Board Back</span>

[![Atorch J7 C Board Front](./img/ATORCH_J7-c_Board_Front.jpg)](./img/ATORCH_J7-c_Board_Front.jpg "Atorch J7 C Board Front"){ .glightbox data-gallery="atorch_j7-c" }
<span class="caption">Atorch J7 C Board Front</span>

</div>
