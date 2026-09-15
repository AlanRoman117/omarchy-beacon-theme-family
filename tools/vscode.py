"""Build a VS Code colour theme from a verified Beacon palette.

Why this exists
---------------
Omarchy themes VS Code in one of two ways. A stock theme names a marketplace
theme in `vscode.json`, and Omarchy installs it. A theme installed from git may
not ship `vscode.json` (installing an extension runs code), so Omarchy falls
back to a generic template filled from `colors.toml`. That template assumes a
palette shaped like the stock ones: `muted` is a dim border tone there, while
in Beacon it is AAA comment text, so the template paints bright grey patches
and leaves secondary buttons at under 2:1.

A cloned theme *may* ship `vscode-theme.json` itself: it is colour-only JSON,
it survives the install filter, and Omarchy's template step never overwrites a
file the theme already provides. So Beacon generates its own.

How the surfaces are chosen
---------------------------
Text is solved for AAA against `background`, so every other resting surface
steps *away* from the text: darker on dark themes, lighter on light ones. That
way nothing solved against the editor loses contrast in the sidebar, status
bar or a hover widget, and `background` is always the restrictive case.

Highlights (selection, find matches, diff lines) have to move toward the text
to be visible at all. Each one is solved so that every text colour the editor
can draw still clears 4.5:1 on top of it, then emitted as a translucent overlay
so VS Code can still layer decorations underneath.

`build()` returns the theme and every text/surface pair it creates. verify.py
refuses to write a theme with a failing pair.
"""
from colorlib import contrast, hex_to_rgb, hex_to_oklch, rel_luminance, \
    solve_for_contrast

TEXT = 7.0        # WCAG 1.4.6, body text
HIGHLIGHT = 4.5   # text sitting on a transient highlight (documented exception)
NONTEXT = 3.0     # WCAG 1.4.11, borders, indicators, focus
MARGIN = 0.15     # solve a little past each target so overlay rounding can't miss

NAMES = {"dark": "Dark", "light": "Light", "redgreen": "Red-Green",
         "blueyellow": "Blue-Yellow", "beacon": "Beacon"}


def title(name):
    parts = name.replace("omarchy-", "").replace("-theme", "").split("-")
    return " ".join(NAMES[x] for x in parts)


def _byte(h):
    return [round(c * 255) for c in hex_to_rgb(h)]


def overlay(target, under):
    """Return (#RRGGBBAA, composite) that lands on `target` over `under`.

    Uses the lowest alpha that keeps the overlay inside sRGB, so the highlight
    stays as see-through as the maths allows.
    """
    t, u = _byte(target), _byte(under)
    for a255 in range(140, 256, 4):
        a = a255 / 255
        o = [round((t[i] - u[i] * (1 - a)) / a) for i in range(3)]
        if all(0 <= c <= 255 for c in o):
            comp = [round(o[i] * a + u[i] * (1 - a)) for i in range(3)]
            return ("#" + "".join(f"{c:02X}" for c in o) + f"{a255:02X}",
                    "#" + "".join(f"{c:02X}" for c in comp))
    return target + "FF", target


