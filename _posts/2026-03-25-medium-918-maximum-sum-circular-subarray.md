---
layout: post
title: "[Medium] 918. Maximum Sum Circular Subarray"
date: 2026-03-25 00:00:00 -0700
categories: [leetcode, medium, array, kadane]
tags: [leetcode, medium, array, dynamic-programming, kadane]
permalink: /2026/03/25/medium-918-maximum-sum-circular-subarray/
---

# [Medium] 918. Maximum Sum Circular Subarray

## Problem Statement

Given a circular integer array `nums` of length `n`, return the maximum possible sum of a non-empty subarray.

A subarray can be:

- **normal (non-wrapping):** contiguous inside `[0..n-1]`
- **wrapping:** takes suffix + prefix due to circular connection

## Examples

**Example 1:**

```python
Input: nums = [1,-2,3,-2]
Output: 3
```

**Example 2:**

```python
Input: nums = [5,-3,5]
Output: 10
# wrapping subarray: [5] + [5]
```

**Example 3:**

```python
Input: nums = [-3,-2,-3]
Output: -2
```

## Constraints

- `1 <= nums.length <= 3 * 10^4`
- `-3 * 10^4 <= nums[i] <= 3 * 10^4`

## Clarification Questions

1. **Must subarray be non-empty?**  
   Yes, at least one element must be chosen.
2. **Can wrapping use all elements?**  
   Conceptually wrapping is total minus a middle gap, but removing all elements is invalid (empty subarray).
3. **How to handle all-negative arrays?**  
   Return the largest single element (standard Kadane result).

## Analysis Process

### 1) Brute force

Try all start/end pairs on a doubled array with length cap `n`.  
This is O(n^2) (or worse), too slow.

### 2) Key split

Maximum circular subarray is either:

- **Case A:** non-wrapping max subarray -> standard Kadane (`maxSum`)
- **Case B:** wrapping max subarray

For wrapping, think as:

`wrapping_sum = total_sum - minimum_subarray_sum`

So compute:

- `maxSum` using Kadane max
- `minSum` using Kadane min
- `total`

Final answer is:

- if all numbers are negative (`maxSum < 0`): return `maxSum`
- else: `max(maxSum, total - minSum)`

## Solution Options

### Option 1: Kadane max + Kadane min (Optimal)

```python
from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total = 0
        maxSum = nums[0]
        curMax = 0
        minSum = nums[0]
        curMin = 0

        for x in nums:
            curMax = max(x, curMax + x)
            maxSum = max(maxSum, curMax)

            curMin = min(x, curMin + x)
            minSum = min(minSum, curMin)

            total += x
        if maxSum < 0:
            return maxSum
        return max(maxSum, total - minSum)
```

### Option 2: Prefix/Suffix helper arrays

Precompute best prefix sums and suffix sums, then combine wrapping candidates.  
Works in O(n) time but O(n) space and more code; usually less preferred than Option 1.

## Comparison

| Option | Time | Extra Space | Pros | Cons |
|---|---:|---:|---|---|
| Kadane max + min | O(n) | O(1) | Short, optimal, interview-friendly | Needs care for all-negative case |
| Prefix/Suffix combine | O(n) | O(n) | Intuitive wrap construction | More memory, more implementation detail |

## Why the All-Negative Guard Is Required

If all numbers are negative:

- `maxSum` is the maximum element (correct)
- `minSum` equals `total`
- `total - minSum = 0` would incorrectly imply empty subarray

So when `maxSum < 0`, return `maxSum` directly.

## Complexity Analysis

- **Time:** O(n)
- **Space:** O(1)

## Common Mistakes

- Forgetting the all-negative guard.
- Using `total - minSum` without ensuring non-empty result.
- Mixing initialization of Kadane states incorrectly.

## Related Problems

- [LC 53: Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)
- [LC 152: Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/)
