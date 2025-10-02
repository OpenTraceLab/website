---
title: SUMP compatibles
---

# SUMP compatibles

<div class="infobox" markdown>

![SUMP compatibles](./img/Sigrok_logo_no_text_transparent_512.png){ .infobox-image }

### SUMP compatibles

| | |
|---|---|
| **Status** | supported |
| **Source code** | [openbench-logic-sniffer](https://github.com/OpenTraceLab/OpenTraceCapture/tree/main/src/hardware/openbench-logic-sniffer) |
| **Channels** | ? |
| **Samplerate** | ? |
| **Samplerate (state)** | ? |
| **Triggers** | ? |
| **Min/max voltage** | ? |
| **Memory** | ? |
| **Compression** | ? |
| **Website** | [sump.org](http://www.sump.org/projects/analyzer/protocol/) |

</div>

The **SUMP protocol** is a means to acquire logic data and download the samples from the acquisition device to the host. Physical transports can be UART or USB (stream of bytes over a serial connection). Several acquisition devices implement the SUMP protocol, and there are several host side SUMP clients. Up to 32 channels are supported, and sample rates in the 60MHz range were seen. The acquisition data goes to local sample memory before transmission to the host after the acquisition is complete (non-streaming operation).

See the [sump.org](http://www.sump.org/projects/analyzer/protocol/) documentation for details.

## SUMP compatible devices

Here is a list of devices which the sigrok project is aware of.

- [ Openbench Logic Sniffer](https://sigrok.org/wiki/Openbench_Logic_Sniffer)
- [ Saanlima Pipistrello OLS](https://sigrok.org/wiki/Saanlima_Pipistrello_OLS)
- [ Dangerous Prototypes Buspirate](https://sigrok.org/wiki/Dangerous_Prototypes_Buspirate)
- [ Dangerous Prototypes USB IR Toy](https://sigrok.org/wiki/Dangerous_Prototypes_USB_IR_Toy)
- [ Logic Shrimp](https://sigrok.org/wiki/Logic_Shrimp)
- [AGLA](https://github.com/gillham/logic_analyzer)
- [ JTAGulator](https://sigrok.org/wiki/JTAGulator)
### AGLA

AGLA is an Arduino sketch which implements the SUMP protocol. The software supports ATmega168, ATmega328, and ATmega2560 MCUs. Channel count is 5 (or is it 6?). Samplerates are 4MHz or below (depending on the MCU). Sample memory depth is 532 to 7168 (depending on the MCU), compression is not supported. Triggers may be supported at lower rates.

There are a lot of details in the [Arduino](https://sigrok.org/wiki/Arduino) page though much of it feels out of place for the sigrok project.

### JTAGulator

The JTAGulator supports a [Logic Analyzer mode](https://github.com/grandideastudio/jtagulator/wiki/Logic-Analyzer) which implements the SUMP protocol and thus transparently is covered by the sigrok **ols** driver. This LA mode gets enabled/disabled manually, then is persisted in the device across power cycles.

Channel count is 24, sample rate is 1.2MSa/s, memory depth is 1024Sa. Low/high level triggers are supported. Target voltage levels are adjustable.

**TODO** Add more sections on compatibles which don't have their own page. Or add few details here as an overview and link to a page with more details. Though the bove list of devices has the links ... Or setup a table instead of individual subsections, for easier comparison.

## Resources

## Photos

<div class="photo-grid" markdown>

[![Sigrok Logo No Text Transparent 512](./img/Sigrok_logo_no_text_transparent_512.png)](./img/Sigrok_logo_no_text_transparent_512.png "Sigrok Logo No Text Transparent 512"){ .glightbox data-gallery="sump-compatibles" }
<span class="caption">Sigrok Logo No Text Transparent 512</span>

</div>
