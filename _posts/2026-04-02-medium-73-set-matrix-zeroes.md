---
layout: post
title: "73. Set Matrix Zeroes"
date: 2026-04-02 00:00:00 -0700
categories: [leetcode, medium, array, matrix]
tags: [leetcode, medium, matrix, in-place]
permalink: /2026/04/02/medium-73-set-matrix-zeroes/
---

# 73. Set Matrix Zeroes

## Problem Statement

Given an `m x n` integer matrix, if an element is `0`, set its entire row and column to `0`.

You must do it **in-place**.

## Examples

**Example 1:**

```python
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
```

**Example 2:**

```python
Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
```

## Constraints

- `m == matrix.length`
- `n == matrix[0].length`
- `1 <= m, n <= 200`
- `-2^31 <= matrix[i][j] <= 2^31 - 1`

## Clarification Questions

1. **Must we preserve original non-zero values outside zeroed rows/cols?** Yes.
2. **Extra space allowed?** Follow-up usually asks for **O(1)** extra space; O(m + n) is fine for the first solution.

## Solution Option 1: O(m + n) space with row/col sets

```python
from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        R = len(matrix)
        C = len(matrix[0])
        rows, cols = set(), set()
        for i in range(R):
            for j in range(C):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
        for i in range(R):
            for j in range(C):
                if i in rows or j in cols:
                    matrix[i][j] = 0
```

Two passes: first collect which rows/columns must become zero; second, rewrite accordingly.

## Solution Option 2: O(1) extra space using first row/col as markers

Idea:

- Use `matrix[0][j]` as a marker that column `j` must be zeroed.
- Use `matrix[i][0]` as a marker that row `i` must be zeroed.
- Track separately whether the **first column** should become all zero (`is_col`).

```python
from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        is_col = False
        R = len(matrix)
        C = len(matrix[0])

        for i in range(R):
            if matrix[i][0] == 0:
                is_col = True
            for j in range(1, C):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        for i in range(1, R):
            for j in range(1, C):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if matrix[0][0] == 0:
            for j in range(C):
                matrix[0][j] = 0

        if is_col:
            for i in range(R):
                matrix[i][0] = 0
```

## Complexity

For both options:

- **Time:** O(m·n)
- **Space:** Option 1 — O(m + n); Option 2 — O(1) extra

## Common Mistakes

- Zeroing a row/column immediately when you see a zero (this can create new zeros that incorrectly propagate).
- Forgetting to handle the first row/first column separately when using them as markers.

## Related Problems

- [LC 289: Game of Life](https://leetcode.com/problems/game-of-life/)
