import html
import yaml
from pathlib import Path

def define_env(env):
    """Define macros and filters for mkdocs-macros"""
    
    def esc(x): 
        return html.escape(str(x)) if x is not None else ""

    STATUS_CLASS = {
        "supported": "ok", "stable": "ok",
        "experimental": "exp", "alpha": "exp", "beta": "exp",
        "untested": "untested",
        "wip": "wip", "in progress": "wip",
        "deprecated": "deprecated",
        "broken": "broken", "unsupported": "broken",
    }

    def status_badge(val: str) -> str:
        if not val: return ""
        cls = STATUS_CLASS.get(val.strip().lower(), "neutral")
        return f'<span class="hw-badge hw-{cls}" title="{esc(val)}">{esc(val)}</span>'

    @env.macro
    def load_yaml(filename):
        """Load YAML data from docs/data directory"""
        yaml_path = Path("docs/data") / filename
        if yaml_path.exists():
            with open(yaml_path, 'r', encoding='utf-8') as f:
                return yaml.safe_load(f)
        return {}

    @env.macro
    def hardware_tables(data):
        cats = data.get("categories", [])
        out = []
        site_url = env.variables.get('config', {}).get('site_url', '')
        
        for cat in cats:
            cid, title, cols, rows = cat["id"], cat["title"], cat["columns"], cat.get("rows", [])
            out.append(f'### {title}')
            out.append('')
            
            # Create markdown table header
            header = '| ' + ' | '.join(cols) + ' |'
            separator = '| ' + ' | '.join(['---'] * len(cols)) + ' |'
            out.append(header)
            out.append(separator)
            
            # Create markdown table rows
            for r in rows:
                row_data = []
                for c in cols:
                    val, lc = r.get(c), c.lower()
                    if lc == "image" and val:
                        model = r.get("Model", "")
                        row_data.append(f'![{model}]({val}){{: style="width:64px;height:48px;object-fit:contain"}}')
                    elif lc == "model" and val:
                        if r.get("Page"): 
                            # Use full absolute URL to bypass MkDocs link processing
                            full_url = f"{site_url}hardware/{r['Page']}"
                            row_data.append(f'<a href="{full_url}">{val}</a>')
                        else: 
                            row_data.append(val)
                    elif lc == "status":
                        # Create status badge using markdown
                        status_class = STATUS_CLASS.get(val.strip().lower() if val else "", "neutral")
                        row_data.append(f'<span class="hw-badge hw-{status_class}">{val or "unknown"}</span>')
                    else:
                        row_data.append(val or '')
                
                out.append('| ' + ' | '.join(str(x) for x in row_data) + ' |')
            
            out.append('')
        
        return "\n".join(out)
