---
layout: post
title: "[Medium] 2461. Maximum Sum of Distinct Subarrays With Length K"
date: 2026-04-09 00:00:00 -0700
categories: [leetcode, medium, array, sliding-window]
tags: [leetcode, medium, sliding-window, hash-map]
permalink: /2026/04/09/medium-2461-maximum-sum-of-distinct-subarrays-with-length-k/
---

# [Medium] 2461. Maximum Sum of Distinct Subarrays With Length K

## Problem Statement

Given an integer array `nums` and an integer `k`, find the maximum sum among all subarrays of length `k` such that all elements in that subarray are distinct.

If no such subarray exists, return `0`.

## Examples

```python
Input: nums = [1,5,4,2,9,9,9], k = 3
Output: 15
# Distinct windows of size 3: [1,5,4]=10, [5,4,2]=11, [4,2,9]=15
```

```python
Input: nums = [4,4,4], k = 3
Output: 0
```

## Clarification Questions

1. **Exactly size `k`?** Yes, not smaller/larger.
2. **If all windows have duplicates?** Return `0`.
3. **Can numbers be large?** Yes; use O(n) approach with running sum.

## Analysis

Use a sliding window with:

- `begin`, `end` pointers
- running `curr_sum`
- `num_to_idx` map of each value’s latest index

When extending with `nums[end]`, if it appeared in the current window, shrink `begin` past its last occurrence. Also shrink if window size exceeds `k`.

Whenever window length is exactly `k`, all elements are distinct by construction, so update answer with `curr_sum`.

## Python Solution

```python
from typing import List


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        rtn = 0
        curr_sum = 0
        begin = 0
        end = 0
        num_to_idx = {}
        while end < len(nums):
            curr_num = nums[end]
            last_occur = num_to_idx.get(curr_num, -1)
            while begin <= last_occur or end - begin + 1 > k:
                curr_sum -= nums[begin]
                begin += 1
            num_to_idx[curr_num] = end
            curr_sum += nums[end]
            if end - begin + 1 == k:
                rtn = max(rtn, curr_sum)
            end += 1
        return rtn
```

## Complexity

- **Time:** O(n)
- **Space:** O(n) for the hash map

## Common Mistakes

- Only checking duplicates but forgetting to keep window length at most `k`.
- Recomputing each window sum from scratch (O(nk)).

## Related Problems

- [LC 3: Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)
- [LC 713: Subarray Product Less Than K](https://leetcode.com/problems/subarray-product-less-than-k/)
