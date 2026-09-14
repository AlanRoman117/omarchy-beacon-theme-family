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
| orange | `#FFAC71` | 10.02:1 | AAA | -67 |

- Lowest contrast of any palette colour against the background: **7.05:1** (AAA threshold is 7:1)
- Selected text, `bright_foreground` on `selection`: **7.15:1**
- Selection band against background: 2.58:1
- Active window border against background: 10.45:1 (1.4.11 needs 3:1)
- Inactive window border against background: 3.50:1
- `orange` sits outside the six-slot optimisation and does not move them. Its nearest slot is yellow under normal vision, Oklab distance 0.115

Perceptual separation between the six chromatic slots under simulated colour vision deficiency (Machado 2009 at full severity, Oklab distance). Arrows mark the vision types this variant is tuned for.

| Vision | Weakest pair overall | Weakest priority pair |
|---|---|---|
| normal <- | blue/cyan 0.132 | green/yellow 0.207 |
| protan | blue/magenta 0.037 | green/yellow 0.099 |
| deutan | red/green 0.013 | red/green 0.013 |
| tritan | yellow/magenta 0.040 | green/cyan 0.173 |

### VS Code (`vscode-theme.json`)

Every text and indicator pair the generated VS Code theme creates. Translucent highlights are measured as composited over the editor background. Rows marked advisory carry no requirement.

| Area | Foreground | On | Contrast | Needs |
|---|---|---|---|---|
| Editor syntax | red `#FA7C75` | editor `#10141A` | 7.22:1 | 7:1 |
| Editor syntax | green `#59C977` | editor `#10141A` | 8.84:1 | 7:1 |
| Editor syntax | yellow `#FFDA70` | editor `#10141A` | 13.65:1 | 7:1 |
| Editor syntax | blue `#99C6FF` | editor `#10141A` | 10.45:1 | 7:1 |
| Editor syntax | magenta `#FFBDE8` | editor `#10141A` | 12.05:1 | 7:1 |
| Editor syntax | cyan `#A8F6FF` | editor `#10141A` | 15.21:1 | 7:1 |
| Editor syntax | orange `#FFAC71` | editor `#10141A` | 10.02:1 | 7:1 |
| Editor syntax | muted (comments) `#95A2A9` | editor `#10141A` | 7.05:1 | 7:1 |
| Editor syntax | dark_foreground (operators) `#A3AEBD` | editor `#10141A` | 8.22:1 | 7:1 |
| Editor syntax | light_foreground (parameters) `#EDF1F6` | editor `#10141A` | 16.28:1 | 7:1 |
| Editor syntax | bright_red `#FF9A92` | editor `#10141A` | 9.05:1 | 7:1 |
| Editor syntax | bright_green `#59DD7F` | editor `#10141A` | 10.62:1 | 7:1 |
| Editor syntax | bright_yellow `#FFE9AD` | editor `#10141A` | 15.40:1 | 7:1 |
| Editor syntax | bright_blue `#B4D5FF` | editor `#10141A` | 12.23:1 | 7:1 |
| Editor syntax | bright_magenta `#FFD2EE` | editor `#10141A` | 13.81:1 | 7:1 |
| Editor syntax | bright_cyan `#C7F9FF` | editor `#10141A` | 16.20:1 | 7:1 |
| Text | foreground `#D8DFE8` | editor `#10141A` | 13.76:1 | 7:1 |
| Text | secondary text `#95A2A9` | editor `#10141A` | 7.05:1 | 7:1 |
| Non-text | control border `#5F6973` | editor `#10141A` | 3.30:1 | 3:1 |
| Non-text | focus ring `#99C6FF` | editor `#10141A` | 10.45:1 | 3:1 |
| Text | foreground `#D8DFE8` | side bar / status bar `#0A0E13` | 14.41:1 | 7:1 |
| Text | secondary text `#95A2A9` | side bar / status bar `#0A0E13` | 7.39:1 | 7:1 |
| Non-text | control border `#5F6973` | side bar / status bar `#0A0E13` | 3.46:1 | 3:1 |
| Non-text | focus ring `#99C6FF` | side bar / status bar `#0A0E13` | 10.94:1 | 3:1 |
| Text | foreground `#D8DFE8` | widgets, menus, inputs `#05070B` | 15.01:1 | 7:1 |
| Text | secondary text `#95A2A9` | widgets, menus, inputs `#05070B` | 7.70:1 | 7:1 |
| Non-text | control border `#5F6973` | widgets, menus, inputs `#05070B` | 3.60:1 | 3:1 |
| Non-text | focus ring `#99C6FF` | widgets, menus, inputs `#05070B` | 11.40:1 | 3:1 |
| Source control, side bar | red `#FA7C75` | side bar `#0A0E13` | 7.56:1 | 7:1 |
| Source control, side bar | green `#59C977` | side bar `#0A0E13` | 9.26:1 | 7:1 |
| Source control, side bar | yellow `#FFDA70` | side bar `#0A0E13` | 14.30:1 | 7:1 |
| Source control, side bar | magenta `#FFBDE8` | side bar `#0A0E13` | 12.62:1 | 7:1 |
| Source control, side bar | cyan `#A8F6FF` | side bar `#0A0E13` | 15.93:1 | 7:1 |
| Source control, side bar | blue `#99C6FF` | side bar `#0A0E13` | 10.94:1 | 7:1 |
| Lists | selected item `#FFFFFF` | active selection `#28364A` | 12.23:1 | 7:1 |
| Lists | foreground `#D8DFE8` | active selection `#28364A` | 9.11:1 | 7:1 |
| Lists | foreground `#D8DFE8` | hover `#252F3E` | 10.06:1 | 7:1 |
| Lists | secondary text `#95A2A9` | hover `#252F3E` | 5.16:1 | 4.5:1 |
| Lists | secondary text `#95A2A9` | active selection `#28364A` | 4.67:1 | 4.5:1 |
| Lists | match highlight `#99C6FF` | active selection `#28364A` | 6.92:1 | 4.5:1 |
| Buttons | label `#10141A` | primary button `#99C6FF` | 10.45:1 | 7:1 |
| Buttons | label `#10141A` | primary button, hover `#B4D5FF` | 12.23:1 | 7:1 |
| Buttons | label `#D8DFE8` | secondary button `#252F3E` | 10.06:1 | 7:1 |
| Buttons | label `#D8DFE8` | secondary button, hover `#28364A` | 9.11:1 | 7:1 |
| Status bar | label `#10141A` | debugging `#FFAC71` | 10.02:1 | 7:1 |
| Status bar | label `#10141A` | error item `#FA7C75` | 7.22:1 | 7:1 |
| Status bar | label `#10141A` | warning item `#FFDA70` | 13.65:1 | 7:1 |
| Non-text | cursor `#FFFFFF` | editor `#10141A` | 18.47:1 | 3:1 |
| Non-text | find match border `#FFDA70` | editor `#10141A` | 13.65:1 | 3:1 |
| Non-text | active tab indicator `#99C6FF` | editor `#10141A` | 10.45:1 | 3:1 |
| Non-text | gutter: added `#59C977` | editor `#10141A` | 8.84:1 | 3:1 |
| Non-text | gutter: modified `#FFDA70` | editor `#10141A` | 13.65:1 | 3:1 |
| Non-text | gutter: deleted `#FA7C75` | editor `#10141A` | 7.22:1 | 3:1 |
| Highlights | weakest syntax colour (muted (comments)) `#95A2A9` | selection `#24364F` | 4.67:1 | 4.5:1 |
| Highlights | weakest syntax colour (muted (comments)) `#95A2A9` | inactive selection `#1E2837` | 5.67:1 | 4.5:1 |
| Highlights | weakest syntax colour (muted (comments)) `#95A2A9` | current find match `#41340A` | 4.66:1 | 4.5:1 |
| Highlights | weakest syntax colour (muted (comments)) `#95A2A9` | other find matches `#2F270F` | 5.66:1 | 4.5:1 |
| Highlights | weakest syntax colour (muted (comments)) `#95A2A9` | word highlight `#1E2837` | 5.67:1 | 4.5:1 |
| Highlights | weakest syntax colour (muted (comments)) `#95A2A9` | line highlight `#181D24` | 6.47:1 | 4.5:1 |
| Highlights | weakest syntax colour (muted (comments)) `#95A2A9` | diff: inserted line `#182C1C` | 5.66:1 | 4.5:1 |
| Highlights | weakest syntax colour (muted (comments)) `#95A2A9` | diff: inserted text `#143D20` | 4.67:1 | 4.5:1 |
| Highlights | weakest syntax colour (muted (comments)) `#95A2A9` | diff: removed line `#3A211F` | 5.66:1 | 4.5:1 |
| Highlights | weakest syntax colour (muted (comments)) `#95A2A9` | diff: removed text `#562725` | 4.68:1 | 4.5:1 |
| Highlights | weakest syntax colour (muted (comments)) `#95A2A9` | merge conflict `#1A3420` | 5.15:1 | 4.5:1 |
| Highlights | weakest syntax colour (muted (comments)) `#95A2A9` | debug stack frame `#382D0D` | 5.18:1 | 4.5:1 |
| Highlight visibility | selection `#24364F` | editor `#10141A` | 1.51:1 | advisory |
| Highlight visibility | current find match `#41340A` | editor `#10141A` | 1.51:1 | advisory |
| Highlight visibility | diff: inserted text `#143D20` | editor `#10141A` | 1.51:1 | advisory |
| Highlight visibility | diff: removed text `#562725` | editor `#10141A` | 1.51:1 | advisory |
| Highlight visibility | active list row `#28364A` | side bar `#0A0E13` | 1.58:1 | advisory |
| Highlight visibility | hovered list row `#252F3E` | side bar `#0A0E13` | 1.43:1 | advisory |


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
| orange | `#FFC798` | 12.20:1 | AAA | -79 |

