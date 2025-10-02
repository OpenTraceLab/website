---
title: Protocol decoders
---

# Protocol decoders

<div class="infobox" markdown>

### Protocol decoders

| | |
|---|---|

</div>

This is a list of **supported protocol decoders (PDs)** already supported by [libsigrokdecode](https://sigrok.org/wiki/Libsigrokdecode) and also **a list of work in progress or yet to be implemented decoders**,

See [Protocol decoder API](https://sigrok.org/wiki/Protocol_decoder_API) for details on how the decoders work in sigrok, and [Protocol decoder HOWTO](https://sigrok.org/wiki/Protocol_decoder_HOWTO) for a quick introduction about how to write your own decoders.




## Supported protocol decoders

Number of currently supported protocol decoders: **131**.

| Protocol | Tags | Input IDs | Output IDs | Status | Full name | Description |
|---|---|---|---|---|---|---|
| [AC '97](https://sigrok.org/wiki/Protocol_decoder:Ac97) | Audio, PC | logic | — | supported | Audio Codec '97 | Audio and modem control for PC systems. |
| [AD5626](/w/index.php?title=Protocol_decoder:Ad5626&action=edit&redlink=1) | IC, Analog/digital | spi | — | supported | Analog Devices AD5626 | Analog Devices AD5626 12-bit nanoDAC. |
| [AD79x0](/w/index.php?title=Protocol_decoder:Ad79x0&action=edit&redlink=1) | IC, Analog/digital | spi | — | supported | Analog Devices AD79x0 | Analog Devices AD7910/AD7920 12-bit ADC. |
| [ADE77xx](/w/index.php?title=Protocol_decoder:Ade77xx&action=edit&redlink=1) | Analog/digital, IC, Sensor | spi | — | supported | Analog Devices ADE77xx | Poly phase multifunction energy metering IC protocol. |
| [ADF435x](/w/index.php?title=Protocol_decoder:Adf435x&action=edit&redlink=1) | Clock/timing, IC, Wireless/RF | spi | — | supported | Analog Devices ADF4350/1 | Wideband synthesizer with integrated VCO. |
| [ADNS-5020](https://sigrok.org/wiki/Protocol_decoder:Adns5020) | IC, PC, Sensor | spi | — | supported | Avago ADNS-5020 | Bidirectional optical mouse sensor protocol. |
| [ADXL345](/w/index.php?title=Protocol_decoder:Adxl345&action=edit&redlink=1) | IC, Sensor | spi | — | supported | Analog Devices ADXL345 | Analog Devices ADXL345 3-axis accelerometer. |
| [AM230x](https://sigrok.org/wiki/Protocol_decoder:Am230x) | IC, Sensor | logic | — | supported | Aosong AM230x/DHTxx/RHTxx | Aosong AM230x/DHTxx/RHTxx humidity/temperature sensor. |
| [Amulet ASCII](/w/index.php?title=Protocol_decoder:Amulet_ascii&action=edit&redlink=1) | Display | uart | — | supported | Amulet LCD ASCII | Amulet Technologies LCD controller ASCII protocol. |
| [ARM ETMv3](https://sigrok.org/wiki/Protocol_decoder:Arm_etmv3) | Debug/trace | uart | — | supported | ARM Embedded Trace Macroblock v3 | ARM ETM v3 instruction trace protocol. |
| [ARM ITM](https://sigrok.org/wiki/Protocol_decoder:Arm_itm) | Debug/trace | uart | — | supported | ARM Instrumentation Trace Macroblock | ARM Cortex-M / ARMv7m ITM trace protocol. |
| [ARM TPIU](https://sigrok.org/wiki/Protocol_decoder:Arm_tpiu) | Debug/trace | uart | uart | supported | ARM Trace Port Interface Unit | Filter TPIU formatted trace data into separate streams. |
| [ATSHA204A](/w/index.php?title=Protocol_decoder:Atsha204a&action=edit&redlink=1) | Security/crypto, IC, Memory | i2c | — | supported | Microchip ATSHA204A | Microchip ATSHA204A family crypto authentication protocol. |
| [AUD](https://sigrok.org/wiki/Protocol_decoder:Aud) | Debug/trace | logic | — | supported | Advanced User Debugger | Renesas/Hitachi Advanced User Debugger (AUD) protocol. |
| [AVR ISP](/w/index.php?title=Protocol_decoder:Avr_isp&action=edit&redlink=1) | Debug/trace | spi | — | supported | AVR In-System Programming | Atmel AVR In-System Programming (ISP) protocol. |
| [AVR PDI](https://sigrok.org/wiki/Protocol_decoder:Avr_pdi) | Debug/trace | logic | — | supported | Atmel Program and Debug Interface | Atmel ATxmega Program and Debug Interface (PDI) protocol. |
| [Caliper](https://sigrok.org/wiki/Protocol_decoder:Caliper) | Analog/digital, Sensor | logic | — | supported | Digital calipers | Protocol of cheap generic digital calipers. |
| [CAN](/w/index.php?title=Protocol_decoder:Can&action=edit&redlink=1) | Automotive | logic | — | supported | Controller Area Network | Field bus protocol for distributed realtime control. |
| [CC1101](https://sigrok.org/wiki/Protocol_decoder:Cc1101) | IC, Wireless/RF | spi | — | supported | Texas Instruments CC1101 | Low-power sub-1GHz RF transceiver chip. |
| [CEC](https://sigrok.org/wiki/Protocol_decoder:Cec) | Display, PC | logic | — | supported | HDMI-CEC | HDMI Consumer Electronics Control (CEC) protocol. |
| [CFP](/w/index.php?title=Protocol_decoder:Cfp&action=edit&redlink=1) | Networking | mdio | — | supported | 100 Gigabit C form-factor pluggable | 100 Gigabit C form-factor pluggable (CFP) protocol. |
| [cJTAG](/w/index.php?title=Protocol_decoder:Cjtag&action=edit&redlink=1) | Debug/trace | logic | jtag | supported | Compact Joint Test Action Group (IEEE 1149.7) | Protocol for testing, debugging, and flashing ICs. |
| [Counter](/w/index.php?title=Protocol_decoder:Counter&action=edit&redlink=1) | Util | logic | — | supported | Edge counter | Count the number of edges in a signal. |
| [DALI](/w/index.php?title=Protocol_decoder:Dali&action=edit&redlink=1) | Embedded/industrial, Lighting | logic | — | supported | Digital Addressable Lighting Interface | Digital Addressable Lighting Interface (DALI) protocol. |
| [DCF77](https://sigrok.org/wiki/Protocol_decoder:Dcf77) | Clock/timing | logic | — | supported | DCF77 time protocol | European longwave time signal (77.5kHz carrier signal). |
| [DMX512](/w/index.php?title=Protocol_decoder:Dmx512&action=edit&redlink=1) | Embedded/industrial, Lighting | uart | dmx512 | supported | Digital MultipleX 512 | Digital MultipleX 512 (DMX512) lighting protocol. |
| [DS1307](/w/index.php?title=Protocol_decoder:Ds1307&action=edit&redlink=1) | Clock/timing, IC | i2c | — | supported | Dallas DS1307 | Dallas DS1307 realtime clock module protocol. |
| [DS2408](/w/index.php?title=Protocol_decoder:Ds2408&action=edit&redlink=1) | Embedded/industrial, IC | onewire_network | — | supported | Maxim DS2408 | 1-Wire 8-channel addressable switch. |
| [DS243x](/w/index.php?title=Protocol_decoder:Ds243x&action=edit&redlink=1) | IC, Memory | onewire_network | — | supported | Maxim DS2432/3 | Maxim DS243x series 1-Wire EEPROM protocol. |
| [DS28EA00](/w/index.php?title=Protocol_decoder:Ds28ea00&action=edit&redlink=1) | IC, Sensor | onewire_network | — | supported | Maxim DS28EA00 1-Wire digital thermometer | 1-Wire digital thermometer with Sequence Detect and PIO. |
| [DSI](/w/index.php?title=Protocol_decoder:Dsi&action=edit&redlink=1) | Embedded/industrial, Lighting | logic | — | supported | Digital Serial Interface | Digital Serial Interface (DSI) lighting protocol. |
| [EDID](/w/index.php?title=Protocol_decoder:Edid&action=edit&redlink=1) | Display, Memory, PC | i2c | — | supported | Extended Display Identification Data | Data structure describing display device capabilities. |
| [24xx EEPROM](/w/index.php?title=Protocol_decoder:Eeprom24xx&action=edit&redlink=1) | IC, Memory | i2c | — | supported | 24xx I²C EEPROM | 24xx series I²C EEPROM protocol. |
| [93xx EEPROM](/w/index.php?title=Protocol_decoder:Eeprom93xx&action=edit&redlink=1) | IC, Memory | microwire | — | supported | 93xx Microwire EEPROM | 93xx series Microwire EEPROM protocol. |
| [EM4100](/w/index.php?title=Protocol_decoder:Em4100&action=edit&redlink=1) | IC, RFID | logic | — | supported | RFID EM4100 | EM4100 100-150kHz RFID protocol. |
| [EM4305](/w/index.php?title=Protocol_decoder:Em4305&action=edit&redlink=1) | IC, RFID | logic | — | supported | RFID EM4205/EM4305 | EM4205/EM4305 100-150kHz RFID protocol. |
| [ENC28J60](/w/index.php?title=Protocol_decoder:Enc28j60&action=edit&redlink=1) | Embedded/industrial, Networking | spi | — | supported | Microchip ENC28J60 | Microchip ENC28J60 10Base-T Ethernet controller protocol. |
| [FlexRay](https://sigrok.org/wiki/Protocol_decoder:Flexray) | Automotive | logic | — | supported | FlexRay | Automotive network communications protocol. |
| [Gray code](https://sigrok.org/wiki/Protocol_decoder:Graycode) | Encoding | logic | — | supported | Gray code and rotary encoder | Accumulate rotary encoder increments, provide statistics. |
| [Guess bitrate](/w/index.php?title=Protocol_decoder:Guess_bitrate&action=edit&redlink=1) | Clock/timing, Util | logic | — | supported | Guess bitrate/baudrate | Guess the bitrate/baudrate of a UART (or other) protocol. |
| [HDCP](/w/index.php?title=Protocol_decoder:Hdcp&action=edit&redlink=1) | PC, Security/crypto | i2c | hdcp | supported | HDCP over HDMI | HDCP protocol over HDMI. |
| [I²C](https://sigrok.org/wiki/Protocol_decoder:I2c) | Embedded/industrial | logic | i2c | supported | Inter-Integrated Circuit | Two-wire, multi-master, serial bus. |
| [I²C demux](/w/index.php?title=Protocol_decoder:I2cdemux&action=edit&redlink=1) | Util | i2c | — | supported | I²C demultiplexer | Demux I²C packets into per-slave-address streams. |
| [I²C filter](/w/index.php?title=Protocol_decoder:I2cfilter&action=edit&redlink=1) | Util | i2c | i2c | supported | I²C filter | Filter out addresses/directions in an I²C stream. |
| [I²S](/w/index.php?title=Protocol_decoder:I2s&action=edit&redlink=1) | Audio, PC | logic | i2s | supported | Integrated Interchip Sound | Serial bus for connecting digital audio devices. |
| [IEEE-488](https://sigrok.org/wiki/Protocol_decoder:Ieee488) | PC, Retro computing | logic | ieee488 | supported | IEEE-488 GPIB/HPIB/IEC | IEEE-488 General Purpose Interface Bus (GPIB/HPIB or IEC). |
| [IR IRMP](https://sigrok.org/wiki/Protocol_decoder:Ir_irmp) | IR | logic | — | supported | IR IRMP | IRMP infrared remote control multi protocol. |
| [IR NEC](https://sigrok.org/wiki/Protocol_decoder:Ir_nec) | IR | logic | — | supported | IR NEC | NEC infrared remote control protocol. |
| [IR RC-5](/w/index.php?title=Protocol_decoder:Ir_rc5&action=edit&redlink=1) | IR | logic | — | supported | IR RC-5 | RC-5 infrared remote control protocol. |
| [IR RC-6](/w/index.php?title=Protocol_decoder:Ir_rc6&action=edit&redlink=1) | IR | logic | — | supported | IR RC-6 | RC-6 infrared remote control protocol. |
| [IR SIRC](https://sigrok.org/wiki/Protocol_decoder:Ir_sirc) | IR | logic | — | supported | Sony IR (SIRC) | Sony infrared remote control protocol (SIRC). |
| [Jitter](/w/index.php?title=Protocol_decoder:Jitter&action=edit&redlink=1) | Clock/timing, Util | logic | — | supported | Timing jitter calculation | Retrieves the timing jitter between two digital signals. |
| [JTAG](/w/index.php?title=Protocol_decoder:Jtag&action=edit&redlink=1) | Debug/trace | logic | jtag | supported | Joint Test Action Group (IEEE 1149.1) | Protocol for testing, debugging, and flashing ICs. |
| [JTAG / EJTAG](/w/index.php?title=Protocol_decoder:Jtag_ejtag&action=edit&redlink=1) | Debug/trace | jtag | — | supported | Joint Test Action Group / EJTAG (MIPS) | MIPS EJTAG protocol. |
| [JTAG / STM32](/w/index.php?title=Protocol_decoder:Jtag_stm32&action=edit&redlink=1) | Debug/trace | jtag | — | supported | Joint Test Action Group / ST STM32 | ST STM32-specific JTAG protocol. |
| [LFAST](/w/index.php?title=Protocol_decoder:Lfast&action=edit&redlink=1) | Embedded/industrial | logic | lfast | supported | NXP LFAST interface | Differential high-speed P2P interface |
| [LIN](/w/index.php?title=Protocol_decoder:Lin&action=edit&redlink=1) | Automotive | uart | — | supported | Local Interconnect Network | Local Interconnect Network (LIN) protocol. |
| [LM75](/w/index.php?title=Protocol_decoder:Lm75&action=edit&redlink=1) | Sensor | i2c | — | supported | National LM75 | National LM75 (and compatibles) temperature sensor. |
| [LPC](https://sigrok.org/wiki/Protocol_decoder:Lpc) | PC | logic | — | supported | Low Pin Count | Protocol for low-bandwidth devices on PC mainboards. |
| [LTC242x](/w/index.php?title=Protocol_decoder:Ltc242x&action=edit&redlink=1) | IC, Analog/digital | spi | — | supported | Linear Technology LTC242x | Linear Technology LTC2421/LTC2422 1-/2-channel 20-bit ADC. |
| [LTC26x7](/w/index.php?title=Protocol_decoder:Ltc26x7&action=edit&redlink=1) | IC, Analog/digital | i2c | — | supported | Linear Technology LTC26x7 | Linear Technology LTC26x7 16-/14-/12-bit rail-to-rail DACs. |
| [Maple bus](/w/index.php?title=Protocol_decoder:Maple_bus&action=edit&redlink=1) | Retro computing | logic | — | supported | SEGA Maple bus | Maple bus peripheral protocol for SEGA Dreamcast. |
| [MAX7219](/w/index.php?title=Protocol_decoder:Max7219&action=edit&redlink=1) | Display | spi | — | supported | Maxim MAX7219/MAX7221 | Maxim MAX72xx series 8-digit LED display driver. |
| [MCS-48](https://sigrok.org/wiki/Protocol_decoder:Mcs48) | Retro computing | logic | — | supported | Intel MCS-48 | Intel MCS-48 external memory access protocol. |
| [MDIO](https://sigrok.org/wiki/Protocol_decoder:Mdio) | Networking | logic | mdio | supported | Management Data Input/Output | MII management bus between MAC and PHY. |
| [Microwire](/w/index.php?title=Protocol_decoder:Microwire&action=edit&redlink=1) | Embedded/industrial | logic | microwire | supported | Microwire | 3-wire, half-duplex, synchronous serial bus. |
| [MIDI](/w/index.php?title=Protocol_decoder:Midi&action=edit&redlink=1) | Audio, PC | uart | — | supported | Musical Instrument Digital Interface | Musical Instrument Digital Interface (MIDI) protocol. |
| [MIL-STD-1553](https://sigrok.org/wiki/Protocol_decoder:Mil-std-1553) | Embedded/industrial, Networking | logic | — | soon | MIL-STD-1553 avionic data bus. | MIL-STD-1553 avionic data bus protocol. |
| [Miller](https://sigrok.org/wiki/Protocol_decoder:Miller) | Encoding | logic | — | supported | Miller encoding | Miller encoding protocol. |
| [MLX90614](/w/index.php?title=Protocol_decoder:Mlx90614&action=edit&redlink=1) | IC, Sensor | i2c | — | supported | Melexis MLX90614 | Melexis MLX90614 infrared thermometer protocol. |
| [Modbus](https://sigrok.org/wiki/Protocol_decoder:Modbus) | Embedded/industrial | uart | modbus | supported | Modbus RTU over RS232/RS485 | Modbus RTU protocol for industrial applications. |
| [Morse](https://sigrok.org/wiki/Protocol_decoder:Morse) | Encoding | logic | — | supported | Morse code | Demodulated morse code protocol. |
| [MRF24J40](https://sigrok.org/wiki/Protocol_decoder:Mrf24j40) | IC, Wireless/RF | spi | — | supported | Microchip MRF24J40 | IEEE 802.15.4 2.4 GHz RF tranceiver chip. |
| [MXC6225XU](/w/index.php?title=Protocol_decoder:Mxc6225xu&action=edit&redlink=1) | IC, Sensor | i2c | — | supported | MEMSIC MXC6225XU | Digital Thermal Orientation Sensor (DTOS) protocol. |
| [NES gamepad](https://sigrok.org/wiki/Protocol_decoder:Nes_gamepad) | Retro computing | spi | — | supported | Nintendo Entertainment System gamepad | NES gamepad button states. |
| [nRF24L01(+)](https://sigrok.org/wiki/Protocol_decoder:Nrf24l01) | IC, Wireless/RF | spi | — | supported | Nordic Semiconductor nRF24L01(+) | 2.4GHz RF transceiver chip. |
| [nRF905](/w/index.php?title=Protocol_decoder:Nrf905&action=edit&redlink=1) | IC, Wireless/RF | spi | — | supported | Nordic Semiconductor nRF905 | 433/868/933MHz transceiver chip. |
| [Numbers and State](https://sigrok.org/wiki/Protocol_decoder:Numbers_and_state) | Encoding, Util | logic | numbers_and_state | supported | Interpret bit patters as numbers or state enums | Interpret bit patterns as different kinds of numbers (integer, float, enum). |
| [Nunchuk](https://sigrok.org/wiki/Protocol_decoder:Nunchuk) | Sensor | i2c | — | supported | Nintendo Wii Nunchuk | Nintendo Wii Nunchuk controller protocol. |
| [1-Wire link layer](/w/index.php?title=Protocol_decoder:Onewire_link&action=edit&redlink=1) | Embedded/industrial | logic | onewire_link | supported | 1-Wire serial communication bus (link layer) | Bidirectional, half-duplex, asynchronous serial bus. |
| [1-Wire network layer](/w/index.php?title=Protocol_decoder:Onewire_network&action=edit&redlink=1) | Embedded/industrial | onewire_link | onewire_network | supported | 1-Wire serial communication bus (network layer) | Bidirectional, half-duplex, asynchronous serial bus. |
| [OOK](https://sigrok.org/wiki/Protocol_decoder:Ook) | Encoding | logic | ook | supported | On-off keying | On-off keying protocol. |
| [Oregon](https://sigrok.org/wiki/Protocol_decoder:Ook_oregon) | Sensor | ook | — | supported | Oregon Scientific | Oregon Scientific weather sensor protocol. |
| [OOK visualisation](https://sigrok.org/wiki/Protocol_decoder:Ook_vis) | Encoding | ook | ook | supported | On-off keying visualisation | OOK visualisation in various formats. |
| [PAN1321](https://sigrok.org/wiki/Protocol_decoder:Pan1321) | Wireless/RF | uart | — | supported | Panasonic PAN1321 | Bluetooth RF module with Serial Port Profile (SPP). |
| [Parallel](https://sigrok.org/wiki/Protocol_decoder:Parallel) | Util | logic | parallel | supported | Parallel sync bus | Generic parallel synchronous bus. |
| [PCA9571](/w/index.php?title=Protocol_decoder:Pca9571&action=edit&redlink=1) | Embedded/industrial, IC | i2c | — | supported | NXP PCA9571 | NXP PCA9571 8-bit I²C output expander. |
| [PJDL](https://sigrok.org/wiki/Protocol_decoder:Pjdl) | Embedded/industrial | logic | pjon_link | supported | Padded Jittering Data Link | PJDL, a single wire serial link layer for PJON. |
| [PJON](https://sigrok.org/wiki/Protocol_decoder:Pjon) | Embedded/industrial | pjon_link | — | supported | PJON | The PJON protocol. |
| [PS/2](/w/index.php?title=Protocol_decoder:Ps2&action=edit&redlink=1) | PC | logic | — | supported | PS/2 | PS/2 keyboard/mouse interface. |
| [PWM](https://sigrok.org/wiki/Protocol_decoder:Pwm) | Encoding | logic | — | supported | Pulse-width modulation | Analog level encoded in duty cycle percentage. |
| [Qi](https://sigrok.org/wiki/Protocol_decoder:Qi) | Embedded/industrial, Wireless/RF | logic | — | supported | Qi charger protocol | Protocol used by Qi receiver. |
| [RC encode](https://sigrok.org/wiki/Protocol_decoder:Rc_encode) | IC, IR | logic | — | supported | Remote control encoder | PT2262/HX2262/SC5262 remote control encoder protocol. |
| [RFM12](https://sigrok.org/wiki/Protocol_decoder:Rfm12) | Wireless/RF | spi | — | supported | HopeRF RFM12 | HopeRF RFM12 wireless transceiver control protocol. |
| [RGB LED (SPI)](https://sigrok.org/wiki/Protocol_decoder:Rgb_led_spi) | Display | spi | — | supported | RGB LED string decoder (SPI) | RGB LED string protocol (RGB values clocked over SPI). |
| [RGB LED (WS281x)](/w/index.php?title=Protocol_decoder:Rgb_led_ws281x&action=edit&redlink=1) | Display, IC | logic | — | supported | RGB LED string decoder (WS281x) | RGB LED string protocol (WS281x). |
| [RTC-8564](https://sigrok.org/wiki/Protocol_decoder:Rtc8564) | Clock/timing | i2c | — | supported | Epson RTC-8564 JE/NB | Realtime clock module protocol. |
| [SAE J1850 VPW](https://sigrok.org/wiki/Protocol_decoder:Sae_j1850_vpw) | Automotive | logic | — | supported | SAE J1850 VPW. | SAE J1850 Variable Pulse Width 1x and 4x. |
| [SBUS (Futaba)](https://sigrok.org/wiki/Protocol_decoder:Sbus_futaba) | Remote Control | uart | sbus_futaba | supported | Futaba SBUS (Serial bus) | Serial bus for hobby remote control by Futaba |
| [SDA2506](/w/index.php?title=Protocol_decoder:Sda2506&action=edit&redlink=1) | IC, Memory | logic | — | supported | Siemens SDA 2506-5 | Serial nonvolatile 1-Kbit EEPROM. |
| [SD card (SD mode)](/w/index.php?title=Protocol_decoder:Sdcard_sd&action=edit&redlink=1) | Memory | logic | — | supported | Secure Digital card (SD mode) | Secure Digital card (SD mode) low-level protocol. |
| [SD card (SPI mode)](/w/index.php?title=Protocol_decoder:Sdcard_spi&action=edit&redlink=1) | Memory | spi | — | supported | Secure Digital card (SPI mode) | Secure Digital card (SPI mode) low-level protocol. |
| [SDQ](https://sigrok.org/wiki/Protocol_decoder:Sdq) | Embedded/industrial | logic | — | supported | Texas Instruments SDQ | Texas Instruments SDQ. The SDQ protocol is also used by Apple. |
| [7-segment](/w/index.php?title=Protocol_decoder:Seven_segment&action=edit&redlink=1) | Display | logic | — | supported | 7-segment display | 7-segment display protocol. |
| [Signature](https://sigrok.org/wiki/Protocol_decoder:Signature) | Debug/trace, Util, Encoding | logic | — | supported | Signature analysis | Annotate signature of logic patterns. |
| [SIPI (Zipwire)](/w/index.php?title=Protocol_decoder:Sipi&action=edit&redlink=1) | Embedded/industrial | lfast | none | supported | NXP SIPI interface | Serial Inter-Processor Interface (SIPI) aka Zipwire, aka HSSL |
| [SLE 44xx](https://sigrok.org/wiki/Protocol_decoder:Sle44xx) | Memory | logic | — | supported | SLE44xx memory card | SLE 4418/28/32/42 memory card serial protocol |
| [S/PDIF](https://sigrok.org/wiki/Protocol_decoder:Spdif) | Audio, PC | logic | — | supported | Sony/Philips Digital Interface Format | Serial bus for connecting digital audio devices. |
| [SPI](https://sigrok.org/wiki/Protocol_decoder:Spi) | Embedded/industrial | logic | spi | supported | Serial Peripheral Interface | Full-duplex, synchronous, serial bus. |
| [SPI flash/EEPROM](https://sigrok.org/wiki/Protocol_decoder:Spiflash) | IC, Memory | spi | — | supported | SPI flash/EEPROM chips | xx25 series SPI (NOR) flash/EEPROM chip protocol. |
| [SSI32](/w/index.php?title=Protocol_decoder:Ssi32&action=edit&redlink=1) | Embedded/industrial | spi | — | supported | Synchronous Serial Interface (32bit) | Synchronous Serial Interface (32bit) protocol. |
| [ST25R39xx](/w/index.php?title=Protocol_decoder:St25r39xx&action=edit&redlink=1) | IC, Wireless/RF | spi | — | supported | STMicroelectronics ST25R39xx | High performance NFC universal device and EMVCo reader protocol. |
| [ST7735](/w/index.php?title=Protocol_decoder:St7735&action=edit&redlink=1) | Display, IC | logic | — | supported | Sitronix ST7735 | Sitronix ST7735 TFT controller protocol. |
| [Stepper motor](https://sigrok.org/wiki/Protocol_decoder:Stepper_motor) | Embedded/industrial | logic | — | supported | Stepper motor position / speed | Absolute position and movement speed from step/dir. |
| [SWD](/w/index.php?title=Protocol_decoder:Swd&action=edit&redlink=1) | Debug/trace | logic | swd | supported | Serial Wire Debug | Two-wire protocol for debug access to ARM CPUs. |
| [SWIM](/w/index.php?title=Protocol_decoder:Swim&action=edit&redlink=1) | Debug/trace | logic | — | supported | STM8 SWIM bus | STM8 Single Wire Interface Module (SWIM) protocol. |
| [T55xx](/w/index.php?title=Protocol_decoder:T55xx&action=edit&redlink=1) | IC, RFID | logic | — | supported | RFID T55xx | T55xx 100-150kHz RFID protocol. |
| [TI TCA6408A](/w/index.php?title=Protocol_decoder:Tca6408a&action=edit&redlink=1) | Embedded/industrial, IC | i2c | — | supported | Texas Instruments TCA6408A | Texas Instruments TCA6408A 8-bit I²C I/O expander. |
| [TDM audio](/w/index.php?title=Protocol_decoder:Tdm_audio&action=edit&redlink=1) | Audio | logic | — | supported | Time division multiplex audio | TDM multi-channel audio protocol. |
| [Timing](/w/index.php?title=Protocol_decoder:Timing&action=edit&redlink=1) | Clock/timing, Util | logic | — | supported | Timing calculation with frequency and averaging | Calculate time between edges. |
| [TI TLC5620](https://sigrok.org/wiki/Protocol_decoder:Tlc5620) | IC, Analog/digital | logic | — | supported | Texas Instruments TLC5620 | Texas Instruments TLC5620 8-bit quad DAC. |
| [UART](https://sigrok.org/wiki/Protocol_decoder:Uart) | Embedded/industrial | logic | uart | supported | Universal Asynchronous Receiver/Transmitter | Asynchronous, serial bus. |
| [USB packet](/w/index.php?title=Protocol_decoder:Usb_packet&action=edit&redlink=1) | PC | usb_signalling | usb_packet | supported | Universal Serial Bus (LS/FS) packet | USB (low-speed and full-speed) packet protocol. |
| [USB PD](/w/index.php?title=Protocol_decoder:Usb_power_delivery&action=edit&redlink=1) | PC | logic | usb_pd | supported | USB Power Delivery | USB Power Delivery protocol. |
| [USB request](/w/index.php?title=Protocol_decoder:Usb_request&action=edit&redlink=1) | PC | usb_packet | usb_request | supported | Universal Serial Bus (LS/FS) transaction/request | USB (low-speed/full-speed) transaction/request protocol. |
| [USB signalling](/w/index.php?title=Protocol_decoder:Usb_signalling&action=edit&redlink=1) | PC | logic | usb_signalling | supported | Universal Serial Bus (LS/FS) signalling | USB (low-speed/full-speed) signalling protocol. |
| [Wiegand](/w/index.php?title=Protocol_decoder:Wiegand&action=edit&redlink=1) | Embedded/industrial, RFID | logic | — | supported | Wiegand interface | Wiegand interface for electronic entry systems. |
| [X2444M/P](/w/index.php?title=Protocol_decoder:X2444m&action=edit&redlink=1) | IC, Memory | spi | — | supported | Xicor X2444M/P | Xicor X2444M/P nonvolatile static RAM protocol. |
| [XFP](/w/index.php?title=Protocol_decoder:Xfp&action=edit&redlink=1) | Networking | i2c | — | supported | 10 Gigabit Small Form Factor Pluggable Module (XFP) | XFP I²C management interface structures/protocol |
| [XY2-100](https://sigrok.org/wiki/Protocol_decoder:Xy2-100) | Embedded/industrial | logic | — | supported | XY2-100 and XY2-200 interface | XY2-100 protocol used for laser applications. |
| [Z80](https://sigrok.org/wiki/Protocol_decoder:Z80) | Retro computing | logic | — | supported | Zilog Z80 CPU | Zilog Z80 microprocessor disassembly. |

## Possible candidates for future protocol decoders
| Protocol | Category | Input ID(s) | Output ID(s) | Status | Description | Comments |
|---|---|---|---|---|---|---|
| [AVC-LAN](https://sigrok.org/wiki/Protocol_decoder:Avclan) | Automotive | iebus |  | 100% | The multimedia control protocol used in Toyota and other vehicle brands | Pull request open: [[1]](https://github.com/sigrokproject/libsigrokdecode/pull/106) |
| [IEBus](https://sigrok.org/wiki/Protocol_decoder:Iebus) | Automotive | logic | iebus | 100% | A multidrop differential CAN-like bus used in multimedia applications. | Pull request open: [[2]](https://github.com/sigrokproject/libsigrokdecode/pull/106) |
| SA8807A | Displays | spi |  | 0% | SPI-attached LCD. Datasheet: [Sames SA8807A](http://pdf1.alldatasheet.com/datasheet-pdf/view/36922/SAMES/SA8807A.html). |  |
| EA eDIPTFT43-A | Displays | i2c |  | 0% | I2C-attached LCD. Datasheet: [EA eDIPTFT43-A](http://www.lcd-module.de/pdf/grafik/ediptft43-a.pdf). |  |
| Analog Devices AD7291 | ADC | i2c |  | 0% | I2C-attached ADC. Datasheet: [Analog Devices AD7291](http://pdf1.alldatasheet.com/datasheet-pdf/view/318172/AD/AD7291.html). |  |
| Analog Devices ADS1258 | ADC | spi | ads1258 | 0% | SPI-attached ADC. | Planned (Uwe Hermann). |
| [ccTalk](https://en.wikipedia.org/wiki/ccTalk) | Automation/Industrial | uart | cctalk | 20% | Serial protocol in widespread use throughout the money transaction and point-of-sale industry. | In progress - [https://github.com/plaes/libsigrokdecode/tree/cctalk](https://github.com/plaes/libsigrokdecode/tree/cctalk) |
| Microchip MCP3901 | ADC | spi | mcp3901 | 0% | Can be controlled via a parallel protocol, or SPI, or I2C. | Planned (Uwe Hermann). |
| JTAG / TMPA9xx | Flash/debug | jtag | jtag_tmpa9xx | 0% | Toshiba TMPA9xx specific JTAG protocol details. |  |
| USB transfer | USB | usb_request | usb_transfer | 0% |  |  |
| USB / HID | USB | usb_transfer | usb_hid | 0% |  |  |
| USB / CDC | USB | usb_transfer | usb_cdc | 0% |  |  |
| USB / USBTMC | USB | usb_transfer | usb_usbtmc | 0% |  |  |
| Dallas DS1985 | Other | onewire_network |  | 0% | Dallas DS1985 iButton (1-Wire) device. | Planned (Uwe Hermann). |
| UNI/O | Embedded | — |  | 0% |  |  |
| [SSI](https://en.wikipedia.org/wiki/Synchronous_Serial_Interface) | Embedded | — |  | 0% | Synchronous Serial Interface |  |
| CompactFlash | Memory | — |  | 0% |  |  |
| MMC | Memory | — |  | 0% |  |  |
| Memory Stick | Memory | — |  | 0% |  |  |
| SmartMedia | Memory | — |  | 0% |  |  |
| xD-Picture Card | Memory | — |  | 0% |  |  |
| [ISO 7816](https://en.wikipedia.org/wiki/ISO/IEC_7816) | Smartcards | — |  | 0% |  |  |
| AVR TPI | Flash/debug | — |  | 0% | Atmel Tiny Programming Interface (TPI) protocol. |  |
| FWH | PC | — |  | 0% |  |  |
| ISA | PC | — |  | 0% |  |  |
| PCI | PC | — |  | 0% |  |  |
| SMBus | PC | — |  | 0% |  |  |
| IDE | PC | — |  | 0% |  |  |
| SCSI | PC | — |  | 0% |  |  |
| [PECI](https://en.wikipedia.org/wiki/Platform_Environment_Control_Interface) | PC | — |  | 0% | Platform Environment Control Interface |  |
| [SVID](https://en.wikipedia.org/wiki/SVID) | PC | — |  | 0% | Serial Voltage Identification |  |
| [MFM](https://sigrok.org/wiki/Protocol_decoder:Mfm) | PC | — |  | 90% | Floppy disk FM and [MFM](https://en.wikipedia.org/wiki/Modified_Frequency_Modulation). | Work in progress (David Wiens). |
| HD Audio | Audio | — |  | 0% |  |  |
| Nokia NRC17 | IR | — |  | 0% |  |  |
| Philips RC-MM | IR | — |  | 0% |  |  |
| Philips RECS80 | IR | — |  | 0% |  |  |
| [IrDA](http://en.wikipedia.org/wiki/Infrared_Data_Association) | Misc | — |  | 0% |  |  |
| HD44780 | Displays | — |  | 0% | [HD44780 character LCD](http://en.wikipedia.org/wiki/HD44780_Character_LCD) protocol |  |
| [PCF8814](/w/index.php?title=Protocol_decoder:Pcf8814&action=edit&redlink=1) | Displays | — | pcf8814 | 50% | Philips PCF8814 65 x 96 pixels matrix LCD driver | Work in progress (Uwe Hermann). |
| [PCF8814 LCD](https://sigrok.org/wiki/Protocol_decoder:Pcf8814_lcd) | Displays | pcf8814 | pcf8814_lcd | 50% | Philips PCF8814 65 x 96 pixels matrix LCD driver | Work in progress (Uwe Hermann). |
| [RDM](https://en.wikipedia.org/wiki/RDM_%28lighting%29) | Industrial Lighting | — | rdm | 0% |  |  |
| [NMEA 0183](https://en.wikipedia.org/wiki/NMEA_0183) | GPS | uart | nmea0183 | 0% |  |  |
| [NMEA2000](https://sigrok.org/wiki/Protocol_decoder:Nmea2000) | Marine | can | nmea2000 | 0% | [NMEA 2000 Wikipedia page](https://en.wikipedia.org/wiki/NMEA_2000) |  |
| [DCC](https://en.wikipedia.org/wiki/Digital_Command_Control) | Trains | — | dcc | 0% |  |  |
| [MVB](https://en.wikipedia.org/wiki/Train_Communication_Network) | Trains | — | mvb | 90% | Multifunction Vehicle Bus | Working in separate [repository](https://github.com/yeckel/sigrok_mvb_decoder/) (Libor Tomsik). |
| [WTB](https://en.wikipedia.org/wiki/Train_Communication_Network) | Trains | — | wtb | 0% | Wire Train Bus |  |
| [C-Bus](https://en.wikipedia.org/wiki/C-Bus_%28protocol%29) | Home automation | — | cbus | 0% |  |  |
| [X10](https://en.wikipedia.org/wiki/X10_%28industry_standard%29) | Home automation | — | x10 | 0% |  |  |
| [LonWorks](https://en.wikipedia.org/wiki/LonWorks) | Home automation | — | lonworks | 0% |  |  |
| [M-Bus](https://en.wikipedia.org/wiki/Meter-Bus) | Automation | — | mbus | 0% |  |  |
| [Modbus ASCII](https://en.wikipedia.org/wiki/Modbus) | Automation | uart | modbus | 0% |  |  |
| [Modbus TCP](https://en.wikipedia.org/wiki/Modbus) | Automation | ip | modbus | 0% |  |  |
| [HART protocol](https://en.wikipedia.org/wiki/Highway_Addressable_Remote_Transducer_Protocol) | Automation | — | hart | 0% |  |  |
| [INTERBUS](https://en.wikipedia.org/wiki/INTERBUS) | Automation | — | interbus | 0% |  |  |
| [DirectNET](https://en.wikipedia.org/wiki/DirectNET_Protocol) | Automation | uart | directnet | 0% |  |  |
| [KNX](https://en.wikipedia.org/wiki/KNX_%28standard%29) | Automation | various | knx | 0% |  |  |
| [BACnet](https://en.wikipedia.org/wiki/Bacnet) | Automation |  | bacnet | 0% |  |  |
| [OpenTherm](https://en.wikipedia.org/wiki/OpenTherm) | Automation | — | opentherm | 0% |  |  |
| [EBUS](https://en.wikipedia.org/wiki/EBUS_%28serial_buses%29) | Automation | uart | ebus | 0% |  |  |
| [AUI](https://en.wikipedia.org/wiki/Attachment_Unit_Interface) | Networking | — | aui | 0% | Attachment Unit Interface |  |
| [MDI](https://en.wikipedia.org/wiki/Medium_Dependent_Interface) | Networking | — | mdi | 0% | Medium Dependent Interface |  |
| [MII](https://en.wikipedia.org/wiki/Media_Independent_Interface) | Networking | — | mii | 0% | Media Independent Interface |  |
| [GMII](https://en.wikipedia.org/wiki/Gigabit_Media_Independent_Interface#Gigabit_Media_Independent_Interface) | Networking | — | gmii | 0% | Gigabit Media Independent Interface |  |
| [XGMII](https://en.wikipedia.org/wiki/10_Gigabit_Media_Independent_Interface#10_Gigabit_Media_Independent_Interface) | Networking | — | xgmii | 0% | 10 Gigabit Media Independent Interface |  |
| [ESP8266](https://sigrok.org/wiki/Protocol_decoder:Esp8266) | Wireless | uart | esp8266 | 0% | WiFi Serial Transceiver |  |
| [TMDS (HDMI / DVI Pixel Data)](/w/index.php?title=Protocol_decoder:Tmds&action=edit&redlink=1) | Display | tmds | — | 1% | [https://github.com/mithro/tmds_encoding](https://github.com/mithro/tmds_encoding) | Work in progress ([mithro](/w/index.php?title=User:Mithro&action=edit&redlink=1)) |
| [Easymatic](https://sigrok.org/wiki/Protocol_decoder:Easymatic) | Home automation | uart | easymatic | 10% |  | Work in progress (Platypus) |
| [DDC/CI](/w/index.php?title=Protocol_decoder:DDC/CI&action=edit&redlink=1) | PC | i2c | — | 0% |  |  |
| Kenwood VH | Misc | — | — | 50% | SYSTEM CONTROL protocol used by Kenwood's VH HiFi-system | In progress: [https://github.com/kripton/libsigrokdecode/compare/kenwood_vh](https://github.com/kripton/libsigrokdecode/compare/kenwood_vh) |
| IEC 61131-9 | Industrial | — | — | 0% | "Single-drop digital communication interface for small sensors and actuators (SDCI, marketed as IO-Link)" [https://en.wikipedia.org/wiki/IEC_61131](https://en.wikipedia.org/wiki/IEC_61131) |  |
| NRZ encoding family | — | — | — | 0% | Non-Return-to-Zero and its [variants](https://en.wikipedia.org/wiki/Non-return-to-zero#Variants) | whoever wants it |
| Bi-Phase encoding family | — | — | — | 0% | [several variations](http://ckp.made-it.com/encodingschemes.html) of codes, including [Manchester code](https://en.wikipedia.org/wiki/Manchester_code) | whoever wants it |
| Sony LANC | — | — | — | 0% | [Sony LANC](http://www.boehmel.de/lanc.htm) | whoever wants it, contact [AlexDaniel](https://sigrok.org/wiki/User:Alexdaniel) for more info. You can already decode the raw data by using UART with 9600 baud and no parity, but it'd be better if pulseview displayed the meaning (as in what these commands do) |
| CCD (Chrysler's Collision Detection) | — | — | — | 99% | CCD (Chrysler's Collision Detection) is internal bus used on Chrysler cars produced about 1990-2000. | It works, but decodes only subset of all possible CCD messages, mostly from Jeep ZJ '98. Need a little work to improve performance and better support of API 3. [https://github.com/majekw/sigrok-ccd-pd](https://github.com/majekw/sigrok-ccd-pd) |
| Mate-trac | — | (bi-phase) | — | 0% | 20th century protocol for remote control of projectors, often stored on audio tapes; [described well by Adrian McCarthy](https://www.aidtopia.com/mccarthy/aid/multi-image/matetrac.html) | whoever wants it, possibly [chrysn](/w/index.php?title=User:Chrysn&action=edit&redlink=1) |
| PN532 NFC reader communication protocol | NFC | uart / spi / i2c | ISO14443 | 80% | PN532 is a 13.56 MHz NFC reader, supporting SPI, I2C or Serial UART | WIP for Serial UART: [https://github.com/plaes/libsigrokdecode/tree/pn542-uart](https://github.com/plaes/libsigrokdecode/tree/pn542-uart) based on [code from this repository](https://git.mittelab.org/wifasoi/sigrokdecode-pn532) |
| SAE J2716 SENT | Automotive | — |  | 0% | SENT - Single Edge Nibble Transmission for Automotive Applications |  |

