# Verification report

Regenerate with `python3 tools/verify.py`.

## `omarchy-beacon-dark-theme`

Neutral high-contrast dark. The full hue range, tuned for normal colour vision. If red and green are hard to tell apart, use the protan-deutan variant instead; this one does not solve that.

Background `#10141A`, mode `dark`.

| Role | Hex | WCAG vs bg | Level | APCA Lc |
|---|---|---|---|---|
| foreground | `#D8DFE8` | 13.76:1 | AAA | -86 |
| light_foreground | `#EDF1F6` | 16.28:1 | AAA | -98 |
| bright_foreground | `#FFFFFF` | 18.47:1 | AAA | -107 |
| dark_foreground | `#A3AEBD` | 8.22:1 | AAA | -57 |
| muted / color8 | `#95A2A9` | 7.05:1 | AAA | -50 |
| accent | `#99C6FF` | 10.45:1 | AAA | -70 |
| red | `#FA7C75` | 7.22:1 | AAA | -52 |
| green | `#59C977` | 8.84:1 | AAA | -61 |
| yellow | `#FFDA70` | 13.65:1 | AAA | -86 |
| blue | `#99C6FF` | 10.45:1 | AAA | -70 |
| magenta | `#FFBDE8` | 12.05:1 | AAA | -78 |
| cyan | `#A8F6FF` | 15.21:1 | AAA | -93 |
| bright_red | `#FF9A92` | 9.05:1 | AAA | -62 |
| bright_green | `#59DD7F` | 10.62:1 | AAA | -71 |
| bright_yellow | `#FFE9AD` | 15.40:1 | AAA | -94 |
| bright_blue | `#B4D5FF` | 12.23:1 | AAA | -79 |
| bright_magenta | `#FFD2EE` | 13.81:1 | AAA | -86 |
| bright_cyan | `#C7F9FF` | 16.20:1 | AAA | -97 |

- Lowest contrast of any palette colour against the background: **7.05:1** (AAA threshold is 7:1)
- Selected text, `bright_foreground` on `selection`: **7.15:1**
- Selection band against background: 2.58:1
- Active window border against background: 10.45:1 (1.4.11 needs 3:1)
- Inactive window border against background: 3.50:1

Perceptual separation between the six chromatic slots under simulated colour vision deficiency (Machado 2009 at full severity, Oklab distance). Arrows mark the vision types this variant is tuned for.

| Vision | Weakest pair overall | Weakest priority pair |
|---|---|---|
| normal <- | blue/cyan 0.132 | green/yellow 0.207 |
| protan | blue/magenta 0.037 | green/yellow 0.099 |
| deutan | red/green 0.013 | red/green 0.013 |
| tritan | yellow/magenta 0.040 | green/cyan 0.173 |


## `omarchy-beacon-redgreen-dark-theme`

Red-green safe dark. Red shifts to vermilion and green to bluish-green, then the two are pulled apart by lightness for the protan worst case.

Background `#10141A`, mode `dark`.

| Role | Hex | WCAG vs bg | Level | APCA Lc |
|---|---|---|---|---|
| foreground | `#D8DFE8` | 13.76:1 | AAA | -86 |
| light_foreground | `#EDF1F6` | 16.28:1 | AAA | -98 |
| bright_foreground | `#FFFFFF` | 18.47:1 | AAA | -107 |
| dark_foreground | `#A3AEBD` | 8.22:1 | AAA | -57 |
| muted / color8 | `#95A2A9` | 7.05:1 | AAA | -50 |
| accent | `#9BC6FF` | 10.48:1 | AAA | -70 |
| red | `#F5825E` | 7.24:1 | AAA | -52 |
| green | `#8DFEDB` | 15.24:1 | AAA | -93 |
| yellow | `#FCCA39` | 12.00:1 | AAA | -78 |
| blue | `#9BC6FF` | 10.48:1 | AAA | -70 |
| magenta | `#F9D0FF` | 13.63:1 | AAA | -86 |
| cyan | `#53C1DA` | 8.80:1 | AAA | -61 |
| bright_red | `#FF9B7D` | 9.00:1 | AAA | -62 |
| bright_green | `#C5FFEB` | 16.60:1 | AAA | -99 |
| bright_yellow | `#FFDB80` | 13.80:1 | AAA | -86 |
| bright_blue | `#B5D5FF` | 12.25:1 | AAA | -79 |
| bright_magenta | `#FBDFFF` | 15.04:1 | AAA | -92 |
| bright_cyan | `#46D5F3` | 10.62:1 | AAA | -71 |

