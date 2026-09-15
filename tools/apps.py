"""Verify the app themes Omarchy generates from Beacon's palettes.

Omarchy renders $OMARCHY_PATH/default/themed/*.tpl from colors.toml for every
theme: btop, Helix, Obsidian, Pi, Claude, T3 Code, Hermes and the share picker
among them. Those templates were written for stock palettes, and nothing checked
them against Beacon's contrast guarantees. btop's selected row, for one, drew
the accent on the selection band at 3.4-4.7:1.

This renders every in-scope template exactly the way Omarchy does, measures the
pairs people have to read, and writes a patched copy into the theme only for
apps that fail. A theme-provided file survives the install filter, and Omarchy's
template step never overwrites a file the theme already ships. Apps that pass
ship nothing and keep Omarchy's generated file.

Fixes never invent colours: they swap in a palette role, or a surface that
tools/vscode.py already solved and verified (selection rows, diff lines).

Omarchy-only: needs `omarchy-theme-color` and the installed templates. Run it
after `omarchy update`, because a shipped file freezes the template as of the
last run.

    python3 tools/apps.py            # audit, patch, write APPS-REPORT.md
    python3 tools/apps.py --parity   # prove the renderer matches Omarchy
"""
import os, re, subprocess, sys
from colorlib import contrast, hex_to_rgb
from verify import VARIANTS, build, OUT, ROOT
import vscode

TEMPLATES = os.path.join(os.environ.get("OMARCHY_PATH", "/usr/share/omarchy"),
                         "default", "themed")
USER_TEMPLATES = os.path.expanduser("~/.config/omarchy/themed")
STAGED = os.path.expanduser("~/.local/state/omarchy/current/theme")
TEXT, HIGHLIGHT, NONTEXT = vscode.TEXT, vscode.HIGHLIGHT, vscode.NONTEXT

HEX = r"#[0-9A-Fa-f]{6}"
JSON_SLOT = rf'"(?P<key>[A-Za-z0-9_]+)": "(?P<hex>{HEX})"'


# ---------------------------------------------------------------- rendering

def theme_colors(colors_toml):
    """Resolved key -> value, exactly as Omarchy's templates receive them."""
    try:
        out = subprocess.run(["omarchy-theme-color", "--file", colors_toml, "--all"],
                             capture_output=True, text=True, check=True).stdout
    except (OSError, subprocess.CalledProcessError) as e:
        raise SystemExit(f"omarchy-theme-color failed ({e}); apps.py needs Omarchy")
    return dict(line.split("\t", 1) for line in out.splitlines() if "\t" in line)


def mix_color(start, end, amount):
    """Port of mix_color in omarchy-theme-set-templates, awk rounding included."""
    amount = amount.strip()
    if amount.endswith("%"):
        a = float(amount[:-1]) / 100
    else:
        a = float(amount)
        a = a / 100 if a > 1 else a
    a = min(max(a, 0.0), 1.0)
    s = [int(start.lstrip("#")[i:i + 2], 16) for i in (0, 2, 4)]
    e = [int(end.lstrip("#")[i:i + 2], 16) for i in (0, 2, 4)]
    return "#" + "".join(f"{int(s[i] * (1 - a) + e[i] * a + 0.5):02x}" for i in range(3))


def render(tpl_text, colors):
    """Port of the sed script: plain keys, _strip and _rgb variants, then mix."""
    out = tpl_text
    for key, value in colors.items():
        out = out.replace("{{ %s }}" % key, value)
        out = out.replace("{{ %s_strip }}" % key, value.lstrip("#"))
        if re.fullmatch(HEX, value):
            rgb = ",".join(str(int(c * 255 + 0.5)) for c in hex_to_rgb(value))
            out = out.replace("{{ %s_rgb }}" % key, rgb)

    def mix(m):
        fn, a, b, amount = m.group(1), m.group(2), m.group(3), m.group(4)
        start, end = colors.get(a, ""), colors.get(b, "")
        if not (re.fullmatch(HEX, start) and re.fullmatch(HEX, end)):
            return m.group(0)
        v = mix_color(start, end, amount)
        if fn == "mix_strip":
            return v.lstrip("#")
        if fn == "mix_rgb":
            return ",".join(str(int(v[i:i + 2], 16)) for i in (1, 3, 5))
        return v

    return re.sub(r"\{\{\s*(mix(?:_strip|_rgb)?)\s+([A-Za-z0-9_]+)\s+([A-Za-z0-9_]+)"
                  r"\s+([0-9]+(?:\.[0-9]+)?%?)\s*\}\}", mix, out)


