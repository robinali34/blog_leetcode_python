---
layout: post
title: "2270. Number of Ways to Split Array"
date: 2026-04-06 00:00:00 -0700
categories: [leetcode, medium, array, prefix-sum]
tags: [leetcode, medium, prefix-sum, two-pointers]
permalink: /2026/04/06/medium-2270-number-of-ways-to-split-array/
---

# 2270. Number of Ways to Split Array

## Problem Statement

You are given a **0-indexed** integer array `nums` of length `n`.

A **split** at index `i` means `0 <= i < n - 1`: the left part is `nums[0..i]` and the right part is `nums[i+1..n-1]`.

Return the number of splits such that the **sum of the left part** is **greater than or equal to** the **sum of the right part**.

## Examples

**Example 1:**

```python
Input: nums = [10,4,-8,7]
Output: 2
# Splits: i=0 -> 10 >= 3 ; i=1 -> 14 >= -1
```

**Example 2:**

```python
Input: nums = [2,3,1,0]
Output: 2
```

## Constraints

- `2 <= nums.length <= 10^5`
- `-10^5 <= nums[i] <= 10^5`

## Analysis

For a split after index `i` (left is indices `0..i`):

- `left_sum = sum(nums[0:i+1])`
- `right_sum = total - left_sum`

Count indices `i` in `0..n-2` with `left_sum >= right_sum`.

Either precompute prefix sums once, or maintain running `left_sum` / `right_sum` in one pass (O(n) time, O(1) extra space).

## Solution Option 1: Prefix array

```python
from typing import List


class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n = len(nums)
        pref_sum = [0] * n
        pref_sum[0] = nums[0]
        for i in range(1, n):
            pref_sum[i] = pref_sum[i - 1] + nums[i]
        return sum(
            1 for i in range(n - 1) if pref_sum[i] >= pref_sum[-1] - pref_sum[i]
        )
```

## Solution Option 2: Running left / right sums

```python
from typing import List


class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        left_sum = 0
        right_sum = sum(nums)
        count = 0
        for i in range(len(nums) - 1):
            left_sum += nums[i]
            right_sum -= nums[i]
            if left_sum >= right_sum:
                count += 1
        return count
```

## Complexity

- **Time:** O(n)
- **Space:** Option 1 — O(n) for `pref_sum`; Option 2 — O(1) extra

## Common Mistakes

- Allowing `i == n - 1` as a split (right part must be non-empty).
- Off-by-one on what “left” includes for index `i`.

## Related Problems

- [LC 1480: Running Sum of 1d Array](https://leetcode.com/problems/running-sum-of-1d-array/)
- [LC 238: Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/)
