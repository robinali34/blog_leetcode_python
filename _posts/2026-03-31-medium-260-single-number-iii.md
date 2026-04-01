---
layout: post
title: "260. Single Number III"
date: 2026-03-31 00:00:00 -0700
categories: [leetcode, medium, array, bit-manipulation]
tags: [leetcode, medium, xor, bit-manipulation]
permalink: /2026/03/31/medium-260-single-number-iii/
---

# 260. Single Number III

## Problem Statement

Given an integer array `nums` where exactly **two** elements appear only once and the rest appear **twice**, return the two unique numbers in **any order**.

## Examples

**Example 1:**

```python
Input: nums = [1,2,1,3,2,5]
Output: [3,5]  # order may vary
# The integers with odd frequency are 3 and 5.
```

**Example 2:**

```python
Input: nums = [-1,0]
Output: [-1,0]
```

## Constraints

- `2 <= nums.length <= 3 * 10^4`
- `-2^31 <= nums[i] <= 2^31 - 1`
- Exactly two integers appear once; the others appear twice.

## Clarification Questions

1. **Output order?** Any order is fine.
2. **Can numbers be negative?** Yes; use two’s complement; `x & -x` is still valid in Python (handles signed semantics via unlimited-precision integers consistently for bit tests).

## Analysis Process

XOR of the whole array: every value that appears twice cancels (`a ^ a == 0`).  
Let the two singletons be `p` and `q`. Then:

`x = p ^ q`

Because `p != q`, `x != 0`. Some bit in `x` differs between `p` and `q`. isolating the lowest set bit:

`diff = x & -x`

every `num` either has that bit set or not, splitting the array into two groups—each group XORs to one of `{p, q}`.

## Python Solution

```python
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        x = 0
        for num in nums:
            x ^= num

        diff = x & -x
        a = 0
        b = 0
        for num in nums:
            if num & diff:
                a ^= num
            else:
                b ^= num
        return [a, b]
```

## Why `x & -x`?

`-x` is bitwise negation plus one. `x & -x` yields the lowest set bit of `x` (or zero if `x` is zero), which is non-zero here because `p != q`.

## Complexity Analysis

- **Time:** O(n) — two passes
- **Space:** O(1) extra

## Common Mistakes

- Assuming `diff` must be a power-of-two *value* yourself; use `x & -x`.
- Forgetting that both passes XOR within each bucket must recover both unknowns.

## Related Problems

- [LC 136: Single Number](https://leetcode.com/problems/single-number/)
- [LC 137: Single Number II](https://leetcode.com/problems/single-number-ii/)
- [LC 389: Find the Difference](/2026/03/27/easy-389-find-the-difference/)
