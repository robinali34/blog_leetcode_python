---
layout: post
title: "LeetCode Templates: Dynamic Programming"
date: 2025-10-29 00:00:00 -0700
categories: leetcode templates dynamic-programming
permalink: /posts/2025-10-29-leetcode-templates-dp/
tags: [leetcode, templates, dp]
---

## Contents

- [1D DP](#1d-dp-knapsacklinear)
- [2D DP](#2d-dp-gridpath)
- [Digit DP](#digit-dp-count-numbers-with-property)
- [Bitmask DP](#bitmask-dp-tsp--subsets)

## 1D DP (knapsack/linear)

```python
def knap01(wt: list[int], val: list[int], W: int) -> int:
    dp = [0] * (W + 1)
    for i in range(len(wt)):
        for w in range(W, wt[i] - 1, -1):
            dp[w] = max(dp[w], dp[w - wt[i]] + val[i])
    return dp[W]
```

| ID | Title | Link |
|---|---|---|
| 322 | [Coin Change](https://robinali34.github.io/blog_leetcode_python/posts/2025-10-20-medium-322-coin-change/) | [Coin Change](https://leetcode.com/problems/coin-change/) |
| 139 | Word Break | [Word Break](https://leetcode.com/problems/word-break/) |

## 2D DP (grid/path)

```python
def unique_paths(g: list[list[int]]) -> int:
    m, n = len(g), len(g[0])
    dp = [[0] * n for _ in range(m)]
    if g[0][0] == 1:
        return 0
    dp[0][0] = 1
    for i in range(m):
        for j in range(n):
            if g[i][j] == 1:
                dp[i][j] = 0
                continue
            if i > 0:
                dp[i][j] += dp[i-1][j]
            if j > 0:
                dp[i][j] += dp[i][j-1]
    return dp[m-1][n-1]
```

| ID | Title | Link |
|---|---|---|
| 62 | Unique Paths | https://leetcode.com/problems/unique-paths/ |
| 63 | Unique Paths II | https://leetcode.com/problems/unique-paths-ii/ |
| 221 | Maximal Square | https://leetcode.com/problems/maximal-square/ |

## Digit DP (count numbers with property)

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def dfs_dp(i: int, prev: int, tight: bool, started: bool, s_n: str) -> int:
    if i == len(s_n):
        return 1 if started else 0
    res = 0
    lim = int(s_n[i]) if tight else 9
    for d in range(lim + 1):
        nt = tight and d == lim
        ns = started or d != 0
        if not ns or prev == -1 or d != prev:
            res += dfs_dp(i + 1, d if ns else prev, nt, ns, s_n)
    return res

def solve_dp(N: int) -> int:
    s_n = str(N)
    dfs_dp.cache_clear()
    return dfs_dp(0, -1, True, False, s_n)
```

| ID | Title | Link |
|---|---|---|
| 233 | Number of Digit One | https://leetcode.com/problems/number-of-digit-one/ |
| 902 | Numbers At Most N Given Digit Set | https://leetcode.com/problems/numbers-at-most-n-given-digit-set/ |
| 1012 | Numbers With Repeated Digits | https://leetcode.com/problems/numbers-with-repeated-digits/ |

## Bitmask DP (TSP / subsets)

```python
def tsp(w: list[list[int]]) -> int:
    n = len(w)
    INF = 10**9
    dp = [[INF] * n for _ in range(1 << n)]
    dp[1][0] = 0
    for mask in range(1, 1 << n):
        for u in range(n):
            if dp[mask][u] < INF:
                for v in range(n):
                    if not (mask & (1 << v)):
                        new_mask = mask | (1 << v)
                        dp[new_mask][v] = min(dp[new_mask][v], dp[mask][u] + w[u][v])
    return min(dp[(1 << n) - 1])
```

| ID | Title | Link |
|---|---|---|
| 847 | Shortest Path Visiting All Nodes | https://leetcode.com/problems/shortest-path-visiting-all-nodes/ |
| 698 | Partition to K Equal Sum Subsets | https://leetcode.com/problems/partition-to-k-equal-sum-subsets/ |