- Lowest contrast of any palette colour against the background: **7.05:1** (AAA threshold is 7:1)
- Selected text, `bright_foreground` on `selection`: **7.15:1**
- Selection band against background: 2.58:1
- Active window border against background: 10.48:1 (1.4.11 needs 3:1)
- Inactive window border against background: 3.50:1
- `orange` sits outside the six-slot optimisation and does not move them. Its nearest slot is yellow under deutan vision, Oklab distance 0.080

Perceptual separation between the six chromatic slots under simulated colour vision deficiency (Machado 2009 at full severity, Oklab distance). Arrows mark the vision types this variant is tuned for.

| Vision | Weakest pair overall | Weakest priority pair |
|---|---|---|
| normal | blue/cyan 0.092 | green/cyan 0.183 |
| protan <- | blue/cyan 0.054 | green/cyan 0.182 |
| deutan <- | green/magenta 0.054 | red/yellow 0.143 |
| tritan | blue/cyan 0.068 | green/cyan 0.157 |

### VS Code (`vscode-theme.json`)

Every text and indicator pair the generated VS Code theme creates. Translucent highlights are measured as composited over the editor background. Rows marked advisory carry no requirement.

| Area | Foreground | On | Contrast | Needs |
|---|---|---|---|---|
| Editor syntax | red `#F5825E` | editor `#10141A` | 7.24:1 | 7:1 |
| Editor syntax | green `#8DFEDB` | editor `#10141A` | 15.24:1 | 7:1 |
| Editor syntax | yellow `#FCCA39` | editor `#10141A` | 12.00:1 | 7:1 |
| Editor syntax | blue `#9BC6FF` | editor `#10141A` | 10.48:1 | 7:1 |
| Editor syntax | magenta `#F9D0FF` | editor `#10141A` | 13.63:1 | 7:1 |
| Editor syntax | cyan `#53C1DA` | editor `#10141A` | 8.80:1 | 7:1 |
| Editor syntax | orange `#FFC798` | editor `#10141A` | 12.20:1 | 7:1 |
| Editor syntax | muted (comments) `#95A2A9` | editor `#10141A` | 7.05:1 | 7:1 |
| Editor syntax | dark_foreground (operators) `#A3AEBD` | editor `#10141A` | 8.22:1 | 7:1 |
| Editor syntax | light_foreground (parameters) `#EDF1F6` | editor `#10141A` | 16.28:1 | 7:1 |
| Editor syntax | bright_red `#FF9B7D` | editor `#10141A` | 9.00:1 | 7:1 |
| Editor syntax | bright_green `#C5FFEB` | editor `#10141A` | 16.60:1 | 7:1 |
| Editor syntax | bright_yellow `#FFDB80` | editor `#10141A` | 13.80:1 | 7:1 |
| Editor syntax | bright_blue `#B5D5FF` | editor `#10141A` | 12.25:1 | 7:1 |
| Editor syntax | bright_magenta `#FBDFFF` | editor `#10141A` | 15.04:1 | 7:1 |
| Editor syntax | bright_cyan `#46D5F3` | editor `#10141A` | 10.62:1 | 7:1 |
| Text | foreground `#D8DFE8` | editor `#10141A` | 13.76:1 | 7:1 |
| Text | secondary text `#95A2A9` | editor `#10141A` | 7.05:1 | 7:1 |
| Non-text | control border `#5F6973` | editor `#10141A` | 3.30:1 | 3:1 |
| Non-text | focus ring `#9BC6FF` | editor `#10141A` | 10.48:1 | 3:1 |
| Text | foreground `#D8DFE8` | side bar / status bar `#0A0E13` | 14.41:1 | 7:1 |
| Text | secondary text `#95A2A9` | side bar / status bar `#0A0E13` | 7.39:1 | 7:1 |
| Non-text | control border `#5F6973` | side bar / status bar `#0A0E13` | 3.46:1 | 3:1 |
| Non-text | focus ring `#9BC6FF` | side bar / status bar `#0A0E13` | 10.98:1 | 3:1 |
| Text | foreground `#D8DFE8` | widgets, menus, inputs `#05070B` | 15.01:1 | 7:1 |
| Text | secondary text `#95A2A9` | widgets, menus, inputs `#05070B` | 7.70:1 | 7:1 |
| Non-text | control border `#5F6973` | widgets, menus, inputs `#05070B` | 3.60:1 | 3:1 |
| Non-text | focus ring `#9BC6FF` | widgets, menus, inputs `#05070B` | 11.44:1 | 3:1 |
| Source control, side bar | red `#F5825E` | side bar `#0A0E13` | 7.59:1 | 7:1 |
| Source control, side bar | green `#8DFEDB` | side bar `#0A0E13` | 15.97:1 | 7:1 |
| Source control, side bar | yellow `#FCCA39` | side bar `#0A0E13` | 12.58:1 | 7:1 |
| Source control, side bar | magenta `#F9D0FF` | side bar `#0A0E13` | 14.28:1 | 7:1 |
| Source control, side bar | cyan `#53C1DA` | side bar `#0A0E13` | 9.22:1 | 7:1 |
| Source control, side bar | blue `#9BC6FF` | side bar `#0A0E13` | 10.98:1 | 7:1 |
| Lists | selected item `#FFFFFF` | active selection `#28364A` | 12.23:1 | 7:1 |
| Lists | foreground `#D8DFE8` | active selection `#28364A` | 9.11:1 | 7:1 |
| Lists | foreground `#D8DFE8` | hover `#252F3E` | 10.06:1 | 7:1 |
| Lists | secondary text `#95A2A9` | hover `#252F3E` | 5.16:1 | 4.5:1 |
| Lists | secondary text `#95A2A9` | active selection `#28364A` | 4.67:1 | 4.5:1 |
| Lists | match highlight `#9BC6FF` | active selection `#28364A` | 6.94:1 | 4.5:1 |
| Buttons | label `#10141A` | primary button `#9BC6FF` | 10.48:1 | 7:1 |
| Buttons | label `#10141A` | primary button, hover `#B5D5FF` | 12.25:1 | 7:1 |
| Buttons | label `#D8DFE8` | secondary button `#252F3E` | 10.06:1 | 7:1 |
| Buttons | label `#D8DFE8` | secondary button, hover `#28364A` | 9.11:1 | 7:1 |
| Status bar | label `#10141A` | debugging `#FFC798` | 12.20:1 | 7:1 |
| Status bar | label `#10141A` | error item `#F5825E` | 7.24:1 | 7:1 |
| Status bar | label `#10141A` | warning item `#FCCA39` | 12.00:1 | 7:1 |
| Non-text | cursor `#FFFFFF` | editor `#10141A` | 18.47:1 | 3:1 |
| Non-text | find match border `#FCCA39` | editor `#10141A` | 12.00:1 | 3:1 |
| Non-text | active tab indicator `#9BC6FF` | editor `#10141A` | 10.48:1 | 3:1 |
| Non-text | gutter: added `#8DFEDB` | editor `#10141A` | 15.24:1 | 3:1 |
| Non-text | gutter: modified `#FCCA39` | editor `#10141A` | 12.00:1 | 3:1 |
| Non-text | gutter: deleted `#F5825E` | editor `#10141A` | 7.24:1 | 3:1 |
| Highlights | weakest syntax colour (muted (comments)) `#95A2A9` | selection `#24364F` | 4.67:1 | 4.5:1 |
| Highlights | weakest syntax colour (muted (comments)) `#95A2A9` | inactive selection `#1E2837` | 5.67:1 | 4.5:1 |
| Highlights | weakest syntax colour (muted (comments)) `#95A2A9` | current find match `#42330A` | 4.69:1 | 4.5:1 |
| Highlights | weakest syntax colour (muted (comments)) `#95A2A9` | other find matches `#30260F` | 5.69:1 | 4.5:1 |
| Highlights | weakest syntax colour (muted (comments)) `#95A2A9` | word highlight `#1E2837` | 5.67:1 | 4.5:1 |
| Highlights | weakest syntax colour (muted (comments)) `#95A2A9` | line highlight `#181D24` | 6.47:1 | 4.5:1 |
| Highlights | weakest syntax colour (muted (comments)) `#95A2A9` | diff: inserted line `#0E2C24` | 5.71:1 | 4.5:1 |
| Highlights | weakest syntax colour (muted (comments)) `#95A2A9` | diff: inserted text `#003D2F` | 4.69:1 | 4.5:1 |
| Highlights | weakest syntax colour (muted (comments)) `#95A2A9` | diff: removed line `#3A211A` | 5.68:1 | 4.5:1 |
| Highlights | weakest syntax colour (muted (comments)) `#95A2A9` | diff: removed text `#55291B` | 4.66:1 | 4.5:1 |
| Highlights | weakest syntax colour (muted (comments)) `#95A2A9` | merge conflict `#0B352A` | 5.15:1 | 4.5:1 |
| Highlights | weakest syntax colour (muted (comments)) `#95A2A9` | debug stack frame `#392D0E` | 5.15:1 | 4.5:1 |
| Highlight visibility | selection `#24364F` | editor `#10141A` | 1.51:1 | advisory |
| Highlight visibility | current find match `#42330A` | editor `#10141A` | 1.50:1 | advisory |
| Highlight visibility | diff: inserted text `#003D2F` | editor `#10141A` | 1.50:1 | advisory |
| Highlight visibility | diff: removed text `#55291B` | editor `#10141A` | 1.51:1 | advisory |
| Highlight visibility | active list row `#28364A` | side bar `#0A0E13` | 1.58:1 | advisory |
| Highlight visibility | hovered list row `#252F3E` | side bar `#0A0E13` | 1.43:1 | advisory |


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
| orange | `#FFB37E` | 10.56:1 | AAA | -70 |

