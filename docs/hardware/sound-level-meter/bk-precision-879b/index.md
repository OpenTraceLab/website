---
title: BK Precision 879B
---

# BK Precision 879B

<div class="infobox" markdown>

### BK Precision 879B

| | |
|---|---|
| **Status** | planned |
| **Counts** | 40000 |
| **Connectivity** | USB (VCP) |
| **Measurements** | inductance, capacitance, resistance, |
| **Features** | phase angle, dissipation factor, quality factor, min/max/avg, tolerance, dual display |
| **Website** | [bkprecision.com](https://www.bkprecision.com/products/component-testers/879B-40000-count-dual-display-handheld-lcr-meter-with-esr.html) |

</div>

# BK Precision 879B

The **BK Precision 879B** is a 40000 count (10000 for the secondary display) 0.5% handheld LCR meter with USB connectivity (VCP). It looks similar to the **Escort design** which other devices are based on, but really is a **new design** by BK Precision. The serial interface communicates SCPI commands over UART.

The 879B is **currently not supported** by mainline sigrok. Ideally there'd be a **scpi-lcr** driver if the command set is found to be of general nature, and not specific to this very device.

## Resources
- [vendor's product page](https://www.bkprecision.com/products/component-testers/879B-40000-count-dual-display-handheld-lcr-meter-with-esr.html)
- [user manual](https://bkpmedia.s3.amazonaws.com/downloads/manuals/en-us/87xB_manual.pdf) including the SCPI command set
- [EEVBlog review](https://www.eevblog.com/2011/01/02/eevblog-137-bk-precision-879b-handheld-lcr-meter-review/) episode 137, including a short appearance of Agilent 1732B (Escort)

