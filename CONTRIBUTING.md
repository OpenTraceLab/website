# Contributing to OpenTraceLab Documentation

Thank you for your interest in contributing to OpenTraceLab documentation!

## Local Development

Start local server while writing:

```bash
pip install -r requirements.txt
mkdocs serve
```

Open your browser at http://127.0.0.1:8000 to preview changes.

## Publishing Versions

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

## Edit/View Source Buttons

Already enabled in mkdocs.yml:

```yaml
theme:
  features:
    - content.action.edit
    - content.action.view
```

Use the "Edit this page" button on any documentation page to quickly contribute changes.

## Report Issues

Use the floating "Report issue" button on any page to create GitHub issues with automatic page context and selected text inclusion.

## References

- [Material's versioning docs](https://squidfunk.github.io/mkdocs-material/setup/setting-up-versioning/)
- [mike documentation](https://github.com/jimporter/mike)
