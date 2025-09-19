# Rigol DP Series Power Supplies
Professional programmable DC power supplies from Rigol with multiple outputs and advanced features.
## Supported Models
### DP832 Triple Output
- **Output 1**: 0-30V, 0-3A (90W)
- **Output 2**: 0-30V, 0-3A (90W)
- **Output 3**: 0-5V, 0-3A (15W)
- **Total Power**: 195W
- **Connectivity**: USB, Ethernet, RS232
- **Display**: 3.5" TFT color display
### DP831A Triple Output
- **Output 1**: 0-8V, 0-5A (40W)
- **Output 2**: 0-30V, 0-2A (60W)
- **Output 3**: 0-5V, 0-3A (15W)
- **Total Power**: 160W
- **Connectivity**: USB, Ethernet, RS232
- **Display**: 3.5" TFT color display
### DP821A Dual Output
- **Output 1**: 0-60V, 0-1A (60W)
- **Output 2**: 0-8V, 0-10A (80W)
- **Total Power**: 140W
- **Connectivity**: USB, Ethernet, RS232
- **Display**: 3.5" TFT color display
## Features
### Multiple Outputs
- **Independent control**: Each output controlled separately
- **Tracking modes**: Series, parallel tracking
- **Output coupling**: Link outputs for higher voltage/current
- **Isolation**: Outputs are isolated from each other
### Advanced Measurements
- **High resolution**: 1mV/0.1mA resolution
- **Fast measurement**: 2000 readings/second
- **Statistics**: Min, max, average measurements
- **Data logging**: Internal memory for measurements
### Protection Features
- **OVP/OCP**: Over-voltage/current protection per channel
- **OTP**: Over-temperature protection
- **Sense terminals**: 4-wire remote sensing
- **Timer functions**: Output timer control
## Installation
### Driver Support
Rigol DP series supplies are supported through the `rigol-dp832` driver using USBTMC or VXI-11 protocols.
### USB Connection (USBTMC)
```bash
# Check for USBTMC device
ls /dev/usbtmc*
# Ensure USBTMC module is loaded
sudo modprobe usbtmc
```
### Network Connection (VXI-11)
```bash
# Configure power supply network settings
# Enable VXI-11 service in system menu
# Set IP address, subnet, gateway
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
# Scan for Rigol power supplies
sigrok-cli --driver rigol-dp832 --scan
# Scan specific connections
sigrok-cli --driver rigol-dp832 --config conn=usbtmc --scan
sigrok-cli --driver rigol-dp832 --config conn=vxi11/192.168.1.100 --scan
```
### Basic Control
```bash
# Set voltage and current for channel 1
sigrok-cli --driver rigol-dp832 --config conn=usbtmc \
  --config CH1:voltage_target=12.0:current_limit=2.0:output_enabled=true
# Set multiple channels
sigrok-cli --driver rigol-dp832 --config conn=usbtmc \
  --config CH1:voltage_target=5.0:current_limit=1.0:output_enabled=true \
  --config CH2:voltage_target=3.3:current_limit=0.5:output_enabled=true
```
### Data Logging
```bash
# Monitor all channels continuously
sigrok-cli --driver rigol-dp832 --config conn=usbtmc \
  --channels CH1,CH2,CH3 --continuous \
  --output-format csv:time=true --output-file power_log.csv
```
## Hardware Setup
### Output Connections
Each channel has dedicated terminals:
```
Channel 1:  (+) (-) (+S) (-S)
Channel 2:  (+) (-) (+S) (-S)
Channel 3:  (+) (-) (+S) (-S)
```
### Remote Sensing (4-wire)
For accurate voltage regulation at the load:
```
Power Supply         Load
    (+) ──────────── Load (+)
    (-) ──────────── Load (-)
    (+S) ─────────── Load (+) [sense]
    (-S) ─────────── Load (-) [sense]
```
### Output Coupling
```bash
# Series connection (higher voltage)
# Connect CH1(+) to CH2(-), use CH1(-) and CH2(+) as outputs
# Parallel connection (higher current)
# Connect CH1(+) to CH2(+), CH1(-) to CH2(-)
# Configure tracking mode
```
## Configuration Options
### Channel Settings
- `voltage_target`: Target output voltage (V)
- `current_limit`: Current limit setting (A)
- `output_enabled`: Enable/disable output (true/false)
- `ovp_threshold`: Over-voltage protection level
- `ocp_threshold`: Over-current protection level
### Measurement Settings
- `voltage_range`: Voltage measurement range
- `current_range`: Current measurement range
- `measurement_rate`: Measurement update rate
### System Settings
- `beeper`: Enable/disable beeper
- `display_brightness`: Display brightness level
- `key_lock`: Front panel key lock
## Remote Control
### SCPI Commands
Rigol DP series supports standard SCPI commands:
```bash
# Query instrument identification
echo "*IDN?" | nc 192.168.1.100 5555
# Set channel 1 voltage to 12V
echo ":SOUR1:VOLT 12.0" | nc 192.168.1.100 5555
# Set channel 1 current limit to 2A
echo ":SOUR1:CURR 2.0" | nc 192.168.1.100 5555
# Enable channel 1 output
echo ":OUTP1 ON" | nc 192.168.1.100 5555
# Measure channel 1 voltage
echo ":MEAS:VOLT? CH1" | nc 192.168.1.100 5555
# Measure channel 1 current
echo ":MEAS:CURR? CH1" | nc 192.168.1.100 5555
```
### Advanced Control
```bash
# Configure tracking mode (parallel)
echo ":OUTP:TRAC:STAT ON" | nc 192.168.1.100 5555
echo ":OUTP:TRAC:MODE PARA" | nc 192.168.1.100 5555
# Set timer for channel 1 (10 seconds)
echo ":OUTP1:TIM:STAT ON" | nc 192.168.1.100 5555
echo ":OUTP1:TIM 10" | nc 192.168.1.100 5555
```
## Data Analysis
### Multi-Channel Monitoring
```python
#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
# Load multi-channel data
data = pd.read_csv('power_log.csv')
# Separate channels
ch1_data = data[data['Channel'] == 'CH1']
ch2_data = data[data['Channel'] == 'CH2']
ch3_data = data[data['Channel'] == 'CH3']
# Calculate power for each channel
ch1_power = ch1_data['Voltage'] * ch1_data['Current']
ch2_power = ch2_data['Voltage'] * ch2_data['Current']
ch3_power = ch3_data['Voltage'] * ch3_data['Current']
# Plot results
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 10))
# Voltage plot
ax1.plot(ch1_data['Time'], ch1_data['Voltage'], label='CH1', color='red')
ax1.plot(ch2_data['Time'], ch2_data['Voltage'], label='CH2', color='green')
ax1.plot(ch3_data['Time'], ch3_data['Voltage'], label='CH3', color='blue')
ax1.set_ylabel('Voltage (V)')
ax1.set_title('Output Voltages')
ax1.legend()
ax1.grid(True)
# Current plot
ax2.plot(ch1_data['Time'], ch1_data['Current'], label='CH1', color='red')
ax2.plot(ch2_data['Time'], ch2_data['Current'], label='CH2', color='green')
ax2.plot(ch3_data['Time'], ch3_data['Current'], label='CH3', color='blue')
ax2.set_ylabel('Current (A)')
ax2.set_title('Output Currents')
ax2.legend()
ax2.grid(True)
# Power plot
ax3.plot(ch1_data['Time'], ch1_power, label='CH1', color='red')
ax3.plot(ch2_data['Time'], ch2_power, label='CH2', color='green')
ax3.plot(ch3_data['Time'], ch3_power, label='CH3', color='blue')
ax3.set_ylabel('Power (W)')
ax3.set_xlabel('Time (s)')
ax3.set_title('Output Power')
ax3.legend()
ax3.grid(True)
# Total power
total_power = ch1_power.values + ch2_power.values + ch3_power.values
ax4.plot(ch1_data['Time'], total_power, color='black', linewidth=2)
ax4.set_ylabel('Total Power (W)')
ax4.set_xlabel('Time (s)')
ax4.set_title('Total Power Consumption')
ax4.grid(True)
plt.tight_layout()
plt.show()
# Print statistics
print("Power Supply Statistics:")
print(f"CH1 - Avg: {np.mean(ch1_power):.2f}W, Max: {np.max(ch1_power):.2f}W")
print(f"CH2 - Avg: {np.mean(ch2_power):.2f}W, Max: {np.max(ch2_power):.2f}W")
print(f"CH3 - Avg: {np.mean(ch3_power):.2f}W, Max: {np.max(ch3_power):.2f}W")
print(f"Total - Avg: {np.mean(total_power):.2f}W, Max: {np.max(total_power):.2f}W")
```
### Load Regulation Analysis
```python
#!/usr/bin/env python3
# Load regulation test analysis
import subprocess
import time
import numpy as np
def set_load_current(channel, current):
    """Simulate setting electronic load current"""
    # This would interface with electronic load
    print(f"Set load current CH{channel}: {current}A")
def measure_voltage(channel):
    """Measure actual output voltage"""
    cmd = f"sigrok-cli --driver rigol-dp832 --config conn=usbtmc --samples 1 --channels CH{channel} --output-format csv"
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    lines = result.stdout.strip().split('\n')
    if len(lines) >= 2:
        data = lines[1].split(',')
        return float(data[2])  # voltage
    return 0
# Test load regulation for each channel
channels = [1, 2, 3]
test_voltages = [5.0, 12.0, 24.0]  # Test voltages
load_currents = [0.0, 0.5, 1.0, 1.5, 2.0]  # Load current steps
print("Load Regulation Test Results")
print("=" * 50)
for channel in channels:
    print(f"\nChannel {channel} Results:")
    print("Voltage\tLoad(A)\tMeasured(V)\tRegulation(%)")
    for voltage in test_voltages:
        # Set output voltage
        cmd = f"sigrok-cli --driver rigol-dp832 --config conn=usbtmc --config CH{channel}:voltage_target={voltage}:current_limit=3.0:output_enabled=true"
        subprocess.run(cmd, shell=True)
        time.sleep(0.5)
        no_load_voltage = None
        for load_current in load_currents:
            set_load_current(channel, load_current)
            time.sleep(1)  # Settling time
            measured_voltage = measure_voltage(channel)
            if load_current == 0.0:
                no_load_voltage = measured_voltage
                regulation = 0.0
            else:
                regulation = abs(no_load_voltage - measured_voltage) / no_load_voltage * 100
            print(f"{voltage}V\t{load_current}\t{measured_voltage:.4f}\t{regulation:.3f}")
print("\nTest completed")
```
## Troubleshooting
### Connection Issues
**USB/Network problems:**
- Verify USBTMC driver installation
- Check network configuration
- Test with front panel ping function
- Verify VXI-11 service enabled
**Communication timeouts:**
- Increase command timeout
- Check network latency
- Verify command syntax
- Try lower communication rate
### Output Issues
**Voltage/current not as expected:**
- Check output enable status
- Verify protection settings
- Check load connections
- Verify remote sensing connections
**Protection activation:**
- Check OVP/OCP thresholds
- Verify load characteristics
- Check for short circuits
- Monitor temperature
### Performance Optimization
- Use remote sensing for accurate regulation
- Set appropriate protection levels
- Use tracking modes for related outputs
- Monitor total power consumption
## Applications
### Multi-Rail System Testing
```bash
#!/bin/bash
# Test multi-rail embedded system
echo "Multi-Rail Power Sequence Test"
# Power-up sequence
echo "Step 1: Enable 3.3V rail"
sigrok-cli --driver rigol-dp832 --config conn=usbtmc \
  --config CH3:voltage_target=3.3:current_limit=1.0:output_enabled=true
sleep 0.1
echo "Step 2: Enable 5V rail"
sigrok-cli --driver rigol-dp832 --config conn=usbtmc \
  --config CH1:voltage_target=5.0:current_limit=2.0:output_enabled=true
sleep 0.1
echo "Step 3: Enable 12V rail"
sigrok-cli --driver rigol-dp832 --config conn=usbtmc \
  --config CH2:voltage_target=12.0:current_limit=1.5:output_enabled=true
echo "All rails enabled - monitoring for 60 seconds"
sigrok-cli --driver rigol-dp832 --config conn=usbtmc \
  --channels CH1,CH2,CH3 --time 60 \
  --output-format csv:time=true --output-file startup_test.csv
echo "Power-down sequence"
sigrok-cli --driver rigol-dp832 --config conn=usbtmc \
  --config CH2:output_enabled=false
sleep 0.1
sigrok-cli --driver rigol-dp832 --config conn=usbtmc \
  --config CH1:output_enabled=false
sleep 0.1
sigrok-cli --driver rigol-dp832 --config conn=usbtmc \
  --config CH3:output_enabled=false
echo "Test completed"
```
### Battery Simulation
```python
#!/usr/bin/env python3
# Battery discharge simulation
import time
import subprocess
import math
def set_voltage(voltage):
    cmd = f"sigrok-cli --driver rigol-dp832 --config conn=usbtmc --config CH1:voltage_target={voltage}:current_limit=5.0:output_enabled=true"
    subprocess.run(cmd, shell=True)
# Simulate Li-ion battery discharge curve
print("Battery Discharge Simulation")
start_voltage = 4.2  # Fully charged
end_voltage = 3.0    # Discharged
duration = 3600      # 1 hour simulation
steps = 100
for i in range(steps + 1):
    # Non-linear discharge curve
    progress = i / steps
    # Exponential decay for realistic battery curve
    voltage = end_voltage + (start_voltage - end_voltage) * math.exp(-3 * progress)
    set_voltage(voltage)
    print(f"Step {i}/{steps}: {voltage:.3f}V")
    time.sleep(duration / steps)
print("Battery simulation completed")
```
### Production Testing
- **Device characterization**: Multi-voltage testing
- **Power sequencing**: Verify startup/shutdown sequences
- **Efficiency testing**: Measure power conversion efficiency
- **Compliance testing**: Verify power consumption limits
## Specifications
### DP832 Specifications
- **Voltage Accuracy**: ±(0.02% + 2mV)
- **Current Accuracy**: ±(0.1% + 500µA)
- **Voltage Resolution**: 1mV
- **Current Resolution**: 0.1mA
- **Load Regulation**: <0.01% + 2mV
- **Line Regulation**: <0.01% + 1mV
- **Ripple & Noise**: <350µVrms (20Hz-20MHz)
- **Temperature Coefficient**: <100ppm/°C
## Comparison
| Model | Outputs | Max Power | Accuracy | Interface | Price |
|-------|---------|-----------|----------|-----------|-------|
| DP832 | 3 (30V/3A + 5V/3A) | 195W | ±0.02% | USB+Ethernet | $$$$ |
| DP831A | 3 (8V/5A + 30V/2A + 5V/3A) | 160W | ±0.02% | USB+Ethernet | $$$$ |
| Korad KA3005P | 1 (30V/5A) | 150W | ±0.01% | USB | $$ |
| Keysight E36313A | 3 (6V/5A each) | 160W | ±0.05% | USB+Ethernet | $$$$$ |
## See Also
- [Korad Series](korad.md) - Budget alternatives
- [Power Supply Comparison](../../opentracecapture/overview.md#power-supplies) - Feature comparison
