# Postmortem: Git Author Identity Credential Exposure

**Status:** Final. Written 2026-07-25 (overnight AUTO batch, worklist item L151).
**Classification:** Internal postmortem, safe for the public archive repo —
this document does **not** contain the leaked credential value anywhere.
See "Redaction note" at the bottom.

## Summary

A personal credential (the leaked value is referred to throughout this
document only as "the leaked credential" — never reproduced) was, at some
point prior to detection, mistakenly set as both the local `git config
user.name` value on the working machine and as the display name on the
associated GitHub profile. Because both the local git identity and the
GitHub account display name carried the same string, the credential was
written into the **Author metadata of every commit made under that
configuration** — not just a config file that could be quietly rotated.

## Cause

The root cause was a configuration mistake: a personal credential string
ended up populating two identity fields that are not treated as secrets by
git or GitHub:

1. **Local `git config user.name`** — this value is embedded verbatim into
   every commit's Author field at commit time. It is not encrypted, hashed,
   or hidden; it is plain text in the commit object.
2. **GitHub account profile display name** — this is a public-facing field.

Because commits were made both via local `git commit` (using the local
config) and via the GitHub API using the authenticated token (which
resolves the committer's display name from the GitHub account profile —
not from any local git config), **both paths independently wrote the same
leaked value into commit Author metadata.**

## API-commit identity gotcha

A specific and easy-to-miss detail surfaced during investigation: when
commits are made through the GitHub REST API using a personal access
token (rather than a local `git commit` + `git push`), the Author/Committer
display name that ends up in the commit is sourced from **the GitHub
account's profile name**, not from whatever `git config user.name` is set
to locally. This means that even after the local git config was corrected,
API-authored commits continued to carry the leaked value until the GitHub
profile display name itself was also corrected. Both surfaces had to be
fixed independently — fixing only one was not sufficient.

## Blast radius

Approximately **976 commits** across the affected repository history carry
the leaked value in their Author (and/or Committer) metadata. This is a
large blast radius because the misconfiguration was in place for an
extended period covering the bulk of the repository's commit history up to
the point of detection.

## Detection

The exposure was detected on **2026-06-01 (PM)**, when the leaked value was
noticed in commit metadata during a routine review.

## Remediation

Upon detection, the identity was rotated immediately:

- Local `git config user.name` was corrected to the proper handle,
  **`shorttack`**.
- The GitHub account profile display name was corrected to match, closing
  the API-commit identity gap described above.

Both fixes were necessary; fixing only the local git config (as noted
above) would have left API-authored commits still leaking the value via
the GitHub profile name field.

## Residual risk

The leaked value **persists in the historical Author metadata of the
~976 affected commits** and cannot be removed without a full git history
rewrite (e.g., `git filter-repo` or equivalent, followed by a force-push
and coordination of all clones). A history rewrite of this scope is a
significant, disruptive operation and is **explicitly out of scope** for
this postmortem and for this remediation pass. The residual risk is
therefore accepted for now: the leaked value remains discoverable by
anyone who inspects historical commit metadata in the affected repository,
until and unless a history rewrite is separately planned, authorized, and
executed by Pete.

## Recommendations going forward

- Never set `git config user.name` (or any git identity field) to a
  password, API key, or any other secret value — these fields are stored
  and transmitted as plain text and become permanently embedded in commit
  history.
- Remember that API-authored commits resolve author identity from the
  GitHub account profile, not local git config — both surfaces must be
  checked when auditing or rotating identity-related credentials.
- If a full history rewrite is ever undertaken for unrelated reasons, this
  would be an opportunity to also scrub the residual leaked value from
  historical Author metadata — but that should be planned as its own
  explicitly-authorized project given the disruption it causes to existing
  clones and any forks.

## Redaction note (why this document is safe to commit publicly)

This document is committed to the `Perplexity_Only/` directory of the
**public** `shorttack/aberdeen-group-archive` repository. Because of that,
this postmortem deliberately:

- Never states the actual leaked credential value anywhere in this file.
- Refers to it only generically, as "the leaked credential", "the leaked
  value", or "a personal credential".
- Describes the historical commit metadata exposure generically
  ("the leaked value persists in historical Author metadata") without
  reproducing the string itself, even as an example or partial fragment.

This redaction was verified by grepping the finished document for the
literal credential string before committing (see batch log for the
verification step and result).

---

**Maintained by:** Pete Kastner + Perplexity Computer.
**Related:** `_decisions_log.md` (detection/rotation event history).
