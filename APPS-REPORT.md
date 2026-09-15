# App theme report

Omarchy generates these app themes from each palette. Every pair below is measured on the file Omarchy would render. Where a pair fails, Beacon ships a patched copy; the patched value is shown.
Regenerate with `python3 tools/apps.py` (needs Omarchy).

## `omarchy-beacon-dark-theme`

### btop.theme: 1 failing pair(s) patched

| Area | Foreground | On | Generated | Shipped | Needs |
|---|---|---|---|---|---|
| Text | main_fg `#D8DFE8` | main_bg `#10141A` | 13.76:1 | 13.76:1 | 7:1 |
| Text | title `#D8DFE8` | main_bg `#10141A` | 13.76:1 | 13.76:1 | 7:1 |
| Text | hi_fg `#99C6FF` | main_bg `#10141A` | 10.45:1 | 10.45:1 | 7:1 |
| Text | inactive_fg `#95A2A9` | main_bg `#10141A` | 7.05:1 | 7.05:1 | 7:1 |
| Text | graph_text `#EDF1F6` | main_bg `#10141A` | 16.28:1 | 16.28:1 | 7:1 |
| Text | proc_misc `#EDF1F6` | main_bg `#10141A` | 16.28:1 | 16.28:1 | 7:1 |
| Selected process row | selected_fg `#FFFFFF` | selected_bg `#475971` | 4.05:1 ✗ | 7.15:1 | 7:1 |
| Box outlines | cpu_box `#FFBDE8` | main_bg `#10141A` | 12.05:1 | 12.05:1 | 3:1 |
| Box outlines | mem_box `#59C977` | main_bg `#10141A` | 8.84:1 | 8.84:1 | 3:1 |
| Box outlines | net_box `#FA7C75` | main_bg `#10141A` | 7.22:1 | 7.22:1 | 3:1 |
| Box outlines | proc_box `#99C6FF` | main_bg `#10141A` | 10.45:1 | 10.45:1 | 3:1 |
| Box outlines | div_line `#95A2A9` | main_bg `#10141A` | 7.05:1 | 7.05:1 | 3:1 |

Patched: `selected_fg` → bright_foreground

### helix.toml: passes as generated

| Area | Foreground | On | Generated | Shipped | Needs |
|---|---|---|---|---|---|
| Syntax and text | foreground `#D8DFE8` | background `#10141A` | 13.76:1 | 13.76:1 | 7:1 |
| Syntax and text | color1 `#FA7C75` | background `#10141A` | 7.22:1 | 7.22:1 | 7:1 |
| Syntax and text | color2 `#59C977` | background `#10141A` | 8.84:1 | 8.84:1 | 7:1 |
| Syntax and text | color3 `#FFDA70` | background `#10141A` | 13.65:1 | 13.65:1 | 7:1 |
| Syntax and text | color4 `#99C6FF` | background `#10141A` | 10.45:1 | 10.45:1 | 7:1 |
| Syntax and text | color5 `#FFBDE8` | background `#10141A` | 12.05:1 | 12.05:1 | 7:1 |
| Syntax and text | color6 `#A8F6FF` | background `#10141A` | 15.21:1 | 15.21:1 | 7:1 |
| Syntax and text | color8 `#95A2A9` | background `#10141A` | 7.05:1 | 7.05:1 | 7:1 |
| Statusline band | background `#10141A` | foreground `#D8DFE8` | 13.76:1 | 13.76:1 | 7:1 |
| Statusline band | background `#10141A` | color8 `#95A2A9` | 7.05:1 | 7.05:1 | 7:1 |
| Statusline band | background `#10141A` | color4 `#99C6FF` | 10.45:1 | 10.45:1 | 7:1 |
| Statusline band | background `#10141A` | color2 `#59C977` | 8.84:1 | 8.84:1 | 7:1 |
| Statusline band | background `#10141A` | color5 `#FFBDE8` | 12.05:1 | 12.05:1 | 7:1 |
| Selection | selection_foreground `#FFFFFF` | selection_background `#475971` | 7.15:1 | 7.15:1 | 7:1 |
| Cursor | background `#10141A` | cursor `#FFFFFF` | 18.47:1 | 18.47:1 | 7:1 |
| Focused text | foreground `#D8DFE8` | lighter_background `#1B2029` | 12.17:1 | 12.17:1 | 7:1 |
| Menu selection | background `#10141A` | foreground `#D8DFE8` | 13.76:1 | 13.76:1 | 7:1 |
| Cursor line and highlights | color1 `#FA7C75` | lighter_background `#1B2029` | 6.38:1 | 6.38:1 | 4.5:1 |
| Cursor line and highlights | color2 `#59C977` | lighter_background `#1B2029` | 7.82:1 | 7.82:1 | 4.5:1 |
| Cursor line and highlights | color3 `#FFDA70` | lighter_background `#1B2029` | 12.07:1 | 12.07:1 | 4.5:1 |
| Cursor line and highlights | color4 `#99C6FF` | lighter_background `#1B2029` | 9.24:1 | 9.24:1 | 4.5:1 |
| Cursor line and highlights | color5 `#FFBDE8` | lighter_background `#1B2029` | 10.66:1 | 10.66:1 | 4.5:1 |
| Cursor line and highlights | color6 `#A8F6FF` | lighter_background `#1B2029` | 13.45:1 | 13.45:1 | 4.5:1 |
| Cursor line and highlights | color8 `#95A2A9` | lighter_background `#1B2029` | 6.24:1 | 6.24:1 | 4.5:1 |

### pi.json: 3 failing pair(s) patched

| Area | Foreground | On | Generated | Shipped | Needs |
|---|---|---|---|---|---|
| Text | foreground `#D8DFE8` | background `#10141A` | 13.76:1 | 13.76:1 | 7:1 |
| Text | accent `#99C6FF` | background `#10141A` | 10.45:1 | 10.45:1 | 7:1 |
| Text | color1 `#FA7C75` | background `#10141A` | 7.22:1 | 7.22:1 | 7:1 |
| Text | color2 `#59C977` | background `#10141A` | 8.84:1 | 8.84:1 | 7:1 |
| Text | color3 `#FFDA70` | background `#10141A` | 13.65:1 | 13.65:1 | 7:1 |
| Text | color4 `#99C6FF` | background `#10141A` | 10.45:1 | 10.45:1 | 7:1 |
| Text | color5 `#FFBDE8` | background `#10141A` | 12.05:1 | 12.05:1 | 7:1 |
| Text | color6 `#A8F6FF` | background `#10141A` | 15.21:1 | 15.21:1 | 7:1 |
| Text | color8 `#95A2A9` | background `#10141A` | 7.05:1 | 7.05:1 | 7:1 |
| Text | mutedText `#A3AEBD` | background `#10141A` | 6.51:1 ✗ | 8.22:1 | 7:1 |
| Text | dimText `#95A2A9` | background `#10141A` | 3.98:1 ✗ | 7.05:1 | 7:1 |
| Message panels | foreground `#D8DFE8` | panel `#1c2026` | 12.18:1 | 12.18:1 | 7:1 |
| Message panels | foreground `#D8DFE8` | panelAlt `#24282f` | 11.02:1 | 11.02:1 | 7:1 |
| Message panels | foreground `#D8DFE8` | selectedBackground `#2e3b4c` | 8.47:1 | 8.47:1 | 7:1 |
| Message panels | foreground `#D8DFE8` | panelPending `#202935` | 10.94:1 | 10.94:1 | 7:1 |
| Message panels | foreground `#D8DFE8` | panelSuccess `#192a25` | 11.18:1 | 11.18:1 | 7:1 |
| Message panels | foreground `#D8DFE8` | panelError `#2c2025` | 11.67:1 | 11.67:1 | 7:1 |
| Tool titles | accent `#99C6FF` | panelPending `#202935` | 8.30:1 | 8.30:1 | 7:1 |
| Tool titles | accent `#99C6FF` | panelSuccess `#192a25` | 8.49:1 | 8.49:1 | 7:1 |
| Tool titles | accent `#99C6FF` | panelError `#2c2025` | 8.86:1 | 8.86:1 | 7:1 |
| Input border | border `#5F6973` | background `#10141A` | 2.31:1 ✗ | 3.30:1 | 3:1 |

Patched: `mutedText` → dark_foreground, `dimText` → muted, `border` → border

### claude.json: 1 failing pair(s) patched

| Area | Foreground | On | Generated | Shipped | Needs |
|---|---|---|---|---|---|
| Text | text `#D8DFE8` | @background `#10141A` | 13.76:1 | 13.76:1 | 7:1 |
| Text | subtle `#95A2A9` | @background `#10141A` | 7.05:1 | 7.05:1 | 7:1 |
| Text | inactive `#A3AEBD` | @background `#10141A` | 5.59:1 ✗ | 8.22:1 | 7:1 |
| Text | suggestion `#A8F6FF` | @background `#10141A` | 15.21:1 | 15.21:1 | 7:1 |
| Text | permission `#99C6FF` | @background `#10141A` | 10.45:1 | 10.45:1 | 7:1 |
| Text | remember `#FFDA70` | @background `#10141A` | 13.65:1 | 13.65:1 | 7:1 |
| Text | success `#59C977` | @background `#10141A` | 8.84:1 | 8.84:1 | 7:1 |
| Text | error `#FA7C75` | @background `#10141A` | 7.22:1 | 7.22:1 | 7:1 |
| Text | warning `#FFDA70` | @background `#10141A` | 13.65:1 | 13.65:1 | 7:1 |
| Text | merged `#FFBDE8` | @background `#10141A` | 12.05:1 | 12.05:1 | 7:1 |
| Text | planMode `#A8F6FF` | @background `#10141A` | 15.21:1 | 15.21:1 | 7:1 |
| Text | autoAccept `#FFDA70` | @background `#10141A` | 13.65:1 | 13.65:1 | 7:1 |
| Text | claude `#99C6FF` | @background `#10141A` | 10.45:1 | 10.45:1 | 7:1 |
| Badges | inverseText `#10141A` | claude `#99C6FF` | 10.45:1 | 10.45:1 | 7:1 |
| Message backgrounds | text `#D8DFE8` | userMessageBackground `#1c2026` | 12.18:1 | 12.18:1 | 7:1 |
| Message backgrounds | text `#D8DFE8` | userMessageBackgroundHover `#24282f` | 11.02:1 | 11.02:1 | 7:1 |
| Message backgrounds | text `#D8DFE8` | bashMessageBackgroundColor `#1c2026` | 12.18:1 | 12.18:1 | 7:1 |
| Message backgrounds | text `#D8DFE8` | memoryBackgroundColor `#1c2026` | 12.18:1 | 12.18:1 | 7:1 |
| Diff lines | text `#D8DFE8` | diffAdded `#1b2f28` | 10.54:1 | 10.54:1 | 7:1 |
| Diff lines | text `#D8DFE8` | diffRemoved `#332428` | 10.99:1 | 10.99:1 | 7:1 |
| Diff words and selection | text `#D8DFE8` | diffAddedWord `#274e38` | 7.00:1 | 7.00:1 | 4.5:1 |
| Diff words and selection | text `#D8DFE8` | diffRemovedWord `#5b3537` | 7.78:1 | 7.78:1 | 4.5:1 |
| Diff words and selection | text `#D8DFE8` | selectionBg `#475971` | 5.33:1 | 5.33:1 | 4.5:1 |
| Prompt border | promptBorder `#99C6FF` | @background `#10141A` | 10.45:1 | 10.45:1 | 3:1 |

Patched: `inactive` → dark_foreground

### t3code.json: 1 failing pair(s) patched

| Area | Foreground | On | Generated | Shipped | Needs |
|---|---|---|---|---|---|
| Text | text `#D8DFE8` | chrome `#10141A` | 13.76:1 | 13.76:1 | 7:1 |
| Toolbar | toolbarForeground `#D8DFE8` | toolbar `#10141A` | 13.76:1 | 13.76:1 | 7:1 |
| Sidebar | sidebarForeground `#D8DFE8` | sidebar `#0A0E13` | 14.41:1 | 14.41:1 | 7:1 |
| Code | codeForeground `#D8DFE8` | codeBackground `#0A0E13` | 14.41:1 | 14.41:1 | 7:1 |
| Terminal | terminalForeground `#D8DFE8` | terminalBackground `#10141A` | 13.76:1 | 13.76:1 | 7:1 |
| Status text | error `#ee9f9d` | chrome `#10141A` | 8.87:1 | 8.87:1 | 7:1 |
| Status text | warning `#f1dc9a` | chrome `#10141A` | 13.58:1 | 13.58:1 | 7:1 |
| Sidebar rows | sidebarForeground `#D8DFE8` | sidebarRowHover `#161b20` | 12.91:1 | 12.91:1 | 7:1 |
| Sidebar rows | sidebarForeground `#D8DFE8` | sidebarRowActive `#242f3d` | 10.10:1 | 10.10:1 | 7:1 |
| Sidebar rows | sidebarForeground `#D8DFE8` | sidebarRowSelected `#28364A` | 5.33:1 ✗ | 9.11:1 | 7:1 |
| Terminal selection | terminalForeground `#D8DFE8` | terminalSelection `#475971` | 5.33:1 | 5.33:1 | 4.5:1 |
| Borders and focus | border `#95A2A9` | chrome `#10141A` | 7.05:1 | 7.05:1 | 3:1 |
| Borders and focus | toolbarBorder `#95A2A9` | chrome `#10141A` | 7.05:1 | 7.05:1 | 3:1 |
| Borders and focus | focus `#99C6FF` | chrome `#10141A` | 10.45:1 | 10.45:1 | 3:1 |
| Borders and focus | sidebarBorder `#95A2A9` | sidebar `#0A0E13` | 7.39:1 | 7.39:1 | 3:1 |

Patched: `sidebarRowSelected` → row_active

### hermes.yaml: 2 failing pair(s) patched

| Area | Foreground | On | Generated | Shipped | Needs |
|---|---|---|---|---|---|
| Text | ui_text `#D8DFE8` | background `#10141A` | 13.76:1 | 13.76:1 | 7:1 |
| Text | ui_primary `#99C6FF` | background `#10141A` | 10.45:1 | 10.45:1 | 7:1 |
| Text | ui_label `#99C6FF` | background `#10141A` | 10.45:1 | 10.45:1 | 7:1 |
| Text | ui_ok `#59C977` | background `#10141A` | 8.84:1 | 8.84:1 | 7:1 |
| Text | ui_warn `#FFDA70` | background `#10141A` | 13.65:1 | 13.65:1 | 7:1 |
| Text | ui_error `#FA7C75` | background `#10141A` | 7.22:1 | 7.22:1 | 7:1 |
| Text | ui_tool `#A8F6FF` | background `#10141A` | 15.21:1 | 15.21:1 | 7:1 |
| Text | ui_thinking `#A3AEBD` | background `#10141A` | 8.22:1 | 8.22:1 | 7:1 |
| Text | banner_title `#99C6FF` | background `#10141A` | 10.45:1 | 10.45:1 | 7:1 |
| Text | banner_dim `#A3AEBD` | background `#10141A` | 8.22:1 | 8.22:1 | 7:1 |
| Text | banner_text `#D8DFE8` | background `#10141A` | 13.76:1 | 13.76:1 | 7:1 |
| Text | prompt `#FFFFFF` | background `#10141A` | 18.47:1 | 18.47:1 | 7:1 |
| Text | shell_dollar `#99C6FF` | background `#10141A` | 10.45:1 | 10.45:1 | 7:1 |
| Text | session_label `#99C6FF` | background `#10141A` | 10.45:1 | 10.45:1 | 7:1 |
| Text | syntax_string `#59C977` | background `#10141A` | 8.84:1 | 8.84:1 | 7:1 |
| Text | syntax_number `#FFDA70` | background `#10141A` | 13.65:1 | 13.65:1 | 7:1 |
| Text | syntax_keyword `#FFBDE8` | background `#10141A` | 12.05:1 | 12.05:1 | 7:1 |
| Text | syntax_comment `#95A2A9` | background `#10141A` | 7.05:1 | 7.05:1 | 7:1 |
| Text | diff_added_word `#59C977` | background `#10141A` | 8.84:1 | 8.84:1 | 7:1 |
| Text | diff_removed_word `#FA7C75` | background `#10141A` | 7.22:1 | 7.22:1 | 7:1 |
| Status bar | status_bar_text `#D8DFE8` | status_bar_bg `#0A0E13` | 14.41:1 | 14.41:1 | 7:1 |
| Status bar | status_bar_strong `#99C6FF` | status_bar_bg `#0A0E13` | 10.94:1 | 10.94:1 | 7:1 |
| Status bar | status_bar_dim `#A3AEBD` | status_bar_bg `#0A0E13` | 8.61:1 | 8.61:1 | 7:1 |
| Status bar | status_bar_good `#59C977` | status_bar_bg `#0A0E13` | 9.26:1 | 9.26:1 | 7:1 |
| Status bar | status_bar_warn `#FFDA70` | status_bar_bg `#0A0E13` | 14.30:1 | 14.30:1 | 7:1 |
| Status bar | status_bar_bad `#FA7C75` | status_bar_bg `#0A0E13` | 7.56:1 | 7.56:1 | 7:1 |
| Status bar | status_bar_critical `#FF9A92` | status_bar_bg `#0A0E13` | 9.48:1 | 9.48:1 | 7:1 |
| Completion menu | ui_text `#D8DFE8` | completion_menu_bg `#1B2029` | 12.17:1 | 12.17:1 | 7:1 |
| Completion menu | ui_text `#D8DFE8` | completion_menu_current_bg `#28364A` | 5.33:1 ✗ | 9.11:1 | 7:1 |
| Completion menu | ui_text `#D8DFE8` | completion_menu_meta_bg `#1B2029` | 12.17:1 | 12.17:1 | 7:1 |
| Completion menu | ui_text `#D8DFE8` | completion_menu_meta_current_bg `#28364A` | 5.33:1 ✗ | 9.11:1 | 7:1 |
| Diff lines | ui_text `#D8DFE8` | diff_added `#1b2f28` | 10.54:1 | 10.54:1 | 7:1 |
| Diff lines | ui_text `#D8DFE8` | diff_removed `#332428` | 10.99:1 | 10.99:1 | 7:1 |
| Selection | ui_text `#D8DFE8` | selection_bg `#475971` | 5.33:1 | 5.33:1 | 4.5:1 |
| Borders | ui_border `#95A2A9` | background `#10141A` | 7.05:1 | 7.05:1 | 3:1 |
| Borders | banner_border `#95A2A9` | background `#10141A` | 7.05:1 | 7.05:1 | 3:1 |
| Borders | input_rule `#95A2A9` | background `#10141A` | 7.05:1 | 7.05:1 | 3:1 |
| Borders | session_border `#95A2A9` | background `#10141A` | 7.05:1 | 7.05:1 | 3:1 |
| Borders | response_border `#99C6FF` | background `#10141A` | 10.45:1 | 10.45:1 | 3:1 |

