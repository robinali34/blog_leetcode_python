---
layout: post
title: "Python 3 Guide: Modern Features (3.8–3.13)"
date: 2026-04-22 00:00:00 -0700
categories: python guide modern-features reference
permalink: /posts/2026-04-22-python-3-guide-modern-features/
tags: [python, guide, modern-python, typing]
---

{% raw %}
# Python 3 Guide: Modern Features (3.8–3.13)

What changed in recent Python, and what is **worth using** in LeetCode / interviews vs what is **nice on latest only**.

## Quick recommendation

| Tier | Versions | Use in contests? |
| ---- | -------- | ---------------- |
| **Safe default** | 3.8–3.10 syntax | Yes — walrus, `list[int]`, `match`, dict `\|` merge |
| **Usually OK** | 3.11+ speed, small stdlib adds | Yes if environment supports |
| **Latest only** | 3.12 `type` statement, 3.13 niche APIs | Avoid unless you know the judge version |

LeetCode Python version varies by account; when unsure, stick to **3.9-style** code.

## Version highlights

### Python 3.8 — still very common baseline

| Feature | Example | LeetCode |
| ------- | ------- | -------- |
| Walrus `:=` | `while (n := n // 2): ...` | Useful |
| `math.prod` | `math.prod(nums)` | Useful |
| Positional-only `/` | `def f(a, b, /, c):` | Rare in LC |
| f-string `=` debug | `f"{ans=}"` | Local debugging only |

```python
# walrus in while / if
if (m := len(s)) > 0 and s[0] == "a":
    pass
```

### Python 3.9 — dict merge, str helpers, built-in generics

| Feature | Old | New (3.9+) |
| ------- | --- | ---------- |
| Dict merge | `{**a, **b}` | `a \| b` (3.9+) |
| Remove prefix | slice hack | `s.removeprefix("pre")` |
| Type hints | `from typing import List` | `list[int]` |

```python
freq = freq1 | freq2          # merge counts (new dict)
nums: list[int] = []
```

**Blog style:** this repo uses `list[int]`, `dict[str, int]` in newer posts — prefer that over `typing.List`.

### Python 3.10 — structural pattern matching

```python
# classify a two-value status code
match (ok, err):
    case (True, _):
        return "success"
    case (False, "timeout"):
        return "retry"
    case (False, _):
        return "fail"
```

For optional values, `case None:` / `case int(x):` (3.10+) are common in newer solutions; LeetCode's `TreeNode` does not support full structural matching unless you add `__match_args__`.

| Feature | Notes |
| ------- | ----- |
| `match` / `case` | Great for tree/linked-list variants; optional on LC |
| `X \| Y` unions | `int \| None` instead of `Optional[int]` |
| `zip(strict=True)` | Catches length mismatch — good for tests |

### Python 3.11 — faster runtime, small stdlib

| Feature | LeetCode relevance |
| ------- | ------------------ |
| Faster CPython | Free speedup |
| `ExceptionGroup` | Rare in algorithms |
| `tomllib` | Not used on LC |

### Python 3.12 — typing & syntax polish

| Feature | Use on LC? |
| ------- | ---------- |
| `type Alias = list[int]` | Optional clarity |
| Improved error messages | Dev experience only |
| `sys.set_int_max_str_digits` | N/A for most LC |

### Python 3.13 — latest

New REPL, experimental free-threading — **not** relevant for standard LeetCode submissions. Stick to portable stdlib patterns.

## Common APIs: classic vs modern

### Type hints

```python
# Classic (still valid)
from typing import List, Dict, Optional, Tuple

def f(nums: List[int]) -> Optional[int]:
    pass

# Modern (3.9+)
def f(nums: list[int]) -> int | None:
    pass
```

### Dict get / setdefault / merge

```python
# Classic
cnt = {}
cnt[x] = cnt.get(x, 0) + 1

# Modern
from collections import Counter
cnt = Counter(nums)

# Merge (3.9+)
merged = a | b
```

### String formatting

```python
# Prefer f-strings everywhere
f"sum={total}, len={len(nums)}"

# Debug (3.8+)
f"{total=}"   # prints total=42
```

### Enum / constants

```python
from enum import IntEnum

class Color(IntEnum):
    RED = 1
    GREEN = 2
```

Rare on LC; plain `int` constants are fine.

## What to avoid in interviews

- Syntax that requires **3.12+** unless confirmed
- Heavy **metaclass** / decorator magic
- **numpy/pandas** unless problem says so
- Over-typing every local variable — hints on function signatures are enough

## Feature checklist for this blog

When reading solutions here, expect:

- `list[int]`, `dict[...]` type hints
- `Counter`, `defaultdict`, `deque`, `heapq`, `bisect`, `lru_cache`
- f-strings, occasionally walrus `:=`
- `match` in some newer posts (optional)

## More in this guide

- [Python 3 Guide (intro)](/posts/2026-04-22-python-3-guide/)
- [Basics & Idioms](/posts/2026-04-22-python-3-guide-basics/)
- [Quick reference for LeetCode](/2025/09/23/python-quick-reference-for-leetcode/)
- [LeetCode templates](/posts/2025-10-29-leetcode-categories-and-templates/)
{% endraw %}
