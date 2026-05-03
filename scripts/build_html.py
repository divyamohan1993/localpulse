"""Render the same content as a single self-contained HTML file."""
from __future__ import annotations

import html as h
from pathlib import Path

import content as C

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "public" / "report.html"


def esc(s: str) -> str:
    return h.escape(s, quote=False)


def p(text: str) -> str:
    return f"<p>{esc(text)}</p>"


def paras(items) -> str:
    return "\n".join(p(t) for t in items)


def ul(items) -> str:
    body = "\n".join(f"<li>{esc(t)}</li>" for t in items)
    return f"<ul>{body}</ul>"


def ol(items) -> str:
    body = "\n".join(f"<li>{esc(t)}</li>" for t in items)
    return f"<ol>{body}</ol>"


def deflist(mapping) -> str:
    items = []
    for k, v in mapping.items():
        items.append(
            f"<div class='dl-row'>"
            f"<dt>{esc(k)}</dt>"
            f"<dd>{esc(v)}</dd>"
            f"</div>"
        )
    return f"<dl class='kv'>{''.join(items)}</dl>"


def table(rows, *, head: bool = True, caption: str | None = None) -> str:
    if not rows:
        return ""
    out = ["<div class='table-wrap'>"]
    out.append("<table>")
    if caption:
        out.append(f"<caption>{esc(caption)}</caption>")
    if head:
        out.append("<thead><tr>")
        for cell in rows[0]:
            out.append(f"<th scope='col'>{esc(str(cell))}</th>")
        out.append("</tr></thead>")
        body_rows = rows[1:]
    else:
        body_rows = rows
    out.append("<tbody>")
    for row in body_rows:
        out.append("<tr>")
        for cell in row:
            out.append(f"<td>{esc(str(cell))}</td>")
        out.append("</tr>")
    out.append("</tbody></table></div>")
    return "\n".join(out)


def code_block(code: str, *, lang: str = "javascript", caption: str | None = None) -> str:
    cap = f"<figcaption>{esc(caption)}</figcaption>" if caption else ""
    return (
        "<figure class='code-fig'>"
        f"{cap}"
        f"<pre><code class='language-{lang}'>{esc(code)}</code></pre>"
        "</figure>"
    )


# ---------------------------------------------------------------------------
# inline SVG figures
# ---------------------------------------------------------------------------

FIG_ARCHITECTURE = """
<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 800 380' role='img' aria-labelledby='fig1-title fig1-desc'>
  <title id='fig1-title'>LocalPulse high-level architecture</title>
  <desc id='fig1-desc'>Four layers stacked vertically. Presentation, Application, Intelligence and Data, with Cloud Run hosting Express. Twilio and OpenAI are external. Pub/Sub fans out to Firestore and BigQuery.</desc>
  <defs>
    <marker id='arr' viewBox='0 0 10 10' refX='10' refY='5' markerWidth='8' markerHeight='8' orient='auto-start-reverse'>
      <path d='M 0 0 L 10 5 L 0 10 z' fill='currentColor' />
    </marker>
  </defs>
  <g font-family='Inter,Arial,sans-serif' font-size='13'>
    <rect x='20' y='20' width='760' height='60' rx='10' fill='#eef2ff' stroke='#6366f1' />
    <text x='400' y='55' text-anchor='middle' font-weight='700' fill='#1e1b4b'>Resident phones, responder tablets, voice callers</text>
    <text x='400' y='72' text-anchor='middle' fill='#3730a3'>Presentation: HTML + Tailwind + Leaflet + Web Speech API</text>

    <rect x='20' y='110' width='400' height='80' rx='10' fill='#fef3c7' stroke='#d97706' />
    <text x='220' y='140' text-anchor='middle' font-weight='700' fill='#78350f'>Cloud Run (asia-east1)</text>
    <text x='220' y='160' text-anchor='middle' fill='#78350f'>Express server, /api/v1/*, SSE, /healthz</text>
    <text x='220' y='178' text-anchor='middle' fill='#78350f'>scale 0–2 instances · 1 vCPU · 512 MiB</text>

    <rect x='450' y='110' width='330' height='80' rx='10' fill='#dcfce7' stroke='#16a34a' />
    <text x='615' y='140' text-anchor='middle' font-weight='700' fill='#14532d'>Intelligence services</text>
    <text x='615' y='160' text-anchor='middle' fill='#14532d'>OpenAI Whisper · GPT-4o · Twilio</text>
    <text x='615' y='178' text-anchor='middle' fill='#14532d'>Summariser worker · Intent classifier</text>

    <rect x='20' y='220' width='220' height='80' rx='10' fill='#e0f2fe' stroke='#0284c7' />
    <text x='130' y='250' text-anchor='middle' font-weight='700' fill='#0c4a6e'>Pub/Sub</text>
    <text x='130' y='270' text-anchor='middle' fill='#0c4a6e'>incidents-v1</text>
    <text x='130' y='287' text-anchor='middle' fill='#0c4a6e'>incidents-classified</text>

    <rect x='270' y='220' width='220' height='80' rx='10' fill='#ede9fe' stroke='#7c3aed' />
    <text x='380' y='250' text-anchor='middle' font-weight='700' fill='#3b0764'>Firestore (Native)</text>
    <text x='380' y='270' text-anchor='middle' fill='#3b0764'>incidents · summaries</text>
    <text x='380' y='287' text-anchor='middle' fill='#3b0764'>reports</text>

    <rect x='520' y='220' width='260' height='80' rx='10' fill='#fee2e2' stroke='#dc2626' />
    <text x='650' y='250' text-anchor='middle' font-weight='700' fill='#7f1d1d'>BigQuery analytics</text>
    <text x='650' y='270' text-anchor='middle' fill='#7f1d1d'>localpulse_analytics</text>
    <text x='650' y='287' text-anchor='middle' fill='#7f1d1d'>partitioned by day</text>

    <rect x='20' y='330' width='760' height='38' rx='8' fill='#f1f5f9' stroke='#475569' />
    <text x='400' y='355' text-anchor='middle' fill='#0f172a'>Cloud Logging · Cloud Trace · OpenTelemetry · Cloud Armor at the edge</text>

    <g stroke='currentColor' stroke-width='1.5' fill='none' marker-end='url(#arr)' color='#475569'>
      <line x1='400' y1='90' x2='400' y2='108' />
      <line x1='420' y1='150' x2='448' y2='150' />
      <line x1='130' y1='195' x2='130' y2='218' />
      <line x1='240' y1='260' x2='268' y2='260' />
      <line x1='490' y1='260' x2='518' y2='260' />
    </g>
  </g>
</svg>
"""