Patched: `completion_menu_current_bg` → row_active, `completion_menu_meta_current_bg` → row_active

### hyprland-preview-share-picker.css: passes as generated

| Area | Foreground | On | Generated | Shipped | Needs |
|---|---|---|---|---|---|
| Text | foreground `#D8DFE8` | background `#10141A` | 13.76:1 | 13.76:1 | 7:1 |
| Selected tab | selected_tab `#99C6FF` | background `#10141A` | 10.45:1 | 10.45:1 | 7:1 |
| Cards | text `#D8DFE8` | card_bg `#1B2029` | 12.17:1 | 12.17:1 | 7:1 |
| Region button | text_dark `#10141A` | accent `#99C6FF` | 10.45:1 | 10.45:1 | 7:1 |
| Region button, hover | text_dark `#10141A` | accent_hover `#B4D5FF` | 12.23:1 | 12.23:1 | 7:1 |
| Focus border | accent `#99C6FF` | background `#10141A` | 10.45:1 | 10.45:1 | 3:1 |

### obsidian.css: 2 failing pair(s) patched

| Area | Foreground | On | Generated | Shipped | Needs |
|---|---|---|---|---|---|
| Text | text-normal `#D8DFE8` | background-primary `#10141A` | 13.76:1 | 13.76:1 | 7:1 |
| Text | text-title-h1 `#FA7C75` | background-primary `#10141A` | 7.22:1 | 7.22:1 | 7:1 |
| Text | text-title-h2 `#59C977` | background-primary `#10141A` | 8.84:1 | 8.84:1 | 7:1 |
| Text | text-title-h3 `#FFDA70` | background-primary `#10141A` | 13.65:1 | 13.65:1 | 7:1 |
| Text | text-title-h4 `#99C6FF` | background-primary `#10141A` | 10.45:1 | 10.45:1 | 7:1 |
| Text | text-title-h5 `#FFBDE8` | background-primary `#10141A` | 12.05:1 | 12.05:1 | 7:1 |
| Text | text-link `#99C6FF` | background-primary `#10141A` | 10.45:1 | 10.45:1 | 7:1 |
| Text | text-accent `#99C6FF` | background-primary `#10141A` | 10.45:1 | 10.45:1 | 7:1 |
| Text | text-muted `#9ca2aa` | background-primary `#10141A` | 7.18:1 | 7.18:1 | 7:1 |
| Text | text-faint `#95A2A9` | background-primary `#10141A` | 4.89:1 ✗ | 7.05:1 | 7:1 |
| Text | code-normal `#A8F6FF` | background-primary `#10141A` | 15.21:1 | 15.21:1 | 7:1 |
| Text | text-error `#FA7C75` | background-primary `#10141A` | 7.22:1 | 7.22:1 | 7:1 |
| Text | text-success `#59C977` | background-primary `#10141A` | 8.84:1 | 8.84:1 | 7:1 |
| Tags | tag-color `#A8F6FF` | tag-background `#252F3E` | 2.16:1 ✗ | 11.12:1 | 7:1 |
| Selection | text-normal `#D8DFE8` | text-selection `#475971` | 5.33:1 | 5.33:1 | 4.5:1 |
| Borders | background-modifier-border `#95A2A9` | background-primary `#10141A` | 7.05:1 | 7.05:1 | 3:1 |

Patched: `text-faint` → muted, `tag-background` → row_hover

## `omarchy-beacon-redgreen-dark-theme`

### btop.theme: 1 failing pair(s) patched

| Area | Foreground | On | Generated | Shipped | Needs |
|---|---|---|---|---|---|
| Text | main_fg `#D8DFE8` | main_bg `#10141A` | 13.76:1 | 13.76:1 | 7:1 |
| Text | title `#D8DFE8` | main_bg `#10141A` | 13.76:1 | 13.76:1 | 7:1 |
| Text | hi_fg `#9BC6FF` | main_bg `#10141A` | 10.48:1 | 10.48:1 | 7:1 |
| Text | inactive_fg `#95A2A9` | main_bg `#10141A` | 7.05:1 | 7.05:1 | 7:1 |
| Text | graph_text `#EDF1F6` | main_bg `#10141A` | 16.28:1 | 16.28:1 | 7:1 |
| Text | proc_misc `#EDF1F6` | main_bg `#10141A` | 16.28:1 | 16.28:1 | 7:1 |
| Selected process row | selected_fg `#FFFFFF` | selected_bg `#475971` | 4.06:1 ✗ | 7.15:1 | 7:1 |
| Box outlines | cpu_box `#F9D0FF` | main_bg `#10141A` | 13.63:1 | 13.63:1 | 3:1 |
| Box outlines | mem_box `#8DFEDB` | main_bg `#10141A` | 15.24:1 | 15.24:1 | 3:1 |
| Box outlines | net_box `#F5825E` | main_bg `#10141A` | 7.24:1 | 7.24:1 | 3:1 |
| Box outlines | proc_box `#9BC6FF` | main_bg `#10141A` | 10.48:1 | 10.48:1 | 3:1 |
| Box outlines | div_line `#95A2A9` | main_bg `#10141A` | 7.05:1 | 7.05:1 | 3:1 |

Patched: `selected_fg` → bright_foreground

### helix.toml: passes as generated

| Area | Foreground | On | Generated | Shipped | Needs |
|---|---|---|---|---|---|
| Syntax and text | foreground `#D8DFE8` | background `#10141A` | 13.76:1 | 13.76:1 | 7:1 |
| Syntax and text | color1 `#F5825E` | background `#10141A` | 7.24:1 | 7.24:1 | 7:1 |
| Syntax and text | color2 `#8DFEDB` | background `#10141A` | 15.24:1 | 15.24:1 | 7:1 |
| Syntax and text | color3 `#FCCA39` | background `#10141A` | 12.00:1 | 12.00:1 | 7:1 |
| Syntax and text | color4 `#9BC6FF` | background `#10141A` | 10.48:1 | 10.48:1 | 7:1 |
| Syntax and text | color5 `#F9D0FF` | background `#10141A` | 13.63:1 | 13.63:1 | 7:1 |
| Syntax and text | color6 `#53C1DA` | background `#10141A` | 8.80:1 | 8.80:1 | 7:1 |
| Syntax and text | color8 `#95A2A9` | background `#10141A` | 7.05:1 | 7.05:1 | 7:1 |
| Statusline band | background `#10141A` | foreground `#D8DFE8` | 13.76:1 | 13.76:1 | 7:1 |
| Statusline band | background `#10141A` | color8 `#95A2A9` | 7.05:1 | 7.05:1 | 7:1 |
| Statusline band | background `#10141A` | color4 `#9BC6FF` | 10.48:1 | 10.48:1 | 7:1 |
| Statusline band | background `#10141A` | color2 `#8DFEDB` | 15.24:1 | 15.24:1 | 7:1 |
| Statusline band | background `#10141A` | color5 `#F9D0FF` | 13.63:1 | 13.63:1 | 7:1 |
| Selection | selection_foreground `#FFFFFF` | selection_background `#475971` | 7.15:1 | 7.15:1 | 7:1 |
| Cursor | background `#10141A` | cursor `#FFFFFF` | 18.47:1 | 18.47:1 | 7:1 |
| Focused text | foreground `#D8DFE8` | lighter_background `#1B2029` | 12.17:1 | 12.17:1 | 7:1 |
| Menu selection | background `#10141A` | foreground `#D8DFE8` | 13.76:1 | 13.76:1 | 7:1 |
| Cursor line and highlights | color1 `#F5825E` | lighter_background `#1B2029` | 6.41:1 | 6.41:1 | 4.5:1 |
| Cursor line and highlights | color2 `#8DFEDB` | lighter_background `#1B2029` | 13.49:1 | 13.49:1 | 4.5:1 |
| Cursor line and highlights | color3 `#FCCA39` | lighter_background `#1B2029` | 10.62:1 | 10.62:1 | 4.5:1 |
| Cursor line and highlights | color4 `#9BC6FF` | lighter_background `#1B2029` | 9.27:1 | 9.27:1 | 4.5:1 |
| Cursor line and highlights | color5 `#F9D0FF` | lighter_background `#1B2029` | 12.06:1 | 12.06:1 | 4.5:1 |
| Cursor line and highlights | color6 `#53C1DA` | lighter_background `#1B2029` | 7.79:1 | 7.79:1 | 4.5:1 |
| Cursor line and highlights | color8 `#95A2A9` | lighter_background `#1B2029` | 6.24:1 | 6.24:1 | 4.5:1 |

### pi.json: 3 failing pair(s) patched

| Area | Foreground | On | Generated | Shipped | Needs |
|---|---|---|---|---|---|
| Text | foreground `#D8DFE8` | background `#10141A` | 13.76:1 | 13.76:1 | 7:1 |
| Text | accent `#9BC6FF` | background `#10141A` | 10.48:1 | 10.48:1 | 7:1 |
| Text | color1 `#F5825E` | background `#10141A` | 7.24:1 | 7.24:1 | 7:1 |
| Text | color2 `#8DFEDB` | background `#10141A` | 15.24:1 | 15.24:1 | 7:1 |
| Text | color3 `#FCCA39` | background `#10141A` | 12.00:1 | 12.00:1 | 7:1 |
| Text | color4 `#9BC6FF` | background `#10141A` | 10.48:1 | 10.48:1 | 7:1 |
| Text | color5 `#F9D0FF` | background `#10141A` | 13.63:1 | 13.63:1 | 7:1 |
| Text | color6 `#53C1DA` | background `#10141A` | 8.80:1 | 8.80:1 | 7:1 |
| Text | color8 `#95A2A9` | background `#10141A` | 7.05:1 | 7.05:1 | 7:1 |
| Text | mutedText `#A3AEBD` | background `#10141A` | 6.51:1 ✗ | 8.22:1 | 7:1 |
| Text | dimText `#95A2A9` | background `#10141A` | 3.98:1 ✗ | 7.05:1 | 7:1 |
| Message panels | foreground `#D8DFE8` | panel `#1c2026` | 12.18:1 | 12.18:1 | 7:1 |
| Message panels | foreground `#D8DFE8` | panelAlt `#24282f` | 11.02:1 | 11.02:1 | 7:1 |
| Message panels | foreground `#D8DFE8` | selectedBackground `#2f3b4c` | 8.45:1 | 8.45:1 | 7:1 |
| Message panels | foreground `#D8DFE8` | panelPending `#212935` | 10.91:1 | 10.91:1 | 7:1 |
| Message panels | foreground `#D8DFE8` | panelSuccess `#1f3031` | 10.25:1 | 10.25:1 | 7:1 |
| Message panels | foreground `#D8DFE8` | panelError `#2b2122` | 11.64:1 | 11.64:1 | 7:1 |
| Tool titles | accent `#9BC6FF` | panelPending `#212935` | 8.31:1 | 8.31:1 | 7:1 |
| Tool titles | accent `#9BC6FF` | panelSuccess `#1f3031` | 7.81:1 | 7.81:1 | 7:1 |
| Tool titles | accent `#9BC6FF` | panelError `#2b2122` | 8.87:1 | 8.87:1 | 7:1 |
| Input border | border `#5F6973` | background `#10141A` | 2.31:1 ✗ | 3.30:1 | 3:1 |

Patched: `mutedText` → dark_foreground, `dimText` → muted, `border` → border

### claude.json: 1 failing pair(s) patched

| Area | Foreground | On | Generated | Shipped | Needs |
|---|---|---|---|---|---|
| Text | text `#D8DFE8` | @background `#10141A` | 13.76:1 | 13.76:1 | 7:1 |
| Text | subtle `#95A2A9` | @background `#10141A` | 7.05:1 | 7.05:1 | 7:1 |
| Text | inactive `#A3AEBD` | @background `#10141A` | 5.59:1 ✗ | 8.22:1 | 7:1 |
| Text | suggestion `#53C1DA` | @background `#10141A` | 8.80:1 | 8.80:1 | 7:1 |
| Text | permission `#9BC6FF` | @background `#10141A` | 10.48:1 | 10.48:1 | 7:1 |
| Text | remember `#FCCA39` | @background `#10141A` | 12.00:1 | 12.00:1 | 7:1 |
| Text | success `#8DFEDB` | @background `#10141A` | 15.24:1 | 15.24:1 | 7:1 |
| Text | error `#F5825E` | @background `#10141A` | 7.24:1 | 7.24:1 | 7:1 |
| Text | warning `#FCCA39` | @background `#10141A` | 12.00:1 | 12.00:1 | 7:1 |
| Text | merged `#F9D0FF` | @background `#10141A` | 13.63:1 | 13.63:1 | 7:1 |
| Text | planMode `#53C1DA` | @background `#10141A` | 8.80:1 | 8.80:1 | 7:1 |
| Text | autoAccept `#FCCA39` | @background `#10141A` | 12.00:1 | 12.00:1 | 7:1 |
| Text | claude `#9BC6FF` | @background `#10141A` | 10.48:1 | 10.48:1 | 7:1 |
| Badges | inverseText `#10141A` | claude `#9BC6FF` | 10.48:1 | 10.48:1 | 7:1 |
| Message backgrounds | text `#D8DFE8` | userMessageBackground `#1c2026` | 12.18:1 | 12.18:1 | 7:1 |
| Message backgrounds | text `#D8DFE8` | userMessageBackgroundHover `#24282f` | 11.02:1 | 11.02:1 | 7:1 |
| Message backgrounds | text `#D8DFE8` | bashMessageBackgroundColor `#1c2026` | 12.18:1 | 12.18:1 | 7:1 |
| Message backgrounds | text `#D8DFE8` | memoryBackgroundColor `#1c2026` | 12.18:1 | 12.18:1 | 7:1 |
| Diff lines | text `#D8DFE8` | diffAdded `#233737` | 9.35:1 | 9.35:1 | 7:1 |
| Diff lines | text `#D8DFE8` | diffRemoved `#322524` | 10.97:1 | 10.97:1 | 7:1 |
| Diff words and selection | text `#D8DFE8` | diffAddedWord `#385f58` | 5.31:1 | 5.31:1 | 4.5:1 |
| Diff words and selection | text `#D8DFE8` | diffRemovedWord `#593730` | 7.77:1 | 7.77:1 | 4.5:1 |
| Diff words and selection | text `#D8DFE8` | selectionBg `#475971` | 5.33:1 | 5.33:1 | 4.5:1 |
| Prompt border | promptBorder `#9BC6FF` | @background `#10141A` | 10.48:1 | 10.48:1 | 3:1 |