- Lowest contrast of any palette colour against the background: **7.05:1** (AAA threshold is 7:1)
- Selected text, `bright_foreground` on `selection`: **7.15:1**
- Selection band against background: 2.58:1
- Active window border against background: 8.80:1 (1.4.11 needs 3:1)
- Inactive window border against background: 3.50:1
- `orange` sits outside the six-slot optimisation and does not move them. Its nearest slot is red under tritan vision, Oklab distance 0.061

Perceptual separation between the six chromatic slots under simulated colour vision deficiency (Machado 2009 at full severity, Oklab distance). Arrows mark the vision types this variant is tuned for.

| Vision | Weakest pair overall | Weakest priority pair |
|---|---|---|
| normal | red/magenta 0.118 | red/yellow 0.190 |
| protan | blue/magenta 0.052 | red/green 0.068 |
| deutan | magenta/cyan 0.028 | red/green 0.094 |
| tritan <- | yellow/magenta 0.079 | green/cyan 0.192 |

### VS Code (`vscode-theme.json`)

Every text and indicator pair the generated VS Code theme creates. Translucent highlights are measured as composited over the editor background. Rows marked advisory carry no requirement.

| Area | Foreground | On | Contrast | Needs |
|---|---|---|---|---|
| Editor syntax | red `#FF968F` | editor `#10141A` | 8.80:1 | 7:1 |
| Editor syntax | green `#59B55F` | editor `#10141A` | 7.21:1 | 7:1 |
| Editor syntax | yellow `#FFE7B4` | editor `#10141A` | 15.25:1 | 7:1 |
| Editor syntax | blue `#9DC5FF` | editor `#10141A` | 10.43:1 | 7:1 |
| Editor syntax | magenta `#FFBEDE` | editor `#10141A` | 12.02:1 | 7:1 |
| Editor syntax | cyan `#75F0F0` | editor `#10141A` | 13.61:1 | 7:1 |
| Editor syntax | orange `#FFB37E` | editor `#10141A` | 10.56:1 | 7:1 |
| Editor syntax | muted (comments) `#95A2A9` | editor `#10141A` | 7.05:1 | 7:1 |
| Editor syntax | dark_foreground (operators) `#A3AEBD` | editor `#10141A` | 8.22:1 | 7:1 |
| Editor syntax | light_foreground (parameters) `#EDF1F6` | editor `#10141A` | 16.28:1 | 7:1 |
| Editor syntax | bright_red `#FFB1A9` | editor `#10141A` | 10.65:1 | 7:1 |
| Editor syntax | bright_green `#60CB67` | editor `#10141A` | 9.00:1 | 7:1 |
| Editor syntax | bright_yellow `#FFECC4` | editor `#10141A` | 15.87:1 | 7:1 |
| Editor syntax | bright_blue `#B7D4FF` | editor `#10141A` | 12.20:1 | 7:1 |
| Editor syntax | bright_magenta `#FFD3E8` | editor `#10141A` | 13.84:1 | 7:1 |
| Editor syntax | bright_cyan `#7FFEFF` | editor `#10141A` | 15.41:1 | 7:1 |
| Text | foreground `#D8DFE8` | editor `#10141A` | 13.76:1 | 7:1 |
| Text | secondary text `#95A2A9` | editor `#10141A` | 7.05:1 | 7:1 |
| Non-text | control border `#5F6973` | editor `#10141A` | 3.30:1 | 3:1 |
| Non-text | focus ring `#FF968F` | editor `#10141A` | 8.80:1 | 3:1 |
| Text | foreground `#D8DFE8` | side bar / status bar `#0A0E13` | 14.41:1 | 7:1 |
| Text | secondary text `#95A2A9` | side bar / status bar `#0A0E13` | 7.39:1 | 7:1 |
| Non-text | control border `#5F6973` | side bar / status bar `#0A0E13` | 3.46:1 | 3:1 |
| Non-text | focus ring `#FF968F` | side bar / status bar `#0A0E13` | 9.23:1 | 3:1 |
| Text | foreground `#D8DFE8` | widgets, menus, inputs `#05070B` | 15.01:1 | 7:1 |
| Text | secondary text `#95A2A9` | widgets, menus, inputs `#05070B` | 7.70:1 | 7:1 |
| Non-text | control border `#5F6973` | widgets, menus, inputs `#05070B` | 3.60:1 | 3:1 |
| Non-text | focus ring `#FF968F` | widgets, menus, inputs `#05070B` | 9.61:1 | 3:1 |
| Source control, side bar | red `#FF968F` | side bar `#0A0E13` | 9.23:1 | 7:1 |
| Source control, side bar | green `#59B55F` | side bar `#0A0E13` | 7.56:1 | 7:1 |
| Source control, side bar | yellow `#FFE7B4` | side bar `#0A0E13` | 15.98:1 | 7:1 |
| Source control, side bar | magenta `#FFBEDE` | side bar `#0A0E13` | 12.60:1 | 7:1 |
| Source control, side bar | cyan `#75F0F0` | side bar `#0A0E13` | 14.26:1 | 7:1 |
| Source control, side bar | blue `#9DC5FF` | side bar `#0A0E13` | 10.93:1 | 7:1 |
| Lists | selected item `#FFFFFF` | active selection `#28364A` | 12.23:1 | 7:1 |
| Lists | foreground `#D8DFE8` | active selection `#28364A` | 9.11:1 | 7:1 |
| Lists | foreground `#D8DFE8` | hover `#252F3E` | 10.06:1 | 7:1 |
| Lists | secondary text `#95A2A9` | hover `#252F3E` | 5.16:1 | 4.5:1 |
| Lists | secondary text `#95A2A9` | active selection `#28364A` | 4.67:1 | 4.5:1 |
| Lists | match highlight `#FF968F` | active selection `#28364A` | 5.83:1 | 4.5:1 |
| Buttons | label `#10141A` | primary button `#FF968F` | 8.80:1 | 7:1 |
| Buttons | label `#10141A` | primary button, hover `#FFB1A9` | 10.65:1 | 7:1 |
| Buttons | label `#D8DFE8` | secondary button `#252F3E` | 10.06:1 | 7:1 |
| Buttons | label `#D8DFE8` | secondary button, hover `#28364A` | 9.11:1 | 7:1 |
| Status bar | label `#10141A` | debugging `#FFB37E` | 10.56:1 | 7:1 |
| Status bar | label `#10141A` | error item `#FF968F` | 8.80:1 | 7:1 |
| Status bar | label `#10141A` | warning item `#FFE7B4` | 15.25:1 | 7:1 |
| Non-text | cursor `#FFFFFF` | editor `#10141A` | 18.47:1 | 3:1 |
| Non-text | find match border `#FFE7B4` | editor `#10141A` | 15.25:1 | 3:1 |
| Non-text | active tab indicator `#FF968F` | editor `#10141A` | 8.80:1 | 3:1 |
| Non-text | gutter: added `#59B55F` | editor `#10141A` | 7.21:1 | 3:1 |
| Non-text | gutter: modified `#FFE7B4` | editor `#10141A` | 15.25:1 | 3:1 |
| Non-text | gutter: deleted `#FF968F` | editor `#10141A` | 8.80:1 | 3:1 |
| Highlights | weakest syntax colour (muted (comments)) `#95A2A9` | selection `#24364F` | 4.67:1 | 4.5:1 |
| Highlights | weakest syntax colour (muted (comments)) `#95A2A9` | inactive selection `#1E2837` | 5.67:1 | 4.5:1 |
| Highlights | weakest syntax colour (muted (comments)) `#95A2A9` | current find match `#44330B` | 4.65:1 | 4.5:1 |
| Highlights | weakest syntax colour (muted (comments)) `#95A2A9` | other find matches `#31260F` | 5.67:1 | 4.5:1 |
| Highlights | weakest syntax colour (muted (comments)) `#95A2A9` | word highlight `#1E2837` | 5.67:1 | 4.5:1 |
| Highlights | weakest syntax colour (muted (comments)) `#95A2A9` | line highlight `#181D24` | 6.47:1 | 4.5:1 |
| Highlights | weakest syntax colour (muted (comments)) `#95A2A9` | diff: inserted line `#1A2C1A` | 5.65:1 | 4.5:1 |
| Highlights | weakest syntax colour (muted (comments)) `#95A2A9` | diff: inserted text `#193C1C` | 4.70:1 | 4.5:1 |
| Highlights | weakest syntax colour (muted (comments)) `#95A2A9` | diff: removed line `#3A211F` | 5.66:1 | 4.5:1 |
| Highlights | weakest syntax colour (muted (comments)) `#95A2A9` | diff: removed text `#562725` | 4.68:1 | 4.5:1 |
| Highlights | weakest syntax colour (muted (comments)) `#95A2A9` | merge conflict `#1C331D` | 5.20:1 | 4.5:1 |
| Highlights | weakest syntax colour (muted (comments)) `#95A2A9` | debug stack frame `#3A2C0D` | 5.19:1 | 4.5:1 |
| Highlight visibility | selection `#24364F` | editor `#10141A` | 1.51:1 | advisory |
| Highlight visibility | current find match `#44330B` | editor `#10141A` | 1.52:1 | advisory |
| Highlight visibility | diff: inserted text `#193C1C` | editor `#10141A` | 1.50:1 | advisory |
| Highlight visibility | diff: removed text `#562725` | editor `#10141A` | 1.51:1 | advisory |
| Highlight visibility | active list row `#28364A` | side bar `#0A0E13` | 1.58:1 | advisory |
| Highlight visibility | hovered list row `#252F3E` | side bar `#0A0E13` | 1.43:1 | advisory |


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
| orange | `#8D3F00` | 7.01:1 | AAA | +81 |

