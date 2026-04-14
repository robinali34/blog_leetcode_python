---
layout: post
title: "1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit"
date: 2026-02-12 00:00:00 -0700
categories: [leetcode, medium, sliding-window, monotonic-queue]
tags: [leetcode, medium, sliding-window, monotonic-queue]
permalink: /2026/02/12/medium-1438-longest-continuous-subarray-with-absolute-diff/
---

## Problem

Given an integer array `nums` and an integer `limit`, return the size of the longest continuous subarray such that the absolute difference between the maximum and minimum element in the subarray is less than or equal to `limit`.

## Examples

**Example 1**

```
Input: nums = [8,2,4,7], limit = 4
Output: 2
Explanation: The longest subarray is [2,4] or [4,7].
```

**Example 2**

```
Input: nums = [10,1,2,4,7,2], limit = 5
Output: 4
Explanation: The longest subarray is [2,4,7,2].
```

**Example 3**

```
Input: nums = [4,2,2,2,4,4,2,2], limit = 0
Output: 3
Explanation: The longest subarray of equal values is length 3 (three 2's).
```

## Constraints

- `1 <= nums.length <= 10^5`
- `0 <= nums[i] <= 10^9`
- `0 <= limit <= 10^9`

## Approach

We need the longest window [l..r] where max(nums[l..r]) - min(nums[l..r]) <= limit.

Two common sliding-window techniques:

1. Multiset (or balanced BST) to maintain current window's min and max. Expand right pointer; when condition violated, shrink left pointer and erase from multiset. Time: O(n log n), Space: O(n).

2. Monotonic deques (optimal): maintain two deques:
   - `decrease` keeps current window's values in decreasing order (front = max)
   - `increase` keeps values in increasing order (front = min)
   Push new value by popping from back while invariant violated. When shrinking left, pop from front if it equals outgoing value. This yields O(n) time and O(n) space.

## Solutions

### Multiset (balanced BST) — O(n log n)

{% raw %}
```python
import bisect

class Solution:
    def longestSubarray(self, nums, limit):
        ms = []  # sorted list
        left = 0
        res = 0
        
        for right in range(len(nums)):
            bisect.insort(ms, nums[right])
            
            while ms[-1] - ms[0] > limit:
                ms.pop(bisect.bisect_left(ms, nums[left]))
                left += 1
            
            res = max(res, right - left + 1)
        
        return res
```
{% endraw %}

### Monotonic Deques — O(n)

{% raw %}
```python
from collections import deque

class Solution:
    def longestSubarray(self, nums, limit):
        increase = deque()  # increasing -> keeps min at front
        decrease = deque()  # decreasing -> keeps max at front
        
        left = 0
        res = 0
        
        for right in range(len(nums)):
            val = nums[right]
            
            # maintain decreasing deque (max at front)
            while decrease and decrease[-1] < val:
                decrease.pop()
            decrease.append(val)
            
            # maintain increasing deque (min at front)
            while increase and increase[-1] > val:
                increase.pop()
            increase.append(val)
            
            # shrink window if invalid
            while decrease[0] - increase[0] > limit:
                if nums[left] == decrease[0]:
                    decrease.popleft()
                if nums[left] == increase[0]:
                    increase.popleft()
                left += 1
            
            res = max(res, right - left + 1)
        
        return resfrom collections import deque

class Solution:
    def longestSubarray(self, nums, limit):
        increase = deque()  # increasing -> keeps min at front
        decrease = deque()  # decreasing -> keeps max at front
        
        left = 0
        res = 0
        
        for right in range(len(nums)):
            val = nums[right]
            
            # maintain decreasing deque (max at front)
            while decrease and decrease[-1] < val:
                decrease.pop()
            decrease.append(val)
            
            # maintain increasing deque (min at front)
            while increase and increase[-1] > val:
                increase.pop()
            increase.append(val)
            
            # shrink window if invalid
            while decrease[0] - increase[0] > limit:
                if nums[left] == decrease[0]:
                    decrease.popleft()
                if nums[left] == increase[0]:
                    increase.popleft()
                left += 1
            
            res = max(res, right - left + 1)
        
        return res

```
{% endraw %}

## Complexity

- Time: O(n) with monotonic deques, O(n log n) with multiset.
- Space: O(n).

## Template Reference

- [Monotonic Queue / Sliding Window](/posts/2025-10-29-leetcode-templates-data-structures/#monotonic-queue)