FIG_DATAFLOW = """
<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 800 220' role='img' aria-labelledby='fig2-title fig2-desc'>
  <title id='fig2-title'>End-to-end data flow</title>
  <desc id='fig2-desc'>Arrows from public sources through ingest, dedupe, classify, summarise, write and read.</desc>
  <defs>
    <marker id='arr2' viewBox='0 0 10 10' refX='10' refY='5' markerWidth='8' markerHeight='8' orient='auto-start-reverse'>
      <path d='M 0 0 L 10 5 L 0 10 z' fill='currentColor' />
    </marker>
  </defs>
  <g font-family='Inter,Arial,sans-serif' font-size='12'>
    <g>
      <rect x='10'  y='90' width='110' height='44' rx='8' fill='#eef2ff' stroke='#4f46e5' />
      <text x='65'  y='117' text-anchor='middle'>Public sources</text>
      <rect x='140' y='90' width='110' height='44' rx='8' fill='#eef2ff' stroke='#4f46e5' />
      <text x='195' y='117' text-anchor='middle'>Ingest</text>
      <rect x='270' y='90' width='110' height='44' rx='8' fill='#eef2ff' stroke='#4f46e5' />
      <text x='325' y='117' text-anchor='middle'>Dedupe (SimHash)</text>
      <rect x='400' y='90' width='110' height='44' rx='8' fill='#eef2ff' stroke='#4f46e5' />
      <text x='455' y='117' text-anchor='middle'>Classify</text>
      <rect x='530' y='90' width='120' height='44' rx='8' fill='#eef2ff' stroke='#4f46e5' />
      <text x='590' y='117' text-anchor='middle'>Summarise (GPT-4o)</text>
      <rect x='670' y='90' width='120' height='44' rx='8' fill='#eef2ff' stroke='#4f46e5' />
      <text x='730' y='117' text-anchor='middle'>Resident dashboard</text>
    </g>
    <g stroke='currentColor' stroke-width='1.5' fill='none' marker-end='url(#arr2)' color='#475569'>
      <line x1='120' y1='112' x2='138' y2='112' />
      <line x1='250' y1='112' x2='268' y2='112' />
      <line x1='380' y1='112' x2='398' y2='112' />
      <line x1='510' y1='112' x2='528' y2='112' />
      <line x1='650' y1='112' x2='668' y2='112' />
    </g>
    <text x='400' y='40' text-anchor='middle' font-weight='700'>Twitter / Reddit / WhatsApp listener  →  status summary in five locales</text>
    <text x='400' y='190' text-anchor='middle' fill='#475569'>Trust score (source × confirmation × recency) gates what residents see.</text>
  </g>
</svg>
"""

FIG_VOICE = """
<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 800 220' role='img' aria-labelledby='fig3-title fig3-desc'>
  <title id='fig3-title'>Voice bot call flow</title>
  <desc id='fig3-desc'>Caller dials Twilio, audio streams to Whisper, intent classified by GPT-4o, response spoken with Polly.</desc>
  <defs>
    <marker id='arr3' viewBox='0 0 10 10' refX='10' refY='5' markerWidth='8' markerHeight='8' orient='auto-start-reverse'>
      <path d='M 0 0 L 10 5 L 0 10 z' fill='currentColor' />
    </marker>
  </defs>
  <g font-family='Inter,Arial,sans-serif' font-size='12'>
    <rect x='20'  y='80' width='110' height='60' rx='8' fill='#fef3c7' stroke='#d97706' />
    <text x='75'  y='110' text-anchor='middle'>Caller</text>
    <text x='75'  y='128' text-anchor='middle' font-size='10' fill='#78350f'>feature phone</text>

    <rect x='160' y='80' width='110' height='60' rx='8' fill='#fef3c7' stroke='#d97706' />
    <text x='215' y='110' text-anchor='middle'>Twilio Voice</text>
    <text x='215' y='128' text-anchor='middle' font-size='10' fill='#78350f'>media stream</text>

    <rect x='300' y='80' width='130' height='60' rx='8' fill='#dcfce7' stroke='#16a34a' />
    <text x='365' y='110' text-anchor='middle'>Cloud Run handler</text>
    <text x='365' y='128' text-anchor='middle' font-size='10' fill='#14532d'>/voice/webhook</text>

    <rect x='460' y='30' width='130' height='50' rx='8' fill='#e0f2fe' stroke='#0284c7' />
    <text x='525' y='60' text-anchor='middle'>Whisper STT</text>

    <rect x='460' y='120' width='130' height='50' rx='8' fill='#ede9fe' stroke='#7c3aed' />
    <text x='525' y='150' text-anchor='middle'>GPT-4o intent</text>

    <rect x='620' y='80' width='150' height='60' rx='8' fill='#fee2e2' stroke='#dc2626' />
    <text x='695' y='110' text-anchor='middle'>TwiML reply</text>
    <text x='695' y='128' text-anchor='middle' font-size='10' fill='#7f1d1d'>Polly Neural / &lt;Dial&gt;</text>

    <g stroke='currentColor' stroke-width='1.5' fill='none' marker-end='url(#arr3)' color='#475569'>
      <line x1='130' y1='110' x2='158' y2='110' />
      <line x1='270' y1='110' x2='298' y2='110' />
      <line x1='430' y1='100' x2='458' y2='60' />
      <line x1='430' y1='118' x2='458' y2='145' />
      <line x1='590' y1='55'  x2='618' y2='100' />
      <line x1='590' y1='145' x2='618' y2='120' />
    </g>
    <text x='400' y='200' text-anchor='middle' fill='#475569'>End to end target: under 1.6 s from caller speaking to first audio.</text>
  </g>
</svg>
"""

