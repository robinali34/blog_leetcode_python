---
layout: post
title: "LeetCode Templates: Graph"
date: 2025-10-29 00:00:00 -0700
categories: [leetcode, templates, graph]
permalink: /posts/2025-10-29-leetcode-templates-graph/
tags: [leetcode, templates, graph]
---

## Contents

- [How to Analyze Graph Problems](#how-to-analyze-graph-problems)
- [BFS / Shortest Path](#bfs--shortest-path-unweighted)
- [Multi-source BFS](#multi-source-bfs-gridsgraphs)
- [BFS on Bitmask State](#bfs-on-bitmask-state-visit-all-keys)
- [Topological Sort (Kahn)](#topological-sort-kahn)
- [Dijkstra](#dijkstra-weights--0)
- [0-1 BFS](#0-1-bfs-weights-0-or-1)
- [Tarjan Bridges & Articulation](#tarjan-bridges--articulation)

## How to Analyze Graph Problems

1. **Graph type**
   - directed/undirected, weighted/unweighted, dense/sparse

2. **Goal type**
   - reachability, shortest path, ordering, components, critical edges

3. **Pick algorithm by edge weights**
   - unweighted -> BFS
   - weights 0/1 -> 0-1 BFS
   - nonnegative weights -> Dijkstra

4. **State design**
   - sometimes node alone is not enough (node + mask, node + extra resource)

## BFS / Shortest Path (unweighted)

```python
from collections import deque


def bfs_grid(g: list[str], s: tuple[int, int], t: tuple[int, int]) -> int:
    m, n = len(g), len(g[0])
    q = deque([s])
    dist = [[-1] * n for _ in range(m)]
    dist[s[0]][s[1]] = 0
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while q:
        x, y = q.popleft()
        if (x, y) == t:
            return dist[x][y]
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and g[nx][ny] != "#" and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))
    return -1
```

| ID | Title | Link |
|---|---|---|
| 200 | Number of Islands | [Number of Islands](https://leetcode.com/problems/number-of-islands/) |
| 417 | Pacific Atlantic Water Flow | [Pacific Atlantic Water Flow](https://leetcode.com/problems/pacific-atlantic-water-flow/) |
| 542 | 01 Matrix | [01 Matrix](https://leetcode.com/problems/01-matrix/) |

## Multi-source BFS (grids/graphs)

```python
from collections import deque


def multi_source_bfs(g: list[str], sources: list[tuple[int, int]]) -> int:
    m, n = len(g), len(g[0])
    q = deque()
    dist = [[-1] * n for _ in range(m)]

    for x, y in sources:
        dist[x][y] = 0
        q.append((x, y))

    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    best = 0
    while q:
        x, y = q.popleft()
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and g[nx][ny] != "#" and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                best = max(best, dist[nx][ny])
                q.append((nx, ny))
    return best
```

| ID | Title | Link |
|---|---|---|
| 994 | Rotting Oranges | [Rotting Oranges](https://leetcode.com/problems/rotting-oranges/) |
| 286 | Walls and Gates | [Walls and Gates](https://leetcode.com/problems/walls-and-gates/) |

## BFS on Bitmask State (visit all keys)

```python
from collections import deque


def bfs_mask(g: list[list[int]], start: int) -> int:
    n = len(g)
    full = (1 << n) - 1
    q = deque([(start, 1 << start, 0)])  # node, mask, distance
    seen = {(start, 1 << start)}

    while q:
        u, mask, d = q.popleft()
        if mask == full:
            return d
        for v in g[u]:
            m2 = mask | (1 << v)
            state = (v, m2)
            if state not in seen:
                seen.add(state)
                q.append((v, m2, d + 1))
    return -1
```

| ID | Title | Link |
|---|---|---|
| 864 | Shortest Path to Get All Keys | [Shortest Path to Get All Keys](https://leetcode.com/problems/shortest-path-to-get-all-keys/) |
| 847 | Shortest Path Visiting All Nodes | [Shortest Path Visiting All Nodes](https://leetcode.com/problems/shortest-path-visiting-all-nodes/) |

## Topological Sort (Kahn)

```python
from collections import deque


def topo_kahn(n: int, g: list[list[int]]) -> list[int]:
    indeg = [0] * n
    for u in range(n):
        for v in g[u]:
            indeg[v] += 1

    q = deque(i for i in range(n) if indeg[i] == 0)
    order = []
    while q:
        u = q.popleft()
        order.append(u)
        for v in g[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    return order if len(order) == n else []
```

| ID | Title | Link |
|---|---|---|
| 207 | Course Schedule | [Course Schedule](https://leetcode.com/problems/course-schedule/) |
| 210 | Course Schedule II | [Course Schedule II](https://leetcode.com/problems/course-schedule-ii/) |
| 269 | Alien Dictionary | [Alien Dictionary](https://leetcode.com/problems/alien-dictionary/) |

## Dijkstra (weights >= 0)

```python
import heapq


def dijkstra(n: int, g: list[list[tuple[int, int]]], s: int) -> list[int]:
    INF = 10**18
    dist = [INF] * n
    dist[s] = 0
    pq = [(0, s)]

    while pq:
        d, u = heapq.heappop(pq)
        if d != dist[u]:
            continue
        for v, w in g[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))
    return dist
```

| ID | Title | Link |
|---|---|---|
| 743 | Network Delay Time | [Network Delay Time](https://leetcode.com/problems/network-delay-time/) |
| 1631 | Path With Minimum Effort | [Path With Minimum Effort](https://leetcode.com/problems/path-with-minimum-effort/) |

## 0-1 BFS (weights 0 or 1)

```python
from collections import deque


def zero_one_bfs(n: int, g: list[list[tuple[int, int]]], s: int) -> list[int]:
    INF = 10**18
    dist = [INF] * n
    dist[s] = 0
    dq = deque([s])

    while dq:
        u = dq.popleft()
        for v, w in g[u]:  # w must be 0 or 1
            nd = dist[u] + w
            if nd < dist[v]:
                dist[v] = nd
                if w == 0:
                    dq.appendleft(v)
                else:
                    dq.append(v)
    return dist
```

| ID | Title | Link |
|---|---|---|
| 1368 | Minimum Cost to Make at Least One Valid Path in a Grid | [Minimum Cost to Make at Least One Valid Path in a Grid](https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/) |
| 2290 | Minimum Obstacle Removal to Reach Corner | [Minimum Obstacle Removal to Reach Corner](https://leetcode.com/problems/minimum-obstacle-removal-to-reach-corner/) |

## Tarjan Bridges & Articulation

```python
def find_bridges(n: int, g: list[list[int]]) -> list[tuple[int, int]]:
    tin = [-1] * n
    low = [-1] * n
    timer = 0
    bridges = []

    def dfs(u: int, p: int) -> None:
        nonlocal timer
        tin[u] = low[u] = timer
        timer += 1

        for v in g[u]:
            if v == p:
                continue
            if tin[v] != -1:
                low[u] = min(low[u], tin[v])
            else:
                dfs(v, u)
                low[u] = min(low[u], low[v])
                if low[v] > tin[u]:
                    bridges.append((u, v))

    for i in range(n):
        if tin[i] == -1:
            dfs(i, -1)
    return bridges
```

| ID | Title | Link |
|---|---|---|
| 1192 | Critical Connections in a Network | [Critical Connections in a Network](https://leetcode.com/problems/critical-connections-in-a-network/) |