- Lowest contrast of any palette colour against the background: **7.00:1** (AAA threshold is 7:1)
- Selected text, `bright_foreground` on `selection`: **7.16:1**
- Selection band against background: 2.55:1
- Active window border against background: 10.66:1 (1.4.11 needs 3:1)
- Inactive window border against background: 3.50:1
- `orange` sits outside the six-slot optimisation and does not move them. Its nearest slot is yellow under normal vision, Oklab distance 0.077

Perceptual separation between the six chromatic slots under simulated colour vision deficiency (Machado 2009 at full severity, Oklab distance). Arrows mark the vision types this variant is tuned for.

| Vision | Weakest pair overall | Weakest priority pair |
|---|---|---|
| normal <- | blue/cyan 0.123 | green/yellow 0.145 |
| protan | blue/magenta 0.040 | green/yellow 0.066 |
| deutan | red/green 0.026 | red/green 0.026 |
| tritan | green/blue 0.059 | red/yellow 0.106 |

### VS Code (`vscode-theme.json`)

Every text and indicator pair the generated VS Code theme creates. Translucent highlights are measured as composited over the editor background. Rows marked advisory carry no requirement.

| Area | Foreground | On | Contrast | Needs |
|---|---|---|---|---|
| Editor syntax | red `#62000A` | editor `#FAF9F6` | 13.09:1 | 7:1 |
| Editor syntax | green `#003D18` | editor `#FAF9F6` | 11.87:1 | 7:1 |
| Editor syntax | yellow `#664500` | editor `#FAF9F6` | 8.26:1 | 7:1 |
| Editor syntax | blue `#003A77` | editor `#FAF9F6` | 10.66:1 | 7:1 |
| Editor syntax | magenta `#781A61` | editor `#FAF9F6` | 9.41:1 | 7:1 |
| Editor syntax | cyan `#005F6B` | editor `#FAF9F6` | 7.00:1 | 7:1 |
| Editor syntax | orange `#8D3F00` | editor `#FAF9F6` | 7.01:1 | 7:1 |
| Editor syntax | muted (comments) `#4B575E` | editor `#FAF9F6` | 7.06:1 | 7:1 |
| Editor syntax | dark_foreground (operators) `#4E4E49` | editor `#FAF9F6` | 7.95:1 | 7:1 |
| Editor syntax | light_foreground (parameters) `#1C1C1A` | editor `#FAF9F6` | 16.21:1 | 7:1 |
| Editor syntax | bright_red `#500006` | editor `#FAF9F6` | 14.84:1 | 7:1 |
| Editor syntax | bright_green `#003212` | editor `#FAF9F6` | 13.62:1 | 7:1 |
| Editor syntax | bright_yellow `#563900` | editor `#FAF9F6` | 10.07:1 | 7:1 |
| Editor syntax | bright_blue `#003064` | editor `#FAF9F6` | 12.41:1 | 7:1 |
| Editor syntax | bright_magenta `#6C0056` | editor `#FAF9F6` | 11.26:1 | 7:1 |
| Editor syntax | bright_cyan `#004F5A` | editor `#FAF9F6` | 8.80:1 | 7:1 |
| Text | foreground `#2B2B28` | editor `#FAF9F6` | 13.49:1 | 7:1 |
| Text | secondary text `#4B575E` | editor `#FAF9F6` | 7.06:1 | 7:1 |
| Non-text | control border `#808A95` | editor `#FAF9F6` | 3.33:1 | 3:1 |
| Non-text | focus ring `#003A77` | editor `#FAF9F6` | 10.66:1 | 3:1 |
| Text | foreground `#2B2B28` | side bar / status bar `#FFFFFF` | 14.20:1 | 7:1 |
| Text | secondary text `#4B575E` | side bar / status bar `#FFFFFF` | 7.44:1 | 7:1 |
| Non-text | control border `#808A95` | side bar / status bar `#FFFFFF` | 3.51:1 | 3:1 |
| Non-text | focus ring `#003A77` | side bar / status bar `#FFFFFF` | 11.22:1 | 3:1 |
| Text | foreground `#2B2B28` | widgets, menus, inputs `#FFFFFF` | 14.20:1 | 7:1 |
| Text | secondary text `#4B575E` | widgets, menus, inputs `#FFFFFF` | 7.44:1 | 7:1 |
| Non-text | control border `#808A95` | widgets, menus, inputs `#FFFFFF` | 3.51:1 | 3:1 |
| Non-text | focus ring `#003A77` | widgets, menus, inputs `#FFFFFF` | 11.22:1 | 3:1 |
| Source control, side bar | red `#62000A` | side bar `#FFFFFF` | 13.78:1 | 7:1 |
| Source control, side bar | green `#003D18` | side bar `#FFFFFF` | 12.49:1 | 7:1 |
| Source control, side bar | yellow `#664500` | side bar `#FFFFFF` | 8.69:1 | 7:1 |
| Source control, side bar | magenta `#781A61` | side bar `#FFFFFF` | 9.91:1 | 7:1 |
| Source control, side bar | cyan `#005F6B` | side bar `#FFFFFF` | 7.37:1 | 7:1 |
| Source control, side bar | blue `#003A77` | side bar `#FFFFFF` | 11.22:1 | 7:1 |
| Lists | selected item `#0F0F0E` | active selection `#BBCFE7` | 12.05:1 | 7:1 |
| Lists | foreground `#2B2B28` | active selection `#BBCFE7` | 8.92:1 | 7:1 |
| Lists | foreground `#2B2B28` | hover `#CBDAED` | 10.00:1 | 7:1 |
| Lists | secondary text `#4B575E` | hover `#CBDAED` | 5.24:1 | 4.5:1 |
| Lists | secondary text `#4B575E` | active selection `#BBCFE7` | 4.67:1 | 4.5:1 |
| Lists | match highlight `#003A77` | active selection `#BBCFE7` | 7.05:1 | 4.5:1 |
| Buttons | label `#FAF9F6` | primary button `#003A77` | 10.66:1 | 7:1 |
| Buttons | label `#FAF9F6` | primary button, hover `#003064` | 12.41:1 | 7:1 |
| Buttons | label `#2B2B28` | secondary button `#CBDAED` | 10.00:1 | 7:1 |
| Buttons | label `#2B2B28` | secondary button, hover `#BBCFE7` | 8.92:1 | 7:1 |
| Status bar | label `#FAF9F6` | debugging `#8D3F00` | 7.01:1 | 7:1 |
| Status bar | label `#FAF9F6` | error item `#62000A` | 13.09:1 | 7:1 |
| Status bar | label `#FAF9F6` | warning item `#664500` | 8.26:1 | 7:1 |
| Non-text | cursor `#0F0F0E` | editor `#FAF9F6` | 18.22:1 | 3:1 |
| Non-text | find match border `#664500` | editor `#FAF9F6` | 8.26:1 | 3:1 |
| Non-text | active tab indicator `#003A77` | editor `#FAF9F6` | 10.66:1 | 3:1 |
| Non-text | gutter: added `#003D18` | editor `#FAF9F6` | 11.87:1 | 3:1 |
| Non-text | gutter: modified `#664500` | editor `#FAF9F6` | 8.26:1 | 3:1 |
| Non-text | gutter: deleted `#62000A` | editor `#FAF9F6` | 13.09:1 | 3:1 |
| Highlights | weakest syntax colour (cyan) `#005F6B` | selection `#B7D0EE` | 4.66:1 | 4.5:1 |
| Highlights | weakest syntax colour (cyan) `#005F6B` | inactive selection `#D4E3F5` | 5.65:1 | 4.5:1 |
| Highlights | weakest syntax colour (cyan) `#005F6B` | current find match `#E4CAA2` | 4.66:1 | 4.5:1 |
| Highlights | weakest syntax colour (cyan) `#005F6B` | other find matches `#F1DFC5` | 5.65:1 | 4.5:1 |
| Highlights | weakest syntax colour (cyan) `#005F6B` | word highlight `#D4E3F5` | 5.65:1 | 4.5:1 |
| Highlights | weakest syntax colour (cyan) `#005F6B` | line highlight `#E9F1FA` | 6.47:1 | 4.5:1 |
| Highlights | weakest syntax colour (cyan) `#005F6B` | diff: inserted line `#CEE8D3` | 5.65:1 | 4.5:1 |
| Highlights | weakest syntax colour (cyan) `#005F6B` | diff: inserted text `#ABD9B3` | 4.67:1 | 4.5:1 |
| Highlights | weakest syntax colour (cyan) `#005F6B` | diff: removed line `#FDDAD6` | 5.68:1 | 4.5:1 |
| Highlights | weakest syntax colour (cyan) `#005F6B` | diff: removed text `#FBBFB9` | 4.65:1 | 4.5:1 |
| Highlights | weakest syntax colour (cyan) `#005F6B` | merge conflict `#BFE0C5` | 5.15:1 | 4.5:1 |
| Highlights | weakest syntax colour (cyan) `#005F6B` | debug stack frame `#EBD5B4` | 5.16:1 | 4.5:1 |
| Highlight visibility | selection `#B7D0EE` | editor `#FAF9F6` | 1.50:1 | advisory |
| Highlight visibility | current find match `#E4CAA2` | editor `#FAF9F6` | 1.50:1 | advisory |
| Highlight visibility | diff: inserted text `#ABD9B3` | editor `#FAF9F6` | 1.50:1 | advisory |
| Highlight visibility | diff: removed text `#FBBFB9` | editor `#FAF9F6` | 1.50:1 | advisory |
| Highlight visibility | active list row `#BBCFE7` | side bar `#FFFFFF` | 1.59:1 | advisory |
| Highlight visibility | hovered list row `#CBDAED` | side bar `#FFFFFF` | 1.42:1 | advisory |


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
| orange | `#603000` | 10.39:1 | AAA | +91 |

