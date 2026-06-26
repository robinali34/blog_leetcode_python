---
layout: post
title: "Algorithm Templates: Math & Geometry"
date: 2025-10-29 00:00:00 -0700
categories: leetcode templates math geometry
permalink: /posts/2025-10-29-leetcode-templates-math-geometry/
tags: [leetcode, templates, math, geometry]
---

Minimal, copy-paste Python for combinatorics (nCk mod P) and 2D geometry primitives (cross product, point on segment).

## Contents

- [Combinatorics (nCk mod P)](#combinatorics-nck-mod-p)
- [Geometry Primitives (2D)](#geometry-primitives-2d)

## Combinatorics (nCk mod P)

```python
MOD = 1_000_000_007
N = 200_000

fact = [1] * (N + 1)
invfact = [1] * (N + 1)


def modexp(a: int, e: int) -> int:
    r = 1
    a %= MOD
    while e > 0:
        if e & 1:
            r = (r * a) % MOD
        a = (a * a) % MOD
        e >>= 1
    return r


def init_comb() -> None:
    for i in range(1, N + 1):
        fact[i] = (fact[i - 1] * i) % MOD
    invfact[N] = modexp(fact[N], MOD - 2)
    for i in range(N, 0, -1):
        invfact[i - 1] = (invfact[i] * i) % MOD


def nCk(n: int, k: int) -> int:
    if k < 0 or k > n:
        return 0
    return fact[n] * invfact[k] % MOD * invfact[n - k] % MOD
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 62 | Unique Paths | [Link](https://leetcode.com/problems/unique-paths/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2025/09/24/medium-62-unique-paths/) |
| 172 | Factorial Trailing Zeroes | [Link](https://leetcode.com/problems/factorial-trailing-zeroes/) | - |

## Geometry Primitives (2D)

```python
from dataclasses import dataclass


@dataclass
class P:
    x: int
    y: int


def cross(a: P, b: P, c: P) -> int:
    # cross((b-a), (c-a))
    return (b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x)


def on_segment(a: P, b: P, c: P) -> bool:
    # c lies on segment ab
    return (
        cross(a, b, c) == 0
        and min(a.x, b.x) <= c.x <= max(a.x, b.x)
        and min(a.y, b.y) <= c.y <= max(a.y, b.y)
    )
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 149 | Max Points on a Line | [Link](https://leetcode.com/problems/max-points-on-a-line/) | - |
| 223 | Rectangle Area | [Link](https://leetcode.com/problems/rectangle-area/) | - |
| 1344 | Angle Between Hands of a Clock | [Link](https://leetcode.com/problems/angle-between-hands-of-a-clock/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2026/03/04/medium-1344-angle-between-hands-of-a-clock/) |

## More templates

- **DP (counting, paths):** [Dynamic Programming](/posts/2025-10-29-leetcode-templates-dp/)
- **Data structures, Graph, Search:** [Data Structures & Core Algorithms](/posts/2025-10-29-leetcode-templates-data-structures/), [Graph](/posts/2025-10-29-leetcode-templates-graph/), [Search](/posts/2026-01-20-leetcode-templates-search/)
- **Master index:** [Categories & Templates](/posts/2025-10-29-leetcode-categories-and-templates/)