- Lowest contrast of any palette colour against the background: **7.05:1** (AAA threshold is 7:1)
- Selected text, `bright_foreground` on `selection`: **7.15:1**
- Selection band against background: 2.58:1
- Active window border against background: 10.48:1 (1.4.11 needs 3:1)
- Inactive window border against background: 3.50:1

Perceptual separation between the six chromatic slots under simulated colour vision deficiency (Machado 2009 at full severity, Oklab distance). Arrows mark the vision types this variant is tuned for.

| Vision | Weakest pair overall | Weakest priority pair |
|---|---|---|
| normal | blue/cyan 0.092 | green/cyan 0.183 |
| protan <- | blue/cyan 0.054 | green/cyan 0.182 |
| deutan <- | green/magenta 0.054 | red/yellow 0.143 |
| tritan | blue/cyan 0.068 | green/cyan 0.157 |


## `omarchy-beacon-blueyellow-dark-theme`

Blue-yellow safe dark. Red and green stay trustworthy here, so the work goes into separating blue from green and yellow from magenta.

Background `#10141A`, mode `dark`.

| Role | Hex | WCAG vs bg | Level | APCA Lc |
|---|---|---|---|---|
| foreground | `#D8DFE8` | 13.76:1 | AAA | -86 |
| light_foreground | `#EDF1F6` | 16.28:1 | AAA | -98 |
| bright_foreground | `#FFFFFF` | 18.47:1 | AAA | -107 |
| dark_foreground | `#A3AEBD` | 8.22:1 | AAA | -57 |
| muted / color8 | `#95A2A9` | 7.05:1 | AAA | -50 |
| accent | `#FF968F` | 8.80:1 | AAA | -61 |
| red | `#FF968F` | 8.80:1 | AAA | -61 |
| green | `#59B55F` | 7.21:1 | AAA | -51 |
| yellow | `#FFE7B4` | 15.25:1 | AAA | -93 |
| blue | `#9DC5FF` | 10.43:1 | AAA | -70 |
| magenta | `#FFBEDE` | 12.02:1 | AAA | -78 |
| cyan | `#75F0F0` | 13.61:1 | AAA | -86 |
| bright_red | `#FFB1A9` | 10.65:1 | AAA | -71 |
| bright_green | `#60CB67` | 9.00:1 | AAA | -62 |
| bright_yellow | `#FFECC4` | 15.87:1 | AAA | -96 |
| bright_blue | `#B7D4FF` | 12.20:1 | AAA | -78 |
| bright_magenta | `#FFD3E8` | 13.84:1 | AAA | -86 |
| bright_cyan | `#7FFEFF` | 15.41:1 | AAA | -94 |

- Lowest contrast of any palette colour against the background: **7.05:1** (AAA threshold is 7:1)
- Selected text, `bright_foreground` on `selection`: **7.15:1**
- Selection band against background: 2.58:1
- Active window border against background: 8.80:1 (1.4.11 needs 3:1)
- Inactive window border against background: 3.50:1

Perceptual separation between the six chromatic slots under simulated colour vision deficiency (Machado 2009 at full severity, Oklab distance). Arrows mark the vision types this variant is tuned for.

| Vision | Weakest pair overall | Weakest priority pair |
|---|---|---|
| normal | red/magenta 0.118 | red/yellow 0.190 |
| protan | blue/magenta 0.052 | red/green 0.068 |
| deutan | magenta/cyan 0.028 | red/green 0.094 |
| tritan <- | yellow/magenta 0.079 | green/cyan 0.192 |