def build(p, mode, name):
    dark = mode == "dark"
    bg = p["background"]
    # One step away from the text for chrome, two for floating widgets. Light
    # mode has only one neutral lighter than `background`, so both use it.
    chrome = p["dark_background"] if dark else p["lighter_background"]
    widget = p["darker_background"] if dark else p["lighter_background"]

    hue_of = lambda h: hex_to_oklch(h)[2]
    ink = [p[k] for k in ("foreground", "light_foreground", "bright_foreground",
                          "dark_foreground", "muted", "orange")]
    ink += list(p["_normals"].values()) + list(p["_brights"].values())
    # The text closest to the background decides how far a highlight can move.
    weakest = min(ink, key=rel_luminance) if dark else max(ink, key=rel_luminance)

    def surface(hue, chroma, text_contrast):
        """A surface that `weakest` still reads on at `text_contrast`."""
        return solve_for_contrast(hue, chroma, weakest, text_contrast + MARGIN,
                                  darker=dark)

    def hl(hue, chroma, text_contrast):
        return overlay(surface(hue, chroma, text_contrast), bg)

    neutral_hue = hue_of(p["selection"])
    subtle = p["muted"]                                   # 7.05:1 on background
    border = solve_for_contrast(250, 0.02, bg, 3.3, not dark)
    divider = solve_for_contrast(250, 0.02, bg, 1.6, not dark)
    # The active row must hold primary text at AAA *and* secondary text at AA;
    # take whichever constraint keeps the row closer to the resting surface.
    rows = [solve_for_contrast(neutral_hue, 0.04, p["foreground"], TEXT + 0.6, dark),
            solve_for_contrast(neutral_hue, 0.04, subtle, HIGHLIGHT + MARGIN, dark)]
    list_active = (min if dark else max)(rows, key=rel_luminance)
    list_hover = solve_for_contrast(neutral_hue, 0.03, p["foreground"],
                                    TEXT + 3.0, dark)

    sel, sel_c = hl(neutral_hue, 0.05, HIGHLIGHT)
    sel_inactive, sel_inactive_c = hl(neutral_hue, 0.03, 5.5)
    word, word_c = hl(neutral_hue, 0.03, 5.5)
    word_strong, word_strong_c = hl(neutral_hue, 0.04, 5.0)
    line, line_c = hl(neutral_hue, 0.015, 6.3)
    find, find_c = hl(hue_of(p["yellow"]), 0.06, HIGHLIGHT)
    find_other, find_other_c = hl(hue_of(p["yellow"]), 0.04, 5.5)
    range_hl, range_c = hl(hue_of(p["accent"]), 0.03, 6.0)
    ins_line, ins_line_c = hl(hue_of(p["green"]), 0.04, 5.5)
    ins_text, ins_text_c = hl(hue_of(p["green"]), 0.07, HIGHLIGHT)
    del_line, del_line_c = hl(hue_of(p["red"]), 0.04, 5.5)
    del_text, del_text_c = hl(hue_of(p["red"]), 0.07, HIGHLIGHT)
    stack, stack_c = hl(hue_of(p["yellow"]), 0.05, 5.0)
    merge_cur, merge_cur_c = hl(hue_of(p["green"]), 0.05, 5.0)
    merge_inc, merge_inc_c = hl(hue_of(p["blue"]), 0.05, 5.0)

    fg, fg_hi, fg_lo = p["foreground"], p["bright_foreground"], p["dark_foreground"]
    acc = p["accent"]
    acc_bright = p["bright_" + next(s for s, v in p["_normals"].items() if v == acc)]
    red, green, yellow, blue = p["red"], p["green"], p["yellow"], p["blue"]
    magenta, cyan, orange = p["magenta"], p["cyan"], p["orange"]
    b = p["_brights"]
    on_acc = bg  # button and badge text: the accent's own contrast, >= 7:1
    shadow = "#00000080" if dark else "#00000024"
    clear = "#00000000"

    colors = {
        # base
        "foreground": fg, "descriptionForeground": subtle,
        "disabledForeground": subtle, "errorForeground": red,
        "icon.foreground": fg, "focusBorder": acc, "contrastActiveBorder": clear,
        "widget.border": border, "widget.shadow": shadow,
        "selection.background": sel, "sash.hoverBorder": acc,
        "textLink.foreground": acc, "textLink.activeForeground": acc_bright,
        "textPreformat.foreground": orange, "textPreformat.background": widget,
        "textBlockQuote.background": widget, "textBlockQuote.border": acc,
        "textCodeBlock.background": widget, "textSeparator.foreground": divider,
        "toolbar.hoverBackground": list_hover, "toolbar.activeBackground": list_active,

        # buttons and controls
        "button.background": acc, "button.foreground": on_acc,
        "button.hoverBackground": acc_bright, "button.border": clear,
        "button.separator": on_acc,
        "button.secondaryBackground": list_hover, "button.secondaryForeground": fg,
        "button.secondaryHoverBackground": list_active,
        "checkbox.background": widget, "checkbox.foreground": fg,
        "checkbox.border": border, "checkbox.selectBackground": widget,
        "checkbox.selectBorder": acc,
        "dropdown.background": widget, "dropdown.listBackground": widget,
        "dropdown.border": border, "dropdown.foreground": fg,
        "input.background": widget, "input.border": border, "input.foreground": fg,
        "input.placeholderForeground": subtle,
        "inputOption.activeBackground": list_active, "inputOption.activeBorder": acc,
        "inputOption.activeForeground": fg, "inputOption.hoverBackground": list_hover,
        "inputValidation.errorBackground": widget, "inputValidation.errorBorder": red,
        "inputValidation.errorForeground": fg,
        "inputValidation.warningBackground": widget,
        "inputValidation.warningBorder": yellow,
        "inputValidation.warningForeground": fg,
        "inputValidation.infoBackground": widget, "inputValidation.infoBorder": blue,
        "inputValidation.infoForeground": fg,
        "badge.background": acc, "badge.foreground": on_acc,
        "progressBar.background": acc,
        "keybindingLabel.background": list_hover, "keybindingLabel.foreground": fg,
        "keybindingLabel.border": border, "keybindingLabel.bottomBorder": border,
        "scrollbar.shadow": shadow,
        "scrollbarSlider.background": border + "66",
        "scrollbarSlider.hoverBackground": border + "B3",
        "scrollbarSlider.activeBackground": acc + "B3",

        # lists and trees
        "list.activeSelectionBackground": list_active,
        "list.activeSelectionForeground": fg_hi,
        "list.activeSelectionIconForeground": fg_hi,
        "list.inactiveSelectionBackground": list_hover,
        "list.inactiveSelectionForeground": fg,
        "list.hoverBackground": list_hover, "list.hoverForeground": fg,
        "list.focusBackground": list_active, "list.focusForeground": fg_hi,
        "list.focusOutline": acc, "list.focusAndSelectionOutline": acc,
        "list.inactiveFocusOutline": border,
        "list.highlightForeground": acc, "list.focusHighlightForeground": acc_bright,
        "list.dropBackground": list_active, "list.errorForeground": red,
        "list.warningForeground": yellow, "list.invalidItemForeground": red,
        "list.deemphasizedForeground": subtle,
        "listFilterWidget.background": widget, "listFilterWidget.outline": acc,
        "listFilterWidget.noMatchesOutline": red,
        "list.filterMatchBackground": find_other, "list.filterMatchBorder": yellow,
        "tree.indentGuidesStroke": border, "tree.inactiveIndentGuidesStroke": divider,

        # activity bar, side bar, panels, title and status bars
        "activityBar.background": chrome, "activityBar.foreground": fg,
        "activityBar.inactiveForeground": subtle, "activityBar.border": divider,
        "activityBar.activeBorder": acc, "activityBar.activeBackground": list_hover,
        "activityBar.activeFocusBorder": acc, "activityBar.dropBorder": acc,
        "activityBarBadge.background": acc, "activityBarBadge.foreground": on_acc,
        "sideBar.background": chrome, "sideBar.foreground": fg,
        "sideBar.border": divider, "sideBar.dropBackground": list_active,
        "sideBarTitle.foreground": fg,
        "sideBarSectionHeader.background": chrome,
        "sideBarSectionHeader.foreground": fg, "sideBarSectionHeader.border": divider,
        "panel.background": bg, "panel.border": divider,
        "panel.dropBorder": acc,
        "panelTitle.activeForeground": fg, "panelTitle.activeBorder": acc,
        "panelTitle.inactiveForeground": subtle,
        "panelInput.border": border, "panelSection.border": divider,
        "panelSectionHeader.background": chrome, "panelSectionHeader.foreground": fg,
        "titleBar.activeBackground": chrome, "titleBar.activeForeground": fg,
        "titleBar.inactiveBackground": chrome, "titleBar.inactiveForeground": subtle,
        "titleBar.border": divider,
        "menubar.selectionBackground": list_hover, "menubar.selectionForeground": fg,
        "menu.background": widget, "menu.foreground": fg, "menu.border": border,
        "menu.selectionBackground": list_active, "menu.selectionForeground": fg_hi,
        "menu.separatorBackground": divider,
        "commandCenter.background": widget, "commandCenter.foreground": fg,
        "commandCenter.border": border, "commandCenter.activeBackground": list_hover,
        "commandCenter.activeForeground": fg,
        "commandCenter.inactiveForeground": subtle,
        "statusBar.background": chrome, "statusBar.foreground": fg,
        "statusBar.border": divider, "statusBar.focusBorder": acc,
        "statusBar.noFolderBackground": chrome, "statusBar.noFolderForeground": fg,
        "statusBar.debuggingBackground": orange, "statusBar.debuggingForeground": on_acc,
        "statusBar.debuggingBorder": orange,
        "statusBarItem.hoverBackground": list_hover,
        "statusBarItem.activeBackground": list_active,
        "statusBarItem.remoteBackground": acc, "statusBarItem.remoteForeground": on_acc,
        "statusBarItem.errorBackground": red, "statusBarItem.errorForeground": on_acc,
        "statusBarItem.warningBackground": yellow,
        "statusBarItem.warningForeground": on_acc,
        "statusBarItem.prominentBackground": list_active,
        "statusBarItem.prominentForeground": fg,
        "notifications.background": widget, "notifications.foreground": fg,
        "notifications.border": border, "notificationCenter.border": border,
        "notificationCenterHeader.background": chrome,
        "notificationCenterHeader.foreground": fg,
        "notificationToast.border": border, "notificationLink.foreground": acc,
        "notificationsErrorIcon.foreground": red,
        "notificationsWarningIcon.foreground": yellow,
        "notificationsInfoIcon.foreground": blue,
        "quickInput.background": widget, "quickInput.foreground": fg,
        "quickInputTitle.background": chrome,
        "quickInputList.focusBackground": list_active,
        "quickInputList.focusForeground": fg_hi,
        "pickerGroup.foreground": acc, "pickerGroup.border": divider,
        "breadcrumb.foreground": subtle, "breadcrumb.focusForeground": fg,
        "breadcrumb.activeSelectionForeground": fg_hi,
        "breadcrumbPicker.background": widget,

        # tabs and editor groups
        "editorGroup.border": divider, "editorGroup.dropBackground": list_active,
        "editorGroupHeader.tabsBackground": chrome,
        "editorGroupHeader.noTabsBackground": bg,
        "editorGroupHeader.tabsBorder": divider,
        "tab.activeBackground": bg, "tab.activeForeground": fg_hi,
        "tab.activeBorderTop": acc, "tab.activeBorder": bg,
        "tab.unfocusedActiveBackground": bg, "tab.unfocusedActiveForeground": fg,
        "tab.unfocusedActiveBorderTop": border,
        "tab.inactiveBackground": chrome, "tab.inactiveForeground": subtle,
        "tab.unfocusedInactiveForeground": subtle,
        "tab.hoverBackground": list_hover, "tab.hoverForeground": fg,
        "tab.unfocusedHoverBackground": list_hover, "tab.border": divider,
        "tab.activeModifiedBorder": yellow, "tab.inactiveModifiedBorder": yellow,
        "tab.lastPinnedBorder": border,

        # editor
        "editor.background": bg, "editor.foreground": fg,
        "editorLineNumber.foreground": subtle,
        "editorLineNumber.activeForeground": fg_hi,
        "editorLineNumber.dimmedForeground": subtle,
        "editorCursor.foreground": fg_hi, "editorCursor.background": bg,
        "editor.selectionBackground": sel,
        "editor.inactiveSelectionBackground": sel_inactive,
        "editor.selectionHighlightBackground": word, "editor.selectionHighlightBorder": border,
        "editor.wordHighlightBackground": word,
        "editor.wordHighlightStrongBackground": word_strong,
        "editor.wordHighlightStrongBorder": border,
        "editor.wordHighlightTextBackground": word,
        "editor.findMatchBackground": find, "editor.findMatchBorder": yellow,
        "editor.findMatchHighlightBackground": find_other,
        "editor.findRangeHighlightBackground": range_hl,
        "searchEditor.findMatchBackground": find_other,
        "searchEditor.findMatchBorder": yellow,
        "editor.hoverHighlightBackground": range_hl,
        "editor.lineHighlightBackground": line, "editor.lineHighlightBorder": clear,
        "editor.rangeHighlightBackground": range_hl,
        "editor.symbolHighlightBackground": find_other,
        "editor.symbolHighlightBorder": yellow,
        "editorLink.activeForeground": acc,
        "editorWhitespace.foreground": divider, "editorRuler.foreground": divider,
        "editorIndentGuide.background1": divider,
        "editorIndentGuide.activeBackground1": border,
        "editorCodeLens.foreground": subtle,
        "editorBracketMatch.background": range_hl, "editorBracketMatch.border": acc,
        "editorBracketHighlight.foreground1": blue,
        "editorBracketHighlight.foreground2": magenta,
        "editorBracketHighlight.foreground3": yellow,
        "editorBracketHighlight.foreground4": cyan,
        "editorBracketHighlight.foreground5": orange,
        "editorBracketHighlight.foreground6": green,
        "editorBracketHighlight.unexpectedBracket.foreground": red,
        "editorInlayHint.background": clear, "editorInlayHint.foreground": subtle,
        "editorGhostText.foreground": subtle,
        "editorGhostText.border": clear,
        # Faded "unused" code would drop below AAA, so it keeps full opacity and
        # is marked with a dotted underline instead.
        "editorUnnecessaryCode.opacity": "#000000FF",
        "editorUnnecessaryCode.border": subtle,
        "editorError.foreground": red, "editorWarning.foreground": yellow,
        "editorInfo.foreground": blue, "editorHint.foreground": cyan,
        "problemsErrorIcon.foreground": red, "problemsWarningIcon.foreground": yellow,
        "problemsInfoIcon.foreground": blue,
        "editorGutter.background": bg,
        "editorGutter.addedBackground": green, "editorGutter.modifiedBackground": yellow,
        "editorGutter.deletedBackground": red,
        "editorGutter.foldingControlForeground": subtle,
        "editorOverviewRuler.border": clear,
        "editorOverviewRuler.errorForeground": red,
        "editorOverviewRuler.warningForeground": yellow,
        "editorOverviewRuler.infoForeground": blue,
        "editorOverviewRuler.findMatchForeground": yellow,
        "editorOverviewRuler.selectionHighlightForeground": border,
        "editorOverviewRuler.addedForeground": green,
        "editorOverviewRuler.modifiedForeground": yellow,
        "editorOverviewRuler.deletedForeground": red,
        "editorStickyScroll.background": bg,
        "editorStickyScroll.shadow": shadow,
        "editorStickyScrollHover.background": list_hover,

        # widgets inside the editor
        "editorWidget.background": widget, "editorWidget.foreground": fg,
        "editorWidget.border": border, "editorWidget.resizeBorder": acc,
        "editorHoverWidget.background": widget, "editorHoverWidget.foreground": fg,
        "editorHoverWidget.border": border,
        "editorHoverWidget.statusBarBackground": chrome,
        "editorSuggestWidget.background": widget, "editorSuggestWidget.foreground": fg,
        "editorSuggestWidget.border": border,
        "editorSuggestWidget.selectedBackground": list_active,
        "editorSuggestWidget.selectedForeground": fg_hi,
        "editorSuggestWidget.highlightForeground": acc,
        "editorSuggestWidget.focusHighlightForeground": acc_bright,
        "editorSuggestWidgetStatus.foreground": subtle,
        "editorMarkerNavigation.background": widget,
        "editorMarkerNavigationError.background": red,
        "editorMarkerNavigationWarning.background": yellow,
        "editorMarkerNavigationInfo.background": blue,
        "peekView.border": acc, "peekViewTitle.background": chrome,
        "peekViewTitleLabel.foreground": fg, "peekViewTitleDescription.foreground": subtle,
        "peekViewEditor.background": widget,
        "peekViewEditor.matchHighlightBackground": find,
        "peekViewEditorGutter.background": widget,
        "peekViewResult.background": widget, "peekViewResult.fileForeground": fg,
        "peekViewResult.lineForeground": fg,
        "peekViewResult.matchHighlightBackground": find_other,
        "peekViewResult.selectionBackground": list_active,
        "peekViewResult.selectionForeground": fg_hi,
        "debugToolBar.background": widget, "debugToolBar.border": border,
        "editor.stackFrameHighlightBackground": stack,
        "editor.focusedStackFrameHighlightBackground": stack,

        # diff and merge
        "diffEditor.insertedLineBackground": ins_line,
        "diffEditor.insertedTextBackground": ins_text,
        "diffEditor.removedLineBackground": del_line,
        "diffEditor.removedTextBackground": del_text,
        "diffEditorGutter.insertedLineBackground": ins_line,
        "diffEditorGutter.removedLineBackground": del_line,
        "diffEditorOverview.insertedForeground": green,
        "diffEditorOverview.removedForeground": red,
        "diffEditor.border": divider, "diffEditor.diagonalFill": divider,
        "merge.currentHeaderBackground": merge_cur,
        "merge.currentContentBackground": merge_cur,
        "merge.incomingHeaderBackground": merge_inc,
        "merge.incomingContentBackground": merge_inc,
        "merge.border": border,
        "editorOverviewRuler.currentContentForeground": green,
        "editorOverviewRuler.incomingContentForeground": blue,

        # source control
        "gitDecoration.addedResourceForeground": green,
        "gitDecoration.untrackedResourceForeground": green,
        "gitDecoration.modifiedResourceForeground": yellow,
        "gitDecoration.deletedResourceForeground": red,
        "gitDecoration.renamedResourceForeground": cyan,
        "gitDecoration.conflictingResourceForeground": magenta,
        "gitDecoration.ignoredResourceForeground": subtle,
        "gitDecoration.submoduleResourceForeground": blue,
        "gitDecoration.stageModifiedResourceForeground": yellow,
        "gitDecoration.stageDeletedResourceForeground": red,

        # terminal
        "terminal.background": bg, "terminal.foreground": fg,
        "terminal.border": divider, "terminal.selectionBackground": sel,
        "terminal.inactiveSelectionBackground": sel_inactive,
        "terminal.findMatchBackground": find, "terminal.findMatchBorder": yellow,
        "terminal.findMatchHighlightBackground": find_other,
        "terminalCursor.foreground": fg_hi, "terminalCursor.background": bg,
        "terminalCommandDecoration.defaultBackground": subtle,
        "terminalCommandDecoration.successBackground": green,
        "terminalCommandDecoration.errorBackground": red,
        **{f"terminal.ansi{n}": p[f"color{i}"] for i, n in enumerate(
            ["Black", "Red", "Green", "Yellow", "Blue", "Magenta", "Cyan", "White",
             "BrightBlack", "BrightRed", "BrightGreen", "BrightYellow",
             "BrightBlue", "BrightMagenta", "BrightCyan", "BrightWhite"])},

        # everything else people run into
        "settings.headerForeground": fg_hi, "settings.modifiedItemIndicator": acc,
        "settings.focusedRowBackground": list_hover, "settings.rowHoverBackground": list_hover,
        "settings.focusedRowBorder": acc,
        "settings.textInputBackground": widget, "settings.textInputBorder": border,
        "settings.numberInputBackground": widget, "settings.numberInputBorder": border,
        "settings.dropdownBackground": widget, "settings.dropdownBorder": border,
        "settings.checkboxBackground": widget, "settings.checkboxBorder": border,
        "extensionButton.prominentBackground": acc,
        "extensionButton.prominentForeground": on_acc,
        "extensionButton.prominentHoverBackground": acc_bright,
        "extensionBadge.remoteBackground": acc, "extensionBadge.remoteForeground": on_acc,
        "extensionIcon.starForeground": yellow,
        "welcomePage.tileBackground": widget, "welcomePage.tileHoverBackground": list_hover,
        "welcomePage.tileBorder": border, "walkThrough.embeddedEditorBackground": widget,
        "testing.iconPassed": green, "testing.iconFailed": red,
        "testing.iconErrored": red, "testing.iconQueued": yellow,
        "testing.iconSkipped": subtle, "testing.iconUnset": subtle,
        "testing.runAction": green,
        "debugIcon.breakpointForeground": red,
        "debugIcon.breakpointUnverifiedForeground": subtle,
        "debugIcon.startForeground": green, "debugIcon.pauseForeground": yellow,
        "debugIcon.stopForeground": red, "debugIcon.restartForeground": green,
        "debugIcon.continueForeground": blue, "debugIcon.stepOverForeground": blue,
        "debugIcon.stepIntoForeground": blue, "debugIcon.stepOutForeground": blue,
        "debugTokenExpression.name": blue, "debugTokenExpression.value": fg,
        "debugTokenExpression.string": green, "debugTokenExpression.number": orange,
        "debugTokenExpression.boolean": orange, "debugTokenExpression.error": red,
        "charts.foreground": fg, "charts.lines": divider, "charts.red": red,
        "charts.blue": blue, "charts.yellow": yellow, "charts.orange": orange,
        "charts.green": green, "charts.purple": magenta,
        "minimap.background": bg, "minimap.selectionHighlight": sel,
        "minimap.findMatchHighlight": yellow, "minimap.errorHighlight": red,
        "minimap.warningHighlight": yellow,
        "minimapGutter.addedBackground": green, "minimapGutter.modifiedBackground": yellow,
        "minimapGutter.deletedBackground": red,
        "minimapSlider.background": border + "40",
        "minimapSlider.hoverBackground": border + "80",
        "minimapSlider.activeBackground": acc + "80",
    }

    # Syntax. Roles follow the conventions most themes share, so code reads the
    # way people expect, and no two neighbouring roles share a slot.
    def tok(scope, fore, style=None):
        s = {"foreground": fore}
        if style:
            s["fontStyle"] = style
        return {"scope": scope, "settings": s}

    token_colors = [
        tok(["comment", "punctuation.definition.comment"], p["muted"], "italic"),
        tok(["keyword", "storage", "storage.type", "storage.modifier",
             "keyword.control"], magenta),
        tok(["keyword.operator", "punctuation", "meta.brace", "meta.delimiter"], fg_lo),
        tok(["keyword.operator.new", "keyword.operator.expression",
             "keyword.operator.logical.python"], magenta),
        tok(["string", "string.quoted", "string.template",
             "punctuation.definition.string"], green),
        tok(["string.regexp", "constant.character.escape",
             "constant.other.placeholder"], cyan),
        tok(["constant.numeric", "constant.language", "constant.other",
             "support.constant", "variable.other.constant",
             "variable.other.enummember"], orange),
        tok(["entity.name.function", "support.function", "meta.function-call",
             "variable.function"], blue),
        tok(["entity.name.type", "entity.name.class", "entity.name.interface",
             "entity.other.inherited-class", "support.type", "support.class",
             "storage.type.primitive", "storage.type.builtin"], yellow),
        tok(["entity.name.namespace", "entity.name.module",
             "entity.name.type.module"], b["blue"]),
        tok(["variable", "meta.definition.variable"], fg),
        tok(["variable.parameter", "meta.parameter"], p["light_foreground"]),
        tok(["variable.language", "variable.language.this",
             "variable.language.self"], red, "italic"),
        tok(["variable.other.property", "variable.other.object.property",
             "support.variable.property", "meta.object-literal.key",
             "entity.name.variable.field"], cyan),
        tok(["meta.decorator", "entity.name.function.decorator",
             "punctuation.decorator", "storage.type.annotation"], b["cyan"]),
        tok(["entity.name.function.macro", "keyword.control.directive",
             "keyword.control.import", "keyword.control.export"], b["magenta"]),
        tok(["entity.name.tag", "punctuation.definition.tag"], red),
        tok(["entity.other.attribute-name"], orange),
        tok(["support.type.property-name.json", "support.type.property-name"], blue),
        tok(["markup.heading", "entity.name.section"], blue, "bold"),
        tok(["markup.bold"], fg_hi, "bold"),
        tok(["markup.italic"], fg, "italic"),
        tok(["markup.underline.link", "string.other.link"], cyan, "underline"),
        tok(["markup.inline.raw", "markup.fenced_code", "markup.raw"], orange),
        tok(["markup.quote"], p["muted"], "italic"),
        tok(["markup.list", "punctuation.definition.list"], magenta),
        tok(["markup.inserted", "meta.diff.header.to-file"], green),
        tok(["markup.deleted", "meta.diff.header.from-file"], red),
        tok(["markup.changed"], yellow),
        tok(["invalid", "invalid.illegal"], red, "underline"),
        tok(["invalid.deprecated"], yellow, "strikethrough"),
    ]

    semantic = {
        "variable": fg, "variable.readonly": orange, "variable.defaultLibrary": fg,
        "parameter": p["light_foreground"], "property": cyan,
        "property.readonly": cyan, "function": blue, "method": blue,
        "function.defaultLibrary": blue, "macro": b["magenta"],
        "class": yellow, "interface": yellow, "struct": yellow, "enum": yellow,
        "type": yellow, "typeParameter": yellow, "type.defaultLibrary": yellow,
        "enumMember": orange, "namespace": b["blue"], "decorator": b["cyan"],
        "keyword": magenta, "string": green, "number": orange, "regexp": cyan,
        "operator": fg_lo, "comment": {"foreground": p["muted"], "fontStyle": "italic"},
        "*.deprecated": {"strikethrough": True},
    }

    theme = {
        "name": title(name),
        "$schema": "vscode://schemas/color-theme",
        "type": mode,
        "semanticHighlighting": True,
        "colors": colors,
        "tokenColors": token_colors,
        "semanticTokenColors": semantic,
    }

    # Every pair a person has to read or find, with the threshold it must meet.
    syntax = {s: p["_normals"][s] for s in p["_normals"]}
    syntax.update({"orange": orange, "muted (comments)": p["muted"],
                   "dark_foreground (operators)": fg_lo,
                   "light_foreground (parameters)": p["light_foreground"],
                   **{"bright_" + s: v for s, v in b.items()}})
    labels = {**syntax, "foreground": fg, "bright_foreground": fg_hi}
    weak_label = next((k for k, v in labels.items() if v == weakest), weakest)

    # minimum=None marks an advisory row: reported, never gating.
    checks = []

    def need(area, fore_label, fore, back_label, back, minimum):
        checks.append((area, fore_label, fore, back_label, back, minimum,
                       contrast(fore, back)))

    for label, v in syntax.items():
        need("Editor syntax", label, v, "editor", bg, TEXT)
    for surf_label, surf in (("editor", bg), ("side bar / status bar", chrome),
                             ("widgets, menus, inputs", widget)):
        need("Text", "foreground", fg, surf_label, surf, TEXT)
        need("Text", "secondary text", subtle, surf_label, surf, TEXT)
        need("Non-text", "control border", border, surf_label, surf, NONTEXT)
        need("Non-text", "focus ring", acc, surf_label, surf, NONTEXT)
    for label in ("red", "green", "yellow", "magenta", "cyan", "blue"):
        need("Source control, side bar", label, p[label], "side bar", chrome, TEXT)
    need("Lists", "selected item", fg_hi, "active selection", list_active, TEXT)
    need("Lists", "foreground", fg, "active selection", list_active, TEXT)
    need("Lists", "foreground", fg, "hover", list_hover, TEXT)
    need("Lists", "secondary text", subtle, "hover", list_hover, HIGHLIGHT)
    need("Lists", "secondary text", subtle, "active selection", list_active, HIGHLIGHT)
    need("Lists", "match highlight", acc, "active selection", list_active, HIGHLIGHT)
    need("Buttons", "label", on_acc, "primary button", acc, TEXT)
    need("Buttons", "label", on_acc, "primary button, hover", acc_bright, TEXT)
    need("Buttons", "label", fg, "secondary button", list_hover, TEXT)
    need("Buttons", "label", fg, "secondary button, hover", list_active, TEXT)
    need("Status bar", "label", on_acc, "debugging", orange, TEXT)
    need("Status bar", "label", on_acc, "error item", red, TEXT)
    need("Status bar", "label", on_acc, "warning item", yellow, TEXT)
    need("Non-text", "cursor", fg_hi, "editor", bg, NONTEXT)
    need("Non-text", "find match border", yellow, "editor", bg, NONTEXT)
    need("Non-text", "active tab indicator", acc, "editor", bg, NONTEXT)
    need("Non-text", "gutter: added", green, "editor", bg, NONTEXT)
    need("Non-text", "gutter: modified", yellow, "editor", bg, NONTEXT)
    need("Non-text", "gutter: deleted", red, "editor", bg, NONTEXT)
    for label, comp in (("selection", sel_c), ("inactive selection", sel_inactive_c),
                        ("current find match", find_c), ("other find matches", find_other_c),
                        ("word highlight", word_c), ("line highlight", line_c),
                        ("diff: inserted line", ins_line_c),
                        ("diff: inserted text", ins_text_c),
                        ("diff: removed line", del_line_c),
                        ("diff: removed text", del_text_c),
                        ("merge conflict", merge_cur_c), ("debug stack frame", stack_c)):
        need("Highlights", f"weakest syntax colour ({weak_label})", weakest,
             label, comp, HIGHLIGHT)
    for label, comp in (("selection", sel_c), ("current find match", find_c),
                        ("diff: inserted text", ins_text_c),
                        ("diff: removed text", del_text_c)):
        need("Highlight visibility", label, comp, "editor", bg, None)
    need("Highlight visibility", "active list row", list_active, "side bar", chrome, None)
    need("Highlight visibility", "hovered list row", list_hover, "side bar", chrome, None)

    return theme, checks
