# OpenTraceLab Website & Documentation

Welcome to the **OpenTraceLab** documentation repository.  
This repo contains the sources for the OpenTraceLab website and user/developer documentation, built using [MkDocs](https://www.mkdocs.org/) with the [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) theme.

OpenTraceLab is an open-source ecosystem for logic analysis, based on a fork of the [sigrok](https://sigrok.org) project.  
It consists of:

- **OpenTraceCapture** – the capture engine and device backends (fork of sigrok)  
- **OpenTraceView** – the graphical user interface for visualizing signals (fork of PulseView)  
- **OpenTraceDecode** – protocol decoders (fork of sigrok-decode)  

This repo provides **end-user documentation, developer guides, and community information** for the whole OpenTraceLab ecosystem.

---

## 📖 Documentation

To build and serve the documentation locally:

```bash
# Install mkdocs and theme
pip install mkdocs mkdocs-material

# Clone the repository
git clone https://github.com/OpenTraceLab/website.git
cd website

# Start local server
mkdocs serve
```

Open your browser at http://127.0.0.1:8000 to preview.

To generate a static site:

```bash
mkdocs build
# Start local server
mkdocs serve
```

This will produce the site in the site/ directory, which can be deployed to GitHub Pages or any static host.

## 🌐 Live Website

When published, the website will be available at:
GitHub Pages: https://opentracelab.github.io/website/
Custom domain (planned): https://opentrace.io

## 🤝 Contributing

We welcome contributions! Please see the CONTRIBUTING.md
 (to be added) for guidelines on how to:

Report issues

Suggest improvements

Submit pull requests

## 📜 License

The documentation in this repository is licensed under the
Creative Commons Attribution-ShareAlike 4.0 International (CC-BY-SA 4.0)

Portions of this documentation are adapted from the sigrok project originally licensed under CC-BY-SA 3.0

Attribution has been preserved where required.

Project logos, branding, and artwork are © 2025 OpenTraceLab contributors, and may be licensed separately.

## 📬 Community

GitHub: OpenTraceLab
Discussions: (planned)
Issue Tracker: OpenTraceLab/website Issues

## 🧪 About OpenTraceLab

OpenTraceLab is an open-source initiative to modernize and extend the capabilities of logic analyzers and protocol decoding, building upon the foundations of the sigrok ecosystem.

It is free software: you can redistribute it and/or modify it under the terms of the GNU GPLv3 for code, and CC-BY-SA for documentation.


