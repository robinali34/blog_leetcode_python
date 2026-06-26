#!/usr/bin/env python3
"""Sync leetcode template posts from blog_leetcode (C++) into blog_leetcode_python."""
from __future__ import annotations

import re
from pathlib import Path

CPP_POSTS = Path("/home/robina/rli/blog_leetcode/_posts")
PY_POSTS = Path("/home/robina/rli/blog_leetcode_python/_posts")


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
    text = text.replace("/blog_leetcode/", "/blog_leetcode_python/")
    text = text.replace("Minimal, copy-paste C++", "Minimal, copy-paste Python")
    text = text.replace("production-ready C++ templates", "production-ready Python templates")
    text = text.replace("New to C++?", "New to Python?")
    text = text.replace("[C++ Guide](/blog_leetcode_python/cpp-guide/)", "[Python 3 Guide](/python-guide/)")
    text = text.replace("[C++ Guide](/blog_leetcode/cpp-guide/)", "[Python 3 Guide](/python-guide/)")
    text = text.replace("C++ Guide", "Python 3 Guide")
    text = text.replace("cpp-guide", "python-guide")
    text = text.replace("title: \"LeetCode Templates:", 'title: "Algorithm Templates:')
    text = re.sub(r"\bC\+\+\b", "Python", text)
    text = re.sub(r"\bSTL\b", "stdlib", text)
    text = re.sub(r"\bstd::", "", text)
    return text


def sync_file(name: str) -> bool:
    cpp_path = CPP_POSTS / name
    py_path = PY_POSTS / name
    if not cpp_path.exists():
        return False

    cpp_text = cpp_path.read_text(encoding="utf-8")
    py_blocks = extract_code_blocks(py_path.read_text(encoding="utf-8"), "python") if py_path.exists() else []

    merged = cpp_text
    if py_blocks:
        merged = replace_code_blocks(merged, "cpp", py_blocks.copy())

    merged = adapt_content(merged)

    if "<svg" in merged and "{% raw %}" not in merged:
        merged = re.sub(r"(---\n\n)", r"\1{% raw %}\n", merged, count=1)
        if "{% endraw %}" not in merged:
            merged = merged.rstrip() + "\n{% endraw %}\n"

    py_path.write_text(merged, encoding="utf-8")
    return True


def main() -> None:
    names = sorted(p.name for p in CPP_POSTS.glob("*leetcode-templates*.md"))
    synced = 0
    for name in names:
        if sync_file(name):
            synced += 1
            print(f"synced {name}")
    print(f"\nSynced {synced} template posts")


if __name__ == "__main__":
    main()
