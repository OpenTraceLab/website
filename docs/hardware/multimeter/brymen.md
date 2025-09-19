# Brymen Multimeter Series
High-accuracy digital multimeters from Brymen with PC connectivity for professional measurements and data logging.
## Supported Models
### Brymen BM25x Series
- **Models**: BM257, BM258, BM259
- **Display**: 50000 count dual display
- **DC Voltage**: 500mV to 1000V
- **AC Voltage**: 500mV to 750V (True RMS)
- **DC Current**: 500µA to 10A
- **AC Current**: 500µA to 10A (True RMS)
- **Resistance**: 500Ω to 50MΩ
- **Connectivity**: USB (HID interface)
### Brymen BM86x Series
- **Models**: BM867, BM869
- **Display**: 20000 count
- **DC Voltage**: 200mV to 1000V
- **AC Voltage**: 200mV to 750V (True RMS)
- **Additional**: Frequency, capacitance, temperature
- **Connectivity**: USB or RS232
## Features
### High Accuracy
- **0.02% basic accuracy** on DC voltage
- **True RMS** AC measurements
- **Low noise** front-end design
- **Temperature compensation** for stability
### Advanced Functions
- **Dual display**: Show two measurements simultaneously
- **Data logging**: Internal memory for measurements
- **Min/Max/Average**: Statistical functions
- **Relative mode**: Null/zero adjustment
- **Auto-hold**: Stable reading capture
### PC Connectivity
- **Real-time streaming**: Live measurement data
- **Remote control**: PC command interface
- **Data export**: CSV format support
- **Graphing**: Real-time trend display
## Installation
### Driver Support
Brymen multimeters are supported through the `brymen-bm25x` and `brymen-bm86x` drivers.
### USB Connection
Modern Brymen meters use USB HID interface:
```bash
# No special drivers required
# Device appears as HID device
lsusb | grep Brymen
```
### Device Permissions (Linux)
```bash
# Install udev rules for Brymen devices
sudo cp contrib/60-opentracelab.rules /etc/udev/rules.d/
sudo udevadm control --reload-rules
sudo usermod -a -G plugdev $USER
```
## Usage
### Device Detection
```bash
# Scan for Brymen multimeters
sigrok-cli --driver brymen-bm25x --scan
sigrok-cli --driver brymen-bm86x --scan
```
### Basic Measurements
```bash
# Single high-accuracy measurement
sigrok-cli --driver brymen-bm25x --samples 1
# Average of multiple readings
sigrok-cli --driver brymen-bm25x --samples 10 \
  --output-format csv | awk -F, 'NR>1 {sum+=$3; count++} END {print sum/count}'
```
### Precision Data Logging
```bash
# High-precision voltage logging
sigrok-cli --driver brymen-bm25x --time 3600 \
  --output-format csv:time=true:precision=6 \
  --output-file precision_log.csv
# Dual-channel logging (if supported)
sigrok-cli --driver brymen-bm25x --channels P1,P2 \
  --continuous --output-file dual_channel.csv
```
## Hardware Setup
### Measurement Configuration
1. **Function selection**: Use multimeter front panel
2. **Range selection**: Auto or manual ranging
3. **Display mode**: Single or dual display
4. **USB connection**: Connect to PC
### High-Accuracy Setup
For maximum accuracy:
1. **Warm-up time**: Allow 30 minutes stabilization
2. **Environmental**: Stable temperature (23°C ±5°C)
3. **Connections**: Use high-quality test leads
4. **Shielding**: Minimize electromagnetic interference
### Calibration Verification
```bash
# Measure precision voltage reference
sigrok-cli --driver brymen-bm25x --samples 20 \
  --output-format csv | awk -F, 'NR>1 {
    sum+=$3; sumsq+=$3*$3; count++
  } END {
    avg=sum/count
    std=sqrt(sumsq/count - avg*avg)
    print "Average:", avg
    print "Std Dev:", std
    print "Accuracy:", std/avg*100 "%"
  }'
```
## Configuration Options
### Measurement Settings
- `data_source`: Primary or secondary display
- `range`: Manual range selection
- `rate`: Measurement update rate
- `digits`: Display resolution
### Data Format Options
- `precision`: Number of decimal places
- `time`: Include timestamps
- `units`: Include measurement units
## Advanced Features
### Statistical Analysis
```bash
# Collect statistics over time
sigrok-cli --driver brymen-bm25x --samples 1000 \
  --output-format csv | awk -F, 'NR>1 {
    values[NR-1] = $3
    sum += $3
    count++
  } END {
    # Calculate mean
    mean = sum / count
    # Calculate standard deviation
    for (i=1; i<=count; i++) {
      variance += (values[i] - mean)^2
    }
    stddev = sqrt(variance / count)
    print "Samples:", count
    print "Mean:", mean
    print "Std Dev:", stddev
    print "Min:", min
    print "Max:", max
  }'
```
### Trend Monitoring
```bash
# Monitor for drift over time
sigrok-cli --driver brymen-bm25x --continuous \
  --output-format csv:time=true | \
  awk -F, 'NR>1 {
    print $1, $3
    if (NR==2) baseline=$3
    drift = ($3-baseline)/baseline*1000000
    print "Drift:", drift, "ppm"
  }'
```
## Accuracy Specifications
### BM25x Series Accuracy
- **DC Voltage**: ±(0.02% + 2 digits) [1 year, 23°C ±5°C]
- **AC Voltage**: ±(0.3% + 40 digits) [40Hz-1kHz]
- **DC Current**: ±(0.1% + 5 digits)
- **Resistance**: ±(0.05% + 2 digits)
### Temperature Coefficient
- **DC Voltage**: ±(0.002% + 1 digit)/°C
- **AC Voltage**: ±(0.01% + 2 digits)/°C
- **Current**: ±(0.01% + 2 digits)/°C
### Long-term Stability
- **1 year**: Specifications as listed
- **2 years**: Add 50% to accuracy specification
- **Calibration cycle**: Annual recommended
## Troubleshooting
### Accuracy Issues
**Readings outside specification:**
- Check calibration date
- Verify environmental conditions
- Allow adequate warm-up time
- Check test lead resistance
**Unstable readings:**
- Check for electromagnetic interference
- Verify proper grounding
- Use shielded test leads
- Check connection quality
**Temperature effects:**
- Allow temperature stabilization
- Use temperature compensation
- Monitor ambient temperature
- Consider thermal EMF effects
### Communication Issues
**Device not detected:**
- Check USB cable connection
- Verify device permissions
- Try different USB port
- Check multimeter display for PC mode
**Data corruption:**
- Verify USB cable quality
- Check for ground loops
- Reduce measurement rate
- Use error checking
## Applications
### Calibration Laboratory
```bash
#!/bin/bash
# Precision voltage calibration
echo "Calibrating voltage references..."
for voltage in 1.0000 2.0000 5.0000 10.0000; do
    echo "Apply ${voltage}V reference"
    read -p "Press Enter when ready..."
    # Take multiple readings for statistics
    sigrok-cli --driver brymen-bm25x --samples 20 \
      --output-format csv | awk -F, -v ref=$voltage 'NR>1 {
        sum+=$3; count++
      } END {
        measured=sum/count
        error=(measured-ref)/ref*100
        printf "Reference: %.4fV, Measured: %.6fV, Error: %.3f%%\n",
               ref, measured, error
      }'
done
```
### Research Measurements
```bash
# Long-term stability study
sigrok-cli --driver brymen-bm25x --continuous \
  --output-format csv:time=true:precision=8 | \
  tee stability_$(date +%Y%m%d_%H%M%S).csv
```
### Production Testing
- **Component verification**: High-accuracy component testing
- **Reference standards**: Calibration of secondary standards
- **Quality assurance**: Statistical process control
## Comparison
| Model | Resolution | DC Accuracy | AC Accuracy | Interface | Price |
|-------|------------|-------------|-------------|-----------|-------|
| BM257 | 50000 count | ±0.02% | ±0.3% | USB | $$$ |
| BM867 | 20000 count | ±0.025% | ±0.4% | USB/RS232 | $$$ |
| Fluke 8846A | 200000 count | ±0.0024% | ±0.06% | USB/Ethernet | $$$$$ |
| Keysight 34461A | 6½ digit | ±0.0030% | ±0.06% | USB/Ethernet | $$$$$ |
## Maintenance
### Calibration Schedule
- **Annual calibration**: Recommended for critical applications
- **Verification**: Monthly with known references
- **Adjustment**: Only by qualified service centers
### Care Instructions
- **Storage**: Clean, dry environment
- **Transport**: Use protective case
- **Cleaning**: Soft cloth, mild detergent
- **Fuses**: Replace only with specified types
## See Also
- [UNI-T Series](uni-t.md) - Budget alternatives
- [Voltcraft Series](voltcraft.md) - Mid-range options
- [Multimeter Comparison](../../opentracecapture/overview.md#multimeters) - Feature comparison