def template_path(name):
    user = os.path.join(USER_TEMPLATES, name + ".tpl")
    return user if os.path.isfile(user) else os.path.join(TEMPLATES, name + ".tpl")


# ---------------------------------------------------------------- app specs
#
# Each app: a slot regex (named groups key and hex), checks as
# (area, fg, bg, minimum) where fg/bg are slot names or "@role" palette/surface
# names, and fixes: slot -> candidate roles, tried in order.

SELECT_TEXT = ["@bright_foreground", "@foreground"]
MUTED_TEXT = ["@dark_foreground", "@muted", "@foreground"]

APPS = {
    "btop.theme": dict(
        slot=rf'theme\[(?P<key>[a-z_0-9]+)\]="(?P<hex>{HEX})"',
        checks=[("Text", k, "main_bg", TEXT) for k in
                ("main_fg", "title", "hi_fg", "inactive_fg", "graph_text", "proc_misc")]
        + [("Selected process row", "selected_fg", "selected_bg", TEXT)]
        + [("Box outlines", k, "main_bg", NONTEXT) for k in
           ("cpu_box", "mem_box", "net_box", "proc_box", "div_line")],
        fixes={"selected_fg": SELECT_TEXT, "inactive_fg": MUTED_TEXT},
    ),
    "helix.toml": dict(
        slot=rf'^(?P<key>[a-z_0-9]+) = "(?P<hex>{HEX})"',
        checks=[("Syntax and text", k, "background", TEXT) for k in
                ("foreground", "color1", "color2", "color3", "color4", "color5",
                 "color6", "color8")]
        + [("Statusline band", "background", k, TEXT) for k in
           ("foreground", "color8", "color4", "color2", "color5")]
        + [("Selection", "selection_foreground", "selection_background", TEXT),
           ("Cursor", "background", "cursor", TEXT),
           ("Focused text", "foreground", "lighter_background", TEXT),
           ("Menu selection", "background", "foreground", TEXT)]
        + [("Cursor line and highlights", k, "lighter_background", HIGHLIGHT) for k in
           ("color1", "color2", "color3", "color4", "color5", "color6", "color8")],
        fixes={"selection_foreground": SELECT_TEXT, "lighter_background": ["@row_hover"]},
    ),
    "pi.json": dict(
        slot=JSON_SLOT,
        checks=[("Text", k, "background", TEXT) for k in
                ("foreground", "accent", "color1", "color2", "color3", "color4",
                 "color5", "color6", "color8", "mutedText", "dimText")]
        + [("Message panels", "foreground", k, TEXT) for k in
           ("panel", "panelAlt", "selectedBackground", "panelPending",
            "panelSuccess", "panelError")]
        + [("Tool titles", "accent", k, TEXT) for k in
           ("panelPending", "panelSuccess", "panelError")]
        + [("Input border", "border", "background", NONTEXT)],
        fixes={"mutedText": MUTED_TEXT, "dimText": ["@muted", "@dark_foreground"],
               "panel": ["@row_hover"], "panelAlt": ["@row_hover"],
               "selectedBackground": ["@row_active"], "panelPending": ["@row_hover"],
               "panelSuccess": ["@diff_add_line", "@row_hover"],
               "panelError": ["@diff_del_line", "@row_hover"],
               "border": ["@border"]},
    ),
    "claude.json": dict(
        slot=JSON_SLOT,
        checks=[("Text", k, "@background", TEXT) for k in
                ("text", "subtle", "inactive", "suggestion", "permission", "remember",
                 "success", "error", "warning", "merged", "planMode", "autoAccept",
                 "claude")]
        + [("Badges", "inverseText", "claude", TEXT)]
        + [("Message backgrounds", "text", k, TEXT) for k in
           ("userMessageBackground", "userMessageBackgroundHover",
            "bashMessageBackgroundColor", "memoryBackgroundColor")]
        + [("Diff lines", "text", k, TEXT) for k in ("diffAdded", "diffRemoved")]
        + [("Diff words and selection", "text", k, HIGHLIGHT) for k in
           ("diffAddedWord", "diffRemovedWord", "selectionBg")]
        + [("Prompt border", "promptBorder", "@background", NONTEXT)],
        fixes={"inactive": MUTED_TEXT,
               "userMessageBackground": ["@row_hover"],
               "userMessageBackgroundHover": ["@row_active"],
               "bashMessageBackgroundColor": ["@row_hover"],
               "memoryBackgroundColor": ["@row_hover"],
               "diffAdded": ["@diff_add_line"], "diffRemoved": ["@diff_del_line"],
               "diffAddedWord": ["@diff_add_text"], "diffRemovedWord": ["@diff_del_text"],
               "selectionBg": ["@selection_hl", "@row_active"]},
    ),
    "t3code.json": dict(
        slot=JSON_SLOT,
        checks=[("Text", "text", "chrome", TEXT),
                ("Toolbar", "toolbarForeground", "toolbar", TEXT),
                ("Sidebar", "sidebarForeground", "sidebar", TEXT),
                ("Code", "codeForeground", "codeBackground", TEXT),
                ("Terminal", "terminalForeground", "terminalBackground", TEXT),
                ("Status text", "error", "chrome", TEXT),
                ("Status text", "warning", "chrome", TEXT)]
        + [("Sidebar rows", "sidebarForeground", k, TEXT) for k in
           ("sidebarRowHover", "sidebarRowActive", "sidebarRowSelected")]
        + [("Terminal selection", "terminalForeground", "terminalSelection", HIGHLIGHT)]
        + [("Borders and focus", k, "chrome", NONTEXT) for k in
           ("border", "toolbarBorder", "focus")]
        + [("Borders and focus", "sidebarBorder", "sidebar", NONTEXT)],
        fixes={"sidebarRowHover": ["@row_hover"], "sidebarRowActive": ["@row_active"],
               "sidebarRowSelected": ["@row_active"],
               "terminalSelection": ["@selection_hl", "@row_active"],
               "error": ["@red", "@bright_red"], "warning": ["@yellow", "@bright_yellow"]},
    ),
    "hermes.yaml": dict(
        slot=rf'^\s+(?P<key>[a-z_]+): "(?P<hex>{HEX})"',
        checks=[("Text", k, "background", TEXT) for k in
                ("ui_text", "ui_primary", "ui_label", "ui_ok", "ui_warn", "ui_error",
                 "ui_tool", "ui_thinking", "banner_title", "banner_dim", "banner_text",
                 "prompt", "shell_dollar", "session_label", "syntax_string",
                 "syntax_number", "syntax_keyword", "syntax_comment",
                 "diff_added_word", "diff_removed_word")]
        + [("Status bar", k, "status_bar_bg", TEXT) for k in
           ("status_bar_text", "status_bar_strong", "status_bar_dim", "status_bar_good",
            "status_bar_warn", "status_bar_bad", "status_bar_critical")]
        + [("Completion menu", "ui_text", k, TEXT) for k in
           ("completion_menu_bg", "completion_menu_current_bg",
            "completion_menu_meta_bg", "completion_menu_meta_current_bg")]
        + [("Diff lines", "ui_text", k, TEXT) for k in ("diff_added", "diff_removed")]
        + [("Selection", "ui_text", "selection_bg", HIGHLIGHT)]
        + [("Borders", k, "background", NONTEXT) for k in
           ("ui_border", "banner_border", "input_rule", "session_border",
            "response_border")],
        fixes={"completion_menu_current_bg": ["@row_active"],
               "completion_menu_meta_current_bg": ["@row_active"],
               "completion_menu_bg": ["@row_hover"],
               "completion_menu_meta_bg": ["@row_hover"],
               "selection_bg": ["@selection_hl", "@row_active"],
               "diff_added": ["@diff_add_line"], "diff_removed": ["@diff_del_line"],
               "status_bar_dim": MUTED_TEXT,
               # Light themes: dark_background sits closer to the text than
               # background does, so the bar must step away from the text.
               "status_bar_bg": ["@lighter_background", "@background"]},
    ),
    "hyprland-preview-share-picker.css": dict(
        slot=rf'@define-color (?P<key>[a-z_]+) (?P<hex>{HEX});',
        checks=[("Text", "foreground", "background", TEXT),
                ("Selected tab", "selected_tab", "background", TEXT),
                ("Cards", "text", "card_bg", TEXT),
                ("Region button", "text_dark", "accent", TEXT),
                ("Region button, hover", "text_dark", "accent_hover", TEXT),
                ("Focus border", "accent", "background", NONTEXT)],
        fixes={"accent_hover": ["@accent_bright", "@accent"], "card_bg": ["@row_hover"]},
    ),
    "obsidian.css": dict(
        slot=rf'--(?P<key>[a-z0-9-]+): (?P<hex>{HEX});',
        mix=r'--(?P<key>text-muted|text-faint): color-mix\(in srgb, (?P<hex>' + HEX +
            r') (?P<pct>\d+)%, transparent\);',
        mix_over="background-primary",
        checks=[("Text", k, "background-primary", TEXT) for k in
                ("text-normal", "text-title-h1", "text-title-h2", "text-title-h3",
                 "text-title-h4", "text-title-h5", "text-link", "text-accent",
                 "text-muted", "text-faint", "code-normal", "text-error",
                 "text-success")]
        + [("Tags", "tag-color", "tag-background", TEXT),
           ("Selection", "text-normal", "text-selection", HIGHLIGHT),
           ("Borders", "background-modifier-border", "background-primary", NONTEXT)],
        fixes={"text-muted": MUTED_TEXT, "text-faint": ["@muted", "@dark_foreground"],
               "tag-background": ["@row_hover", "@lighter_background"],
               "text-selection": ["@selection_hl", "@row_active"]},
    ),
}


