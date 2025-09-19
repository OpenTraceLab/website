# Soundcard
Currently there is [PR pending](https://github.com/opentracelab/OpenTraceCapture/pull/185/) to add support for acquisition of analog signals using common soundcard HW. Some cheap USB soundcards can even be modified to bypass DC decoupling and thus enable for DC coupled acquisition. Bypassing is usualy done by [shorting some capacitor](https://www.daqarta.com/dw_ggll.htm). This module allows usage of any audio device recognized by OS, therefore it is also possible to use high-end ADC interfaces connected to I2S bus on devices like Raspberry PI. SDL2 multiplatform multimedia layer is used to provide excellent compatibility with most operating systems and their respective audio infrastructures while also preventing any compatibility issues in the future (eg. on Linux this allows operation no matter if you use raw ALSA, PulseAudio or PipeWire audio system).
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=Soundcard&oldid=16316](https://OpenTraceLab.org/w/index.php?title=Soundcard&oldid=16316)"
: \- *Device* \- *Oscilloscope* \- *In progress*
## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
