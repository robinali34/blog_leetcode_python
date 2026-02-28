#!/usr/bin/env python3
"""
List posts (and optionally block index) that contain Python code blocks
with syntax errors. Useful after C++→Python conversion to find remaining issues.

Usage:
  python scripts/list_invalid_python_blocks.py              # list files with invalid blocks
  python scripts/list_invalid_python_blocks.py --verbose    # list (file, block_index) for each invalid block
"""

import re
import ast
import argparse
from pathlib import Path


def main():
    ap = argparse.ArgumentParser(description="List posts with invalid Python code blocks")
    ap.add_argument("--verbose", "-v", action="store_true", help="Print (file, block_index) per invalid block")
    ap.add_argument("--posts", default="_posts", help="Directory containing post .md files")
    args = ap.parse_args()

    posts_dir = Path(args.posts)
    if not posts_dir.is_dir():
        print(f"Not a directory: {posts_dir}")
        return 1

    total_blocks = 0
    invalid_blocks = []  # (path, block_index, error_msg)
    files_with_invalid = set()

    for f in sorted(posts_dir.glob("*.md")):
        text = f.read_text(encoding="utf-8", errors="ignore")
        blocks = re.findall(r"```python\s*\n(.*?)```", text, re.DOTALL)
        for i, block in enumerate(blocks):
            total_blocks += 1
            code = block.strip()
            if len(code) < 5:
                continue
            try:
                ast.parse(code)
            except SyntaxError as e:
                invalid_blocks.append((f.name, i, str(e)))
                files_with_invalid.add(f.name)

    print(f"Total Python blocks: {total_blocks}")
    print(f"Invalid blocks: {len(invalid_blocks)}")
    print(f"Files with at least one invalid block: {len(files_with_invalid)}")
    print()

    if args.verbose:
        print("(file, block_index, error)")
        for name, idx, err in invalid_blocks:
            print(f"  {name}  block={idx}  {err[:60]}")
    else:
        print("Files with invalid Python blocks:")
        for name in sorted(files_with_invalid):
            count = sum(1 for n, _, _ in invalid_blocks if n == name)
            print(f"  {name}  ({count} invalid block(s))")

    return 0


if __name__ == "__main__":
    exit(main())
