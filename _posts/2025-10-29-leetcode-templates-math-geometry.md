---
layout: post
title: "LeetCode Templates: Math & Geometry"
date: 2025-10-29 00:00:00 -0700
categories: [leetcode, templates, math, geometry]
permalink: /posts/2025-10-29-leetcode-templates-math-geometry/
tags: [leetcode, templates, math, geometry]
---

## Contents

- [How to Analyze Math & Geometry](#how-to-analyze-math--geometry)
- [Combinatorics (nCk mod P)](#combinatorics-nck-mod-p)
- [Geometry Primitives (2D)](#geometry-primitives-2d)

## How to Analyze Math & Geometry

1. **Choose representation first**
   - integers vs floating point
   - normalized slope / gcd fractions for line problems

2. **Avoid precision drift**
   - use cross products and integer arithmetic when possible

3. **Precompute for repeated queries**
   - factorial / inverse factorial for many combination queries

4. **Complexity targets**
   - combinatorics preprocessing `O(N)`, query `O(1)`
   - geometry primitives `O(1)` per orientation/intersection test

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

| ID | Title | Link |
|---|---|---|
| 62 | Unique Paths | [Unique Paths](https://leetcode.com/problems/unique-paths/) |
| 172 | Factorial Trailing Zeroes | [Factorial Trailing Zeroes](https://leetcode.com/problems/factorial-trailing-zeroes/) |

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

| ID | Title | Link |
|---|---|---|
| 149 | Max Points on a Line | [Max Points on a Line](https://leetcode.com/problems/max-points-on-a-line/) |
| 223 | Rectangle Area | [Rectangle Area](https://leetcode.com/problems/rectangle-area/) |

