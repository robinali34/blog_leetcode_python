---
layout: post
title: "LeetCode Templates: Math & Geometry"
date: 2025-10-29 00:00:00 -0700
categories: leetcode templates math geometry
permalink: /posts/2025-10-29-leetcode-templates-math-geometry/
tags: [leetcode, templates, math, geometry]
---

## Contents

- [Combinatorics (nCk mod P)](#combinatorics-nck-mod-p)
- [Geometry Primitives (2D)](#geometry-primitives-2d)

## Combinatorics (nCk mod P)

```python
MOD = 1_000_000_007
N = 200000

def modexp(a: int, e: int) -> int:
    r = 1 % MOD
    while e:
        if e & 1:
            r = (r * a) % MOD
        a = (a * a) % MOD
        e >>= 1
    return r

fact = [0] * (N + 1)
invfact = [0] * (N + 1)

def init_comb():
    fact[0] = 1
    for i in range(1, N + 1):
        fact[i] = (fact[i-1] * i) % MOD
    invfact[N] = modexp(fact[N], MOD - 2)
    for i in range(N, 0, -1):
        invfact[i-1] = (invfact[i] * i) % MOD

def nCk(n: int, k: int) -> int:
    if k < 0 or k > n:
        return 0
    return (fact[n] * invfact[k] % MOD * invfact[n-k]) % MOD
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
    return (b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x)

def on_seg(a: P, b: P, c: P) -> bool:
    return (min(a.x, b.x) <= c.x <= max(a.x, b.x) and
            min(a.y, b.y) <= c.y <= max(a.y, b.y) and
            cross(a, b, c) == 0)
```

| ID | Title | Link |
|---|---|---|
| 149 | Max Points on a Line | [Max Points on a Line](https://leetcode.com/problems/max-points-on-a-line/) |
| 223 | Rectangle Area | [Rectangle Area](https://leetcode.com/problems/rectangle-area/) |
