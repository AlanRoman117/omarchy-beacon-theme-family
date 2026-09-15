# To-do

## Nature wallpapers (replaces the Bauhaus set)

The palettes stay as they are. The current geometric wallpapers are being
replaced with nature scenes, one landscape idea per family:

| Family | Setting | Why it fits |
|---|---|---|
| Beacon Dark | Night: mountains, forest, a lighthouse on a headland | Full hue range, kept quiet |
| Beacon Light | Morning: dunes, snow, shoreline | Ink on paper, like the palette |
| Red-Green | Ocean and desert | Blue and orange stay vivid for red-green colour blindness |
| Blue-Yellow | Forest, flowers, volcano | Greens and warm reds only, so no blue sky |

### Why flat papercut, not photos

Realistic nature brings grass, leaves, star fields and water ripples. That is
the fine repeating detail that causes visual stress and shimmers through the
bar. A landscape also wants a horizon across the middle, where the lock screen
draws. So these prompts use a flat papercut style, with landforms kept low or in
the corners and open sky across the centre. The audit rules stay unchanged.
Allowing photos would mean rethinking the visual-stress rule first.

### Steps

- [x] Generate all 24 images. For each one, paste the scene prompt and then the
      style block for its mode.
- [x] Keep the `01`–`24` numbering in the filenames, e.g.
      `09-beacon-rg-dark-desert-blue-hour.jpg`, and put them in one folder.
- [x] Upscale. Done with Upscayl `digital-art-4x`, resized to 2560x1440 at
      JPEG quality 90, and re-audited: all 24 still pass.
- [x] Touch up the faint smudge-like upscaling artefacts, then re-audit. Done:
      all 24 cleaned in GIMP and re-audited, and all pass. Optional: a few
      faint lighter blotches remain in the upper dune of Red-Green Dark 01,
      visible only at 1:1.
- [x] Ask Claude to audit them: centre third, hue policy, CVD model divergence,
      and a look at every image. Check the dark greens and plums in 17–20 by
      eye, because they pass the 20% luminance number even when they sit in the
      centre.
- [x] Once they pass, replace the Bauhaus images in `themes/*/backgrounds/`.
- [x] Update `BG_PROMPTS` and `STYLE` in `tools/assets.py` to the nature
      prompts, re-run it, and update the "Current set" notes in `CLAUDE.md` and
      the Wallpapers section of `README.md`.

### First batch audit (2026-09-14)

**Resolved:** 09–12 were regenerated and pass (model divergence 0.70–2.44,
no glow). All 24 now ship in `themes/*/backgrounds/`.

20 of 24 pass: every image has an empty centre third and no forbidden hue.
**09–12 (Red-Green Dark) need regenerating.**

- **Model divergence 4.3–6.6** (limit 4). The generator read "deep navy" over
  the hex and painted saturated navy skies (`#0A285A`–`#102D69`). That sky
  colour alone scores up to 7.17, while the requested `#10141A` scores 0.34.
  The orange shapes are not the problem.
- **12 also has a glow** on the rising sun, a soft orange halo along the horizon.

- [x] Regenerate 09–12 with the prompts below, which drop the word "navy" from
      the sky and forbid a halo. Add the dark style block as before.

```
09 Desert at night. Solid very dark desaturated blue-black sky, almost black (#10141A); not navy, not royal blue. Amber and burnt-orange dune silhouettes confined to the bottom fifth of the frame. A small pale orange moon in the top-left corner. Only blue-black, orange and amber. No green, no red, no magenta anywhere.
```

```
10 Ocean moonrise. Solid very dark desaturated blue-black sky, almost black (#10141A); not navy, not royal blue. A flat sea in two dark slate-blue layers along the bottom fifth. A small amber moon in the top-right corner, with a short flat amber reflection directly below it, kept in the bottom-right of the sea. Only blue-black, dark slate blue, orange and amber. No green, no red, no magenta anywhere.
```

```
11 Canyon walls. Solid very dark desaturated blue-black sky, almost black (#10141A); not navy, not royal blue. Tall, simple burnt-orange and amber rock walls rising along the left and right edges of the frame only, leaving open sky between them. Only blue-black, orange and amber. No green, no red, no magenta anywhere.
```

