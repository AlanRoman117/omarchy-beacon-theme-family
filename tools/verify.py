"""Generate the six Omarchy accessible theme variants and a verification report.

Design method
-------------
1. Six chromatic hues per variant are chosen for the target vision type
   (Okabe-Ito informed: vermilion rather than crimson, bluish-green rather
   than grass, etc).
2. A fixed ladder of WCAG contrast targets is assigned across those six hues
   by brute-force search over all 720 permutations, maximising the minimum
   perceptual distance between the semantically important pairs under the
   simulated vision type. Lightness is the only channel a dichromat keeps,
   so contrast targets *are* the separation mechanism.
3. Each colour's Oklch lightness is then solved by binary search so it hits
   its contrast target exactly. Compliance is true by construction, not by
   inspection.
"""
import os, itertools, json
from colorlib import *
import vscode

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
OUT = os.path.join(ROOT, "themes")

# Pairs whose confusion actually costs a user something: git diff, test
# output, log levels, diagnostics. Held to a higher bar than the merely
# decorative combinations.
PRIORITY_PAIRS = [
    ("red", "green"),
    ("red", "yellow"),
    ("green", "cyan"),
    ("red", "blue"),
    ("yellow", "green"),
]

DARK_NEUTRALS = dict(
    background="#10141A",
    darker_background="#05070B",
    dark_background="#0A0E13",
    lighter_background="#1B2029",
    bright_foreground="#FFFFFF",
    light_foreground="#EDF1F6",
    foreground="#D8DFE8",
    dark_foreground="#A3AEBD",
    color0="#1B2029",
    color7="#D8DFE8",
    color15="#FFFFFF",
)

LIGHT_NEUTRALS = dict(
    background="#FAF9F6",
    lighter_background="#FFFFFF",
    dark_background="#F1EFE9",
    darker_background="#E3E0D8",
    bright_foreground="#0F0F0E",
    light_foreground="#1C1C1A",
    foreground="#2B2B28",
    dark_foreground="#4E4E49",
    color0="#E3E0D8",
    color7="#2B2B28",
    color15="#0F0F0E",
)

DARK_LADDER = [7.2, 8.8, 10.4, 12.0, 13.6, 15.2]

# A colour that has been pushed so far up (or down) the lightness axis that its
# chroma is gamut-crushed stops reading as a hue at all: "green" becomes white,
# "cyan" becomes black. Any assignment that does that to a slot is rejected
# outright, which is what keeps an AAA palette from turning into greyscale.
CHROMA_FLOOR = {"dark": 0.055, "light": 0.055}
LIGHT_LADDER = [7.0, 8.2, 9.4, 10.6, 11.8, 13.0]

