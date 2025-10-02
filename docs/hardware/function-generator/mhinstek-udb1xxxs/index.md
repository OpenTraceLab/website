---
title: MHINSTEK UDB1xxxS
---

# MHINSTEK UDB1xxxS

<div class="infobox" markdown>

![MHINSTEK UDB1xxxS](./img/MHINSTEK_UDB1305S_persp.jpg){ .infobox-image }

### MHINSTEK UDB1xxxS

| | |
|---|---|
| **Status** | planned |
| **Frequency (user)** | 0.01Hz-2MHz/5MHz/8MHz |
| **Waveforms** | sine/square/triangle/sawtooth, TTL rect |
| **Amplitude** | 10 V (open)/5 V (50 Ohm) (adjustable) |
| **Connectivity** | Serial TTL (3.3V) |

</div>

The UDB1302S/UDB1305S/UDB1308S is a Dual-Channel standalone function generator. It can be controlled with the push-buttons and the rotary
encoder, or via a bidirectional serial interface.

Amplitude and offset voltage can only be controlled using potentiometers.

This device can be bought on ebay or aliexpress from various sellers for 40€/50€/60€.

## Hardware
- CPLD: Altera MAXII
- Clock: 34.56MHz
- STM8S105K4 8-bit MCU with 16 Kbytes Flash, 16 MHz CPU, integrated EEPROM [STM8S10K54 procuct page](http://www.st.com/web/catalog/mmc/FM141/SC1244/SS1010/LN754/PF215111)
- 74AHC14 Hex inverting Schmitt trigger (TTL output buffer, Freq/counter input buffer)

## Photos

<div class="photo-grid" markdown>

[![Mhinstek Udb1305s Persp](./img/MHINSTEK_UDB1305S_persp.jpg)](./img/MHINSTEK_UDB1305S_persp.jpg "Mhinstek Udb1305s Persp"){ .glightbox data-gallery="mhinstek-udb1xxxs" }
<span class="caption">Mhinstek Udb1305s Persp</span>

[![Mhinstek Udb1305s Detail Analog](./img/MHINSTEK_UDB1305S_detail_analog.jpg)](./img/MHINSTEK_UDB1305S_detail_analog.jpg "Mhinstek Udb1305s Detail Analog"){ .glightbox data-gallery="mhinstek-udb1xxxs" }
<span class="caption">Mhinstek Udb1305s Detail Analog</span>

[![Mhinstek Udb1305s Detail Digital](./img/MHINSTEK_UDB1305S_detail_digital.jpg)](./img/MHINSTEK_UDB1305S_detail_digital.jpg "Mhinstek Udb1305s Detail Digital"){ .glightbox data-gallery="mhinstek-udb1xxxs" }
<span class="caption">Mhinstek Udb1305s Detail Digital</span>

[![Mhinstek Udb1305s Baseboard](./img/MHINSTEK_UDB1305S_baseboard.jpg)](./img/MHINSTEK_UDB1305S_baseboard.jpg "Mhinstek Udb1305s Baseboard"){ .glightbox data-gallery="mhinstek-udb1xxxs" }
<span class="caption">Mhinstek Udb1305s Baseboard</span>

</div>
## Connection

All models communicate via an serial connection, at either 19200 or 57600 bps, 8 bits, no parity, and 1 stop bit (57600/8n1 or 19200/8n1). Connecting to the devices can be done with any USB-serial converter. Signalling level is 3.3V

UDB1505S uses 57600 bps.

## Protocol

The generator will respond to commands, which consist of a short ASCII string followed by CR (additional LFs are ignored). The meter will either send no response at all or some ASCII text followed by CR+LF.

There a three classes of commands:

- Identication
- Set request
- Get request

Most set requests have a corresponding get request.

### Identification command
```
&#8594; a
&#8592; UDB1305S

```
### Set/get requests
#### Select channel A/B
```
&#8594; bh1
&#8592; ok

&#8594; bh2
&#8592; ok

```

Query (`ch`) always reports channel 0 (i.e. neither 1 or 2)

#### Set/get frequency
```
5 MHz
&#8594; bf500000000
&#8592; ok

&#8594; cf
&#8592; cf500000000

2 kHz
&#8594; bf000200000
&#8592; ok

&#8594; cf
&#8592; cf000200000

1 Hz
&#8594; bf      100
&#8592; ok

&#8594; cf
&#8592; cf000000100

```
## Resources
- [User Manuals UDB130xS/UDB12xxS/UDB110xS/UDB100xS](http://www.mhinstek.com/down/class/?24.html)
- [Software Download (Chinese?)](http://www.mhinstek.com/down/html/?84.html)
- [Software Download (Google translation)](https://translate.google.de/translate?sl=auto&tl=de&u=http%3A%2F%2Fwww.mhinstek.com%2Fdown%2Fhtml%2F%3F84.html)

