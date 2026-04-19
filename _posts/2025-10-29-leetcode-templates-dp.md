---
layout: post
title: "LeetCode Templates: Dynamic Programming"
date: 2025-10-29 00:00:00 -0700
categories: [leetcode, templates, dynamic-programming]
permalink: /posts/2025-10-29-leetcode-templates-dp/
tags: [leetcode, templates, dp]
---

## Contents

- [How to Analyze DP Problems](#how-to-analyze-dp-problems)
- [1D DP](#1d-dp-knapsacklinear)
- [2D DP](#2d-dp-gridpath)
- [Digit DP](#digit-dp-count-numbers-with-property)
- [Bitmask DP](#bitmask-dp-tsp--subsets)

## How to Analyze DP Problems

For fast and reliable DP design:

1. **Define state**  
   `dp[state]` must represent one precise subproblem.

2. **Write transition**  
   Express current answer using smaller states.

3. **Determine order**  
   Top-down (memo DFS) or bottom-up (iteration).

4. **Base cases + invalid states**  
   Missing this is the most common source of bugs.

5. **Space optimization**  
   If transition only uses previous row/column, compress dimensions.

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
| 322 | Coin Change | [Coin Change](https://leetcode.com/problems/coin-change/) |
| 139 | Word Break | [Word Break](https://leetcode.com/problems/word-break/) |
| 309 | [Best Time to Buy and Sell Stock with Cooldown](/2026/03/20/medium-309-best-time-to-buy-and-sell-stock-with-cooldown/) | [Best Time to Buy and Sell Stock with Cooldown](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/) |

## 2D DP (grid/path)

```python
def unique_paths_with_obstacles(g: list[list[int]]) -> int:
    m, n = len(g), len(g[0])
    if g[0][0] == 1:
        return 0

    dp = [[0] * n for _ in range(m)]
    dp[0][0] = 1

    for i in range(m):
        for j in range(n):
            if g[i][j] == 1:
                dp[i][j] = 0
                continue
            if i > 0:
                dp[i][j] += dp[i - 1][j]
            if j > 0:
                dp[i][j] += dp[i][j - 1]
    return dp[m - 1][n - 1]
```

| ID | Title | Link |
|---|---|---|
| 62 | Unique Paths | [Unique Paths](https://leetcode.com/problems/unique-paths/) |
| 63 | Unique Paths II | [Unique Paths II](https://leetcode.com/problems/unique-paths-ii/) |
| 221 | Maximal Square | [Problem](https://leetcode.com/problems/maximal-square/) · [Solution](https://robinali34.github.io/blog_leetcode_python/2026/04/18/medium-221-maximal-square/) |

## Digit DP (count numbers with property)

```python
from functools import lru_cache


def count_without_adjacent_equal_digits(N: int) -> int:
    s = str(N)

    @lru_cache(maxsize=None)
    def dfs(i: int, prev: int, tight: bool, started: bool) -> int:
        if i == len(s):
            return 1 if started else 0

        res = 0
        lim = int(s[i]) if tight else 9
        for d in range(lim + 1):
            nt = tight and (d == lim)
            ns = started or (d != 0)
            if not ns or prev == -1 or d != prev:
                res += dfs(i + 1, d if ns else prev, nt, ns)
        return res

    return dfs(0, -1, True, False)
```

| ID | Title | Link |
|---|---|---|
| 233 | Number of Digit One | [Number of Digit One](https://leetcode.com/problems/number-of-digit-one/) |
| 902 | Numbers At Most N Given Digit Set | [Numbers At Most N Given Digit Set](https://leetcode.com/problems/numbers-at-most-n-given-digit-set/) |
| 1012 | Numbers With Repeated Digits | [Numbers With Repeated Digits](https://leetcode.com/problems/numbers-with-repeated-digits/) |

## Bitmask DP (TSP / subsets)

```python
def tsp_min_cycle_cost(w: list[list[int]]) -> int:
    n = len(w)
    INF = 10**18
    dp = [[INF] * n for _ in range(1 << n)]
    dp[1][0] = 0  # start at node 0

    for mask in range(1, 1 << n):
        for u in range(n):
            if dp[mask][u] == INF:
                continue
            for v in range(n):
                if (mask >> v) & 1:
                    continue
                nm = mask | (1 << v)
                dp[nm][v] = min(dp[nm][v], dp[mask][u] + w[u][v])

    full = (1 << n) - 1
    return min(dp[full][u] + w[u][0] for u in range(n))
```

| ID | Title | Link |
|---|---|---|
| 847 | Shortest Path Visiting All Nodes | [Shortest Path Visiting All Nodes](https://leetcode.com/problems/shortest-path-visiting-all-nodes/) |
| 698 | Partition to K Equal Sum Subsets | [Partition to K Equal Sum Subsets](https://leetcode.com/problems/partition-to-k-equal-sum-subsets/) |

