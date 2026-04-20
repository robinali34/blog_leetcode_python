---
layout: post
title: "[Medium] 329. Longest Increasing Path in a Matrix"
date: 2026-04-18 00:00:00 -0700
categories: [leetcode, medium, matrix, dynamic-programming, dfs]
permalink: /2026/04/18/medium-329-longest-increasing-path-in-a-matrix/
tags: [leetcode, medium, matrix, dfs, memoization, topological-sort, dag]
---

# [Medium] 329. Longest Increasing Path in a Matrix

Given an `m x n` integer matrix, return the length of the longest strictly increasing path.

You may move in four directions: up, down, left, right.

## Problem Summary

- each next cell must be strictly greater
- no diagonal moves
- no out-of-bounds moves

## Core Idea (DFS + Memoization)

Brute force repeats the same subproblems many times.

Use:

1. DFS to explore increasing paths
2. DP memoization to cache best answer from each cell

Define:

`dp[r][c] = longest increasing path length starting from (r, c)`

Transition:

`dp[r][c] = 1 + max(dp[nr][nc])` over valid neighbors with `matrix[nr][nc] > matrix[r][c]`.

If no valid neighbor exists, `dp[r][c] = 1`.

### Example

```text
9  9  4
6  6  8
2  1  1
```

One longest path is:

`1 -> 2 -> 6 -> 9`

Answer: `4`

## Why Memoization Matters

Without memoization, each cell can branch repeatedly and recompute paths.

With memoization:

- each cell is solved once
- each edge check is constant work
- total time becomes `O(m * n)`

## Solution 1: DFS + Memoization (Top-down DP)

```python
from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0

        rows, cols = len(matrix), len(matrix[0])
        dp = [[0] * cols for _ in range(rows)]
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

        def dfs(r: int, c: int) -> int:
            if dp[r][c] != 0:
                return dp[r][c]

            best = 1
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] > matrix[r][c]:
                    best = max(best, 1 + dfs(nr, nc))

            dp[r][c] = best
            return best

        ans = 0
        for r in range(rows):
            for c in range(cols):
                ans = max(ans, dfs(r, c))
        return ans
```

## Solution 2: Topological Sort (Kahn's Algorithm)

Treat each cell as a node in a DAG:

- edge `u -> v` when `matrix[v] > matrix[u]`
- indegree of a cell = count of smaller neighbors that point to it

Start BFS from indegree-0 nodes (local minima).
Each BFS layer increases path length by 1.
Number of layers = longest increasing path.

```python
from collections import deque
from typing import List


class Solution:
    def longestIncreasingPathTopo(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0

        rows, cols = len(matrix), len(matrix[0])
        indegree = [[0] * cols for _ in range(rows)]
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

        # Build indegree: smaller neighbor -> current cell.
        for r in range(rows):
            for c in range(cols):
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] < matrix[r][c]:
                        indegree[r][c] += 1

        q = deque()
        for r in range(rows):
            for c in range(cols):
                if indegree[r][c] == 0:
                    q.append((r, c))

        path_len = 0
        while q:
            path_len += 1
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] > matrix[r][c]:
                        indegree[nr][nc] -= 1
                        if indegree[nr][nc] == 0:
                            q.append((nr, nc))

        return path_len
```

## Complexity

- **Time:** `O(m * n)`
- **Space:** `O(m * n)` for DP/indegree
- **Recursion stack (DFS version):** up to `O(m * n)` in worst case
