#!/usr/bin/env python3
"""
Generate an animated SVG info card (info-card.svg) styled like neofetch.
Uses SMIL animations (supported by GitHub) for:
  - Line-by-line fade-in on startup
  - Marquee scroll for the Stack row
"""

import html
import os

# Customize your information here
NAME        = "Tanishq4258"
TITLE       = html.escape("Software Developer & Engineering Student")
LOCATION    = "Chandigarh, India"
STACK       = html.escape("Python  ·  C++  ·  Java  ·  SQL  ·  JavaScript  ·  HTML/CSS  ·  React  ·  Node.js  ·  Git  ·  Linux")
INTERESTS   = html.escape("AI/ML, Web Systems, IoT & Hardware")
HIGHLIGHTS  = "Building Intellitrade"

# SMIL fade-in helper — each line fades in sequentially on load
def fade_in(delay: float) -> str:
    return (
        f'<animate attributeName="opacity" from="0" to="1" '
        f'dur="0.5s" begin="{delay:.2f}s" fill="freeze" />'
    )

# Width of the scrollable stack area (px)
SCROLL_AREA_W = 342   # 490 - 24(left pad) - 100(key col) - 24(right pad)
# Approximate text width at 13px monospace (~7.8px per char)
STACK_TEXT_W  = int(len(STACK) * 7.9)
# Scroll duration scales with text length
SCROLL_DUR    = max(8, len(STACK) // 8)

SVG_TEMPLATE = f"""<svg fill="none" width="490" height="340" viewBox="0 0 490 340"
     xmlns="http://www.w3.org/2000/svg">

  <defs>
    <!-- Clip mask so stack text doesn't overflow its cell -->
    <clipPath id="stack-clip">
      <rect x="0" y="-14" width="{SCROLL_AREA_W}" height="20" />
    </clipPath>
  </defs>

  <style>
    .bg          {{ fill: #0d1117; stroke: #30363d; stroke-width: 1px; }}
    .title-bar   {{ fill: #161b22; }}
    .dot-r       {{ fill: #ff5f56; }}
    .dot-y       {{ fill: #ffbd2e; }}
    .dot-g       {{ fill: #27c93f; }}
    .hdr         {{ font-family: 'Fira Code', monospace; font-size: 13px; fill: #8b949e; font-weight: 600; }}
    .key         {{ font-family: 'Fira Code', monospace; font-size: 13px; fill: #58a6ff; font-weight: bold; }}
    .val         {{ font-family: 'Fira Code', monospace; font-size: 13px; fill: #c9d1d9; }}
    .prompt      {{ font-family: 'Fira Code', monospace; font-size: 13px; fill: #7fe436; font-weight: bold; }}
    .cursor      {{ fill: #7fe436; }}
  </style>

  <!-- ── Card Background ────────────────────────────────────── -->
  <rect class="bg" width="490" height="340" rx="10" ry="10" />

  <!-- ── Terminal Title Bar ─────────────────────────────────── -->
  <path class="title-bar"
        d="M 0 10 C 0 4.477 4.477 0 10 0 L 480 0 C 485.523 0 490 4.477 490 10 L 490 32 L 0 32 Z" />
  <circle class="dot-r" cx="18" cy="16" r="5" />
  <circle class="dot-y" cx="34" cy="16" r="5" />
  <circle class="dot-g" cx="50" cy="16" r="5" />
  <text class="hdr" x="70" y="20">{NAME}@github:~ $ neofetch</text>

  <!-- ── Content ───────────────────────────────────────────── -->
  <g transform="translate(24, 60)">

    <!-- Line 0: username header  (fade in at 0.1s) -->
    <g opacity="0">
      {fade_in(0.1)}
      <text class="prompt" x="0" y="0">{NAME}</text>
      <text class="val"    x="90" y="0">@github</text>
      <!-- blinking cursor after username -->
      <rect class="cursor" x="175" y="-12" width="8" height="14" rx="1">
        <animate attributeName="opacity" values="1;0;1" dur="1s"
                 begin="0.6s" repeatCount="3" fill="freeze"/>
      </rect>
      <line x1="0" y1="10" x2="442" y2="10" stroke="#30363d" stroke-width="1"/>
    </g>

    <!-- Line 1: Role  (fade in at 0.5s) -->
    <g transform="translate(0, 35)" opacity="0">
      {fade_in(0.5)}
      <text class="key" x="0" y="0">Role</text>
      <text class="val" x="100" y="0">›  {TITLE}</text>
    </g>

    <!-- Line 2: Location  (fade in at 0.8s) -->
    <g transform="translate(0, 65)" opacity="0">
      {fade_in(0.8)}
      <text class="key" x="0" y="0">Location</text>
      <text class="val" x="100" y="0">›  {LOCATION}</text>
    </g>

    <!-- Line 3: Stack — scrolling marquee  (fade in at 1.1s) -->
    <g transform="translate(0, 95)" opacity="0">
      {fade_in(1.1)}
      <text class="key" x="0" y="0">Stack</text>
      <!-- clip the scrolling text to its column -->
      <g transform="translate(100, 0)" clip-path="url(#stack-clip)">
        <text class="val" x="0" y="0">
          ›  {STACK}
          <!-- After a 1.5s pause, scroll left; loop forever -->
          <animateTransform attributeName="transform" type="translate"
            values="0,0; -{STACK_TEXT_W},0"
            dur="{SCROLL_DUR}s"
            begin="1.6s"
            repeatCount="indefinite"
            calcMode="linear"/>
        </text>
      </g>
    </g>

    <!-- Line 4: Interests  (fade in at 1.4s) -->
    <g transform="translate(0, 125)" opacity="0">
      {fade_in(1.4)}
      <text class="key" x="0" y="0">Interests</text>
      <text class="val" x="100" y="0">›  {INTERESTS}</text>
    </g>

    <!-- Line 5: Projects  (fade in at 1.7s) -->
    <g transform="translate(0, 155)" opacity="0">
      {fade_in(1.7)}
      <text class="key" x="0" y="0">Projects</text>
      <text class="val" x="100" y="0">›  {HIGHLIGHTS}</text>
    </g>

    <!-- Line 6: Color swatch bar  (fade in at 2.0s) -->
    <g transform="translate(0, 195)" opacity="0">
      {fade_in(2.0)}
      <rect fill="#21262d" x="0"   y="0" width="20" height="12" rx="2"/>
      <rect fill="#ff7b72" x="26"  y="0" width="20" height="12" rx="2"/>
      <rect fill="#7ee787" x="52"  y="0" width="20" height="12" rx="2"/>
      <rect fill="#ffa657" x="78"  y="0" width="20" height="12" rx="2"/>
      <rect fill="#79c0ff" x="104" y="0" width="20" height="12" rx="2"/>
      <rect fill="#d2a8ff" x="130" y="0" width="20" height="12" rx="2"/>
      <rect fill="#a5d6ff" x="156" y="0" width="20" height="12" rx="2"/>
    </g>

  </g>
</svg>
"""


def main():
    output_path = os.path.join(os.path.dirname(__file__), "..", "info-card.svg")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(SVG_TEMPLATE.strip())
    print(f"Generated {output_path}")


if __name__ == "__main__":
    main()