# Beacon Blue-Yellow Light

Light theme for Omarchy 4 Quattro, designed for tritanopia. Blue is separated from green and yellow from magenta; the red-green axis is left intact.

Part of the [Beacon theme family](https://github.com/YOURNAME/omarchy-beacon-theme-family), which explains the design method,
ships the verification tooling, and contains the other five variants.

![preview](preview.png)

## Install

```bash
omarchy theme install YOURNAME/omarchy-beacon-blueyellow-light-theme
omarchy theme set beacon-blueyellow-light
```

## Who this is for

Blue and green, or yellow and pink, are hard for you to tell apart. This is rare, around 0.01% of people, and unlike red-green deficiency it is not sex-linked.

Not sure? The family README has a short decision guide. Short version: if you
have never had trouble telling colours apart, use plain **Beacon Light**.

## Verified numbers

Background `#FAF9F6`, mode `light`.

| Role | Hex | Contrast vs background | APCA Lc |
|---|---|---|---|
| foreground | `#2B2B28` | 13.49:1 | +97 |
| bright_foreground | `#0F0F0E` | 18.22:1 | +102 |
| dark_foreground | `#4E4E49` | 7.95:1 | +85 |
| muted / comments / color8 | `#4B575E` | 7.06:1 | +82 |
| accent | `#6F000D` | 11.86:1 | +93 |
| orange (not an ANSI slot) | `#4D2100` | 13.01:1 | +96 |

| ANSI | Hex | Contrast vs background |
|---|---|---|
| red | `#6F000D` | 11.86:1 |
| green | `#003608` | 13.03:1 |
| yellow | `#724F00` | 7.04:1 |
| blue | `#003880` | 10.62:1 |
| magenta | `#7B1956` | 9.43:1 |
| cyan | `#005555` | 8.21:1 |

- **Lowest contrast of any colour in the palette: 7.04:1.** The WCAG AAA
  threshold for body text is 7:1. Nothing here is below it, including comment
  text and the bright ANSI colours.
- Selected text on the selection band: 7.16:1
- Active window border against the desktop: 11.86:1 (WCAG 1.4.11 asks 3:1)
- Inactive window border against the desktop: 3.50:1

Reproduce all of it with `tools/verify.py` in the family repo.

## Colour vision simulation

Perceptual separation between the six chromatic slots, under the Machado,
Oliveira and Fernandes (2009) matrices at full severity. The number is the
Oklab distance of the closest pair, so higher is better and the pair named is
the palette's weakest link under that vision type.

| Vision | Closest pair | Distance |
|---|---|---|
| normal | red / magenta | 0.109 |
| protan | red / green | 0.049 |
| deutan | magenta / cyan | 0.004 |
| tritan **(tuned for this)** | blue / cyan | 0.048 |

`cvd-proof.png` in this repo shows the palette rendered four times: normal
vision plus all three simulations. Note that it collapses under protanopia and deuteranopia by design. That is the trade being made, not a defect.

## What is different about this variant

Blue is pulled away from green, and yellow away from magenta, since those are
the pairs that collapse on the tritan axis.

Red and green are **not** separated here, because they do not need to be.
Tritanopia leaves the red-green axis intact, so this palette spends its
lightness budget on the blue-yellow problem instead.

That has a consequence worth stating plainly: **this theme is not a
general-purpose colourblind theme.** If you have red-green deficiency, this
palette will be actively worse for you than the default. Use the red-green
variant instead.

## VS Code

Omarchy normally themes VS Code from a generic template, which assumes a palette
shaped like the stock themes and leaves parts of the interface unreadable with
this one. This theme ships its own `vscode-theme.json` instead. Omarchy applies
it automatically as the theme called "Omarchy" whenever this theme is active.

**After switching to this theme, reload VS Code once:** open the command
palette and run **Developer: Reload Window**, or restart VS Code. Omarchy gives
every theme without a marketplace theme the same VS Code name, "Omarchy", and
only swaps the colour file behind it. VS Code's theme setting therefore does
not change, so VS Code keeps the colours it already loaded until the window
reloads. The same happens with any Omarchy theme installed from git. Switching
to a stock theme such as Osaka Jade updates live, because its VS Code theme
has a different name.

- 71 text and indicator pairs checked. Every piece of resting text,
  including syntax colours, comments, line numbers and side bar labels, is at
  least **7.04:1**.
- Borders, focus rings, the cursor and gutter markers are at least
  **3.33:1** (WCAG 1.4.11 asks 3:1).
- **Highlighted text drops to AA.** Selection, find matches and diff
  highlights have to move toward the text colour to be visible at all. Each is
  solved so every syntax colour still reads at **4.66:1** or better on top
  of it, which leaves the highlight itself at about 1.5:1 against the
  editor. This is the same trade-off as the selection band, applied to more
  kinds of highlight.
- Faded "unused" code keeps full opacity and gets a dotted underline instead,
  because fading drops it below AAA.

The full table is in `CONTRAST-REPORT.md` in the family repo.

## What ships here

| File | Purpose |
|---|---|
| `colors.toml` | The palette. Omarchy generates every app config from this. |
| `shell.controls.toml` | Focus rings at 3px, all border alphas pinned to 1.0. |
| `shell.notifications.toml` | 6px left edge as a non-colour urgency cue. |
| `shell.menu.toml` | Selected rows marked by an edge, not only a fill. |
| `shell.lock.toml` | Lock screen text and placeholder contrast. |
| `light.mode` | Pairs the theme with light mode across GTK apps. |
| `preview.png` | Theme-switcher preview, 1200x675. |
| `cvd-proof.png` | Simulation proof sheet. |
| `vscode-theme.json` | VS Code, VSCodium and Cursor theme, generated and verified with the palette. |
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
general    { border_size = 3 }     # focus visibility, WCAG 2.4.13
animations { enabled = false }     # reduced motion, WCAG 2.3.3
```

## Scope

This theme improves things for people with low vision and colour vision
deficiency. It does **not** make Omarchy usable with a screen reader. That is a
compositor and toolkit problem, not a palette problem. See the family README.

## Licence

MIT, to match Omarchy.
