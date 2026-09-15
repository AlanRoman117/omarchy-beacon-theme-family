# Beacon Themes

Six high-contrast colour themes for VS Code, VSCodium and Cursor: a dark and a
light default, plus red-green safe and blue-yellow safe variants of each.

Every colour is solved for a contrast target rather than picked by eye, then
checked against WCAG 2.2, APCA and simulated colour vision deficiency. All
resting text, including comments, line numbers and every syntax colour, is at
least 7:1 against its background.

| Theme | Tuned for |
|---|---|
| Beacon Dark | typical colour vision |
| Beacon Red-Green Dark | protanopia and deuteranopia |
| Beacon Blue-Yellow Dark | tritanopia |
| Beacon Light | typical colour vision |
| Beacon Red-Green Light | protanopia and deuteranopia |
| Beacon Blue-Yellow Light | tritanopia |

Beacon helps people with **low vision** and **colour vision deficiency**. It
does not add screen reader support; that is outside what a colour theme can do.

## Which one?

- **Have you ever had trouble telling red from green?** Use a Red-Green theme.
- **Blue from green, or yellow from pink?** Use a Blue-Yellow theme. These
  deliberately leave red and green close, so they are worse than the default
  for red-green colour vision deficiency.
- **Neither?** Use Beacon Dark or Beacon Light.

## What is deliberately not AAA

Highlighted text (selection, find matches, diff highlights) is held at 4.5:1
rather than 7:1. A highlight has to move toward the text colour to be visible
at all; at 7:1 it would be invisible. On the Red-Green themes, diff inserted and
removed highlights differ by hue only, so read the gutter `+`/`-` markers and
bars there.

## Using Beacon with Omarchy

Omarchy applies its themes to VS Code under a single theme name, so VS Code
normally needs **Developer: Reload Window** after every theme switch. With this
extension installed, add the Beacon hook once and switching becomes live:

```bash
curl -fsSL -o /tmp/beacon-vscode.sh https://raw.githubusercontent.com/AlanRoman117/omarchy-beacon-theme-family/main/tools/omarchy-hooks/beacon-vscode.sh
omarchy hook install theme-set /tmp/beacon-vscode.sh
```

Read the script first if you like; it is about sixty lines and only edits the
`workbench.colorTheme` line of VS Code, VSCodium or Cursor settings.

The hook only acts on Beacon themes and only when this extension is installed.
Every other Omarchy theme keeps working exactly as before.

The full verification report and the tools that generate these themes are in
the [Beacon family repository](https://github.com/AlanRoman117/omarchy-beacon-theme-family).
