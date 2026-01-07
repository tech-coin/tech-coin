#!/usr/bin/env python3
from PIL import Image
import argparse
from pathlib import Path

def main():
    ap = argparse.ArgumentParser(description="Cut a 1:1 image into 3 stacked 3:1 banners.")
    ap.add_argument("input", help="Path to square (1:1) image")
    ap.add_argument("-o", "--outdir", default="out_banners", help="Output directory")
    ap.add_argument("--prefix", default="banner", help="Output filename prefix")
    args = ap.parse_args()

    inp = Path(args.input)
    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    im = Image.open(inp).convert("RGBA")
    w, h = im.size
    if w != h:
        raise SystemExit(f"Input must be 1:1 (square). Got {w}x{h}.")

    # Trim to multiple of 3 (center crop) so each banner is exactly 3:1
    s = w
    s3 = (s // 3) * 3
    if s3 != s:
        pad = (s - s3) // 2
        im = im.crop((pad, pad, pad + s3, pad + s3))
        s = s3

    band_h = s // 3  # so width:s = 3*band_h => 3:1

    for i in range(3):
        y0 = i * band_h
        crop = im.crop((0, y0, s, y0 + band_h))
        crop.save(outdir / f"{args.prefix}_{i+1}_3x1.png")

    print(f"Saved 3 banners to: {outdir.resolve()}")

if __name__ == "__main__":
    main()