# Circuits For Barebone Boards

This page describes which input protection / measuring circuits for barebone or other more minimal boards can be used. 
## Contents 
\- [1 Probing a circuit](Circuits_for_barebone_boards.html#Probing_a_circuit) \- [2 Input protection](Circuits_for_barebone_boards.html#Input_protection) \- [2.1 Clamp circuits with resistor / Z-Diodes](Circuits_for_barebone_boards.html#Clamp_circuits_with_resistor_/_Z-Diodes) \- [2.1.1 Issues measuring higher frequencies](Circuits_for_barebone_boards.html#Issues_measuring_higher_frequencies) \- [2.2 With buffer IC](Circuits_for_barebone_boards.html#With_buffer_IC) \- [3 Analog frontends](Circuits_for_barebone_boards.html#Analog_frontends) 
## Probing a circuit Usually for a logic analyzer high input impedance (and low capacitance) is wanted, to influence the measured circuit as least as possible (don't put an additional capacitive load on it). On the other hand, one might want to use an R-C low-pass filter for the signal to block possible higher frequency spikes. If that is wanted or required, it is best to introduce an additional buffering IC that will then drive the load of the introduced capacity of the filter. This can not directly be advised for logic analyzers, but rather for analog instruments (oscilloscopes) that will usually be used in a bigger variety of cases with possibly more noise in the signal. ## Input protection ### Clamp circuits with resistor / Z-Diodes A clamp circuit can be used, for example view below at [Spiralbrain's Blog](http://web.archive.org/web/20140604115345/http://sunbizhosting.co.uk/~spiral/blog/?p=117). When using Zener diodes instead of the normal diodes in Spiralbrain's blog we can get also a protection from negative voltages: The circuit is shown here again with Zener diodes and numbering for [fx2lafw](Fx2lafw.html "Fx2lafw") pins: 
[![\1](../../assets/hardware/general/\2)](./File:Clamp_circuit1.png.html)
[](./File:Clamp_circuit1.png.html "Enlarge")
3.3V clamping circuit

## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
