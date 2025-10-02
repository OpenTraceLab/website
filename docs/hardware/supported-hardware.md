# Supported Hardware

OpenTraceLab supports a wide range of test and measurement devices across multiple categories. This page provides an overview of all supported hardware with status indicators, specifications, and links to detailed documentation.

{% set hw = load_yaml('hardware.yaml') %}
{{ hardware_tables(hw) }}

## Status Legend

- **supported** - Fully functional with stable drivers
- **experimental** - Working but may have limitations
- **wip** - Work in progress, basic functionality available
- **untested** - Driver exists but not thoroughly tested

## Contributing

Found a device that should be supported? Check our [contributing guide](../community/contributing.md) to learn how to add support for new hardware.
