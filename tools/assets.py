"""Write the non-palette theme assets: shell section overrides, background
prompts, and the installer."""
import os
from verify import VARIANTS, build, OUT
from colorlib import contrast, hex_to_rgb, rgb_to_hex

HEADER = ("# Section override for the Omarchy shell. The filename selects the\n"
          "# section, so no [header] is needed. Only this section is replaced;\n"
          "# the rest of shell.toml is still generated from the default template.\n\n")

# Per-variant wallpaper direction. Every shipped wallpaper is a flat papercut
# nature scene: landforms low in the frame or in the corners, open sky across
# the centre, because the lock screen draws there. Papercut rather than photo,
# because real grass, leaves, stars and ripples are exactly the fine repeating
# detail that causes visual stress. The palette dictates the luminance envelope
# of the centre; the vision type dictates which hues are allowed at all.
STYLE = {
    "dark": (
        "Flat papercut illustration style: large simple shapes, solid matte colour, "
        "hard crisp edges, no gradients, no glow, no halo, no drop shadows, no texture "
        "or grain. No fine detail: no star fields, no individual grass blades, no leaf "
        "veins, no water ripples, no foliage texture. No text, no people. Keep the "
        "central third of the frame, horizontally and vertically, completely empty "
        "flat sky: nothing there above 20% luminance and no shape crossing into it, "
        "not even a dark one. 16:9, as large as the generator allows."),
    "light": (
        "Flat papercut illustration style: large simple shapes, solid matte colour, "
        "hard crisp edges, no gradients, no glow, no halo, no drop shadows, no texture "
        "or grain. No fine detail: no individual grass blades, no leaf veins, no water "
        "ripples, no foliage texture. No text, no people. Keep the central third of "
        "the frame, horizontally and vertically, completely empty flat pale sky: "
        "nothing there below 50% luminance and no shape crossing into it, not even a "
        "pale one. 16:9, as large as the generator allows."),
}

# One example scene per variant, in that family's setting. The skies name the
# hex *and* say what not to paint: asked for a "deep navy sky (#10141A)", the
# generator painted saturated navy, which pushed CVD model divergence past 4.
BG_PROMPTS = {
    "omarchy-beacon-dark-theme": (
        "Night landscape. Solid very dark desaturated blue-charcoal sky, almost "
        "black (#10141A). Three layers of muted slate and dusty blue mountain "
        "silhouettes confined to the bottom fifth of the frame, with a flat still "
        "lake below them. A small pale cream full moon in the top-left corner. Low "
        "saturation throughout."),
    "omarchy-beacon-redgreen-dark-theme": (
        "Desert or ocean at night. Solid very dark desaturated blue-black sky, "
        "almost black (#10141A); not navy, not royal blue. Amber and burnt-orange "
        "dune silhouettes confined to the bottom fifth of the frame. A small pale "
        "orange moon in the top-left corner. Only blue-black, blue, sky blue, orange "
        "and amber. No green, no red, no magenta anywhere."),
    "omarchy-beacon-blueyellow-dark-theme": (
        "Forest, flowers or volcano at night. Solid very dark warm plum-charcoal "
        "sky, almost black (#10141A); not blue. Deep-green conifer silhouettes "
        "confined to the bottom fifth of the frame. A thin amber crescent moon in "
        "the top-left corner. Only vermilion, green, magenta, amber and cream. No "
        "blue, no teal, no cyan anywhere."),
    "omarchy-beacon-light-theme": (
        "Morning landscape. Solid warm off-white sky (#FAF9F6). Layered sand-beige "
        "and pale warm-grey dune shapes confined to the bottom fifth of the frame. "
        "A small soft charcoal sun disc in the top-right corner. Low saturation "
        "throughout."),
    "omarchy-beacon-redgreen-light-theme": (
        "Desert, beach or glacier in daylight. Solid warm off-white or very pale "
        "sky-blue sky. Flat amber and burnt-orange mesa silhouettes confined to the "
        "bottom fifth of the frame, with navy shadows on their faces. Only blue, sky "
        "blue, navy, orange and amber. No green, no red, no magenta anywhere."),
    "omarchy-beacon-blueyellow-light-theme": (
        "Meadow, leaves or hills in daylight. Solid warm cream sky (#FAF9F6). Large, "
        "simple monstera and banana leaves in mid green and deep green, entering "
        "from the top-right and bottom-left corners only. Only vermilion, green, "
        "magenta, amber and cream. No blue, no teal, no cyan anywhere."),
}

