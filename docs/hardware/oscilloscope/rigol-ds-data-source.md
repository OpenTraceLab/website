# Rigol Ds Data Source

## Contents 
\- [1 Overview](Rigol-ds_data_source.html#Overview) \- [2 Data as displayed on oscilloscope's screen](Rigol-ds_data_source.html#Data_as_displayed_on_oscilloscope's_screen) \- [3 Live](Rigol-ds_data_source.html#Live) \- [4 Memory](Rigol-ds_data_source.html#Memory) \- [5 Segmented](Rigol-ds_data_source.html#Segmented) 
## Overview The driver for Rigol oscilloscopes (rigol-ds) uses three different data sources: 1\. Live (default) 2\. Memory 3\. Segmented Below you can find the same data as shown on the oscilloscope's screen, read out with data source Live and read out with data source Memory. ## Data as displayed on oscilloscope's screen [![\1](../../assets/hardware/general/\2)](./File:Rigol_mso5000_displayed_image.png.html) ## Live Data source Live reads out the data displayed on the oscilloscope's screen. The number of data points returned depends on the model and can be 600, 1000, 1200 or 1400, i.e. each horizontal div is represented e.g. for an MSO5000 by 1000 data points / 10 div = 100 data points. [![\1](../../assets/hardware/general/\2)](./File:Rigol_mso5000_data_source_live.png.html) ## Memory Data source Memory reads out the whole memory of the oscilloscope. This allows zooming into the data, as it is possible on the oscilloscope. [![\1](../../assets/hardware/general/\2)](./File:Rigol_mso5000_data_source_memory.png.html) ## Segmented Rigol oscilloscopes sometimes offer to capture multiple frames, aka records. The segmented data source allows to read out these records. For MSO5000 with FW 00.01.02.00.03 this does not work properly. 
Retrieved from "[https://OpenTraceLab.org/w/index.php?title=Rigol-ds_data_source&oldid=16080](https://OpenTraceLab.org/w/index.php?title=Rigol-ds_data_source&oldid=16080)"

## See Also
- [Supported Hardware Overview](../supported-hardware.md)
- [OpenTraceCapture Documentation](../../opentracecapture/overview.md)
