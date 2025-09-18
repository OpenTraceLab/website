# License

## Software License

OpenTraceLab software components are licensed under the **GNU General Public License v3.0 (GPL-3.0)**.

### What this means:
- ✅ **Free to use** - Use OpenTraceLab for any purpose
- ✅ **Free to modify** - Change the code to suit your needs  
- ✅ **Free to distribute** - Share OpenTraceLab with others
- ✅ **Commercial use** - Use in commercial products and services
- ⚠️ **Copyleft** - Derivative works must also be GPL-3.0 licensed
- ⚠️ **Source disclosure** - Must provide source code when distributing

### GPL-3.0 Summary

The GPL-3.0 ensures that OpenTraceLab remains free and open source. Key requirements:

1. **Source code availability** - Source must be provided with binaries
2. **License preservation** - GPL license must be included
3. **Modification disclosure** - Changes must be documented
4. **Patent protection** - Contributors grant patent rights
5. **No additional restrictions** - Cannot add further limitations

## Documentation License

OpenTraceLab documentation is licensed under **Creative Commons Attribution-ShareAlike 4.0 International (CC-BY-SA 4.0)**.

### What this means:
- ✅ **Share** - Copy and redistribute in any medium or format
- ✅ **Adapt** - Remix, transform, and build upon the material
- ✅ **Commercial use** - Use for commercial purposes
- ⚠️ **Attribution** - Must give appropriate credit
- ⚠️ **ShareAlike** - Derivatives must use same license

## Component Licenses

### OpenTraceCapture (libsigrok)
- **License:** GPL-3.0-or-later
- **Repository:** [github.com/OpenTraceLab/opentracecapture](https://github.com/OpenTraceLab/opentracecapture)

### OpenTraceView (PulseView)
- **License:** GPL-3.0-or-later  
- **Repository:** [github.com/OpenTraceLab/opentraceview](https://github.com/OpenTraceLab/opentraceview)

### OpenTraceDecode (libsigrokdecode)
- **License:** GPL-3.0-or-later
- **Repository:** [github.com/OpenTraceLab/opentracedecode](https://github.com/OpenTraceLab/opentracedecode)

### Protocol Decoders
- **License:** GPL-2.0-or-later (individual decoders may vary)
- **Location:** `decoders/` directory in OpenTraceDecode

## Third-Party Dependencies

OpenTraceLab uses various third-party libraries, each with their own licenses:

### Core Dependencies
- **Qt** - LGPL-3.0 (GUI framework)
- **libusb** - LGPL-2.1 (USB device access)
- **libserialport** - LGPL-3.0 (serial port access)
- **Python** - PSF License (decoder runtime)
- **glib** - LGPL-2.1 (utility library)

### Build Dependencies
- **CMake** - BSD-3-Clause (build system)
- **pkg-config** - GPL-2.0 (configuration tool)
- **SWIG** - GPL-3.0 (language bindings)

## Firmware Licenses

Some supported devices require firmware uploads:

### fx2lafw
- **License:** GPL-2.0-or-later
- **Description:** Open source firmware for FX2-based logic analyzers
- **Repository:** [github.com/OpenTraceLab/fx2lafw](https://github.com/OpenTraceLab/fx2lafw)

### Device-Specific Firmware
- Various licenses depending on manufacturer
- See individual device documentation for details

## Trademark and Branding

### OpenTraceLab Name and Logo
- **Copyright:** © 2025 OpenTraceLab contributors
- **Usage:** Community use encouraged, commercial use requires permission
- **Guidelines:** Maintain association with open source project

### sigrok Attribution
- OpenTraceLab is based on the sigrok project
- sigrok name and trademarks remain property of sigrok project
- Appropriate attribution maintained in source code and documentation

## Patent Considerations

### GPL-3.0 Patent Grant
The GPL-3.0 includes explicit patent protection:
- Contributors grant patent rights for their contributions
- Patent retaliation clause protects against patent litigation
- Ensures freedom to use, modify, and distribute

### Third-Party Patents
- Users responsible for patent compliance in their jurisdiction
- OpenTraceLab project does not provide patent indemnification
- Consult legal counsel for commercial patent concerns

## Export Control

### Software Export
- OpenTraceLab software is generally not subject to export controls
- Encryption components may have restrictions in some jurisdictions
- Users responsible for compliance with local export laws

### Hardware Considerations
- Logic analyzers may be subject to export controls
- High-speed devices may have additional restrictions
- Check regulations before international shipping

## Compliance Guidelines

### For Users
1. **Include license** - Provide GPL-3.0 text with distributions
2. **Provide source** - Make source code available
3. **Document changes** - Note modifications made
4. **Respect trademarks** - Use OpenTraceLab name appropriately

### For Distributors
1. **Complete source** - Include all source code and build scripts
2. **License compatibility** - Ensure all components are GPL-compatible
3. **Clear attribution** - Maintain copyright notices
4. **User rights** - Inform users of their GPL rights

### For Commercial Users
1. **Internal use** - No restrictions on internal company use
2. **Distribution** - Must comply with GPL when distributing
3. **Linking** - Dynamic linking generally permitted
4. **Consulting** - Consider legal review for complex scenarios

## Getting Help

### License Questions
- **General questions:** Use GitHub Discussions
- **Commercial licensing:** Contact project maintainers
- **Legal advice:** Consult qualified legal counsel
- **Compliance issues:** Report via GitHub Issues

### Resources
- **GPL-3.0 Full Text:** [gnu.org/licenses/gpl-3.0.html](https://www.gnu.org/licenses/gpl-3.0.html)
- **CC-BY-SA 4.0 Full Text:** [creativecommons.org/licenses/by-sa/4.0/](https://creativecommons.org/licenses/by-sa/4.0/)
- **FSF GPL FAQ:** [gnu.org/licenses/gpl-faq.html](https://www.gnu.org/licenses/gpl-faq.html)

## License Compatibility

### Compatible Licenses
- GPL-2.0-or-later (can upgrade to GPL-3.0)
- LGPL-2.1, LGPL-3.0 (can link with GPL code)
- BSD, MIT, Apache 2.0 (can incorporate into GPL projects)

### Incompatible Licenses
- GPL-2.0-only (cannot upgrade to GPL-3.0)
- Proprietary licenses (cannot combine with GPL)
- Some copyleft licenses with different terms

The license information provided here is for informational purposes only and does not constitute legal advice. For specific legal questions, please consult qualified legal counsel.
