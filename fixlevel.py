#!/usr/bin/env python3
"""
Fix internal GitBook links to be file-relative after moving content under a subfolder
(e.g., moving everything into ./fvr/).

What it does (default):
- Rewrites Markdown inline links and images: [text](target) and ![alt](target)
- Converts "book-root-relative" targets like 03-vote/04-integrity-observation.md
  into correct file-relative targets like ../03-vote/04-integrity-observation.md
- Skips fenced code blocks
- Leaves external links (http:, https:, mailto:, etc.) and #anchors untouched

Optional:
- --convert-backticks: turn inline code file refs like `03-vote/00-vote-overview.md`
  into clickable links.
"""

from __future__ import annotations

import argparse
import os
import re
from pathlib import Path
from typing import Iterable

SCHEME_RE = re.compile(r"^[a-zA-Z][a-zA-Z0-9+.\-]*:")
MD_LINK_RE = re.compile(r"(!?\[[^\]]*\]\()([^)]+)(\))")  # captures (...target...)
BACKTICK_PATH_RE = re.compile(r"`([^`\n]+\.md(?:#[^`\n]+)?)`")  # `path.md` or `path.md#anchor`

def is_external_or_anchor_only(href: str) -> bool:
    h = href.strip()
    if not h:
        return True
    if h.startswith("#"):
        return True
    if SCHEME_RE.match(h):  # http:, https:, mailto:, etc.
        return True
    return False

def split_suffix(href: str) -> tuple[str, str]:
    """
    Split into (path, suffix) where suffix includes ?query or #anchor (preserved).
    """
    h = href.strip()
    m = re.search(r"[?#]", h)
    if m:
        return h[: m.start()], h[m.start():]
    return h, ""

def normalize_slashes(p: str) -> str:
    return p.replace(os.sep, "/")

def maybe_add_dot(rel: str, explicit_dot: bool) -> str:
    if not explicit_dot:
        return rel
    # Add ./ for same-directory simple filenames (GitBook doesn’t require it; this is style-only)
    if not rel.startswith(".") and "/" not in rel:
        return "./" + rel
    return rel

def resolve_internal_target(path_part: str, book_root: Path) -> Path | None:
    """
    Interpret non-dot, non-absolute paths as book-root-relative (old convention).
    If path starts with '/', treat it as repo-root-relative and try to map into book_root.
    """
    p = path_part.strip()

    if p.startswith("."):
        return None  # already relative to file; leave alone
    if p.startswith("/"):
        # Try interpreting as repo-root-relative:
        # e.g. /fvr/03-vote/x.md or /03-vote/x.md
        # Strip leading slash and resolve under repo root
        # The caller will pass book_root; we can derive repo root as book_root.parent
        repo_root = book_root.parent
        abs_candidate = (repo_root / p.lstrip("/")).resolve()
        return abs_candidate if abs_candidate.exists() else None

    abs_candidate = (book_root / p).resolve()
    return abs_candidate if abs_candidate.exists() else None

def rewrite_markdown_links(
    md_path: Path,
    book_root: Path,
    dry_run: bool,
    explicit_dot: bool,
) -> tuple[int, int, list[str]]:
    """
    Returns: (scanned_link_targets, rewritten_count, unresolved_targets)
    """
    text = md_path.read_text(encoding="utf-8")
    lines = text.splitlines(True)

    in_fence = False
    scanned = 0
    rewritten = 0
    unresolved: list[str] = []

    def replace_match(m: re.Match) -> str:
        nonlocal scanned, rewritten, unresolved
        prefix, target, suffix_paren = m.group(1), m.group(2), m.group(3)

        raw = target.strip()
        if is_external_or_anchor_only(raw):
            return m.group(0)

        path_part, suffix = split_suffix(raw)

        # Already file-relative or absolute? keep unless it's absolute and resolvable
        if path_part.startswith("."):
            return m.group(0)

        abs_target = resolve_internal_target(path_part, book_root)
        scanned += 1

        if abs_target is None:
            # either already relative, or couldn't interpret
            return m.group(0)

        if not abs_target.exists():
            unresolved.append(f"{md_path}: {raw}")
            return m.group(0)

        rel = os.path.relpath(abs_target, start=md_path.parent.resolve())
        rel = normalize_slashes(rel)
        rel = maybe_add_dot(rel, explicit_dot)

        new_target = rel + suffix
        if new_target != raw:
            rewritten += 1
            return f"{prefix}{new_target}{suffix_paren}"

        return m.group(0)

    out_lines: list[str] = []
    for line in lines:
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            out_lines.append(line)
            continue
        if in_fence:
            out_lines.append(line)
            continue
        out_lines.append(MD_LINK_RE.sub(replace_match, line))

    if rewritten and not dry_run:
        md_path.write_text("".join(out_lines), encoding="utf-8")

    return scanned, rewritten, unresolved

