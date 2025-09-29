# Voltcraft Multimeter Series
Digital multimeters from Voltcraft with serial/USB connectivity for PC-based measurements and logging.
## Supported Models
### Voltcraft VC-820
- **Display**: 4000 count LCD
- **DC Voltage**: 400mV to 1000V
- **AC Voltage**: 400mV to 750V
- **DC Current**: 400µA to 10A
- **AC Current**: 400µA to 10A
- **Resistance**: 400Ω to 40MΩ
- **Connectivity**: Serial (RS232)
### Voltcraft VC-840
- **Display**: 4000 count LCD with bargraph
- **DC Voltage**: 400mV to 1000V
- **AC Voltage**: 400mV to 750V
- **DC Current**: 400µA to 10A
- **AC Current**: 400µA to 10A
- **Resistance**: 400Ω to 40MΩ
- **Additional**: Frequency, capacitance, temperature
- **Connectivity**: Serial (RS232)
### Voltcraft M-3860D
- **Display**: 6000 count LCD
- **DC Voltage**: 600mV to 1000V
- **AC Voltage**: 600mV to 750V
- **DC Current**: 600µA to 10A
- **Resistance**: 600Ω to 60MΩ
- **Connectivity**: USB
## Features
### Measurement Functions
- **True RMS**: Accurate AC measurements
- **Auto-ranging**: Automatic range selection
- **Data hold**: Freeze current reading
- **Min/Max**: Record minimum and maximum values
- **Relative mode**: Zero reference measurements
### PC Interface
- **Real-time data**: Live measurement streaming
- **Command control**: Remote function selection
- **Data logging**: Continuous measurement recording
- **Protocol**: Standard SCPI-like commands
## Installation
### Driver Support
Voltcraft multimeters are supported through the `voltcraft-vc820` driver family.
### Serial Connection
Most Voltcraft meters use RS232 serial interface:
```bash
# Check available serial ports
ls /dev/ttyUSB* /dev/ttyACM*
# Set proper permissions
sudo usermod -a -G dialout $USER
```
### Device Permissions (Linux)
```bash
# Install udev rules
sudo cp contrib/60-opentracelab.rules /etc/udev/rules.d/
sudo udevadm control --reload-rules
```
## Usage
### Device Detection
```bash
# Scan for Voltcraft devices on serial ports
OpenTraceCLI --driver voltcraft-vc820 --config conn=/dev/ttyUSB0 --scan
# Auto-detect on all serial ports
OpenTraceCLI --driver voltcraft-vc820 --scan
```
### Basic Measurements
```bash
# Single measurement
OpenTraceCLI --driver voltcraft-vc820 --config conn=/dev/ttyUSB0 --samples 1
# Continuous measurements
OpenTraceCLI --driver voltcraft-vc820 --config conn=/dev/ttyUSB0 \
  --continuous --output-file measurements.csv
```
### Data Logging
```bash
# Log measurements with timestamps
OpenTraceCLI --driver voltcraft-vc820 --config conn=/dev/ttyUSB0 \
  --time 3600 --output-format csv:time=true \
  --output-file hourly_log.csv
# High-speed logging
OpenTraceCLI --driver voltcraft-vc820 --config conn=/dev/ttyUSB0 \
  --limit-samples 1000 --output-format csv
```
## Hardware Setup
### Serial Connection (VC-820/VC-840)
1. Connect RS232 cable to multimeter
2. Connect USB-to-serial adapter if needed
3. Configure serial parameters:
   - **Baud rate**: 2400 bps
   - **Data bits**: 8
   - **Parity**: None
   - **Stop bits**: 1
