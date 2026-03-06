---
layout: post
title: "78. Subsets"
date: 2026-03-05 00:00:00 -0700
categories: [leetcode, medium, backtracking, dfs]
tags: [leetcode, medium, backtracking, dfs, recursion]
permalink: /2026/03/05/medium-78-subsets/
---

# 78. Subsets

## Problem Statement

Given an integer array `nums` of **unique** elements, return **all possible subsets** (the power set).

The solution set must not contain duplicate subsets. You may return the subsets in any order.

## Examples

**Example 1:**

```python
Input:  nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
```

**Example 2:**

```python
Input:  nums = [0]
Output: [[],[0]]
```

## Constraints

- `1 <= nums.length <= 10`
- `-10 <= nums[i] <= 10`
- All the numbers of `nums` are unique.

## Clarification Questions

1. **Uniqueness**: Are all elements unique so we don’t need dedup logic?  
   **Assumption**: Yes.
2. **Order**: Can subsets and elements inside subsets be in any order?  
   **Assumption**: Yes — any order is accepted.
3. **Return all**: Do we need exactly \(2^n\) subsets including the empty subset?  
   **Assumption**: Yes.

## Interview Deduction Process (20 minutes)

**Step 1: Brute force via bitmask (5 min)**  
For each mask from `0` to `2^n - 1`, build a subset by checking which bits are set. This is clean and works in \(O(n \cdot 2^n)\).

**Step 2: Backtracking as a decision tree (7 min)**  
At each index, decide whether to include the current element. This naturally generates all subsets and matches many “choose / not choose” problems.

**Step 3: Efficient recursion with a start pointer (8 min)**  
Build subsets incrementally:
- Always record the current `path` as one subset.
- For each next index `i >= start`, pick `nums[i]`, recurse to `i+1`, then undo (pop).

This avoids copying large intermediate structures beyond the current path.

## Solution Approach

Use backtracking with:
- `start`: the index in `nums` from which we are allowed to choose next elements.
- `path`: the current subset under construction.

Algorithm:

1. Add the current `path` to the answer.
2. Iterate `i` from `start` to end:
   - Add `nums[i]` to `path`.
   - Recurse with `start = i + 1`.
   - Remove `nums[i]` (backtrack).

### Key Insights

1. **Every prefix is a valid subset**  
   The moment we have a `path`, it represents one subset, so we append it before exploring extensions.

2. **Start index prevents duplicates**  
   We only move forward (`i + 1`), ensuring each element is used at most once per subset and subsets are generated once.

3. **Backtracking pattern**  
   `choose -> recurse -> unchoose` is the core template for combinatorial enumeration.

## Python Solution

```python
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        rtn: List[List[int]] = []

        def backtrack(start: int, path: List[int]) -> None:
            rtn.append(path[:])
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, [])
        return rtn
```

## Algorithm Explanation

Think of building subsets in increasing index order:

- `backtrack(start, path)` means: “All subsets that begin with current `path`, using only elements from indices `start..end`.”
- We record `path` immediately because choosing nothing further is one valid subset.
- Each loop iteration chooses one next element and explores all subsets that include it.

This generates exactly \(2^n\) subsets.

## Complexity Analysis

- **Time Complexity**: \(O(n \cdot 2^n)\)  
  There are \(2^n\) subsets, and copying each subset costs up to \(O(n)\).
- **Space Complexity**: \(O(n)\) recursion depth (excluding output).

## Edge Cases

- Single element input, e.g. `[0]` → `[[], [0]]`.
- Negative numbers are fine; we only enumerate subsets.
- Minimum size `n = 1` still includes the empty subset.

## Common Mistakes

- Forgetting to append a copy `path[:]` (and appending `path` directly), which causes all saved subsets to mutate.
- Off-by-one errors in the recursion call (`backtrack(i + 1, path)` is required to avoid reusing the same element).
- Returning early inside the loop, which would cut off branches of the recursion tree.

## Related Problems

- [LC 77: Combinations](https://leetcode.com/problems/combinations/) — Choose `k` elements (same backtracking template).
- [LC 90: Subsets II](https://leetcode.com/problems/subsets-ii/) — Subsets when duplicates exist (adds sorting + skip logic).
- [LC 46: Permutations](https://leetcode.com/problems/permutations/) — Backtracking with used markers instead of a start pointer.

