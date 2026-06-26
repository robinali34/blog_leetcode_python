---
layout: post
title: "Algorithm Templates: Graph"
date: 2025-10-29 00:00:00 -0700
categories: leetcode templates graph
permalink: /posts/2025-10-29-leetcode-templates-graph/
tags: [leetcode, templates, graph]
---

{% raw %}
Graph algorithms are among the most versatile tools in competitive programming and coding interviews. A graph is simply a collection of nodes (vertices) connected by edges, and nearly every "network," "grid," or "relationship" problem maps onto one. This page provides production-ready Python templates for the most common graph patterns — from basic traversal to advanced connectivity — so you can focus on modeling the problem rather than re-deriving algorithms from scratch. All templates are 0-indexed unless noted.

> **New to Graphs?** A graph consists of **nodes** (things) connected by **edges** (relationships between things). Most graph problems on LeetCode reduce to one of three categories: **traversal** (BFS/DFS — explore or find shortest paths), **shortest paths** with weights (Dijkstra, Bellman-Ford), or **connectivity / ordering** (Union-Find, Topological Sort). If you can identify which category your problem falls into, you're halfway to the solution.

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 370" style="max-width:720px;width:100%;height:auto;display:block;margin:1.5em auto;">
  <defs>
    <marker id="ah" markerWidth="10" markerHeight="7" refX="10" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#B8B5B0"/>
    </marker>
  </defs>
  <!-- Start node -->
  <rect x="260" y="10" width="200" height="44" rx="8" fill="#E8E3D8" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="360" y="38" text-anchor="middle" font-family="system-ui,sans-serif" font-size="14" fill="#5A5752" font-weight="bold">Graph Problem?</text>
  <!-- Level 1 branches -->
  <line x1="300" y1="54" x2="160" y2="100" stroke="#B8B5B0" stroke-width="1.5" marker-end="url(#ah)"/>
  <line x1="360" y1="54" x2="360" y2="100" stroke="#B8B5B0" stroke-width="1.5" marker-end="url(#ah)"/>
  <line x1="420" y1="54" x2="520" y2="100" stroke="#B8B5B0" stroke-width="1.5" marker-end="url(#ah)"/>
  <!-- Question nodes -->
  <rect x="50" y="100" width="220" height="40" rx="8" fill="#D4D8D0" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="160" y="125" text-anchor="middle" font-family="system-ui,sans-serif" font-size="12" fill="#5A5752">Unweighted edges?</text>
  <rect x="260" y="100" width="200" height="40" rx="8" fill="#D4D8D0" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="360" y="125" text-anchor="middle" font-family="system-ui,sans-serif" font-size="12" fill="#5A5752">Ordering with dependencies?</text>
  <rect x="470" y="100" width="200" height="40" rx="8" fill="#D4D8D0" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="570" y="125" text-anchor="middle" font-family="system-ui,sans-serif" font-size="12" fill="#5A5752">Connected components?</text>
  <!-- Arrows to answers -->
  <line x1="160" y1="140" x2="160" y2="186" stroke="#B8B5B0" stroke-width="1.5" marker-end="url(#ah)"/>
  <line x1="320" y1="140" x2="280" y2="186" stroke="#B8B5B0" stroke-width="1.5" marker-end="url(#ah)"/>
  <line x1="400" y1="140" x2="440" y2="186" stroke="#B8B5B0" stroke-width="1.5" marker-end="url(#ah)"/>
  <line x1="570" y1="140" x2="570" y2="186" stroke="#B8B5B0" stroke-width="1.5" marker-end="url(#ah)"/>
  <!-- Answer nodes row 1 -->
  <rect x="80" y="190" width="160" height="40" rx="8" fill="#E8D5D0" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="160" y="215" text-anchor="middle" font-family="system-ui,sans-serif" font-size="13" fill="#5A5752" font-weight="bold">BFS</text>
  <rect x="200" y="190" width="160" height="40" rx="8" fill="#E8D5D0" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="280" y="215" text-anchor="middle" font-family="system-ui,sans-serif" font-size="13" fill="#5A5752" font-weight="bold">Topological Sort</text>
  <rect x="490" y="190" width="160" height="40" rx="8" fill="#E8D5D0" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="570" y="215" text-anchor="middle" font-family="system-ui,sans-serif" font-size="13" fill="#5A5752" font-weight="bold">DSU or DFS</text>
  <!-- Weighted branch from start -->
  <line x1="360" y1="140" x2="360" y2="252" stroke="#B8B5B0" stroke-width="1.5" marker-end="url(#ah)"/>
  <rect x="260" y="256" width="200" height="40" rx="8" fill="#D4D8E0" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="360" y="281" text-anchor="middle" font-family="system-ui,sans-serif" font-size="12" fill="#5A5752">Weighted edges?</text>
  <!-- Weighted sub-branches -->
  <line x1="310" y1="296" x2="220" y2="326" stroke="#B8B5B0" stroke-width="1.5" marker-end="url(#ah)"/>
  <line x1="410" y1="296" x2="500" y2="326" stroke="#B8B5B0" stroke-width="1.5" marker-end="url(#ah)"/>
  <rect x="100" y="320" width="240" height="40" rx="8" fill="#E8D5D0" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="220" y="345" text-anchor="middle" font-family="system-ui,sans-serif" font-size="13" fill="#5A5752" font-weight="bold">Dijkstra</text>
  <text x="220" y="355" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10" fill="#5A5752">(non-negative)</text>
  <rect x="380" y="320" width="240" height="40" rx="8" fill="#E8D5D0" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="500" y="345" text-anchor="middle" font-family="system-ui,sans-serif" font-size="13" fill="#5A5752" font-weight="bold">Bellman-Ford</text>
  <text x="500" y="355" text-anchor="middle" font-family="system-ui,sans-serif" font-size="10" fill="#5A5752">(negative allowed)</text>
  <!-- Answer node for topo -->
  <rect x="360" y="190" width="120" height="40" rx="8" fill="#E8D5D0" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="420" y="210" text-anchor="middle" font-family="system-ui,sans-serif" font-size="11" fill="#5A5752">↓ weighted?</text>
  <text x="420" y="224" text-anchor="middle" font-family="system-ui,sans-serif" font-size="11" fill="#5A5752">see below</text>