```
12 Polar night. Solid very dark desaturated blue-black sky, almost black (#10141A); not navy, not royal blue. Large simple iceberg shapes in sky blue and mid blue in the bottom-left corner, on a flat dark slate-blue sea along the bottom edge. A low amber sun half above the horizon in the bottom-right corner, drawn as a hard-edged flat disc with no glow, no halo and no light along the horizon. Only blue-black, sky blue, mid blue, orange and amber. No green, no red, no magenta anywhere.
```

Advisory, keep or regenerate as you prefer: 04 (thin grass blades), 06 (repeated
bark dashes), 21 (dense small flowers) and 24 (thin zigzag stripes) carry more
fine detail than the prompts asked for. All of it sits at the frame edges. 24 is
the closest to a repeating-stripe pattern.

### Style block, dark themes (01–04, 09–12, 17–20)

```
Flat papercut illustration style: large simple shapes, solid matte colour, hard crisp edges, no gradients, no glow, no drop shadows, no texture or grain. No fine detail: no star fields, no individual grass blades, no leaf veins, no water ripples, no foliage texture. No text, no people. Keep the central third of the frame, horizontally and vertically, completely empty flat sky: nothing there above 20% luminance and no shape crossing into it, not even a dark one. 16:9, as large as the generator allows.
```

### Style block, light themes (05–08, 13–16, 21–24)

```
Flat papercut illustration style: large simple shapes, solid matte colour, hard crisp edges, no gradients, no glow, no drop shadows, no texture or grain. No fine detail: no individual grass blades, no leaf veins, no water ripples, no foliage texture. No text, no people. Keep the central third of the frame, horizontally and vertically, completely empty flat pale sky: nothing there below 50% luminance and no shape crossing into it, not even a pale one. 16:9, as large as the generator allows.
```

### Beacon Dark: night (any hue, low saturation)

```
01 Alpine lake at night. Solid near-black blue-charcoal sky (#10141A). Three layers of muted slate and dusty blue mountain silhouettes confined to the bottom fifth of the frame, with a flat still lake below them. A small pale cream full moon in the top-left corner. Low saturation throughout.
```

```
02 Pine ridge at night. Solid near-black blue-charcoal sky (#10141A). A treeline of large simple conifer silhouettes in muted sage and slate, rising only along the left edge and bottom edge of the frame. A thin pale cream crescent moon in the top-right corner. Low saturation throughout.
```

```
03 Headland with a lighthouse. Solid near-black blue-charcoal sky (#10141A). A dark slate rocky headland rising from the bottom-right corner, with a small cream lighthouse on its tip and a single flat soft-amber lamp. Calm flat dark sea along the bottom fifth. Low saturation throughout.
```

```
04 Night meadow. Solid near-black blue-charcoal sky (#10141A). A few large, simple seed-head and tall-grass silhouettes in dusty lavender, ochre and slate, growing up from the bottom-left corner and along the bottom edge only. Low saturation throughout.
```

### Beacon Light: morning (any hue, low saturation)

```
05 Misty dunes. Solid warm off-white sky (#FAF9F6). Layered sand-beige and pale warm-grey dune shapes confined to the bottom fifth of the frame. A small soft charcoal sun disc in the top-right corner. Low saturation throughout.
```

```
06 Birch grove in snow. Solid warm off-white background (#FAF9F6). A few tall birch trunks in pale grey with bold charcoal bands, standing only along the left and right edges of the frame. A low snowbank in pale warm grey along the bottom edge. Low saturation throughout.
```

```
07 Shoreline stones. Solid warm off-white background (#FAF9F6). A cluster of large smooth pebbles and one simple shell, in charcoal, sand, dusty blue and soft amber, gathered in the bottom-right corner only. Low saturation throughout.
```

```
08 Distant range. Solid warm off-white sky (#FAF9F6). A layered mountain range in pale blue-grey and warm grey, confined to the bottom fifth of the frame, darkest layer nearest the bottom edge. Two small charcoal birds in flight in the top-left corner. Low saturation throughout.
```

### Beacon Red-Green: ocean and desert (blue, sky blue, navy, orange, amber only)

```
09 Desert at blue hour. Solid deep navy sky (#10141A), not pure black. Amber and burnt-orange dune silhouettes confined to the bottom fifth of the frame. A small pale orange moon in the top-left corner. Only blue, navy, orange and amber. No green, no red, no magenta anywhere.
```

