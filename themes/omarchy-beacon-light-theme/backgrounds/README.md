# Backgrounds for `omarchy-beacon-light-theme`

The Omarchy shell renders the background itself in Quattro; cycle images with
**Super + Ctrl + Space**. Users can add their own without touching this theme by
putting files in `~/.config/omarchy/backgrounds/omarchy-beacon-light-theme/`.

## Shipped wallpapers

- `beacon-light-01.jpg`
- `beacon-light-02.jpg`
- `beacon-light-03.jpg`
- `beacon-light-04.jpg`

All are flat geometric compositions with the central third of the frame left
empty, checked against the rules below before shipping.

## What makes a wallpaper accessible

A wallpaper is not decoration here, it is the substrate the lock screen, the bar
and any desktop text sit on. Three rules:

1. **Keep the centre clear.** The lock screen draws in the middle of the frame.
   This is a light theme, so the central third must stay empty and light, with nothing below 50% luminance. Shapes
   belong at the edges and corners.
2. **No high-frequency detail.** Fine stripes, dot grids, halftones and dense
   noise cause visual stress and can trigger symptoms in photosensitive users.
   They also shimmer through the bar's translucency. Flat colour, hard edges.
3. **Match the palette's hue policy.** Any hue is fine, but keep saturation low so it does not compete with the palette's accent colours.

## Adding another

Generation prompt matched to this variant:

```
Minimal abstract desktop wallpaper. Solid warm off-white base (#FAF9F6). A small group of simple geometric shapes (circles, half-circles, rectangles, triangles) clustered in one corner or along one edge, in charcoal, mid-grey, dusty blue and soft amber. Low saturation. Keep the central third of the frame, horizontally and vertically, completely empty background: nothing there below 50% luminance, and no shape crossing into it, even a pale one. Flat matte colour, hard crisp edges, no gradients, no vignette, no glow, no drop shadows, no film or paper grain, no text or lettering, no logos, no dot grids, halftones or fine repeating patterns. 16:9, as large as the generator allows.
```

Then audit it:

```bash
python3 tools/check-wallpaper.py --mode light path/to/image.jpg
```

Trust the model divergence figure (under 4 is clean) and the "area that fights
overlaid text" percentage. The worst-block contrast line scans the whole frame,
not just the centre, so it fails images whose shapes sit harmlessly in a corner.
Check the central third by eye.

Name new files `beacon-light-NN.jpg`, continuing the sequence.

## Export

- 16:9 at your panel's native resolution.
- Also export **1200x675 WebP under 100 KB** if you submit this theme to the
  Omarchy theme gallery, which is the screenshot spec.