Patched: `inactive` → dark_foreground

### t3code.json: 1 failing pair(s) patched

| Area | Foreground | On | Generated | Shipped | Needs |
|---|---|---|---|---|---|
| Text | text `#D8DFE8` | chrome `#10141A` | 13.76:1 | 13.76:1 | 7:1 |
| Toolbar | toolbarForeground `#D8DFE8` | toolbar `#10141A` | 13.76:1 | 13.76:1 | 7:1 |
| Sidebar | sidebarForeground `#D8DFE8` | sidebar `#0A0E13` | 14.41:1 | 14.41:1 | 7:1 |
| Code | codeForeground `#D8DFE8` | codeBackground `#0A0E13` | 14.41:1 | 14.41:1 | 7:1 |
| Terminal | terminalForeground `#D8DFE8` | terminalBackground `#10141A` | 13.76:1 | 13.76:1 | 7:1 |
| Status text | error `#eba38e` | chrome `#10141A` | 8.94:1 | 8.94:1 | 7:1 |
| Status text | warning `#efd176` | chrome `#10141A` | 12.36:1 | 12.36:1 | 7:1 |
| Sidebar rows | sidebarForeground `#D8DFE8` | sidebarRowHover `#161b20` | 12.91:1 | 12.91:1 | 7:1 |
| Sidebar rows | sidebarForeground `#D8DFE8` | sidebarRowActive `#242f3d` | 10.10:1 | 10.10:1 | 7:1 |
| Sidebar rows | sidebarForeground `#D8DFE8` | sidebarRowSelected `#28364A` | 5.33:1 ✗ | 9.11:1 | 7:1 |
| Terminal selection | terminalForeground `#D8DFE8` | terminalSelection `#475971` | 5.33:1 | 5.33:1 | 4.5:1 |
| Borders and focus | border `#95A2A9` | chrome `#10141A` | 7.05:1 | 7.05:1 | 3:1 |
| Borders and focus | toolbarBorder `#95A2A9` | chrome `#10141A` | 7.05:1 | 7.05:1 | 3:1 |
| Borders and focus | focus `#9BC6FF` | chrome `#10141A` | 10.48:1 | 10.48:1 | 3:1 |
| Borders and focus | sidebarBorder `#95A2A9` | sidebar `#0A0E13` | 7.39:1 | 7.39:1 | 3:1 |

Patched: `sidebarRowSelected` → row_active

### hermes.yaml: 2 failing pair(s) patched

| Area | Foreground | On | Generated | Shipped | Needs |
|---|---|---|---|---|---|
| Text | ui_text `#D8DFE8` | background `#10141A` | 13.76:1 | 13.76:1 | 7:1 |
| Text | ui_primary `#9BC6FF` | background `#10141A` | 10.48:1 | 10.48:1 | 7:1 |
| Text | ui_label `#9BC6FF` | background `#10141A` | 10.48:1 | 10.48:1 | 7:1 |
| Text | ui_ok `#8DFEDB` | background `#10141A` | 15.24:1 | 15.24:1 | 7:1 |
| Text | ui_warn `#FCCA39` | background `#10141A` | 12.00:1 | 12.00:1 | 7:1 |
| Text | ui_error `#F5825E` | background `#10141A` | 7.24:1 | 7.24:1 | 7:1 |
| Text | ui_tool `#53C1DA` | background `#10141A` | 8.80:1 | 8.80:1 | 7:1 |
| Text | ui_thinking `#A3AEBD` | background `#10141A` | 8.22:1 | 8.22:1 | 7:1 |
| Text | banner_title `#9BC6FF` | background `#10141A` | 10.48:1 | 10.48:1 | 7:1 |
| Text | banner_dim `#A3AEBD` | background `#10141A` | 8.22:1 | 8.22:1 | 7:1 |
| Text | banner_text `#D8DFE8` | background `#10141A` | 13.76:1 | 13.76:1 | 7:1 |
| Text | prompt `#FFFFFF` | background `#10141A` | 18.47:1 | 18.47:1 | 7:1 |
| Text | shell_dollar `#9BC6FF` | background `#10141A` | 10.48:1 | 10.48:1 | 7:1 |
| Text | session_label `#9BC6FF` | background `#10141A` | 10.48:1 | 10.48:1 | 7:1 |
| Text | syntax_string `#8DFEDB` | background `#10141A` | 15.24:1 | 15.24:1 | 7:1 |
| Text | syntax_number `#FCCA39` | background `#10141A` | 12.00:1 | 12.00:1 | 7:1 |
| Text | syntax_keyword `#F9D0FF` | background `#10141A` | 13.63:1 | 13.63:1 | 7:1 |
| Text | syntax_comment `#95A2A9` | background `#10141A` | 7.05:1 | 7.05:1 | 7:1 |
| Text | diff_added_word `#8DFEDB` | background `#10141A` | 15.24:1 | 15.24:1 | 7:1 |
| Text | diff_removed_word `#F5825E` | background `#10141A` | 7.24:1 | 7.24:1 | 7:1 |
| Status bar | status_bar_text `#D8DFE8` | status_bar_bg `#0A0E13` | 14.41:1 | 14.41:1 | 7:1 |
| Status bar | status_bar_strong `#9BC6FF` | status_bar_bg `#0A0E13` | 10.98:1 | 10.98:1 | 7:1 |
| Status bar | status_bar_dim `#A3AEBD` | status_bar_bg `#0A0E13` | 8.61:1 | 8.61:1 | 7:1 |
| Status bar | status_bar_good `#8DFEDB` | status_bar_bg `#0A0E13` | 15.97:1 | 15.97:1 | 7:1 |
| Status bar | status_bar_warn `#FCCA39` | status_bar_bg `#0A0E13` | 12.58:1 | 12.58:1 | 7:1 |
| Status bar | status_bar_bad `#F5825E` | status_bar_bg `#0A0E13` | 7.59:1 | 7.59:1 | 7:1 |
| Status bar | status_bar_critical `#FF9B7D` | status_bar_bg `#0A0E13` | 9.43:1 | 9.43:1 | 7:1 |
| Completion menu | ui_text `#D8DFE8` | completion_menu_bg `#1B2029` | 12.17:1 | 12.17:1 | 7:1 |
| Completion menu | ui_text `#D8DFE8` | completion_menu_current_bg `#28364A` | 5.33:1 ✗ | 9.11:1 | 7:1 |
| Completion menu | ui_text `#D8DFE8` | completion_menu_meta_bg `#1B2029` | 12.17:1 | 12.17:1 | 7:1 |
| Completion menu | ui_text `#D8DFE8` | completion_menu_meta_current_bg `#28364A` | 5.33:1 ✗ | 9.11:1 | 7:1 |
| Diff lines | ui_text `#D8DFE8` | diff_added `#233737` | 9.35:1 | 9.35:1 | 7:1 |
| Diff lines | ui_text `#D8DFE8` | diff_removed `#322524` | 10.97:1 | 10.97:1 | 7:1 |
| Selection | ui_text `#D8DFE8` | selection_bg `#475971` | 5.33:1 | 5.33:1 | 4.5:1 |
| Borders | ui_border `#95A2A9` | background `#10141A` | 7.05:1 | 7.05:1 | 3:1 |
| Borders | banner_border `#95A2A9` | background `#10141A` | 7.05:1 | 7.05:1 | 3:1 |
| Borders | input_rule `#95A2A9` | background `#10141A` | 7.05:1 | 7.05:1 | 3:1 |
| Borders | session_border `#95A2A9` | background `#10141A` | 7.05:1 | 7.05:1 | 3:1 |
| Borders | response_border `#9BC6FF` | background `#10141A` | 10.48:1 | 10.48:1 | 3:1 |

Patched: `completion_menu_current_bg` → row_active, `completion_menu_meta_current_bg` → row_active

### hyprland-preview-share-picker.css: passes as generated

| Area | Foreground | On | Generated | Shipped | Needs |
|---|---|---|---|---|---|
| Text | foreground `#D8DFE8` | background `#10141A` | 13.76:1 | 13.76:1 | 7:1 |
| Selected tab | selected_tab `#9BC6FF` | background `#10141A` | 10.48:1 | 10.48:1 | 7:1 |
| Cards | text `#D8DFE8` | card_bg `#1B2029` | 12.17:1 | 12.17:1 | 7:1 |
| Region button | text_dark `#10141A` | accent `#9BC6FF` | 10.48:1 | 10.48:1 | 7:1 |
| Region button, hover | text_dark `#10141A` | accent_hover `#B5D5FF` | 12.25:1 | 12.25:1 | 7:1 |
| Focus border | accent `#9BC6FF` | background `#10141A` | 10.48:1 | 10.48:1 | 3:1 |

### obsidian.css: 2 failing pair(s) patched

| Area | Foreground | On | Generated | Shipped | Needs |
|---|---|---|---|---|---|
| Text | text-normal `#D8DFE8` | background-primary `#10141A` | 13.76:1 | 13.76:1 | 7:1 |
| Text | text-title-h1 `#F5825E` | background-primary `#10141A` | 7.24:1 | 7.24:1 | 7:1 |
| Text | text-title-h2 `#8DFEDB` | background-primary `#10141A` | 15.24:1 | 15.24:1 | 7:1 |
| Text | text-title-h3 `#FCCA39` | background-primary `#10141A` | 12.00:1 | 12.00:1 | 7:1 |
| Text | text-title-h4 `#9BC6FF` | background-primary `#10141A` | 10.48:1 | 10.48:1 | 7:1 |
| Text | text-title-h5 `#F9D0FF` | background-primary `#10141A` | 13.63:1 | 13.63:1 | 7:1 |
| Text | text-link `#9BC6FF` | background-primary `#10141A` | 10.48:1 | 10.48:1 | 7:1 |
| Text | text-accent `#9BC6FF` | background-primary `#10141A` | 10.48:1 | 10.48:1 | 7:1 |
| Text | text-muted `#9ca2aa` | background-primary `#10141A` | 7.18:1 | 7.18:1 | 7:1 |
| Text | text-faint `#95A2A9` | background-primary `#10141A` | 4.89:1 ✗ | 7.05:1 | 7:1 |
| Text | code-normal `#53C1DA` | background-primary `#10141A` | 8.80:1 | 8.80:1 | 7:1 |
| Text | text-error `#F5825E` | background-primary `#10141A` | 7.24:1 | 7.24:1 | 7:1 |
| Text | text-success `#8DFEDB` | background-primary `#10141A` | 15.24:1 | 15.24:1 | 7:1 |
| Tags | tag-color `#53C1DA` | tag-background `#1B2029` | 1.25:1 ✗ | 7.79:1 | 7:1 |
| Selection | text-normal `#D8DFE8` | text-selection `#475971` | 5.33:1 | 5.33:1 | 4.5:1 |
| Borders | background-modifier-border `#95A2A9` | background-primary `#10141A` | 7.05:1 | 7.05:1 | 3:1 |

Patched: `text-faint` → muted, `tag-background` → lighter_background

## `omarchy-beacon-blueyellow-dark-theme`

### btop.theme: 1 failing pair(s) patched

| Area | Foreground | On | Generated | Shipped | Needs |
|---|---|---|---|---|---|
| Text | main_fg `#D8DFE8` | main_bg `#10141A` | 13.76:1 | 13.76:1 | 7:1 |
| Text | title `#D8DFE8` | main_bg `#10141A` | 13.76:1 | 13.76:1 | 7:1 |
| Text | hi_fg `#FF968F` | main_bg `#10141A` | 8.80:1 | 8.80:1 | 7:1 |
| Text | inactive_fg `#95A2A9` | main_bg `#10141A` | 7.05:1 | 7.05:1 | 7:1 |
| Text | graph_text `#EDF1F6` | main_bg `#10141A` | 16.28:1 | 16.28:1 | 7:1 |
| Text | proc_misc `#EDF1F6` | main_bg `#10141A` | 16.28:1 | 16.28:1 | 7:1 |
| Selected process row | selected_fg `#FFFFFF` | selected_bg `#475971` | 3.41:1 ✗ | 7.15:1 | 7:1 |
| Box outlines | cpu_box `#FFBEDE` | main_bg `#10141A` | 12.02:1 | 12.02:1 | 3:1 |
| Box outlines | mem_box `#59B55F` | main_bg `#10141A` | 7.21:1 | 7.21:1 | 3:1 |
| Box outlines | net_box `#FF968F` | main_bg `#10141A` | 8.80:1 | 8.80:1 | 3:1 |
| Box outlines | proc_box `#FF968F` | main_bg `#10141A` | 8.80:1 | 8.80:1 | 3:1 |
| Box outlines | div_line `#95A2A9` | main_bg `#10141A` | 7.05:1 | 7.05:1 | 3:1 |

Patched: `selected_fg` → bright_foreground

### helix.toml: passes as generated

| Area | Foreground | On | Generated | Shipped | Needs |
|---|---|---|---|---|---|
| Syntax and text | foreground `#D8DFE8` | background `#10141A` | 13.76:1 | 13.76:1 | 7:1 |
| Syntax and text | color1 `#FF968F` | background `#10141A` | 8.80:1 | 8.80:1 | 7:1 |
| Syntax and text | color2 `#59B55F` | background `#10141A` | 7.21:1 | 7.21:1 | 7:1 |
| Syntax and text | color3 `#FFE7B4` | background `#10141A` | 15.25:1 | 15.25:1 | 7:1 |
| Syntax and text | color4 `#9DC5FF` | background `#10141A` | 10.43:1 | 10.43:1 | 7:1 |
| Syntax and text | color5 `#FFBEDE` | background `#10141A` | 12.02:1 | 12.02:1 | 7:1 |
| Syntax and text | color6 `#75F0F0` | background `#10141A` | 13.61:1 | 13.61:1 | 7:1 |
| Syntax and text | color8 `#95A2A9` | background `#10141A` | 7.05:1 | 7.05:1 | 7:1 |
| Statusline band | background `#10141A` | foreground `#D8DFE8` | 13.76:1 | 13.76:1 | 7:1 |
| Statusline band | background `#10141A` | color8 `#95A2A9` | 7.05:1 | 7.05:1 | 7:1 |
| Statusline band | background `#10141A` | color4 `#9DC5FF` | 10.43:1 | 10.43:1 | 7:1 |
| Statusline band | background `#10141A` | color2 `#59B55F` | 7.21:1 | 7.21:1 | 7:1 |
| Statusline band | background `#10141A` | color5 `#FFBEDE` | 12.02:1 | 12.02:1 | 7:1 |
| Selection | selection_foreground `#FFFFFF` | selection_background `#475971` | 7.15:1 | 7.15:1 | 7:1 |
| Cursor | background `#10141A` | cursor `#FFFFFF` | 18.47:1 | 18.47:1 | 7:1 |
| Focused text | foreground `#D8DFE8` | lighter_background `#1B2029` | 12.17:1 | 12.17:1 | 7:1 |
| Menu selection | background `#10141A` | foreground `#D8DFE8` | 13.76:1 | 13.76:1 | 7:1 |
| Cursor line and highlights | color1 `#FF968F` | lighter_background `#1B2029` | 7.79:1 | 7.79:1 | 4.5:1 |
| Cursor line and highlights | color2 `#59B55F` | lighter_background `#1B2029` | 6.38:1 | 6.38:1 | 4.5:1 |
| Cursor line and highlights | color3 `#FFE7B4` | lighter_background `#1B2029` | 13.49:1 | 13.49:1 | 4.5:1 |
| Cursor line and highlights | color4 `#9DC5FF` | lighter_background `#1B2029` | 9.23:1 | 9.23:1 | 4.5:1 |
| Cursor line and highlights | color5 `#FFBEDE` | lighter_background `#1B2029` | 10.64:1 | 10.64:1 | 4.5:1 |
| Cursor line and highlights | color6 `#75F0F0` | lighter_background `#1B2029` | 12.04:1 | 12.04:1 | 4.5:1 |
| Cursor line and highlights | color8 `#95A2A9` | lighter_background `#1B2029` | 6.24:1 | 6.24:1 | 4.5:1 |

### pi.json: 3 failing pair(s) patched