BG_README = """# Backgrounds for `{name}`

The Omarchy shell renders the background itself in Quattro; cycle images with
**Super + Ctrl + Space**. Users can add their own without touching this theme by
putting files in `~/.config/omarchy/backgrounds/{name}/`.

## Shipped wallpapers

{listing}

All are flat papercut nature scenes with the central third of the frame left
as open sky, checked against the rules below before shipping.

## What makes a wallpaper accessible

A wallpaper is not decoration here, it is the substrate the lock screen, the bar
and any desktop text sit on. Three rules:

1. **Keep the centre clear.** The lock screen draws in the middle of the frame.
   This is a {mode} theme, so the central third must stay {envelope}.
   Landforms belong low in the frame or in the corners, moons and suns in a
   corner.
2. **No high-frequency detail.** Fine stripes, dot grids, halftones and dense
   noise cause visual stress and can trigger symptoms in photosensitive users.
   They also shimmer through the bar's translucency. That rules out realistic
   grass, leaves, star fields and water, which is why these are papercut.
3. **Match the palette's hue policy.** {hue_note}

## Adding another

Generation prompt matched to this variant. Swap the scene for any other in
this family's setting, but keep the sky wording and the style sentences:

```
{prompt}
```

Then audit it:

```bash
python3 tools/check-wallpaper.py --mode {mode} path/to/image.jpg
```

Trust the model divergence figure (under 4 is clean) and the "area that fights
overlaid text" percentage. The worst-block contrast line scans the whole frame,
not just the centre, so it fails images whose shapes sit harmlessly in a corner.
Check the central third by eye.

Name new files `{stem}-NN-scene-name.jpg`, continuing the sequence.

## Export

- 16:9 at your panel's native resolution.
- Also export **1200x675 WebP under 100 KB** if you submit this theme to the
  Omarchy theme gallery, which is the screenshot spec.
"""

HUE_NOTE = {
    "omarchy-beacon-dark-theme": "Any hue is fine, but keep saturation low so it "
        "does not compete with the palette's accent colours.",
    "omarchy-beacon-light-theme": "Any hue is fine, but keep saturation low so it "
        "does not compete with the palette's accent colours.",
    "omarchy-beacon-redgreen-dark-theme": "Blue, sky blue, navy, orange and amber "
        "only. No green, red or magenta: a red-green contrast in the wallpaper is "
        "invisible to the people this variant is for.",
    "omarchy-beacon-redgreen-light-theme": "Blue, sky blue, navy, orange and amber "
        "only. No green, red or magenta: a red-green contrast in the wallpaper is "
        "invisible to the people this variant is for.",
    "omarchy-beacon-blueyellow-dark-theme": "Vermilion, green, magenta, amber and "
        "cream only. No blue, teal or cyan, which collapse together under "
        "tritanopia.",
    "omarchy-beacon-blueyellow-light-theme": "Vermilion, green, magenta, amber and "
        "cream only. No blue, teal or cyan, which collapse together under "
        "tritanopia.",
}


ICONS = {"blue": "Yaru-blue", "red": "Yaru-red"}
TEXT, HIGHLIGHT, NONTEXT = 7.0, 4.5, 3.0


def over(color, alpha, under):
    """The shell draws a state fill as `color` at `alpha` over the surface."""
    c, u = hex_to_rgb(color), hex_to_rgb(under)
    return rgb_to_hex(tuple(c[i] * alpha + u[i] * (1 - alpha) for i in range(3)))


def selection_fill_alpha(fg, bg, ceiling=0.35):
    """Strongest text-selection tint, up to Omarchy's 0.35, that keeps 4.5:1."""
    alpha = ceiling
    while alpha > 0.05 and contrast(fg, over(fg, alpha, bg)) < HIGHLIGHT + 0.1:
        alpha = round(alpha - 0.01, 2)
    return alpha


def write(path, text):
    with open(path, "w") as f:
        f.write(text)


