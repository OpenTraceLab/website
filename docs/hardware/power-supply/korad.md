# Korad Power Supply Series
Programmable DC power supplies from Korad with PC connectivity for automated testing and remote control.
## Supported Models
### KA3005P Series
- **Models**: KA3005P, KA3010P, KA6003P
- **Output Voltage**: 0-30V, 0-30V, 0-60V
- **Output Current**: 0-5A, 0-10A, 0-3A
- **Power**: 150W, 300W, 180W
- **Connectivity**: USB (Virtual COM port)
- **Display**: 4-digit LED voltage/current
### KD3005P Series
- **Models**: KD3005P, KD3010P, KD6003P
- **Output Voltage**: 0-30V, 0-30V, 0-60V
- **Output Current**: 0-5A, 0-10A, 0-3A
- **Power**: 150W, 300W, 180W
- **Connectivity**: USB + RS232
- **Display**: 4-digit LED with additional features
### KWR Series (Switching)
- **Models**: KWR103, KWR203
- **Output Voltage**: 0-30V, 0-60V
- **Output Current**: 0-3A, 0-3A
- **Power**: 90W, 180W
- **Connectivity**: USB
- **Features**: Switching topology, higher efficiency
## Features
### Programmable Control
- **Voltage setting**: 10mV resolution
- **Current setting**: 1mA resolution (varies by model)
- **Output enable/disable**: Remote on/off control
- **Protection**: OVP, OCP, OTP protection
### Measurement Capabilities
- **Voltage readback**: Actual output voltage
- **Current readback**: Actual output current
- **Power calculation**: Real-time power display
- **Status monitoring**: CV/CC mode indication
### PC Interface
- **Real-time control**: Set voltage/current remotely
- **Data logging**: Monitor voltage/current over time
- **Automated testing**: Scripted test sequences
- **Status monitoring**: Protection status and mode
## Installation
### Driver Support
Korad power supplies are supported through the `korad-kaxxxxp` driver family.
### USB Connection
Most Korad supplies use USB-to-serial converter:
```bash
# Check for USB-serial device
ls /dev/ttyUSB* /dev/ttyACM*
# Set permissions for serial access
sudo usermod -a -G dialout $USER
```
### Device Permissions (Linux)
```bash
# Install udev rules for Korad devices
sudo cp contrib/60-opentracelab.rules /etc/udev/rules.d/
sudo udevadm control --reload-rules
```
## Usage
### Device Detection
```bash
# Scan for Korad power supplies
sigrok-cli --driver korad-kaxxxxp --scan
# Scan specific serial port
sigrok-cli --driver korad-kaxxxxp --config conn=/dev/ttyUSB0 --scan
```
### Basic Control
```bash
# Set voltage and current limits
sigrok-cli --driver korad-kaxxxxp --config conn=/dev/ttyUSB0 \
  --config voltage_target=12.0:current_limit=2.0
# Enable output
sigrok-cli --driver korad-kaxxxxp --config conn=/dev/ttyUSB0 \
  --config output_enabled=true
# Monitor voltage and current
sigrok-cli --driver korad-kaxxxxp --config conn=/dev/ttyUSB0 \
  --continuous --output-format csv --output-file power_log.csv
```
### Automated Testing
```bash
# Voltage sweep test
for voltage in 5.0 10.0 15.0 20.0; do
    echo "Setting voltage to ${voltage}V"
    sigrok-cli --driver korad-kaxxxxp --config conn=/dev/ttyUSB0 \
      --config voltage_target=$voltage:output_enabled=true
    sleep 2  # Allow settling time
    # Read back actual values
    sigrok-cli --driver korad-kaxxxxp --config conn=/dev/ttyUSB0 \
      --samples 1 --output-format csv
done
```
## Hardware Setup
### Output Connections
1. **Positive terminal**: Red binding post (+)
2. **Negative terminal**: Black binding post (-)
3. **Sense terminals**: Optional remote sensing (4-wire)
4. **Ground**: Chassis ground (separate from output)
### Load Connection
```
Power Supply    Load
    (+) ────────── (+)
    (-) ────────── (-)
    Optional 4-wire sensing:
    (+S) ───────── (+) at load
    (-S) ───────── (-) at load
```
### Safety Considerations
- **Current limiting**: Always set appropriate current limit
- **Voltage verification**: Verify voltage before connecting sensitive loads
- **Protection**: Use external fuses for critical applications
- **Grounding**: Ensure proper grounding for safety
## Configuration Options
### Output Settings
- `voltage_target`: Target output voltage (V)
- `current_limit`: Current limit setting (A)
- `output_enabled`: Enable/disable output (true/false)
### Protection Settings
- `ovp_threshold`: Over-voltage protection threshold
- `ocp_threshold`: Over-current protection threshold
- `ovp_enabled`: Enable over-voltage protection
- `ocp_enabled`: Enable over-current protection
### Communication Settings
- `conn`: Serial port connection
- `serialcomm`: Serial parameters (9600/8n1)
## Protocol Details
### Command Set
Korad supplies use a simple ASCII protocol:
```bash
# Set voltage (12.34V)
echo "VSET1:12.34" > /dev/ttyUSB0
# Set current limit (2.50A)
echo "ISET1:2.50" > /dev/ttyUSB0
# Enable output
echo "OUT1" > /dev/ttyUSB0
# Disable output
echo "OUT0" > /dev/ttyUSB0
# Read voltage
echo "VOUT1?" > /dev/ttyUSB0
# Read current
echo "IOUT1?" > /dev/ttyUSB0
# Read status
echo "STATUS?" > /dev/ttyUSB0
```
### Response Format
```
VOUT1?  → 12.34    (voltage in volts)
IOUT1?  → 02.50    (current in amps)
STATUS? → 0x01     (status byte)
```
### Status Byte Decoding
```
Bit 0: CV/CC mode (0=CV, 1=CC)
Bit 1: Output state (0=off, 1=on)
Bit 2-7: Reserved
```
## Data Logging and Analysis
### Continuous Monitoring
```bash
# Log voltage and current with timestamps
sigrok-cli --driver korad-kaxxxxp --config conn=/dev/ttyUSB0 \
  --continuous --output-format csv:time=true | \
  tee power_monitor_$(date +%Y%m%d_%H%M%S).csv
```
### Load Testing
```python
#!/usr/bin/env python3
import time
import subprocess
import csv
def set_voltage(voltage):
    """Set power supply voltage"""
    cmd = f"sigrok-cli --driver korad-kaxxxxp --config conn=/dev/ttyUSB0 --config voltage_target={voltage}:output_enabled=true"
    subprocess.run(cmd, shell=True)
def read_measurements():
    """Read voltage and current"""
    cmd = "sigrok-cli --driver korad-kaxxxxp --config conn=/dev/ttyUSB0 --samples 1 --output-format csv"
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    lines = result.stdout.strip().split('\n')
    if len(lines) >= 2:
        data = lines[1].split(',')
        return float(data[2]), float(data[3])  # voltage, current
    return 0, 0
# Load regulation test
print("Load Regulation Test")
print("Voltage\tNo Load\tFull Load\tRegulation")
for voltage in [5.0, 12.0, 24.0]:
    set_voltage(voltage)
    time.sleep(1)
    # No load measurement
    v_no_load, i_no_load = read_measurements()
    input(f"Connect load for {voltage}V test and press Enter...")
    # Full load measurement
    v_full_load, i_full_load = read_measurements()
    # Calculate load regulation
    regulation = abs(v_no_load - v_full_load) / v_no_load * 100
    print(f"{voltage}V\t{v_no_load:.3f}V\t{v_full_load:.3f}V\t{regulation:.2f}%")
print("Test completed")
```
## Troubleshooting
### Common Issues
**Device not detected:**
- Check USB cable connection
- Verify correct COM port
- Check device power
- Try different USB port
**Communication errors:**
- Verify serial parameters (9600,8,N,1)
- Check for other software using port
- Try power cycling the supply
- Check cable integrity
**Output issues:**
- Verify output is enabled
- Check current limit setting
- Verify load connections
- Check protection status
### Calibration Verification
```bash
# Verify voltage accuracy with DMM
echo "Voltage Calibration Check"
for voltage in 1.000 5.000 10.000 15.000 20.000; do
    sigrok-cli --driver korad-kaxxxxp --config conn=/dev/ttyUSB0 \
      --config voltage_target=$voltage:output_enabled=true
    echo "Set to ${voltage}V - measure with DMM and record"
    read -p "Press Enter to continue..."
done
```
## Applications
### Automated Testing
```bash
#!/bin/bash
# Device power consumption test
echo "Power Consumption Test"
echo "Voltage,Current,Power" > power_test.csv
# Test at different voltages
for voltage in 3.3 5.0 9.0 12.0; do
    echo "Testing at ${voltage}V..."
    # Set voltage
    sigrok-cli --driver korad-kaxxxxp --config conn=/dev/ttyUSB0 \
      --config voltage_target=$voltage:current_limit=3.0:output_enabled=true
    sleep 2  # Settling time
    # Measure for 10 seconds
    sigrok-cli --driver korad-kaxxxxp --config conn=/dev/ttyUSB0 \
      --time 10 --output-format csv | \
      awk -F, 'NR>1 {print $3","$4","$3*$4}' >> power_test.csv
done
echo "Test completed. Results in power_test.csv"
```
### Battery Charging
```python
#!/usr/bin/env python3
# Simple battery charger controller
import time
import subprocess
def get_measurements():
    cmd = "sigrok-cli --driver korad-kaxxxxp --config conn=/dev/ttyUSB0 --samples 1 --output-format csv"
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    lines = result.stdout.strip().split('\n')
    if len(lines) >= 2:
        data = lines[1].split(',')
        return float(data[2]), float(data[3])
    return 0, 0
def set_output(voltage, current, enabled=True):
    cmd = f"sigrok-cli --driver korad-kaxxxxp --config conn=/dev/ttyUSB0 --config voltage_target={voltage}:current_limit={current}:output_enabled={enabled}"
    subprocess.run(cmd, shell=True)
# Battery charging parameters
charge_voltage = 14.4  # Lead acid battery
charge_current = 2.0   # 2A charging current
float_voltage = 13.8   # Float voltage
print("Starting battery charging sequence...")
# Constant current phase
print("Phase 1: Constant Current")
set_output(charge_voltage, charge_current, True)
while True:
    voltage, current = get_measurements()
    print(f"V: {voltage:.2f}V, I: {current:.2f}A")
    # Switch to float when current drops
    if current < 0.2:  # 200mA termination
        break
    time.sleep(10)
# Float phase
print("Phase 2: Float Charging")
set_output(float_voltage, 0.5, True)
print("Charging complete - switched to float mode")
```
### Production Testing
- **Device characterization**: Measure device power consumption
- **Burn-in testing**: Long-term reliability testing
- **Compliance testing**: Verify power supply specifications
- **Quality control**: Statistical process monitoring
## Specifications
### KA3005P Specifications
- **Voltage Range**: 0-30V
- **Current Range**: 0-5A
- **Voltage Resolution**: 10mV
- **Current Resolution**: 1mA
- **Voltage Accuracy**: ±(0.01% + 3mV)
- **Current Accuracy**: ±(0.2% + 3mA)
- **Load Regulation**: <0.01% + 3mV
- **Line Regulation**: <0.01% + 2mV
- **Ripple**: <1mVrms
## Comparison
| Model | Voltage | Current | Power | Accuracy | Interface | Price |
|-------|---------|---------|-------|----------|-----------|-------|
| KA3005P | 0-30V | 0-5A | 150W | ±0.01% | USB | $$ |
| KD3010P | 0-30V | 0-10A | 300W | ±0.01% | USB+RS232 | $$$ |
| Rigol DP832 | 3x30V | 3x3A | 195W | ±0.02% | USB+Ethernet | $$$$ |
| Keysight E36313A | 3x6V | 3x5A | 160W | ±0.05% | USB+Ethernet | $$$$$ |
## See Also
- [Rigol DP Series](rigol-dp.md) - Professional alternatives
- [Power Supply Comparison](../../opentracecapture/overview.md#power-supplies) - Feature comparison
