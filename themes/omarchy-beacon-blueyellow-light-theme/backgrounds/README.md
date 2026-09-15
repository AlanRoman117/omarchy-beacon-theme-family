# Backgrounds for `omarchy-beacon-blueyellow-light-theme`

The Omarchy shell renders the background itself in Quattro; cycle images with
**Super + Ctrl + Space**. Users can add their own without touching this theme by
putting files in `~/.config/omarchy/backgrounds/omarchy-beacon-blueyellow-light-theme/`.

## Shipped wallpapers

- `beacon-blueyellow-light-01-wildflower-meadow.jpg` — Wildflower meadow
- `beacon-blueyellow-light-02-tropical-leaves.jpg` — Tropical leaves
- `beacon-blueyellow-light-03-citrus-branch.jpg` — Citrus branch
- `beacon-blueyellow-light-04-terraced-hills-sunrise.jpg` — Terraced hills sunrise

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
3. **Match the palette's hue policy.** Vermilion, green, magenta, amber and cream only. No blue, teal or cyan, which collapse together under tritanopia.

## Adding another

Generation prompt matched to this variant. Swap the scene for any other in
this family's setting, but keep the sky wording and the style sentences:

```
Meadow, leaves or hills in daylight. Solid warm cream sky (#FAF9F6). Large, simple monstera and banana leaves in mid green and deep green, entering from the top-right and bottom-left corners only. Only vermilion, green, magenta, amber and cream. No blue, no teal, no cyan anywhere. Flat papercut illustration style: large simple shapes, solid matte colour, hard crisp edges, no gradients, no glow, no halo, no drop shadows, no texture or grain. No fine detail: no individual grass blades, no leaf veins, no water ripples, no foliage texture. No text, no people. Keep the central third of the frame, horizontally and vertically, completely empty flat pale sky: nothing there below 50% luminance and no shape crossing into it, not even a pale one. 16:9, as large as the generator allows.
```

Then audit it:

```bash
python3 tools/check-wallpaper.py --mode light path/to/image.jpg
```

Trust the model divergence figure (under 4 is clean) and the "area that fights
overlaid text" percentage. The worst-block contrast line scans the whole frame,
not just the centre, so it fails images whose shapes sit harmlessly in a corner.
Check the central third by eye.

Name new files `beacon-blueyellow-light-NN-scene-name.jpg`, continuing the sequence.

## Export

- 16:9 at your panel's native resolution.
- Also export **1200x675 WebP under 100 KB** if you submit this theme to the
  Omarchy theme gallery, which is the screenshot spec.
