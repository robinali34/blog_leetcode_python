---
layout: post
title: "[Medium] 1197. Minimum Knight Moves"
date: 2026-03-19 00:00:00 -0700
categories: [leetcode, medium, bfs]
tags: [leetcode, medium, bfs, chess, shortest-path]
permalink: /2026/03/19/medium-1197-minimum-knight-moves/
---

# [Medium] 1197. Minimum Knight Moves

On an infinite chessboard, a knight starts at `(0, 0)`. Return the **minimum number of moves** to reach `(x, y)`.

Knight moves: 8 “L” shapes (±2, ±1 permutations).

Constraints: `-300 ≤ x, y ≤ 300`.

## Why BFS?

Unweighted shortest path on a graph where each cell connects to 8 knight neighbors → **BFS**.

## Symmetry

Fold to the first quadrant: `x, y = abs(x), abs(y)`. Knight moves are symmetric across axes.

## Why allow `nx >= -1` and `ny >= -1`?

Small targets like `(1, 0)` may require briefly stepping into negative coordinates. After folding, allowing down to `-1` (not further) is enough for correctness near the origin.

## Python solution

```python
from collections import deque


class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        x, y = abs(x), abs(y)
        dirs = (
            (2, 1), (1, 2), (-1, 2), (-2, 1),
            (-2, -1), (-1, -2), (1, -2), (2, -1),
        )
        q = deque([(0, 0)])
        vis = {(0, 0): 0}

        while q:
            cx, cy = q.popleft()
            steps = vis[(cx, cy)]
            if cx == x and cy == y:
                return steps
            for dx, dy in dirs:
                nx, ny = cx + dx, cy + dy
                if nx >= -1 and ny >= -1 and (nx, ny) not in vis:
                    vis[(nx, ny)] = steps + 1
                    q.append((nx, ny))
        return -1
```

**Time:** O(|x| · |y|) in the explored region  
**Space:** O(|x| · |y|) for `vis`

### Alternative: fixed offset grid

Because `|x|, |y| ≤ 300`, you can use a 2D array with offset `(nx + 302, ny + 302)` instead of a hash map — often faster in Python.

## Common mistakes

- Not using `abs(x)`, `abs(y)` — explores ~4× the area
- Restricting to `nx >= 0, ny >= 0` — misses valid paths near the origin

## Key takeaways

- **Minimum moves with special piece rules** → BFS
- **Symmetry pruning** + **`-1` boundary** are the subtle details

## Related & templates

- [433. Minimum Genetic Mutation](https://leetcode.com/problems/minimum-genetic-mutation/)
- [1091. Shortest Path in Binary Matrix](https://leetcode.com/problems/shortest-path-in-binary-matrix/)
- [BFS](/posts/2025-11-24-leetcode-templates-bfs/)
