---
layout: post
title: "[Hard] 317. Shortest Distance from All Buildings"
date: 2025-09-24 19:00:00 -0000
categories: leetcode algorithm bfs graph data-structures matrix shortest-path hard cpp shortest-distance buildings problem-solving
---

{% raw %}
<!-- Fixed Liquid syntax error -->

This is a graph traversal problem that requires finding the optimal location to build a new building such that the total distance to all existing buildings is minimized. The key insight is using BFS from each building to calculate distances and finding the spot with minimum total distance.

Given a 2D grid where:
- `0` represents empty land
- `1` represents a building  
- `2` represents an obstacle

Find the shortest distance from all buildings to a single empty land cell. Return -1 if it's impossible.

## Examples
**Example 1:**
```
Input: grid = [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]
Output: 7
Explanation: The optimal location is (1,2) with total distance 7.
```

**Example 2:**
```
Input: grid = [[1,0]]
Output: 1
```

**Example 3:**
```
Input: grid = [[1]]
Output: -1
```

## Constraints
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 50
- grid[i][j] is either 0, 1, or 2
- There will be at least one building in the grid

## Thinking Process

There are three main approaches to solve this problem:

1. **BFS from Each Empty Land**: For each empty land, BFS to all buildings
2. **BFS from Each Building**: For each building, BFS to all empty lands and accumulate distances
3. **Optimized BFS with Grid Modification**: Use grid values to track reachability

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 280 135" style="max-width:100%;height:auto;display:block;margin:1.5em auto;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif">
<text x="50%" y="18" text-anchor="middle" font-size="13" font-weight="600" fill="#5A5752">Graph BFS layers</text>

  <circle cx="60" cy="70" r="16" fill="#D4D8E0" stroke="#8B8680"/><text x="60" y="74" text-anchor="middle" font-size="11">S</text>
  <circle cx="140" cy="45" r="14" fill="#E8E3D8" stroke="#B8B5B0"/><text x="140" y="49" text-anchor="middle" font-size="10">a</text>
  <circle cx="140" cy="95" r="14" fill="#E8E3D8" stroke="#B8B5B0"/><text x="140" y="99" text-anchor="middle" font-size="10">b</text>
  <circle cx="210" cy="70" r="14" fill="#E8D5D0" stroke="#B8A5A0"/><text x="210" y="74" text-anchor="middle" font-size="10">t</text>
  <line x1="74" y1="65" x2="126" y2="50" stroke="#9A9792" stroke-width="1.5"/>
  <line x1="74" y1="75" x2="126" y2="95" stroke="#9A9792" stroke-width="1.5"/>
  <line x1="154" y1="50" x2="196" y2="65" stroke="#9A9792" stroke-width="1.5"/>
  <text x="140" y="125" text-anchor="middle" font-size="11" fill="#6B6560">BFS: expand by layers (queue)</text>

</svg>

## Common Approaches

Typical techniques for this pattern:

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| **Queue BFS** *(this problem)* | O(n) | O(n) | Shortest path in unweighted graphs |
| Multi-source BFS | O(n) | O(n) | Start from all sources simultaneously |
| 0-1 BFS / deque | O(n) | O(n) | Weights 0 or 1 |
| Level-order BFS | O(n) | O(w) | Process by depth/layer |

## Solution

**Time Complexity:** O(m²n²) - For each empty land, BFS to all buildings  
**Space Complexity:** O(mn) - For visited array and queue

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

### Solution Explanation

**Approach:** Queue BFS (this problem)

**Key idea:** There are three main approaches to solve this problem:

**How the code works:**
1. **BFS from Each Empty Land**: For each empty land, BFS to all buildings
2. **BFS from Each Building**: For each building, BFS to all empty lands and accumulate distances
3. **Optimized BFS with Grid Modification**: Use grid values to track reachability

**Walkthrough** — input `grid = [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]`, expected output `7`:

The optimal location is (1,2) with total distance 7.
## Step-by-Step Example

Let's trace through Solution 2 with grid = `[[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]`:

**Step 1:** Count total houses = 3

**Step 2:** BFS from each building
- Building at (0,0): Updates distances to all reachable empty lands
- Building at (0,4): Updates distances to all reachable empty lands  
- Building at (2,2): Updates distances to all reachable empty lands

**Step 3:** Check each empty land
- Only empty lands reachable by all 3 buildings are considered
- Find minimum total distance among valid positions

**Result:** Position (1,2) with total distance 7

## Approach Comparison

| Approach | Pros | Cons |
|----------|------|------|
| **Solution 1** | Simple logic, easy to understand | Less efficient, modifies original grid |
| **Solution 2** | Clean separation, tracks reachability | Uses extra space for distance tracking |
| **Solution 3** | Most efficient, reuses grid space | Complex logic, harder to debug |

## Common Mistakes

- **Incorrect Distance Calculation**: Not using level-by-level BFS
- **Reachability Issues**: Not checking if all buildings can reach empty land
- **Grid Modification**: Modifying original grid without proper restoration
- **Boundary Conditions**: Not handling edge cases properly

---

## References

- [LC 317: Shortest Distance from All Buildings on LeetCode](https://www.leetcode.com/problems/shortest-distance-from-all-buildings/)
- [LeetCode Discuss — LC 317: Shortest Distance from All Buildings](https://www.leetcode.com/problems/shortest-distance-from-all-buildings/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/shortest-distance-from-all-buildings/editorial/) *(may require premium)*

## Key Takeaways

1. **BFS Level Processing**: Process each level of BFS to calculate distances correctly
2. **Reachability Check**: Ensure all buildings can reach the chosen empty land
3. **Distance Accumulation**: Sum distances from all buildings to each empty land
4. **Grid Optimization**: Use grid modification to track reachability efficiently

{% endraw %}
