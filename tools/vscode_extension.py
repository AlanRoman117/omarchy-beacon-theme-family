"""Generate vscode-extension/: all six Beacon VS Code themes as one extension.

Omarchy applies each theme's vscode-theme.json under one shared VS Code theme
name, "Omarchy", so VS Code needs a window reload after every switch. This
extension gives each variant its own name ("Beacon Dark", ...). Paired with
tools/omarchy-hooks/beacon-vscode.sh, Omarchy theme switches then apply live.

The theme files are built by the same vscode.build() call verify.py checks, so
the extension cannot drift from the verified numbers or from the files the
Omarchy themes ship.
"""
import json, os, shutil
from PIL import Image, ImageDraw
from verify import VARIANTS, build, OUT, ROOT
import vscode

EXT = os.path.join(ROOT, "vscode-extension")
NAME = "beacon-themes"
PUBLISHER = "AlanRoman117"
VERSION = "0.1.0"
FAMILY = "https://github.com/AlanRoman117/omarchy-beacon-theme-family"

TAGLINE = {
    "dark": "typical colour vision",
    "light": "typical colour vision",
    "redgreen-dark": "protanopia and deuteranopia",
    "redgreen-light": "protanopia and deuteranopia",
    "blueyellow-dark": "tritanopia",
    "blueyellow-light": "tritanopia",
}

README = """# Beacon Themes

Six high-contrast colour themes for VS Code, VSCodium and Cursor: a dark and a
light default, plus red-green safe and blue-yellow safe variants of each.

Every colour is solved for a contrast target rather than picked by eye, then
checked against WCAG 2.2, APCA and simulated colour vision deficiency. All
resting text, including comments, line numbers and every syntax colour, is at
least 7:1 against its background.

| Theme | Tuned for |
|---|---|
{rows}

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
the [Beacon family repository]({family}).
"""


def icon(p, path):
    """256x256 swatch: background, a bright border and the six slots as bars."""
    size = 256
    img = Image.new("RGB", (size, size), p["background"])
    d = ImageDraw.Draw(img)
    d.rounded_rectangle([12, 12, size - 13, size - 13], radius=36,
                        outline=p["accent"], width=10)
    slots = ["red", "orange", "yellow", "green", "blue", "magenta"]
    bw = (size - 80) / len(slots)
    for i, s in enumerate(slots):
        x = 40 + i * bw
        d.rectangle([x + 4, 70, x + bw - 4, 186], fill=p[s])
    img.save(path, optimize=True)


def main():
    if os.path.isdir(EXT):
        shutil.rmtree(EXT)
    os.makedirs(os.path.join(EXT, "themes"))

    contributes, rows = [], []
    for name, spec in VARIANTS.items():
        p = build(spec)
        theme, checks = vscode.build(p, spec["mode"], name)
        failed = [c for c in checks if c[5] is not None and c[6] < c[5]]
        if failed:
            raise SystemExit(f"{name}: VS Code theme failed verification; run verify.py")
        slug = name.replace("omarchy-", "").replace("-theme", "")
        rel = f"./themes/{slug}.json"
        with open(os.path.join(EXT, rel), "w") as f:
            json.dump(theme, f, indent=4)
            f.write("\n")
        contributes.append({"label": theme["name"],
                            "uiTheme": "vs-dark" if spec["mode"] == "dark" else "vs",
                            "path": rel})
        rows.append(f"| {theme['name']} | {TAGLINE[slug.replace('beacon-', '')]} |")
        if name == "omarchy-beacon-dark-theme":
            icon(p, os.path.join(EXT, "icon.png"))

    package = {
        "name": NAME,
        "displayName": "Beacon Themes",
        "description": "High-contrast themes solved for WCAG AAA, with red-green "
                       "and blue-yellow safe variants for colour vision deficiency.",
        "version": VERSION,
        "publisher": PUBLISHER,
        "license": "MIT",
        "icon": "icon.png",
        "engines": {"vscode": "^1.70.0"},
        "categories": ["Themes"],
        "keywords": ["high contrast", "low vision", "colour vision deficiency",
                     "color blind", "protanopia", "deuteranopia", "tritanopia",
                     "wcag", "omarchy"],
        "galleryBanner": {"color": "#10141A", "theme": "dark"},
        "repository": {"type": "git", "url": FAMILY + ".git"},
        "contributes": {"themes": contributes},
    }
    with open(os.path.join(EXT, "package.json"), "w") as f:
        json.dump(package, f, indent=2)
        f.write("\n")

    with open(os.path.join(EXT, "README.md"), "w") as f:
        f.write(README.format(rows="\n".join(rows), family=FAMILY))
    with open(os.path.join(EXT, "CHANGELOG.md"), "w") as f:
        f.write(f"# Changelog\n\n## {VERSION}\n\n- First build: six Beacon themes.\n")
    shutil.copy(os.path.join(ROOT, "LICENSE"), os.path.join(EXT, "LICENSE"))
    with open(os.path.join(EXT, ".vscodeignore"), "w") as f:
        f.write("*.vsix\n")
    print(f"extension written: {EXT} ({len(contributes)} themes)")


if __name__ == "__main__":
    main()
