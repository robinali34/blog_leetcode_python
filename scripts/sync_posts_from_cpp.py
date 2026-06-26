#!/usr/bin/env python3
"""Sync LC problem posts from blog_leetcode (C++) into blog_leetcode_python."""
from __future__ import annotations

import re
from pathlib import Path

CPP_POSTS = Path("/home/robina/rli/blog_leetcode/_posts")
PY_POSTS = Path("/home/robina/rli/blog_leetcode_python/_posts")
LC_PATTERN = re.compile(r"-(easy|medium|hard)-", re.I)
SKIP_SUBSTRINGS = (
    "leetcode-templates",
    "leetcode-categories",
    "leetcode-beginners-guide",
    "question-list",
    "cheatsheet",
    "python-3-guide",
    "round-trip-ticket",
)


def should_sync(name: str) -> bool:
    if not LC_PATTERN.search(name):
        return False
    return not any(s in name for s in SKIP_SUBSTRINGS)


def split_frontmatter(text: str) -> tuple[str, str]:
    if not text.startswith("---"):
        return "", text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return "", text
    return parts[1], parts[2].lstrip("\n")


def extract_code_blocks(text: str, lang: str) -> list[str]:
    return re.findall(rf"```{lang}\n(.*?)\n```", text, flags=re.DOTALL)


def replace_code_blocks(text: str, lang_from: str, blocks_to: list[str]) -> str:
    pattern = rf"```{lang_from}\n.*?\n```"

    def repl(_: re.Match[str]) -> str:
        if not blocks_to:
            return _.group(0)
        return f"```python\n{blocks_to.pop(0)}\n```"

    return re.sub(pattern, repl, text, flags=re.DOTALL)


def adapt_content(text: str) -> str:
    text = text.replace("blog_leetcode_python_python", "blog_leetcode_python")
    text = text.replace("https://robinali34.github.io/blog_leetcode/", "https://robinali34.github.io/blog_leetcode_python/")
    text = text.replace("/blog_leetcode/", "/")
    text = text.replace("## C++ Solution", "## Python Solution")
    text = re.sub(r"##\s*C\+\+\s*Solution", "## Python Solution", text, flags=re.IGNORECASE)
    text = re.sub(r"\bC\+\+\b", "Python", text)
    return text


def wrap_raw(body: str) -> str:
    if "<svg" not in body or "{% raw %}" in body:
        return body
    return "{% raw %}\n" + body + "\n{% endraw %}\n"


def sync_file(name: str) -> bool:
    cpp_path = CPP_POSTS / name
    py_path = PY_POSTS / name
    if not should_sync(name) or not cpp_path.exists() or not py_path.exists():
        return False

    cpp_text = cpp_path.read_text(encoding="utf-8")
    py_text = py_path.read_text(encoding="utf-8")

    cpp_fm, cpp_body = split_frontmatter(cpp_text)
    _, py_body = split_frontmatter(py_text)
    py_body = re.sub(r"\{%\s*raw\s*%\}|\{%\s*endraw\s*%\}", "", py_body)
    py_body = re.split(r"\n## Additional Implementations\n", py_body)[0]

    py_blocks = extract_code_blocks(py_body, "python")
    cpp_block_count = len(extract_code_blocks(cpp_body, "cpp"))
    merged_body = replace_code_blocks(cpp_body, "cpp", py_blocks.copy())
    merged_body = adapt_content(merged_body)

    extras = py_blocks[cpp_block_count:]
    if extras:
        sections = [f"```python\n{block}\n```" for block in extras]
        merged_body = merged_body.rstrip() + "\n\n## Additional Implementations\n\n" + "\n\n".join(sections) + "\n"

    merged_body = wrap_raw(merged_body)
    out = f"---{cpp_fm}---\n\n{merged_body}"
    py_path.write_text(out, encoding="utf-8")
    return True


def main() -> None:
    names = sorted(
        p.name
        for p in CPP_POSTS.glob("*.md")
        if should_sync(p.name) and (PY_POSTS / p.name).exists()
    )
    synced = 0
    for name in names:
        if sync_file(name):
            synced += 1
    print(f"Synced {synced} LC posts")


if __name__ == "__main__":
    main()