# ---------------------------------------------------------------- measuring

def composite(overlay_hex8, under):
    o = overlay_hex8.lstrip("#")
    a = int(o[6:8], 16) / 255
    u = under.lstrip("#")
    return "#" + "".join(
        f"{round(int(o[i:i + 2], 16) * a + int(u[i:i + 2], 16) * (1 - a)):02X}"
        for i in (0, 2, 4))


def roles(p, mode, name):
    """Palette roles plus the verified surfaces tools/vscode.py solved."""
    theme, _ = vscode.build(p, mode, name)
    c, bg = theme["colors"], p["background"]
    accent_slot = next(s for s, v in p["_normals"].items() if v == p["accent"])
    r = {k: v for k, v in p.items() if not k.startswith("_") and isinstance(v, str)
         and re.fullmatch(HEX, v)}
    r.update(row_active=c["list.activeSelectionBackground"],
             row_hover=c["list.hoverBackground"],
             border=c["widget.border"],
             accent_bright=p["bright_" + accent_slot],
             selection_hl=composite(c["editor.selectionBackground"], bg),
             diff_add_line=composite(c["diffEditor.insertedLineBackground"], bg),
             diff_del_line=composite(c["diffEditor.removedLineBackground"], bg),
             diff_add_text=composite(c["diffEditor.insertedTextBackground"], bg),
             diff_del_text=composite(c["diffEditor.removedTextBackground"], bg))
    return r


