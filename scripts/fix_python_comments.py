#!/usr/bin/env python3
"""
Replace // comments with # inside Python code blocks in _posts.
Preserves // when used as floor division (e.g. n // 2).
"""

import re
from pathlib import Path


def process_file(path: Path) -> int:
    text = path.read_text(encoding="utf-8", errors="ignore")
    # Find all ```python\n...\n``` blocks
    pattern = re.compile(r"(```python\s*\n)(.*?)(\n```)", re.DOTALL)
    replacements = 0

    def replace_in_block(m):
        prefix, code, suffix = m.group(1), m.group(2), m.group(3)
        # Replace // (comment) with #. Do NOT replace floor division (e.g. "n // 2").
        # Replace "// " when followed by non-digit (comment text)
        new_code = re.sub(r"// (?=\D)", "# ", code)
        # Replace "//[" (comment like //[a - z]) with "# ["
        new_code = re.sub(r"//\[", "# [", new_code)
        if new_code != code:
            nonlocal replacements
            replacements += 1
        return prefix + new_code + suffix

    new_text = pattern.sub(replace_in_block, text)
    if new_text != text:
        path.write_text(new_text, encoding="utf-8")
    return replacements


def main():
    posts_dir = Path(__file__).resolve().parent.parent / "_posts"
    total = 0
    for f in sorted(posts_dir.glob("*.md")):
        n = process_file(f)
        if n > 0:
            total += n
            print(f"  {f.name}: {n} block(s)")
    print(f"\nTotal: {total} Python block(s) updated")
    return 0


if __name__ == "__main__":
    exit(main())
