---
layout: post
title: "[Hard] 317. Shortest Distance from All Buildings"
date: 2025-09-24 19:00:00 -0000
categories: python shortest-distance buildings problem-solving
---

# [Hard] 317. Shortest Distance from All Buildings

<!-- Fixed Liquid syntax error -->

This is a graph traversal problem that requires finding the optimal location to build a new building such that the total distance to all existing buildings is minimized. The key insight is using BFS from each building to calculate distances and finding the spot with minimum total distance.

## Problem Description

Given a 2D grid where:
- `0` represents empty land
- `1` represents a building  
- `2` represents an obstacle

Find the shortest distance from all buildings to a single empty land cell. Return -1 if it's impossible.

### Examples

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

### Constraints
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 50
- grid[i][j] is either 0, 1, or 2
- There will be at least one building in the grid

## Approach

There are three main approaches to solve this problem:

1. **BFS from Each Empty Land**: For each empty land, BFS to all buildings
2. **BFS from Each Building**: For each building, BFS to all empty lands and accumulate distances
3. **Optimized BFS with Grid Modification**: Use grid values to track reachability

## Solution 1: BFS from Each Empty Land

**Time Complexity:** O(m²n²) - For each empty land, BFS to all buildings  
**Space Complexity:** O(mn) - For visited array and queue

```python
from collections import deque

class Solution:
    def shortestDistance(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        totalHouses = 0
        for row in grid:
            for cell in row:
                if cell == 1:
                    totalHouses += 1

        minDistance = float('inf')
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    result = self.bfs(grid, r, c, totalHouses)
                    minDistance = min(minDistance, result)

        return -1 if minDistance == float('inf') else minDistance

    def bfs(self, grid: list[list[int]], startRow: int, startCol: int, totalHouses: int) -> int:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        rows = len(grid)
        cols = len(grid[0])

        distanceSum = 0
        housesReached = 0
        steps = 0

        q = deque([(startRow, startCol)])
        visited = [[False] * cols for _ in range(rows)]
        visited[startRow][startCol] = True

        while q and housesReached != totalHouses:
            levelSize = len(q)

            for _ in range(levelSize):
                r, c = q.popleft()

                if grid[r][c] == 1:
                    distanceSum += steps
                    housesReached += 1
                    continue

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if (0 <= nr < rows and 0 <= nc < cols and 
                        not visited[nr][nc] and grid[nr][nc] != 2):
                        visited[nr][nc] = True
                        q.append((nr, nc))
            steps += 1

        if housesReached != totalHouses:
            for r in range(rows):
                for c in range(cols):
                    if grid[r][c] == 0 and visited[r][c]:
                        grid[r][c] = 2  # Mark as unreachable
            return float('inf')

        return distanceSum
```

## Solution 2: BFS from Each Building

**Time Complexity:** O(m²n²) - For each building, BFS to all empty lands  
**Space Complexity:** O(mn) - For distance tracking and visited array

```python
from collections import deque

class Solution:
    def shortestDistance(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        minDistance = float('inf')
        totalHouses = 0
        # distances[row][col] = [totalDistance, housesReached]
        distances = [[[0, 0] for _ in range(cols)] for _ in range(rows)]
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    totalHouses += 1
                    self.bfs(grid, distances, row, col)
        
        for row in range(rows):
            for col in range(cols):
                if distances[row][col][1] == totalHouses:
                    minDistance = min(minDistance, distances[row][col][0])
        
        return -1 if minDistance == float('inf') else minDistance

    def bfs(self, grid: list[list[int]], distances: list[list[list[int]]], 
            startRow: int, startCol: int) -> None:
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        rows, cols = len(grid), len(grid[0])
        q = deque([(startRow, startCol)])
        vis = [[False] * cols for _ in range(rows)]
        vis[startRow][startCol] = True
        steps = 0
        
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                if grid[r][c] == 0:
                    distances[r][c][0] += steps
                    distances[r][c][1] += 1
                for dr, dc in dirs:
                    nextRow = r + dr
                    nextCol = c + dc
                    if (0 <= nextRow < rows and 0 <= nextCol < cols and
                        not vis[nextRow][nextCol] and grid[nextRow][nextCol] == 0):
                        vis[nextRow][nextCol] = True
                        q.append((nextRow, nextCol))
            steps += 1
```

## Solution 3: Optimized BFS with Grid Modification

**Time Complexity:** O(m²n²) - For each building, BFS to all reachable empty lands  
**Space Complexity:** O(mn) - For total distance tracking

```python
from collections import deque

class Solution:
    def shortestDistance(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        emptyLandValue = 0
        minDist = float('inf')
        total = [[0] * cols for _ in range(rows)]
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    minDist = float('inf')
                    q = deque([(row, col)])
                    steps = 0
                    while q:
                        steps += 1
                        for _ in range(len(q)):
                            r, c = q.popleft()
                            for dr, dc in dirs:
                                nextRow = r + dr
                                nextCol = c + dc
                                if (0 <= nextRow < rows and 0 <= nextCol < cols and
                                    grid[nextRow][nextCol] == emptyLandValue):
                                    grid[nextRow][nextCol] -= 1
                                    total[nextRow][nextCol] += steps
                                    q.append((nextRow, nextCol))
                                    minDist = min(minDist, total[nextRow][nextCol])
                    emptyLandValue -= 1
        
        return -1 if minDist == float('inf') else minDist
```

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

## Key Insights

1. **BFS Level Processing**: Process each level of BFS to calculate distances correctly
2. **Reachability Check**: Ensure all buildings can reach the chosen empty land
3. **Distance Accumulation**: Sum distances from all buildings to each empty land
4. **Grid Optimization**: Use grid modification to track reachability efficiently

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
