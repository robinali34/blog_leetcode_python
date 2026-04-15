---
layout: post
title: "[Medium] 260. Single Number III"
date: 2026-03-31 00:00:00 -0700
categories: [leetcode, medium, array, bit-manipulation]
tags: [leetcode, medium, xor, bit-manipulation]
permalink: /2026/03/31/medium-260-single-number-iii/
---

# [Medium] 260. Single Number III

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

Because `p != q`, `x != 0`. Some bit in `x` differs between `p` and `q`. Isolating the lowest set bit:

`diff = x & -x`

every `num` either has that bit set or not, splitting the array into two groups—each group XORs to one of `{p, q}`.

## Detailed walkthrough

**Working example**

- **Input:** `nums = [1, 2, 1, 3, 2, 5]`
- **Output:** `[3, 5]` (either order is acceptable)

**What makes the problem special**

- Exactly **two** values appear **once** (call them `a` and `b`).
- Every other value appears **twice**, so those pairs cancel under XOR.

**Step 1 — XOR the entire array**

XOR everything into one accumulator `x`:

- Duplicate values cancel: `y ^ y == 0`.
- After the full pass, only contributions from `a` and `b` remain:

`x = a ^ b`

This does **not** tell you `a` and `b` individually—it only tells you where they differ.

**Step 2 — Find one bit that separates `a` from `b`**

If `a != b`, then `x != 0`, so at least one bit of `x` is `1`. That bit is `0` in one number and `1` in the other.

Use the standard trick:

`diff = x & (-x)`

`diff` is a single bit mask: the **least significant** `1`-bit of `x`. Any `1` in `x` would work in principle, but this one is cheap to compute and enough to split the two singletons.

**Step 3 — Partition `nums` into two buckets**

For each `num`, test `num & diff`:

- **Group A:** numbers with that bit set (`num & diff != 0`).
- **Group B:** numbers with that bit clear (`num & diff == 0`).

Crucial fact: **`a` and `b` land in different buckets**, because they disagree on the bit encoded by `diff`.  
Duplicates still stay together: both copies of the same value always share the same bit pattern, so they always go to the **same** bucket.

**Step 4 — XOR inside each bucket**

Run XOR independently in each bucket:

- One bucket XORs down to `a`.
- The other XORs down to `b`.

Return `[a, b]` in any order.

**Sanity check on the example**

Pairwise cancellation leaves `3 ^ 5`:

`1 ^ 2 ^ 1 ^ 3 ^ 2 ^ 5 = 3 ^ 5 = 6` (binary `110`).

The lowest separating bit is `2` (`diff = 6 & (-6) = 2`).  
Partition by `num & 2`: values `2`, `3`, `2` share that bit; `1`, `1`, `5` do not. XOR within the two buckets yields `3` and `5` respectively.

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