## `omarchy-beacon-light-theme`

Neutral high-contrast light. The full hue range, tuned for normal colour vision. If red and green are hard to tell apart, use the protan-deutan variant instead; this one does not solve that.

Background `#FAF9F6`, mode `light`.

| Role | Hex | WCAG vs bg | Level | APCA Lc |
|---|---|---|---|---|
| foreground | `#2B2B28` | 13.49:1 | AAA | +97 |
| light_foreground | `#1C1C1A` | 16.21:1 | AAA | +100 |
| bright_foreground | `#0F0F0E` | 18.22:1 | AAA | +102 |
| dark_foreground | `#4E4E49` | 7.95:1 | AAA | +85 |
| muted / color8 | `#4B575E` | 7.06:1 | AAA | +82 |
| accent | `#003A77` | 10.66:1 | AAA | +92 |
| red | `#62000A` | 13.09:1 | AAA | +95 |
| green | `#003D18` | 11.87:1 | AAA | +94 |
| yellow | `#664500` | 8.26:1 | AAA | +86 |
| blue | `#003A77` | 10.66:1 | AAA | +92 |
| magenta | `#781A61` | 9.41:1 | AAA | +88 |
| cyan | `#005F6B` | 7.00:1 | AAA | +82 |
| bright_red | `#500006` | 14.84:1 | AAA | +98 |
| bright_green | `#003212` | 13.62:1 | AAA | +97 |
| bright_yellow | `#563900` | 10.07:1 | AAA | +91 |
| bright_blue | `#003064` | 12.41:1 | AAA | +95 |
| bright_magenta | `#6C0056` | 11.26:1 | AAA | +92 |
| bright_cyan | `#004F5A` | 8.80:1 | AAA | +87 |

- Lowest contrast of any palette colour against the background: **7.00:1** (AAA threshold is 7:1)
- Selected text, `bright_foreground` on `selection`: **7.16:1**
- Selection band against background: 2.55:1
- Active window border against background: 10.66:1 (1.4.11 needs 3:1)
- Inactive window border against background: 3.50:1

Perceptual separation between the six chromatic slots under simulated colour vision deficiency (Machado 2009 at full severity, Oklab distance). Arrows mark the vision types this variant is tuned for.

| Vision | Weakest pair overall | Weakest priority pair |
|---|---|---|
| normal <- | blue/cyan 0.123 | green/yellow 0.145 |
| protan | blue/magenta 0.040 | green/yellow 0.066 |
| deutan | red/green 0.026 | red/green 0.026 |
| tritan | green/blue 0.059 | red/yellow 0.106 |


## `omarchy-beacon-redgreen-light-theme`

Red-green safe light. Red shifts to vermilion and green to bluish-green, then the two are pulled apart by lightness for the protan worst case.

Background `#FAF9F6`, mode `light`.

| Role | Hex | WCAG vs bg | Level | APCA Lc |
|---|---|---|---|---|
| foreground | `#2B2B28` | 13.49:1 | AAA | +97 |
| light_foreground | `#1C1C1A` | 16.21:1 | AAA | +100 |
| bright_foreground | `#0F0F0E` | 18.22:1 | AAA | +102 |
| dark_foreground | `#4E4E49` | 7.95:1 | AAA | +85 |
| muted / color8 | `#4B575E` | 7.06:1 | AAA | +82 |
| accent | `#004188` | 9.45:1 | AAA | +89 |
| red | `#581600` | 13.04:1 | AAA | +96 |
| green | `#00614D` | 7.08:1 | AAA | +82 |
| yellow | `#664500` | 8.26:1 | AAA | +86 |
| blue | `#004188` | 9.45:1 | AAA | +89 |
| magenta | `#611A6C` | 10.65:1 | AAA | +91 |
| cyan | `#003A44` | 11.81:1 | AAA | +94 |
| bright_red | `#471000` | 14.86:1 | AAA | +98 |
| bright_green | `#005140` | 8.86:1 | AAA | +88 |
| bright_yellow | `#563900` | 10.07:1 | AAA | +91 |
| bright_blue | `#003674` | 11.21:1 | AAA | +93 |
| bright_magenta | `#580065` | 12.44:1 | AAA | +94 |
| bright_cyan | `#002F39` | 13.61:1 | AAA | +97 |

