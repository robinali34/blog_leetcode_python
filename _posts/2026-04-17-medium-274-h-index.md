---
layout: post
title: "[Medium] 274. H-Index"
date: 2026-04-17 00:00:00 -0700
categories: [leetcode, medium, array, sorting]
permalink: /2026/04/17/medium-274-h-index/
tags: [leetcode, medium, array, sorting, greedy, h-index]
---

# [Medium] 274. H-Index

You are given an array `citations` where `citations[i]` is the number of citations of the *i*-th paper.

Return the **maximum** integer `h` such that there are **at least** `h` papers with **at least** `h` citations each.

## Problem Core

This is not about total citations.

It is about a **balance point**:

How large can `h` be such that enough papers “support” that threshold?

## Key Insight

Sort citations in **descending** order. After sorting, the *i*-th position (1-based) asks:

“Do I have at least `i` papers with citation count ≥ `i`?”

The largest `i` where `citations[i-1] >= i` holds is the answer; the first index where `citations[i] < i + 1` (0-based) stops the streak.

## Example

`[3, 0, 6, 1, 5]`

Sort descending: `[6, 5, 3, 1, 0]`

| papers (h) | citations at rank | check   |
| ---------- | ----------------- | ------- |
| 1          | 6                 | 6 ≥ 1   |
| 2          | 5                 | 5 ≥ 2   |
| 3          | 3                 | 3 ≥ 3   |
| 4          | 1                 | 1 < 4   |

Answer: **3**.

## Solution — Sorting (interview-friendly)

```python
from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        for i in range(len(citations)):
            if citations[i] < i + 1:
                return i
        return len(citations)
```

## Complexity

- **Time:** `O(n log n)` for sorting
- **Space:** `O(1)` extra (in-place sort aside from the language/runtime)