VARIANTS = {
    "omarchy-beacon-dark-theme": dict(
        mode="dark", accent_slot="blue", optimise=("normal",),
        hues={"red": (25, 0.155), "green": (150, 0.155), "yellow": (90, 0.160),
              "blue": (255, 0.150), "magenta": (340, 0.150), "cyan": (205, 0.125),
              "orange": (55, 0.150)},
        blurb="Neutral high-contrast dark. The full hue range, tuned for normal "
              "colour vision. If red and green are hard to tell apart, use the "
              "protan-deutan variant instead; this one does not solve that.",
    ),
    "omarchy-beacon-redgreen-dark-theme": dict(
        mode="dark", accent_slot="blue", optimise=("protan", "deutan"),
        hues={"red": (38, 0.150), "green": (172, 0.115), "yellow": (88, 0.160),
              "blue": (256, 0.150), "magenta": (322, 0.140), "cyan": (215, 0.105),
              "orange": (62, 0.150)},
        blurb="Red-green safe dark. Red shifts to vermilion and green to "
              "bluish-green, then the two are pulled apart by lightness for the "
              "protan worst case.",
    ),
    "omarchy-beacon-blueyellow-dark-theme": dict(
        mode="dark", accent_slot="red", optimise=("tritan",),
        hues={"red": (25, 0.160), "green": (145, 0.150), "yellow": (85, 0.160),
              "blue": (258, 0.145), "magenta": (348, 0.140), "cyan": (196, 0.110),
              "orange": (55, 0.155)},
        blurb="Blue-yellow safe dark. Red and green stay trustworthy here, so the "
              "work goes into separating blue from green and yellow from magenta.",
    ),
    "omarchy-beacon-light-theme": dict(
        mode="light", accent_slot="blue", optimise=("normal",),
        hues={"red": (25, 0.160), "green": (150, 0.130), "yellow": (78, 0.130),
              "blue": (255, 0.150), "magenta": (340, 0.150), "cyan": (210, 0.120),
              "orange": (50, 0.145)},
        blurb="Neutral high-contrast light. The full hue range, tuned for normal "
              "colour vision. If red and green are hard to tell apart, use the "
              "protan-deutan variant instead; this one does not solve that.",
    ),
    "omarchy-beacon-redgreen-light-theme": dict(
        mode="light", accent_slot="blue", optimise=("protan", "deutan"),
        hues={"red": (38, 0.155), "green": (172, 0.110), "yellow": (78, 0.130),
              "blue": (256, 0.150), "magenta": (322, 0.145), "cyan": (215, 0.110),
              "orange": (58, 0.145)},
        blurb="Red-green safe light. Red shifts to vermilion and green to "
              "bluish-green, then the two are pulled apart by lightness for the "
              "protan worst case.",
    ),
    "omarchy-beacon-blueyellow-light-theme": dict(
        mode="light", accent_slot="red", optimise=("tritan",),
        hues={"red": (25, 0.160), "green": (145, 0.140), "yellow": (80, 0.130),
              "blue": (258, 0.150), "magenta": (348, 0.145), "cyan": (196, 0.115),
              "orange": (52, 0.145)},
        blurb="Blue-yellow safe light. Red and green stay trustworthy here, so the "
              "work goes into separating blue from green and yellow from magenta.",
    ),
}

SLOTS = ["red", "green", "yellow", "blue", "magenta", "cyan"]
ANSI_INDEX = {"red": 1, "green": 2, "yellow": 3, "blue": 4, "magenta": 5, "cyan": 6}


def score(assign, spec, bg, darker, ladder, cache):
    hexes = {}
    for s in SLOTS:
        key = (s, assign[s])
        if key not in cache:
            cache[key] = solve_for_contrast(*spec["hues"][s], bg,
                                            ladder[assign[s]], darker)
        hexes[s] = cache[key]
    floor = CHROMA_FLOOR[spec["mode"]]
    if any(hex_to_oklch(h)[1] < floor for h in hexes.values()):
        return -1.0, -1.0, hexes
    pri, allp = 1e9, 1e9
    for a, b in itertools.combinations(SLOTS, 2):
        worst = 1e9
        for kind in spec["optimise"]:
            ca, cb = hexes[a], hexes[b]
            if kind != "normal":
                ca, cb = simulate(ca, kind), simulate(cb, kind)
            worst = min(worst, oklab_distance(ca, cb))
        allp = min(allp, worst)
        if (a, b) in PRIORITY_PAIRS or (b, a) in PRIORITY_PAIRS:
            pri = min(pri, worst)
    return pri, allp, hexes


def plausible(assign, mode):
    """Keep colours recognisable as themselves.

    Rank 0 is the lowest contrast target: the darkest colour on a dark
    background, the lightest on a light one. Yellow must never be the darkest
    thing on screen and red must never be the palest.
    """
    y, r = assign["yellow"], assign["red"]
    return (y >= 3 and r <= 2) if mode == "dark" else (y <= 2 and r >= 3)