FIG_DASHBOARD = """
<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 360 720' role='img' aria-labelledby='fig4-title fig4-desc'>
  <title id='fig4-title'>Resident dashboard wireframe (mobile, 360x720)</title>
  <desc id='fig4-desc'>Header with logo, language switcher, status summary card, map taking middle two-thirds, report-incident floating action button.</desc>
  <g font-family='Inter,Arial,sans-serif' font-size='12'>
    <rect x='0' y='0' width='360' height='720' fill='#f8fafc' stroke='#cbd5e1' />
    <rect x='0' y='0' width='360' height='56' fill='#1e293b' />
    <text x='16' y='34' fill='#fff' font-weight='700' font-size='16'>LocalPulse</text>
    <rect x='270' y='14' width='74' height='28' rx='14' fill='#334155' />
    <text x='307' y='32' text-anchor='middle' fill='#fff' font-size='11'>हिंदी ▾</text>
    <rect x='12' y='72' width='336' height='110' rx='10' fill='#fff' stroke='#cbd5e1' />
    <text x='24' y='96' font-weight='700'>Status summary · Solan</text>
    <text x='24' y='118' fill='#475569'>Roads: NH-5 open. Detour at Subzi Mandi.</text>
    <text x='24' y='136' fill='#475569'>Shelter: Govt Senior Sec School open · 200 beds.</text>
    <text x='24' y='154' fill='#475569'>Power: BBMB grid restored 18:42.</text>
    <text x='24' y='172' fill='#475569'>Water: tankers at Sector 4 ward office.</text>
    <rect x='12' y='198' width='336' height='420' rx='10' fill='#dbeafe' stroke='#3b82f6' />
    <text x='180' y='418' text-anchor='middle' fill='#1e40af' font-size='13'>Leaflet map · OSM tiles</text>
    <circle cx='120' cy='350' r='10' fill='#dc2626' />
    <circle cx='220' cy='420' r='10' fill='#f59e0b' />
    <circle cx='180' cy='480' r='10' fill='#16a34a' />
    <rect x='280' y='640' width='60' height='60' rx='30' fill='#ef4444' />
    <text x='310' y='678' text-anchor='middle' fill='#fff' font-size='28' font-weight='700'>+</text>
  </g>
</svg>
"""

FIG_RESPONDER = """
<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 1024 640' role='img' aria-labelledby='fig5-title fig5-desc'>
  <title id='fig5-title'>Responder console wireframe (tablet, 1024x640)</title>
  <desc id='fig5-desc'>Three-column layout. Left: incident list with filters. Middle: map. Right: source feed.</desc>
  <g font-family='Inter,Arial,sans-serif' font-size='12'>
    <rect x='0' y='0' width='1024' height='640' fill='#f8fafc' stroke='#cbd5e1' />
    <rect x='0' y='0' width='1024' height='56' fill='#0f172a' />
    <text x='20' y='34' fill='#fff' font-weight='700' font-size='16'>LocalPulse · Responder</text>
    <text x='960' y='34' fill='#fff'>logout</text>
    <rect x='12' y='68' width='280' height='560' rx='10' fill='#fff' stroke='#cbd5e1' />
    <text x='24' y='96' font-weight='700'>Active incidents</text>
    <rect x='24' y='110' width='256' height='60' rx='6' fill='#fee2e2' stroke='#fca5a5' />
    <text x='36' y='132' font-weight='700'>Cloudburst @ Anhech</text>
    <text x='36' y='150' fill='#475569'>2 min ago · trust 0.91 · road blocked</text>
    <rect x='24' y='180' width='256' height='60' rx='6' fill='#fef3c7' stroke='#fde68a' />
    <text x='36' y='202' font-weight='700'>Power outage · sector 4</text>
    <text x='36' y='220' fill='#475569'>14 min ago · trust 0.66 · investigating</text>
    <rect x='24' y='250' width='256' height='60' rx='6' fill='#dcfce7' stroke='#86efac' />
    <text x='36' y='272' font-weight='700'>Shelter open · GSSS Solan</text>
    <text x='36' y='290' fill='#475569'>1 hr ago · trust 1.00 · resolved</text>
    <rect x='304' y='68' width='430' height='560' rx='10' fill='#dbeafe' stroke='#3b82f6' />
    <text x='519' y='358' text-anchor='middle' fill='#1e40af'>Leaflet map · live pins</text>
    <rect x='746' y='68' width='266' height='560' rx='10' fill='#fff' stroke='#cbd5e1' />
    <text x='760' y='96' font-weight='700'>Source feed</text>
    <rect x='760' y='110' width='240' height='60' rx='6' fill='#f1f5f9' />
    <text x='770' y='132' fill='#475569'>@solan_news · road washed out near...</text>
    <rect x='760' y='180' width='240' height='60' rx='6' fill='#f1f5f9' />
    <text x='770' y='202' fill='#475569'>r/HimachalPradesh · power back at 18:42</text>
  </g>
</svg>
"""