- Lowest contrast of any palette colour against the background: **7.06:1** (AAA threshold is 7:1)
- Selected text, `bright_foreground` on `selection`: **7.16:1**
- Selection band against background: 2.55:1
- Active window border against background: 9.45:1 (1.4.11 needs 3:1)
- Inactive window border against background: 3.50:1
- `orange` sits outside the six-slot optimisation and does not move them. Its nearest slot is yellow under deutan vision, Oklab distance 0.052

Perceptual separation between the six chromatic slots under simulated colour vision deficiency (Machado 2009 at full severity, Oklab distance). Arrows mark the vision types this variant is tuned for.

| Vision | Weakest pair overall | Weakest priority pair |
|---|---|---|
| normal | blue/cyan 0.118 | red/yellow 0.126 |
| protan <- | blue/magenta 0.073 | green/yellow 0.094 |
| deutan <- | blue/magenta 0.055 | green/yellow 0.082 |
| tritan | green/blue 0.052 | red/yellow 0.119 |

### VS Code (`vscode-theme.json`)

Every text and indicator pair the generated VS Code theme creates. Translucent highlights are measured as composited over the editor background. Rows marked advisory carry no requirement.

| Area | Foreground | On | Contrast | Needs |
|---|---|---|---|---|
| Editor syntax | red `#581600` | editor `#FAF9F6` | 13.04:1 | 7:1 |
| Editor syntax | green `#00614D` | editor `#FAF9F6` | 7.08:1 | 7:1 |
| Editor syntax | yellow `#664500` | editor `#FAF9F6` | 8.26:1 | 7:1 |
| Editor syntax | blue `#004188` | editor `#FAF9F6` | 9.45:1 | 7:1 |
| Editor syntax | magenta `#611A6C` | editor `#FAF9F6` | 10.65:1 | 7:1 |
| Editor syntax | cyan `#003A44` | editor `#FAF9F6` | 11.81:1 | 7:1 |
| Editor syntax | orange `#603000` | editor `#FAF9F6` | 10.39:1 | 7:1 |
| Editor syntax | muted (comments) `#4B575E` | editor `#FAF9F6` | 7.06:1 | 7:1 |
| Editor syntax | dark_foreground (operators) `#4E4E49` | editor `#FAF9F6` | 7.95:1 | 7:1 |
| Editor syntax | light_foreground (parameters) `#1C1C1A` | editor `#FAF9F6` | 16.21:1 | 7:1 |
| Editor syntax | bright_red `#471000` | editor `#FAF9F6` | 14.86:1 | 7:1 |
| Editor syntax | bright_green `#005140` | editor `#FAF9F6` | 8.86:1 | 7:1 |
| Editor syntax | bright_yellow `#563900` | editor `#FAF9F6` | 10.07:1 | 7:1 |
| Editor syntax | bright_blue `#003674` | editor `#FAF9F6` | 11.21:1 | 7:1 |
| Editor syntax | bright_magenta `#580065` | editor `#FAF9F6` | 12.44:1 | 7:1 |
| Editor syntax | bright_cyan `#002F39` | editor `#FAF9F6` | 13.61:1 | 7:1 |
| Text | foreground `#2B2B28` | editor `#FAF9F6` | 13.49:1 | 7:1 |
| Text | secondary text `#4B575E` | editor `#FAF9F6` | 7.06:1 | 7:1 |
| Non-text | control border `#808A95` | editor `#FAF9F6` | 3.33:1 | 3:1 |
| Non-text | focus ring `#004188` | editor `#FAF9F6` | 9.45:1 | 3:1 |
| Text | foreground `#2B2B28` | side bar / status bar `#FFFFFF` | 14.20:1 | 7:1 |
| Text | secondary text `#4B575E` | side bar / status bar `#FFFFFF` | 7.44:1 | 7:1 |
| Non-text | control border `#808A95` | side bar / status bar `#FFFFFF` | 3.51:1 | 3:1 |
| Non-text | focus ring `#004188` | side bar / status bar `#FFFFFF` | 9.94:1 | 3:1 |
| Text | foreground `#2B2B28` | widgets, menus, inputs `#FFFFFF` | 14.20:1 | 7:1 |
| Text | secondary text `#4B575E` | widgets, menus, inputs `#FFFFFF` | 7.44:1 | 7:1 |
| Non-text | control border `#808A95` | widgets, menus, inputs `#FFFFFF` | 3.51:1 | 3:1 |
| Non-text | focus ring `#004188` | widgets, menus, inputs `#FFFFFF` | 9.94:1 | 3:1 |
| Source control, side bar | red `#581600` | side bar `#FFFFFF` | 13.73:1 | 7:1 |
| Source control, side bar | green `#00614D` | side bar `#FFFFFF` | 7.45:1 | 7:1 |
| Source control, side bar | yellow `#664500` | side bar `#FFFFFF` | 8.69:1 | 7:1 |
| Source control, side bar | magenta `#611A6C` | side bar `#FFFFFF` | 11.21:1 | 7:1 |
| Source control, side bar | cyan `#003A44` | side bar `#FFFFFF` | 12.44:1 | 7:1 |
| Source control, side bar | blue `#004188` | side bar `#FFFFFF` | 9.94:1 | 7:1 |
| Lists | selected item `#0F0F0E` | active selection `#BBCFE7` | 12.05:1 | 7:1 |
| Lists | foreground `#2B2B28` | active selection `#BBCFE7` | 8.92:1 | 7:1 |
| Lists | foreground `#2B2B28` | hover `#CBDAED` | 10.00:1 | 7:1 |
| Lists | secondary text `#4B575E` | hover `#CBDAED` | 5.24:1 | 4.5:1 |
| Lists | secondary text `#4B575E` | active selection `#BBCFE7` | 4.67:1 | 4.5:1 |
| Lists | match highlight `#004188` | active selection `#BBCFE7` | 6.25:1 | 4.5:1 |
| Buttons | label `#FAF9F6` | primary button `#004188` | 9.45:1 | 7:1 |
| Buttons | label `#FAF9F6` | primary button, hover `#003674` | 11.21:1 | 7:1 |
| Buttons | label `#2B2B28` | secondary button `#CBDAED` | 10.00:1 | 7:1 |
| Buttons | label `#2B2B28` | secondary button, hover `#BBCFE7` | 8.92:1 | 7:1 |
| Status bar | label `#FAF9F6` | debugging `#603000` | 10.39:1 | 7:1 |
| Status bar | label `#FAF9F6` | error item `#581600` | 13.04:1 | 7:1 |
| Status bar | label `#FAF9F6` | warning item `#664500` | 8.26:1 | 7:1 |
| Non-text | cursor `#0F0F0E` | editor `#FAF9F6` | 18.22:1 | 3:1 |
| Non-text | find match border `#664500` | editor `#FAF9F6` | 8.26:1 | 3:1 |
| Non-text | active tab indicator `#004188` | editor `#FAF9F6` | 9.45:1 | 3:1 |
| Non-text | gutter: added `#00614D` | editor `#FAF9F6` | 7.08:1 | 3:1 |
| Non-text | gutter: modified `#664500` | editor `#FAF9F6` | 8.26:1 | 3:1 |
| Non-text | gutter: deleted `#581600` | editor `#FAF9F6` | 13.04:1 | 3:1 |
| Highlights | weakest syntax colour (muted (comments)) `#4B575E` | selection `#B6CFED` | 4.65:1 | 4.5:1 |
| Highlights | weakest syntax colour (muted (comments)) `#4B575E` | inactive selection `#D3E2F5` | 5.65:1 | 4.5:1 |
| Highlights | weakest syntax colour (muted (comments)) `#4B575E` | current find match `#E3C9A1` | 4.65:1 | 4.5:1 |
| Highlights | weakest syntax colour (muted (comments)) `#4B575E` | other find matches `#F0DFC4` | 5.69:1 | 4.5:1 |
| Highlights | weakest syntax colour (muted (comments)) `#4B575E` | word highlight `#D3E2F5` | 5.65:1 | 4.5:1 |
| Highlights | weakest syntax colour (muted (comments)) `#4B575E` | line highlight `#E8F0F9` | 6.47:1 | 4.5:1 |
| Highlights | weakest syntax colour (muted (comments)) `#4B575E` | diff: inserted line `#C6E8DC` | 5.66:1 | 4.5:1 |
| Highlights | weakest syntax colour (muted (comments)) `#4B575E` | diff: inserted text `#9BDAC5` | 4.68:1 | 4.5:1 |
| Highlights | weakest syntax colour (muted (comments)) `#4B575E` | diff: removed line `#FBDACF` | 5.68:1 | 4.5:1 |
| Highlights | weakest syntax colour (muted (comments)) `#4B575E` | diff: removed text `#F8C0AE` | 4.65:1 | 4.5:1 |
| Highlights | weakest syntax colour (muted (comments)) `#4B575E` | merge conflict `#B5E0D1` | 5.15:1 | 4.5:1 |
| Highlights | weakest syntax colour (muted (comments)) `#4B575E` | debug stack frame `#EAD4B3` | 5.16:1 | 4.5:1 |
| Highlight visibility | selection `#B6CFED` | editor `#FAF9F6` | 1.52:1 | advisory |
| Highlight visibility | current find match `#E3C9A1` | editor `#FAF9F6` | 1.52:1 | advisory |
| Highlight visibility | diff: inserted text `#9BDAC5` | editor `#FAF9F6` | 1.51:1 | advisory |
| Highlight visibility | diff: removed text `#F8C0AE` | editor `#FAF9F6` | 1.52:1 | advisory |
| Highlight visibility | active list row `#BBCFE7` | side bar `#FFFFFF` | 1.59:1 | advisory |
| Highlight visibility | hovered list row `#CBDAED` | side bar `#FFFFFF` | 1.42:1 | advisory |


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
| orange | `#4D2100` | 13.01:1 | AAA | +96 |