def optimise(spec):
    bg = (DARK_NEUTRALS if spec["mode"] == "dark" else LIGHT_NEUTRALS)["background"]
    ladder = DARK_LADDER if spec["mode"] == "dark" else LIGHT_LADDER
    darker = spec["mode"] == "light"
    cache, best = {}, None
    for perm in itertools.permutations(range(6)):
        assign = dict(zip(SLOTS, perm))
        if not plausible(assign, spec["mode"]):
            continue
        pri, allp, hexes = score(assign, spec, bg, darker, ladder, cache)
        key = (round(pri, 4), round(allp, 4))
        if best is None or key > best[0]:
            best = (key, assign, hexes)
    return best


def solve_orange(spec, bg, darker, normals, ladder):
    """Place orange without disturbing the six optimised slots.

    Omarchy's app templates expect an `orange` and substitute yellow when a
    theme has none, which silently merges numbers with types in VS Code and
    elsewhere. Orange is solved afterwards, on its own: every contrast target
    across the ladder's range is tried, and the one that keeps orange furthest
    from its nearest neighbour under the variant's vision types wins. The six
    slots, and every number already verified for them, stay exactly as they were.
    """
    h, c = spec["hues"]["orange"]
    floor = CHROMA_FLOOR[spec["mode"]]
    best, t = None, ladder[0]
    while t <= ladder[-1] + 1e-9:
        cand = solve_for_contrast(h, c, bg, t, darker)
        if hex_to_oklch(cand)[1] >= floor:
            near = nearest(cand, normals, spec["optimise"])
            if best is None or near[0] > best[0][0]:
                best = (near, cand)
        t = round(t + 0.1, 2)
    return best[1], best[0]


def nearest(hexv, normals, kinds):
    """(distance, slot, vision) of the slot closest to hexv under any of kinds."""
    out = None
    for kind in kinds:
        a = hexv if kind == "normal" else simulate(hexv, kind)
        for s in SLOTS:
            b = normals[s] if kind == "normal" else simulate(normals[s], kind)
            d = oklab_distance(a, b)
            if out is None or d < out[0]:
                out = (d, s, kind)
    return out


def build(spec):
    n = dict(DARK_NEUTRALS if spec["mode"] == "dark" else LIGHT_NEUTRALS)
    bg = n["background"]
    darker = spec["mode"] == "light"
    (pri, allp), assign, normals = optimise(spec)
    ladder = DARK_LADDER if spec["mode"] == "dark" else LIGHT_LADDER

    # Bright variants are the same hue, one notch more readable. The bump is
    # backed off rather than applied blindly, so a bright colour never washes
    # out past the chroma floor just to gain contrast it does not need.
    floor = CHROMA_FLOOR[spec["mode"]] * 0.9
    brights = {}
    for s in SLOTS:
        h, c = spec["hues"][s]
        base = ladder[assign[s]]
        for bump in (1.8, 1.4, 1.0, 0.6, 0.3):
            cand = solve_for_contrast(h, min(c + 0.02, 0.33), bg, base + bump, darker)
            if hex_to_oklch(cand)[1] >= floor:
                break
        brights[s] = cand

    # muted / ANSI color8 carries comment text, so it clears AAA like any text
    n["muted"] = solve_for_contrast(230, 0.018, bg, 7.05, darker)
    # selection band: hold selected text at AAA, then take as much band edge
    # contrast as that allows
    n["selection"] = solve_for_contrast(255, 0.045, n["bright_foreground"],
                                        7.1, not darker)

    out = dict(n)
    out.update(normals)
    for s, v in normals.items():
        out[f"color{ANSI_INDEX[s]}"] = v
    for s, v in brights.items():
        out[f"bright_{s}"] = v
        out[f"color{ANSI_INDEX[s] + 8}"] = v
    out["color8"] = n["muted"]
    out["accent"] = normals[spec["accent_slot"]]
    out["inactive_border"] = solve_for_contrast(250, 0.02, bg, 3.5, darker)
    out["orange"], out["_orange_nearest"] = solve_orange(spec, bg, darker,
                                                         normals, ladder)
    out["_normals"], out["_brights"], out["_scores"] = normals, brights, (pri, allp)
    return out