FIG_DEPLOY = """
<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 800 320' role='img' aria-labelledby='fig6-title fig6-desc'>
  <title id='fig6-title'>Cloud Run deployment topology in asia-east1</title>
  <desc id='fig6-desc'>User → Cloud DNS → Google Front-End → Cloud Armor → Cloud Run service backed by Artifact Registry. CI/CD via GitHub Actions.</desc>
  <g font-family='Inter,Arial,sans-serif' font-size='12'>
    <rect x='10'  y='130' width='110' height='60' rx='8' fill='#eef2ff' stroke='#4f46e5' />
    <text x='65'  y='160' text-anchor='middle'>User device</text>
    <text x='65'  y='178' text-anchor='middle' font-size='10' fill='#475569'>localpulse.dmj.one</text>

    <rect x='140' y='130' width='110' height='60' rx='8' fill='#fef3c7' stroke='#d97706' />
    <text x='195' y='160' text-anchor='middle'>Cloud DNS</text>

    <rect x='270' y='130' width='130' height='60' rx='8' fill='#fef3c7' stroke='#d97706' />
    <text x='335' y='160' text-anchor='middle'>Google Front-End</text>
    <text x='335' y='178' text-anchor='middle' font-size='10'>TLS 1.3 · HSTS</text>

    <rect x='420' y='130' width='130' height='60' rx='8' fill='#fee2e2' stroke='#dc2626' />
    <text x='485' y='160' text-anchor='middle'>Cloud Armor</text>
    <text x='485' y='178' text-anchor='middle' font-size='10'>edge rate limit</text>

    <rect x='570' y='130' width='200' height='60' rx='8' fill='#dcfce7' stroke='#16a34a' />
    <text x='670' y='160' text-anchor='middle'>Cloud Run service</text>
    <text x='670' y='178' text-anchor='middle' font-size='10'>asia-east1 · 0–2 inst</text>

    <rect x='420' y='40' width='200' height='50' rx='8' fill='#ede9fe' stroke='#7c3aed' />
    <text x='520' y='70' text-anchor='middle'>Artifact Registry</text>

    <rect x='220' y='240' width='200' height='50' rx='8' fill='#e0f2fe' stroke='#0284c7' />
    <text x='320' y='270' text-anchor='middle'>GitHub Actions CI/CD</text>

    <g stroke='currentColor' stroke-width='1.5' fill='none' color='#475569'>
      <line x1='120' y1='160' x2='138' y2='160' marker-end='url(#arr2)' />
      <line x1='250' y1='160' x2='268' y2='160' marker-end='url(#arr2)' />
      <line x1='400' y1='160' x2='418' y2='160' marker-end='url(#arr2)' />
      <line x1='550' y1='160' x2='568' y2='160' marker-end='url(#arr2)' />
      <line x1='620' y1='65'  x2='670' y2='128' marker-end='url(#arr2)' />
      <line x1='320' y1='240' x2='420' y2='90'  marker-end='url(#arr2)' />
    </g>
  </g>
</svg>
"""


# ---------------------------------------------------------------------------
# section renderers
# ---------------------------------------------------------------------------

def render_acknowledgement():
    return f"<section id='acknowledgement'><h2>Acknowledgement</h2>{paras(C.ACKNOWLEDGEMENT)}</section>"


def render_abstract():
    body = paras(C.ABSTRACT)
    body += (
        "<p><strong>Keywords.</strong> crisis management, disaster response, "
        "NLP summarisation, multilingual voice assistant, Twilio, Whisper, "
        "GPT-4o, Cloud Run, accessibility, WCAG 2.2, DPDP Act 2023, "
        "Aatmanirbhar Bharat.</p>"
    )
    return f"<section id='abstract'><h2>Abstract</h2>{body}</section>"


def render_toc():
    rows = [("Section", "Page")] + list(C.TOC_ENTRIES)
    return (
        "<section id='toc'><h2>Table of Contents</h2>"
        f"{table(rows)}"
        "</section>"
    )


def render_figures():
    rows = [("Label", "Caption", "Page")] + list(C.FIGURES)
    return (
        "<section id='list-figures'><h2>List of Figures</h2>"
        f"{table(rows)}"
        "</section>"
    )


def render_tables_list():
    rows = [("Label", "Caption", "Page")] + list(C.TABLES_LIST)
    return (
        "<section id='list-tables'><h2>List of Tables</h2>"
        f"{table(rows)}"
        "</section>"
    )


def render_introduction():
    return f"""
<section id='introduction'>
  <h2>1. Introduction and Problem Definition</h2>
  <h3>1.1 Background</h3>
  {paras(C.INTRO_BACKGROUND)}
  <h3>1.2 Problem Statement</h3>
  {paras(C.INTRO_PROBLEM_STATEMENT)}
  <h3>1.3 Objectives</h3>
  {ol(C.INTRO_OBJECTIVES)}
  <h3>1.4 Scope</h3>
  {paras(C.INTRO_SCOPE)}
  <h3>1.5 Target Users</h3>
  {ul(C.INTRO_TARGET_USERS)}
  <h3>1.6 Significance</h3>
  {paras(C.INTRO_SIGNIFICANCE)}
</section>
"""


def render_requirements():
    return f"""
<section id='requirements'>
  <h2>2. System Requirements</h2>
  <h3>2.1 Functional Requirements</h3>
  {ul(C.REQ_FUNCTIONAL)}
  <h3>2.2 Non-functional Requirements</h3>
  {deflist(C.REQ_NONFUNCTIONAL)}
  <h3>2.3 Hardware and Software Requirements</h3>
  {deflist(C.REQ_HARDWARE_SOFTWARE)}
</section>
"""


def render_architecture():
    components_rows = [("Component", "Description")] + list(C.ARCH_COMPONENTS)
    stride_rows = [
        ("Threat (STRIDE)", "Vector", "Mitigation"),
        ("Spoofing", "Fake resident reports",
         "Anonymous signed-cookie session, CAPTCHA gate on spike."),
        ("Tampering", "Man-in-the-middle on transit",
         "TLS 1.3, HSTS preload, SRI hashes on CDN scripts."),
        ("Repudiation", "Disputed actions",
         "Structured audit logs with correlation identifier."),
        ("Information Disclosure", "Leak of caller phone numbers",
         "AES-256-GCM at rest, no PII in logs/URLs."),
        ("Denial of Service", "Flood of fake reports",
         "Cloud Armor edge limits, per-route token bucket."),
        ("Elevation of Privilege", "Compromised service account",
         "Least-privilege IAM, no long-lived keys, WIF."),
    ]
    return f"""
<section id='architecture'>
  <h2>3. System Architecture and Design</h2>
  <h3>3.1 Architectural Overview</h3>
  {paras(C.ARCH_OVERVIEW)}
  <figure class='diagram'>
    {FIG_ARCHITECTURE}
    <figcaption>Figure 1. High-level system architecture of LocalPulse.</figcaption>
  </figure>
  <h3>3.2 Component Inventory</h3>
  {table(components_rows)}
  <h3>3.3 Data Flow</h3>
  {paras(C.ARCH_DATAFLOW)}
  <figure class='diagram'>
    {FIG_DATAFLOW}
    <figcaption>Figure 2. End-to-end data flow from public source to resident device.</figcaption>
  </figure>
  <h3>3.4 API Design</h3>
  {paras(C.ARCH_API_DESIGN)}
  <h3>3.5 Data and State Design</h3>
  {paras(C.ARCH_DATA_DESIGN)}
  <h3>3.6 Security Architecture</h3>
  {paras(C.ARCH_SECURITY)}
  {table(stride_rows, caption='Table 4. STRIDE threat model and mitigations.')}
  <h3>3.7 Deployment Topology</h3>
  {paras(C.ARCH_DEPLOYMENT)}
  <figure class='diagram'>
    {FIG_DEPLOY}
    <figcaption>Figure 6. Cloud Run deployment topology in asia-east1.</figcaption>
  </figure>
</section>
"""


