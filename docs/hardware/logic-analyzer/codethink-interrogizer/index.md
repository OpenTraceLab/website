---
title: Codethink Interrogizer
---

# Codethink Interrogizer

<div class="infobox" markdown>

### Codethink Interrogizer

| | |
|---|---|
| **Status** | planned |
| **Channels** | 16 |
| **Samplerate** | 200kHz |
| **Samplerate (state)** | — |
| **Triggers** | — |
| **Min/max voltage** | 3.3V, some pins 5.0V tolerant |
| **Memory** | ? |
| **Compression** | no |
| **Website** | [gitlab.com](https://gitlab.com/CodethinkLabs/interrogizer) |

</div>

The **Codethink Interrogizer** is an Open Source logic analyzer, aiming at providing an affordable and easily producible tool to measure digital signals.

See [Codethink Interrogator/Info](/w/index.php?title=Codethink_Interrogator/Info&action=edit&redlink=1) for more details (such as **lsusb -v** output) about the device.

## Hardware
- STM32F072C8T6 (MCU, Cortex M0)
- ...

KiCAD schematics and firmware at [https://gitlab.com/CodethinkLabs/interrogizer](https://gitlab.com/CodethinkLabs/interrogizer)

vendor's sigrok driver at [https://gitlab.com/CodethinkLabs/interrogizer-libsigrok](https://gitlab.com/CodethinkLabs/interrogizer-libsigrok)

## Resources
- gitlab repos of the [device's project](https://gitlab.com/CodethinkLabs/interrogizer) and the [vendor's sigrok driver](https://gitlab.com/CodethinkLabs/interrogizer-libsigrok)
- [blog article](https://www.codethink.co.uk/articles/2020/introducing-interrogizer-providing-affordable-troubleshooting/) introducing the device