| Area | Foreground | On | Generated | Shipped | Needs |
|---|---|---|---|---|---|
| Text | foreground `#D8DFE8` | background `#10141A` | 13.76:1 | 13.76:1 | 7:1 |
| Text | accent `#FF968F` | background `#10141A` | 8.80:1 | 8.80:1 | 7:1 |
| Text | color1 `#FF968F` | background `#10141A` | 8.80:1 | 8.80:1 | 7:1 |
| Text | color2 `#59B55F` | background `#10141A` | 7.21:1 | 7.21:1 | 7:1 |
| Text | color3 `#FFE7B4` | background `#10141A` | 15.25:1 | 15.25:1 | 7:1 |
| Text | color4 `#9DC5FF` | background `#10141A` | 10.43:1 | 10.43:1 | 7:1 |
| Text | color5 `#FFBEDE` | background `#10141A` | 12.02:1 | 12.02:1 | 7:1 |
| Text | color6 `#75F0F0` | background `#10141A` | 13.61:1 | 13.61:1 | 7:1 |
| Text | color8 `#95A2A9` | background `#10141A` | 7.05:1 | 7.05:1 | 7:1 |
| Text | mutedText `#A3AEBD` | background `#10141A` | 6.51:1 ✗ | 8.22:1 | 7:1 |
| Text | dimText `#95A2A9` | background `#10141A` | 3.98:1 ✗ | 7.05:1 | 7:1 |
| Message panels | foreground `#D8DFE8` | panel `#1c2026` | 12.18:1 | 12.18:1 | 7:1 |
| Message panels | foreground `#D8DFE8` | panelAlt `#24282f` | 11.02:1 | 11.02:1 | 7:1 |
| Message panels | foreground `#D8DFE8` | selectedBackground `#453134` | 8.98:1 | 8.98:1 | 7:1 |
| Message panels | foreground `#D8DFE8` | panelPending `#2d2428` | 11.22:1 | 11.22:1 | 7:1 |
| Message panels | foreground `#D8DFE8` | panelSuccess `#192722` | 11.55:1 | 11.55:1 | 7:1 |
| Message panels | foreground `#D8DFE8` | panelError `#2d2428` | 11.22:1 | 11.22:1 | 7:1 |
| Tool titles | accent `#FF968F` | panelPending `#2d2428` | 7.18:1 | 7.18:1 | 7:1 |
| Tool titles | accent `#FF968F` | panelSuccess `#192722` | 7.39:1 | 7.39:1 | 7:1 |
| Tool titles | accent `#FF968F` | panelError `#2d2428` | 7.18:1 | 7.18:1 | 7:1 |
| Input border | border `#5F6973` | background `#10141A` | 2.31:1 ✗ | 3.30:1 | 3:1 |

Patched: `mutedText` → dark_foreground, `dimText` → muted, `border` → border

### claude.json: 1 failing pair(s) patched

| Area | Foreground | On | Generated | Shipped | Needs |
|---|---|---|---|---|---|
| Text | text `#D8DFE8` | @background `#10141A` | 13.76:1 | 13.76:1 | 7:1 |
| Text | subtle `#95A2A9` | @background `#10141A` | 7.05:1 | 7.05:1 | 7:1 |
| Text | inactive `#A3AEBD` | @background `#10141A` | 5.59:1 ✗ | 8.22:1 | 7:1 |
| Text | suggestion `#75F0F0` | @background `#10141A` | 13.61:1 | 13.61:1 | 7:1 |
| Text | permission `#9DC5FF` | @background `#10141A` | 10.43:1 | 10.43:1 | 7:1 |
| Text | remember `#FFE7B4` | @background `#10141A` | 15.25:1 | 15.25:1 | 7:1 |
| Text | success `#59B55F` | @background `#10141A` | 7.21:1 | 7.21:1 | 7:1 |
| Text | error `#FF968F` | @background `#10141A` | 8.80:1 | 8.80:1 | 7:1 |
| Text | warning `#FFE7B4` | @background `#10141A` | 15.25:1 | 15.25:1 | 7:1 |
| Text | merged `#FFBEDE` | @background `#10141A` | 12.02:1 | 12.02:1 | 7:1 |
| Text | planMode `#75F0F0` | @background `#10141A` | 13.61:1 | 13.61:1 | 7:1 |
| Text | autoAccept `#FFE7B4` | @background `#10141A` | 15.25:1 | 15.25:1 | 7:1 |
| Text | claude `#FF968F` | @background `#10141A` | 8.80:1 | 8.80:1 | 7:1 |
| Badges | inverseText `#10141A` | claude `#FF968F` | 8.80:1 | 8.80:1 | 7:1 |
| Message backgrounds | text `#D8DFE8` | userMessageBackground `#1c2026` | 12.18:1 | 12.18:1 | 7:1 |
| Message backgrounds | text `#D8DFE8` | userMessageBackgroundHover `#24282f` | 11.02:1 | 11.02:1 | 7:1 |
| Message backgrounds | text `#D8DFE8` | bashMessageBackgroundColor `#1c2026` | 12.18:1 | 12.18:1 | 7:1 |
| Message backgrounds | text `#D8DFE8` | memoryBackgroundColor `#1c2026` | 12.18:1 | 12.18:1 | 7:1 |
| Diff lines | text `#D8DFE8` | diffAdded `#1b2c24` | 10.92:1 | 10.92:1 | 7:1 |
| Diff lines | text `#D8DFE8` | diffRemoved `#34282c` | 10.53:1 | 10.53:1 | 7:1 |
| Diff words and selection | text `#D8DFE8` | diffAddedWord `#274830` | 7.61:1 | 7.61:1 | 4.5:1 |
| Diff words and selection | text `#D8DFE8` | diffRemovedWord `#5c3e3f` | 7.06:1 | 7.06:1 | 4.5:1 |
| Diff words and selection | text `#D8DFE8` | selectionBg `#475971` | 5.33:1 | 5.33:1 | 4.5:1 |
| Prompt border | promptBorder `#FF968F` | @background `#10141A` | 8.80:1 | 8.80:1 | 3:1 |

Patched: `inactive` → dark_foreground

### t3code.json: 1 failing pair(s) patched

| Area | Foreground | On | Generated | Shipped | Needs |
|---|---|---|---|---|---|
| Text | text `#D8DFE8` | chrome `#10141A` | 13.76:1 | 13.76:1 | 7:1 |
| Toolbar | toolbarForeground `#D8DFE8` | toolbar `#10141A` | 13.76:1 | 13.76:1 | 7:1 |
| Sidebar | sidebarForeground `#D8DFE8` | sidebar `#0A0E13` | 14.41:1 | 14.41:1 | 7:1 |
| Code | codeForeground `#D8DFE8` | codeBackground `#0A0E13` | 14.41:1 | 14.41:1 | 7:1 |
| Terminal | terminalForeground `#D8DFE8` | terminalBackground `#10141A` | 13.76:1 | 13.76:1 | 7:1 |
| Status text | error `#f1b0ae` | chrome `#10141A` | 10.17:1 | 10.17:1 | 7:1 |
| Status text | warning `#f1e4c6` | chrome `#10141A` | 14.65:1 | 14.65:1 | 7:1 |
| Sidebar rows | sidebarForeground `#D8DFE8` | sidebarRowHover `#161b20` | 12.91:1 | 12.91:1 | 7:1 |
| Sidebar rows | sidebarForeground `#D8DFE8` | sidebarRowActive `#362629` | 10.67:1 | 10.67:1 | 7:1 |
| Sidebar rows | sidebarForeground `#D8DFE8` | sidebarRowSelected `#28364A` | 5.33:1 ✗ | 9.11:1 | 7:1 |
| Terminal selection | terminalForeground `#D8DFE8` | terminalSelection `#475971` | 5.33:1 | 5.33:1 | 4.5:1 |
| Borders and focus | border `#95A2A9` | chrome `#10141A` | 7.05:1 | 7.05:1 | 3:1 |
| Borders and focus | toolbarBorder `#95A2A9` | chrome `#10141A` | 7.05:1 | 7.05:1 | 3:1 |
| Borders and focus | focus `#FF968F` | chrome `#10141A` | 8.80:1 | 8.80:1 | 3:1 |
| Borders and focus | sidebarBorder `#95A2A9` | sidebar `#0A0E13` | 7.39:1 | 7.39:1 | 3:1 |

Patched: `sidebarRowSelected` → row_active

### hermes.yaml: 2 failing pair(s) patched

| Area | Foreground | On | Generated | Shipped | Needs |
|---|---|---|---|---|---|
| Text | ui_text `#D8DFE8` | background `#10141A` | 13.76:1 | 13.76:1 | 7:1 |
| Text | ui_primary `#FF968F` | background `#10141A` | 8.80:1 | 8.80:1 | 7:1 |
| Text | ui_label `#FF968F` | background `#10141A` | 8.80:1 | 8.80:1 | 7:1 |
| Text | ui_ok `#59B55F` | background `#10141A` | 7.21:1 | 7.21:1 | 7:1 |
| Text | ui_warn `#FFE7B4` | background `#10141A` | 15.25:1 | 15.25:1 | 7:1 |
| Text | ui_error `#FF968F` | background `#10141A` | 8.80:1 | 8.80:1 | 7:1 |
| Text | ui_tool `#75F0F0` | background `#10141A` | 13.61:1 | 13.61:1 | 7:1 |
| Text | ui_thinking `#A3AEBD` | background `#10141A` | 8.22:1 | 8.22:1 | 7:1 |
| Text | banner_title `#FF968F` | background `#10141A` | 8.80:1 | 8.80:1 | 7:1 |
| Text | banner_dim `#A3AEBD` | background `#10141A` | 8.22:1 | 8.22:1 | 7:1 |
| Text | banner_text `#D8DFE8` | background `#10141A` | 13.76:1 | 13.76:1 | 7:1 |
| Text | prompt `#FFFFFF` | background `#10141A` | 18.47:1 | 18.47:1 | 7:1 |
| Text | shell_dollar `#9DC5FF` | background `#10141A` | 10.43:1 | 10.43:1 | 7:1 |
| Text | session_label `#FF968F` | background `#10141A` | 8.80:1 | 8.80:1 | 7:1 |
| Text | syntax_string `#59B55F` | background `#10141A` | 7.21:1 | 7.21:1 | 7:1 |
| Text | syntax_number `#FFE7B4` | background `#10141A` | 15.25:1 | 15.25:1 | 7:1 |
| Text | syntax_keyword `#FFBEDE` | background `#10141A` | 12.02:1 | 12.02:1 | 7:1 |
| Text | syntax_comment `#95A2A9` | background `#10141A` | 7.05:1 | 7.05:1 | 7:1 |
| Text | diff_added_word `#59B55F` | background `#10141A` | 7.21:1 | 7.21:1 | 7:1 |
| Text | diff_removed_word `#FF968F` | background `#10141A` | 8.80:1 | 8.80:1 | 7:1 |
| Status bar | status_bar_text `#D8DFE8` | status_bar_bg `#0A0E13` | 14.41:1 | 14.41:1 | 7:1 |
| Status bar | status_bar_strong `#FF968F` | status_bar_bg `#0A0E13` | 9.23:1 | 9.23:1 | 7:1 |
| Status bar | status_bar_dim `#A3AEBD` | status_bar_bg `#0A0E13` | 8.61:1 | 8.61:1 | 7:1 |
| Status bar | status_bar_good `#59B55F` | status_bar_bg `#0A0E13` | 7.56:1 | 7.56:1 | 7:1 |
| Status bar | status_bar_warn `#FFE7B4` | status_bar_bg `#0A0E13` | 15.98:1 | 15.98:1 | 7:1 |
| Status bar | status_bar_bad `#FF968F` | status_bar_bg `#0A0E13` | 9.23:1 | 9.23:1 | 7:1 |
| Status bar | status_bar_critical `#FFB1A9` | status_bar_bg `#0A0E13` | 11.16:1 | 11.16:1 | 7:1 |
| Completion menu | ui_text `#D8DFE8` | completion_menu_bg `#1B2029` | 12.17:1 | 12.17:1 | 7:1 |
| Completion menu | ui_text `#D8DFE8` | completion_menu_current_bg `#28364A` | 5.33:1 ✗ | 9.11:1 | 7:1 |
| Completion menu | ui_text `#D8DFE8` | completion_menu_meta_bg `#1B2029` | 12.17:1 | 12.17:1 | 7:1 |
| Completion menu | ui_text `#D8DFE8` | completion_menu_meta_current_bg `#28364A` | 5.33:1 ✗ | 9.11:1 | 7:1 |
| Diff lines | ui_text `#D8DFE8` | diff_added `#1b2c24` | 10.92:1 | 10.92:1 | 7:1 |
| Diff lines | ui_text `#D8DFE8` | diff_removed `#34282c` | 10.53:1 | 10.53:1 | 7:1 |
| Selection | ui_text `#D8DFE8` | selection_bg `#475971` | 5.33:1 | 5.33:1 | 4.5:1 |
| Borders | ui_border `#95A2A9` | background `#10141A` | 7.05:1 | 7.05:1 | 3:1 |
| Borders | banner_border `#95A2A9` | background `#10141A` | 7.05:1 | 7.05:1 | 3:1 |
| Borders | input_rule `#95A2A9` | background `#10141A` | 7.05:1 | 7.05:1 | 3:1 |
| Borders | session_border `#95A2A9` | background `#10141A` | 7.05:1 | 7.05:1 | 3:1 |
| Borders | response_border `#FF968F` | background `#10141A` | 8.80:1 | 8.80:1 | 3:1 |

Patched: `completion_menu_current_bg` → row_active, `completion_menu_meta_current_bg` → row_active

### hyprland-preview-share-picker.css: passes as generated

| Area | Foreground | On | Generated | Shipped | Needs |
|---|---|---|---|---|---|
| Text | foreground `#D8DFE8` | background `#10141A` | 13.76:1 | 13.76:1 | 7:1 |
| Selected tab | selected_tab `#FF968F` | background `#10141A` | 8.80:1 | 8.80:1 | 7:1 |
| Cards | text `#D8DFE8` | card_bg `#1B2029` | 12.17:1 | 12.17:1 | 7:1 |
| Region button | text_dark `#10141A` | accent `#FF968F` | 8.80:1 | 8.80:1 | 7:1 |
| Region button, hover | text_dark `#10141A` | accent_hover `#B7D4FF` | 12.20:1 | 12.20:1 | 7:1 |
| Focus border | accent `#FF968F` | background `#10141A` | 8.80:1 | 8.80:1 | 3:1 |

### obsidian.css: 2 failing pair(s) patched

| Area | Foreground | On | Generated | Shipped | Needs |
|---|---|---|---|---|---|
| Text | text-normal `#D8DFE8` | background-primary `#10141A` | 13.76:1 | 13.76:1 | 7:1 |
| Text | text-title-h1 `#FF968F` | background-primary `#10141A` | 8.80:1 | 8.80:1 | 7:1 |
| Text | text-title-h2 `#59B55F` | background-primary `#10141A` | 7.21:1 | 7.21:1 | 7:1 |
| Text | text-title-h3 `#FFE7B4` | background-primary `#10141A` | 15.25:1 | 15.25:1 | 7:1 |
| Text | text-title-h4 `#9DC5FF` | background-primary `#10141A` | 10.43:1 | 10.43:1 | 7:1 |
| Text | text-title-h5 `#FFBEDE` | background-primary `#10141A` | 12.02:1 | 12.02:1 | 7:1 |
| Text | text-link `#9DC5FF` | background-primary `#10141A` | 10.43:1 | 10.43:1 | 7:1 |
| Text | text-accent `#FF968F` | background-primary `#10141A` | 8.80:1 | 8.80:1 | 7:1 |
| Text | text-muted `#9ca2aa` | background-primary `#10141A` | 7.18:1 | 7.18:1 | 7:1 |
| Text | text-faint `#95A2A9` | background-primary `#10141A` | 4.89:1 ✗ | 7.05:1 | 7:1 |
| Text | code-normal `#75F0F0` | background-primary `#10141A` | 13.61:1 | 13.61:1 | 7:1 |
| Text | text-error `#FF968F` | background-primary `#10141A` | 8.80:1 | 8.80:1 | 7:1 |
| Text | text-success `#59B55F` | background-primary `#10141A` | 7.21:1 | 7.21:1 | 7:1 |
| Tags | tag-color `#75F0F0` | tag-background `#252F3E` | 1.93:1 ✗ | 9.96:1 | 7:1 |
| Selection | text-normal `#D8DFE8` | text-selection `#475971` | 5.33:1 | 5.33:1 | 4.5:1 |
| Borders | background-modifier-border `#95A2A9` | background-primary `#10141A` | 7.05:1 | 7.05:1 | 3:1 |

Patched: `text-faint` → muted, `tag-background` → row_hover

## `omarchy-beacon-light-theme`

### btop.theme: 1 failing pair(s) patched

