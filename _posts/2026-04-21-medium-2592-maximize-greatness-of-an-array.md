---
layout: post
title: "[Medium] 2592. Maximize Greatness of an Array"
date: 2026-04-21 00:00:00 -0700
categories: [leetcode, medium, array, greedy, sorting]
permalink: /2026/04/21/medium-2592-maximize-greatness-of-an-array/
tags: [leetcode, medium, array, greedy, sorting, two-pointers]
---

# [Medium] 2592. Maximize Greatness of an Array

Given an array `nums`, permute it into `perm` to maximize:

`count(i) where perm[i] > nums[i]`

Return that maximum count (called **greatness**).

## Core idea

Sort `nums`. Then greedily match a larger element to beat each smaller element.

- Let `i` point to the smallest value we still need to beat.
- Scan sorted values `x` from left to right.
- If `x > nums[i]`, use `x` to beat it and increment `i`.

At the end, `i` is the answer.

Why this works:

- Using the smallest possible winner for each target preserves larger numbers for harder matches later.
- If a value cannot beat the current smallest target, it cannot beat any later target either.

## Python

```python
from typing import List


class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        for x in nums:
            if x > nums[i]:
                i += 1
        return i
```

## Example

`nums = [1, 3, 5, 2, 1, 3, 1]`

Sorted: `[1, 1, 1, 2, 3, 3, 5]`

- `1` cannot beat `1`
- `1` cannot beat `1`
- `1` cannot beat `1`
- `2` beats `1` -> `i = 1`
- `3` beats `1` -> `i = 2`
- `3` beats `1` -> `i = 3`
- `5` beats `2` -> `i = 4`

Answer: `4`.

## Complexity

- Time: `O(n log n)` due to sorting
- Space: `O(1)` extra (ignoring sort internals)

## Pattern

Greedy matching after sorting (two pointers / sweep matching).
