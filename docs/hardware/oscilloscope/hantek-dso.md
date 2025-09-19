# Hantek DSO Series Oscilloscopes
Affordable USB oscilloscopes from Hantek with PC-based operation and good performance for the price.
## Supported Models
### DSO-2xxx Series
- **Models**: DSO-2090, DSO-2150, DSO-2250
- **Channels**: 2 analog channels
- **Bandwidth**: 40MHz, 60MHz, 100MHz
- **Sample Rate**: Up to 250 MSa/s
- **Memory Depth**: 32K samples
- **Connectivity**: USB 2.0
### DSO-5xxx Series
- **Models**: DSO-5072P, DSO-5102P, DSO-5202P
- **Channels**: 2 analog channels + 16 digital (MSO)
- **Bandwidth**: 70MHz, 100MHz, 200MHz
- **Sample Rate**: Up to 1 GSa/s
- **Memory Depth**: 1M samples
- **Connectivity**: USB 2.0
### DSO-6xxx Series
- **Models**: DSO-6022BE, DSO-6022BL, DSO-6074BC
- **Channels**: 2 analog channels
- **Bandwidth**: 20MHz, 48MHz, 70MHz
- **Sample Rate**: Up to 250 MSa/s
- **Memory Depth**: 48K samples
- **Connectivity**: USB 2.0
## Features
### PC-Based Operation
- **Software oscilloscope**: Runs entirely on PC
- **Compact hardware**: Small USB-powered device
- **Flexible display**: Use full PC screen
- **Data storage**: Easy file save/load
### Mixed Signal (MSO Models)
- **16 digital channels**: Logic analyzer functionality
- **Synchronized capture**: Analog and digital together
- **Protocol decoding**: I2C, SPI, UART, CAN
- **Timing correlation**: Precise timing between analog/digital
### Built-in Generator (Some Models)
- **Function generator**: Sine, square, triangle waves
- **Arbitrary waveform**: Custom waveform generation
- **Frequency range**: 1Hz to 25MHz
- **Amplitude control**: Programmable output level
## Installation
### Driver Support
Hantek oscilloscopes are supported through the `hantek-dso` driver family.
### Windows Drivers
```bash
# Install Hantek USB drivers
# Download from Hantek website
# Install .inf driver package
```
### Linux Support
```bash
# Install udev rules
sudo cp contrib/60-opentracelab.rules /etc/udev/rules.d/
sudo udevadm control --reload-rules
sudo usermod -a -G plugdev $USER
# Load firmware (automatic with OpenTraceLab)
```
## Usage
### Device Detection
```bash
# Scan for Hantek oscilloscopes
sigrok-cli --driver hantek-dso --scan
# Specific model detection
sigrok-cli --driver hantek-dso-2xxx --scan
sigrok-cli --driver hantek-dso-5xxx --scan
```
### Basic Waveform Capture
```bash
# Capture single waveform
sigrok-cli --driver hantek-dso-2xxx \
  --config samplerate=1000000:framesize=1024 \
  --samples 1024 --output-file waveform.sr
# Capture both channels
sigrok-cli --driver hantek-dso-2xxx \
  --channels CH1,CH2 --samples 2048 \
  --output-file dual_channel.sr
```
### Mixed Signal Capture (MSO)
```bash
# Capture analog + digital channels
sigrok-cli --driver hantek-dso-5xxx \
  --channels CH1,CH2,D0,D1,D2,D3 \
  --config samplerate=100000000 \
  --samples 4096 --output-file mso_capture.sr
```
## Hardware Setup
### Probe Connection
1. **Probe compensation**: Adjust using calibration signal
2. **Attenuation**: Set 1x or 10x probe attenuation
3. **Ground connection**: Connect probe ground to circuit ground
4. **Bandwidth**: Consider probe bandwidth limitations
### Channel Configuration
- **Voltage range**: Adjust for signal amplitude
- **Coupling**: AC or DC coupling selection
- **Offset**: Vertical position adjustment
- **Invert**: Invert channel if needed
### Triggering
- **Source**: Select trigger channel
- **Level**: Set trigger voltage level
- **Slope**: Rising or falling edge
- **Mode**: Auto, normal, or single shot
## Configuration Options
### Sampling Settings
- `samplerate`: Sample rate (1kSa/s to 1GSa/s)
- `framesize`: Number of samples per frame
- `numframes`: Number of frames to capture
### Channel Settings
- `voltage`: Voltage range per channel
- `coupling`: AC or DC coupling
- `vdiv`: Voltage per division
### Trigger Settings
- `trigger_source`: Trigger source channel
- `trigger_slope`: POS or NEG
- `horiz_triggerpos`: Horizontal trigger position
## Performance Characteristics
### Sample Rate vs Memory
| Model | Max Sample Rate | Memory Depth | Max Capture Time |
|-------|----------------|--------------|------------------|
| DSO-2090 | 250 MSa/s | 32K | 128 µs |
| DSO-5072P | 1 GSa/s | 1M | 1 ms |
| DSO-6022BE | 48 MSa/s | 48K | 1 ms |
### Bandwidth Limitations
- **Analog bandwidth**: Limited by hardware frontend
- **Digital bandwidth**: Limited by sample rate
- **Probe bandwidth**: Consider probe specifications
- **USB bandwidth**: May limit continuous capture
## Troubleshooting
### Common Issues
**Device not detected:**
- Check USB cable connection
- Install/update USB drivers
- Try different USB port
- Check device power LED
**Firmware upload fails:**
- Ensure device is in bootloader mode
- Check USB connection stability
- Try manual firmware reload
- Verify firmware file integrity
**Poor signal quality:**
- Check probe compensation
- Verify ground connections
- Adjust voltage range
- Check for USB interference
### Performance Issues
**Slow capture rate:**
- Reduce sample rate if possible
- Minimize number of active channels
- Use smaller frame sizes
- Check USB bandwidth usage
**Triggering problems:**
- Adjust trigger level
- Check trigger source
- Use appropriate trigger slope
- Try different trigger modes
## Data Analysis
### Waveform Processing
```python
#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
# Load captured data
data = np.loadtxt('waveform.csv', delimiter=',', skiprows=1)
time = data[:, 0]
ch1 = data[:, 1]
ch2 = data[:, 2] if data.shape[1] > 2 else None
# Basic measurements
def measure_frequency(time, voltage):
    # Find zero crossings
    zero_crossings = np.where(np.diff(np.signbit(voltage)))[0]
    if len(zero_crossings) >= 2:
        period = (time[zero_crossings[-1]] - time[zero_crossings[0]]) / (len(zero_crossings) - 1) * 2
        return 1.0 / period
    return 0
freq = measure_frequency(time, ch1)
vpp = np.max(ch1) - np.min(ch1)
vrms = np.sqrt(np.mean(ch1**2))
print(f"Frequency: {freq:.2f} Hz")
print(f"Peak-to-Peak: {vpp:.3f} V")
print(f"RMS: {vrms:.3f} V")
# Plot results
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.plot(time * 1000, ch1)
plt.xlabel('Time (ms)')
plt.ylabel('Voltage (V)')
plt.title('Channel 1')
plt.grid(True)
if ch2 is not None:
    plt.subplot(1, 2, 2)
    plt.plot(time * 1000, ch2)
    plt.xlabel('Time (ms)')
    plt.ylabel('Voltage (V)')
    plt.title('Channel 2')
    plt.grid(True)
plt.tight_layout()
plt.show()
```
### Protocol Decoding
```bash
# Decode I2C protocol from digital channels
sigrok-cli --driver hantek-dso-5xxx \
  --channels D0,D1 --samples 10000 \
  --protocol-decoders i2c:scl=D0:sda=D1 \
  --protocol-decoder-annotations i2c
```
## Applications
### Educational Use
- **Electronics courses**: Demonstrate waveforms and measurements
- **Student labs**: Affordable oscilloscope for each student
- **Home projects**: Hobbyist electronics debugging
- **Repair work**: Troubleshoot electronic devices
### Professional Applications
- **Embedded development**: Debug microcontroller projects
- **Signal integrity**: Basic signal quality checks
- **Protocol analysis**: Decode serial communications
- **Production testing**: Simple automated tests
### Automation Example
```bash
#!/bin/bash
# Automated waveform capture script
echo "Starting automated capture sequence..."
for voltage in 1.0 2.0 3.0 5.0; do
    echo "Set signal generator to ${voltage}V and press Enter"
    read
    # Capture waveform
    sigrok-cli --driver hantek-dso-2xxx \
      --config samplerate=1000000 \
      --samples 1024 --output-format csv \
      --output-file "capture_${voltage}V.csv"
    # Quick analysis
    python3 -c "
import numpy as np
data = np.loadtxt('capture_${voltage}V.csv', delimiter=',', skiprows=1)
voltage = data[:, 1]
print(f'${voltage}V: Measured Vpp = {np.max(voltage)-np.min(voltage):.3f}V')
"
done
echo "Capture sequence completed"
```
## Limitations
### Hardware Limitations
- **Limited memory depth**: Shorter capture times
- **USB bandwidth**: May limit sample rates
- **No hardware triggering**: Software triggering only
- **Basic frontend**: Limited input protection
### Software Limitations
- **PC dependent**: Requires PC for operation
- **USB latency**: May affect real-time performance
- **Driver complexity**: More complex than standalone scopes
- **Power consumption**: Powered from USB only
## Comparison
| Model | Channels | Bandwidth | Sample Rate | Memory | Price |
|-------|----------|-----------|-------------|---------|-------|
| DSO-2090 | 2 | 40 MHz | 250 MSa/s | 32K | $ |
| DSO-5072P | 2+16 | 70 MHz | 1 GSa/s | 1M | $$ |
| Rigol DS1054Z | 4 | 50 MHz | 1 GSa/s | 12M | $$$ |
| Siglent SDS1104X-E | 4 | 100 MHz | 1 GSa/s | 14M | $$$ |
## See Also
- [Rigol DS Series](rigol-ds.md) - Professional alternatives
- [Siglent SDS Series](siglent-sds.md) - Similar price range
- [Oscilloscope Comparison](../../opentracecapture/overview.md#oscilloscopes) - Feature comparison
