---
layout: post
title: "[Medium] 931. Minimum Falling Path Sum"
date: 2026-03-23 00:00:00 -0700
categories: [leetcode, medium, dp, matrix]
tags: [leetcode, medium, dynamic-programming, matrix]
permalink: /2026/03/23/medium-931-minimum-falling-path-sum/
---

# [Medium] 931. Minimum Falling Path Sum

## Problem Statement

Given an `n x n` integer matrix, return the minimum sum of any falling path through `matrix`.

A falling path starts at any element in the first row and chooses one element from each row.  
From position `(row, col)`, the next row's chosen column can be:

- `col`
- `col - 1`
- `col + 1`

## Examples

**Example 1:**

```python
Input: matrix = [[2,1,3],[6,5,4],[7,8,9]]
Output: 13
# Path: 1 -> 5 -> 7
```

**Example 2:**

```python
Input: matrix = [[-19,57],[-40,-5]]
Output: -59
```

## Constraints

- `n == matrix.length == matrix[i].length`
- `1 <= n <= 100`
- `-100 <= matrix[i][j] <= 100`

## Clarification Questions

1. **Can we start from any column in the first row?**  
   Yes, start can be any `matrix[0][j]`.
2. **From `(i, j)`, are moves limited to the next row only?**  
   Yes, only to row `i + 1` at columns `j-1`, `j`, `j+1` (if in bounds).
3. **Can matrix values be negative?**  
   Yes, values may be negative, so greedy local choices are unsafe.
4. **Is modifying the input matrix allowed?**  
   Usually yes on LeetCode; if not, use the row-buffer DP option.
5. **What should be returned for `n = 1`?**  
   Return the single cell value.

## Analysis Process

### 1) Brute force baseline

At each row you can branch up to 3 ways, so naive DFS explores about `3^(n-1)` paths (exponential).

### 2) Overlapping subproblems

Many different paths reach the same cell `(i, j)`.  
So compute the minimum path sum to each cell once and reuse it.

### 3) DP state and transition

Let DP value at `(i, j)` be minimum falling path sum ending at `(i, j)`.

Transition comes from previous row:
- up: `(i - 1, j)`
- up-left: `(i - 1, j - 1)` if valid
- up-right: `(i - 1, j + 1)` if valid

So:

`matrix[i][j] += min(three valid parents)`

### 4) Result extraction

A valid falling path ends anywhere in last row, so final answer is:

`min(last_row_dp_values)`

## Solution Options

### Option 1: Top-Down DFS + Memoization

Define `dfs(i, j)` = minimum falling path sum starting at cell `(i, j)` and going to the last row.

Transition:

- next row same column: `(i + 1, j)`
- next row left diagonal: `(i + 1, j - 1)` if valid
- next row right diagonal: `(i + 1, j + 1)` if valid

Memoization avoids repeated subproblems.

```python
from functools import lru_cache
from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)

        @lru_cache(maxsize=None)
        def dfs(i: int, j: int) -> int:
            if j < 0 or j >= n:
                return float("inf")
            if i == n - 1:
                return matrix[i][j]
            return matrix[i][j] + min(
                dfs(i + 1, j),
                dfs(i + 1, j - 1),
                dfs(i + 1, j + 1),
            )

        return min(dfs(0, j) for j in range(n))
```

### Option 2: Bottom-Up DP with Extra Row Buffer

Use a separate `prev` array for DP values of the previous row and build `curr` for the current row.

```python
from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        prev = matrix[0][:]

        for i in range(1, n):
            curr = [0] * n
            for j in range(n):
                best = prev[j]
                if j > 0:
                    best = min(best, prev[j - 1])
                if j < n - 1:
                    best = min(best, prev[j + 1])
                curr[j] = matrix[i][j] + best
            prev = curr

        return min(prev)
```

### Option 3: Bottom-Up In-Place DP (Most Space-Efficient)

Reuse `matrix` itself as the DP table.

```python
from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        for i in range(1, n):
            for j in range(n):
                best = matrix[i - 1][j]
                if j > 0:
                    best = min(best, matrix[i - 1][j - 1])
                if j < n - 1:
                    best = min(best, matrix[i - 1][j + 1])
                matrix[i][j] += best
        return min(matrix[-1])
```

## Comparison

| Option | Idea | Time | Extra Space | Pros | Cons |
|---|---|---:|---:|---|---|
| Top-down memo | DFS + cache | O(n^2) | O(n^2) | Very intuitive recurrence | Recursion overhead, stack depth |
| Bottom-up buffer | Iterative + `prev/curr` | O(n^2) | O(n) | No recursion, does not mutate input | Slightly more memory |
| In-place bottom-up | Write DP into `matrix` | O(n^2) | O(1) | Best space usage, concise | Mutates input matrix |

In interviews:

- If mutation is allowed, in-place DP is usually the best final answer.
- If mutation is not allowed, use the row-buffer version.
- If you want to show recurrence thinking first, start with top-down memo.

## Why In-Place DP Works

Each row only depends on the row directly above it.  
When processing row `i`, row `i-1` is already finalized, so updating `matrix[i][j]` in place is safe and saves extra space.

## Recommended Python Solution

Use Option 3 (in-place DP) for minimal extra space.

## Complexity Analysis

- **Time:** O(n^2)
- **Space:** O(1) extra (in-place update)

## Edge Cases

- `n = 1` -> answer is the single cell value.
- Negative values -> still valid; DP naturally handles negatives.
- Left/right boundaries -> only valid neighbors are considered.

## Common Mistakes

- Accessing out-of-bounds neighbors at `j = 0` or `j = n - 1`.
- Using exponential DFS without memoization.
- Forgetting that answer is minimum in the last row, not bottom-right cell.

## Related Problems

- [LC 64: Minimum Path Sum](https://leetcode.com/problems/minimum-path-sum/)
- [LC 120: Triangle](https://leetcode.com/problems/triangle/)
- [LC 1289: Minimum Falling Path Sum II](https://leetcode.com/problems/minimum-falling-path-sum-ii/)
