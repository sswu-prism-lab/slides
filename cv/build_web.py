#!/usr/bin/env python3
"""Render cv/Wonjun_Ko_CV.yaml into a standalone web page (screen view of the CV
with a Download-PDF button). Same single source as the PDF.
Usage: python3 build_web.py <input.yaml> <output.html> [pdf_filename]
"""
import sys, re, html, yaml

inp = sys.argv[1] if len(sys.argv) > 1 else "cv/Wonjun_Ko_CV.yaml"
outp = sys.argv[2] if len(sys.argv) > 2 else "dist/cv/index.html"
pdf_name = sys.argv[3] if len(sys.argv) > 3 else "Wonjun_Ko_CV.pdf"

d = yaml.safe_load(open(inp, encoding="utf-8"))
cv = d["cv"]
S = cv["sections"]

def md(text):
    t = html.escape(text, quote=False)
    t = t.replace("\\*", "\x00")
    t = re.sub(r"\[link\]\((.*?)\)", r'<a href="\1" target="_blank" rel="noopener">link</a>', t)
    t = re.sub(r"\[([^\]]+)\]\((.*?)\)", r'<a href="\2" target="_blank" rel="noopener">\1</a>', t)
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"\*(.+?)\*", r"<em>\1</em>", t)
    t = t.replace("\x00", "*")
    return t

def social_line():
    parts = [html.escape(cv["location"]),
             f'<a href="mailto:{cv["email"]}">{html.escape(cv["email"])}</a>',
             html.escape(str(cv.get("phone",""))),
             f'<a href="{cv["website"]}" target="_blank" rel="noopener">Website</a>']
    for s in cv.get("social_networks", []):
        n, u = s["network"], s["username"]
        if n == "LinkedIn": parts.append(f'<a href="https://www.linkedin.com/in/{u}" target="_blank" rel="noopener">LinkedIn</a>')
        elif n == "ORCID": parts.append(f'<a href="https://orcid.org/{u}" target="_blank" rel="noopener">ORCID</a>')
        elif n in ("Google Scholar","GoogleScholar"): parts.append(f'<a href="https://scholar.google.com/citations?user={u}" target="_blank" rel="noopener">Google Scholar</a>')
    return ' &nbsp;·&nbsp; '.join(p for p in parts if p)

def render_section(title, items):
    out = [f'<section><h2>{html.escape(title)}</h2>']
    if items and isinstance(items[0], dict) and ("company" in items[0] or "institution" in items[0]):
        for e in items:
            head = e.get("company") or e.get("institution")
            right = f'{e.get("start_date","")} – {e.get("end_date","")}'.replace("present","Present")
            sub = e.get("position") or " · ".join(x for x in [e.get("degree"), e.get("area")] if x)
            loc = e.get("location","")
            out.append('<div class="entry">')
            out.append(f'<div class="entry-head"><span class="lhs"><strong>{html.escape(head)}</strong></span><span class="rhs">{html.escape(right)}</span></div>')
            out.append(f'<div class="entry-sub"><span>{html.escape(sub)}</span><span class="loc">{html.escape(loc)}</span></div>')
            for h in e.get("highlights", []):
                out.append(f'<ul class="hl"><li>{md(h)}</li></ul>')
            out.append('</div>')
    elif items and isinstance(items[0], dict) and "name" in items[0]:
        for e in items:
            right = e.get("date","")
            head = f'<span class="lhs"><strong>{md(e["name"])}</strong></span>'
            if right: head += f'<span class="rhs">{html.escape(right)}</span>'
            out.append(f'<div class="entry"><div class="entry-head">{head}</div>')
            if e.get("highlights"):
                out.append('<ul class="hl">')
                for h in e["highlights"]:
                    out.append(f'<li>{md(h)}</li>')
                out.append('</ul>')
            out.append('</div>')
    elif items and isinstance(items[0], dict) and "label" in items[0]:
        out.append('<table class="skills">')
        for e in items:
            out.append(f'<tr><td class="sk-l"><strong>{html.escape(e["label"])}</strong></td><td>{md(e["details"])}</td></tr>')
        out.append('</table>')
    else:
        out.append('<ul class="plain">')
        for s in items:
            out.append(f'<li>{md(s)}</li>')
        out.append('</ul>')
    out.append('</section>')
    return "\n".join(out)

role = "Assistant Professor · School of AI Convergence, Sungshin Women's University"
body = [f'<header class="cv"><h1>{html.escape(cv["name"])}, Ph.D.</h1>',
        f'<div class="role">{html.escape(role)}</div>',
        f'<div class="contact">{social_line()}</div></header>']
for title, items in S.items():
    body.append(render_section(title, items))

