"""Render preview.png for each variant, plus a CVD proof sheet showing how the
palette holds up under simulated protanopia, deuteranopia and tritanopia."""
import os
from PIL import Image, ImageDraw
from colorlib import hex_to_rgb, rgb_to_hex, simulate
from verify import VARIANTS, build, OUT, SLOTS

W, H = 1200, 675
PAD = 48


def rgb(h):
    return tuple(round(c * 255) for c in hex_to_rgb(h))


def swatch(p, sim=None):
    """One 1200x675 panel: background, neutral ramp, chromatic row, bright row."""
    conv = (lambda h: simulate(h, sim)) if sim else (lambda h: h)
    img = Image.new("RGB", (W, H), rgb(conv(p["background"])))
    d = ImageDraw.Draw(img)

    # window-chrome band, to show the active border against the desktop
    d.rectangle([PAD, PAD, W - PAD, PAD + 150],
                fill=rgb(conv(p["lighter_background"])),
                outline=rgb(conv(p["accent"])), width=4)

    # neutral ramp inside the band
    ramp = ["darker_background", "dark_background", "background",
            "lighter_background", "selection", "muted", "dark_foreground",
            "foreground", "light_foreground", "bright_foreground"]
    cw = (W - 2 * PAD - 32) / len(ramp)
    for i, k in enumerate(ramp):
        x = PAD + 16 + i * cw
        d.rectangle([x, PAD + 16, x + cw - 6, PAD + 134], fill=rgb(conv(p[k])))

    # chromatic rows
    for row, prefix in enumerate(("", "bright_")):
        y = PAD + 200 + row * 150
        cw2 = (W - 2 * PAD) / 6
        for i, s in enumerate(SLOTS):
            x = PAD + i * cw2
            d.rectangle([x, y, x + cw2 - 10, y + 130],
                        fill=rgb(conv(p[prefix + s])))

    # a strip of foreground on background, so text contrast is visible as bars
    y = PAD + 510
    for i, k in enumerate(("foreground", "muted", "accent")):
        d.rectangle([PAD + i * 380, y, PAD + i * 380 + 340, y + 22],
                    fill=rgb(conv(p[k])))
        d.rectangle([PAD + i * 380, y + 34, PAD + i * 380 + 200, y + 48],
                    fill=rgb(conv(p[k])))
    return img


def main():
    for name, spec in VARIANTS.items():
        p = build(spec)
        d = os.path.join(OUT, name)
        swatch(p).save(os.path.join(d, "preview.png"), optimize=True)

        # proof sheet: normal + three simulations stacked
        sheet = Image.new("RGB", (W, H * 4), (0, 0, 0))
        for i, sim in enumerate((None, "protan", "deutan", "tritan")):
            sheet.paste(swatch(p, sim), (0, i * H))
        sheet.save(os.path.join(d, "cvd-proof.png"), optimize=True)
        print("preview + proof:", name)


if __name__ == "__main__":
    main()
