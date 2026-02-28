#!/usr/bin/env python3
"""
Fix Python code blocks in _posts that have syntax errors (C++→Python leftovers).
Applies: list repetition *, empty dict/set {}, split class/def onto new lines, reindent.
"""

import re
import ast
from pathlib import Path


def fix_block(code: str) -> str:
    if not code or len(code) < 5:
        return code

    # --- Literal / C++→Python fixes ---
    # List repetition: ]  n, ]  (expr), ]  100
    code = re.sub(r"\]  +(?=[a-zA-Z0-9_(])", r"] * ", code)
    code = re.sub(r"(result\s*=\s*result)  +(?=\()", r"\1 * ", code)
    # Missing * in "step  2", "rows  cols", "m  n" (common in loops/conditions)
    code = re.sub(r"\bstep\s{2,}2\b", r"step * 2", code)
    code = re.sub(r"\brows\s{2,}cols\b", r"rows * cols", code)
    code = re.sub(r"\bm\s{2,}n\b", r"m * n", code)
    # Empty dict/set
    code = re.sub(r"=\s*:\s*#", r"= {}  #", code)
    code = re.sub(r"=\s*:\s*$", r"= {}", code, flags=re.MULTILINE)
    code = re.sub(r'=\s*:\s*"', r'= {"', code)
    # C++ single-line comments only: line starting with // or after newline "  // "
    # Do NOT replace // when used as Python floor division (e.g. "x // 2")
    code = re.sub(r"(?<![/\d])\n\s*//\s+", r"\n# ", code)
    code = re.sub(r"^//\s+", r"# ", code, flags=re.MULTILINE)
    # INT_MAX
    code = re.sub(r"\bINT_MAX\b", r"float('inf')", code)
    # nullptr / NULL
    code = re.sub(r"\bnullptr\b", r"None", code)
    code = re.sub(r"\bNULL\b", r"None", code)

    # --- Remove leading C++ junk (/, // Definition, etc.) ---
    lines_pre = code.split("\n")
    cleaned = []
    for line in lines_pre:
        s = line.strip()
        if s in ("/", "") and (not cleaned or all(x.strip() in ("", "/") for x in cleaned)):
            continue
        if s.startswith("// ") and not cleaned:
            continue
        cleaned.append(line)
    code = "\n".join(cleaned).strip()

    # --- Split single-line "class X: def ..." and "): stmt" ---
    code = re.sub(r":\s+(def\s+)", r":\n\1", code)
    code = re.sub(r"(def\s+\w+\([^)]*\)(?:\s*->\s*[^:]+)?):\s+", r"\1:\n", code)
    # Split "): " after def or after "for/if/while ...):" so body is on next line
    code = re.sub(r"\)\s*:\s+([a-zA-Z_][a-zA-Z0-9_]*\s*=)", r"):\n\1", code)
    code = re.sub(r"\)\s*:\s+(return\s)", r"):\n\1", code)
    code = re.sub(r"\)\s*:\s+(if\s)", r"):\n\1", code)
    code = re.sub(r"\)\s*:\s+(for\s)", r"):\n\1", code)
    code = re.sub(r"\)\s*:\s+(while\s)", r"):\n\1", code)
    code = re.sub(r"\)\s*:\s+(else\s)", r"):\n\1", code)
    code = re.sub(r"\)\s*:\s+(elif\s)", r"):\n\1", code)
    # Any "): " followed by a word (common in one-liner methods)
    code = re.sub(r"\)\s*:\s+([a-zA-Z_][a-zA-Z0-9_]*)", r"):\n\1", code)

    # --- Reindent: track block starters so else/elif/except/finally match if/for/try ---
    lines = code.split("\n")
    out = []
    indent = 0
    stack = []  # indent of each block starter (if/for/while/try) for else/elif/except/finally
    prev_terminator = False  # previous line was return/break/continue/raise
    for i, line in enumerate(lines):
        stripped = line.strip()
        if not stripped:
            out.append("")
            continue
        if stripped.startswith("def ") and indent == 8:
            indent = 4
        elif stripped.startswith("class ") and indent >= 4:
            indent = 0
            stack.clear()
        if stripped.startswith("@") and indent > 0:
            indent = max(0, indent - 4)
        # else/elif/except/finally align with the matching if/for/while/try
        if stripped.startswith(("else:", "elif ", "except:", "except ", "finally:")):
            if stack:
                indent = stack.pop()
        # Line after return/break/continue/raise often wrongly nested in source: dedent one level
        elif prev_terminator and indent > 0 and not stripped.startswith(("else", "elif", "except", "finally")):
            indent = max(0, indent - 4)
        prev_terminator = stripped in ("return", "break", "continue") or stripped.startswith(("return ", "raise "))
        out.append(" " * indent + stripped)
        if stripped.endswith(":") and not stripped.startswith("#"):
            if not stripped.startswith(("else:", "elif ", "except:", "except ", "finally:")):
                stack.append(indent)
            indent += 4
    return "\n".join(out)


def process_file(path: Path) -> int:
    text = path.read_text(encoding="utf-8", errors="ignore")
    blocks = list(re.finditer(r"```python\s*\n(.*?)```", text, re.DOTALL))
    if not blocks:
        return 0

    new_parts = []
    last_end = 0
    fixed_count = 0

    for m in blocks:
        new_parts.append(text[last_end : m.start()])
        code = m.group(1)
        try:
            ast.parse(code.strip())
            new_parts.append(m.group(0))
        except SyntaxError:
            fixed = fix_block(code)
            try:
                ast.parse(fixed)
                new_parts.append("```python\n" + fixed + "\n```")
                fixed_count += 1
            except SyntaxError:
                new_parts.append(m.group(0))
        last_end = m.end()

    new_parts.append(text[last_end:])
    if fixed_count > 0:
        path.write_text("".join(new_parts), encoding="utf-8")
    return fixed_count


def main():
    posts_dir = Path("_posts")
    if not posts_dir.is_dir():
        posts_dir = Path(__file__).resolve().parent.parent / "_posts"
    total_fixed = 0
    files_modified = 0
    for f in sorted(posts_dir.glob("*.md")):
        n = process_file(f)
        if n > 0:
            total_fixed += n
            files_modified += 1
            print(f"  {f.name}: {n} block(s) fixed")
    print(f"\nTotal blocks fixed: {total_fixed} in {files_modified} files")
    return 0


if __name__ == "__main__":
    exit(main())