def parse(spec, text):
    slots = {}
    for m in re.finditer(spec["slot"], text, re.M):
        slots.setdefault(m.group("key"), m.group("hex"))
    if "mix" in spec:
        base = slots[spec["mix_over"]]
        for m in re.finditer(spec["mix"], text):
            slots[m.group("key")] = mix_color(base, m.group("hex"), m.group("pct"))
    return slots


def measure(spec, slots, r):
    out = []
    for area, fg, bg, minimum in spec["checks"]:
        fv = r[fg[1:]] if fg.startswith("@") else slots.get(fg)
        bv = r[bg[1:]] if bg.startswith("@") else slots.get(bg)
        if fv is None or bv is None:
            raise SystemExit(f"missing slot {fg if fv is None else bg}; template changed?")
        out.append((area, fg, fv, bg, bv, minimum, contrast(fv, bv)))
    return out


def fix(spec, slots, r):
    """Swap failing slots for candidate roles until every check passes."""
    slots, changed = dict(slots), {}
    for _ in range(len(spec["checks"])):
        failing = [c for c in measure(spec, slots, r) if c[6] < c[5]]
        if not failing:
            return slots, changed
        area, fg, _, bg, _, _, _ = failing[0]
        target = fg if fg in spec["fixes"] else bg if bg in spec["fixes"] else None
        if target is None:
            raise SystemExit(f"no fix defined for {fg} on {bg} ({area})")
        for cand in spec["fixes"][target]:
            trial = dict(slots, **{target: r[cand[1:]]})
            involved = [c for c in measure(spec, trial, r)
                        if target in (c[1], c[3]) and c[6] < c[5]]
            if not involved:
                slots, changed[target] = trial, cand[1:]
                break
        else:
            raise SystemExit(f"no candidate fixes {target} ({area})")
    raise SystemExit("fix loop did not converge")


def patch(spec, text, slots, changed):
    for key in changed:
        value = slots[key]
        if "mix" in spec and re.search(spec["mix"].replace("(?P<key>text-muted|text-faint)",
                                                           re.escape(key)), text):
            text = re.sub(rf'(--{re.escape(key)}: )color-mix\([^;]*\);', rf'\g<1>{value};',
                          text)
            continue
        pattern = spec["slot"].replace("(?P<key>[a-z_0-9]+)", f"(?P<key>{re.escape(key)})") \
            .replace("(?P<key>[A-Za-z0-9_]+)", f"(?P<key>{re.escape(key)})") \
            .replace("(?P<key>[a-z_]+)", f"(?P<key>{re.escape(key)})") \
            .replace("(?P<key>[a-z0-9-]+)", f"(?P<key>{re.escape(key)})")
        text, n = re.subn(pattern, lambda m: m.group(0).replace(m.group("hex"), value),
                          text, count=1, flags=re.M)
        if n != 1:
            raise SystemExit(f"could not patch {key}")
    return text


