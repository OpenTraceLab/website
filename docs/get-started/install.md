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

### Requirements

**Ubuntu/Debian:**
```bash
sudo apt-get install git gcc make cmake autoconf automake libtool \
  pkg-config libglib2.0-dev libzip-dev libusb-1.0-0-dev libftdi1-dev \
  python3-dev python3-setuptools python3-numpy python3-scipy \
  qtbase5-dev qtchooser qt5-qmake qtbase5-dev-tools libqt5svg5-dev
```

**Fedora:**
```bash
sudo dnf install git gcc make cmake autoconf automake libtool \
  pkgconfig glib2-devel libzip-devel libusb1-devel libftdi-devel \
  python3-devel python3-setuptools python3-numpy python3-scipy \
  qt5-qtbase-devel qt5-qtsvg-devel
```

### Build Script (Recommended)

```bash
git clone https://github.com/OpenTraceLab/opentracelab-util
cd opentracelab-util/cross-compile/linux
./opentracelab-cross-linux
```

This installs to `$HOME/sr`. Add to your PATH:
```bash
export PATH=$HOME/sr/bin:$PATH
export LD_LIBRARY_PATH=$HOME/sr/lib:$LD_LIBRARY_PATH
```

### Manual Build

```bash
# 1. libserialport
git clone https://github.com/OpenTraceLab/libserialport
cd libserialport
./autogen.sh
./configure
make
sudo make install

# 2. OpenTraceCapture
git clone https://github.com/OpenTraceLab/opentraceCapture
cd opentraceCapture
./autogen.sh
./configure
make
sudo make install

# 3. OpenTraceDecode
git clone https://github.com/OpenTraceLab/opentraceDecode
cd opentraceDecode
./autogen.sh
./configure
make
sudo make install

# 4. OpenTraceView
git clone https://github.com/OpenTraceLab/opentraceView
cd opentraceView
cmake .
make
sudo make install
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
