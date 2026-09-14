#!/usr/bin/env python3
"""check-wallpaper.py — batch CVD simulation and luminance audit for wallpapers.

Requires only Pillow. The colour maths is stdlib, matching the rest of tools/.

Two things a live screen filter cannot give you:

  1. Cross-validation. Colour vision simulation is a model, not ground truth,
     and models disagree. This runs BOTH the Machado, Oliveira & Fernandes
     (2009) matrices and the Vienot, Brettel & Mollon (1999) matrices used by
     Color Oracle. Where the two agree, trust the result. Where they diverge,
     those colours sit near a perceptual boundary and should be changed
     regardless of which model is right.

  2. A luminance audit. The lock screen and bar draw straight onto the
     wallpaper. This measures whether any region is bright enough (dark theme)
     or dark enough (light theme) to swallow overlaid text, which is a failure
     a colour filter will not show you.

Usage:
    python3 check-wallpaper.py --mode dark  wallpapers/*.png
    python3 check-wallpaper.py --mode light --no-render paper-*.jpg
"""
import argparse, os, sys

try:
    from PIL import Image
except ImportError:
    sys.exit("Pillow is required.  sudo pacman -S python-pillow")

# ---------------------------------------------------------------- models

# Machado, Oliveira & Fernandes (2009), severity 1.0.
MACHADO = {
    "protan": (0.152286, 1.052583, -0.204868,
               0.114503, 0.786281, 0.099216,
               -0.003882, -0.048116, 1.051998),
    "deutan": (0.367322, 0.860646, -0.227968,
               0.280085, 0.672501, 0.047413,
               -0.011820, 0.042940, 0.968881),
    "tritan": (1.255528, -0.076749, -0.178779,
               -0.078411, 0.930809, 0.147602,
               0.004733, 0.691367, 0.303900),
}

# Vienot, Brettel & Mollon (1999). Independent derivation, so this is a real
# cross-check rather than a restatement of the same model.
VIENOT = {
    "protan": (0.11238, 0.88762, 0.00000,
               0.11238, 0.88762, 0.00000,
               0.00401, -0.00401, 1.00000),
    "deutan": (0.29275, 0.70725, 0.00000,
               0.29275, 0.70725, 0.00000,
               -0.02234, 0.02234, 1.00000),
    "tritan": (1.00000, 0.14461, -0.14461,
               0.00000, 1.00000, 0.00000,
               0.00000, 0.85659, 0.14341),
}

# 8-bit sRGB -> linear, precomputed once.
_LIN = [((c / 255) / 12.92 if (c / 255) <= 0.04045
         else (((c / 255) + 0.055) / 1.055) ** 2.4) for c in range(256)]


def _encode(v):
    v = 0.0 if v < 0.0 else (1.0 if v > 1.0 else v)
    return v * 12.92 if v <= 0.0031308 else 1.055 * v ** (1 / 2.4) - 0.055


def simulate_px(px, m):
    """Apply a 3x3 matrix in LINEAR light. px is an (r,g,b) 0-255 tuple."""
    r, g, b = _LIN[px[0]], _LIN[px[1]], _LIN[px[2]]
    return (_encode(m[0] * r + m[1] * g + m[2] * b),
            _encode(m[3] * r + m[4] * g + m[5] * b),
            _encode(m[6] * r + m[7] * g + m[8] * b))


def luminance_px(px):
    return 0.2126 * _LIN[px[0]] + 0.7152 * _LIN[px[1]] + 0.0722 * _LIN[px[2]]


# ---------------------------------------------------------------- audits

def divergence(pixels, kind):
    """Mean gap between the two models, 0-100.

    High divergence means the image leans on colours the models disagree
    about, which is itself a reason to pick different colours.
    """
    a, b = MACHADO[kind], VIENOT[kind]
    total = 0.0
    for px in pixels:
        pa, pb = simulate_px(px, a), simulate_px(px, b)
        total += (abs(pa[0] - pb[0]) + abs(pa[1] - pb[1]) + abs(pa[2] - pb[2])) / 3
    return total / len(pixels) * 100


