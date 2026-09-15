#!/bin/bash
# Omarchy theme-set hook: switch VS Code to the matching Beacon theme, live.
#
# Omarchy points VS Code at one shared theme called "Omarchy" and swaps the file
# behind it, so the setting never changes and VS Code needs a window reload.
# When the Beacon extension is installed, this rewrites the setting to the
# variant's own name ("Beacon Dark", ...), which VS Code applies immediately.
#
# Omarchy runs this after omarchy-theme-set-vscode has finished, so the setting
# already reads "Omarchy" here. Install once with:
#   omarchy hook install theme-set beacon-vscode.sh
#
# $1 is the Omarchy theme slug, e.g. beacon-redgreen-light.

slug="$1"
[[ $slug == beacon-* ]] || exit 0

label="Beacon"
IFS=- read -ra parts <<<"${slug#beacon-}"
for part in "${parts[@]}"; do
  case "$part" in
    dark) label+=" Dark" ;;
    light) label+=" Light" ;;
    redgreen) label+=" Red-Green" ;;
    blueyellow) label+=" Blue-Yellow" ;;
    *) exit 0 ;;
  esac
done

toggles="$HOME/.local/state/omarchy/toggles"

switch() {
  local cmd="$1" toggle="$2" settings="$3" extensions="$4"

  command -v "$cmd" >/dev/null 2>&1 || return 0
  [[ -f $toggles/$toggle ]] && return 0
  [[ -f $settings ]] || return 0
  # Trust the editor's extension registry, not the folder: a running editor
  # leaves an uninstalled extension's folder on disk until it restarts, and
  # naming a theme that no longer exists would drop VS Code to its default.
  # Matching on ".beacon-themes" works for any publisher ID.
  local registry="$extensions/extensions.json"
  [[ -f $registry ]] || return 0
  if command -v jq >/dev/null 2>&1; then
    jq -e 'any(.[]; .identifier.id | ascii_downcase | endswith(".beacon-themes"))' \
      "$registry" >/dev/null 2>&1 || return 0
  else
    grep -Eqi '"id"[[:space:]]*:[[:space:]]*"[^"]*\.beacon-themes"' "$registry" || return 0
  fi

  # Only replace Omarchy's own choice, never a theme the user picked by hand.
  grep -Eq '"workbench\.colorTheme"[[:space:]]*:[[:space:]]*"Omarchy"' "$settings" || return 0

  sed -i --follow-symlinks -E \
    "s|(\"workbench.colorTheme\"[[:space:]]*:[[:space:]]*\")Omarchy(\")|\1$label\2|" \
    "$settings"
}

switch code skip-vscode-theme-changes "$HOME/.config/Code/User/settings.json" "$HOME/.vscode/extensions"
switch code-insiders skip-vscode-insiders-theme-changes "$HOME/.config/Code - Insiders/User/settings.json" "$HOME/.vscode-insiders/extensions"
switch codium skip-codium-theme-changes "$HOME/.config/VSCodium/User/settings.json" "$HOME/.vscode-oss/extensions"
switch /usr/bin/cursor skip-cursor-theme-changes "$HOME/.config/Cursor/User/settings.json" "$HOME/.cursor/extensions"

exit 0