def convert_backticked_paths(
    md_path: Path,
    book_root: Path,
    dry_run: bool,
    explicit_dot: bool,
) -> int:
    """
    Convert inline code `some/path.md` into a clickable link when it resolves.
    Returns number of conversions.
    """
    text = md_path.read_text(encoding="utf-8")
    lines = text.splitlines(True)

    in_fence = False
    conversions = 0

    def repl(m: re.Match) -> str:
        nonlocal conversions
        raw = m.group(1).strip()
        path_part, suffix = split_suffix(raw)

        if is_external_or_anchor_only(path_part):
            return m.group(0)

        # Only convert “book-root-style” paths (not ./ or ../)
        if path_part.startswith(".") or path_part.startswith("/"):
            return m.group(0)

        abs_target = (book_root / path_part).resolve()
        if not abs_target.exists():
            return m.group(0)

        rel = os.path.relpath(abs_target, start=md_path.parent.resolve())
        rel = normalize_slashes(rel)
        rel = maybe_add_dot(rel, explicit_dot)

        conversions += 1
        display = raw  # keep the visible text identical to what was in backticks
        return f"[`{display}`]({rel}{suffix})"

    out_lines: list[str] = []
    for line in lines:
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            out_lines.append(line)
            continue
        if in_fence:
            out_lines.append(line)
            continue
        out_lines.append(BACKTICK_PATH_RE.sub(repl, line))

    if conversions and not dry_run:
        md_path.write_text("".join(out_lines), encoding="utf-8")

    return conversions

def iter_md_files(book_root: Path) -> Iterable[Path]:
    # Skip common noise folders if present
    for p in sorted(book_root.rglob("*.md")):
        parts = set(p.parts)
        if ".git" in parts or "node_modules" in parts:
            continue
        yield p

def main():
    ap = argparse.ArgumentParser(description="Rewrite GitBook internal links to file-relative paths.")
    ap.add_argument("--bookdir", type=str, default="fvr", help="Folder containing the moved book (default: fvr)")
    ap.add_argument("--repo", type=Path, default=Path("."), help="Repo root (default: .)")
    ap.add_argument("--dry-run", action="store_true", help="Do not write changes; only report")
    ap.add_argument("--explicit-dot", action="store_true", help="Add ./ to same-directory links (style only)")
    ap.add_argument("--convert-backticks", action="store_true", help="Convert inline `path.md` references to links")
    args = ap.parse_args()

    repo = args.repo.resolve()
    book_root = (repo / args.bookdir).resolve()
    if not book_root.exists():
        raise SystemExit(f"Book directory not found: {book_root}")

    total_scanned = 0
    total_rewritten = 0
    total_backtick = 0
    changed_files = 0
    unresolved_all: list[str] = []

    for md in iter_md_files(book_root):
        scanned, rewritten, unresolved = rewrite_markdown_links(
            md, book_root, dry_run=args.dry_run, explicit_dot=args.explicit_dot
        )
        total_scanned += scanned
        total_rewritten += rewritten
        if rewritten:
            changed_files += 1
            print(f"{md.relative_to(repo)}: {rewritten} link rewrites")

        if args.convert_backticks:
            conv = convert_backticked_paths(
                md, book_root, dry_run=args.dry_run, explicit_dot=args.explicit_dot
            )
            total_backtick += conv
            if conv:
                if rewritten == 0:
                    changed_files += 1
                print(f"{md.relative_to(repo)}: {conv} backtick-path conversions")

        unresolved_all.extend(unresolved)

    mode = "DRY RUN" if args.dry_run else "WROTE"
    print(f"{mode}: changed_files={changed_files}, rewritten_links={total_rewritten}, scanned={total_scanned}, backtick_conversions={total_backtick}")

    if unresolved_all:
        print("\nUnresolved targets (left unchanged):")
        for u in unresolved_all[:200]:
            print(" -", u)
        if len(unresolved_all) > 200:
            print(f" ... {len(unresolved_all)-200} more")

if __name__ == "__main__":
    main()
