# v2.0 Post-Release Backlog

Created: 2026-06-30 (after v2.0 ship + Zenodo cleanup)
Status: both items OPTIONAL / parked. Neither blocks anything.

Context: v2.0 of `shorttack/aberdeen-group-archive` shipped to GitHub (tag `v2.0`,
release published 2026-06-30T14:01:20Z) and the Zenodo archive record published at
2.0 (concept DOI `10.5281/zenodo.20245076`). The wiki record stays intentionally at
v1.9.0 (independent "sibling" version line). An empty new-version DRAFT left on the
wiki record by the failed v2.0 webhook was discarded 2026-06-30 — Zenodo is clean.

---

## Item 1 — Rotate the exposed Zenodo webhook token

### Why
The GitHub webhook URL carries the Zenodo access token in its query string, so the
token (`qI7z8oHd...Pyw4U`) is visible in the repo's webhook config and in git history
(v2.0 `.zenodo.json` / hook references). Rotating mints a fresh token and re-wires the
hook. NOTE: revoking the old token on Zenodo's side is what actually neutralizes it —
git-history scrubbing is NOT required.

### Priority
LOW. The v2.0 archive published fine via manual `gh release create` despite the
webhook erroring (deliveries: published->403, created->202, released->409). The token
only matters if you want FUTURE releases to auto-deposit via webhook. Given the
webhook has been flaky and you publish manually, low value.

### Known facts
- Hook id: `624205979` on `shorttack/aberdeen-group-archive`
- Current (exposed) token ends `...Pyw4U`
- `admin:repo_hook` scope already granted to the Mac's `gh` token (done 2026-06-30)

### Steps

**A. On Zenodo (browser) — create new token FIRST, before any PATCH:**
1. Open https://zenodo.org/account/settings/applications/tokens/new/
   (or: top-right name -> Applications -> Personal access tokens -> "+ New token")
2. Name e.g. `github-webhook-aberdeen`; scopes `deposit:write` + `deposit:actions`; Create.
3. Copy the token string (shown once).
4. Revoke the OLD token (ends `...Pyw4U`) at
   https://zenodo.org/account/settings/applications/ — this is the real fix.

**B. Re-wire the GitHub webhook (sandbox or Mac, `gh` with admin:repo_hook):**
```bash
# Confirm hook id (already known: 624205979)
gh api /repos/shorttack/aberdeen-group-archive/hooks \
  --jq '.[] | select(.config.url | contains("zenodo")) | {id, url: .config.url}'

# PATCH with the new token (substitute NEW_TOKEN locally — do NOT paste into chat)
gh api --method PATCH /repos/shorttack/aberdeen-group-archive/hooks/624205979 \
  -f "config[url]=https://zenodo.org/api/hooks/receivers/github/events/?access_token=NEW_TOKEN" \
  -f "config[content_type]=json"

# Verify
gh api /repos/shorttack/aberdeen-group-archive/hooks/624205979 --jq '.config.url'
```

Note: per-delivery payload reads (`/hooks/<id>/deliveries/<delivery_id>`) age out
quickly and 404 even with scope — don't rely on reading old delivery bodies. The
deliveries LIST summary still works for status codes.

---

## Item 2 — Enable commit signing on the Mac

### Why
Branch protection on `main` requires verified signatures, but your commits currently
rely on owner BYPASS ("Bypassed rule violations" notices on every push). Enabling SSH
signing makes the rule pass cleanly without bypass.

### Priority
LOW. Cosmetic/hygiene — pushes succeed today via owner bypass.

### Steps (on the Mac, Terminal)

**A. Configure SSH signing (reuses your existing SSH key):**
```bash
git config --global gpg.format ssh
git config --global user.signingkey ~/.ssh/id_ed25519.pub
git config --global commit.gpgsign true
git config --global tag.gpgsign true

# Trust your key for local verification
echo "$(git config user.email) $(cat ~/.ssh/id_ed25519.pub)" >> ~/.config/git/allowed_signers
git config --global gpg.ssh.allowedSignersFile ~/.config/git/allowed_signers
```
(If no `id_ed25519`, use your actual key filename or `ssh-keygen -t ed25519`.)

**B. Register the key as a SIGNING key on GitHub (separate from auth key):**
- https://github.com/settings/ssh/new -> Key type = **Signing Key** -> paste
  contents of `~/.ssh/id_ed25519.pub`.

**C. Verify:**
```bash
git commit --allow-empty -m "test: signed commit" -S
git log --show-signature -1     # expect "Good signature"
git push                        # GitHub should show green "Verified" badge
```

Once a normal commit shows verified, the branch-protection rule passes without the
owner-bypass notices.
