"""Entry point for the badge CLI."""

from __future__ import annotations

import argparse
import hashlib
import re
import sys
from pathlib import Path

from . import __version__


def read_text_from_args(text: str | None, file_path: str | None) -> str:
    if text:
        return text

    if file_path:
        return Path(file_path).read_text(encoding="utf-8")

    if not sys.stdin.isatty():
        return sys.stdin.read()

    raise SystemExit("Provide --text, --file, or pipe input via stdin.")


def cmd_greet(args: argparse.Namespace) -> None:
    target = args.name or "world"
    print(f"Hello, {target}!")


def cmd_wordcount(args: argparse.Namespace) -> None:
    text = read_text_from_args(args.text, args.file)
    words = re.findall(r"\b\w+\b", text)
    print(len(words))


def cmd_slugify(args: argparse.Namespace) -> None:
    text = read_text_from_args(args.text, args.file)
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", text.strip()).strip("-")
    print(slug.lower())


def cmd_hash(args: argparse.Namespace) -> None:
    text = read_text_from_args(args.text, args.file)
    digest = hashlib.sha256(text.encode("utf-8")).hexdigest()
    print(digest)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="badge-cli",
        description="Small CLI utilities for quick text tasks.",
    )
    parser.add_argument("--version", action="version", version=__version__)

    subparsers = parser.add_subparsers(dest="command", required=True)

    greet = subparsers.add_parser("greet", help="Print a greeting.")
    greet.add_argument("name", nargs="?", help="Name to greet.")
    greet.set_defaults(func=cmd_greet)

    wordcount = subparsers.add_parser("wordcount", help="Count words in text.")
    wordcount.add_argument("--text", help="Text to analyze.")
    wordcount.add_argument("--file", help="Path to a file to analyze.")
    wordcount.set_defaults(func=cmd_wordcount)

    slugify = subparsers.add_parser("slugify", help="Create a URL-friendly slug.")
    slugify.add_argument("--text", help="Text to slugify.")
    slugify.add_argument("--file", help="Path to a file to slugify.")
    slugify.set_defaults(func=cmd_slugify)

    hash_cmd = subparsers.add_parser("hash", help="Compute sha256 of text.")
    hash_cmd.add_argument("--text", help="Text to hash.")
    hash_cmd.add_argument("--file", help="Path to a file to hash.")
    hash_cmd.set_defaults(func=cmd_hash)

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
