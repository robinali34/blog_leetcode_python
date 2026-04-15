---
layout: post
title: "[Easy] 217. Contains Duplicate"
date: 2026-03-07 00:00:00 -0700
categories: [leetcode, easy, array, hash-table]
tags: [leetcode, easy, array, set]
permalink: /2026/03/07/easy-217-contains-duplicate/
---

# [Easy] 217. Contains Duplicate

## Problem Statement

Given an integer array `nums`, return `true` if any value appears **at least twice** in the array, and return `false` if every element is distinct.

## Examples

**Example 1:**

```python
Input: nums = [1,2,3,1]
Output: True
```

**Example 2:**

```python
Input: nums = [1,2,3,4]
Output: False
```

**Example 3:**

```python
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: True
```

## Constraints

- `1 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`

## Clarification Questions

1. **At least twice** — Any duplicate (two or more of the same value) suffices?  
   **Assumption**: Yes.
2. **Return as soon as duplicate found** — We can short-circuit.  
   **Assumption**: Yes.

## Interview Deduction Process (20 minutes)

**Step 1: Brute force (5 min)**  
For each element, check if it appears again later — O(n²). Too slow for n up to 10^5.

**Step 2: Sort (5 min)**  
Sort and scan adjacent pairs; if any pair is equal, return true. O(n log n) time, O(1) or O(log n) space depending on sort.

**Step 3: Hash set (10 min)**  
Maintain a set of seen values. For each number, if it is already in the set, return true; otherwise add it. One pass, O(n) time, O(n) space.

## Solution Approach

**Set:** Iterate over `nums`. For each value, if it is in a set of previously seen values, return `True`. Otherwise add it to the set. If the loop finishes, return `False`.

**Sort:** Sort `nums`, then check if any `nums[i] == nums[i+1]`. O(n log n) time.

### Key Insights

1. **Seen set** — One pass with a set gives O(n) time; first repeat triggers true.
2. **No need to count** — We only care about “seen before,” not frequency.
3. **Sort alternative** — If O(n) extra space is undesirable, sorting uses O(log n) stack space (or O(1) for some sorts) but O(n log n) time.

## Python Solution

### Set (O(n) time, O(n) space)

```python
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        for x in nums:
            if x in seen:
                return True
            seen.add(x)
        return False
```

### Sort (O(n log n) time, O(1) extra if in-place)

```python
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False
```

## Algorithm Explanation

**Set:** We only need to know if we’ve seen a value before. As we scan, the first time we see a value we add it to `seen`. The second time we see it we return `True`. If we never see a repeat, return `False`.

**Sort:** After sorting, duplicates (if any) are adjacent. One linear scan over adjacent pairs suffices.

## Complexity Analysis

- **Set**: Time O(n), space O(n).
- **Sort**: Time O(n log n), space O(1) or O(log n) depending on sort implementation.

## Edge Cases

- Single element → no duplicate → `False`.
- Two elements, same value → `True`.
- All distinct → `False`.

## Common Mistakes

- **Using a list instead of a set** — `x in list` is O(n) per check, making the overall solution O(n²). Use a set for O(1) membership.
- **Counting with Counter** — Works but overkill; we only need “seen at least twice,” so a set is enough.

## Related Problems

- [LC 219: Contains Duplicate II](/2026/03/07/easy-219-contains-duplicate-ii/) — Duplicate within distance k.
- [LC 220: Contains Duplicate III](https://leetcode.com/problems/contains-duplicate-iii/) — Near-duplicate within index and value range.
- [LC 268: Missing Number](https://leetcode.com/problems/missing-number/) — Set or math on indices.
