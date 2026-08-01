#!/usr/bin/env python3
"""
Generate an animated SVG card (info-card.svg) styled like neofetch.
"""

import os

# Set STATIC=1 in environment variables if you want a non-animated preview frame
STATIC = os.getenv("STATIC") == "1"

# Customize your information here
NAME = "Tanishq Chhabra"
TITLE = "Software Developer & Engineering Student"
LOCATION = "Chandiarh, India"
STACK = " Python, C++, Java, SQL, JavaScript, HTML/CSS, React, Node.js"
INTERESTS = "AI/ML, Web Systems, IoT & Hardware"
HIGHLIGHTS = "Building Intellitrade"

line_styles = "".join(f"""
    .line-{i} {{
      animation: fadeIn 0.4s ease-out {0.1 + i * 0.15}s forwards;
      opacity: {1 if STATIC else 0};
      transform: translateY(5px);
    }}""" for i in range(7))

SVG_TEMPLATE = f"""<svg fill="none" width="490" height="340" viewBox="0 0 490 340" xmlns="http://www.w3.org/2000/svg">
  <style>
    .bg {{ fill: #0d1117; rx: 10px; ry: 10px; stroke: #30363d; stroke-width: 1px; }}
    .title-bar {{ fill: #161b22; }}
    .dot-red {{ fill: #ff5f56; }}
    .dot-yellow {{ fill: #ffbd2e; }}
    .dot-green {{ fill: #27c93f; }}
    .header-text {{ font-family: 'Fira Code', monospace, Consolas; font-size: 13px; fill: #8b949e; font-weight: 600; }}
    .key {{ font-family: 'Fira Code', monospace, Consolas; font-size: 13px; fill: #58a6ff; font-weight: bold; }}
    .val {{ font-family: 'Fira Code', monospace, Consolas; font-size: 13px; fill: #c9d1d9; }}
    .prompt {{ font-family: 'Fira Code', monospace, Consolas; font-size: 13px; fill: #7fe436; font-weight: bold; }}
    
    {line_styles}

    @keyframes fadeIn {{
      to {{
        opacity: 1;
        transform: translateY(0);
      }}
    }}
  </style>

  <!-- Card Background -->
  <rect class="bg" width="490" height="340" />

  <!-- Terminal Header Bar -->
  <path class="title-bar" d="M 0 10 C 0 4.477 4.477 0 10 0 L 480 0 C 485.523 0 490 4.477 490 10 L 490 32 L 0 32 Z" />
  <circle class="dot-red" cx="18" cy="16" r="5" />
  <circle class="dot-yellow" cx="34" cy="16" r="5" />
  <circle class="dot-green" cx="50" cy="16" r="5" />
  <text class="header-text" x="70" y="20">{NAME}@github:~ (neofetch)</text>

  <!-- Neofetch Content Lines -->
  <g transform="translate(24, 60)">
    <!-- Line 0: User Header -->
    <g class="line-0">
      <text class="prompt" x="0" y="0">{NAME}</text>
      <text class="val" x="120" y="0">@github</text>
      <line x1="0" y1="10" x2="442" y2="10" stroke="#30363d" stroke-width="1"/>
    </g>

    <!-- Line 1: Role -->
    <g class="line-1" transform="translate(0, 35)">
      <text class="key" x="0" y="0">Role</text>
      <text class="val" x="100" y="0">› {TITLE}</text>
    </g>

    <!-- Line 2: Location -->
    <g class="line-2" transform="translate(0, 65)">
      <text class="key" x="0" y="0">Location</text>
      <text class="val" x="100" y="0">› {LOCATION}</text>
    </g>

    <!-- Line 3: Stack -->
    <g class="line-3" transform="translate(0, 95)">
      <text class="key" x="0" y="0">Stack</text>
      <text class="val" x="100" y="0">› {STACK}</text>
    </g>

    <!-- Line 4: Focus -->
    <g class="line-4" transform="translate(0, 125)">
      <text class="key" x="0" y="0">Interests</text>
      <text class="val" x="100" y="0">› {INTERESTS}</text>
    </g>

    <!-- Line 5: Highlights -->
    <g class="line-5" transform="translate(0, 155)">
      <text class="key" x="0" y="0">Projects</text>
      <text class="val" x="100" y="0">› {HIGHLIGHTS}</text>
    </g>

    <!-- Line 6: Color Palette Bar -->
    <g class="line-6" transform="translate(0, 195)">
      <rect fill="#21262d" x="0" y="0" width="20" height="12" rx="2" />
      <rect fill="#ff7b72" x="26" y="0" width="20" height="12" rx="2" />
      <rect fill="#7ee787" x="52" y="0" width="20" height="12" rx="2" />
      <rect fill="#ffa657" x="78" y="0" width="20" height="12" rx="2" />
      <rect fill="#79c0ff" x="104" y="0" width="20" height="12" rx="2" />
      <rect fill="#d2a8ff" x="130" y="0" width="20" height="12" rx="2" />
      <rect fill="#a5d6ff" x="156" y="0" width="20" height="12" rx="2" />
    </g>
  </g>
</svg>
"""

def main():
    output_path = "info-card.svg"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(SVG_TEMPLATE.strip())
    print(f"Generated {output_path}")

if __name__ == "__main__":
    main()