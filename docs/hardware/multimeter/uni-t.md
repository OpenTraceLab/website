# UNI-T Multimeter Series
Digital multimeters from UNI-T with PC connectivity for automated measurements and data logging.
## Supported Models
### UNI-T UT61E
- **Display**: 22000 count LCD
- **DC Voltage**: 220mV to 1000V
- **AC Voltage**: 220mV to 750V
- **DC Current**: 220µA to 10A
- **AC Current**: 220µA to 10A
- **Resistance**: 220Ω to 22MΩ
- **Connectivity**: USB (HID interface)
### UNI-T UT61D
- **Display**: 6000 count LCD
- **DC Voltage**: 200mV to 1000V
- **AC Voltage**: 200mV to 750V
- **DC Current**: 200µA to 10A
- **AC Current**: 200µA to 10A
- **Resistance**: 200Ω to 20MΩ
- **Connectivity**: USB (HID interface)
### UNI-T UT32x Series
- **Models**: UT325, UT326, UT327
- **Specialization**: Temperature measurement
- **Channels**: Dual thermocouple inputs
- **Temperature Range**: -200°C to +1372°C
- **Connectivity**: USB (HID interface)
## Features
### Measurement Capabilities
- **True RMS**: AC voltage and current measurement
- **Auto-ranging**: Automatic range selection
- **Data hold**: Freeze display readings
- **Min/Max recording**: Track minimum and maximum values
- **Relative mode**: Zero adjustment for comparative measurements
### PC Connectivity
- **Real-time data**: Live measurement streaming
- **Data logging**: Continuous measurement recording
- **Remote control**: PC-controlled measurement functions
- **No drivers required**: Uses standard HID interface
## Installation
### Driver Support
UNI-T multimeters are supported through the `uni-t-ut61e` and `uni-t-ut32x` drivers.
### Device Permissions (Linux)
```bash
# Install udev rules for UNI-T devices
sudo cp contrib/60-opentracelab.rules /etc/udev/rules.d/
sudo udevadm control --reload-rules
sudo usermod -a -G plugdev $USER
```
## Usage
### Device Detection
```bash
# Scan for UNI-T multimeters
OpenTraceCLI --driver uni-t-ut61e --scan
OpenTraceCLI --driver uni-t-ut32x --scan
```
### Basic Measurements
```bash
# Single measurement
OpenTraceCLI --driver uni-t-ut61e --samples 1
# Continuous measurements for 60 seconds
OpenTraceCLI --driver uni-t-ut61e --time 60 --output-file measurements.csv
# Temperature logging with UT32x
OpenTraceCLI --driver uni-t-ut32x --time 3600 --output-file temperature.csv
```
### Data Logging
```bash
# Log voltage measurements every second
OpenTraceCLI --driver uni-t-ut61e --continuous \
  --output-format csv --output-file voltage_log.csv
# Log with timestamps
OpenTraceCLI --driver uni-t-ut61e --continuous \
  --output-format csv:time=true --output-file timestamped.csv
```
## Hardware Setup
### UT61E/UT61D Connection
1. Connect USB cable to multimeter
2. Set multimeter to desired measurement function
3. Select appropriate range (or auto-range)
4. Start measurement in software
### UT32x Temperature Setup
1. Connect thermocouples to T1/T2 inputs
2. Select thermocouple type (K, J, T, E, R, S, B, N)
3. Connect USB cable
4. Configure temperature units (°C/°F)
### Measurement Functions
#### Voltage Measurement
- **DC Voltage**: Direct measurement of DC voltages
- **AC Voltage**: True RMS AC voltage measurement
- **Range selection**: Manual or automatic ranging
#### Current Measurement
- **DC Current**: Direct current measurement
- **AC Current**: True RMS AC current measurement
- **Fused inputs**: 200mA and 10A current inputs
#### Resistance Measurement
- **2-wire**: Standard resistance measurement
- **Continuity**: Audible continuity testing
- **Diode test**: Forward voltage measurement
## Configuration Options
### Measurement Settings
- `data_source`: Select measurement function
- `range`: Manual range selection
- `rate`: Measurement update rate
### Data Format
- `output-format csv`: Comma-separated values
- `output-format analog`: Analog data format
- `time=true`: Include timestamps
## Data Analysis
### CSV Output Format
```csv
Time,Channel,Value,Unit
0.000000,P1,12.345,V
1.000000,P1,12.346,V
2.000000,P1,12.344,V
```
### Real-time Monitoring
```bash
# Monitor voltage in real-time
OpenTraceCLI --driver uni-t-ut61e --continuous | \
  while read line; do
    echo "$(date): $line"
  done
```
### Statistical Analysis
```bash
# Calculate statistics from logged data
OpenTraceCLI --driver uni-t-ut61e --samples 100 \
  --output-format csv | \
  awk -F, 'NR>1 {sum+=$3; count++} END {print "Average:", sum/count}'
```
## Troubleshooting
### Common Issues
**Device not detected:**
- Check USB cable connection
- Verify multimeter is powered on
- Try different USB port
- Check device permissions (Linux)
**No measurements:**
- Ensure multimeter is in correct mode
- Check measurement function selection
- Verify probe connections
- Check for overload conditions
**Incorrect readings:**
- Verify measurement range
- Check probe calibration
- Ensure proper connection to circuit
- Check for interference sources
### Performance Tips
- Use appropriate measurement range for accuracy
- Allow multimeter to stabilize before logging
- Use shielded cables for sensitive measurements
- Avoid ground loops in measurement setup
## Calibration
### Factory Calibration
UNI-T multimeters are factory calibrated and typically don't require user calibration.
### Verification
```bash
# Measure known reference voltage
OpenTraceCLI --driver uni-t-ut61e --samples 10
# Compare with reference standard
```
### Accuracy Specifications
#### UT61E Accuracy
- **DC Voltage**: ±(0.5% + 3 digits)
- **AC Voltage**: ±(0.8% + 5 digits)
- **DC Current**: ±(0.8% + 5 digits)
- **Resistance**: ±(0.8% + 3 digits)
#### Temperature Accuracy (UT32x)
- **K-type**: ±(0.3% + 1°C)
- **J-type**: ±(0.3% + 1°C)
- **Other types**: Varies by type
## Applications
### Automated Testing
```bash
#!/bin/bash
# Automated voltage test script
for voltage in 1.0 2.0 3.0 5.0; do
    echo "Set voltage to ${voltage}V and press Enter"
    read
    measurement=$(OpenTraceCLI --driver uni-t-ut61e --samples 5 | tail -1)
    echo "Measured: $measurement"
done
```
### Data Logging
```bash
# Long-term temperature monitoring
OpenTraceCLI --driver uni-t-ut32x --continuous \
  --output-format csv:time=true \
  --output-file "temp_$(date +%Y%m%d).csv" &
```
### Quality Control
- **Production testing**: Automated component testing
- **Incoming inspection**: Verify component specifications
- **Environmental monitoring**: Temperature and voltage logging
## Comparison
| Model | Display | Accuracy | Connectivity | Price |
|-------|---------|----------|--------------|-------|
| UT61E | 22000 count | ±0.5% | USB | $$ |
| UT61D | 6000 count | ±0.8% | USB | $ |
| UT325 | Temperature | ±0.3% | USB | $$ |
| Fluke 87V | 20000 count | ±0.05% | Optional | $$$$ |
## See Also
- [Voltcraft Series](voltcraft.md) - Similar price range
- [Brymen Series](brymen.md) - Higher accuracy options
- [Multimeter Comparison](../../opentracecapture/overview.md#multimeters) - Feature comparison
