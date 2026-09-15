# Backgrounds for `omarchy-beacon-light-theme`

The Omarchy shell renders the background itself in Quattro; cycle images with
**Super + Ctrl + Space**. Users can add their own without touching this theme by
putting files in `~/.config/omarchy/backgrounds/omarchy-beacon-light-theme/`.

## Shipped wallpapers

- `beacon-light-01-misty-dunes.jpg` — Misty dunes
- `beacon-light-02-birch-grove-snow.jpg` — Birch grove snow
- `beacon-light-03-shoreline-stones.jpg` — Shoreline stones
- `beacon-light-04-distant-range.jpg` — Distant range

All are flat papercut nature scenes with the central third of the frame left
as open sky, checked against the rules below before shipping.

## What makes a wallpaper accessible

A wallpaper is not decoration here, it is the substrate the lock screen, the bar
and any desktop text sit on. Three rules:

1. **Keep the centre clear.** The lock screen draws in the middle of the frame.
   This is a light theme, so the central third must stay empty and light, with nothing below 50% luminance.
   Landforms belong low in the frame or in the corners, moons and suns in a
   corner.
2. **No high-frequency detail.** Fine stripes, dot grids, halftones and dense
   noise cause visual stress and can trigger symptoms in photosensitive users.
   They also shimmer through the bar's translucency. That rules out realistic
   grass, leaves, star fields and water, which is why these are papercut.
3. **Match the palette's hue policy.** Any hue is fine, but keep saturation low so it does not compete with the palette's accent colours.

## Adding another

Generation prompt matched to this variant. Swap the scene for any other in
this family's setting, but keep the sky wording and the style sentences:

```
Morning landscape. Solid warm off-white sky (#FAF9F6). Layered sand-beige and pale warm-grey dune shapes confined to the bottom fifth of the frame. A small soft charcoal sun disc in the top-right corner. Low saturation throughout. Flat papercut illustration style: large simple shapes, solid matte colour, hard crisp edges, no gradients, no glow, no halo, no drop shadows, no texture or grain. No fine detail: no individual grass blades, no leaf veins, no water ripples, no foliage texture. No text, no people. Keep the central third of the frame, horizontally and vertically, completely empty flat pale sky: nothing there below 50% luminance and no shape crossing into it, not even a pale one. 16:9, as large as the generator allows.
```

Then audit it:

```bash
python3 tools/check-wallpaper.py --mode light path/to/image.jpg
```

Trust the model divergence figure (under 4 is clean) and the "area that fights
overlaid text" percentage. The worst-block contrast line scans the whole frame,
not just the centre, so it fails images whose shapes sit harmlessly in a corner.
Check the central third by eye.

Name new files `beacon-light-NN-scene-name.jpg`, continuing the sequence.

## Export

- 16:9 at your panel's native resolution.
- Also export **1200x675 WebP under 100 KB** if you submit this theme to the
  Omarchy theme gallery, which is the screenshot spec.