COLORS_TPL = """# {name}
#
# {blurb}
#
# Every value here is machine-verified before release: WCAG 2.2
# relative-luminance contrast, APCA Lc (which WCAG 2.x gets wrong on dark
# backgrounds), and Machado et al. (2009) simulation of protanopia,
# deuteranopia and tritanopia. Run tools/verify.py to reproduce the numbers.

mode = "{mode}"

accent    = "{accent}"
selection = "{selection}"
muted     = "{muted}"

background         = "{background}"
dark_background    = "{dark_background}"
darker_background  = "{darker_background}"
lighter_background = "{lighter_background}"

foreground        = "{foreground}"
dark_foreground   = "{dark_foreground}"
light_foreground  = "{light_foreground}"
bright_foreground = "{bright_foreground}"

red     = "{red}"
green   = "{green}"
yellow  = "{yellow}"
blue    = "{blue}"
magenta = "{magenta}"
cyan    = "{cyan}"
orange  = "{orange}"

bright_red     = "{bright_red}"
bright_green   = "{bright_green}"
bright_yellow  = "{bright_yellow}"
bright_blue    = "{bright_blue}"
bright_magenta = "{bright_magenta}"
bright_cyan    = "{bright_cyan}"

# ANSI 16. color8 is `muted`, per Omarchy convention.
color0  = "{color0}"
color1  = "{color1}"
color2  = "{color2}"
color3  = "{color3}"
color4  = "{color4}"
color5  = "{color5}"
color6  = "{color6}"
color7  = "{color7}"
color8  = "{color8}"
color9  = "{color9}"
color10 = "{color10}"
color11 = "{color11}"
color12 = "{color12}"
color13 = "{color13}"
color14 = "{color14}"
color15 = "{color15}"

# Window borders. The active border is a flat accent rather than a gradient so
# every pixel of it clears 3:1 against the desktop (WCAG 1.4.11, and 2.4.13
# Focus Appearance). A gradient dips below threshold at one end.
hyprland_active_border   = "{accent}"
hyprland_inactive_border = "{inactive_border}"
"""


def report(name, spec, p):
    bg = p["background"]
    L = [f"## `{name}`", "", spec["blurb"], "",
         f"Background `{bg}`, mode `{spec['mode']}`.", "",
         "| Role | Hex | WCAG vs bg | Level | APCA Lc |", "|---|---|---|---|---|"]
    rows = [("foreground", p["foreground"]),
            ("light_foreground", p["light_foreground"]),
            ("bright_foreground", p["bright_foreground"]),
            ("dark_foreground", p["dark_foreground"]),
            ("muted / color8", p["muted"]),
            ("accent", p["accent"])]
    rows += [(s, p["_normals"][s]) for s in SLOTS]
    rows += [("bright_" + s, p["_brights"][s]) for s in SLOTS]
    rows += [("orange", p["orange"])]
    worst = 99.0
    for role, hexv in rows:
        cr = contrast(hexv, bg)
        worst = min(worst, cr)
        lvl = "AAA" if cr >= 7 else ("AA" if cr >= 4.5 else "FAIL")
        L.append(f"| {role} | `{hexv}` | {cr:.2f}:1 | {lvl} | {apca_lc(hexv, bg):+.0f} |")
    L += ["",
          f"- Lowest contrast of any palette colour against the background: "
          f"**{worst:.2f}:1** (AAA threshold is 7:1)",
          f"- Selected text, `bright_foreground` on `selection`: "
          f"**{contrast(p['bright_foreground'], p['selection']):.2f}:1**",
          f"- Selection band against background: {contrast(p['selection'], bg):.2f}:1",
          f"- Active window border against background: "
          f"{contrast(p['accent'], bg):.2f}:1 (1.4.11 needs 3:1)",
          f"- Inactive window border against background: "
          f"{contrast(p['inactive_border'], bg):.2f}:1",
          f"- `orange` sits outside the six-slot optimisation and does not move "
          f"them. Its nearest slot is {p['_orange_nearest'][1]} under "
          f"{p['_orange_nearest'][2]} vision, Oklab distance "
          f"{p['_orange_nearest'][0]:.3f}",
          ""]
    L += ["Perceptual separation between the six chromatic slots under simulated "
          "colour vision deficiency (Machado 2009 at full severity, Oklab "
          "distance). Arrows mark the vision types this variant is tuned for.", "",
          "| Vision | Weakest pair overall | Weakest priority pair |",
          "|---|---|---|"]
    for kind in ("normal", "protan", "deutan", "tritan"):
        allw = prw = None
        for a, b in itertools.combinations(SLOTS, 2):
            ca, cb = p["_normals"][a], p["_normals"][b]
            if kind != "normal":
                ca, cb = simulate(ca, kind), simulate(cb, kind)
            d = oklab_distance(ca, cb)
            if allw is None or d < allw[0]:
                allw = (d, a, b)
            if ((a, b) in PRIORITY_PAIRS or (b, a) in PRIORITY_PAIRS) and \
               (prw is None or d < prw[0]):
                prw = (d, a, b)
        mark = " <-" if kind in spec["optimise"] else ""
        L.append(f"| {kind}{mark} | {allw[1]}/{allw[2]} {allw[0]:.3f} | "
                 f"{prw[1]}/{prw[2]} {prw[0]:.3f} |")
    L.append("")
    return "\n".join(L), worst