| Area | Foreground | On | Generated | Shipped | Needs |
|---|---|---|---|---|---|
| Text | main_fg `#2B2B28` | main_bg `#FAF9F6` | 13.49:1 | 13.49:1 | 7:1 |
| Text | title `#2B2B28` | main_bg `#FAF9F6` | 13.49:1 | 13.49:1 | 7:1 |
| Text | hi_fg `#003A77` | main_bg `#FAF9F6` | 10.66:1 | 10.66:1 | 7:1 |
| Text | inactive_fg `#4B575E` | main_bg `#FAF9F6` | 7.06:1 | 7.06:1 | 7:1 |
| Text | graph_text `#1C1C1A` | main_bg `#FAF9F6` | 16.21:1 | 16.21:1 | 7:1 |
| Text | proc_misc `#1C1C1A` | main_bg `#FAF9F6` | 16.21:1 | 16.21:1 | 7:1 |
| Selected process row | selected_fg `#0F0F0E` | selected_bg `#8BA0BA` | 4.19:1 ✗ | 7.16:1 | 7:1 |
| Box outlines | cpu_box `#781A61` | main_bg `#FAF9F6` | 9.41:1 | 9.41:1 | 3:1 |
| Box outlines | mem_box `#003D18` | main_bg `#FAF9F6` | 11.87:1 | 11.87:1 | 3:1 |
| Box outlines | net_box `#62000A` | main_bg `#FAF9F6` | 13.09:1 | 13.09:1 | 3:1 |
| Box outlines | proc_box `#003A77` | main_bg `#FAF9F6` | 10.66:1 | 10.66:1 | 3:1 |
| Box outlines | div_line `#4B575E` | main_bg `#FAF9F6` | 7.06:1 | 7.06:1 | 3:1 |

Patched: `selected_fg` → bright_foreground

### helix.toml: passes as generated

| Area | Foreground | On | Generated | Shipped | Needs |
|---|---|---|---|---|---|
| Syntax and text | foreground `#2B2B28` | background `#FAF9F6` | 13.49:1 | 13.49:1 | 7:1 |
| Syntax and text | color1 `#62000A` | background `#FAF9F6` | 13.09:1 | 13.09:1 | 7:1 |
| Syntax and text | color2 `#003D18` | background `#FAF9F6` | 11.87:1 | 11.87:1 | 7:1 |
| Syntax and text | color3 `#664500` | background `#FAF9F6` | 8.26:1 | 8.26:1 | 7:1 |
| Syntax and text | color4 `#003A77` | background `#FAF9F6` | 10.66:1 | 10.66:1 | 7:1 |
| Syntax and text | color5 `#781A61` | background `#FAF9F6` | 9.41:1 | 9.41:1 | 7:1 |
| Syntax and text | color6 `#005F6B` | background `#FAF9F6` | 7.00:1 | 7.00:1 | 7:1 |
| Syntax and text | color8 `#4B575E` | background `#FAF9F6` | 7.06:1 | 7.06:1 | 7:1 |
| Statusline band | background `#FAF9F6` | foreground `#2B2B28` | 13.49:1 | 13.49:1 | 7:1 |
| Statusline band | background `#FAF9F6` | color8 `#4B575E` | 7.06:1 | 7.06:1 | 7:1 |
| Statusline band | background `#FAF9F6` | color4 `#003A77` | 10.66:1 | 10.66:1 | 7:1 |
| Statusline band | background `#FAF9F6` | color2 `#003D18` | 11.87:1 | 11.87:1 | 7:1 |
| Statusline band | background `#FAF9F6` | color5 `#781A61` | 9.41:1 | 9.41:1 | 7:1 |
| Selection | selection_foreground `#0F0F0E` | selection_background `#8BA0BA` | 7.16:1 | 7.16:1 | 7:1 |
| Cursor | background `#FAF9F6` | cursor `#0F0F0E` | 18.22:1 | 18.22:1 | 7:1 |
| Focused text | foreground `#2B2B28` | lighter_background `#FFFFFF` | 14.20:1 | 14.20:1 | 7:1 |
| Menu selection | background `#FAF9F6` | foreground `#2B2B28` | 13.49:1 | 13.49:1 | 7:1 |
| Cursor line and highlights | color1 `#62000A` | lighter_background `#FFFFFF` | 13.78:1 | 13.78:1 | 4.5:1 |
| Cursor line and highlights | color2 `#003D18` | lighter_background `#FFFFFF` | 12.49:1 | 12.49:1 | 4.5:1 |
| Cursor line and highlights | color3 `#664500` | lighter_background `#FFFFFF` | 8.69:1 | 8.69:1 | 4.5:1 |
| Cursor line and highlights | color4 `#003A77` | lighter_background `#FFFFFF` | 11.22:1 | 11.22:1 | 4.5:1 |
| Cursor line and highlights | color5 `#781A61` | lighter_background `#FFFFFF` | 9.91:1 | 9.91:1 | 4.5:1 |
| Cursor line and highlights | color6 `#005F6B` | lighter_background `#FFFFFF` | 7.37:1 | 7.37:1 | 4.5:1 |
| Cursor line and highlights | color8 `#4B575E` | lighter_background `#FFFFFF` | 7.44:1 | 7.44:1 | 4.5:1 |

### pi.json: 3 failing pair(s) patched

| Area | Foreground | On | Generated | Shipped | Needs |
|---|---|---|---|---|---|
| Text | foreground `#2B2B28` | background `#FAF9F6` | 13.49:1 | 13.49:1 | 7:1 |
| Text | accent `#003A77` | background `#FAF9F6` | 10.66:1 | 10.66:1 | 7:1 |
| Text | color1 `#62000A` | background `#FAF9F6` | 13.09:1 | 13.09:1 | 7:1 |
| Text | color2 `#003D18` | background `#FAF9F6` | 11.87:1 | 11.87:1 | 7:1 |
| Text | color3 `#664500` | background `#FAF9F6` | 8.26:1 | 8.26:1 | 7:1 |
| Text | color4 `#003A77` | background `#FAF9F6` | 10.66:1 | 10.66:1 | 7:1 |
| Text | color5 `#781A61` | background `#FAF9F6` | 9.41:1 | 9.41:1 | 7:1 |
| Text | color6 `#005F6B` | background `#FAF9F6` | 7.00:1 | 7.00:1 | 7:1 |
| Text | color8 `#4B575E` | background `#FAF9F6` | 7.06:1 | 7.06:1 | 7:1 |
| Text | mutedText `#4E4E49` | background `#FAF9F6` | 4.65:1 ✗ | 7.95:1 | 7:1 |
| Text | dimText `#4B575E` | background `#FAF9F6` | 2.81:1 ✗ | 7.06:1 | 7:1 |
| Message panels | foreground `#2B2B28` | panel `#eeedea` | 12.13:1 | 12.13:1 | 7:1 |
| Message panels | foreground `#2B2B28` | panelAlt `#e5e4e1` | 11.17:1 | 11.17:1 | 7:1 |
| Message panels | foreground `#2B2B28` | selectedBackground `#c3cfda` | 8.96:1 | 8.96:1 | 7:1 |
| Message panels | foreground `#2B2B28` | panelPending `#dce2e7` | 10.87:1 | 10.87:1 | 7:1 |
| Message panels | foreground `#2B2B28` | panelSuccess `#dce2db` | 10.78:1 | 10.78:1 | 7:1 |
| Message panels | foreground `#2B2B28` | panelError `#e8dbda` | 10.53:1 | 10.53:1 | 7:1 |
| Tool titles | accent `#003A77` | panelPending `#dce2e7` | 8.59:1 | 8.59:1 | 7:1 |
| Tool titles | accent `#003A77` | panelSuccess `#dce2db` | 8.52:1 | 8.52:1 | 7:1 |
| Tool titles | accent `#003A77` | panelError `#e8dbda` | 8.32:1 | 8.32:1 | 7:1 |
| Input border | border `#808A95` | background `#FAF9F6` | 1.82:1 ✗ | 3.33:1 | 3:1 |

Patched: `mutedText` → dark_foreground, `dimText` → muted, `border` → border

### claude.json: 1 failing pair(s) patched

| Area | Foreground | On | Generated | Shipped | Needs |
|---|---|---|---|---|---|
| Text | text `#2B2B28` | @background `#FAF9F6` | 13.49:1 | 13.49:1 | 7:1 |
| Text | subtle `#4B575E` | @background `#FAF9F6` | 7.06:1 | 7.06:1 | 7:1 |
| Text | inactive `#4E4E49` | @background `#FAF9F6` | 3.91:1 ✗ | 7.95:1 | 7:1 |
| Text | suggestion `#005F6B` | @background `#FAF9F6` | 7.00:1 | 7.00:1 | 7:1 |
| Text | permission `#003A77` | @background `#FAF9F6` | 10.66:1 | 10.66:1 | 7:1 |
| Text | remember `#664500` | @background `#FAF9F6` | 8.26:1 | 8.26:1 | 7:1 |
| Text | success `#003D18` | @background `#FAF9F6` | 11.87:1 | 11.87:1 | 7:1 |
| Text | error `#62000A` | @background `#FAF9F6` | 13.09:1 | 13.09:1 | 7:1 |
| Text | warning `#664500` | @background `#FAF9F6` | 8.26:1 | 8.26:1 | 7:1 |
| Text | merged `#781A61` | @background `#FAF9F6` | 9.41:1 | 9.41:1 | 7:1 |
| Text | planMode `#005F6B` | @background `#FAF9F6` | 7.00:1 | 7.00:1 | 7:1 |
| Text | autoAccept `#664500` | @background `#FAF9F6` | 8.26:1 | 8.26:1 | 7:1 |
| Text | claude `#003A77` | @background `#FAF9F6` | 10.66:1 | 10.66:1 | 7:1 |
| Badges | inverseText `#FAF9F6` | claude `#003A77` | 10.66:1 | 10.66:1 | 7:1 |
| Message backgrounds | text `#2B2B28` | userMessageBackground `#eeedea` | 12.13:1 | 12.13:1 | 7:1 |
| Message backgrounds | text `#2B2B28` | userMessageBackgroundHover `#e5e4e1` | 11.17:1 | 11.17:1 | 7:1 |
| Message backgrounds | text `#2B2B28` | bashMessageBackgroundColor `#eeedea` | 12.13:1 | 12.13:1 | 7:1 |
| Message backgrounds | text `#2B2B28` | memoryBackgroundColor `#eeedea` | 12.13:1 | 12.13:1 | 7:1 |
| Diff lines | text `#2B2B28` | diffAdded `#d5ddd5` | 10.23:1 | 10.23:1 | 7:1 |
| Diff lines | text `#2B2B28` | diffRemoved `#e3d4d3` | 9.89:1 | 9.89:1 | 7:1 |
| Diff words and selection | text `#2B2B28` | diffAddedWord `#aabdaf` | 7.17:1 | 7.17:1 | 4.5:1 |
| Diff words and selection | text `#2B2B28` | diffRemovedWord `#c9a9aa` | 6.59:1 | 6.59:1 | 4.5:1 |
| Diff words and selection | text `#2B2B28` | selectionBg `#8BA0BA` | 5.30:1 | 5.30:1 | 4.5:1 |
| Prompt border | promptBorder `#003A77` | @background `#FAF9F6` | 10.66:1 | 10.66:1 | 3:1 |

Patched: `inactive` → dark_foreground

### t3code.json: 1 failing pair(s) patched

| Area | Foreground | On | Generated | Shipped | Needs |
|---|---|---|---|---|---|
| Text | text `#2B2B28` | chrome `#FAF9F6` | 13.49:1 | 13.49:1 | 7:1 |
| Toolbar | toolbarForeground `#2B2B28` | toolbar `#FAF9F6` | 13.49:1 | 13.49:1 | 7:1 |
| Sidebar | sidebarForeground `#2B2B28` | sidebar `#F1EFE9` | 12.35:1 | 12.35:1 | 7:1 |
| Code | codeForeground `#2B2B28` | codeBackground `#F1EFE9` | 12.35:1 | 12.35:1 | 7:1 |
| Terminal | terminalForeground `#2B2B28` | terminalBackground `#FAF9F6` | 13.49:1 | 13.49:1 | 7:1 |
| Status text | error `#4f0f15` | chrome `#FAF9F6` | 14.13:1 | 14.13:1 | 7:1 |
| Status text | warning `#513c0e` | chrome `#FAF9F6` | 9.96:1 | 9.96:1 | 7:1 |
| Sidebar rows | sidebarForeground `#2B2B28` | sidebarRowHover `#e5e3dd` | 11.06:1 | 11.06:1 | 7:1 |
| Sidebar rows | sidebarForeground `#2B2B28` | sidebarRowActive `#c6ced4` | 8.91:1 | 8.91:1 | 7:1 |
| Sidebar rows | sidebarForeground `#2B2B28` | sidebarRowSelected `#BBCFE7` | 5.30:1 ✗ | 8.92:1 | 7:1 |
| Terminal selection | terminalForeground `#2B2B28` | terminalSelection `#8BA0BA` | 5.30:1 | 5.30:1 | 4.5:1 |
| Borders and focus | border `#4B575E` | chrome `#FAF9F6` | 7.06:1 | 7.06:1 | 3:1 |
| Borders and focus | toolbarBorder `#4B575E` | chrome `#FAF9F6` | 7.06:1 | 7.06:1 | 3:1 |
| Borders and focus | focus `#003A77` | chrome `#FAF9F6` | 10.66:1 | 10.66:1 | 3:1 |
| Borders and focus | sidebarBorder `#4B575E` | sidebar `#F1EFE9` | 6.47:1 | 6.47:1 | 3:1 |

Patched: `sidebarRowSelected` → row_active

### hermes.yaml: 2 failing pair(s) patched

| Area | Foreground | On | Generated | Shipped | Needs |
|---|---|---|---|---|---|
| Text | ui_text `#2B2B28` | background `#FAF9F6` | 13.49:1 | 13.49:1 | 7:1 |
| Text | ui_primary `#003A77` | background `#FAF9F6` | 10.66:1 | 10.66:1 | 7:1 |
| Text | ui_label `#003A77` | background `#FAF9F6` | 10.66:1 | 10.66:1 | 7:1 |
| Text | ui_ok `#003D18` | background `#FAF9F6` | 11.87:1 | 11.87:1 | 7:1 |
| Text | ui_warn `#664500` | background `#FAF9F6` | 8.26:1 | 8.26:1 | 7:1 |
| Text | ui_error `#62000A` | background `#FAF9F6` | 13.09:1 | 13.09:1 | 7:1 |
| Text | ui_tool `#005F6B` | background `#FAF9F6` | 7.00:1 | 7.00:1 | 7:1 |
| Text | ui_thinking `#4E4E49` | background `#FAF9F6` | 7.95:1 | 7.95:1 | 7:1 |
| Text | banner_title `#003A77` | background `#FAF9F6` | 10.66:1 | 10.66:1 | 7:1 |
| Text | banner_dim `#4E4E49` | background `#FAF9F6` | 7.95:1 | 7.95:1 | 7:1 |
| Text | banner_text `#2B2B28` | background `#FAF9F6` | 13.49:1 | 13.49:1 | 7:1 |
| Text | prompt `#0F0F0E` | background `#FAF9F6` | 18.22:1 | 18.22:1 | 7:1 |
| Text | shell_dollar `#003A77` | background `#FAF9F6` | 10.66:1 | 10.66:1 | 7:1 |
| Text | session_label `#003A77` | background `#FAF9F6` | 10.66:1 | 10.66:1 | 7:1 |
| Text | syntax_string `#003D18` | background `#FAF9F6` | 11.87:1 | 11.87:1 | 7:1 |
| Text | syntax_number `#664500` | background `#FAF9F6` | 8.26:1 | 8.26:1 | 7:1 |
| Text | syntax_keyword `#781A61` | background `#FAF9F6` | 9.41:1 | 9.41:1 | 7:1 |
| Text | syntax_comment `#4B575E` | background `#FAF9F6` | 7.06:1 | 7.06:1 | 7:1 |
| Text | diff_added_word `#003D18` | background `#FAF9F6` | 11.87:1 | 11.87:1 | 7:1 |
| Text | diff_removed_word `#62000A` | background `#FAF9F6` | 13.09:1 | 13.09:1 | 7:1 |
| Status bar | status_bar_text `#2B2B28` | status_bar_bg `#F1EFE9` | 12.35:1 | 12.35:1 | 7:1 |
| Status bar | status_bar_strong `#003A77` | status_bar_bg `#F1EFE9` | 9.76:1 | 9.76:1 | 7:1 |
| Status bar | status_bar_dim `#4E4E49` | status_bar_bg `#F1EFE9` | 7.28:1 | 7.28:1 | 7:1 |
| Status bar | status_bar_good `#003D18` | status_bar_bg `#F1EFE9` | 10.87:1 | 10.87:1 | 7:1 |
| Status bar | status_bar_warn `#664500` | status_bar_bg `#F1EFE9` | 7.56:1 | 7.56:1 | 7:1 |
| Status bar | status_bar_bad `#62000A` | status_bar_bg `#F1EFE9` | 11.99:1 | 11.99:1 | 7:1 |
| Status bar | status_bar_critical `#500006` | status_bar_bg `#F1EFE9` | 13.59:1 | 13.59:1 | 7:1 |
| Completion menu | ui_text `#2B2B28` | completion_menu_bg `#FFFFFF` | 14.20:1 | 14.20:1 | 7:1 |
| Completion menu | ui_text `#2B2B28` | completion_menu_current_bg `#BBCFE7` | 5.30:1 ✗ | 8.92:1 | 7:1 |
| Completion menu | ui_text `#2B2B28` | completion_menu_meta_bg `#FFFFFF` | 14.20:1 | 14.20:1 | 7:1 |
| Completion menu | ui_text `#2B2B28` | completion_menu_meta_current_bg `#BBCFE7` | 5.30:1 ✗ | 8.92:1 | 7:1 |
| Diff lines | ui_text `#2B2B28` | diff_added `#d5ddd5` | 10.23:1 | 10.23:1 | 7:1 |
| Diff lines | ui_text `#2B2B28` | diff_removed `#e3d4d3` | 9.89:1 | 9.89:1 | 7:1 |
| Selection | ui_text `#2B2B28` | selection_bg `#8BA0BA` | 5.30:1 | 5.30:1 | 4.5:1 |
| Borders | ui_border `#4B575E` | background `#FAF9F6` | 7.06:1 | 7.06:1 | 3:1 |
| Borders | banner_border `#4B575E` | background `#FAF9F6` | 7.06:1 | 7.06:1 | 3:1 |
| Borders | input_rule `#4B575E` | background `#FAF9F6` | 7.06:1 | 7.06:1 | 3:1 |
| Borders | session_border `#4B575E` | background `#FAF9F6` | 7.06:1 | 7.06:1 | 3:1 |
| Borders | response_border `#003A77` | background `#FAF9F6` | 10.66:1 | 10.66:1 | 3:1 |