def render_stack():
    return f"""
<section id='stack'>
  <h2>4. Technology Stack</h2>
  <p>Table 1 lists every technology choice in the LocalPulse stack with the
  reason it was selected over alternatives. The selection is guided by three
  constraints: idle cost close to zero, mobile-first performance on a 3G
  connection and accessibility at WCAG 2.2 level AAA.</p>
  {table(C.TECH_STACK, caption='Table 1. Technology choices and rationale.')}
</section>
"""


def render_implementation():
    api_rows = [("Endpoint", "Description")] + list(C.IMPL_KEY_APIS)
    snips = "".join(
        code_block(s["code"], lang=s["lang"], caption=s["caption"])
        for s in C.IMPL_CODE_SNIPPETS
    )
    return f"""
<section id='implementation'>
  <h2>5. Implementation</h2>
  <h3>5.1 Code Organisation</h3>
  {paras(C.IMPL_CODE_ORG)}
  <h3>5.2 Public API Endpoints</h3>
  {table(api_rows, caption='Table 2. Public HTTP and JSON API endpoints.')}
  <h3>5.3 Internationalisation</h3>
  {paras(C.IMPL_I18N)}
  <h3>5.4 Mobile-first Responsive Layout</h3>
  {paras(C.IMPL_RESPONSIVE)}
  <figure class='diagram wire'>
    {FIG_DASHBOARD}
    <figcaption>Figure 4. Resident dashboard wireframe (mobile, 360x720).</figcaption>
  </figure>
  <figure class='diagram'>
    {FIG_RESPONDER}
    <figcaption>Figure 5. Responder console wireframe (tablet, 1024x640).</figcaption>
  </figure>
  <h3>5.5 Real-time Update Loop</h3>
  {paras(C.IMPL_REALTIME)}
  <h3>5.6 AI Summarisation Pipeline</h3>
  {paras(C.IMPL_AI_PIPELINE)}
  <h3>5.7 Voice Bot Flow</h3>
  {paras(C.IMPL_VOICE_FLOW)}
  <figure class='diagram'>
    {FIG_VOICE}
    <figcaption>Figure 3. Voice bot call flow over Twilio with Whisper and GPT-4o.</figcaption>
  </figure>
  <h3>5.8 Selected Code Listings</h3>
  {snips}
</section>
"""


def render_algorithms():
    return f"""
<section id='algorithms'>
  <h2>6. Algorithms and Models</h2>
  <h3>6.1 Social-media Summarisation Pipeline</h3>
  {paras(C.ALGO_SUMMARISATION)}
  <h3>6.2 Voice Intent Classification</h3>
  {paras(C.ALGO_INTENT)}
  <h3>6.3 Trust Score</h3>
  {paras(C.ALGO_TRUST)}
  <h3>6.4 Language Identification</h3>
  {paras(C.ALGO_LANGID)}
</section>
"""


def render_testing():
    layers_rows = [("Layer", "Tooling", "Coverage")] + list(C.TEST_LAYERS)
    return f"""
<section id='testing'>
  <h2>7. Testing</h2>
  <p>Tests run at six layers, each chosen to catch a specific class of
  regression as early as possible in the development cycle.</p>
  {table(layers_rows)}
  <h3>7.1 Sample Test Results</h3>
  {table(C.TEST_SAMPLE_RESULTS, caption='Table 5. Test suite coverage and sample results.')}
</section>
"""


def render_results():
    return f"""
<section id='results'>
  <h2>8. Results and Performance Analysis</h2>
  <p>The minimum lovable product was measured against a set of engineering
  targets that map back to the non-functional requirements in Section 2.2.
  Table 3 reports the target value, the achieved value and a short note on
  the measurement context.</p>
  {table(C.RESULTS_TARGETS, caption='Table 3. Performance targets and achieved numbers.')}
  <h3>8.1 Discussion</h3>
  {paras(C.RESULTS_DISCUSSION)}
</section>
"""


def render_deployment():
    cost_rows = [
        ("Profile", "Requests / day", "Cloud Run cost", "Egress", "Total / month"),
        ("Idle (MLP demo)", "≈ 200", "0 INR (free tier)", "0 INR", "0 INR"),
        ("Steady (pilot)", "≈ 50,000", "≈ 60 INR", "≈ 25 INR", "≈ 85 INR"),
        ("Peak (1 incident)", "≈ 500,000", "≈ 600 INR", "≈ 250 INR", "≈ 850 INR"),
    ]
    return f"""
<section id='deployment'>
  <h2>9. Deployment</h2>
  {paras(C.DEPLOY_OVERVIEW)}
  <h3>9.1 Dockerfile</h3>
  {code_block(C.DEPLOY_DOCKERFILE, lang='dockerfile', caption='Listing 4. Multi-stage Dockerfile.')}
  <h3>9.2 Cloud Run Deploy</h3>
  {code_block(C.DEPLOY_GCLOUD, lang='bash', caption='Listing 5. gcloud run deploy with custom domain mapping.')}
  <h3>9.3 Continuous Integration and Release</h3>
  {paras(C.DEPLOY_CICD)}
  {table(cost_rows, caption='Table 6. Cost profile at idle, steady and peak load (Indian rupees).')}
</section>
"""


