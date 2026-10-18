#!/usr/bin/env python3
"""Generate a stroked {7/2} heptagram inside a circle. Stdlib only."""

import math
from pathlib import Path

OUT = Path(__file__).resolve().parents[1] / "profile" / "logo.svg"

SIZE = 128
CX = 64.0
CY = 64.0
RADIUS = 46.0
STROKE = 3.0
COLOR = "#c4a35a"
N = 7
STEP = 2


def vertex(i: int) -> tuple[float, float]:
  angle = -math.pi / 2 + i * (2 * math.pi / N)
  return (CX + RADIUS * math.cos(angle), CY + RADIUS * math.sin(angle))


def main() -> None:
  points = [vertex(i) for i in range(N)]
  # One closed polyline: 0 -> 2 -> 4 -> 6 -> 1 -> 3 -> 5 -> 0.
  order = [(i * STEP) % N for i in range(N)]
  cmds = [f"M {points[order[0]][0]:.3f} {points[order[0]][1]:.3f}"]
  for i in order[1:]:
    cmds.append(f"L {points[i][0]:.3f} {points[i][1]:.3f}")
  cmds.append("Z")
  star = " ".join(cmds)
  svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {SIZE} {SIZE}" fill="none" stroke="{COLOR}" stroke-width="{STROKE}" stroke-linejoin="round" stroke-linecap="round">
  <circle cx="{CX:.0f}" cy="{CY:.0f}" r="{RADIUS:.0f}"/>
  <path d="{star}"/>
</svg>
"""
  OUT.parent.mkdir(parents=True, exist_ok=True)
  OUT.write_text(svg)
  print(f"wrote {OUT}")


if __name__ == "__main__":
  main()
