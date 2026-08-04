#!/usr/bin/env python3
"""Import external content repos into MkDocs."""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path


CONTENT_REPOS = ("gyms", "labs", "blogs", "projects")


def ignore_patterns(_: str, names: list[str]) -> set[str]:
    ignored = {
        ".git",
        ".github",
        ".venv",
        "__pycache__",
        "site",
        ".cache",
        "AGENTS.md",
        "AGENT.md",
    }
    return {name for name in names if name in ignored or name.endswith(".pyc")}


def copy_tree(src: Path, dst: Path) -> None:
    if dst.exists():
        shutil.rmtree(dst)
    if src.exists():
        shutil.copytree(src, dst, ignore=ignore_patterns)


def import_repo(content_root: Path, docs_dir: Path, repo: str) -> None:
    source_docs = content_root / repo / "docs"
    destination = docs_dir / repo

    if not source_docs.exists():
        raise FileNotFoundError(f"Missing content docs directory: {source_docs}")

    copy_tree(source_docs, destination)
    print(f"Imported {repo} into {destination}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--content-root",
        type=Path,
        default=Path(".."),
        help="Directory containing external content repos.",
    )
    parser.add_argument(
        "--docs-dir",
        type=Path,
        default=Path("docs"),
        help="MkDocs docs directory.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    content_root = args.content_root.resolve()
    docs_dir = args.docs_dir.resolve()
    for repo in CONTENT_REPOS:
        import_repo(content_root, docs_dir, repo)


if __name__ == "__main__":
    main()
