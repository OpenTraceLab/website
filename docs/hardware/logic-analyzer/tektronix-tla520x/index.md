---
title: Tektronix TLA520X
---

# Tektronix TLA520X

<div class="infobox" markdown>

![Tektronix TLA520X](./img/Tektronix_TLA5204_1000.png){ .infobox-image }

### Tektronix TLA520X

| | |
|---|---|
| **Status** | planned |
| **Channels** | 32/64/96/128 |
| **Samplerate** | Asynchronous 2Ghz @ 32/64/96/128ch, MagniVu 8Ghz @ 32/64/96/128ch |
| **Samplerate (state)** | Synchronous (state) 235MHz @ 32/64/96/128ch |
| **Triggers** | complex trigger state machine @ 32/64/96/128CH |
| **Min/max voltage** | -3.5V — 6.5V continuous |
| **Threshold voltage** | Configurable: -2V — 4.5V |
| **Memory** | 1MB,2MB,4MB,16MB,32MB (16K MagniVu high speed buffer) |
| **Compression** | None |
| **Website** | [tla5200 series logic analyzers](https://www.tek.com/tla5201-manual/tla5200-series) |

</div>

The **Tektronix TLA520X** series logic analyzer is a networked, 32/64/96/128-channel logic analyzer with up to 2Ghz Asynchronous, 8Ghz memory-limited glitch detection, 235Mhz synchronous sample rate

TLA5201/TLA5201B: 34 channels (2 are clock channels)
TLA5202/TLA5202B: 68 channels (4 are clock channels).
TLA5203/TLA5203B: 102 channels (4 are clock and 2 are qualifier channels).
TLA5204/TLA5204B: 136 channels (4 are clock and 4 are qualifier channels).

## Hardware

The sampling front end stores a short 16K-sample buffer at 8GHz (125ps), called MagniVu.  This buffer then is driven directly into a multiplexer stage then into a Clock/Trigger state machine that allows for complex clock/signal-qualifier sequences, and signal sequence storage control (conditional storage, complex conditional triggering, or cascaded triggering )

Sampled data is passed into the multiplexer, allowing to sample all probe channels (1X), or half the probe channels at twice the speed (2X / DDR mode) or one quarter of the probe channels at four times the speed (4X)

Irrespective of the multiplexer speed, samples are stored along with 51-Bits at 125 ps resolution timestamps (aprox 3 days) either continuously or conditionally based on one of the trigger controller edge detection methods.

The trigger controller has

```
* 16 Independent Trigger States
* with 16 Conditional expression clauses per state
* with 8 Events per Conditional expression Clause
* Each Conditional expression clauses can take 8 Actions

```

Events

```
 * 18 Events
   Single Channel, Group, Word, Range, signal transition, glitch, setup-hold violation, timer hit, counter hit, external signal, snapshot.
 * 2 counter/timers 
 * plus 16 other resources ( Word value recognizers, Signal Transition recognizers )
 * 4 Range Recognizers

```

Actions

```
* Trigger main, trigger MagniVu, 
* store, don’t store, start store, stop store,
* increment counter, decrement counter, reset counter,
* start timer, stop timer, reset timer, snapshot current
* sample, goto state, set/clear signal, do nothing.

```

Clock state machine is similar to the trigger state machine, it allows multiple states with any combination of rising / falling or both edge logic being used to choose when to signal the trigger state machine to be clocked.

All of the TLA520X are based on a VME bus acquisition card, plugged into a 32bit/33MHz PCI card that plugs into a custom Intel PC running the Tektronix Logic Analyzer controller software under windows.

The VME acquisition card requires matching firmware to the version of the application software, with the newest being 5.7 firmware under 6.1sp1 software.

## Photos

<div class="photo-grid" markdown>

[![Tektronix Tla5204 1000](./img/Tektronix_TLA5204_1000.png)](./img/Tektronix_TLA5204_1000.png "Tektronix Tla5204 1000"){ .glightbox data-gallery="tektronix-tla520x" }
<span class="caption">Tektronix Tla5204 1000</span>

</div>
## Protocol

TODO.

## Resources
- [[1]](https://www.tek.com/tla5201-manual/tla5200-series) (PDF)

