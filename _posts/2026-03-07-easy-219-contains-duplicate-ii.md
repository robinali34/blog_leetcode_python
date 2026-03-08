---
layout: post
title: "219. Contains Duplicate II"
date: 2026-03-07 00:00:00 -0700
categories: [leetcode, easy, array, hash-table, sliding-window]
tags: [leetcode, easy, array, set, sliding-window]
permalink: /2026/03/07/easy-219-contains-duplicate-ii/
---

# 219. Contains Duplicate II

## Problem Statement

Given an integer array `nums` and an integer `k`, return `true` if there are two **distinct indices** `i` and `j` in the array such that `nums[i] == nums[j]` and `abs(i - j) <= k`.

## Examples

**Example 1:**

```python
Input: nums = [1,2,3,1], k = 3
Output: True
# Indices 0 and 3: nums[0] == nums[3] == 1, abs(0-3) == 3 <= 3.
```

**Example 2:**

```python
Input: nums = [1,0,1,1], k = 1
Output: True
# Adjacent 1s at indices 2 and 3; abs(2-3) == 1 <= 1.
```

**Example 3:**

```python
Input: nums = [1,2,3,1,2,3], k = 2
Output: False
# Duplicate 1s at distance 3, duplicate 2s at 3, duplicate 3s at 3; all > 2.
```

## Constraints

- `1 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`
- `0 <= k <= 10^5`

## Clarification Questions

1. **Distinct indices** — i and j must be different?  
   **Assumption**: Yes — “two distinct indices.”
2. **abs(i - j) <= k** — So at most k apart.  
   **Assumption**: Yes.

## Interview Deduction Process (20 minutes)

**Step 1: Brute force (5 min)**  
For each index i, check indices j in [i+1, i+k] for same value. O(n * k). For large k this is slow.

**Step 2: Hash map of last index (10 min)**  
For each value, we only care: “have we seen this value within the last k indices?” So maintain a map: value → most recent index where we saw it. When we see a value, if it’s in the map and current index - last index <= k, return true; else update the map to current index. One pass, O(n).

**Step 3: Sliding window set (5 min)**  
Alternatively, keep a set of the last k elements (by value). When we add a new element, if it’s already in the set we have a duplicate within distance k. When we slide, remove the element that falls out of the window. Same O(n); window set is at most size k+1.

### Key Insights

1. **Last index is enough** — For each value, we only need the most recent index; if the same value appears again within distance k, we’re done.
2. **Update on every occurrence** — When we see a duplicate beyond k, update the stored index to the current one so future occurrences can use it.
3. **Sliding window** — Keeping only the last k indices’ values in a set gives an alternative one-pass solution; remove `nums[i - k - 1]` when moving right.

## Solution Approach

**Map (value → last index):** Scan left to right. For each index `i` and value `v = nums[i]`, if `v` is in the map and `i - map[v] <= k`, return `True`. Otherwise set `map[v] = i`. Return `False` after the loop.

**Sliding window set:** Maintain a set of values in the window `[i-k, i]`. For each new `nums[i]`, if it’s in the set return True; add it; then if `i >= k` remove `nums[i-k]` (the one that just left the window). Window size is k+1.

## Python Solution

### Map: value → last index (O(n) time, O(n) space)

```python
class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        last: dict[int, int] = {}
        for i, x in enumerate(nums):
            if x in last and i - last[x] <= k:
                return True
            last[x] = i
        return False
```

### Sliding window set (O(n) time, O(min(n, k)) space)

```python
class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        window: set[int] = set()
        for i, x in enumerate(nums):
            if x in window:
                return True
            window.add(x)
            if i >= k:
                window.discard(nums[i - k])
        return False
```

## Algorithm Explanation

**Map:** We only need to know the most recent index for each value. When we see `x` at index `i`, we check whether we’ve seen `x` before at an index `j` with `i - j <= k`. If so, return True. Otherwise record `last[x] = i` and continue. If we never find such a pair, return False.

**Sliding window:** The set holds values that are in the “current window” of the last k+1 indices. When we add `nums[i]`, if it’s already in the set we have a duplicate within distance k. After adding, we drop `nums[i-k]` from the set when `i >= k` so the set only has indices in `[i-k, i]`.

## Complexity Analysis

- **Time**: O(n) for both approaches.
- **Space**: O(n) for the map (in the worst case all distinct values); O(min(n, k+1)) for the window set.

## Edge Cases

- k == 0 → no two distinct indices can have distance <= 0 → always `False` (unless we interpret “distance 0” differently; problem says distinct indices so distance at least 1). So k==0 → False.
- Single element → no pair → `False`.
- Two equal elements at distance 1, k >= 1 → `True`.

## Common Mistakes

- **Storing all indices per value** — We only need the last index; storing a list is unnecessary and uses more space.
- **Wrong window boundary** — For “within k,” we care about indices in `[i-k, i]` (inclusive), so the window has size k+1. When at index i, remove the value at index `i - k - 1`? No: if we’re at index i, the valid previous indices are i-1, i-2, ..., i-k. So the value that “exits” when we move to i is at index i-k-1. So when i >= k, we remove nums[i - k - 1]. Wait: at index i, we want to check if any of indices i-1, i-2, ..., i-k has the same value. So the “window” of indices we care about is [i-k, i-1]. So we haven’t added nums[i] yet when we check. So: check if x in window; if yes return true; add x; then if len(window) > k we need to remove the oldest. The oldest in the window would be at index i-k. So when we’re at index i, the window should contain values from indices [i-k, i-1] before we add i. After we add i, window has [i-k, i]. So we should remove the value at index i-k when we’re at index i+1... So when at index i, after adding nums[i], we remove nums[i-k] (the one that is now at distance k+1 from current). So condition: if i >= k, remove nums[i - k]. That’s what I had. Good.
- **k == 0**: For distinct indices i and j, abs(i-j) >= 1. So if k == 0, no pair can satisfy abs(i-j) <= 0. So return False. The map solution: when k==0, i - last[x] <= 0 implies i == last[x], but we’re updating last[x] = i when we see x, so we’d have seen x at last[x] and now at i; if they’re the same index we don’t have “two distinct indices.” So we check i - last[x] <= k only when we already have last[x] from a previous index. So when we see x at i, if x in last then last[x] is some j < i, so i - j >= 1. For k==0, i - j <= 0 is never true (since i > j). So we return False. Good.

## Related Problems

- [LC 217: Contains Duplicate](/2026/03/07/easy-217-contains-duplicate/) — Any duplicate (no distance constraint).
- [LC 220: Contains Duplicate III](https://leetcode.com/problems/contains-duplicate-iii/) — Duplicate within index distance k and value distance t.
- [LC 242: Valid Anagram](/2026/03/07/easy-242-valid-anagram/) — Character counting.
