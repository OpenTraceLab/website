# Contributing to OpenTraceLab
We welcome contributions from everyone! OpenTraceLab is a community-driven project that benefits from diverse perspectives and expertise.
## Ways to Contribute
### 🐛 Report Bugs
- Use the "Report Issue" button on any documentation page
- Create detailed GitHub issues with reproduction steps
- Include system information and sample files when relevant
### 📝 Improve Documentation
- Fix typos and improve clarity
- Add examples and tutorials
- Translate content to other languages
- Update outdated information
### 💻 Contribute Code
- Fix bugs and improve performance
- Add new features and capabilities
- Write protocol decoders
- Improve device drivers
### 🧪 Test and Validate
- Test new releases and features
- Validate hardware compatibility
- Provide feedback on user experience
- Report performance issues
### 🎓 Help Others
- Answer questions in discussions
- Help troubleshoot issues
- Share knowledge and best practices
- Mentor new contributors
## Getting Started
### 1. Set Up Development Environment
**Clone repositories:**
```bash
# Main documentation
git clone https://github.com/OpenTraceLab/website
cd website
# Core components
git clone https://github.com/OpenTraceLab/opentracecapture
git clone https://github.com/OpenTraceLab/opentraceview
git clone https://github.com/OpenTraceLab/opentracedecode
```
**Install dependencies:**
```bash
# Documentation (this site)
pip install -r requirements.txt
mkdocs serve
# Core libraries - see installation guide
sudo apt install build-essential cmake libglib2.0-dev libusb-1.0-0-dev
```
### 2. Find Something to Work On
**Good first issues:**
- Documentation improvements
- Simple bug fixes
- Protocol decoder enhancements
- Test case additions
**Check these resources:**
- GitHub Issues labeled "good first issue"
- [Roadmap](../about/roadmap.md) for planned features
- Community discussions for ideas
- [FAQ](../get-started/faq.md) for common problems
### 3. Make Your Changes
**Follow our guidelines:**
- Write clear, descriptive commit messages
- Include tests for new functionality
- Update documentation as needed
- Follow existing code style
**Test your changes:**
```bash
# Documentation
mkdocs serve  # Test locally
# Code changes
make check    # Run unit tests
make install  # Test installation
```
## Contribution Guidelines
### Code Style
**C/C++ Code:**
- Follow existing style in the codebase
- Use descriptive variable names
- Add comments for complex logic
- Keep functions focused and small
**Python Code (Decoders):**
- Follow PEP 8 style guidelines
- Use type hints where appropriate
- Include docstrings for public functions
- Write comprehensive test cases
**Documentation:**
- Use clear, concise language
- Include code examples
- Add screenshots for UI features
- Follow Markdown best practices
### Commit Messages
Use clear, descriptive commit messages:
```
component: Brief description of change
Longer explanation of what changed and why.
Include any relevant issue numbers.
Fixes #123
```
Examples:
```
docs: Add protocol decoder development guide
opentraceview: Fix crash when loading large files
opentracedecode: Add support for USB HID protocol
```
### Pull Request Process
1. **Fork the repository** on GitHub
2. **Create a feature branch** from main
3. **Make your changes** with clear commits
4. **Test thoroughly** on your system
5. **Submit pull request** with description
6. **Respond to feedback** from reviewers
7. **Celebrate** when merged! 🎉
**Pull request template:**
```markdown
## Description
Brief description of changes
## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Performance improvement
## Testing
- [ ] Tested on Linux
- [ ] Tested on Windows
- [ ] Tested on macOS
- [ ] Added/updated tests
## Checklist
- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Documentation updated
- [ ] No breaking changes
```
## Specific Contribution Areas
### Protocol Decoders
**High-priority protocols:**
- USB (HID, CDC, Mass Storage)
- Ethernet protocols
- Automotive diagnostics (OBD-II, UDS)
- IoT protocols (LoRaWAN, Zigbee)
**Decoder development:**
1. **Study the protocol** - Read specifications and examples
2. **Create decoder skeleton** - Use existing decoders as templates
3. **Implement decode logic** - Handle all protocol states
4. **Add comprehensive tests** - Cover edge cases and errors
5. **Write documentation** - Usage examples and parameter descriptions
See our [Protocol Decoder HOWTO](../opentracedecode/decoder-howto.md) for detailed guidance.
### Device Drivers
**Popular device requests:**
- Newer Saleae Logic analyzers
- High-speed USB 3.0 devices
- Wireless logic analyzers
- Mixed-signal analyzers
**Driver development:**
1. **Understand the hardware** - Study datasheets and protocols
2. **Implement basic communication** - Device detection and configuration
3. **Add capture functionality** - Data acquisition and streaming
4. **Handle edge cases** - Error conditions and recovery
5. **Test thoroughly** - Various configurations and scenarios
### User Interface
**OpenTraceView improvements:**
- Performance optimizations
- Usability enhancements
- New visualization features
- Accessibility improvements
**Design principles:**
- Keep interfaces intuitive
- Maintain consistency with existing UI
- Consider accessibility requirements
- Test with real users
### Documentation
**High-impact areas:**
- Getting started tutorials
- Protocol-specific guides
- Troubleshooting documentation
- API reference improvements
**Documentation standards:**
- Write for your audience (beginner vs expert)
- Include practical examples
- Use screenshots and diagrams
- Keep content up-to-date
## Community Guidelines
### Communication
**Be respectful and inclusive:**
- Welcome newcomers and help them get started
- Provide constructive feedback
- Assume good intentions
- Follow our [Code of Conduct](code-of-conduct.md)
**Effective communication:**
- Ask questions when unclear
- Provide context for issues
- Share knowledge and resources
- Celebrate others' contributions
### Getting Help
**Stuck on something?**
- Check existing documentation and issues
- Ask in GitHub Discussions
- Join community chat channels
- Reach out to maintainers
**Mentorship:**
- New contributors can request mentorship
- Experienced contributors encouraged to mentor
- Pair programming sessions available
- Regular community calls for discussion
## Recognition
### Contributor Recognition
**We recognize contributions through:**
- Contributor lists in repositories
- Release notes acknowledgments
- Community highlights
- Conference presentations
**Types of recognition:**
- Code contributors
- Documentation writers
- Bug reporters
- Community helpers
- Hardware testers
### Maintainer Path
**Becoming a maintainer:**
1. **Consistent contributions** - Regular, quality contributions
2. **Community involvement** - Help others and participate in discussions
3. **Technical expertise** - Deep knowledge of project areas
4. **Leadership skills** - Guide project direction and mentor others
**Maintainer responsibilities:**
- Review and merge pull requests
- Triage issues and bugs
- Guide project roadmap
- Mentor new contributors
## Legal Considerations
### Licensing
**All contributions must be compatible with:**
- GPL-3.0-or-later for code
- CC-BY-SA 4.0 for documentation
**By contributing, you agree to:**
- License your contributions under project licenses
- Grant necessary rights for project use
- Ensure you have rights to contribute the code
### Copyright
**Copyright assignment:**
- Contributors retain copyright to their contributions
- Grant project rights to use and distribute
- Include appropriate copyright notices
## Resources
### Development Resources
- **[Installation Guide](../get-started/install.md)** - Set up development environment
- **[API References](https://opentracelab.org/api/)** - Complete API documentation
### Community Resources
- **[GitHub Discussions](https://github.com/OpenTraceLab/website/discussions)** - Community forum
- **[Issue Tracker](https://github.com/OpenTraceLab/website/issues)** - Bug reports and features
- **[Roadmap](../about/roadmap.md)** - Project direction and priorities
## Questions?
**Need help getting started?**
- Create a GitHub Discussion
- Use the "Report Issue" button for documentation questions
- Join our community chat
- Email maintainers directly
**Want to propose a major change?**
- Start with a GitHub Discussion
- Create a design document
- Get community feedback
- Submit implementation plan
Thank you for contributing to OpenTraceLab! Together, we're making digital signal analysis accessible to everyone. 🚀
