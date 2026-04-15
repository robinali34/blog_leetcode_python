---
layout: post
title: "[Medium] 2342. Max Sum of a Pair With Equal Sum of Digits"
date: 2026-04-11 00:00:00 -0700
categories: [leetcode, medium, array, hash-table]
tags: [leetcode, medium, hash-map, digits]
permalink: /2026/04/11/medium-2342-max-sum-of-a-pair-with-equal-sum-of-digits/
---

# [Medium] 2342. Max Sum of a Pair With Equal Sum of Digits

## Problem Statement

You are given a **0-indexed** array `nums` of **positive** integers.

For each number, define **digit sum** as the sum of its decimal digits.

Return the **maximum** value of `nums[i] + nums[j]` over pairs `i < j` such that both numbers have the **same** digit sum. If no such pair exists, return `-1`.

## Examples

**Example 1:**

```python
Input: nums = [18,43,36,13,7]
Output: 54
# Pairs with equal digit sum: (18,36) -> 9+9 -> sum 54
```

**Example 2:**

```python
Input: nums = [10,12,19,14]
Output: -1
```

## Constraints

- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^9`

## Analysis

Group numbers by digit sum `s`. For each `x`, if we have seen another number with the same `s`, update answer with `best[s] + x`, then set `best[s] = max(best[s], x)`.

Only the **largest** value per digit sum matters for future pairs.

## Python Solution

```python
from typing import List


class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        best = {}
        rtn = -1
        for x in nums:
            s = sum(map(int, str(x)))
            if s in best:
                rtn = max(rtn, best[s] + x)
            best[s] = max(best.get(s, 0), x)
        return rtn
```

## Complexity

- **Time:** O(n · d) where `d` is the number of digits per value (at most 10 here)
- **Space:** O(k) for distinct digit sums `k` (at most on the order of `9 * digits`)

## Common Mistakes

- Using a list per group and sorting (slower); tracking only the max per key is enough.
- Forgetting to return `-1` when no pair exists.

## Related Problems

- [LC 1679: Max Number of K-Sum Pairs](https://leetcode.com/problems/max-number-of-k-sum-pairs/)
- [LC 1010: Pairs of Songs With Total Durations Divisible by 60](https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/)