def main():
    for name, spec in VARIANTS.items():
        p = build(spec)
        d = os.path.join(OUT, name)
        acc, fg, bfg = p["accent"], p["foreground"], p["bright_foreground"]
        muted, inact = p["muted"], p["inactive_border"]

        bgc = p["background"]
        acc_bright = p["bright_" + spec["accent_slot"]]
        # Every key of each section is written, because an override replaces the
        # whole section and the shell's fallbacks are not always safe:
        # menu.selected-border-alpha falls back to 0.0, which made the selected
        # row's edge cue invisible while only selected-border was set.
        sel_alpha = selection_fill_alpha(fg, bgc)
        checks = [
            ("controls normal", fg, over(fg, 0.04, bgc), TEXT),
            ("controls hover", bfg, over(bfg, 0.08, bgc), TEXT),
            ("controls focus", bfg, over(bfg, 0.08, bgc), TEXT),
            ("controls selected", bfg, over(bfg, 0.18, bgc), TEXT),
            ("controls pressed", bfg, over(bfg, 0.22, bgc), HIGHLIGHT),
            ("controls text selection", fg, over(fg, sel_alpha, bgc), HIGHLIGHT),
            ("controls borders", muted, bgc, NONTEXT),
            ("controls focus ring", acc, bgc, NONTEXT),
            ("notification text", fg, bgc, TEXT),
            ("notification border", acc, bgc, NONTEXT),
            ("menu text", fg, bgc, TEXT),
            ("menu selected text", acc, over(fg, 0.08, bgc), TEXT),
            ("menu border", inact, bgc, NONTEXT),
            ("menu selected edge", acc, over(fg, 0.08, bgc), NONTEXT),
            ("lock text", bfg, bgc, TEXT),
            ("lock placeholder", muted, bgc, TEXT),
            ("lock error text", p["red"], bgc, TEXT),
            ("lock selected text", bfg, p["selection"], TEXT),
            ("lock borders", acc, bgc, NONTEXT),
            ("lock border, typing", acc_bright, bgc, NONTEXT),
            ("lock border, error", p["red"], bgc, NONTEXT),
        ]
        failed = [(a, contrast(f, b), m) for a, f, b, m in checks if contrast(f, b) < m]
        if failed:
            raise SystemExit(f"{name}: shell sections fail: {failed}")

        # Controls. Focus is 3px on every side rather than a thin ring, the
        # selected state gets a 2px edge rather than none, and every border alpha
        # is 1.0 -- translucency silently eats the 3:1 that WCAG 1.4.11 requires
        # of a control boundary.
        write(os.path.join(d, "shell.controls.toml"), HEADER + f"""normal-color        = "{fg}"
normal-fill-alpha   = 0.04
normal-border       = "{muted}"
normal-border-width = 1
normal-border-alpha = 1.0

hover-cursor-color        = "{bfg}"
hover-cursor-fill-alpha   = 0.08
hover-cursor-border       = "{acc}"
hover-cursor-border-width = 2
hover-cursor-border-alpha = 1.0

focus-color        = "{bfg}"
focus-fill-alpha   = 0.08
focus-border       = "{acc}"
focus-border-width = 3
focus-border-alpha = 1.0

selected-color        = "{bfg}"
selected-fill-alpha   = 0.18
selected-border       = "{acc}"
selected-border-width = 2
selected-border-alpha = 1.0

pressed-fill-alpha   = 0.22
selection-fill-alpha = {sel_alpha:.2f}
""")

        # Notifications. The heavy left edge is a non-colour cue, so urgency is
        # not carried by hue alone (WCAG 1.4.1).
        write(os.path.join(d, "shell.notifications.toml"), HEADER + f"""background        = "{bgc}"
background-alpha  = 1.0
text              = "{fg}"
border            = "{acc}"
border-alpha      = 1.0
border-width      = 2
border-width-left = 6
countdown         = "{acc}"
""")

        # Menu. Selection is marked by a 4px left edge as well as a fill, again
        # so the cue survives without colour discrimination.
        write(os.path.join(d, "shell.menu.toml"), HEADER + f"""background                = "{bgc}"
background-alpha          = 1.0
text                      = "{fg}"
border                    = "{inact}"
border-width              = 2
border-alpha              = 1.0
scrim                     = "{bgc}"
scrim-alpha               = 0.5
selected-background       = "{fg}"
selected-background-alpha = 0.08
selected-text             = "{acc}"
selected-border           = "{acc}"
selected-border-width     = "1 1 1 4"
selected-border-alpha     = 1.0
""")

        # Lock. The password card is fully opaque, so its text keeps its verified
        # contrast over any wallpaper. The default 0.8 lets a bright image show
        # through behind the text.
        write(os.path.join(d, "shell.lock.toml"), HEADER + f"""background       = "{bgc}"
background-alpha = 1.0
text             = "{bfg}"
placeholder      = "{muted}"
text-error       = "{p['red']}"
border           = "{acc}"
border-active    = "{acc_bright}"
border-error     = "{p['red']}"
border-alpha     = 1.0
selection        = "{p['selection']}"
selection-alpha  = 1.0
""")

        # GTK icon colour. Every stock Omarchy theme ships one; without it Omarchy
        # falls back to Yaru-blue. Matched to the accent, which also keeps
        # Blue-Yellow variants off the blue their hue policy forbids.
        write(os.path.join(d, "icons.theme"), ICONS[spec["accent_slot"]])

        bg = os.path.join(d, "backgrounds")
        images = sorted(f for f in os.listdir(bg)
                        if f.lower().endswith((".png", ".jpg", ".jpeg", ".webp")))
        stem = name.replace("omarchy-", "").replace("-theme", "")

        def scene(f):
            # beacon-dark-01-alpine-lake-night.jpg -> "Alpine lake night"
            words = os.path.splitext(f)[0][len(stem) + 4:].replace("-", " ")
            return f" — {words.capitalize()}" if words else ""

        listing = "\n".join(f"- `{f}`{scene(f)}" for f in images) or "None yet."
        write(os.path.join(bg, "README.md"), BG_README.format(
            name=name, mode=spec["mode"], listing=listing,
            stem=stem,
            envelope=("empty and dark, with nothing above 20% luminance"
                      if spec["mode"] == "dark" else
                      "empty and light, with nothing below 50% luminance"),
            hue_note=HUE_NOTE[name],
            prompt=BG_PROMPTS[name] + " " + STYLE[spec["mode"]]))

        print(f"assets written: {name}")


if __name__ == "__main__":
    main()