Patched: `completion_menu_current_bg` → row_active, `completion_menu_meta_current_bg` → row_active

### hyprland-preview-share-picker.css: passes as generated

| Area | Foreground | On | Generated | Shipped | Needs |
|---|---|---|---|---|---|
| Text | foreground `#2B2B28` | background `#FAF9F6` | 13.49:1 | 13.49:1 | 7:1 |
| Selected tab | selected_tab `#003A77` | background `#FAF9F6` | 10.66:1 | 10.66:1 | 7:1 |
| Cards | text `#2B2B28` | card_bg `#FFFFFF` | 14.20:1 | 14.20:1 | 7:1 |
| Region button | text_dark `#FAF9F6` | accent `#003A77` | 10.66:1 | 10.66:1 | 7:1 |
| Region button, hover | text_dark `#FAF9F6` | accent_hover `#003064` | 12.41:1 | 12.41:1 | 7:1 |
| Focus border | accent `#003A77` | background `#FAF9F6` | 10.66:1 | 10.66:1 | 3:1 |

### obsidian.css: 3 failing pair(s) patched

| Area | Foreground | On | Generated | Shipped | Needs |
|---|---|---|---|---|---|
| Text | text-normal `#2B2B28` | background-primary `#FAF9F6` | 13.49:1 | 13.49:1 | 7:1 |
| Text | text-title-h1 `#62000A` | background-primary `#FAF9F6` | 13.09:1 | 13.09:1 | 7:1 |
| Text | text-title-h2 `#003D18` | background-primary `#FAF9F6` | 11.87:1 | 11.87:1 | 7:1 |
| Text | text-title-h3 `#664500` | background-primary `#FAF9F6` | 8.26:1 | 8.26:1 | 7:1 |
| Text | text-title-h4 `#003A77` | background-primary `#FAF9F6` | 10.66:1 | 10.66:1 | 7:1 |
| Text | text-title-h5 `#781A61` | background-primary `#FAF9F6` | 9.41:1 | 9.41:1 | 7:1 |
| Text | text-link `#003A77` | background-primary `#FAF9F6` | 10.66:1 | 10.66:1 | 7:1 |
| Text | text-accent `#003A77` | background-primary `#FAF9F6` | 10.66:1 | 10.66:1 | 7:1 |
| Text | text-muted `#4E4E49` | background-primary `#FAF9F6` | 5.23:1 ✗ | 7.95:1 | 7:1 |
| Text | text-faint `#4B575E` | background-primary `#FAF9F6` | 3.38:1 ✗ | 7.06:1 | 7:1 |
| Text | code-normal `#005F6B` | background-primary `#FAF9F6` | 7.00:1 | 7.00:1 | 7:1 |
| Text | text-error `#62000A` | background-primary `#FAF9F6` | 13.09:1 | 13.09:1 | 7:1 |
| Text | text-success `#003D18` | background-primary `#FAF9F6` | 11.87:1 | 11.87:1 | 7:1 |
| Tags | tag-color `#005F6B` | tag-background `#FFFFFF` | 1.01:1 ✗ | 7.37:1 | 7:1 |
| Selection | text-normal `#2B2B28` | text-selection `#8BA0BA` | 5.30:1 | 5.30:1 | 4.5:1 |
| Borders | background-modifier-border `#4B575E` | background-primary `#FAF9F6` | 7.06:1 | 7.06:1 | 3:1 |

Patched: `text-muted` → dark_foreground, `text-faint` → muted, `tag-background` → lighter_background

## `omarchy-beacon-redgreen-light-theme`

### btop.theme: 1 failing pair(s) patched

| Area | Foreground | On | Generated | Shipped | Needs |
|---|---|---|---|---|---|
| Text | main_fg `#2B2B28` | main_bg `#FAF9F6` | 13.49:1 | 13.49:1 | 7:1 |
| Text | title `#2B2B28` | main_bg `#FAF9F6` | 13.49:1 | 13.49:1 | 7:1 |
| Text | hi_fg `#004188` | main_bg `#FAF9F6` | 9.45:1 | 9.45:1 | 7:1 |
| Text | inactive_fg `#4B575E` | main_bg `#FAF9F6` | 7.06:1 | 7.06:1 | 7:1 |
| Text | graph_text `#1C1C1A` | main_bg `#FAF9F6` | 16.21:1 | 16.21:1 | 7:1 |
| Text | proc_misc `#1C1C1A` | main_bg `#FAF9F6` | 16.21:1 | 16.21:1 | 7:1 |
| Selected process row | selected_fg `#0F0F0E` | selected_bg `#8BA0BA` | 3.71:1 ✗ | 7.16:1 | 7:1 |
| Box outlines | cpu_box `#611A6C` | main_bg `#FAF9F6` | 10.65:1 | 10.65:1 | 3:1 |
| Box outlines | mem_box `#00614D` | main_bg `#FAF9F6` | 7.08:1 | 7.08:1 | 3:1 |
| Box outlines | net_box `#581600` | main_bg `#FAF9F6` | 13.04:1 | 13.04:1 | 3:1 |
| Box outlines | proc_box `#004188` | main_bg `#FAF9F6` | 9.45:1 | 9.45:1 | 3:1 |
| Box outlines | div_line `#4B575E` | main_bg `#FAF9F6` | 7.06:1 | 7.06:1 | 3:1 |

Patched: `selected_fg` → bright_foreground

### helix.toml: passes as generated

| Area | Foreground | On | Generated | Shipped | Needs |
|---|---|---|---|---|---|
| Syntax and text | foreground `#2B2B28` | background `#FAF9F6` | 13.49:1 | 13.49:1 | 7:1 |
| Syntax and text | color1 `#581600` | background `#FAF9F6` | 13.04:1 | 13.04:1 | 7:1 |
| Syntax and text | color2 `#00614D` | background `#FAF9F6` | 7.08:1 | 7.08:1 | 7:1 |
| Syntax and text | color3 `#664500` | background `#FAF9F6` | 8.26:1 | 8.26:1 | 7:1 |
| Syntax and text | color4 `#004188` | background `#FAF9F6` | 9.45:1 | 9.45:1 | 7:1 |
| Syntax and text | color5 `#611A6C` | background `#FAF9F6` | 10.65:1 | 10.65:1 | 7:1 |
| Syntax and text | color6 `#003A44` | background `#FAF9F6` | 11.81:1 | 11.81:1 | 7:1 |
| Syntax and text | color8 `#4B575E` | background `#FAF9F6` | 7.06:1 | 7.06:1 | 7:1 |
| Statusline band | background `#FAF9F6` | foreground `#2B2B28` | 13.49:1 | 13.49:1 | 7:1 |
| Statusline band | background `#FAF9F6` | color8 `#4B575E` | 7.06:1 | 7.06:1 | 7:1 |
| Statusline band | background `#FAF9F6` | color4 `#004188` | 9.45:1 | 9.45:1 | 7:1 |
| Statusline band | background `#FAF9F6` | color2 `#00614D` | 7.08:1 | 7.08:1 | 7:1 |
| Statusline band | background `#FAF9F6` | color5 `#611A6C` | 10.65:1 | 10.65:1 | 7:1 |
| Selection | selection_foreground `#0F0F0E` | selection_background `#8BA0BA` | 7.16:1 | 7.16:1 | 7:1 |
| Cursor | background `#FAF9F6` | cursor `#0F0F0E` | 18.22:1 | 18.22:1 | 7:1 |
| Focused text | foreground `#2B2B28` | lighter_background `#FFFFFF` | 14.20:1 | 14.20:1 | 7:1 |
| Menu selection | background `#FAF9F6` | foreground `#2B2B28` | 13.49:1 | 13.49:1 | 7:1 |
| Cursor line and highlights | color1 `#581600` | lighter_background `#FFFFFF` | 13.73:1 | 13.73:1 | 4.5:1 |
| Cursor line and highlights | color2 `#00614D` | lighter_background `#FFFFFF` | 7.45:1 | 7.45:1 | 4.5:1 |
| Cursor line and highlights | color3 `#664500` | lighter_background `#FFFFFF` | 8.69:1 | 8.69:1 | 4.5:1 |
| Cursor line and highlights | color4 `#004188` | lighter_background `#FFFFFF` | 9.94:1 | 9.94:1 | 4.5:1 |
| Cursor line and highlights | color5 `#611A6C` | lighter_background `#FFFFFF` | 11.21:1 | 11.21:1 | 4.5:1 |
| Cursor line and highlights | color6 `#003A44` | lighter_background `#FFFFFF` | 12.44:1 | 12.44:1 | 4.5:1 |
| Cursor line and highlights | color8 `#4B575E` | lighter_background `#FFFFFF` | 7.44:1 | 7.44:1 | 4.5:1 |

### pi.json: 3 failing pair(s) patched

| Area | Foreground | On | Generated | Shipped | Needs |
|---|---|---|---|---|---|
| Text | foreground `#2B2B28` | background `#FAF9F6` | 13.49:1 | 13.49:1 | 7:1 |
| Text | accent `#004188` | background `#FAF9F6` | 9.45:1 | 9.45:1 | 7:1 |
| Text | color1 `#581600` | background `#FAF9F6` | 13.04:1 | 13.04:1 | 7:1 |
| Text | color2 `#00614D` | background `#FAF9F6` | 7.08:1 | 7.08:1 | 7:1 |
| Text | color3 `#664500` | background `#FAF9F6` | 8.26:1 | 8.26:1 | 7:1 |
| Text | color4 `#004188` | background `#FAF9F6` | 9.45:1 | 9.45:1 | 7:1 |
| Text | color5 `#611A6C` | background `#FAF9F6` | 10.65:1 | 10.65:1 | 7:1 |
| Text | color6 `#003A44` | background `#FAF9F6` | 11.81:1 | 11.81:1 | 7:1 |
| Text | color8 `#4B575E` | background `#FAF9F6` | 7.06:1 | 7.06:1 | 7:1 |
| Text | mutedText `#4E4E49` | background `#FAF9F6` | 4.65:1 ✗ | 7.95:1 | 7:1 |
| Text | dimText `#4B575E` | background `#FAF9F6` | 2.81:1 ✗ | 7.06:1 | 7:1 |
| Message panels | foreground `#2B2B28` | panel `#eeedea` | 12.13:1 | 12.13:1 | 7:1 |
| Message panels | foreground `#2B2B28` | panelAlt `#e5e4e1` | 11.17:1 | 11.17:1 | 7:1 |
| Message panels | foreground `#2B2B28` | selectedBackground `#c3d1de` | 9.13:1 | 9.13:1 | 7:1 |
| Message panels | foreground `#2B2B28` | panelPending `#dce3e9` | 10.96:1 | 10.96:1 | 7:1 |
| Message panels | foreground `#2B2B28` | panelSuccess `#dce7e2` | 11.21:1 | 11.21:1 | 7:1 |
| Message panels | foreground `#2B2B28` | panelError `#e7ded8` | 10.71:1 | 10.71:1 | 7:1 |
| Tool titles | accent `#004188` | panelPending `#dce3e9` | 7.68:1 | 7.68:1 | 7:1 |
| Tool titles | accent `#004188` | panelSuccess `#dce7e2` | 7.85:1 | 7.85:1 | 7:1 |
| Tool titles | accent `#004188` | panelError `#e7ded8` | 7.50:1 | 7.50:1 | 7:1 |
| Input border | border `#808A95` | background `#FAF9F6` | 1.82:1 ✗ | 3.33:1 | 3:1 |

Patched: `mutedText` → dark_foreground, `dimText` → muted, `border` → border

### claude.json: 1 failing pair(s) patched

| Area | Foreground | On | Generated | Shipped | Needs |
|---|---|---|---|---|---|
| Text | text `#2B2B28` | @background `#FAF9F6` | 13.49:1 | 13.49:1 | 7:1 |
| Text | subtle `#4B575E` | @background `#FAF9F6` | 7.06:1 | 7.06:1 | 7:1 |
| Text | inactive `#4E4E49` | @background `#FAF9F6` | 3.91:1 ✗ | 7.95:1 | 7:1 |
| Text | suggestion `#003A44` | @background `#FAF9F6` | 11.81:1 | 11.81:1 | 7:1 |
| Text | permission `#004188` | @background `#FAF9F6` | 9.45:1 | 9.45:1 | 7:1 |
| Text | remember `#664500` | @background `#FAF9F6` | 8.26:1 | 8.26:1 | 7:1 |
| Text | success `#00614D` | @background `#FAF9F6` | 7.08:1 | 7.08:1 | 7:1 |
| Text | error `#581600` | @background `#FAF9F6` | 13.04:1 | 13.04:1 | 7:1 |
| Text | warning `#664500` | @background `#FAF9F6` | 8.26:1 | 8.26:1 | 7:1 |
| Text | merged `#611A6C` | @background `#FAF9F6` | 10.65:1 | 10.65:1 | 7:1 |
| Text | planMode `#003A44` | @background `#FAF9F6` | 11.81:1 | 11.81:1 | 7:1 |
| Text | autoAccept `#664500` | @background `#FAF9F6` | 8.26:1 | 8.26:1 | 7:1 |
| Text | claude `#004188` | @background `#FAF9F6` | 9.45:1 | 9.45:1 | 7:1 |
| Badges | inverseText `#FAF9F6` | claude `#004188` | 9.45:1 | 9.45:1 | 7:1 |
| Message backgrounds | text `#2B2B28` | userMessageBackground `#eeedea` | 12.13:1 | 12.13:1 | 7:1 |
| Message backgrounds | text `#2B2B28` | userMessageBackgroundHover `#e5e4e1` | 11.17:1 | 11.17:1 | 7:1 |
| Message backgrounds | text `#2B2B28` | bashMessageBackgroundColor `#eeedea` | 12.13:1 | 12.13:1 | 7:1 |
| Message backgrounds | text `#2B2B28` | memoryBackgroundColor `#eeedea` | 12.13:1 | 12.13:1 | 7:1 |
| Diff lines | text `#2B2B28` | diffAdded `#d5e2dd` | 10.65:1 | 10.65:1 | 7:1 |
| Diff lines | text `#2B2B28` | diffRemoved `#e2d7d1` | 10.06:1 | 10.06:1 | 7:1 |
| Diff words and selection | text `#2B2B28` | diffAddedWord `#aac8c0` | 7.93:1 | 7.93:1 | 4.5:1 |
| Diff words and selection | text `#2B2B28` | diffRemovedWord `#c6b0a7` | 6.88:1 | 6.88:1 | 4.5:1 |
| Diff words and selection | text `#2B2B28` | selectionBg `#8BA0BA` | 5.30:1 | 5.30:1 | 4.5:1 |
| Prompt border | promptBorder `#004188` | @background `#FAF9F6` | 9.45:1 | 9.45:1 | 3:1 |

Patched: `inactive` → dark_foreground

### t3code.json: 1 failing pair(s) patched