- Lowest contrast of any palette colour against the background: **7.04:1** (AAA threshold is 7:1)
- Selected text, `bright_foreground` on `selection`: **7.16:1**
- Selection band against background: 2.55:1
- Active window border against background: 11.86:1 (1.4.11 needs 3:1)
- Inactive window border against background: 3.50:1
- `orange` sits outside the six-slot optimisation and does not move them. Its nearest slot is red under tritan vision, Oklab distance 0.081

Perceptual separation between the six chromatic slots under simulated colour vision deficiency (Machado 2009 at full severity, Oklab distance). Arrows mark the vision types this variant is tuned for.

| Vision | Weakest pair overall | Weakest priority pair |
|---|---|---|
| normal | red/magenta 0.109 | green/cyan 0.137 |
| protan | red/green 0.049 | red/green 0.049 |
| deutan | magenta/cyan 0.004 | red/green 0.067 |
| tritan <- | blue/cyan 0.048 | red/yellow 0.116 |

### VS Code (`vscode-theme.json`)

Every text and indicator pair the generated VS Code theme creates. Translucent highlights are measured as composited over the editor background. Rows marked advisory carry no requirement.

| Area | Foreground | On | Contrast | Needs |
|---|---|---|---|---|
| Editor syntax | red `#6F000D` | editor `#FAF9F6` | 11.86:1 | 7:1 |
| Editor syntax | green `#003608` | editor `#FAF9F6` | 13.03:1 | 7:1 |
| Editor syntax | yellow `#724F00` | editor `#FAF9F6` | 7.04:1 | 7:1 |
| Editor syntax | blue `#003880` | editor `#FAF9F6` | 10.62:1 | 7:1 |
| Editor syntax | magenta `#7B1956` | editor `#FAF9F6` | 9.43:1 | 7:1 |
| Editor syntax | cyan `#005555` | editor `#FAF9F6` | 8.21:1 | 7:1 |
| Editor syntax | orange `#4D2100` | editor `#FAF9F6` | 13.01:1 | 7:1 |
| Editor syntax | muted (comments) `#4B575E` | editor `#FAF9F6` | 7.06:1 | 7:1 |
| Editor syntax | dark_foreground (operators) `#4E4E49` | editor `#FAF9F6` | 7.95:1 | 7:1 |
| Editor syntax | light_foreground (parameters) `#1C1C1A` | editor `#FAF9F6` | 16.21:1 | 7:1 |
| Editor syntax | bright_red `#5C0009` | editor `#FAF9F6` | 13.67:1 | 7:1 |
| Editor syntax | bright_green `#002A05` | editor `#FAF9F6` | 14.96:1 | 7:1 |
| Editor syntax | bright_yellow `#5F4200` | editor `#FAF9F6` | 8.80:1 | 7:1 |
| Editor syntax | bright_blue `#002E6C` | editor `#FAF9F6` | 12.41:1 | 7:1 |
| Editor syntax | bright_magenta `#6F004B` | editor `#FAF9F6` | 11.22:1 | 7:1 |
| Editor syntax | bright_cyan `#004747` | editor `#FAF9F6` | 10.01:1 | 7:1 |
| Text | foreground `#2B2B28` | editor `#FAF9F6` | 13.49:1 | 7:1 |
| Text | secondary text `#4B575E` | editor `#FAF9F6` | 7.06:1 | 7:1 |
| Non-text | control border `#808A95` | editor `#FAF9F6` | 3.33:1 | 3:1 |
| Non-text | focus ring `#6F000D` | editor `#FAF9F6` | 11.86:1 | 3:1 |
| Text | foreground `#2B2B28` | side bar / status bar `#FFFFFF` | 14.20:1 | 7:1 |
| Text | secondary text `#4B575E` | side bar / status bar `#FFFFFF` | 7.44:1 | 7:1 |
| Non-text | control border `#808A95` | side bar / status bar `#FFFFFF` | 3.51:1 | 3:1 |
| Non-text | focus ring `#6F000D` | side bar / status bar `#FFFFFF` | 12.49:1 | 3:1 |
| Text | foreground `#2B2B28` | widgets, menus, inputs `#FFFFFF` | 14.20:1 | 7:1 |
| Text | secondary text `#4B575E` | widgets, menus, inputs `#FFFFFF` | 7.44:1 | 7:1 |
| Non-text | control border `#808A95` | widgets, menus, inputs `#FFFFFF` | 3.51:1 | 3:1 |
| Non-text | focus ring `#6F000D` | widgets, menus, inputs `#FFFFFF` | 12.49:1 | 3:1 |
| Source control, side bar | red `#6F000D` | side bar `#FFFFFF` | 12.49:1 | 7:1 |
| Source control, side bar | green `#003608` | side bar `#FFFFFF` | 13.71:1 | 7:1 |
| Source control, side bar | yellow `#724F00` | side bar `#FFFFFF` | 7.41:1 | 7:1 |
| Source control, side bar | magenta `#7B1956` | side bar `#FFFFFF` | 9.93:1 | 7:1 |
| Source control, side bar | cyan `#005555` | side bar `#FFFFFF` | 8.64:1 | 7:1 |
| Source control, side bar | blue `#003880` | side bar `#FFFFFF` | 11.19:1 | 7:1 |
| Lists | selected item `#0F0F0E` | active selection `#BBCFE7` | 12.05:1 | 7:1 |
| Lists | foreground `#2B2B28` | active selection `#BBCFE7` | 8.92:1 | 7:1 |
| Lists | foreground `#2B2B28` | hover `#CBDAED` | 10.00:1 | 7:1 |
| Lists | secondary text `#4B575E` | hover `#CBDAED` | 5.24:1 | 4.5:1 |
| Lists | secondary text `#4B575E` | active selection `#BBCFE7` | 4.67:1 | 4.5:1 |
| Lists | match highlight `#6F000D` | active selection `#BBCFE7` | 7.84:1 | 4.5:1 |
| Buttons | label `#FAF9F6` | primary button `#6F000D` | 11.86:1 | 7:1 |
| Buttons | label `#FAF9F6` | primary button, hover `#5C0009` | 13.67:1 | 7:1 |
| Buttons | label `#2B2B28` | secondary button `#CBDAED` | 10.00:1 | 7:1 |
| Buttons | label `#2B2B28` | secondary button, hover `#BBCFE7` | 8.92:1 | 7:1 |
| Status bar | label `#FAF9F6` | debugging `#4D2100` | 13.01:1 | 7:1 |
| Status bar | label `#FAF9F6` | error item `#6F000D` | 11.86:1 | 7:1 |
| Status bar | label `#FAF9F6` | warning item `#724F00` | 7.04:1 | 7:1 |
| Non-text | cursor `#0F0F0E` | editor `#FAF9F6` | 18.22:1 | 3:1 |
| Non-text | find match border `#724F00` | editor `#FAF9F6` | 7.04:1 | 3:1 |
| Non-text | active tab indicator `#6F000D` | editor `#FAF9F6` | 11.86:1 | 3:1 |
| Non-text | gutter: added `#003608` | editor `#FAF9F6` | 13.03:1 | 3:1 |
| Non-text | gutter: modified `#724F00` | editor `#FAF9F6` | 7.04:1 | 3:1 |
| Non-text | gutter: deleted `#6F000D` | editor `#FAF9F6` | 11.86:1 | 3:1 |
| Highlights | weakest syntax colour (yellow) `#724F00` | selection `#B7D0EE` | 4.68:1 | 4.5:1 |
| Highlights | weakest syntax colour (yellow) `#724F00` | inactive selection `#D4E3F5` | 5.68:1 | 4.5:1 |
| Highlights | weakest syntax colour (yellow) `#724F00` | current find match `#E3CAA2` | 4.67:1 | 4.5:1 |
| Highlights | weakest syntax colour (yellow) `#724F00` | other find matches `#EFDFC4` | 5.65:1 | 4.5:1 |
| Highlights | weakest syntax colour (yellow) `#724F00` | word highlight `#D4E3F5` | 5.68:1 | 4.5:1 |
| Highlights | weakest syntax colour (yellow) `#724F00` | line highlight `#E9F0F9` | 6.46:1 | 4.5:1 |
| Highlights | weakest syntax colour (yellow) `#724F00` | diff: inserted line `#D0E7CF` | 5.65:1 | 4.5:1 |
| Highlights | weakest syntax colour (yellow) `#724F00` | diff: inserted text `#AFD8AF` | 4.68:1 | 4.5:1 |
| Highlights | weakest syntax colour (yellow) `#724F00` | diff: removed line `#FCD9D5` | 5.65:1 | 4.5:1 |
| Highlights | weakest syntax colour (yellow) `#724F00` | diff: removed text `#FABFB9` | 4.66:1 | 4.5:1 |
| Highlights | weakest syntax colour (yellow) `#724F00` | merge conflict `#C2DFC1` | 5.16:1 | 4.5:1 |
| Highlights | weakest syntax colour (yellow) `#724F00` | debug stack frame `#EAD5B3` | 5.18:1 | 4.5:1 |
| Highlight visibility | selection `#B7D0EE` | editor `#FAF9F6` | 1.50:1 | advisory |
| Highlight visibility | current find match `#E3CAA2` | editor `#FAF9F6` | 1.51:1 | advisory |
| Highlight visibility | diff: inserted text `#AFD8AF` | editor `#FAF9F6` | 1.50:1 | advisory |
| Highlight visibility | diff: removed text `#FABFB9` | editor `#FAF9F6` | 1.51:1 | advisory |
| Highlight visibility | active list row `#BBCFE7` | side bar `#FFFFFF` | 1.59:1 | advisory |
| Highlight visibility | hovered list row `#CBDAED` | side bar `#FFFFFF` | 1.42:1 | advisory |