def render_challenges():
    items = []
    for ch in C.CHALLENGES:
        items.append(
            f"<article class='challenge'>"
            f"<h3>{esc(ch['title'])}</h3>"
            f"<p><strong>Problem.</strong> {esc(ch['problem'])}</p>"
            f"<p><strong>Solution.</strong> {esc(ch['solution'])}</p>"
            f"<p><strong>Outcome.</strong> {esc(ch['outcome'])}</p>"
            f"</article>"
        )
    return f"""
<section id='challenges'>
  <h2>10. Challenges and Solutions</h2>
  {''.join(items)}
</section>
"""


def render_conclusion():
    return f"""
<section id='conclusion'>
  <h2>11. Conclusion and Future Scope</h2>
  <h3>11.1 Conclusion</h3>
  {paras(C.CONCLUSION)}
  <h3>11.2 Future Scope</h3>
  {ul(C.FUTURE_SCOPE)}
  <p class='close'>{esc(C.CONCLUSION_CLOSE[0])}</p>
</section>
"""


def render_viva():
    items = []
    for i, qa in enumerate(C.VIVA_QA, 1):
        items.append(
            f"<article class='qa'>"
            f"<h3>Q{i}. {esc(qa['q'])}</h3>"
            f"<p>{esc(qa['a'])}</p>"
            f"</article>"
        )
    return f"""
<section id='viva'>
  <h2>Questions and Answers</h2>
  <p>The following ten questions are the standard viva voce set for this
  capstone. Each answer is written to be defensible on the stand.</p>
  {''.join(items)}
</section>
"""


def render_references():
    items = []
    for i, ref in enumerate(C.REFERENCES, 1):
        items.append(f"<li id='ref-{i}'>{esc(ref)}</li>")
    return (
        "<section id='references'>"
        "<h2>References</h2>"
        f"<ol class='refs'>{''.join(items)}</ol>"
        "</section>"
    )


# ---------------------------------------------------------------------------
# top-level
# ---------------------------------------------------------------------------

NAV = [
    ("acknowledgement", "Acknowledgement"),
    ("abstract", "Abstract"),
    ("toc", "Table of Contents"),
    ("list-figures", "List of Figures"),
    ("list-tables", "List of Tables"),
    ("introduction", "1. Introduction"),
    ("requirements", "2. System Requirements"),
    ("architecture", "3. Architecture and Design"),
    ("stack", "4. Technology Stack"),
    ("implementation", "5. Implementation"),
    ("algorithms", "6. Algorithms and Models"),
    ("testing", "7. Testing"),
    ("results", "8. Results and Performance"),
    ("deployment", "9. Deployment"),
    ("challenges", "10. Challenges and Solutions"),
    ("conclusion", "11. Conclusion and Future Scope"),
    ("viva", "Questions and Answers"),
    ("references", "References"),
]


def render_html() -> str:
    nav_html = "\n".join(
        f"<li><a href='#{slug}'>{esc(label)}</a></li>" for slug, label in NAV
    )

    body = "\n".join([
        render_acknowledgement(),
        render_abstract(),
        render_toc(),
        render_figures(),
        render_tables_list(),
        render_introduction(),
        render_requirements(),
        render_architecture(),
        render_stack(),
        render_implementation(),
        render_algorithms(),
        render_testing(),
        render_results(),
        render_deployment(),
        render_challenges(),
        render_conclusion(),
        render_viva(),
        render_references(),
    ])

    title = esc(C.PROJECT["title"])
    author = esc(C.PROJECT["author"])
    roll = esc(C.PROJECT["roll"])
    mentor = esc(C.PROJECT["mentor"])
    school = esc(C.PROJECT["school"])
    uni = esc(C.PROJECT["university"])
    loc = esc(C.PROJECT["location"])
    year = esc(C.PROJECT["year"])
    domain = esc(C.PROJECT["domain"])
    degree = esc(C.PROJECT["degree"])

    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<title>{title} — Capstone Report</title>
