"""Write the non-palette theme assets: shell section overrides, background
prompts, and the installer."""
import os
from verify import VARIANTS, build, OUT
from colorlib import contrast

HEADER = ("# Section override for the Omarchy shell. The filename selects the\n"
          "# section, so no [header] is needed. Only this section is replaced;\n"
          "# the rest of shell.toml is still generated from the default template.\n\n")

# Per-variant wallpaper direction. Every shipped wallpaper is flat geometric
# shapes kept to the edges and corners, because the lock screen draws in the
# centre of the frame. The palette dictates the luminance envelope of that
# centre; the vision type dictates which hues are allowed at all.
STYLE = (
    "Flat matte colour, hard crisp edges, no gradients, no vignette, no glow, no "
    "drop shadows, no film or paper grain, no text or lettering, no logos, no dot "
    "grids, halftones or fine repeating patterns. 16:9, as large as the generator "
    "allows.")

CENTRE = {
    "dark": ("Keep the central third of the frame, horizontally and vertically, "
             "completely empty background: nothing there above 20% luminance, and "
             "no shape crossing into it, even a dark one."),
    "light": ("Keep the central third of the frame, horizontally and vertically, "
              "completely empty background: nothing there below 50% luminance, and "
              "no shape crossing into it, even a pale one."),
}

BG_PROMPTS = {
    "omarchy-beacon-dark-theme": (
        "Minimal abstract desktop wallpaper. Solid very dark blue-charcoal base "
        "(#10141A). A small group of simple geometric shapes (circles, half-circles, "
        "rectangles, triangles) clustered in one corner or along one edge, in muted "
        "cream, dusty blue and soft amber. Low saturation."),
    "omarchy-beacon-redgreen-dark-theme": (
        "Minimal abstract desktop wallpaper. Solid very dark blue-charcoal base "
        "(#10141A), not pure black. A small group of simple geometric shapes "
        "clustered in one corner or along one edge, using only blue, sky blue, navy, "
        "orange and amber. No green, no red, no magenta anywhere."),
    "omarchy-beacon-blueyellow-dark-theme": (
        "Minimal abstract desktop wallpaper. Solid very dark charcoal base "
        "(#10141A). A small group of simple geometric shapes clustered in one corner "
        "or along one edge, using only vermilion, deep green, magenta, amber and "
        "cream. No blue, no teal, no cyan anywhere."),
    "omarchy-beacon-light-theme": (
        "Minimal abstract desktop wallpaper. Solid warm off-white base (#FAF9F6). A "
        "small group of simple geometric shapes (circles, half-circles, rectangles, "
        "triangles) clustered in one corner or along one edge, in charcoal, "
        "mid-grey, dusty blue and soft amber. Low saturation."),
    "omarchy-beacon-redgreen-light-theme": (
        "Minimal abstract desktop wallpaper. Solid warm off-white base (#FAF9F6). A "
        "small group of simple geometric shapes clustered in one corner or along "
        "one edge, using only blue, sky blue, navy, orange and amber. No green, no "
        "red, no magenta anywhere."),
    "omarchy-beacon-blueyellow-light-theme": (
        "Minimal abstract desktop wallpaper. Solid warm off-white base (#FAF9F6). A "
        "small group of simple geometric shapes clustered in one corner or along "
        "one edge, using only vermilion, mid green, magenta, amber, cream and "
        "charcoal. No blue, no teal, no cyan anywhere."),
}

BG_README = """# Backgrounds for `{name}`

The Omarchy shell renders the background itself in Quattro; cycle images with
**Super + Ctrl + Space**. Users can add their own without touching this theme by
putting files in `~/.config/omarchy/backgrounds/{name}/`.

## Shipped wallpapers

{listing}

All are flat geometric compositions with the central third of the frame left
empty, checked against the rules below before shipping.

## What makes a wallpaper accessible

A wallpaper is not decoration here, it is the substrate the lock screen, the bar
and any desktop text sit on. Three rules:

1. **Keep the centre clear.** The lock screen draws in the middle of the frame.
   This is a {mode} theme, so the central third must stay {envelope}. Shapes
   belong at the edges and corners.
2. **No high-frequency detail.** Fine stripes, dot grids, halftones and dense
   noise cause visual stress and can trigger symptoms in photosensitive users.
   They also shimmer through the bar's translucency. Flat colour, hard edges.
3. **Match the palette's hue policy.** {hue_note}

## Adding another

Generation prompt matched to this variant:

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

Name new files `{stem}-NN.jpg`, continuing the sequence.

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


def write(path, text):
    with open(path, "w") as f:
        f.write(text)


def main():
    for name, spec in VARIANTS.items():
        p = build(spec)
        d = os.path.join(OUT, name)
        acc, fg, bfg = p["accent"], p["foreground"], p["bright_foreground"]
        muted, inact = p["muted"], p["inactive_border"]

        # Controls. Focus is 3px on every side rather than a thin ring, and every
        # border alpha is 1.0 -- translucency silently eats the 3:1 that
        # WCAG 1.4.11 requires of a control boundary.
        write(os.path.join(d, "shell.controls.toml"), HEADER + f"""normal-color        = "{fg}"
normal-border       = "{muted}"
normal-border-width = 1
normal-border-alpha = 1.0

hover-cursor-color        = "{bfg}"
hover-cursor-border       = "{acc}"
hover-cursor-border-width = 2
hover-cursor-border-alpha = 1.0

focus-border       = "{acc}"
focus-border-width = 3
focus-border-alpha = 1.0
""")

        # Notifications. The heavy left edge is a non-colour cue, so urgency is
        # not carried by hue alone (WCAG 1.4.1).
        write(os.path.join(d, "shell.notifications.toml"), HEADER + f"""border            = "{acc}"
border-alpha      = 1.0
border-width      = 2
border-width-left = 6
""")

        # Menu. Selection is marked by a 4px left edge as well as a fill, again
        # so the cue survives without colour discrimination.
        write(os.path.join(d, "shell.menu.toml"), HEADER + f"""selected-border       = "{acc}"
selected-border-width = "1 1 1 4"
border                = "{inact}"
border-width          = 2
border-alpha          = 1.0
""")

        write(os.path.join(d, "shell.lock.toml"), HEADER + f"""text        = "{bfg}"
placeholder = "{muted}"
border      = "{acc}"
""")

        bg = os.path.join(d, "backgrounds")
        images = sorted(f for f in os.listdir(bg)
                        if f.lower().endswith((".png", ".jpg", ".jpeg", ".webp")))
        listing = "\n".join(f"- `{f}`" for f in images) or "None yet."
        write(os.path.join(bg, "README.md"), BG_README.format(
            name=name, mode=spec["mode"], listing=listing,
            stem=name.replace("omarchy-", "").replace("-theme", ""),
            envelope=("empty and dark, with nothing above 20% luminance"
                      if spec["mode"] == "dark" else
                      "empty and light, with nothing below 50% luminance"),
            hue_note=HUE_NOTE[name],
            prompt=BG_PROMPTS[name] + " " + CENTRE[spec["mode"]] + " " + STYLE))

        print(f"assets written: {name}")


if __name__ == "__main__":
    main()