```
10 Ocean moonrise. Solid deep navy sky (#10141A), not pure black. Flat layered navy and dark blue sea along the bottom fifth. A small amber moon in the top-right corner, with a short flat amber reflection kept in the bottom-right of the sea. Only blue, navy, orange and amber. No green, no red, no magenta anywhere.
```

```
11 Canyon walls. Solid deep navy sky (#10141A), not pure black. Tall, simple burnt-orange and amber rock walls rising along the left and right edges of the frame only, leaving open sky between them. Only blue, navy, orange and amber. No green, no red, no magenta anywhere.
```

```
12 Polar night. Solid deep navy sky (#10141A), not pure black. Large simple iceberg shapes in sky blue and mid blue in the bottom-left corner, on a flat navy sea along the bottom edge. A low amber sun just rising in the bottom-right corner. Only blue, navy, orange and amber. No green, no red, no magenta anywhere.
```

```
13 Sandstone mesas. Solid pale sky blue background, very light. Flat amber and burnt-orange mesa silhouettes confined to the bottom fifth of the frame, with navy shadows on their faces. Only blue, sky blue, navy, orange and amber. No green, no red, no magenta anywhere.
```

```
14 Beach morning. Solid warm off-white sky (#FAF9F6). A flat sky-blue and mid-blue sea band and an amber sand strip, both confined to the bottom fifth. A starfish in orange and a shell in navy in the bottom-right corner. Only blue, sky blue, navy, orange and amber. No green, no red, no magenta anywhere.
```

```
15 Glacier and sun. Solid warm off-white sky (#FAF9F6). Large simple glacier and ice shapes in pale blue, sky blue and navy rising from the bottom-left corner. An apricot-orange sun disc in the top-right corner. Only blue, sky blue, navy, orange and amber. No green, no red, no magenta anywhere.
```

```
16 Falling leaves. Solid warm off-white background (#FAF9F6). Five large, simple sycamore leaves in amber and burnt orange, with flat navy stems, scattered along the edges and corners of the frame. No leaf veins. Only blue, navy, orange and amber. No green, no red, no magenta anywhere.
```

### Beacon Blue-Yellow: forest, flowers, fire (vermilion, green, magenta, amber, cream only)

```
17 Rainforest canopy. Solid near-black warm plum sky (#10141A). Large, simple deep-green monstera and palm leaves entering from the top-left and bottom-right corners only. One small amber moon in the top-right corner. Only vermilion, green, magenta, amber and cream. No blue, no teal, no cyan anywhere.
```

```
18 Night garden. Solid near-black warm charcoal background (#10141A). Three large, simple flower heads in magenta, vermilion and amber, on deep-green stems, rising from the bottom edge in the bottom-left quarter only. Only vermilion, green, magenta, amber and cream. No blue, no teal, no cyan anywhere.
```

```
19 Volcano. Solid near-black warm charcoal sky (#10141A). A simple charcoal volcanic cone in the bottom-right corner, with a flat vermilion lava flow running along the bottom edge. A small cream moon in the top-left corner. No glow. Only vermilion, green, magenta, amber and cream. No blue, no teal, no cyan anywhere.
```

```
20 Forest at dusk. Solid near-black warm plum sky (#10141A). Deep-green conifer silhouettes confined to the bottom fifth of the frame. A thin amber crescent moon in the top-left corner. Only vermilion, green, magenta, amber and cream. No blue, no teal, no cyan anywhere.
```

```
21 Wildflower meadow. Solid warm cream sky (#FAF9F6). Large, simple poppies in vermilion and cosmos in magenta, on mid-green stems, confined to the bottom fifth of the frame. Only vermilion, green, magenta, amber and cream. No blue, no teal, no cyan anywhere.
```

```
22 Tropical leaves. Solid warm cream background (#FAF9F6). Large, simple monstera and banana leaves in mid green and deep green, entering from the top-right and bottom-left corners only. Only vermilion, green, magenta, amber and cream. No blue, no teal, no cyan anywhere.
```

```
23 Citrus branch. Solid warm cream background (#FAF9F6). A single branch with mid-green leaves and three amber citrus fruits, entering from the top-left corner only. Only vermilion, green, magenta, amber and cream. No blue, no teal, no cyan anywhere.
```

