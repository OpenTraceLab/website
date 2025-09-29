# Rigol DS Series Oscilloscopes
Digital storage oscilloscopes from Rigol with PC connectivity for automated measurements and waveform analysis.
## Supported Models
### DS1000Z Series
- **Models**: DS1054Z, DS1074Z, DS1104Z
- **Channels**: 4 analog channels
- **Bandwidth**: 50MHz, 70MHz, 100MHz
- **Sample Rate**: Up to 1 GSa/s
- **Memory Depth**: 12 Mpts
- **Connectivity**: USB, Ethernet, optional WiFi
### DS2000 Series
- **Models**: DS2072A, DS2102A, DS2202A, DS2302A
- **Channels**: 2 analog channels
- **Bandwidth**: 70MHz, 100MHz, 200MHz, 300MHz
- **Sample Rate**: Up to 2 GSa/s
- **Memory Depth**: 14 Mpts
- **Connectivity**: USB, Ethernet
### DS4000 Series
- **Models**: DS4012, DS4014, DS4024, DS4054
- **Channels**: 2 or 4 analog channels
- **Bandwidth**: 100MHz, 200MHz, 500MHz
- **Sample Rate**: Up to 4 GSa/s
- **Memory Depth**: 140 Mpts
- **Connectivity**: USB, Ethernet
## Features
### Waveform Capture
- **Real-time sampling**: Up to 4 GSa/s
- **Equivalent-time sampling**: Up to 50 GSa/s
- **Deep memory**: Up to 140 Mpts per channel
- **Segmented memory**: Capture multiple events
### Triggering
- **Edge triggering**: Rising, falling, both edges
- **Pulse triggering**: Width, timeout, runt pulses
- **Video triggering**: NTSC, PAL, HDTV standards
- **Serial triggering**: I2C, SPI, UART, CAN, LIN
### Measurements
- **Automatic measurements**: 30+ parameters
- **Cursors**: Manual measurements
- **Math functions**: Add, subtract, multiply, divide, FFT
- **Statistics**: Min, max, mean, standard deviation
## Installation
### Driver Support
Rigol oscilloscopes are supported through the `rigol-ds` driver using USBTMC or VXI-11 protocols.
### USB Connection
```bash
# Check for USBTMC device
ls /dev/usbtmc*
# Install USBTMC support (if needed)
sudo modprobe usbtmc
```
### Network Connection
```bash
# Configure oscilloscope IP address
# Use VXI-11 protocol over Ethernet
```
### Device Permissions (Linux)
```bash
# Install udev rules for Rigol devices
sudo cp contrib/60-opentracelab.rules /etc/udev/rules.d/
sudo udevadm control --reload-rules
sudo usermod -a -G plugdev $USER
```
## Usage
### Device Detection
```bash
# Scan for Rigol oscilloscopes
OpenTraceCLI --driver rigol-ds --scan
# Scan specific connection
OpenTraceCLI --driver rigol-ds --config conn=usbtmc --scan
OpenTraceCLI --driver rigol-ds --config conn=tcp-raw/192.168.1.100/5555 --scan
```
### Waveform Capture
```bash
# Capture single waveform
OpenTraceCLI --driver rigol-ds --config conn=usbtmc \
  --samples 1000 --output-file waveform.sr
# Capture all channels
OpenTraceCLI --driver rigol-ds --config conn=usbtmc \
  --channels CH1,CH2,CH3,CH4 --samples 2000 \
  --output-file all_channels.sr
```
### Automated Measurements
```bash
# Configure and capture
OpenTraceCLI --driver rigol-ds --config conn=usbtmc \
  --config timebase=1e-3:vdiv=1.0 \
  --samples 1000 --output-format csv \
  --output-file measurements.csv
```
## Hardware Setup
### Probe Connection
1. **Probe compensation**: Adjust probe compensation
2. **Attenuation**: Set probe attenuation (1x, 10x, 100x)
3. **Bandwidth limit**: Enable if needed for noise reduction
4. **Coupling**: AC, DC, or GND coupling
### Channel Configuration
```bash
# Configure channel settings
OpenTraceCLI --driver rigol-ds --config conn=usbtmc \
  --config CH1:vdiv=0.1:coupling=DC:probe_attenuation=10
```
### Triggering Setup
```bash
# Edge trigger on CH1 rising edge at 1V
OpenTraceCLI --driver rigol-ds --config conn=usbtmc \
  --config trigger_source=CH1:trigger_slope=POS:trigger_level=1.0
```
## Configuration Options
### Timebase Settings
- `timebase`: Time per division (1ns to 50s)
- `sample_rate`: Sample rate override
- `memory_depth`: Memory depth selection
### Channel Settings
- `vdiv`: Voltage per division
- `coupling`: AC, DC, or GND
- `probe_attenuation`: Probe attenuation factor
- `invert`: Invert channel display
### Trigger Settings
- `trigger_source`: Trigger source channel
- `trigger_slope`: POS, NEG, or RFAL
- `trigger_level`: Trigger level in volts
- `trigger_mode`: AUTO, NORM, or SING
## Remote Control
### SCPI Commands
Rigol oscilloscopes support standard SCPI commands:
```bash
# Query identification
echo "*IDN?" | nc 192.168.1.100 5555
# Set timebase
echo ":TIM:SCAL 1E-3" | nc 192.168.1.100 5555
# Trigger single acquisition
echo ":SING" | nc 192.168.1.100 5555
```
### Waveform Transfer
```bash
# Transfer waveform data
OpenTraceCLI --driver rigol-ds --config conn=tcp-raw/192.168.1.100/5555 \
  --samples 1000 --output-format binary \
  --output-file raw_waveform.bin
```
## Data Analysis
### Waveform Processing
```python
#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
# Load waveform data from CSV
data = np.loadtxt('waveform.csv', delimiter=',', skiprows=1)
time = data[:, 0]
voltage = data[:, 1]
# Calculate measurements
frequency = 1 / (time[-1] - time[0]) * len(time)
peak_to_peak = np.max(voltage) - np.min(voltage)
rms = np.sqrt(np.mean(voltage**2))
print(f"Frequency: {frequency:.2f} Hz")
print(f"Peak-to-Peak: {peak_to_peak:.3f} V")
print(f"RMS: {rms:.3f} V")
# Plot waveform
plt.plot(time, voltage)
plt.xlabel('Time (s)')
plt.ylabel('Voltage (V)')
plt.title('Captured Waveform')
plt.grid(True)
plt.show()
```
### FFT Analysis
```bash
# Capture waveform and perform FFT
OpenTraceCLI --driver rigol-ds --config conn=usbtmc \
  --samples 4096 --output-format csv | \
  python3 -c "
import numpy as np
import sys
data = np.loadtxt(sys.stdin, delimiter=',', skiprows=1)
voltage = data[:, 1]
fft = np.fft.fft(voltage)
freqs = np.fft.fftfreq(len(voltage), d=data[1,0]-data[0,0])
print('Dominant frequency:', freqs[np.argmax(np.abs(fft[1:len(fft)//2]))+1])
"
```
## Troubleshooting
### Connection Issues
**USB connection problems:**
- Check USBTMC driver installation
- Verify device permissions
- Try different USB port/cable
- Check oscilloscope USB settings
**Network connection problems:**
- Verify IP address configuration
- Check network connectivity (ping)
- Ensure VXI-11 service is enabled
- Check firewall settings
### Measurement Issues
**No waveform captured:**
- Check trigger settings
- Verify signal is present
- Adjust trigger level
- Use AUTO trigger mode
**Poor signal quality:**
- Check probe compensation
- Verify probe attenuation settings
- Adjust vertical sensitivity
- Enable bandwidth limiting if needed
### Performance Optimization
- Use appropriate sample rate for signal frequency
- Optimize memory depth for capture requirements
- Use segmented memory for repetitive signals
- Enable averaging for noisy signals
## Applications
### Automated Testing
```bash
#!/bin/bash
# Automated signal integrity test
echo "Signal Integrity Test Report" > report.txt
echo "============================" >> report.txt
for freq in 1000 10000 100000 1000000; do
    echo "Testing ${freq} Hz signal..."
    # Configure generator (external)
    # Configure oscilloscope
    OpenTraceCLI --driver rigol-ds --config conn=usbtmc \
      --config timebase=$((1000000/freq/10)) \
      --samples 1000 --output-format csv > temp.csv
    # Analyze results
    python3 -c "
import numpy as np
data = np.loadtxt('temp.csv', delimiter=',', skiprows=1)
voltage = data[:, 1]
print(f'${freq} Hz: Vpp={np.max(voltage)-np.min(voltage):.3f}V, RMS={np.sqrt(np.mean(voltage**2)):.3f}V')
" >> report.txt
done
echo "Test completed. See report.txt"
```
### Production Testing
- **Component characterization**: Measure component parameters
- **Signal integrity**: Verify signal quality
- **Timing analysis**: Check setup/hold times
- **Power analysis**: Measure power consumption
## Comparison
| Model | Channels | Bandwidth | Sample Rate | Memory | Price |
|-------|----------|-----------|-------------|---------|-------|
| DS1054Z | 4 | 50 MHz | 1 GSa/s | 12 Mpts | $$ |
| DS2102A | 2 | 100 MHz | 2 GSa/s | 14 Mpts | $$$ |
| DS4024 | 4 | 200 MHz | 4 GSa/s | 140 Mpts | $$$$ |
| Keysight DSOX1204G | 4 | 70 MHz | 2 GSa/s | 1 Mpts | $$$ |
## See Also
- [Hantek DSO Series](hantek-dso.md) - Budget alternatives
- [Siglent SDS Series](siglent-sds.md) - Similar price range
- [Oscilloscope Comparison](../../opentracecapture/overview.md#oscilloscopes) - Feature comparison