HTML = f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(cv["name"])} — Curriculum Vitae</title>
<meta name="description" content="Curriculum Vitae of {html.escape(cv["name"])}, {html.escape(role)}.">
<style>
:root{{--accent:#5b21b6;--accent2:#4c1d95;--soft:#f3e8ff;--border:#e9d5ff;--ink:#26262e;--muted:#6b7280;--rule:#e5e0ee;}}
*{{box-sizing:border-box;}}
body{{margin:0;background:#faf9fc;color:var(--ink);line-height:1.5;
  font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,'Helvetica Neue',sans-serif;}}
.topbar{{position:sticky;top:0;z-index:10;background:rgba(255,255,255,.92);backdrop-filter:blur(6px);
  border-bottom:1px solid var(--border);}}
.topbar .inner{{max-width:900px;margin:0 auto;padding:10px 22px;display:flex;justify-content:space-between;
  align-items:center;gap:12px;}}
.topbar .who{{font-weight:700;color:var(--accent);font-size:.98rem;}}
.tb-actions{{display:flex;gap:10px;flex-wrap:wrap;}}
.btn{{display:inline-flex;align-items:center;gap:7px;padding:8px 15px;border-radius:9px;font-weight:600;
  font-size:.86rem;text-decoration:none;border:1px solid var(--border);white-space:nowrap;}}
.btn.primary{{background:var(--accent);color:#fff;border-color:var(--accent);}}
.btn.primary:hover{{background:var(--accent2);}}
.btn.ghost{{background:#fff;color:var(--accent);}}
.btn.ghost:hover{{background:var(--soft);}}
.wrap{{max-width:900px;margin:0 auto;padding:30px 22px 64px;}}
.paper{{background:#fff;border:1px solid var(--rule);border-radius:14px;
  box-shadow:0 1px 10px rgba(91,33,182,.06);padding:44px 50px;}}
header.cv{{border-bottom:2px solid var(--accent);padding-bottom:16px;margin-bottom:8px;text-align:center;}}
h1{{color:var(--accent);font-size:2rem;margin:0 0 3px;}}
.role{{color:var(--muted);font-size:1rem;margin-bottom:10px;}}
.contact{{font-size:.85rem;color:var(--muted);}}
.contact a{{color:var(--accent);text-decoration:none;}}
.contact a:hover{{text-decoration:underline;}}
h2{{font-size:.82rem;text-transform:uppercase;letter-spacing:1px;color:var(--accent);
  border-bottom:1px solid var(--rule);padding-bottom:4px;margin:22px 0 9px;}}
.entry{{margin:0 0 9px;}}
.entry-head{{display:flex;justify-content:space-between;gap:12px;}}
.entry-head .rhs{{color:var(--muted);font-size:.82rem;white-space:nowrap;}}
.entry-sub{{display:flex;justify-content:space-between;font-size:.85rem;color:var(--muted);font-style:italic;}}
ul.hl{{margin:3px 0 0;padding-left:20px;}}
ul.hl li{{font-size:.86rem;margin:1px 0;}}
ul.plain{{margin:0;padding-left:20px;}}
ul.plain li{{font-size:.86rem;margin:3px 0;}}
a{{color:var(--accent);}}
table.skills{{border-collapse:collapse;font-size:.86rem;}}
table.skills td{{padding:2px 10px 2px 0;vertical-align:top;}}
td.sk-l{{white-space:nowrap;width:180px;}}
footer{{max-width:900px;margin:0 auto;padding:20px 22px 40px;font-size:.82rem;color:var(--muted);
  display:flex;flex-wrap:wrap;gap:16px;}}
footer a{{color:var(--accent);text-decoration:none;}}
footer a:hover{{text-decoration:underline;}}
@media (max-width:560px){{.paper{{padding:26px 20px;}} td.sk-l{{width:auto;}}}}
</style></head>
<body>
<div class="topbar"><div class="inner">
  <span class="who">{html.escape(cv["name"])} — CV</span>
  <span class="tb-actions">
    <a class="btn primary" href="./{pdf_name}" download>⬇ Download PDF</a>
    <a class="btn ghost" href="./{pdf_name}" target="_blank" rel="noopener">Open PDF ↗</a>
  </span>
</div></div>
<div class="wrap"><div class="paper">
{chr(10).join(body)}
</div></div>
<footer>
  <a href="https://sites.google.com/sungshin.ac.kr/prism" target="_blank" rel="noopener">← PRISM Lab Home</a>
  <a href="/slides/">Prof. Ko's Lectures</a>
  <a href="https://sswu-prism-lab.github.io/teaching/" target="_blank" rel="noopener">Teaching</a>
</footer>
</body></html>"""

import os
os.makedirs(os.path.dirname(outp) or ".", exist_ok=True)
open(outp, "w", encoding="utf-8").write(HTML)
print("wrote", outp, len(HTML), "bytes")
