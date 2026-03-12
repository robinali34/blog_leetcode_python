---
layout: post
title: "1091. Shortest Path in Binary Matrix"
date: 2026-03-11 00:00:00 -0700
categories: [leetcode, medium, graph, bfs]
tags: [leetcode, medium, grid, bfs, shortest-path]
permalink: /2026/03/11/medium-1091-shortest-path-in-binary-matrix/
---

# 1091. Shortest Path in Binary Matrix

## Problem Statement

You are given an `n x n` binary matrix `grid`.

- `grid[r][c] == 0` → open cell  
- `grid[r][c] == 1` → blocked cell

You start at the **top-left** cell `(0, 0)` and want to reach the **bottom-right** cell `(n - 1, n - 1)`.

You may move to any of the **8 neighboring cells** (horizontally, vertically, or diagonally) **that are open (0)**.

Return the **length of the shortest path** from `(0, 0)` to `(n - 1, n - 1)`, where the length is the **number of cells visited** along the path (including start and end). If no such path exists, return `-1`.

## Examples

**Example 1:**

```python
Input: grid = [
  [0,1],
  [1,0]
]
Output: 2
# Path: (0,0) → (1,1)
```

**Example 2:**

```python
Input: grid = [
  [0,0,0],
  [1,1,0],
  [1,1,0]
]
Output: 4
# One shortest path: (0,0) → (0,1) → (0,2) → (1,2) → (2,2)
```

**Example 3:**

```python
Input: grid = [
  [1,0],
  [0,0]
]
Output: -1
# Start is blocked → no path.
```

## Constraints

- `1 <= n <= 100`
- `grid[r][c]` is either `0` or `1`.

## Clarification Questions

1. **Diagonal moves**: Can we move diagonally?  
   **Assumption**: Yes — 8 directions (up, down, left, right, and 4 diagonals).
2. **Start/end blocked**: If `grid[0][0] == 1` or `grid[n-1][n-1] == 1`, is the answer `-1`?  
   **Assumption**: Yes — no valid path exists.
3. **Path length definition**: Length counts **cells**, including both start and end?  
   **Assumption**: Yes — a direct move `(0,0) → (1,1)` has length 2.
4. **In-place modification**: Can we mark visited cells directly in `grid`?  
   **Assumption**: Yes — common in LeetCode; otherwise use a separate `visited` matrix.

## Interview Deduction Process (20 minutes)

**Step 1: Abstraction (5 min)**  
Model this as a shortest-path problem on a **grid graph**:

- Nodes: cells `(r, c)` with `grid[r][c] == 0`.  
- Edges: valid moves between neighboring open cells (8 directions).  
- Edge weight: 1 for every move.

We need the shortest path from `(0,0)` to `(n-1,n-1)` in an **unweighted** graph.

**Step 2: Naive DFS (5 min)**  
We could try all paths (DFS/backtracking) and track the minimum length, but:

- Each cell has up to 8 neighbors.  
- Number of possible paths can explode: worst-case exponential in `n²`.  
- DFS does not guarantee we find the shortest path early.

Too slow and complex; not suitable for `n` up to 100.

**Step 3: BFS for unweighted shortest path (10 min)**  
For unweighted graphs, **BFS** is the standard way to find shortest path:

- Explore layer by layer from the start.  
- The first time we reach `(n-1,n-1)`, we have the shortest path length.  
- We maintain a queue of `(row, col, dist)` tuples.

We need to:

1. Early-return `-1` if start or end is blocked.  
2. Initialize queue with `(0, 0, 1)` when `grid[0][0] == 0`.  
3. Track visited cells (either a `visited` matrix or reusing `grid` by setting visited cells to 1).  
4. For each cell, explore its 8 neighbors; if they are inside bounds and open (`0`), push them into the queue with `dist + 1` and mark visited.

## Solution Approach

**Algorithm (BFS):**

1. Let `n = len(grid)`.  
2. If `grid[0][0] == 1` or `grid[n-1][n-1] == 1`, return `-1`.  
3. Maintain 8 directions:

   ```python
   directions = [
       (-1, -1), (-1, 0), (-1, 1),
       (0, -1),           (0, 1),
       (1, -1),  (1, 0),  (1, 1),
   ]
   ```

4. Use a queue for BFS, starting from `(0, 0, 1)` (distance 1).  
5. Mark `(0, 0)` as visited (e.g. set `grid[0][0] = 1`).  
6. While the queue is not empty:
   - Pop `(r, c, dist)`.  
   - If `(r, c)` is `(n-1, n-1)`, return `dist`.  
   - For each direction `(dr, dc)`, compute neighbor `(nr, nc)`.  
   - If `(nr, nc)` is in bounds and `grid[nr][nc] == 0`, push `(nr, nc, dist + 1)` and mark `grid[nr][nc] = 1` (visited).
7. If we exhaust the queue without reaching the target, return `-1`.

### Key Insights

1. **BFS for shortest path** — In unweighted graphs, BFS guarantees the shortest number of edges (here, cells) from start to target.  
2. **8-direction movement** — Just extend the standard 4-direction BFS with diagonals.  
3. **Visited marking** — Marking visited cells directly in `grid` (changing `0` to `1`) avoids an extra `visited` array and ensures we don’t revisit cells.

## Python Solution

### BFS (O(n²) time, O(n²) space)

```python
from collections import deque
from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)

        # If start or end is blocked, no path exists.
        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return -1

        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1),
        ]

        queue = deque([(0, 0, 1)])  # (row, col, distance)
        grid[0][0] = 1  # mark visited

        while queue:
            r, c, dist = queue.popleft()
            if r == n - 1 and c == n - 1:
                return dist

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                    grid[nr][nc] = 1
                    queue.append((nr, nc, dist + 1))

        return -1
```

## Algorithm Explanation

We treat each open cell as a node and edges as moves to any of the 8 neighboring open cells. We run BFS from `(0, 0)` with initial distance 1. The queue stores `(row, col, dist)` so that when we pop the target cell `(n-1, n-1)`, `dist` is the shortest path length. We mark visited cells by setting `grid[r][c] = 1` to avoid revisiting them. If the BFS finishes without reaching the bottom-right cell, there is no valid path and we return `-1`.

## Complexity Analysis

- **Time**: O(n²), since each cell is enqueued and processed at most once and we check up to 8 neighbors per cell.  
- **Space**: O(n²) in the worst case for the BFS queue (when many cells are reachable).

## Edge Cases

- **Blocked start or end** — Immediately return `-1`.  
- **Single cell grid**:
  - `[[0]]` → answer is 1 (start is end).  
  - `[[1]]` → answer is -1 (blocked).
- **All zeros** — BFS explores the whole grid but still runs in O(n²).

## Common Mistakes

- **Forgetting diagonal moves** — Using only 4 directions (up, down, left, right) instead of 8 changes the problem.  
- **Not counting cells correctly** — Path length is number of cells visited, so we start distance at 1, not 0.  
- **Missing start/end check** — If either is blocked, BFS will still run unless we short-circuit; problem requires -1 immediately.

## Related Problems

- [LC 994: Rotting Oranges](https://leetcode.com/problems/rotting-oranges/) — Multi-source BFS on a grid.  
- [LC 542: 01 Matrix](https://leetcode.com/problems/01-matrix/) — BFS to compute distance to nearest zero.  
- [LC 286: Walls and Gates](https://leetcode.com/problems/walls-and-gates/) — Fill distances to the nearest gate.  
- [LC 127: Word Ladder](https://leetcode.com/problems/word-ladder/) — BFS for shortest path in an unweighted graph.

