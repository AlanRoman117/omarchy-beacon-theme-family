"""Write a README.md into each theme directory, populated with that theme's
actual verified numbers so no per-repo README can drift from the palette."""
import os, itertools
from colorlib import contrast, apca_lc, simulate, oklab_distance
from verify import VARIANTS, build, OUT, SLOTS

FAMILY = "https://github.com/YOURNAME/omarchy-beacon-theme-family"

META = {
    "omarchy-beacon-dark-theme": dict(
        title="Beacon Dark", mode="dark", axis=None,
        tagline="High-contrast dark theme for Omarchy 4 Quattro. Every colour "
                "verified at WCAG AAA 7:1, including comment text and all "
                "sixteen ANSI slots.",
        who="You want a dark theme that is genuinely readable and you do not "
            "have a colour vision deficiency.",
    ),
    "omarchy-beacon-light-theme": dict(
        title="Beacon Light", mode="light", axis=None,
        tagline="High-contrast light theme for Omarchy 4 Quattro. Every colour "
                "verified at WCAG AAA 7:1, including comment text and all "
                "sixteen ANSI slots.",
        who="You want a light theme that is genuinely readable and you do not "
            "have a colour vision deficiency.",
    ),
    "omarchy-beacon-redgreen-dark-theme": dict(
        title="Beacon Red-Green Dark", mode="dark", axis="redgreen",
        tagline="Dark theme for Omarchy 4 Quattro, designed for protanopia and "
                "deuteranopia. Red shifts to vermilion and green to bluish-green, "
                "then the two are pulled apart on the lightness axis.",
        who="Red and green are hard for you to tell apart. This is the most "
            "common form of colour vision deficiency by a wide margin.",
    ),
    "omarchy-beacon-redgreen-light-theme": dict(
        title="Beacon Red-Green Light", mode="light", axis="redgreen",
        tagline="Light theme for Omarchy 4 Quattro, designed for protanopia and "
                "deuteranopia. Red shifts to vermilion and green to bluish-green, "
                "tuned for the protan worst case.",
        who="Red and green are hard for you to tell apart. This is the most "
            "common form of colour vision deficiency by a wide margin.",
    ),
    "omarchy-beacon-blueyellow-dark-theme": dict(
        title="Beacon Blue-Yellow Dark", mode="dark", axis="blueyellow",
        tagline="Dark theme for Omarchy 4 Quattro, designed for tritanopia. Blue "
                "is separated from green and yellow from magenta; the red-green "
                "axis is left intact.",
        who="Blue and green, or yellow and pink, are hard for you to tell apart. "
            "This is rare, around 0.01% of people, and unlike red-green "
            "deficiency it is not sex-linked.",
    ),
    "omarchy-beacon-blueyellow-light-theme": dict(
        title="Beacon Blue-Yellow Light", mode="light", axis="blueyellow",
        tagline="Light theme for Omarchy 4 Quattro, designed for tritanopia. Blue "
                "is separated from green and yellow from magenta; the red-green "
                "axis is left intact.",
        who="Blue and green, or yellow and pink, are hard for you to tell apart. "
            "This is rare, around 0.01% of people, and unlike red-green "
            "deficiency it is not sex-linked.",
    ),
}

AXIS_NOTE = {
    "redgreen": """## What is different about this variant

Red is a vermilion (hue 38 rather than 25) and green is a bluish-green (hue 172
rather than 150). Those two survive the protan and deutan confusion axes where
crimson and grass green do not.

More importantly, red and green are placed at opposite ends of the contrast
ladder. Lightness is the only channel a dichromat keeps, so a large lightness
gap is what actually makes a `git diff` readable, not the hue substitution on
its own.

The palette is tuned for the **protan** worst case specifically. Protanopia
comes with reduced luminance sensitivity to red, so reds appear darker than
they do to a deuteranope and can approach black. Anything that works for protan
works for deutan; the reverse is not reliably true.""",
    "blueyellow": """## What is different about this variant

Blue is pulled away from green, and yellow away from magenta, since those are
the pairs that collapse on the tritan axis.

Red and green are **not** separated here, because they do not need to be.
Tritanopia leaves the red-green axis intact, so this palette spends its
lightness budget on the blue-yellow problem instead.

That has a consequence worth stating plainly: **this theme is not a
general-purpose colourblind theme.** If you have red-green deficiency, this
palette will be actively worse for you than the default. Use the red-green
variant instead.""",
}