```
24 Terraced hills at sunrise. Solid warm cream sky (#FAF9F6). Layered green terraced hills in sage, mid green and deep green, confined to the bottom fifth of the frame. A vermilion sun disc in the top-right corner. Only vermilion, green, magenta, amber and cream. No blue, no teal, no cyan anywhere.
```

## VS Code extension

Goal: no more **Developer: Reload Window** after switching Omarchy themes.
`tools/vscode_extension.py` builds all six themes as one extension with their
own names, and `tools/omarchy-hooks/beacon-vscode.sh` switches VS Code to the
matching one after Omarchy's own VS Code step.

- [x] Build the extension (`vscode-extension/`, placeholder publisher
      `beacon-local`) and the hook. Hook logic tested against a fake home: it
      switches only for Beacon themes with the extension installed, and leaves
      other themes, hand-picked themes and skip toggles alone.
- [x] Package the `.vsix` (`npx @vscode/vsce package`), install it, install the
      hook, and confirm live switching while watching VS Code. **Passed
      2026-09-14:** Beacon-to-Beacon switches apply live with no reload and no
      flash; Osaka Jade still gets Ocean Green; uninstalling the extension
      falls back to "Omarchy".
- [ ] When the extension is published: update the reload notes in the
      per-theme READMEs (`tools/theme_readmes.py`) and the root README to say
      "install the extension and the hook". Doing it before publishing would
      point users at an extension they cannot get yet.

### Publishing, only after validation

- [ ] Choose the permanent publisher ID (AlanRoman117 matches the GitHub remote).
- [ ] VS Code Marketplace: Microsoft account, Azure DevOps organisation, a
      Personal Access Token with **Marketplace: Manage** scope for all
      organisations, create the publisher at
      marketplace.visualstudio.com/manage, then `npx @vscode/vsce publish`.
- [ ] Open VSX (VSCodium and Cursor): Eclipse account linked to GitHub, sign
      the publisher agreement, create a namespace, get a token, then
      `npx ovsx publish`.
- [ ] Make the repo public first. vsce rewrites relative README links and
      images to GitHub, and rejects SVG images.
- [ ] Decide where users get the hook: inside each theme repo (on disk after
      `omarchy theme install`, but a script in a colour-only theme) or the
      family repo with a download command.
- [ ] Bump `VERSION` in `tools/vscode_extension.py` whenever a palette or the VS
      Code mapping changes, and add a publish script next to `publish.sh`.

## Ideas from OldJobobo's Aonagi theme (later, optional)

Done: every app theme Omarchy generates is now verified and patched where it
failed (`tools/apps.py`, `APPS-REPORT.md`). Still open, in rough order of value:

- [ ] `icons.theme` per variant. All 22 stock themes ship one; Beacon falls back
      to `Yaru-blue`. Pick a Yaru colour per variant (installed: blue, magenta,
      olive, prussiangreen, purple, red, sage, wartybrown, yellow).
- [ ] Complete `shell.*` sections, including `[bar]` and `[hyprland]` borders,
      which Aonagi styles through `shell.toml`. Overlaps open item 1 in
      CLAUDE.md.
- [ ] Showcase assets: a real desktop screenshot for `preview.png` (Neovim,
      btop, VS Code), a palette sheet, a wallpaper contact sheet in the README,
      and `.omarchy-theme.yml` gallery metadata.
- [ ] Extra manually installed app themes (Zed, Zellij, Base24), each with its
      own contrast checks.

Not possible for git-installed themes: `hyprland.lua` (animations, gaps),
`neovim.lua`, `gum_env.lua` and terminal configs. Omarchy drops them on install.

## Other open items

Also tracked in `CLAUDE.md`:

- [ ] Emit full `shell.*.toml` sections from the palette in `tools/assets.py`
      (overrides currently drop the template keys they do not list), and set
      `[lock] background-alpha = 1.0`.
- [ ] Make `tools/check-wallpaper.py` region-aware: gate on the centre, report
      the rest as advisory.
- [ ] Replace the `YOURNAME` GitHub owner in `README.md`, `publish.sh` and
      `tools/theme_readmes.py`. The git remote points at `AlanRoman117`.
- [ ] Before going public: one `omarchy theme install` per theme from GitHub.
