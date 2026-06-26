---
layout: post
title: "Python 3 Guide: Basics & Idioms"
date: 2026-04-22 00:00:00 -0700
categories: python guide basics reference
permalink: /posts/2026-04-22-python-3-guide-basics/
tags: [python, guide, basics, idioms]
---

{% raw %}
# Python 3 Guide: Basics & Idioms

Minimal foundations for algorithm work. For container cheat sheets, see [Python Quick Reference for LeetCode](/2025/09/23/python-quick-reference-for-leetcode/).

## Contents

- [Types & mutability](#types--mutability)
- [Control flow](#control-flow)
- [Functions](#functions)
- [Comprehensions & unpacking](#comprehensions--unpacking)
- [Classes (sketch)](#classes-sketch)
- [Imports](#imports)
- [Common idioms](#common-idioms)
- [Interview pitfalls](#interview-pitfalls)

## Types & mutability

```python
# Immutable: int, float, bool, str, tuple, frozenset
# Mutable: list, dict, set, bytearray

x = [1, 2, 3]
y = x          # same list object
y.append(4)    # x is also [1, 2, 3, 4]

a = (1, 2, [3])
a[2].append(4) # OK — tuple holds a reference to a mutable list
```

Truthiness: empty containers and `0` are falsy; use `if items:` not `if len(items) > 0:` unless you need the length.

## Control flow

```python
for i, x in enumerate(nums):
    if x < 0:
        continue
    if x == target:
        break

for k in range(n):           # 0 .. n-1
    pass

for k in range(1, n + 1):    # 1 .. n
    pass

while lo <= hi:
    mid = (lo + hi) // 2
    lo = mid + 1
```

`for` / `while` / `else`: the `else` runs only if the loop did **not** `break` (useful for search loops).

## Functions

```python
def add(a: int, b: int) -> int:
    return a + b

def greet(name: str = "world") -> None:
    print(f"hello {name}")

# *args / **kwargs
def f(*args, **kwargs):
    pass
```

**Mutable default pitfall** — never use a mutable default:

```python
# BAD
def bad(x, memo={}):
    memo[x] = True
    return memo

# GOOD
def good(x, memo=None):
    if memo is None:
        memo = {}
    memo[x] = True
    return memo
```

Lambdas — fine for `sort(key=lambda p: p[1])`; prefer `def` for anything non-trivial.

## Comprehensions & unpacking

```python
squares = [x * x for x in range(10)]
evens = [x for x in nums if x % 2 == 0]
matrix = [[0] * cols for _ in range(rows)]   # correct 2D init

# dict / set comprehensions
idx = {v: i for i, v in enumerate(nums)}
unique = {x for x in nums}

# unpacking
first, *rest = nums
a, b = b, a
lo, hi = 0, len(nums) - 1
```

## Classes (sketch)

LeetCode often uses plain functions; classes appear in **design** problems and **DSU**:

```python
class Node:
    __slots__ = ("val", "left", "right")  # optional: less memory

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

`@dataclass` (3.7+) is handy for small structs:

```python
from dataclasses import dataclass

@dataclass
class Edge:
    to: int
    w: int
```

## Imports

Typical competitive / LeetCode header:

```python
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq
import bisect
import math
```

Import once at the top of your solution file (LeetCode editor allows this).

## Common idioms

```python
# frequency
freq = Counter(nums)

# adjacency list
graph = defaultdict(list)
for u, v in edges:
    graph[u].append(v)

# stack as list
st = []
st.append(x)
x = st.pop()

# BFS queue
q = deque([start])

# infinity
INF = 10**18
```

## Interview pitfalls

| Pitfall | Fix |
| ------- | --- |
| `[[0]*m]*n` shared rows | `[[0]*m for _ in range(n)]` |
| Modifying list while iterating | iterate copy or use index |
| `dict` key not hashable | use `tuple` or convert key |
| Deep recursion on large graphs | `sys.setrecursionlimit` or iterative DFS/BFS |
| `heapq` is min-heap only | negate for max-heap |

```python
import sys
sys.setrecursionlimit(10**6)  # deep tree DFS only when needed
```

## More in this guide

- [Python 3 Guide (intro)](/posts/2026-04-22-python-3-guide/)
- [Modern Features (3.8–3.13)](/posts/2026-04-22-python-3-guide-modern-features/)
- [Quick reference for LeetCode](/2025/09/23/python-quick-reference-for-leetcode/)
- [LeetCode templates](/posts/2025-10-29-leetcode-categories-and-templates/)
{% endraw %}
