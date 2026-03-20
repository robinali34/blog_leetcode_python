---
layout: post
title: "[Hard] 317. Shortest Distance from All Buildings"
date: 2025-09-24 19:00:00 -0000
categories: python shortest-distance buildings problem-solving
---

# [Hard] 317. Shortest Distance from All Buildings

The previous Python snippets were malformed and had indentation/logic issues.  
This version uses the standard correct approach: **BFS from each building** and accumulate distances to empty cells.

## Problem Description

Given a 2D grid where:

- `0` = empty land
- `1` = building
- `2` = obstacle

Find an empty land cell such that the sum of shortest distances from this cell to **all buildings** is minimum. Return that minimum sum, or `-1` if no such cell exists.

### Examples

**Example 1**

```text
Input: grid = [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]
Output: 7
```

**Example 2**

```text
Input: grid = [[1,0]]
Output: 1
```

**Example 3**

```text
Input: grid = [[1]]
Output: -1
```

### Constraints

- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 50`
- `grid[i][j]` is `0`, `1`, or `2`
- At least one building exists

## Approaches

### Approach 1: BFS from each empty land (brute force)

For every `0` cell:
- Run BFS and compute shortest distance to all buildings.
- If it can reach all buildings, update minimum sum.

This is correct but expensive because we repeat BFS from many empty cells.

#### Python

```python
from collections import deque
from typing import List


class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        buildings = sum(cell == 1 for row in grid for cell in row)
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs_from_empty(sr: int, sc: int) -> int:
            q = deque([(sr, sc, 0)])
            visited = [[False] * cols for _ in range(rows)]
            visited[sr][sc] = True
            reached = 0
            dist_sum = 0

            while q:
                r, c, d = q.popleft()
                if grid[r][c] == 1:
                    reached += 1
                    dist_sum += d
                    continue

                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if not (0 <= nr < rows and 0 <= nc < cols):
                        continue
                    if visited[nr][nc] or grid[nr][nc] == 2:
                        continue
                    visited[nr][nc] = True
                    q.append((nr, nc, d + 1))

            return dist_sum if reached == buildings else float("inf")

        ans = float("inf")
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    ans = min(ans, bfs_from_empty(r, c))

        return -1 if ans == float("inf") else ans
```

**Time:** `O(E * m * n)` where `E` is #empty cells (worst `O((m*n)^2)`)  
**Space:** `O(m * n)` for BFS visited/queue

---

### Approach 2: BFS from each building (recommended)

Instead of starting from each empty cell, start BFS from each building and accumulate:

- `dist_sum[r][c]`: total distance from all buildings to empty cell `(r,c)`
- `reach_count[r][c]`: how many buildings can reach `(r,c)`

At the end, valid candidate cells are those with:
- `grid[r][c] == 0`
- `reach_count[r][c] == building_count`

Pick minimum `dist_sum`.

#### Python

```python
from collections import deque
from typing import List


class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dist_sum = [[0] * cols for _ in range(rows)]
        reach_count = [[0] * cols for _ in range(rows)]
        buildings = 0
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != 1:
                    continue

                buildings += 1
                visited = [[False] * cols for _ in range(rows)]
                visited[r][c] = True
                q = deque([(r, c, 0)])

                while q:
                    cr, cc, d = q.popleft()
                    for dr, dc in dirs:
                        nr, nc = cr + dr, cc + dc
                        if not (0 <= nr < rows and 0 <= nc < cols):
                            continue
                        if visited[nr][nc] or grid[nr][nc] != 0:
                            continue

                        visited[nr][nc] = True
                        dist_sum[nr][nc] += d + 1
                        reach_count[nr][nc] += 1
                        q.append((nr, nc, d + 1))

        ans = float("inf")
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0 and reach_count[r][c] == buildings:
                    ans = min(ans, dist_sum[r][c])
        return -1 if ans == float("inf") else ans
```

**Time:** `O(B * m * n)` where `B` is #buildings (worst `O((m*n)^2)`)  
**Space:** `O(m * n)` for `dist_sum`, `reach_count`, and BFS `visited`

---

### Approach 3: Optimized BFS with grid-state pruning

Same BFS-from-buildings idea, but avoid visiting cells that were not reachable by previous buildings.

Common trick:
- Maintain `empty_land_value` initially `0`
- For each building BFS, only visit cells with value `empty_land_value`
- Mark visited empty cells by decrementing grid value (e.g., `0 -> -1 -> -2 ...`)

This prunes impossible cells early and improves constants.

#### Python

```python
from collections import deque
from typing import List


class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        total = [[0] * cols for _ in range(rows)]
        empty_land_value = 0
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        min_dist = float("inf")

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != 1:
                    continue

                min_dist = float("inf")
                q = deque([(r, c)])
                steps = 0

                while q:
                    steps += 1
                    for _ in range(len(q)):
                        cr, cc = q.popleft()
                        for dr, dc in dirs:
                            nr, nc = cr + dr, cc + dc
                            if not (0 <= nr < rows and 0 <= nc < cols):
                                continue
                            if grid[nr][nc] != empty_land_value:
                                continue

                            grid[nr][nc] -= 1
                            total[nr][nc] += steps
                            min_dist = min(min_dist, total[nr][nc])
                            q.append((nr, nc))

                empty_land_value -= 1

        return -1 if min_dist == float("inf") else min_dist
```

**Time:** still worst-case `O(B * m * n)`  
**Space:** `O(m * n)` (or less auxiliary compared to approach 2)

## Runtime/Space Tradeoff

| Approach | Time | Space | Notes |
|---|---:|---:|---|
| BFS from each empty land | `O(E*m*n)` | `O(m*n)` | Easiest conceptually, often too slow |
| BFS from each building | `O(B*m*n)` | `O(m*n)` | Clean and standard accepted approach |
| BFS + grid-state pruning | `O(B*m*n)` | `O(m*n)` | Faster in practice due to pruning |

## Common Mistakes

- Running BFS through buildings/obstacles (should only expand into `0` cells).
- Not tracking how many buildings can reach each empty cell.
- Returning min distance for a cell not reachable by all buildings.
- Wrong BFS distance update (distance should increase per level/edge).

