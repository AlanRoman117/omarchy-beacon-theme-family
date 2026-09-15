#!/usr/bin/env bash
# Split each theme out of themes/ and push it to its own repository, so that
# `omarchy theme install` works (Omarchy expects colors.toml at the repo root).
#
#   ./publish.sh                 # all six
#   ./publish.sh beacon-dark     # one, by substring
#
# Pushes over HTTPS using your `gh` login, and creates any theme repository
# that does not exist yet as public. Run it from the branch you want published,
# normally main.
set -euo pipefail

OWNER="${BEACON_OWNER:-AlanRoman117}"
GH="${GH:-gh}"
FILTER="${1:-}"

title() {
  # omarchy-beacon-redgreen-dark-theme -> Beacon Red-Green Dark
  local out="" part
  for part in $(echo "${1#omarchy-}" | sed 's/-theme$//' | tr '-' ' '); do
    case "$part" in
      beacon) out+="Beacon" ;;
      redgreen) out+=" Red-Green" ;;
      blueyellow) out+=" Blue-Yellow" ;;
      *) out+=" ${part^}" ;;
    esac
  done
  printf '%s' "$out"
}

for dir in themes/omarchy-beacon-*/; do
  name="$(basename "$dir")"
  [[ -n "$FILTER" && "$name" != *"$FILTER"* ]] && continue

  echo "==> $name"
  if ! "$GH" repo view "$OWNER/$name" >/dev/null 2>&1; then
    "$GH" repo create "$OWNER/$name" --public --disable-wiki \
      --description "$(title "$name") theme for Omarchy: high contrast, verified at WCAG AAA. Generated from omarchy-beacon-theme-family." \
      --homepage "https://github.com/$OWNER/omarchy-beacon-theme-family" >/dev/null
    echo "    created https://github.com/$OWNER/$name"
  fi

  branch="publish/$name"
  git subtree split --prefix="themes/$name" -b "$branch" >/dev/null
  git push --force "https://github.com/$OWNER/$name.git" "$branch:main"
  git branch -D "$branch" >/dev/null
done

echo
echo "Published. Verify one end to end before announcing:"
echo "  omarchy theme install https://github.com/$OWNER/omarchy-beacon-dark-theme.git"
echo "  omarchy theme set beacon-dark"
echo
echo "Watch stderr on that install. Omarchy names anything it drops. Beacon is"
echo "colour-only by design, so nothing should be dropped; if something is,"
echo "the theme will silently fall back to generated defaults for that file."
