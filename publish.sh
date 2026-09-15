#!/usr/bin/env bash
# Split each theme out of themes/ and push it to its own repository, so that
# `omarchy theme install` works (Omarchy expects colors.toml at the repo root).
#
#   ./publish.sh                 # all six
#   ./publish.sh beacon-dark     # one, by substring
set -euo pipefail

OWNER="${BEACON_OWNER:-AlanRoman117}"
FILTER="${1:-}"

for dir in themes/omarchy-beacon-*/; do
  name="$(basename "$dir")"
  [[ -n "$FILTER" && "$name" != *"$FILTER"* ]] && continue

  branch="publish/$name"
  echo "==> $name"
  git subtree split --prefix="themes/$name" -b "$branch" >/dev/null
  git push --force "git@github.com:$OWNER/$name.git" "$branch:main"
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
