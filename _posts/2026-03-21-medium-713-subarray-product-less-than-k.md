---
layout: post
title: "[Medium] 713. Subarray Product Less Than K"
date: 2026-03-21 00:00:00 -0700
categories: [leetcode, medium, array, sliding-window]
tags: [leetcode, medium, array, sliding-window, two-pointers]
permalink: /2026/03/21/medium-713-subarray-product-less-than-k/
---

# [Medium] 713. Subarray Product Less Than K

## Problem Statement

Given an array of integers `nums` and an integer `k`, return the number of **contiguous** subarrays where the **product** of all the elements in the subarray is **strictly less than** `k`.

## Examples

**Example 1:**

```python
Input: nums = [10,5,2,6], k = 100
Output: 8
# Subarrays with product < 100:
# [10], [5], [2], [6], [10,5], [5,2], [2,6], [5,2,6]
```

**Example 2:**

```python
Input: nums = [1,2,3], k = 0
Output: 0
```

## Constraints

- `1 <= nums.length <= 3 * 10^4`
- `1 <= nums[i] <= 1000`
- `0 <= k <= 10^6`

## Clarification Questions

1. **Strictly less than k**: Product must be `< k`, not `<= k`?  
   **Assumption**: Yes.
2. **k ≤ 1**: If `k <= 1`, no positive product of positive integers can be `< k`?  
   **Assumption**: Return `0` (handles `k == 0` and `k == 1`).
3. **All positive**: `nums[i] >= 1` — no zeros or negatives in constraints?  
   **Assumption**: Yes — sliding window with product division is safe.

## Interview Deduction Process (20 minutes)

**Step 1: Brute force (5 min)**  
For each `(left, right)`, compute product — O(n²) or worse. Too slow for n up to 3×10⁴.

**Step 2: Sliding window (10 min)**  
Because all elements are **positive**, multiplying more elements only **increases** the product. For a fixed `right`, if we shrink `left` until `product < k`, every subarray ending at `right` with `left' ∈ [left, right]` has product `< k`. Count = `right - left + 1`.

**Step 3: Edge case k (5 min)**  
If `k <= 1`, no valid subarray (for positive integers). Early return `0`.

## Solution Approach

**Two pointers + product:** Maintain `[left, right]` with product of that window. Expand `right`, multiply `nums[right]`. While `product >= k`, divide out `nums[left]` and increment `left`. Add `(right - left + 1)` to the answer — that is the number of valid subarrays ending at `right`.

### Key Insights

1. **Positivity** — Monotonicity of product allows shrinking `left` only from the left.
2. **Count trick** — For each `right`, valid subarrays ending at `right` are exactly those starting at `left, left+1, …, right`.
3. **k ≤ 1** — Quick reject; avoids useless loops.

## Python Solution

### Sliding window (O(n) time, O(1) space)

```python
from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        prod = 1
        left = 0
        cnt = 0
        for right in range(len(nums)):
            prod *= nums[right]
            while prod >= k:
                prod //= nums[left]
                left += 1
            cnt += right - left + 1
        return cnt
```

## Algorithm Explanation

We keep a window `[left, right]` whose product is `< k`. When we add `nums[right]`, the product may become `>= k`; we repeatedly remove `nums[left]` from the product (divide) and move `left` right until the product is again `< k` (or the window is empty in the sense that we cannot shrink further — but with `k > 1` and positive nums, we always end with a valid window length). Every subarray ending at `right` with start index in `[left, right]` has product `< k`, giving `right - left + 1` subarrays.

## Complexity Analysis

- **Time**: O(n) — each index enters and leaves the window at most once.
- **Space**: O(1).

## Edge Cases

- `k <= 1` → `0`.
- Single element `nums = [5]`, `k = 10` → `1`.
- Large `k` — still one linear pass.

## Common Mistakes

- **Forgetting `k <= 1`** — Without it, the `while prod >= k` loop can misbehave or overcount.
- **Using `<= k` in problem vs code** — Problem asks strictly `< k`; loop condition is `prod >= k`.
- **Zeros or negatives** — This solution assumes all positive; the given constraints satisfy that.

## Related Problems

- [LC 209: Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/) — Sliding window on sum.
- [LC 904: Fruit Into Baskets](https://leetcode.com/problems/fruit-into-baskets/) — At most K distinct sliding window.
- [LC 325: Maximum Size Subarray Sum Equals k](https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/) — Prefix sum + map.