</svg>

## Contents

- [BFS (unweighted)](#bfs-unweighted)
- [Multi-source BFS](#multi-source-bfs)
- [BFS with state (bitmask)](#bfs-with-state-bitmask)
- [Topological sort (Kahn)](#topological-sort-kahn)
- [Topological sort (DFS)](#topological-sort-dfs)
- [Dijkstra](#dijkstra)
- [0-1 BFS](#0-1-bfs)
- [Bellman-Ford (k edges)](#bellman-ford-k-edges)
- [Tarjan (SCC / bridges)](#tarjan-scc--bridges)
- [DSU](#dsu)

---

## BFS (unweighted)

**When to use:** "shortest path" or "minimum steps" on a grid or unweighted graph; "nearest exit"; "level-order traversal."

Grid: 4-directional. Use for shortest path when all edges have weight 1.

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
|----|--------|------|
| 200 | Number of Islands | [Link](https://leetcode.com/problems/number-of-islands/) |
| 542 | 01 Matrix | [Link](https://leetcode.com/problems/01-matrix/) |

---

## Multi-source BFS

**When to use:** "distance from nearest X"; "spread from multiple starting points simultaneously"; "rotting oranges" or "fire spreading" patterns.

Start from multiple nodes (distance 0). Same as BFS with initial queue containing all sources.

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
|----|--------|------|
| 994 | Rotting Oranges | [Link](https://leetcode.com/problems/rotting-oranges/) |
| 286 | Walls and Gates | [Link](https://leetcode.com/problems/walls-and-gates/) |

---

## BFS with state (bitmask)

**When to use:** "visit all nodes/keys"; "shortest path visiting a subset"; state changes at each step (e.g., collecting keys unlocks doors).

State = (node, mask). Use when “visit all keys” or “visit all nodes” is part of the goal.

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
|----|--------|------|
| 847 | Shortest Path Visiting All Nodes | [Link](https://leetcode.com/problems/shortest-path-visiting-all-nodes/) |
| 864 | Shortest Path to Get All Keys | [Link](https://leetcode.com/problems/shortest-path-to-get-all-keys/) |

---

## Topological sort (Kahn)

**When to use:** "course prerequisites"; "build order"; "can I finish all tasks?"; finding a valid ordering of a DAG; cycle detection in directed graphs.

Indegree-based. Edge (u, v) means u before v. Returns order or empty if cycle.

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
|----|--------|------|
| 207 | Course Schedule | [Link](https://leetcode.com/problems/course-schedule/) |
| 210 | Course Schedule II | [Link](https://leetcode.com/problems/course-schedule-ii/) |
| 269 | Alien Dictionary | [Link](https://leetcode.com/problems/alien-dictionary/) |

---

## Topological sort (DFS)

**When to use:** Same as Kahn's, but preferred when you also need cycle detection via back-edges; "find all safe states"; problems where DFS post-order gives useful structure.

Three colors: 0 unvisited, 1 visiting, 2 done. Push to order when finishing. Reverse = topo order. Back edge (neighbor color 1) = cycle.

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
|----|--------|------|
| 802 | Find Eventual Safe States | [Link](https://leetcode.com/problems/find-eventual-safe-states/) |

---

## Dijkstra

**When to use:** "shortest path" with non-negative weights; "minimum cost to reach destination"; "network delay time"; any weighted graph where all weights ≥ 0.

Nonnegative weights. Adjacency list: g[u] = [(v, w), ...]. Returns distances from source s.

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
|----|--------|------|
| 743 | Network Delay Time | [Link](https://leetcode.com/problems/network-delay-time/) |
| 1976 | Number of Ways to Arrive at Destination | [Link](https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/) |
| 3112 | Minimum Time to Visit Disappearing Nodes | [Link](https://leetcode.com/problems/minimum-time-to-visit-disappearing-nodes/) |
| 3341 | Find Minimum Time to Reach Last Room I | [Link](https://leetcode.com/problems/find-minimum-time-to-reach-last-room-i/) |
| 3342 | Find Minimum Time to Reach Last Room II | [Link](https://leetcode.com/problems/find-minimum-time-to-reach-last-room-ii/) |

**Variant: nodes disappear at given times (3112).** Only relax edge \((u,v)\) if `dist[u] + w < disappear[v]`.

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

**Variant: grid with earliest-entry times (3341).** Moving costs 1, but you may need to wait to enter the next cell:
\[
\text{nextTime} = \max(\text{curTime},\ \text{open}[ni][nj]) + 1
\]

```python
import heapq


def dijkstra_grid_open(open: list[list[int]]) -> int:
    n, m = len(open), len(open[0])
    INF = 10**18
    dist = [[INF] * m for _ in range(n)]
    dist[0][0] = 0
    pq = [(0, 0, 0)]  # (time, i, j)
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    while pq:
        t, i, j = heapq.heappop(pq)
        if t != dist[i][j]:
            continue
        if i == n - 1 and j == m - 1:
            return t
        for di, dj in dirs:
            ni, nj = i + di, j + dj
            if ni < 0 or ni >= n or nj < 0 or nj >= m:
                continue
            nt = max(t, open[ni][nj]) + 1
            if nt < dist[ni][nj]:
                dist[ni][nj] = nt
                heapq.heappush(pq, (nt, ni, nj))
    return dist[n - 1][m - 1]
```

---

## 0-1 BFS

**When to use:** Edge weights are only 0 or 1; "minimum flips/changes to reach target"; grid problems where some moves are free and others cost 1.

Weights 0 or 1. Deque: push front for 0, back for 1. O(V + E).

```python
from collections import deque


def bfs01(n: int, g: list[list[tuple[int, int]]], s: int) -> list[int]:
    dist = [10**9] * n
    dist[s] = 0
    dq = deque([s])
    while dq:
        u = dq.popleft()
        for v, w in g[u]:
            nd = dist[u] + w
            if nd < dist[v]:
                dist[v] = nd
                if w == 0:
                    dq.appendleft(v)
                else:
                    dq.append(v)
    return dist
```

---

## Bellman-Ford (k edges)

**When to use:** "cheapest flight within K stops"; shortest path with a constraint on number of edges; negative edge weights allowed; detecting negative cycles.

Relax all edges up to k times. Use when path length (number of edges) is limited.

```python
def bellman_ford_k(
    n: int, edges: list[tuple[int, int, int]], src: int, k: int
) -> list[int]:
    INF = 10**18
    dist = [INF] * n
    dist[src] = 0
    for _ in range(k + 1):
        ndist = dist[:]
        for u, v, w in edges:
            if dist[u] != INF and dist[u] + w < ndist[v]:
                ndist[v] = dist[u] + w
        dist = ndist
    return dist
```

| ID | Title | Link |
|----|--------|------|
| 787 | Cheapest Flights Within K Stops | [Link](https://leetcode.com/problems/cheapest-flights-within-k-stops/) |

---

## Tarjan (SCC / bridges)

**When to use:** "critical connections"; "articulation points"; "strongly connected components"; finding bridges whose removal disconnects the graph.

SCC: same low-link = same component. Bridges: edge (u,v) is bridge iff low[v] > tin[u].

```python
class Tarjan:
    def __init__(self, n: int):
        self.n = n
        self.timer = 0
        self.g = [[] for _ in range(n)]
        self.tin = [-1] * n
        self.low = [0] * n
        self.comp = [-1] * n
        self.st: list[int] = []
        self.in_stack = [False] * n
        self.ncomp = 0

    def add(self, u: int, v: int) -> None:
        self.g[u].append(v)

    def dfs(self, u: int) -> None:
        self.tin[u] = self.low[u] = self.timer
        self.timer += 1
        self.st.append(u)
        self.in_stack[u] = True
        for v in self.g[u]:
            if self.tin[v] == -1:
                self.dfs(v)
                self.low[u] = min(self.low[u], self.low[v])
            elif self.in_stack[v]:
                self.low[u] = min(self.low[u], self.tin[v])
        if self.low[u] == self.tin[u]:
            while True:
                v = self.st.pop()
                self.in_stack[v] = False
                self.comp[v] = self.ncomp
                if v == u:
                    break
            self.ncomp += 1

    def run(self) -> int:
        for i in range(self.n):
            if self.tin[i] == -1:
                self.dfs(i)
        return self.ncomp


# Bridges: during dfs, if low[v] > tin[u] then (u, v) is a bridge
def bridges(n: int, g: list[list[int]]) -> list[tuple[int, int]]:
    timer = 0
    tin = [-1] * n
    low = [0] * n
    out: list[tuple[int, int]] = []

    def dfs(u: int, p: int) -> None:
        nonlocal timer
        tin[u] = low[u] = timer
        timer += 1
        for v in g[u]:
            if tin[v] == -1:
                dfs(v, u)
                low[u] = min(low[u], low[v])
                if low[v] > tin[u]:
                    out.append((u, v))
            elif v != p:
                low[u] = min(low[u], tin[v])

    for i in range(n):
        if tin[i] == -1:
            dfs(i, -1)
    return out
```

| ID | Title | Link |
|----|--------|------|
| 1192 | Critical Connections in a Network | [Link](https://leetcode.com/problems/critical-connections-in-a-network/) |

---

## DSU

**When to use:** "number of connected components"; "are two nodes in the same group?"; "redundant connection" (cycle detection in undirected graph); dynamic connectivity as edges are added.

Path compression + rank. See [Data Structures & Core Algorithms](/posts/2025-10-29-leetcode-templates-data-structures/#union-find-dsu) for full template.

| ID | Title | Link | Solution |
|----|--------|------|----------|
| 684 | Redundant Connection | [Link](https://leetcode.com/problems/redundant-connection/) | - |
| 721 | Accounts Merge | [Link](https://leetcode.com/problems/accounts-merge/) | - |
| 323 | Number of Connected Components | [Link](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/) | - |
| 399 | Evaluate Division | [Link](https://leetcode.com/problems/evaluate-division/) | - |
| 1202 | Smallest String With Swaps | [Link](https://leetcode.com/problems/smallest-string-with-swaps/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2026/03/09/medium-1202-smallest-string-with-swaps/) |
| 1319 | Number of Operations to Make Network Connected | [Link](https://leetcode.com/problems/number-of-operations-to-make-network-connected/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2026/03/10/medium-1319-number-of-operations-to-make-network-connected/) |
| 1584 | Min Cost to Connect All Points | [Link](https://leetcode.com/problems/min-cost-to-connect-all-points/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2026/03/08/medium-1584-min-cost-to-connect-all-points/) |
| 261 | Graph Valid Tree | [Link](https://leetcode.com/problems/graph-valid-tree/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2026/04/01/medium-261-graph-valid-tree/) |

---

## Algorithm Summary

| Algorithm | When to Use | Time | Space |
|---|---|---|---|
| BFS | Shortest path, unweighted | O(V+E) | O(V) |
| Dijkstra | Shortest path, non-negative weights | O((V+E) log V) | O(V) |
| Bellman-Ford | Shortest path, negative weights, k edges | O(VE) | O(V) |
| Topological Sort | DAG ordering, prerequisites | O(V+E) | O(V) |
| DSU (Union-Find) | Connected components, cycle detection | O(α(n)) per op | O(V) |
| Tarjan | SCC, bridges, articulation points | O(V+E) | O(V) |

---

## More templates

- **Beginner's Guide:** [LeetCode Beginner's Guide](/2026/06/25/leetcode-beginners-guide/)
- **Data structures (DSU, segment tree, etc.):** [Data Structures & Core Algorithms](/posts/2025-10-29-leetcode-templates-data-structures/)
- **Binary search, rotated array, 2D:** [Search](/posts/2026-01-20-leetcode-templates-search/)
- **Master index:** [Categories & Templates](/posts/2025-10-29-leetcode-categories-and-templates/)
{% endraw %}