def vscode_report(checks):
    L = ["### VS Code (`vscode-theme.json`)", "",
         "Every text and indicator pair the generated VS Code theme creates. "
         "Translucent highlights are measured as composited over the editor "
         "background. Rows marked advisory carry no requirement.", "",
         "| Area | Foreground | On | Contrast | Needs |", "|---|---|---|---|---|"]
    for area, fl, fv, bl, bv, need, cr in checks:
        req = "advisory" if need is None else f"{need:g}:1"
        L.append(f"| {area} | {fl} `{fv}` | {bl} `{bv}` | {cr:.2f}:1 | {req} |")
    return L


def main():
    os.makedirs(OUT, exist_ok=True)
    reps = []
    for name, spec in VARIANTS.items():
        p = build(spec)
        d = os.path.join(OUT, name)
        os.makedirs(os.path.join(d, "backgrounds"), exist_ok=True)

        theme, checks = vscode.build(p, spec["mode"], name)
        failed = [c for c in checks if c[5] is not None and c[6] < c[5]]
        if failed:
            for area, fl, fv, bl, bv, need, cr in failed:
                print(f"FAIL {name}: {area}: {fl} {fv} on {bl} {bv} "
                      f"{cr:.2f}:1 < {need}:1")
            raise SystemExit("VS Code theme failed verification; nothing written.")

        fields = {k: v for k, v in p.items() if not k.startswith("_")}
        fields.update(name=name, blurb=spec["blurb"], mode=spec["mode"])
        with open(os.path.join(d, "colors.toml"), "w") as f:
            f.write(COLORS_TPL.format(**fields))
        with open(os.path.join(d, "vscode-theme.json"), "w") as f:
            json.dump(theme, f, indent=4)
            f.write("\n")
        if spec["mode"] == "light":
            open(os.path.join(d, "light.mode"), "w").close()
        r, worst = report(name, spec, p)
        r += "\n" + "\n".join(vscode_report(checks)) + "\n"
        reps.append(r)
        print(f"{name:42s} worst {worst:5.2f}:1  pri {p['_scores'][0]:.3f}  "
              f"all {p['_scores'][1]:.3f}")
    return reps


if __name__ == "__main__":
    reps = main()
    with open(os.path.join(ROOT, "CONTRAST-REPORT.md"), "w") as f:
        f.write("# Verification report\n\n"
                "Regenerate with `python3 tools/verify.py`.\n\n" + "\n\n".join(reps))