<meta name="viewport" content="width=device-width,initial-scale=1" />
<meta name="description" content="LocalPulse capstone report by {author}, B.Tech CSE, Shoolini University, 2026." />
<meta name="theme-color" content="#1f2a44" />
<meta property="og:title" content="{title} — Capstone Report" />
<meta property="og:description" content="AI Crisis Management for Small Communities. Capstone by {author}, mentored by {mentor}." />
<meta property="og:type" content="article" />
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700&family=JetBrains+Mono:wght@400;600&display=swap" />
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/prismjs@1.29.0/themes/prism.min.css" />
<script src="https://cdn.tailwindcss.com"></script>
<style>
  :root {{
    --bg: #fdfbf7;
    --surface: #ffffff;
    --ink: #1a1a1a;
    --ink-soft: #4b5563;
    --muted: #6b7280;
    --line: #e5e7eb;
    --accent: #1f2a44;
    --accent-2: #b45309;
    --link: #1d4ed8;
    --code-bg: #f4f4f5;
    --warn: #b45309;
    --ok: #047857;
    --bad: #b91c1c;
    --maxw: 75ch;
    --radius: 10px;
    --shadow: 0 1px 3px rgba(0,0,0,0.04), 0 4px 12px rgba(0,0,0,0.04);
  }}
  [data-theme="dark"] {{
    --bg: #0e1116;
    --surface: #161b22;
    --ink: #e6edf3;
    --ink-soft: #b1bac4;
    --muted: #8b949e;
    --line: #30363d;
    --accent: #94a3b8;
    --accent-2: #facc15;
    --link: #93c5fd;
    --code-bg: #0b1220;
    --shadow: 0 1px 3px rgba(0,0,0,0.4), 0 4px 12px rgba(0,0,0,0.5);
  }}
  *, *::before, *::after {{ box-sizing: border-box; }}
  html {{ scroll-behavior: smooth; }}
  body {{
    margin: 0;
    font-family: "Inter", system-ui, -apple-system, "Segoe UI", Roboto, "Noto Sans", sans-serif;
    color: var(--ink);
    background: var(--bg);
    line-height: 1.7;
    font-size: 17px;
    -webkit-font-smoothing: antialiased;
  }}
  h1, h2, h3, h4 {{
    font-family: "Space Grotesk", "Inter", sans-serif;
    color: var(--accent);
    line-height: 1.25;
    letter-spacing: -0.01em;
    margin: 2.4em 0 0.6em;
  }}
  [data-theme="dark"] h1, [data-theme="dark"] h2, [data-theme="dark"] h3 {{ color: #f9fafb; }}
  h1 {{ font-size: clamp(2rem, 4vw, 2.6rem); }}
  h2 {{ font-size: clamp(1.5rem, 3vw, 2rem); border-bottom: 1px solid var(--line); padding-bottom: 0.3em; }}
  h3 {{ font-size: 1.25rem; color: var(--ink); }}
  p {{ margin: 0 0 1em; }}
  a {{ color: var(--link); text-decoration: underline; text-underline-offset: 3px; }}
  a:focus-visible {{ outline: 3px solid var(--accent-2); outline-offset: 3px; border-radius: 4px; }}
  ul, ol {{ padding-left: 1.4em; }}
  li {{ margin: 0.3em 0; }}
  code {{ font-family: "JetBrains Mono", ui-monospace, "SFMono-Regular", monospace; font-size: 0.92em; }}
  :not(pre) > code {{ background: var(--code-bg); padding: 0.1em 0.35em; border-radius: 4px; }}
  pre {{
    background: var(--code-bg);
    padding: 1em 1.2em;
    border-radius: var(--radius);
    overflow: auto;
    font-size: 0.86em;
    border: 1px solid var(--line);
  }}
  figure.code-fig {{ margin: 1.2em 0; }}
  figure.code-fig figcaption {{
    font-size: 0.85em;
    color: var(--muted);
    margin-bottom: 0.4em;
    font-style: italic;
  }}
  figure.diagram {{
    margin: 1.6em 0;
    background: var(--surface);
    border: 1px solid var(--line);
    padding: 1em;
    border-radius: var(--radius);
    box-shadow: var(--shadow);
  }}
  figure.diagram svg {{ width: 100%; height: auto; display: block; }}
  figure.diagram.wire svg {{ max-width: 360px; margin: 0 auto; }}
  figure.diagram figcaption {{
    text-align: center;
    color: var(--muted);
    font-size: 0.9em;
    margin-top: 0.6em;
  }}
  .table-wrap {{ overflow-x: auto; margin: 1.2em 0; }}
  table {{
    width: 100%;
    border-collapse: collapse;
    background: var(--surface);
    box-shadow: var(--shadow);
    border-radius: var(--radius);
    overflow: hidden;
  }}
  caption {{
    caption-side: bottom;
    text-align: left;
    font-size: 0.88em;
    color: var(--muted);
    padding: 0.6em 0.4em 0.2em;
    font-style: italic;
  }}
  th, td {{
    text-align: left;
    padding: 0.65em 0.85em;
    border-bottom: 1px solid var(--line);
    vertical-align: top;
    font-size: 0.95em;
  }}
  thead th {{ background: var(--accent); color: #fff; font-weight: 600; }}
  [data-theme="dark"] thead th {{ background: #1f2937; color: #f9fafb; }}
  tbody tr:nth-child(even) {{ background: rgba(0,0,0,0.025); }}
  [data-theme="dark"] tbody tr:nth-child(even) {{ background: rgba(255,255,255,0.03); }}
  dl.kv .dl-row {{
    display: grid;
    grid-template-columns: minmax(180px, 1fr) 3fr;
    gap: 1em;
    padding: 0.65em 0;
    border-bottom: 1px solid var(--line);
  }}
  dl.kv dt {{ font-weight: 600; color: var(--accent); }}
  [data-theme="dark"] dl.kv dt {{ color: #cbd5e1; }}
  dl.kv dd {{ margin: 0; color: var(--ink-soft); }}
  article.challenge, article.qa {{
    background: var(--surface);
    border: 1px solid var(--line);
    border-radius: var(--radius);
    padding: 1.1em 1.3em;
    margin: 1em 0;
    box-shadow: var(--shadow);
  }}
  article.challenge h3, article.qa h3 {{
    margin-top: 0;
    color: var(--accent);
    font-size: 1.1rem;
  }}
  ol.refs li {{
    padding-left: 0.4em;
    margin: 0.6em 0;
    font-size: 0.95em;
    color: var(--ink-soft);
  }}
  /* layout */
  .skip-link {{
    position: absolute; left: -10000px; top: auto; width: 1px; height: 1px; overflow: hidden;
  }}
  .skip-link:focus {{
    position: fixed; left: 1rem; top: 1rem; width: auto; height: auto; padding: 0.5em 1em;
    background: var(--accent); color: #fff; z-index: 1000; border-radius: 6px;
  }}
  header.cover {{
    background: linear-gradient(180deg, #1f2a44 0%, #111827 100%);
    color: #f8fafc;
    padding: 3em 1.5em;
    text-align: center;
  }}
  header.cover h1 {{
    color: #fff;
    margin: 0 0 0.4em;
    font-size: clamp(2.2rem, 5vw, 3.2rem);
  }}
  header.cover .sub {{ color: #cbd5e1; font-size: 1.1rem; margin-bottom: 1.4em; }}
  header.cover .meta {{
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
    max-width: 900px;
    margin: 0 auto;
    gap: 0.8em 2em;
    color: #e2e8f0;
    font-size: 0.95rem;
  }}
  header.cover .meta b {{ display: block; color: #fbbf24; font-weight: 600; font-size: 0.78rem; letter-spacing: 0.08em; text-transform: uppercase; margin-bottom: 0.15em; }}
  .layout {{
    display: grid;
    grid-template-columns: 280px minmax(0, 1fr);
    gap: 2.5em;
    max-width: 1240px;
    margin: 0 auto;
    padding: 2em 1.5em 4em;
  }}
  aside.toc-side {{
    position: sticky;
    top: 1.5em;
    align-self: start;
    max-height: calc(100vh - 3em);
    overflow: auto;
    padding: 1.2em 1em;
    background: var(--surface);
    border: 1px solid var(--line);
    border-radius: var(--radius);
    box-shadow: var(--shadow);
  }}
  aside.toc-side h2 {{
    font-size: 0.78rem;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    margin: 0 0 0.6em;
    color: var(--muted);
    border: none;
    padding: 0;
  }}
  aside.toc-side ol {{ list-style: none; padding: 0; margin: 0; }}
  aside.toc-side li {{ margin: 0.15em 0; }}
  aside.toc-side a {{
    display: block;
    padding: 0.35em 0.5em;
    border-radius: 6px;
    text-decoration: none;
    color: var(--ink-soft);
    font-size: 0.92rem;
  }}
  aside.toc-side a:hover, aside.toc-side a.active {{ background: rgba(31,42,68,0.06); color: var(--accent); }}
  [data-theme="dark"] aside.toc-side a:hover, [data-theme="dark"] aside.toc-side a.active {{ background: rgba(255,255,255,0.06); color: #fff; }}
  main {{ min-width: 0; max-width: var(--maxw); }}
  section {{ scroll-margin-top: 1.5em; }}
  p.close {{ font-style: italic; color: var(--accent-2); border-left: 3px solid var(--accent-2); padding-left: 1em; }}
  .controls {{
    position: fixed;
    right: 1rem;
    bottom: 1rem;
    display: flex;
    gap: 0.5em;
    z-index: 50;
  }}
  .controls button {{
    appearance: none;
    border: 1px solid var(--line);
    background: var(--surface);
    color: var(--ink);
    padding: 0.5em 0.85em;
    border-radius: 999px;
    cursor: pointer;
    font-size: 0.85rem;
    box-shadow: var(--shadow);
  }}
  .controls button:focus-visible {{ outline: 3px solid var(--accent-2); outline-offset: 2px; }}
  /* mobile */
  @media (max-width: 920px) {{
    .layout {{ grid-template-columns: 1fr; padding: 1.4em 1em 3em; }}
    aside.toc-side {{
      position: static;
      max-height: none;
      margin-bottom: 1.4em;
    }}
    aside.toc-side details summary {{
      cursor: pointer;
      list-style: none;
      font-weight: 600;
      color: var(--accent);
    }}
  }}
  /* reduced motion */
  @media (prefers-reduced-motion: reduce) {{
    html {{ scroll-behavior: auto; }}
    * {{ animation: none !important; transition: none !important; }}
  }}
  /* print */
  @media print {{
    .controls, aside.toc-side, .skip-link {{ display: none; }}
    .layout {{ display: block; padding: 0; }}
    main {{ max-width: none; }}
    body {{ font-size: 11pt; }}
    h1, h2, h3 {{ break-after: avoid; }}
    figure, table {{ break-inside: avoid; }}
    pre {{ white-space: pre-wrap; font-size: 9pt; }}
    header.cover {{ background: none; color: #000; }}
    header.cover h1 {{ color: #000; }}
    header.cover .sub, header.cover .meta {{ color: #000; }}
    a {{ color: #000; text-decoration: none; }}
  }}
</style>
</head>
<body data-theme="light">
<a class="skip-link" href="#main-content">Skip to content</a>

<header class="cover" role="banner">
  <h1>{title}</h1>
  <div class="sub">AI Crisis Management for Small Communities</div>
  <div class="meta">
    <div><b>Author</b>{author}</div>
    <div><b>Roll</b>{roll}</div>
    <div><b>Degree</b>{degree}</div>
    <div><b>Mentor</b>{mentor}</div>
    <div><b>School</b>{school}</div>
    <div><b>University</b>{uni}</div>
    <div><b>Location</b>{loc}</div>
    <div><b>Year</b>{year}</div>
    <div><b>Live at</b><a href="https://{domain}">{domain}</a></div>
  </div>
</header>

<div class="layout">
  <aside class="toc-side" aria-label="Table of contents">
    <details open>
      <summary><h2 style="display:inline">On this page</h2></summary>
      <ol>
        {nav_html}
      </ol>
    </details>
  </aside>

  <main id="main-content" role="main">
    {body}
  </main>
</div>

<div class="controls" aria-hidden="false">
  <button id="theme-toggle" aria-label="Toggle dark mode" title="Toggle theme">Dark</button>
  <button id="back-top" aria-label="Back to top" title="Back to top">Top ↑</button>
</div>

<script>
(function() {{
  // theme
  const root = document.body;
  const btn = document.getElementById('theme-toggle');
  const stored = localStorage.getItem('lp-theme');
  if (stored) root.setAttribute('data-theme', stored);
  btn.textContent = root.getAttribute('data-theme') === 'dark' ? 'Light' : 'Dark';
  btn.addEventListener('click', () => {{
    const next = root.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
    root.setAttribute('data-theme', next);
    localStorage.setItem('lp-theme', next);
    btn.textContent = next === 'dark' ? 'Light' : 'Dark';
  }});
  // back-to-top
  document.getElementById('back-top').addEventListener('click', () => {{
    window.scrollTo({{ top: 0, behavior: 'smooth' }});
  }});
  // active section
  const links = document.querySelectorAll('aside.toc-side a');
  const map = new Map();
  links.forEach(l => {{
    const id = l.getAttribute('href').slice(1);
    const el = document.getElementById(id);
    if (el) map.set(el, l);
  }});
  if ('IntersectionObserver' in window) {{
    const io = new IntersectionObserver((entries) => {{
      entries.forEach(e => {{
        if (e.isIntersecting) {{
          links.forEach(l => l.classList.remove('active'));
          const link = map.get(e.target);
          if (link) link.classList.add('active');
        }}
      }});
    }}, {{ rootMargin: '-30% 0px -55% 0px', threshold: 0 }});
    map.forEach((_, sec) => io.observe(sec));
  }}
}})();
</script>
<script defer src="https://cdn.jsdelivr.net/npm/prismjs@1.29.0/components/prism-core.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/prismjs@1.29.0/plugins/autoloader/prism-autoloader.min.js"></script>
</body>
</html>
"""


def build():
    OUT.parent.mkdir(parents=True, exist_ok=True)
    html = render_html()
    OUT.write_text(html, encoding="utf-8")
    print(f"Wrote {OUT} ({OUT.stat().st_size} bytes, {OUT.stat().st_size/1024:.1f} KiB)")


if __name__ == "__main__":
    build()
