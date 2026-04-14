---
layout: post
title: "3342. Find Minimum Time to Reach Last Room II"
date: 2026-02-10 00:00:00 -0700
categories: [leetcode, medium, graph, shortest-path, dijkstra, grid]
permalink: /2026/02/10/medium-3342-find-minimum-time-to-reach-last-room-ii/
tags: [leetcode, medium, graph, shortest-path, dijkstra, grid]
---

## Problem Statement

There is a dungeon with `n x m` rooms arranged as a grid.

You are given a 2D array `moveTime` of size `n x m`, where `moveTime[i][j]` represents the **minimum** time in seconds **after** which the room opens and can be moved to. You start from the room `(0, 0)` at time `t = 0` and can move to an **adjacent** room.

**Moving between adjacent rooms takes:**
*   **1 second** for the first move.
*   **2 seconds** for the second move.
*   **1 second** for the third move.
*   **2 seconds** for the fourth move.
*   ...and so on, alternating between 1 and 2 seconds.

Return the **minimum** time to reach the room `(n - 1, m - 1)`.

Two rooms are adjacent if they share a common wall (up/down/left/right).

## Examples

**Example 1**

```
Input: moveTime = [[0,4],[4,4]]
Output: 7
Explanation:
- At t=0, move to (1,0) (cost 1). Arrive at t=4 (wait for 4). Next move cost will be 2.
- At t=4, wait until t=4. Move to (1,0). Wait? No, arrive t=1 (cost) + max(0, 4) = 5?
  Let's trace carefully:
  - Start (0,0) at t=0.
  - Move to (0,1): moveTime[0][1]=4. Arrive at max(0, 4) + 1 = 5. Next cost 2.
  - Move to (1,1) from (0,1): moveTime[1][1]=4. Arrive max(5, 4) + 2 = 7.
  Alternatively:
  - Start (0,0) at t=0.
  - Move to (1,0): moveTime[1][0]=4. Arrive max(0, 4) + 1 = 5. Next cost 2.
  - Move to (1,1) from (1,0): moveTime[1][1]=4. Arrive max(5, 4) + 2 = 7.
```

**Example 2**

```
Input: moveTime = [[0,0,0,0],[0,0,0,0]]
Output: 6
Explanation:
- (0,0) -> (0,1): cost 1. Arrive t=1.
- (0,1) -> (0,2): cost 2. Arrive t=3.
- (0,2) -> (0,3): cost 1. Arrive t=4.
- (0,3) -> (1,3): cost 2. Arrive t=6.
```

**Example 3**

```
Input: moveTime = [[0,1],[1,2]]
Output: 4
```

## Constraints

- `2 <= n == moveTime.length <= 750`
- `2 <= m == moveTime[i].length <= 750`
- `0 <= moveTime[i][j] <= 10^9`

## Key Insight

This is a **shortest path problem** on a grid where the edge weights are dynamic but depend only on the *sequence* of moves (1, 2, 1, 2...).

Specifically, the cost of the $k$-th move is:
- $1$ if $k$ is odd (1st, 3rd, ...)
- $2$ if $k$ is even (2nd, 4th, ...)

This creates a state `(row, col, next_move_cost)`. Since the cost alternates between 1 and 2, `next_move_cost` is always either 1 or 2.

We can use **Dijkstra's Algorithm**. The state in the priority queue will be `{time, row, col, weight}`.
- `weight` is the cost to move *out* of the current cell to a neighbor.
- When moving from `(r, c)` to `(nr, nc)` with weight `w`:
  - `arrival_time = max(current_time, moveTime[nr][nc]) + w`
  - The next weight for `(nr, nc)` will be `3 - w` (swaps 1 $\to$ 2 and 2 $\to$ 1).

## Solution (Dijkstra)

{% raw %}
```python
import heapq

class Solution:
    def minTimeToReach(self, moveTime):
        n, m = len(moveTime), len(moveTime[0])
        
        INF = float('inf')
        dist = [[INF] * m for _ in range(n)]
        dist[0][0] = 0
        
        # (time, r, c, next_move_cost)
        pq = [(0, 0, 0, 1)]
        
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        while pq:
            t, r, c, w = heapq.heappop(pq)
            
            if t > dist[r][c]:
                continue
            
            if r == n - 1 and c == m - 1:
                return t
            
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                
                if nr < 0 or nr >= n or nc < 0 or nc >= m:
                    continue
                
                nt = max(t, moveTime[nr][nc]) + w
                
                if nt < dist[nr][nc]:
                    dist[nr][nc] = nt
                    heapq.heappush(pq, (nt, nr, nc, 3 - w))  # flip 1 ↔ 2
        
        return -1
```
{% endraw %}

## Complexity

- **Time**: $O(nm \log(nm))$
- **Space**: $O(nm)$

## Template Reference

- [Graph Templates: Dijkstra](/posts/2025-10-29-leetcode-templates-graph/#dijkstra)
