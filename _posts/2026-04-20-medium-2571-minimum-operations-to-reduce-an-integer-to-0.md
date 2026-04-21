---
layout: post
title: "[Medium] 2571. Minimum Operations to Reduce an Integer to 0"
date: 2026-04-20 00:00:00 -0700
categories: [leetcode, medium, math, greedy, bit-manipulation]
permalink: /2026/04/20/medium-2571-minimum-operations-to-reduce-an-integer-to-0/
tags: [leetcode, medium, greedy, bit-manipulation, bfs, binary]
---

# [Medium] 2571. Minimum Operations to Reduce an Integer to 0

You are given a positive integer `n`. In one operation you may **add or subtract** any **power of two** (`± 2^k`, `k ≥ 0`). Return the **minimum** number of operations to reach `0`.

Constraints: `1 ≤ n ≤ 10^5`.

## Problem summary

A naive “only subtract `1`” mindset misses the point: sometimes **adding** creates a **carry** and clears **several trailing 1 bits** at once, so fewer operations than subtracting bit by bit.

## Key insight (binary)

Write `n` in binary. Each operation `± 2^k` toggles the cost landscape on the **low bits**. The optimal strategy is a **greedy bit rule**: when you see a run of `1`s, you either chip one `1` away or **round up** to eliminate a whole block (analogous to `7 → 8 → 0` in two operations instead of three subtractions of `1`).

## Greedy simulation (`+1` / `-1` on the integer)

Work on the current value `n`:

- If `n` is **even**, the lowest set bit is not in the ones place of the *current* decision — you can conceptually **shift right** (`n >>= 1`) to look at the next bit. (**This shift is bookkeeping, not an operation** in the problem statement.)
- If `n` is **odd** and `n > 1`:
  - If the two least significant bits are `11` (`(n & 3) == 3`), **add `1`** (carry: merge a block of ones).
  - Otherwise **subtract `1`**.
- If `n == 1`, one more operation removes it.

Each **`+1` / `-1`** corresponds to one real `± 2^k` operation; the **shifts are free** in this accounting.

```python
class Solution:
    def minOperations(self, n: int) -> int:
        ops = 0
        while n > 0:
            if n & 1 == 0:
                n >>= 1
            else:
                if n == 1:
                    return ops + 1
                if (n & 3) == 3:
                    n += 1
                else:
                    n -= 1
                ops += 1
        return ops
```

### Example: `n = 7` (`111`)

- Add `1` → `8` (`1000`), then subtract `8` → `0`: **2** operations (not three separate `-1`s).

### Example: `n = 23` (`10111`)

The minimum is **3** operations (same as LeetCode’s style of counting only real `± 2^k` steps). A line-by-line trace of the simulation above ends with `ops == 3` — do **not** count each `>>` as an operation; only the `+1` / `-1` steps increment `ops`.

## Alternative greedy: scan runs of `1`s (no `n += 1` loop)

Another standard implementation walks `n` in binary from LSB to MSB, counting **consecutive `1`s** and charging operations when a `0` ends a run (or at the end). It matches the same optimal count in `O(log n)` time and `O(1)` space:

```python
class Solution:
    def minOperations(self, n: int) -> int:
        ans = cnt = 0
        while n:
            if n & 1:
                cnt += 1
            elif cnt:
                ans += 1
                cnt = 0 if cnt == 1 else 1
            n >>= 1
        if cnt == 1:
            ans += 1
        elif cnt > 1:
            ans += 2
        return ans
```

## BFS (shortest path on an implicit graph)

Model states as integers reachable by `x ↦ x ± 2^k`. Breadth-first search from `n` to `0` gives the minimum number of edges — **always correct**, no ad‑hoc proof needed.

- **Nodes:** integers in a bounded range (for `n ≤ 10^5`, keeping `[0, hi]` with `hi` around `5 · 10^5` is safe so all optimal paths stay inside the bound).
- **Edges:** from each state, try every power of two up to `hi` (about `log hi` powers).

```python
from collections import deque


class Solution:
    def minOperations(self, n: int) -> int:
        if n == 0:
            return 0
        hi = 500_000
        powers = []
        p = 1
        while p <= hi:
            powers.append(p)
            p <<= 1

        vis = {n}
        q = deque([(n, 0)])
        while q:
            x, d = q.popleft()
            if x == 0:
                return d
            for w in powers:
                for nx in (x + w, x - w):
                    if 0 <= nx <= hi and nx not in vis:
                        vis.add(nx)
                        q.append((nx, d + 1))
        return -1
```

**Caveat:** This is much **slower** in practice (large visited set, branching factor `2 × #powers`). It is best for **validation**, small `n`, or when you already know the state space is tiny.

## Greedy vs BFS

| | Greedy (bit rules) | BFS |
| -- | ------------------ | --- |
| **Time** | `O(log n)` | Roughly `O(V + E)` over reachable states; much larger here |
| **Space** | `O(1)` | `O(size of visited set)` |
| **Use** | Production / contests | Sanity check, proof by construction, tiny bounds |

## Complexity (greedy)

- **Time:** `O(log n)` bit length.
- **Space:** `O(1)`.

## Pattern

**Bit manipulation + greedy “carry” decisions** — same family as several “integer replacement” / “minimum steps in binary” problems.

### Edge case: `n == 3` (`11`)

Greedy may suggest `+1 → 4 → 0` (two operations) or `−1 → 2 → 0` (two operations). Same optimum — either path is fine.

## Takeaway

The problem is **not** “subtract powers of two until zero” in the naive sense; it is **structuring carries** in binary. **Greedy** is the right tool; **BFS** matches the graph formulation and is useful to **cross-check** the answer.
