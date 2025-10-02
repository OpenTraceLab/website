# Installation
## Quick Install
### Linux
**Distribution packages:**
```bash
# Ubuntu/Debian
sudo apt install opentracelab
# Fedora
sudo dnf install opentracelab
# Arch Linux
sudo pacman -S opentracelab
```
**AppImage (recommended for latest version):**
```bash
# Download and run
chmod +x OpenTraceView-NIGHTLY-x86_64.AppImage
./OpenTraceView-NIGHTLY-x86_64.AppImage
```
### Windows
1. Download the Windows installer from [GitHub Releases](https://github.com/OpenTraceLab/opentracelab/releases)
2. Run the installer as Administrator
3. Launch OpenTraceView from the Start Menu
### macOS
```bash
# Using Homebrew
brew install opentracelab
# Or download the .dmg from GitHub Releases
```
## Building from Source

### Prerequisites

**Ubuntu/Debian:**
```bash
sudo apt install build-essential meson ninja-build pkg-config git \
  libglib2.0-dev libglibmm-2.4-dev libzip-dev libusb-1.0-0-dev \
  libftdi1-dev libserialport-dev libhidapi-dev python3-dev \
  qt6-base-dev qt6-svg-dev libboost-serialization-dev libboost-system-dev
```

**Fedora/RHEL:**
```bash
sudo dnf install gcc-c++ meson ninja-build pkgconfig git \
  glib2-devel glibmm24-devel libzip-devel libusb1-devel \
  libftdi-devel libserialport-devel hidapi-devel python3-devel \
  qt6-qtbase-devel qt6-qtsvg-devel boost-devel
```

**macOS (with Homebrew):**
```bash
brew install meson ninja pkg-config git glib glibmm libzip libusb \
  libftdi libserialport hidapi python3 qt6 boost
```

### Build All Components

```bash
# 1. OpenTraceCapture (core library)
git clone https://github.com/OpenTraceLab/OpenTraceCapture.git
cd OpenTraceCapture
meson setup build --buildtype=release
meson compile -C build
sudo meson install -C build
cd ..

# 2. OpenTraceDecode (protocol decoders)
git clone https://github.com/OpenTraceLab/OpenTraceDecode.git
cd OpenTraceDecode  
meson setup build --buildtype=release
meson compile -C build
sudo meson install -C build
cd ..

# 3. OpenTraceView (GUI application)
git clone https://github.com/OpenTraceLab/OpenTraceView.git
cd OpenTraceView
meson setup builddir --buildtype=release
meson compile -C builddir
sudo meson install -C builddir
```

### Build Options

**OpenTraceCapture options:**
```bash
# Enable all optional features
meson setup build -Dwith_nettle=enabled -Dwith_ieee1284=enabled -Dwith_gpib=enabled

# Custom installation prefix
meson setup build --prefix=/usr/local
```

**OpenTraceDecode options:**
```bash
# Disable Python support (C API only)
meson setup build -Dpython=disabled

# Specify minimum Python version
meson setup build -Dpython_minver=3.8
```

**OpenTraceView options:**
```bash
# Disable protocol decoding
meson setup builddir -Ddecode=false

# Enable debug stacktraces
meson setup builddir -Dstacktrace=true
```
## Device Access
### Linux udev Rules
For USB device access, install udev rules:
```bash
sudo cp contrib/60-opentracelab.rules /etc/udev/rules.d/
sudo udevadm control --reload-rules
sudo udevadm trigger
```
Add your user to the `plugdev` group:
```bash
sudo usermod -a -G plugdev $USER
```
Log out and back in for changes to take effect.
## Troubleshooting
### Cannot access USB device
- Install udev rules (Linux)
- Run as Administrator (Windows)
- Check device permissions
### Library not found
```bash
sudo ldconfig
# Or set LD_LIBRARY_PATH
export LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH
```
### Python module errors
```bash
# Ensure Python development packages are installed
sudo apt install python3-dev python3-setuptools
```
## Next Steps
- [Capture your first trace](capture-first-trace.md)
- Check [supported hardware](../opentracecapture/overview.md)
- Explore [protocol decoders](../opentracedecode/overview.md)
