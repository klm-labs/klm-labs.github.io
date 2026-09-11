#!/usr/bin/env python3
"""Resize a real app capture; no crop, retouching, compositing or UI synthesis."""
import sys
from pathlib import Path
from PIL import Image

if len(sys.argv) != 3:
    raise SystemExit('Usage: prepare-screenshot.py SOURCE.png DESTINATION.webp')
source, destination = map(Path, sys.argv[1:])
if source.resolve() == destination.resolve() or destination.suffix != '.webp':
    raise SystemExit('Use a separate .webp output file; never overwrite the source capture.')
image = Image.open(source).convert('RGB')
image.thumbnail((576, 1280), Image.Resampling.LANCZOS)
destination.parent.mkdir(parents=True, exist_ok=True)
image.save(destination, 'WEBP', quality=86, method=6)
print(f'{destination}: {image.width} × {image.height}, {destination.stat().st_size:,} bytes')
