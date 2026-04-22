---
layout: post
title: "[Medium] 2952. Minimum Number of Coins to be Added"
date: 2026-04-21 00:00:00 -0700
categories: [leetcode, medium, array, greedy, sorting]
permalink: /2026/04/21/medium-2952-minimum-number-of-coins-to-be-added/
tags: [leetcode, medium, greedy, array, sorting, coverage]
---

# [Medium] 2952. Minimum Number of Coins to be Added

You are given an array `coins` and an integer `target`.

You may add new coin values. Return the **minimum number of added coins** so that every value in `[1, target]` can be formed.

## Problem summary

This is a classic greedy coverage problem.

If we can already form every value in `[1, miss)`, then:

- a coin `c <= miss` extends coverage to `[1, miss + c)`;
- but if the next coin is `c > miss`, then `miss` itself is impossible right now.

So the best coin to add is exactly `miss`, because it maximally doubles coverage:

`[1, miss)` -> `[1, 2 * miss)`.

## Greedy strategy

1. Sort `coins`.
2. Track the smallest uncovered value `miss` (start `miss = 1`).
3. While `miss <= target`:
   - If next coin `<= miss`, consume it: `miss += coin`.
   - Else add a new coin `miss`: `miss += miss`, `added += 1`.

Why optimal:

- When `coin > miss`, no existing coin can create `miss`.
- Any added coin `< miss` does not help create `miss`.
- Any added coin `> miss` still misses `miss`.
- So adding `miss` is forced, and also gives the largest jump.

## Python

```python
from typing import List


class Solution:
    def minimumAddedCoins(self, coins: List[int], target: int) -> int:
        coins.sort()
        miss = 1
        i = 0
        added = 0

        while miss <= target:
            if i < len(coins) and coins[i] <= miss:
                miss += coins[i]
                i += 1
            else:
                miss += miss
                added += 1

        return added
```

## Example

`coins = [1, 4, 10]`, `target = 19`

- `miss = 1`, take `1` -> `miss = 2` (now cover `[1, 2)`)
- next coin `4 > 2`, add `2` -> `miss = 4`, `added = 1`
- take `4` -> `miss = 8`
- next coin `10 > 8`, add `8` -> `miss = 16`, `added = 2`
- take `10` -> `miss = 26` (already `> 19`)

Answer: `2`.

## Complexity

- Time: `O(n log n)` (sorting) + `O(n + additions)` scan.
- Space: `O(1)` extra (ignoring sort internals).

## Pattern recognition

This is the same greedy pattern as "patching array" style problems:

- maintain a contiguous representable prefix,
- patch exactly the first gap,
- maximize coverage growth at each forced step.