- Lowest contrast of any palette colour against the background: **7.06:1** (AAA threshold is 7:1)
- Selected text, `bright_foreground` on `selection`: **7.16:1**
- Selection band against background: 2.55:1
- Active window border against background: 9.45:1 (1.4.11 needs 3:1)
- Inactive window border against background: 3.50:1

Perceptual separation between the six chromatic slots under simulated colour vision deficiency (Machado 2009 at full severity, Oklab distance). Arrows mark the vision types this variant is tuned for.

| Vision | Weakest pair overall | Weakest priority pair |
|---|---|---|
| normal | blue/cyan 0.118 | red/yellow 0.126 |
| protan <- | blue/magenta 0.073 | green/yellow 0.094 |
| deutan <- | blue/magenta 0.055 | green/yellow 0.082 |
| tritan | green/blue 0.052 | red/yellow 0.119 |


## `omarchy-beacon-blueyellow-light-theme`

Blue-yellow safe light. Red and green stay trustworthy here, so the work goes into separating blue from green and yellow from magenta.

Background `#FAF9F6`, mode `light`.

| Role | Hex | WCAG vs bg | Level | APCA Lc |
|---|---|---|---|---|
| foreground | `#2B2B28` | 13.49:1 | AAA | +97 |
| light_foreground | `#1C1C1A` | 16.21:1 | AAA | +100 |
| bright_foreground | `#0F0F0E` | 18.22:1 | AAA | +102 |
| dark_foreground | `#4E4E49` | 7.95:1 | AAA | +85 |
| muted / color8 | `#4B575E` | 7.06:1 | AAA | +82 |
| accent | `#6F000D` | 11.86:1 | AAA | +93 |
| red | `#6F000D` | 11.86:1 | AAA | +93 |
| green | `#003608` | 13.03:1 | AAA | +96 |
| yellow | `#724F00` | 7.04:1 | AAA | +82 |
| blue | `#003880` | 10.62:1 | AAA | +92 |
| magenta | `#7B1956` | 9.43:1 | AAA | +88 |
| cyan | `#005555` | 8.21:1 | AAA | +86 |
| bright_red | `#5C0009` | 13.67:1 | AAA | +96 |
| bright_green | `#002A05` | 14.96:1 | AAA | +99 |
| bright_yellow | `#5F4200` | 8.80:1 | AAA | +88 |
| bright_blue | `#002E6C` | 12.41:1 | AAA | +95 |
| bright_magenta | `#6F004B` | 11.22:1 | AAA | +92 |
| bright_cyan | `#004747` | 10.01:1 | AAA | +90 |

- Lowest contrast of any palette colour against the background: **7.04:1** (AAA threshold is 7:1)
- Selected text, `bright_foreground` on `selection`: **7.16:1**
- Selection band against background: 2.55:1
- Active window border against background: 11.86:1 (1.4.11 needs 3:1)
- Inactive window border against background: 3.50:1

Perceptual separation between the six chromatic slots under simulated colour vision deficiency (Machado 2009 at full severity, Oklab distance). Arrows mark the vision types this variant is tuned for.

| Vision | Weakest pair overall | Weakest priority pair |
|---|---|---|
| normal | red/magenta 0.109 | green/cyan 0.137 |
| protan | red/green 0.049 | red/green 0.049 |
| deutan | magenta/cyan 0.004 | red/green 0.067 |
| tritan <- | blue/cyan 0.048 | red/yellow 0.116 |