### USB Connection (M-3860D)
1. Connect USB cable directly to multimeter
2. Device appears as USB HID device
3. No additional drivers required
### Measurement Setup
1. Select measurement function on multimeter
2. Connect test leads to appropriate inputs
3. Set range (manual or auto)
4. Start PC communication
## Configuration Options
### Connection Settings
- `conn`: Serial port or USB device path
- `serialcomm`: Serial parameters (2400/8n1)
### Measurement Settings
- `data_source`: Measurement channel selection
- `range`: Manual range override
- `rate`: Measurement update rate
## Protocol Details
### Command Set (VC-820/VC-840)
The Voltcraft meters use a simple ASCII protocol:
```bash
# Request measurement
echo "D" > /dev/ttyUSB0
# Response format: +1.2345E+00
# Sign + 5 digits + exponent
```
### Data Format
```
+1.2345E+00  # +1.2345 V
-2.3456E-03  # -2.3456 mV
+1.0000E+06  # 1.000 MΩ
```
### Error Codes
- `+9.9999E+99`: Overload condition
- `-9.9999E+99`: Underflow condition
- `+0.0000E+00`: Zero or no signal
## Troubleshooting
### Common Issues
**Device not detected:**
- Check serial cable connection
- Verify correct COM port
- Check cable wiring (null modem may be needed)
- Ensure multimeter is powered on
**Communication errors:**
- Verify serial parameters (2400,8,N,1)
- Check for conflicting software using port
- Try different USB-to-serial adapter
- Test cable with loopback
**Measurement issues:**
- Ensure correct measurement function selected
- Check probe connections
- Verify measurement range
- Check for overload conditions
### Serial Cable Requirements
Some Voltcraft meters require specific cable wiring:
```
PC (DB9)     Meter (DB9)
Pin 2 (RX) → Pin 3 (TX)
Pin 3 (TX) → Pin 2 (RX)
Pin 5 (GND)→ Pin 5 (GND)
```
## Data Analysis
### CSV Output Processing
```bash
# Extract voltage measurements
OpenTraceCLI --driver voltcraft-vc820 --config conn=/dev/ttyUSB0 \
  --samples 100 --output-format csv | \
  awk -F, 'NR>1 && $4=="V" {print $3}' > voltages.txt
# Calculate statistics
awk '{sum+=$1; count++} END {
  print "Count:", count
  print "Average:", sum/count
  print "Total:", sum
}' voltages.txt
```
### Real-time Monitoring
```bash
# Monitor with timestamps
OpenTraceCLI --driver voltcraft-vc820 --config conn=/dev/ttyUSB0 \
  --continuous | while read line; do
    echo "$(date '+%Y-%m-%d %H:%M:%S'): $line"
  done
```
## Applications
### Production Testing
```bash
#!/bin/bash
# Automated component testing
echo "Testing resistor values..."
for expected in 1000 2200 4700 10000; do
    echo "Insert ${expected}Ω resistor and press Enter"
    read
    measured=$(OpenTraceCLI --driver voltcraft-vc820 \
      --config conn=/dev/ttyUSB0 --samples 5 | tail -1)
    echo "Expected: ${expected}Ω, Measured: $measured"
done
```
### Environmental Monitoring
```bash
# Temperature logging (VC-840 with temperature probe)
OpenTraceCLI --driver voltcraft-vc840 --config conn=/dev/ttyUSB0 \
  --continuous --output-format csv:time=true | \
  tee temperature_$(date +%Y%m%d).csv
```
### Quality Control
- **Incoming inspection**: Verify component values
- **Calibration verification**: Check reference standards
- **Process monitoring**: Track voltage/current over time
## Accuracy Specifications
### VC-820 Accuracy
- **DC Voltage**: ±(0.5% + 1 digit)
- **AC Voltage**: ±(1.2% + 3 digits)
- **DC Current**: ±(1.0% + 1 digit)
- **Resistance**: ±(0.8% + 1 digit)
### VC-840 Accuracy
- **DC Voltage**: ±(0.5% + 1 digit)
- **AC Voltage**: ±(1.0% + 3 digits)
- **Frequency**: ±(0.1% + 1 digit)
- **Capacitance**: ±(3.0% + 5 digits)
## Comparison
| Model | Display | Functions | Accuracy | Interface | Price |
|-------|---------|-----------|----------|-----------|-------|
| VC-820 | 4000 count | Basic DMM | ±0.5% | RS232 | $ |
| VC-840 | 4000 count | Extended | ±0.5% | RS232 | $$ |
| M-3860D | 6000 count | Basic DMM | ±0.3% | USB | $$ |
| UNI-T UT61E | 22000 count | Basic DMM | ±0.5% | USB | $$ |
## See Also
- [UNI-T Series](uni-t.md) - USB-based alternatives
- [Brymen Series](brymen.md) - Higher accuracy options
- [Multimeter Comparison](../../opentracecapture/overview.md#multimeters) - Feature comparison