def mass_report(lum, mode):
    """Fraction of the frame that will swallow overlaid text."""
    if mode == "dark":
        bad = sum(1 for y in lum if y > 0.18)
        return bad / len(lum) * 100, "bright"
    bad = sum(1 for y in lum if y < 0.55)
    return bad / len(lum) * 100, "dark"


def worst_block(lum, w, h, mode, grid=12):
    """Scan the frame in blocks; return the worst block's mean luminance."""
    bh, bw = h // grid, w // grid
    vals = []
    for r in range(grid):
        for c in range(grid):
            s = n = 0
            for y in range(r * bh, (r + 1) * bh):
                row = y * w
                for x in range(c * bw, (c + 1) * bw):
                    s += lum[row + x]
                    n += 1
            vals.append(s / n)
    return max(vals) if mode == "dark" else min(vals)


def text_contrast(block_y, mode):
    """WCAG contrast of the shell's text colour over the worst block."""
    text_y = 1.0 if mode == "dark" else 0.0053   # white, or near-black
    hi, lo = max(block_y, text_y), min(block_y, text_y)
    return (hi + 0.05) / (lo + 0.05)


# ---------------------------------------------------------------- main

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("images", nargs="+")
    ap.add_argument("--mode", choices=("dark", "light"), required=True)
    ap.add_argument("--outdir", default="cvd-sim")
    ap.add_argument("--no-render", action="store_true",
                    help="audit only, do not write simulated images")
    args = ap.parse_args()

    if not args.no_render:
        os.makedirs(args.outdir, exist_ok=True)
    failed = []

    for path in args.images:
        try:
            im = Image.open(path).convert("RGB")
        except Exception as e:
            print(f"{path}: cannot open ({e})", file=sys.stderr)
            continue

        W, H = 480, 270
        thumb = im.resize((W, H), Image.BILINEAR)
        # get_flattened_data() is Pillow 11+; getdata() is deprecated but is
        # what Omarchy's current python-pillow still ships.
        small = list(thumb.get_flattened_data()) if hasattr(
            thumb, "get_flattened_data") else list(thumb.getdata())
        lum = [luminance_px(p) for p in small]

        pct, label = mass_report(lum, args.mode)
        blk = worst_block(lum, W, H, args.mode)
        cr = text_contrast(blk, args.mode)

        print(f"\n{os.path.basename(path)}  [{im.width}x{im.height}]")
        print(f"  {label} area that fights overlaid text : {pct:5.1f}%")
        print(f"  worst 1/144 block vs shell text        : {cr:5.2f}:1", end="")
        if cr < 4.5:
            print("   <-- FAILS, text unreadable there")
            failed.append(os.path.basename(path))
        elif cr < 7.0:
            print("   <-- marginal, add a scrim behind lock text")
        else:
            print("   ok")

        for kind in ("protan", "deutan", "tritan"):
            dv = divergence(small, kind)
            note = "  <-- models disagree, colours near a boundary" if dv > 4 else ""
            print(f"  {kind:7s} model divergence             : {dv:5.2f}{note}")

        if not args.no_render:
            stem = os.path.splitext(os.path.basename(path))[0]
            for kind in ("protan", "deutan", "tritan"):
                for tag, mats in (("machado", MACHADO), ("vienot", VIENOT)):
                    m = mats[kind]
                    out = im.convert("RGB", (m[0], m[1], m[2], 0,
                                             m[3], m[4], m[5], 0,
                                             m[6], m[7], m[8], 0))
                    out.save(os.path.join(args.outdir,
                                          f"{stem}.{kind}.{tag}.png"), optimize=True)

    if not args.no_render:
        print(f"\nSimulated images written to {args.outdir}/")
        print("Note: rendered previews apply the matrix in sRGB space for speed.")
        print("The audit numbers above use correct linear-light maths.")
    if failed:
        print(f"\nFAILED: {', '.join(failed)}")
    print("\nAlso view every wallpaper in plain greyscale. If the composition "
          "survives that, it survives any colour vision deficiency.")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()