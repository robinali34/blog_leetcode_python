---
layout: post
title: "LeetCode Templates: Graph"
date: 2025-10-29 00:00:00 -0700
categories: leetcode templates graph
permalink: /posts/2025-10-29-leetcode-templates-graph/
tags: [leetcode, templates, graph]
---

{% raw %}
## Contents

- [BFS / Shortest Path](#bfs--shortest-path-unweighted)
- [Multi-source BFS](#multi-source-bfs-gridsgraphs)
- [BFS on Bitmask State](#bfs-on-bitmask-state-visit-all-keys)
- [Topological Sort (Kahn)](#topological-sort-kahn)
- [Dijkstra](#dijkstra-weights--0)
- [0-1 BFS](#0-1-bfs-weights-0-or-1)
- [Tarjan SCC / Bridges & Articulation](#tarjan-scc--bridges--articulation)

## BFS / Shortest Path (unweighted)

```python
from collections import deque

def bfs_grid(g: list[str], s: tuple[int, int], t: tuple[int, int]) -> int:
    m, n = len(g), len(g[0])
    q = deque([s])
    dist = [[-1] * n for _ in range(m)]
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    dist[s[0]][s[1]] = 0
    while q:
        x, y = q.popleft()
        if (x, y) == t:
            return dist[x][y]
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and g[nx][ny] != '#' and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))
    return -1
```

| ID | Title | Link |
|---|---|---|
| 200 | Number of Islands | [Number of Islands](https://leetcode.com/problems/number-of-islands/) |
| 417 | [Pacific Atlantic Water Flow](https://robinali34.github.io/blog_leetcode_python/posts/2025-10-19-medium-417-pacific-atlantic-water-flow/) | [Pacific Atlantic Water Flow](https://leetcode.com/problems/pacific-atlantic-water-flow/) |
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
            if 0 <= nx < m and 0 <= ny < n and g[nx][ny] != '#' and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                best = max(best, dist[nx][ny])
                q.append((nx, ny))
    return best
```

| ID | Title | Link |
|---|---|---|
| 994 | Rotting Oranges | https://leetcode.com/problems/rotting-oranges/ |
| 286 | Walls and Gates | https://leetcode.com/problems/walls-and-gates/ |

## BFS on Bitmask State (visit all keys)

```python
from collections import deque

def bfs_mask(g: list[list[int]], start: int) -> int:
    n = len(g)
    full = (1 << n) - 1
    q = deque([(start, 1 << start)])
    vis = [[False] * (1 << n) for _ in range(n)]
    vis[start][1 << start] = True
    d = 0
    while q:
        sz = len(q)
        for _ in range(sz):
            u, mask = q.popleft()
            if mask == full:
                return d
            for v in g[u]:
                m2 = mask | (1 << v)
                if not vis[v][m2]:
                    vis[v][m2] = True
                    q.append((v, m2))
        d += 1
    return -1
```

| ID | Title | Link |
|---|---|---|
| 864 | Shortest Path to Get All Keys | https://leetcode.com/problems/shortest-path-to-get-all-keys/ |
| 847 | Shortest Path Visiting All Nodes | https://leetcode.com/problems/shortest-path-visiting-all-nodes/ |

## Topological Sort (Kahn)

```python
from collections import deque

def topo_kahn(n: int, g: list[list[int]]) -> list[int]:
    indeg = [0] * n
    for u in range(n):
        for v in g[u]:
            indeg[v] += 1
    q = deque()
    for i in range(n):
        if indeg[i] == 0:
            q.append(i)
    order = []
    while q:
        u = q.popleft()
        order.append(u)
        for v in g[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    if len(order) != n:
        order.clear()
    return order
```

| ID | Title | Link |
|---|---|---|
| 207 | Course Schedule | https://leetcode.com/problems/course-schedule/ |
| 210 | Course Schedule II | https://leetcode.com/problems/course-schedule-ii/ |
| 269 | Alien Dictionary | https://leetcode.com/problems/alien-dictionary/ |

## Dijkstra (weights ≥ 0)

```python
import heapq

def dijkstra(n: int, g: list[list[tuple[int, int]]], s: int) -> list[int]:
    INF = 1 << 60
    dist = [INF] * n
    dist[s] = 0
    pq = [(0, s)]
    while pq:
        d, u = heapq.heappop(pq)
        if d != dist[u]:
            continue
        for v, w in g[u]:
            if dist[v] > d + w:
                dist[v] = d + w
                heapq.heappush(pq, (dist[v], v))
    return dist
```

| ID | Title | Link |
|---|---|---|
| 743 | Network Delay Time | https://leetcode.com/problems/network-delay-time/ |
| 1631 | Path With Minimum Effort | https://leetcode.com/problems/path-with-minimum-effort/ |

## 0-1 BFS (weights 0 or 1)

```python
from collections import deque

dq = deque([s])
dist = [10**9] * n
dist[s] = 0
while dq:
    u = dq.popleft()
    for v, w in g[u]:
        nd = dist[u] + w  # w in {0, 1}
        if nd < dist[v]:
            dist[v] = nd
            if w == 0:
                dq.appendleft(v)
            else:
                dq.append(v)
```

| ID | Title | Link |
|---|---|---|
| 1293 | Shortest Path in a Grid with Obstacles Elimination | https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/ |
| 847 | Shortest Path Visiting All Nodes | https://leetcode.com/problems/shortest-path-visiting-all-nodes/ |

## Tarjan SCC / Bridges & Articulation

```python
timer2 = 0
tin2 = []
low2 = []
bridges = []

def dfs_br(u: int, p: int, g: list[list[int]]):
    global timer2
    tin2[u] = low2[u] = timer2
    timer2 += 1
    child = 0
    is_ap = False
    for v in g[u]:
        if v != p:
            if tin2[v] == -1:
                child += 1
                dfs_br(v, u, g)
                low2[u] = min(low2[u], low2[v])
                if low2[v] > tin2[u]:
                    bridges.append((u, v))
                if p != -1 and low2[v] >= tin2[u]:
                    is_ap = True
            else:
                low2[u] = min(low2[u], tin2[v])
    if p == -1 and child > 1:
        is_ap = True
```

| ID | Title | Link |
|---|---|---|
| 1192 | Critical Connections in a Network | https://leetcode.com/problems/critical-connections-in-a-network/ |
{% endraw %}