| Area | Foreground | On | Generated | Shipped | Needs |
|---|---|---|---|---|---|
| Text | text `#2B2B28` | chrome `#FAF9F6` | 13.49:1 | 13.49:1 | 7:1 |
| Toolbar | toolbarForeground `#2B2B28` | toolbar `#FAF9F6` | 13.49:1 | 13.49:1 | 7:1 |
| Sidebar | sidebarForeground `#2B2B28` | sidebar `#F1EFE9` | 12.35:1 | 12.35:1 | 7:1 |
| Code | codeForeground `#2B2B28` | codeBackground `#F1EFE9` | 12.35:1 | 12.35:1 | 7:1 |
| Terminal | terminalForeground `#2B2B28` | terminalBackground `#FAF9F6` | 13.49:1 | 13.49:1 | 7:1 |
| Status text | error `#481d0e` | chrome `#FAF9F6` | 13.68:1 | 13.68:1 | 7:1 |
| Status text | warning `#513c0e` | chrome `#FAF9F6` | 9.96:1 | 9.96:1 | 7:1 |
| Sidebar rows | sidebarForeground `#2B2B28` | sidebarRowHover `#e5e3dd` | 11.06:1 | 11.06:1 | 7:1 |
| Sidebar rows | sidebarForeground `#2B2B28` | sidebarRowActive `#c6d0d8` | 9.07:1 | 9.07:1 | 7:1 |
| Sidebar rows | sidebarForeground `#2B2B28` | sidebarRowSelected `#BBCFE7` | 5.30:1 ✗ | 8.92:1 | 7:1 |
| Terminal selection | terminalForeground `#2B2B28` | terminalSelection `#8BA0BA` | 5.30:1 | 5.30:1 | 4.5:1 |
| Borders and focus | border `#4B575E` | chrome `#FAF9F6` | 7.06:1 | 7.06:1 | 3:1 |
| Borders and focus | toolbarBorder `#4B575E` | chrome `#FAF9F6` | 7.06:1 | 7.06:1 | 3:1 |
| Borders and focus | focus `#004188` | chrome `#FAF9F6` | 9.45:1 | 9.45:1 | 3:1 |
| Borders and focus | sidebarBorder `#4B575E` | sidebar `#F1EFE9` | 6.47:1 | 6.47:1 | 3:1 |

Patched: `sidebarRowSelected` → row_active

### hermes.yaml: 3 failing pair(s) patched

| Area | Foreground | On | Generated | Shipped | Needs |
|---|---|---|---|---|---|
| Text | ui_text `#2B2B28` | background `#FAF9F6` | 13.49:1 | 13.49:1 | 7:1 |
| Text | ui_primary `#004188` | background `#FAF9F6` | 9.45:1 | 9.45:1 | 7:1 |
| Text | ui_label `#004188` | background `#FAF9F6` | 9.45:1 | 9.45:1 | 7:1 |
| Text | ui_ok `#00614D` | background `#FAF9F6` | 7.08:1 | 7.08:1 | 7:1 |
| Text | ui_warn `#664500` | background `#FAF9F6` | 8.26:1 | 8.26:1 | 7:1 |
| Text | ui_error `#581600` | background `#FAF9F6` | 13.04:1 | 13.04:1 | 7:1 |
| Text | ui_tool `#003A44` | background `#FAF9F6` | 11.81:1 | 11.81:1 | 7:1 |
| Text | ui_thinking `#4E4E49` | background `#FAF9F6` | 7.95:1 | 7.95:1 | 7:1 |
| Text | banner_title `#004188` | background `#FAF9F6` | 9.45:1 | 9.45:1 | 7:1 |
| Text | banner_dim `#4E4E49` | background `#FAF9F6` | 7.95:1 | 7.95:1 | 7:1 |
| Text | banner_text `#2B2B28` | background `#FAF9F6` | 13.49:1 | 13.49:1 | 7:1 |
| Text | prompt `#0F0F0E` | background `#FAF9F6` | 18.22:1 | 18.22:1 | 7:1 |
| Text | shell_dollar `#004188` | background `#FAF9F6` | 9.45:1 | 9.45:1 | 7:1 |
| Text | session_label `#004188` | background `#FAF9F6` | 9.45:1 | 9.45:1 | 7:1 |
| Text | syntax_string `#00614D` | background `#FAF9F6` | 7.08:1 | 7.08:1 | 7:1 |
| Text | syntax_number `#664500` | background `#FAF9F6` | 8.26:1 | 8.26:1 | 7:1 |
| Text | syntax_keyword `#611A6C` | background `#FAF9F6` | 10.65:1 | 10.65:1 | 7:1 |
| Text | syntax_comment `#4B575E` | background `#FAF9F6` | 7.06:1 | 7.06:1 | 7:1 |
| Text | diff_added_word `#00614D` | background `#FAF9F6` | 7.08:1 | 7.08:1 | 7:1 |
| Text | diff_removed_word `#581600` | background `#FAF9F6` | 13.04:1 | 13.04:1 | 7:1 |
| Status bar | status_bar_text `#2B2B28` | status_bar_bg `#FFFFFF` | 12.35:1 | 14.20:1 | 7:1 |
| Status bar | status_bar_strong `#004188` | status_bar_bg `#FFFFFF` | 8.65:1 | 9.94:1 | 7:1 |
| Status bar | status_bar_dim `#4E4E49` | status_bar_bg `#FFFFFF` | 7.28:1 | 8.37:1 | 7:1 |
| Status bar | status_bar_good `#00614D` | status_bar_bg `#FFFFFF` | 6.48:1 ✗ | 7.45:1 | 7:1 |
| Status bar | status_bar_warn `#664500` | status_bar_bg `#FFFFFF` | 7.56:1 | 8.69:1 | 7:1 |
| Status bar | status_bar_bad `#581600` | status_bar_bg `#FFFFFF` | 11.94:1 | 13.73:1 | 7:1 |
| Status bar | status_bar_critical `#471000` | status_bar_bg `#FFFFFF` | 13.61:1 | 15.65:1 | 7:1 |
| Completion menu | ui_text `#2B2B28` | completion_menu_bg `#FFFFFF` | 14.20:1 | 14.20:1 | 7:1 |
| Completion menu | ui_text `#2B2B28` | completion_menu_current_bg `#BBCFE7` | 5.30:1 ✗ | 8.92:1 | 7:1 |
| Completion menu | ui_text `#2B2B28` | completion_menu_meta_bg `#FFFFFF` | 14.20:1 | 14.20:1 | 7:1 |
| Completion menu | ui_text `#2B2B28` | completion_menu_meta_current_bg `#BBCFE7` | 5.30:1 ✗ | 8.92:1 | 7:1 |
| Diff lines | ui_text `#2B2B28` | diff_added `#d5e2dd` | 10.65:1 | 10.65:1 | 7:1 |
| Diff lines | ui_text `#2B2B28` | diff_removed `#e2d7d1` | 10.06:1 | 10.06:1 | 7:1 |
| Selection | ui_text `#2B2B28` | selection_bg `#8BA0BA` | 5.30:1 | 5.30:1 | 4.5:1 |
| Borders | ui_border `#4B575E` | background `#FAF9F6` | 7.06:1 | 7.06:1 | 3:1 |
| Borders | banner_border `#4B575E` | background `#FAF9F6` | 7.06:1 | 7.06:1 | 3:1 |
| Borders | input_rule `#4B575E` | background `#FAF9F6` | 7.06:1 | 7.06:1 | 3:1 |
| Borders | session_border `#4B575E` | background `#FAF9F6` | 7.06:1 | 7.06:1 | 3:1 |
| Borders | response_border `#004188` | background `#FAF9F6` | 9.45:1 | 9.45:1 | 3:1 |

Patched: `status_bar_bg` → lighter_background, `completion_menu_current_bg` → row_active, `completion_menu_meta_current_bg` → row_active

### hyprland-preview-share-picker.css: passes as generated

| Area | Foreground | On | Generated | Shipped | Needs |
|---|---|---|---|---|---|
| Text | foreground `#2B2B28` | background `#FAF9F6` | 13.49:1 | 13.49:1 | 7:1 |
| Selected tab | selected_tab `#004188` | background `#FAF9F6` | 9.45:1 | 9.45:1 | 7:1 |
| Cards | text `#2B2B28` | card_bg `#FFFFFF` | 14.20:1 | 14.20:1 | 7:1 |
| Region button | text_dark `#FAF9F6` | accent `#004188` | 9.45:1 | 9.45:1 | 7:1 |
| Region button, hover | text_dark `#FAF9F6` | accent_hover `#003674` | 11.21:1 | 11.21:1 | 7:1 |
| Focus border | accent `#004188` | background `#FAF9F6` | 9.45:1 | 9.45:1 | 3:1 |

### obsidian.css: 3 failing pair(s) patched

| Area | Foreground | On | Generated | Shipped | Needs |
|---|---|---|---|---|---|
| Text | text-normal `#2B2B28` | background-primary `#FAF9F6` | 13.49:1 | 13.49:1 | 7:1 |
| Text | text-title-h1 `#581600` | background-primary `#FAF9F6` | 13.04:1 | 13.04:1 | 7:1 |
| Text | text-title-h2 `#00614D` | background-primary `#FAF9F6` | 7.08:1 | 7.08:1 | 7:1 |
| Text | text-title-h3 `#664500` | background-primary `#FAF9F6` | 8.26:1 | 8.26:1 | 7:1 |
| Text | text-title-h4 `#004188` | background-primary `#FAF9F6` | 9.45:1 | 9.45:1 | 7:1 |
| Text | text-title-h5 `#611A6C` | background-primary `#FAF9F6` | 10.65:1 | 10.65:1 | 7:1 |
| Text | text-link `#004188` | background-primary `#FAF9F6` | 9.45:1 | 9.45:1 | 7:1 |
| Text | text-accent `#004188` | background-primary `#FAF9F6` | 9.45:1 | 9.45:1 | 7:1 |
| Text | text-muted `#4E4E49` | background-primary `#FAF9F6` | 5.23:1 ✗ | 7.95:1 | 7:1 |
| Text | text-faint `#4B575E` | background-primary `#FAF9F6` | 3.38:1 ✗ | 7.06:1 | 7:1 |
| Text | code-normal `#003A44` | background-primary `#FAF9F6` | 11.81:1 | 11.81:1 | 7:1 |
| Text | text-error `#581600` | background-primary `#FAF9F6` | 13.04:1 | 13.04:1 | 7:1 |
| Text | text-success `#00614D` | background-primary `#FAF9F6` | 7.08:1 | 7.08:1 | 7:1 |
| Tags | tag-color `#003A44` | tag-background `#CBDAED` | 1.67:1 ✗ | 8.76:1 | 7:1 |
| Selection | text-normal `#2B2B28` | text-selection `#8BA0BA` | 5.30:1 | 5.30:1 | 4.5:1 |
| Borders | background-modifier-border `#4B575E` | background-primary `#FAF9F6` | 7.06:1 | 7.06:1 | 3:1 |

Patched: `text-muted` → dark_foreground, `text-faint` → muted, `tag-background` → row_hover

## `omarchy-beacon-blueyellow-light-theme`

### btop.theme: 1 failing pair(s) patched

| Area | Foreground | On | Generated | Shipped | Needs |
|---|---|---|---|---|---|
| Text | main_fg `#2B2B28` | main_bg `#FAF9F6` | 13.49:1 | 13.49:1 | 7:1 |
| Text | title `#2B2B28` | main_bg `#FAF9F6` | 13.49:1 | 13.49:1 | 7:1 |
| Text | hi_fg `#6F000D` | main_bg `#FAF9F6` | 11.86:1 | 11.86:1 | 7:1 |
| Text | inactive_fg `#4B575E` | main_bg `#FAF9F6` | 7.06:1 | 7.06:1 | 7:1 |
| Text | graph_text `#1C1C1A` | main_bg `#FAF9F6` | 16.21:1 | 16.21:1 | 7:1 |
| Text | proc_misc `#1C1C1A` | main_bg `#FAF9F6` | 16.21:1 | 16.21:1 | 7:1 |
| Selected process row | selected_fg `#0F0F0E` | selected_bg `#8BA0BA` | 4.66:1 ✗ | 7.16:1 | 7:1 |
| Box outlines | cpu_box `#7B1956` | main_bg `#FAF9F6` | 9.43:1 | 9.43:1 | 3:1 |
| Box outlines | mem_box `#003608` | main_bg `#FAF9F6` | 13.03:1 | 13.03:1 | 3:1 |
| Box outlines | net_box `#6F000D` | main_bg `#FAF9F6` | 11.86:1 | 11.86:1 | 3:1 |
| Box outlines | proc_box `#6F000D` | main_bg `#FAF9F6` | 11.86:1 | 11.86:1 | 3:1 |
| Box outlines | div_line `#4B575E` | main_bg `#FAF9F6` | 7.06:1 | 7.06:1 | 3:1 |

Patched: `selected_fg` → bright_foreground

### helix.toml: passes as generated

| Area | Foreground | On | Generated | Shipped | Needs |
|---|---|---|---|---|---|
| Syntax and text | foreground `#2B2B28` | background `#FAF9F6` | 13.49:1 | 13.49:1 | 7:1 |
| Syntax and text | color1 `#6F000D` | background `#FAF9F6` | 11.86:1 | 11.86:1 | 7:1 |
| Syntax and text | color2 `#003608` | background `#FAF9F6` | 13.03:1 | 13.03:1 | 7:1 |
| Syntax and text | color3 `#724F00` | background `#FAF9F6` | 7.04:1 | 7.04:1 | 7:1 |
| Syntax and text | color4 `#003880` | background `#FAF9F6` | 10.62:1 | 10.62:1 | 7:1 |
| Syntax and text | color5 `#7B1956` | background `#FAF9F6` | 9.43:1 | 9.43:1 | 7:1 |
| Syntax and text | color6 `#005555` | background `#FAF9F6` | 8.21:1 | 8.21:1 | 7:1 |
| Syntax and text | color8 `#4B575E` | background `#FAF9F6` | 7.06:1 | 7.06:1 | 7:1 |
| Statusline band | background `#FAF9F6` | foreground `#2B2B28` | 13.49:1 | 13.49:1 | 7:1 |
| Statusline band | background `#FAF9F6` | color8 `#4B575E` | 7.06:1 | 7.06:1 | 7:1 |
| Statusline band | background `#FAF9F6` | color4 `#003880` | 10.62:1 | 10.62:1 | 7:1 |
| Statusline band | background `#FAF9F6` | color2 `#003608` | 13.03:1 | 13.03:1 | 7:1 |
| Statusline band | background `#FAF9F6` | color5 `#7B1956` | 9.43:1 | 9.43:1 | 7:1 |
| Selection | selection_foreground `#0F0F0E` | selection_background `#8BA0BA` | 7.16:1 | 7.16:1 | 7:1 |
| Cursor | background `#FAF9F6` | cursor `#0F0F0E` | 18.22:1 | 18.22:1 | 7:1 |
| Focused text | foreground `#2B2B28` | lighter_background `#FFFFFF` | 14.20:1 | 14.20:1 | 7:1 |
| Menu selection | background `#FAF9F6` | foreground `#2B2B28` | 13.49:1 | 13.49:1 | 7:1 |
| Cursor line and highlights | color1 `#6F000D` | lighter_background `#FFFFFF` | 12.49:1 | 12.49:1 | 4.5:1 |
| Cursor line and highlights | color2 `#003608` | lighter_background `#FFFFFF` | 13.71:1 | 13.71:1 | 4.5:1 |
| Cursor line and highlights | color3 `#724F00` | lighter_background `#FFFFFF` | 7.41:1 | 7.41:1 | 4.5:1 |
| Cursor line and highlights | color4 `#003880` | lighter_background `#FFFFFF` | 11.19:1 | 11.19:1 | 4.5:1 |
| Cursor line and highlights | color5 `#7B1956` | lighter_background `#FFFFFF` | 9.93:1 | 9.93:1 | 4.5:1 |
| Cursor line and highlights | color6 `#005555` | lighter_background `#FFFFFF` | 8.64:1 | 8.64:1 | 4.5:1 |
| Cursor line and highlights | color8 `#4B575E` | lighter_background `#FFFFFF` | 7.44:1 | 7.44:1 | 4.5:1 |

### pi.json: 3 failing pair(s) patched

