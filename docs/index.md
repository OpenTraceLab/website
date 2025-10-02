# OpenTraceLab
OpenTraceLab is an open-source ecosystem for logic analysis, based on a fork of the [sigrok](https://sigrok.org) project.
## Components
- **[OpenTraceCapture](opentracecapture/overview.md)** – Logic analyzer capture engine and device backends
- **[OpenTraceView](opentraceview/overview.md)** – Graphical user interface for visualizing signals
- **[OpenTraceDecode](opentracedecode/overview.md)** – Protocol decoders for analyzing captured data
- **[OpenTraceBroadcaster](opentracebroadcaster/overview.md)** – OBS Studio plugin for real-time measurement overlays
## Quick Start
1. **[Install OpenTraceLab](get-started/install.md)** on your system
2. **[Capture your first trace](get-started/capture-first-trace.md)** with a logic analyzer
3. **[Explore protocol decoders](opentracedecode/overview.md)** to analyze your data
## Use Cases
OpenTraceLab supports a wide range of signal analysis applications:
- **Digital signal analysis** with logic analyzers
- **Protocol debugging** for I2C, SPI, UART, and 100+ other protocols
- **Embedded system development** and reverse engineering
- **Hardware validation** and testing
- **Live streaming** with real-time measurement overlays

## High level architecture
``` mermaid
graph TD
    OV[OpenTraceView<br/>GUI Qt6, no Boost] --> OC
    OC[OpenTraceCapture<br/>Core Library] --> USB[libusb]
    OC --> SER[libserialport]
    OC --> NET[TCP/IP Sockets]
    OV --> OD
    CLI[OpenTraceCLI<br/>Command Line] --> OC
    CLI --> OD

    OD[OpenTraceDecode<br/>Decoder Library Python runtime]
    subgraph Decoders
      PD1[Protocol Decoders<br/>Python modules]
      PD2[Utility/Shared Blocks]
    end
    OD --> PD1
    OD --> PD2


    USB --> DAQ[Logic Analyzers<br/>Function Generators]
    SER --> DMM[Multimeters<br/>Power Supplies]
    NET --> OSC[Oscilloscopes<br/>LCR/SCPI Instruments]

    OC -. samples/frames .-> OV
    OC -. samples/frames .-> CLI
    OV -. decoded buses/fields .-> OD
    CLI -. decoded streams .-> OD

    subgraph Build & Runtime
      Q6[Qt6 Widgets/QPA/QML*]
      MES[Meson + Ninja]
      PY[Embedded Python / CPython]
      NOBOOST[No Boost removed]
    end
    OV --- Q6
    OV --- MES
    OD --- PY
    OC --- MES
    NOBOOST --- OV

    style OC fill:#4f46e5,stroke:#312e81,stroke-width:3px,color:#fff
    style OD fill:#0ea5e9,stroke:#075985,stroke-width:2px,color:#fff
    style OV fill:#f8fafc,stroke:#4f46e5,color:#1e293b
    style CLI fill:#f8fafc,stroke:#4f46e5,color:#1e293b
    style USB fill:#e0f2fe,stroke:#0284c7,color:#0c4a6e
    style SER fill:#e0f2fe,stroke:#0284c7,color:#0c4a6e
    style NET fill:#e0f2fe,stroke:#0284c7,color:#0c4a6e
    style DAQ fill:#fef3c7,stroke:#b45309,color:#7c2d12
    style DMM fill:#fef3c7,stroke:#b45309,color:#7c2d12
    style OSC fill:#fef3c7,stroke:#b45309,color:#7c2d12
    style PD1 fill:#dcfce7,stroke:#15803d,color:#064e3b
    style PD2 fill:#dcfce7,stroke:#15803d,color:#064e3b
    style Q6 fill:#e5e7eb,stroke:#6b7280,color:#111827
    style MES fill:#e5e7eb,stroke:#6b7280,color:#111827
    style PY fill:#e5e7eb,stroke:#6b7280,color:#111827
    style NOBOOST fill:#fee2e2,stroke:#b91c1c,color:#7f1d1d
```
## Community
- **[Contributing](community/contributing.md)** - Help improve OpenTraceLab
- **[Code of Conduct](community/code-of-conduct.md)** - Community guidelines
- **[GitHub](https://github.com/OpenTraceLab)** - Source code and issues
<!-- Updated Tue Sep 30 03:51:12 +07 2025 -->
