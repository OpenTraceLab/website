# OpenTraceLab Website & Documentation

Welcome to the **OpenTraceLab** documentation repository.  
This repo contains the sources for the OpenTraceLab website and user/developer documentation, built using [MkDocs](https://www.mkdocs.org/) with the [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) theme.

OpenTraceLab is an open-source ecosystem for logic analysis, based on a fork of the [sigrok](https://sigrok.org) project.  
It consists of:

- **OpenTraceCapture** – the capture engine and device backends (fork of sigrok)  
- **OpenTraceView** – the graphical user interface for visualizing signals (fork of OpenTraceView)  
- **OpenTraceDecode** – protocol decoders (fork of sigrok-decode)  

This repo provides **end-user documentation, developer guides, and community information** for the whole OpenTraceLab ecosystem.

---

## 📖 Documentation

### Local Development

Start local server while writing:

```bash
pip install -r requirements.txt
mkdocs serve
```

Open your browser at http://127.0.0.1:8000 to preview.

### Publishing Versions

**First version publish (manual):**

```bash
# Build and publish version 1.0, set 'latest' alias, make default:
mike deploy 1.0 latest
mike set-default latest
git push origin gh-pages
```

**After adopting tag-based CI, just create a tag:**

```bash
git tag v1.1
git push origin v1.1
```

The workflow will run and publish 1.1 as a new version + update latest.

See [Material's versioning docs](https://squidfunk.github.io/mkdocs-material/setup/setting-up-versioning/) and [mike documentation](https://github.com/jimporter/mike) for reference.

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