| Area | Foreground | On | Generated | Shipped | Needs |
|---|---|---|---|---|---|
| Text | foreground `#2B2B28` | background `#FAF9F6` | 13.49:1 | 13.49:1 | 7:1 |
| Text | accent `#6F000D` | background `#FAF9F6` | 11.86:1 | 11.86:1 | 7:1 |
| Text | color1 `#6F000D` | background `#FAF9F6` | 11.86:1 | 11.86:1 | 7:1 |
| Text | color2 `#003608` | background `#FAF9F6` | 13.03:1 | 13.03:1 | 7:1 |
| Text | color3 `#724F00` | background `#FAF9F6` | 7.04:1 | 7.04:1 | 7:1 |
| Text | color4 `#003880` | background `#FAF9F6` | 10.62:1 | 10.62:1 | 7:1 |
| Text | color5 `#7B1956` | background `#FAF9F6` | 9.43:1 | 9.43:1 | 7:1 |
| Text | color6 `#005555` | background `#FAF9F6` | 8.21:1 | 8.21:1 | 7:1 |
| Text | color8 `#4B575E` | background `#FAF9F6` | 7.06:1 | 7.06:1 | 7:1 |
| Text | mutedText `#4E4E49` | background `#FAF9F6` | 4.65:1 ✗ | 7.95:1 | 7:1 |
| Text | dimText `#4B575E` | background `#FAF9F6` | 2.81:1 ✗ | 7.06:1 | 7:1 |
| Message panels | foreground `#2B2B28` | panel `#eeedea` | 12.13:1 | 12.13:1 | 7:1 |
| Message panels | foreground `#2B2B28` | panelAlt `#e5e4e1` | 11.17:1 | 11.17:1 | 7:1 |
| Message panels | foreground `#2B2B28` | selectedBackground `#dbc2c3` | 8.46:1 | 8.46:1 | 7:1 |
| Message panels | foreground `#2B2B28` | panelPending `#e9dbda` | 10.55:1 | 10.55:1 | 7:1 |
| Message panels | foreground `#2B2B28` | panelSuccess `#dce2d9` | 10.77:1 | 10.77:1 | 7:1 |
| Message panels | foreground `#2B2B28` | panelError `#e9dbda` | 10.55:1 | 10.55:1 | 7:1 |
| Tool titles | accent `#6F000D` | panelPending `#e9dbda` | 9.28:1 | 9.28:1 | 7:1 |
| Tool titles | accent `#6F000D` | panelSuccess `#dce2d9` | 9.47:1 | 9.47:1 | 7:1 |
| Tool titles | accent `#6F000D` | panelError `#e9dbda` | 9.28:1 | 9.28:1 | 7:1 |
| Input border | border `#808A95` | background `#FAF9F6` | 1.82:1 ✗ | 3.33:1 | 3:1 |

Patched: `mutedText` → dark_foreground, `dimText` → muted, `border` → border

### claude.json: 1 failing pair(s) patched

| Area | Foreground | On | Generated | Shipped | Needs |
|---|---|---|---|---|---|
| Text | text `#2B2B28` | @background `#FAF9F6` | 13.49:1 | 13.49:1 | 7:1 |
| Text | subtle `#4B575E` | @background `#FAF9F6` | 7.06:1 | 7.06:1 | 7:1 |
| Text | inactive `#4E4E49` | @background `#FAF9F6` | 3.91:1 ✗ | 7.95:1 | 7:1 |
| Text | suggestion `#005555` | @background `#FAF9F6` | 8.21:1 | 8.21:1 | 7:1 |
| Text | permission `#003880` | @background `#FAF9F6` | 10.62:1 | 10.62:1 | 7:1 |
| Text | remember `#724F00` | @background `#FAF9F6` | 7.04:1 | 7.04:1 | 7:1 |
| Text | success `#003608` | @background `#FAF9F6` | 13.03:1 | 13.03:1 | 7:1 |
| Text | error `#6F000D` | @background `#FAF9F6` | 11.86:1 | 11.86:1 | 7:1 |
| Text | warning `#724F00` | @background `#FAF9F6` | 7.04:1 | 7.04:1 | 7:1 |
| Text | merged `#7B1956` | @background `#FAF9F6` | 9.43:1 | 9.43:1 | 7:1 |
| Text | planMode `#005555` | @background `#FAF9F6` | 8.21:1 | 8.21:1 | 7:1 |
| Text | autoAccept `#724F00` | @background `#FAF9F6` | 7.04:1 | 7.04:1 | 7:1 |
| Text | claude `#6F000D` | @background `#FAF9F6` | 11.86:1 | 11.86:1 | 7:1 |
| Badges | inverseText `#FAF9F6` | claude `#6F000D` | 11.86:1 | 11.86:1 | 7:1 |
| Message backgrounds | text `#2B2B28` | userMessageBackground `#eeedea` | 12.13:1 | 12.13:1 | 7:1 |
| Message backgrounds | text `#2B2B28` | userMessageBackgroundHover `#e5e4e1` | 11.17:1 | 11.17:1 | 7:1 |
| Message backgrounds | text `#2B2B28` | bashMessageBackgroundColor `#eeedea` | 12.13:1 | 12.13:1 | 7:1 |
| Message backgrounds | text `#2B2B28` | memoryBackgroundColor `#eeedea` | 12.13:1 | 12.13:1 | 7:1 |
| Diff lines | text `#2B2B28` | diffAdded `#d5dcd2` | 10.14:1 | 10.14:1 | 7:1 |
| Diff lines | text `#2B2B28` | diffRemoved `#e5d4d3` | 9.93:1 | 9.93:1 | 7:1 |
| Diff words and selection | text `#2B2B28` | diffAddedWord `#aabbaa` | 7.03:1 | 7.03:1 | 4.5:1 |
| Diff words and selection | text `#2B2B28` | diffRemovedWord `#cea9ab` | 6.69:1 | 6.69:1 | 4.5:1 |
| Diff words and selection | text `#2B2B28` | selectionBg `#8BA0BA` | 5.30:1 | 5.30:1 | 4.5:1 |
| Prompt border | promptBorder `#6F000D` | @background `#FAF9F6` | 11.86:1 | 11.86:1 | 3:1 |

Patched: `inactive` → dark_foreground

### t3code.json: 1 failing pair(s) patched

| Area | Foreground | On | Generated | Shipped | Needs |
|---|---|---|---|---|---|
| Text | text `#2B2B28` | chrome `#FAF9F6` | 13.49:1 | 13.49:1 | 7:1 |
| Toolbar | toolbarForeground `#2B2B28` | toolbar `#FAF9F6` | 13.49:1 | 13.49:1 | 7:1 |
| Sidebar | sidebarForeground `#2B2B28` | sidebar `#F1EFE9` | 12.35:1 | 12.35:1 | 7:1 |
| Code | codeForeground `#2B2B28` | codeBackground `#F1EFE9` | 12.35:1 | 12.35:1 | 7:1 |
| Terminal | terminalForeground `#2B2B28` | terminalBackground `#FAF9F6` | 13.49:1 | 13.49:1 | 7:1 |
| Status text | error `#570f16` | chrome `#FAF9F6` | 13.43:1 | 13.43:1 | 7:1 |
| Status text | warning `#59420e` | chrome `#FAF9F6` | 9.02:1 | 9.02:1 | 7:1 |
| Sidebar rows | sidebarForeground `#2B2B28` | sidebarRowHover `#e5e3dd` | 11.06:1 | 11.06:1 | 7:1 |
| Sidebar rows | sidebarForeground `#2B2B28` | sidebarRowActive `#dac4c1` | 8.55:1 | 8.55:1 | 7:1 |
| Sidebar rows | sidebarForeground `#2B2B28` | sidebarRowSelected `#BBCFE7` | 5.30:1 ✗ | 8.92:1 | 7:1 |
| Terminal selection | terminalForeground `#2B2B28` | terminalSelection `#8BA0BA` | 5.30:1 | 5.30:1 | 4.5:1 |
| Borders and focus | border `#4B575E` | chrome `#FAF9F6` | 7.06:1 | 7.06:1 | 3:1 |
| Borders and focus | toolbarBorder `#4B575E` | chrome `#FAF9F6` | 7.06:1 | 7.06:1 | 3:1 |
| Borders and focus | focus `#6F000D` | chrome `#FAF9F6` | 11.86:1 | 11.86:1 | 3:1 |
| Borders and focus | sidebarBorder `#4B575E` | sidebar `#F1EFE9` | 6.47:1 | 6.47:1 | 3:1 |

Patched: `sidebarRowSelected` → row_active

### hermes.yaml: 3 failing pair(s) patched

| Area | Foreground | On | Generated | Shipped | Needs |
|---|---|---|---|---|---|
| Text | ui_text `#2B2B28` | background `#FAF9F6` | 13.49:1 | 13.49:1 | 7:1 |
| Text | ui_primary `#6F000D` | background `#FAF9F6` | 11.86:1 | 11.86:1 | 7:1 |
| Text | ui_label `#6F000D` | background `#FAF9F6` | 11.86:1 | 11.86:1 | 7:1 |
| Text | ui_ok `#003608` | background `#FAF9F6` | 13.03:1 | 13.03:1 | 7:1 |
| Text | ui_warn `#724F00` | background `#FAF9F6` | 7.04:1 | 7.04:1 | 7:1 |
| Text | ui_error `#6F000D` | background `#FAF9F6` | 11.86:1 | 11.86:1 | 7:1 |
| Text | ui_tool `#005555` | background `#FAF9F6` | 8.21:1 | 8.21:1 | 7:1 |
| Text | ui_thinking `#4E4E49` | background `#FAF9F6` | 7.95:1 | 7.95:1 | 7:1 |
| Text | banner_title `#6F000D` | background `#FAF9F6` | 11.86:1 | 11.86:1 | 7:1 |
| Text | banner_dim `#4E4E49` | background `#FAF9F6` | 7.95:1 | 7.95:1 | 7:1 |
| Text | banner_text `#2B2B28` | background `#FAF9F6` | 13.49:1 | 13.49:1 | 7:1 |
| Text | prompt `#0F0F0E` | background `#FAF9F6` | 18.22:1 | 18.22:1 | 7:1 |
| Text | shell_dollar `#003880` | background `#FAF9F6` | 10.62:1 | 10.62:1 | 7:1 |
| Text | session_label `#6F000D` | background `#FAF9F6` | 11.86:1 | 11.86:1 | 7:1 |
| Text | syntax_string `#003608` | background `#FAF9F6` | 13.03:1 | 13.03:1 | 7:1 |
| Text | syntax_number `#724F00` | background `#FAF9F6` | 7.04:1 | 7.04:1 | 7:1 |
| Text | syntax_keyword `#7B1956` | background `#FAF9F6` | 9.43:1 | 9.43:1 | 7:1 |
| Text | syntax_comment `#4B575E` | background `#FAF9F6` | 7.06:1 | 7.06:1 | 7:1 |
| Text | diff_added_word `#003608` | background `#FAF9F6` | 13.03:1 | 13.03:1 | 7:1 |
| Text | diff_removed_word `#6F000D` | background `#FAF9F6` | 11.86:1 | 11.86:1 | 7:1 |
| Status bar | status_bar_text `#2B2B28` | status_bar_bg `#FFFFFF` | 12.35:1 | 14.20:1 | 7:1 |
| Status bar | status_bar_strong `#6F000D` | status_bar_bg `#FFFFFF` | 10.86:1 | 12.49:1 | 7:1 |
| Status bar | status_bar_dim `#4E4E49` | status_bar_bg `#FFFFFF` | 7.28:1 | 8.37:1 | 7:1 |
| Status bar | status_bar_good `#003608` | status_bar_bg `#FFFFFF` | 11.93:1 | 13.71:1 | 7:1 |
| Status bar | status_bar_warn `#724F00` | status_bar_bg `#FFFFFF` | 6.44:1 ✗ | 7.41:1 | 7:1 |
| Status bar | status_bar_bad `#6F000D` | status_bar_bg `#FFFFFF` | 10.86:1 | 12.49:1 | 7:1 |
| Status bar | status_bar_critical `#5C0009` | status_bar_bg `#FFFFFF` | 12.52:1 | 14.39:1 | 7:1 |
| Completion menu | ui_text `#2B2B28` | completion_menu_bg `#FFFFFF` | 14.20:1 | 14.20:1 | 7:1 |
| Completion menu | ui_text `#2B2B28` | completion_menu_current_bg `#BBCFE7` | 5.30:1 ✗ | 8.92:1 | 7:1 |
| Completion menu | ui_text `#2B2B28` | completion_menu_meta_bg `#FFFFFF` | 14.20:1 | 14.20:1 | 7:1 |
| Completion menu | ui_text `#2B2B28` | completion_menu_meta_current_bg `#BBCFE7` | 5.30:1 ✗ | 8.92:1 | 7:1 |
| Diff lines | ui_text `#2B2B28` | diff_added `#d5dcd2` | 10.14:1 | 10.14:1 | 7:1 |
| Diff lines | ui_text `#2B2B28` | diff_removed `#e5d4d3` | 9.93:1 | 9.93:1 | 7:1 |
| Selection | ui_text `#2B2B28` | selection_bg `#8BA0BA` | 5.30:1 | 5.30:1 | 4.5:1 |
| Borders | ui_border `#4B575E` | background `#FAF9F6` | 7.06:1 | 7.06:1 | 3:1 |
| Borders | banner_border `#4B575E` | background `#FAF9F6` | 7.06:1 | 7.06:1 | 3:1 |
| Borders | input_rule `#4B575E` | background `#FAF9F6` | 7.06:1 | 7.06:1 | 3:1 |
| Borders | session_border `#4B575E` | background `#FAF9F6` | 7.06:1 | 7.06:1 | 3:1 |
| Borders | response_border `#6F000D` | background `#FAF9F6` | 11.86:1 | 11.86:1 | 3:1 |

Patched: `status_bar_bg` → lighter_background, `completion_menu_current_bg` → row_active, `completion_menu_meta_current_bg` → row_active

### hyprland-preview-share-picker.css: passes as generated

| Area | Foreground | On | Generated | Shipped | Needs |
|---|---|---|---|---|---|
| Text | foreground `#2B2B28` | background `#FAF9F6` | 13.49:1 | 13.49:1 | 7:1 |
| Selected tab | selected_tab `#6F000D` | background `#FAF9F6` | 11.86:1 | 11.86:1 | 7:1 |
| Cards | text `#2B2B28` | card_bg `#FFFFFF` | 14.20:1 | 14.20:1 | 7:1 |
| Region button | text_dark `#FAF9F6` | accent `#6F000D` | 11.86:1 | 11.86:1 | 7:1 |
| Region button, hover | text_dark `#FAF9F6` | accent_hover `#002E6C` | 12.41:1 | 12.41:1 | 7:1 |
| Focus border | accent `#6F000D` | background `#FAF9F6` | 11.86:1 | 11.86:1 | 3:1 |

### obsidian.css: 3 failing pair(s) patched

| Area | Foreground | On | Generated | Shipped | Needs |
|---|---|---|---|---|---|
| Text | text-normal `#2B2B28` | background-primary `#FAF9F6` | 13.49:1 | 13.49:1 | 7:1 |
| Text | text-title-h1 `#6F000D` | background-primary `#FAF9F6` | 11.86:1 | 11.86:1 | 7:1 |
| Text | text-title-h2 `#003608` | background-primary `#FAF9F6` | 13.03:1 | 13.03:1 | 7:1 |
| Text | text-title-h3 `#724F00` | background-primary `#FAF9F6` | 7.04:1 | 7.04:1 | 7:1 |
| Text | text-title-h4 `#003880` | background-primary `#FAF9F6` | 10.62:1 | 10.62:1 | 7:1 |
| Text | text-title-h5 `#7B1956` | background-primary `#FAF9F6` | 9.43:1 | 9.43:1 | 7:1 |
| Text | text-link `#003880` | background-primary `#FAF9F6` | 10.62:1 | 10.62:1 | 7:1 |
| Text | text-accent `#6F000D` | background-primary `#FAF9F6` | 11.86:1 | 11.86:1 | 7:1 |
| Text | text-muted `#4E4E49` | background-primary `#FAF9F6` | 5.23:1 ✗ | 7.95:1 | 7:1 |
| Text | text-faint `#4B575E` | background-primary `#FAF9F6` | 3.38:1 ✗ | 7.06:1 | 7:1 |
| Text | code-normal `#005555` | background-primary `#FAF9F6` | 8.21:1 | 8.21:1 | 7:1 |
| Text | text-error `#6F000D` | background-primary `#FAF9F6` | 11.86:1 | 11.86:1 | 7:1 |
| Text | text-success `#003608` | background-primary `#FAF9F6` | 13.03:1 | 13.03:1 | 7:1 |
| Tags | tag-color `#005555` | tag-background `#FFFFFF` | 1.16:1 ✗ | 8.64:1 | 7:1 |
| Selection | text-normal `#2B2B28` | text-selection `#8BA0BA` | 5.30:1 | 5.30:1 | 4.5:1 |
| Borders | background-modifier-border `#4B575E` | background-primary `#FAF9F6` | 7.06:1 | 7.06:1 | 3:1 |

Patched: `text-muted` → dark_foreground, `text-faint` → muted, `tag-background` → lighter_background