# ---------------------------------------------------------------- commands

def parity():
    """Render the active Beacon theme and byte-compare with Omarchy's staging."""
    slug = open(os.path.expanduser("~/.local/state/omarchy/current/theme.name")).read().strip()
    name = f"omarchy-{slug}-theme"
    if name not in VARIANTS:
        raise SystemExit(f"active theme {slug} is not a Beacon theme; switch to one first")
    colors = theme_colors(os.path.join(STAGED, "colors.toml"))
    shipped = set(os.listdir(os.path.join(OUT, name)))
    ok = True
    for tpl in sorted(os.listdir(TEMPLATES)):
        if not tpl.endswith(".tpl"):
            continue
        out_name = tpl[:-4]
        text = open(template_path(out_name)).read()
        if out_name in shipped or re.search(r"hypr_gradient|gradient_start|shell_gradient", text):
            print(f"  skip   {out_name} (theme ships it, or uses gradient functions)")
            continue
        same = render(text, colors) == open(os.path.join(STAGED, out_name)).read()
        ok &= same
        print(f"  {'match ' if same else 'DIFFER'} {out_name}")
    print("parity OK" if ok else "PARITY FAILED")
    return ok


def main():
    report = ["# App theme report", "",
              "Omarchy generates these app themes from each palette. Every pair "
              "below is measured on the file Omarchy would render. Where a pair "
              "fails, Beacon ships a patched copy; the patched value is shown.",
              "Regenerate with `python3 tools/apps.py` (needs Omarchy).", ""]
    summary, errors, writes = [], [], []
    for name, spec_v in VARIANTS.items():
        p = build(spec_v)
        d = os.path.join(OUT, name)
        colors = theme_colors(os.path.join(d, "colors.toml"))
        r = roles(p, spec_v["mode"], name)
        report += [f"## `{name}`", ""]
        for app, spec in APPS.items():
            rendered = render(open(template_path(app)).read(), colors)
            slots = parse(spec, rendered)
            before = measure(spec, slots, r)
            try:
                fixed, changed = fix(spec, slots, r)
            except SystemExit as e:
                errors.append(f"{name} {app}: {e}")
                continue
            after = measure(spec, fixed, r)
            if any(c[6] < c[5] for c in after):
                errors.append(f"{name} {app}: still failing after patch")
                continue
            dest = os.path.join(d, app)
            writes.append((dest, patch(spec, rendered, fixed, changed) if changed else None))
            fails = sum(1 for c in before if c[6] < c[5])
            summary.append((name, app, fails, changed))
            report += [f"### {app}: " + (f"{fails} failing pair(s) patched"
                                         if changed else "passes as generated"), "",
                       "| Area | Foreground | On | Generated | Shipped | Needs |",
                       "|---|---|---|---|---|---|"]
            for b, a in zip(before, after):
                mark = "" if b[6] >= b[5] else " ✗"
                report.append(f"| {b[0]} | {b[1]} `{a[2]}` | {b[3]} `{a[4]}` | "
                              f"{b[6]:.2f}:1{mark} | {a[6]:.2f}:1 | {b[5]:g}:1 |")
            if changed:
                report.append("")
                report.append("Patched: " + ", ".join(f"`{k}` → {v}" for k, v in changed.items()))
            report.append("")
    if errors:
        print("\n".join(errors))
        raise SystemExit("App themes failed verification; nothing written.")
    for dest, text in writes:
        if text is not None:
            with open(dest, "w") as f:
                f.write(text)
        elif os.path.exists(dest):
            os.remove(dest)
    with open(os.path.join(ROOT, "APPS-REPORT.md"), "w") as f:
        f.write("\n".join(report))
    for name, app, fails, changed in summary:
        short = name.replace("omarchy-beacon-", "").replace("-theme", "")
        print(f"{short:18s} {app:36s} "
              + (f"{fails} failing -> patched {', '.join(changed)}" if changed else "ok"))


if __name__ == "__main__":
    if "--parity" in sys.argv:
        sys.exit(0 if parity() else 1)
    main()