TPL = """# {title}

{tagline}

Part of the [Beacon theme family]({family}), which explains the design method,
ships the verification tooling, and contains the other five variants.

![preview](preview.png)

## Install

```bash
omarchy theme install {family_owner}/{name}
omarchy theme set {short}
```

## Who this is for

{who}

Not sure? The family README has a short decision guide. Short version: if you
have never had trouble telling colours apart, use plain **Beacon {mode_title}**.

## Verified numbers

Background `{bg}`, mode `{mode}`.

| Role | Hex | Contrast vs background | APCA Lc |
|---|---|---|---|
{rows}

| ANSI | Hex | Contrast vs background |
|---|---|---|
{cols}

- **Lowest contrast of any colour in the palette: {worst}:1.** The WCAG AAA
  threshold for body text is 7:1. Nothing here is below it, including comment
  text and the bright ANSI colours.
- Selected text on the selection band: {sel}:1
- Active window border against the desktop: {border}:1 (WCAG 1.4.11 asks 3:1)
- Inactive window border against the desktop: {inactive}:1

Reproduce all of it with `tools/verify.py` in the family repo.

## Colour vision simulation

Perceptual separation between the six chromatic slots, under the Machado,
Oliveira and Fernandes (2009) matrices at full severity. The number is the
Oklab distance of the closest pair, so higher is better and the pair named is
the palette's weakest link under that vision type.

| Vision | Closest pair | Distance |
|---|---|---|
{sep}

`cvd-proof.png` in this repo shows the palette rendered four times: normal
vision plus all three simulations. {proof_note}

{axis_note}

## What ships here

| File | Purpose |
|---|---|
| `colors.toml` | The palette. Omarchy generates every app config from this. |
| `shell.controls.toml` | Focus rings at 3px, all border alphas pinned to 1.0. |
| `shell.notifications.toml` | 6px left edge as a non-colour urgency cue. |
| `shell.menu.toml` | Selected rows marked by an edge, not only a fill. |
| `shell.lock.toml` | Lock screen text and placeholder contrast. |{light_mode}
| `preview.png` | Theme-switcher preview, 1200x675. |
| `cvd-proof.png` | Simulation proof sheet. |
| `backgrounds/` | Wallpapers with a clear centre, plus a prompt for adding more. |

The `shell.*.toml` files are **section overrides**, not a replacement
`shell.toml`. Omarchy generates the full file from its own template and each of
these replaces one section. Shipping a whole hand-written `shell.toml` would
silently miss any key a future Omarchy release adds.

Border alphas are pinned to `1.0`. Translucency quietly eats the 3:1 that WCAG
1.4.11 requires of a control boundary, and a focus ring at 60% alpha is not a
focus ring that meets 2.4.13.

## Two things this theme cannot set for you

A theme installed from a git URL has its `hyprland.lua` stripped before staging,
so these have to live in `~/.config/hypr/hyprland.conf`:

```
general    {{ border_size = 3 }}     # focus visibility, WCAG 2.4.13
animations {{ enabled = false }}     # reduced motion, WCAG 2.3.3
```

## Scope

This theme improves things for people with low vision and colour vision
deficiency. It does **not** make Omarchy usable with a screen reader. That is a
compositor and toolkit problem, not a palette problem. See the family README.

## Licence

MIT, to match Omarchy.
"""


def main():
    for name, spec in VARIANTS.items():
        m = META[name]
        p = build(spec)
        bg = p["background"]

        rows = "\n".join(
            f"| {label} | `{p[k]}` | {contrast(p[k], bg):.2f}:1 | {apca_lc(p[k], bg):+.0f} |"
            for k, label in [("foreground", "foreground"),
                             ("bright_foreground", "bright_foreground"),
                             ("dark_foreground", "dark_foreground"),
                             ("muted", "muted / comments / color8"),
                             ("accent", "accent")])
        cols = "\n".join(
            f"| {s} | `{p['_normals'][s]}` | {contrast(p['_normals'][s], bg):.2f}:1 |"
            for s in SLOTS)

        sep_rows, sep_vals = [], {}
        for kind in ("normal", "protan", "deutan", "tritan"):
            best = None
            for a, b in itertools.combinations(SLOTS, 2):
                ca, cb = p["_normals"][a], p["_normals"][b]
                if kind != "normal":
                    ca, cb = simulate(ca, kind), simulate(cb, kind)
                d = oklab_distance(ca, cb)
                if best is None or d < best[0]:
                    best = (d, a, b)
            sep_vals[kind] = best[0]
            mark = " **(tuned for this)**" if kind in spec["optimise"] else ""
            sep_rows.append(f"| {kind}{mark} | {best[1]} / {best[2]} | {best[0]:.3f} |")

        if m["axis"] == "redgreen":
            proof = ("Compare it against the default Beacon "
                     f"{m['mode'].title()} proof sheet: under deuteranopia the "
                     "default collapses red and green into the same olive, and "
                     "this one does not.")
        elif m["axis"] == "blueyellow":
            proof = ("Note that it collapses under protanopia and deuteranopia "
                     "by design. That is the trade being made, not a defect.")
        else:
            proof = ("Under deuteranopia red and green converge here. That is "
                     "expected, and it is what the red-green variant exists to "
                     "fix.")

        short = name.replace("omarchy-", "").replace("-theme", "")
        text = TPL.format(
            title=m["title"], tagline=m["tagline"], who=m["who"],
            family=FAMILY, family_owner="YOURNAME", name=name, short=short,
            mode=m["mode"], mode_title=m["mode"].title(), bg=bg,
            rows=rows, cols=cols, sep="\n".join(sep_rows),
            worst=f"{min([contrast(p[k], bg) for k in ('foreground','light_foreground','bright_foreground','dark_foreground','muted','accent')] + [contrast(v, bg) for v in p['_normals'].values()] + [contrast(v, bg) for v in p['_brights'].values()]):.2f}",
            sel=f"{contrast(p['bright_foreground'], p['selection']):.2f}",
            border=f"{contrast(p['accent'], bg):.2f}",
            inactive=f"{contrast(p['inactive_border'], bg):.2f}",
            proof_note=proof,
            axis_note=AXIS_NOTE.get(m["axis"], ""),
            light_mode=("\n| `light.mode` | Pairs the theme with light mode across "
                        "GTK apps. |" if m["mode"] == "light" else ""))
        with open(os.path.join(OUT, name, "README.md"), "w") as f:
            f.write(text)
        print("README:", name)


if __name__ == "__main__":
    main()
