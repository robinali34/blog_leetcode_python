---
layout: post
title: "[Medium] 1870. Minimum Speed to Arrive on Time"
date: 2026-03-30 00:00:00 -0700
categories: [leetcode, medium, binary-search]
tags: [leetcode, medium, binary-search, math]
permalink: /2026/03/30/medium-1870-minimum-speed-to-arrive-on-time/
---

# [Medium] 1870. Minimum Speed to Arrive on Time

## Problem Statement

You are given an array `dist` where `dist[i]` is the distance of the `i`-th train ride, and a floating-point number `hour` representing the time you must arrive by.

You must take rides in order. For each ride except the last, you can only depart at an integer hour, so travel time is rounded up to the next integer hour. For the last ride, exact fractional time is allowed.

Return the minimum positive integer speed needed to arrive on time. If impossible, return `-1`.

## Examples

**Example 1:**

```python
Input: dist = [1,3,2], hour = 6
Output: 1
```

**Example 2:**

```python
Input: dist = [1,3,2], hour = 2.7
Output: 3
```

## Constraints

- `1 <= dist.length <= 10^5`
- `1 <= dist[i] <= 10^5`
- `1 <= hour <= 10^9`
- At most 2 digits after the decimal point in `hour`

## Clarification Questions

1. **Rounding rule:** For rides `0..n-2`, time is `ceil(dist[i] / speed)`?  
   Yes.
2. **Last ride:** use exact `dist[-1] / speed` without ceil?  
   Yes.
3. **Can speed be non-integer?**  
   No, speed must be a positive integer.

## Analysis Process

We need the **minimum** speed satisfying a condition, which suggests binary search on answer.

- Define `can(k)`: can we finish within `hour` at speed `k`?
- If `can(k)` is true, then any larger speed also works (monotonic).
- Binary search smallest `k` in `[1, 10^7]`.

Early impossibility:

- There are `n-1` rounded segments, each taking at least `1` hour if non-zero distance.
- So if `hour <= n - 1`, impossible immediately.

## Python Solution

```python
from typing import List


class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        n = len(dist)
        if hour <= n - 1:
            return -1

        def can(k: int) -> bool:
            t = 0.0
            for i in range(n - 1):
                t += (dist[i] + k - 1) // k
                if t > hour:
                    return False
            t += dist[-1] / k
            return t <= hour

        l, r = 1, 10**7
        while l < r:
            mid = (l + r) // 2
            if can(mid):
                r = mid
            else:
                l = mid + 1
        return l
```

## Why `(dist[i] + k - 1) // k`?

For positive integers, this is integer arithmetic for `ceil(dist[i] / k)`, avoiding floating-point issues on intermediate legs.

## Complexity Analysis

- **Time:** `O(n log 10^7)`  
- **Space:** `O(1)` extra

## Common Mistakes

- Applying `ceil` to the last ride (should not be rounded).
- Forgetting the impossibility check `hour <= n - 1`.
- Binary searching on floating speed instead of integer speed.

## Related Problems

- [LC 875: Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/)
- [LC 1011: Capacity To Ship Packages Within D Days](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/)
