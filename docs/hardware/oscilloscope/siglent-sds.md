# Siglent SDS Series Oscilloscopes
Digital storage oscilloscopes from Siglent offering excellent value with professional features and PC connectivity.
## Supported Models
### SDS1000X-E Series
- **Models**: SDS1104X-E, SDS1204X-E
- **Channels**: 4 analog channels
- **Bandwidth**: 100MHz, 200MHz
- **Sample Rate**: Up to 1 GSa/s
- **Memory Depth**: 14 Mpts
- **Connectivity**: USB, Ethernet, optional WiFi
### SDS2000X Series
- **Models**: SDS2074X, SDS2104X, SDS2204X, SDS2304X
- **Channels**: 4 analog channels
- **Bandwidth**: 70MHz, 100MHz, 200MHz, 300MHz
- **Sample Rate**: Up to 2 GSa/s
- **Memory Depth**: 140 Mpts
- **Connectivity**: USB, Ethernet, WiFi
### SDS5000X Series
- **Models**: SDS5032X, SDS5054X, SDS5104X
- **Channels**: 2 or 4 analog channels
- **Bandwidth**: 350MHz, 500MHz, 1GHz
- **Sample Rate**: Up to 5 GSa/s
- **Memory Depth**: 500 Mpts
- **Connectivity**: USB, Ethernet, WiFi
## Features
### Advanced Triggering
- **Edge triggering**: Standard rise/fall triggering
- **Pulse triggering**: Width, timeout, runt, window
- **Video triggering**: NTSC, PAL, SECAM, HDTV
- **Serial triggering**: I2C, SPI, UART, CAN, LIN, FlexRay
### Deep Memory
- **Segmented memory**: Capture multiple events
- **History mode**: Navigate through previous acquisitions
- **Zoom and scroll**: Navigate long captures
- **Search and mark**: Find specific events
### Built-in Analysis
- **FFT analysis**: Frequency domain analysis
- **Math functions**: Comprehensive waveform math
- **Measurements**: 38 automatic parameters
- **Statistics**: Measurement statistics and histograms
## Installation
### Driver Support
Siglent oscilloscopes are supported through the `siglent-sds` driver using USBTMC or VXI-11 protocols.
### USB Connection (USBTMC)
```bash
# Check for USBTMC device
ls /dev/usbtmc*
# Ensure USBTMC module is loaded
sudo modprobe usbtmc
```
### Network Connection (VXI-11)
```bash
# Configure oscilloscope network settings
# IP address, subnet mask, gateway
# Enable VXI-11 service in oscilloscope menu
```
### Device Permissions (Linux)
```bash
# Install udev rules for Siglent devices
sudo cp contrib/60-opentracelab.rules /etc/udev/rules.d/
sudo udevadm control --reload-rules
sudo usermod -a -G plugdev $USER
```
## Usage
### Device Detection
```bash
# Scan for Siglent oscilloscopes
OpenTraceCLI --driver siglent-sds --scan
# Scan specific connections
OpenTraceCLI --driver siglent-sds --config conn=usbtmc --scan
OpenTraceCLI --driver siglent-sds --config conn=vxi11/192.168.1.100 --scan
```
### Basic Waveform Capture
```bash
# Capture single waveform
OpenTraceCLI --driver siglent-sds --config conn=usbtmc \
  --samples 1000 --output-file waveform.sr
# Capture all 4 channels
OpenTraceCLI --driver siglent-sds --config conn=usbtmc \
  --channels C1,C2,C3,C4 --samples 5000 \
  --output-file all_channels.sr
```
### Deep Memory Capture
```bash
# Capture with maximum memory depth
OpenTraceCLI --driver siglent-sds --config conn=usbtmc \
  --config memory_depth=14000000 \
  --samples 14000000 --output-file deep_capture.sr
```
## Hardware Setup
### Probe Configuration
1. **Probe compensation**: Use built-in calibration signal
2. **Attenuation setting**: Match probe attenuation (1x, 10x, 100x)
3. **Bandwidth limit**: Enable 20MHz filter if needed
4. **Coupling**: Select AC, DC, or GND coupling
### Channel Setup
```bash
# Configure channel parameters
OpenTraceCLI --driver siglent-sds --config conn=usbtmc \
  --config C1:vdiv=0.5:coupling=DC:bwlimit=off:probe_ratio=10
```
### Trigger Configuration
```bash
# Configure edge trigger
OpenTraceCLI --driver siglent-sds --config conn=usbtmc \
  --config trigger_source=C1:trigger_slope=RISE:trigger_level=1.5
```
## Configuration Options
### Timebase Settings
- `timebase`: Time per division (1ns to 1000s)
- `sample_rate`: Override automatic sample rate
- `memory_depth`: Memory depth selection
### Channel Settings
- `vdiv`: Voltage per division (1mV to 10V)
- `coupling`: AC, DC, or GND
- `probe_ratio`: Probe attenuation (1, 10, 100, 1000)
- `bwlimit`: Bandwidth limit (20MHz or off)
### Trigger Settings
- `trigger_source`: C1, C2, C3, C4, EXT, LINE
- `trigger_slope`: RISE, FALL, or BOTH
- `trigger_level`: Trigger level in volts
- `trigger_mode`: AUTO, NORM, or SINGLE
## Advanced Features
### Segmented Memory
```bash
# Configure segmented memory capture
OpenTraceCLI --driver siglent-sds --config conn=usbtmc \
  --config acquire_mode=SEGMENTED:segment_count=1000 \
  --samples 10000 --output-file segmented.sr
```
### Serial Protocol Decoding
```bash
# Hardware-based I2C decoding
OpenTraceCLI --driver siglent-sds --config conn=usbtmc \
  --config serial_decode=I2C:i2c_scl=C1:i2c_sda=C2 \
  --samples 5000 --output-file i2c_decode.sr
```
### Math Functions
```bash
# Enable math channel (C1 + C2)
OpenTraceCLI --driver siglent-sds --config conn=usbtmc \
  --config math_enable=on:math_function=ADD:math_source1=C1:math_source2=C2 \
  --channels C1,C2,MATH --samples 2000
```
## Remote Control
### SCPI Commands
Siglent oscilloscopes support standard SCPI commands:
```bash
# Query instrument identification
echo "*IDN?" | nc 192.168.1.100 5025
# Set timebase to 1ms/div
echo "TDIV 1E-3" | nc 192.168.1.100 5025
# Start single acquisition
echo "ARM;FRTR" | nc 192.168.1.100 5025
# Query waveform data
echo "C1:WF? DAT2" | nc 192.168.1.100 5025
```
### Automated Measurements
```bash
# Configure and measure frequency
echo "PACU FREQ,C1" | nc 192.168.1.100 5025
echo "C1:PAVA? FREQ" | nc 192.168.1.100 5025
```
## Data Analysis
### Waveform Export and Analysis
```python
#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
# Load waveform data
data = np.loadtxt('waveform.csv', delimiter=',', skiprows=1)
time = data[:, 0]
voltage = data[:, 1]
# Calculate sample rate
sample_rate = 1.0 / (time[1] - time[0])
print(f"Sample Rate: {sample_rate/1e6:.1f} MSa/s")
# Perform FFT analysis
fft = np.fft.fft(voltage)
freqs = np.fft.fftfreq(len(voltage), d=1/sample_rate)
magnitude = np.abs(fft)
# Find dominant frequency
dominant_freq_idx = np.argmax(magnitude[1:len(magnitude)//2]) + 1
dominant_freq = freqs[dominant_freq_idx]
print(f"Dominant Frequency: {dominant_freq/1000:.1f} kHz")
# Calculate measurements
vpp = np.max(voltage) - np.min(voltage)
vrms = np.sqrt(np.mean(voltage**2))
vavg = np.mean(voltage)
print(f"Peak-to-Peak: {vpp:.3f} V")
print(f"RMS: {vrms:.3f} V")
print(f"Average: {vavg:.3f} V")
# Plot time domain and frequency domain
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))
# Time domain plot
ax1.plot(time * 1000, voltage)
ax1.set_xlabel('Time (ms)')
ax1.set_ylabel('Voltage (V)')
ax1.set_title('Time Domain')
ax1.grid(True)
# Frequency domain plot
ax2.semilogy(freqs[:len(freqs)//2]/1000, magnitude[:len(magnitude)//2])
ax2.set_xlabel('Frequency (kHz)')
ax2.set_ylabel('Magnitude')
ax2.set_title('Frequency Domain (FFT)')
ax2.grid(True)
ax2.set_xlim(0, sample_rate/2000)
plt.tight_layout()
plt.show()
```
### Signal Quality Analysis
```python
# Signal quality metrics
def analyze_signal_quality(time, voltage):
    # Calculate SNR
    signal_power = np.mean(voltage**2)
    # Estimate noise (high frequency components)
    b, a = signal.butter(4, 0.1, 'high')
    noise = signal.filtfilt(b, a, voltage)
    noise_power = np.mean(noise**2)
    snr_db = 10 * np.log10(signal_power / noise_power)
    # Calculate THD (Total Harmonic Distortion)
    fft = np.fft.fft(voltage)
    freqs = np.fft.fftfreq(len(voltage), d=time[1]-time[0])
    magnitude = np.abs(fft)
    # Find fundamental frequency
    fundamental_idx = np.argmax(magnitude[1:len(magnitude)//4]) + 1
    fundamental_power = magnitude[fundamental_idx]**2
    # Calculate harmonic power
    harmonic_power = 0
    for h in range(2, 6):  # 2nd to 5th harmonics
        harmonic_idx = fundamental_idx * h
        if harmonic_idx < len(magnitude)//2:
            harmonic_power += magnitude[harmonic_idx]**2
    thd = np.sqrt(harmonic_power / fundamental_power) * 100
    return snr_db, thd
snr, thd = analyze_signal_quality(time, voltage)
print(f"SNR: {snr:.1f} dB")
print(f"THD: {thd:.2f} %")
```
## Troubleshooting
### Connection Issues
**USB connection problems:**
- Verify USBTMC driver installation
- Check device permissions
- Try different USB port
- Restart oscilloscope USB interface
**Network connection problems:**
- Verify IP configuration
- Check VXI-11 service status
- Test network connectivity
- Check firewall settings
### Measurement Issues
**No trigger/capture:**
- Adjust trigger level and slope
- Check signal amplitude
- Verify trigger source
- Use AUTO trigger mode
**Memory depth limitations:**
- Reduce sample rate for longer captures
- Use segmented memory for repetitive signals
- Consider roll mode for continuous monitoring
### Performance Optimization
- Use appropriate memory depth for application
- Enable bandwidth limiting for noisy signals
- Use segmented memory for burst captures
- Optimize trigger settings for stable capture
## Applications
### Power Electronics
```bash
# Capture switching waveforms with deep memory
OpenTraceCLI --driver siglent-sds --config conn=usbtmc \
  --config timebase=1e-6:memory_depth=14000000 \
  --channels C1,C2,C3,C4 --samples 14000000 \
  --output-file power_switching.sr
```
### Signal Integrity Analysis
```bash
# High-speed digital signal analysis
OpenTraceCLI --driver siglent-sds --config conn=usbtmc \
  --config timebase=1e-9:sample_rate=5000000000 \
  --channels C1,C2 --samples 10000 \
  --output-file signal_integrity.sr
```
### Embedded System Debug
- **Serial protocol analysis**: Hardware-accelerated decoding
- **Timing analysis**: Precise timing measurements
- **Power analysis**: Current and voltage correlation
- **EMI debugging**: Frequency domain analysis
## Comparison
| Model | Channels | Bandwidth | Sample Rate | Memory | Price |
|-------|----------|-----------|-------------|---------|-------|
| SDS1104X-E | 4 | 100 MHz | 1 GSa/s | 14 Mpts | $$$ |
| SDS2204X | 4 | 200 MHz | 2 GSa/s | 140 Mpts | $$$$ |
| Rigol DS1054Z | 4 | 50 MHz | 1 GSa/s | 12 Mpts | $$ |
| Keysight DSOX1204G | 4 | 70 MHz | 2 GSa/s | 1 Mpts | $$$ |
## See Also
- [Rigol DS Series](rigol-ds.md) - Similar features and price
- [Hantek DSO Series](hantek-dso.md) - Budget alternatives
- [Oscilloscope Comparison](../../opentracecapture/overview.md#oscilloscopes) - Feature comparison
