---
layout: post
title: "1319. Number of Operations to Make Network Connected"
date: 2026-03-10 00:00:00 -0700
categories: [leetcode, medium, graph, union-find]
tags: [leetcode, medium, graph, dsu, connected-components]
permalink: /2026/03/10/medium-1319-number-of-operations-to-make-network-connected/
---

# 1319. Number of Operations to Make Network Connected

## Problem Statement

There are `n` computers numbered from `0` to `n - 1` connected by ethernet cables. You are given `connections`, where `connections[i] = [a, b]` represents a cable connecting computers `a` and `b`.

You can **remove** any cable and **reconnect** it between two computers.

Return the **minimum number of operations** (cable moves) needed to make all computers connected. If it is impossible, return `-1`.

## Examples

**Example 1:**

```python
Input: n = 4, connections = [[0,1],[0,2],[1,2]]
Output: 1
# Graph:  0    3
#         |\   (isolated)
#         1-2
# One cable is redundant among 0,1,2. We can move it to connect 3.
# Answer = 1.
```

**Example 2:**

```python
Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]
Output: 2
# Multiple components; need 2 cable moves to connect all.
```

**Example 3:**

```python
Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2]]
Output: -1
# Only 4 edges; we need at least n-1 = 5 to connect 6 nodes. Impossible.
```

## Constraints

- `1 <= n <= 10^5`
- `1 <= connections.length <= min(n * (n - 1) / 2, 10^5)`
- No duplicate connections; no self-connections.

## Clarification Questions

1. **Cable move**: Remove one cable and place it between two currently disconnected computers?  
   **Assumption**: Yes — one move = one cable relocated.
2. **Goal**: One connected component (all computers reachable from any other)?  
   **Assumption**: Yes.
3. **Necessary condition**: To connect \(n\) nodes we need at least \(n - 1\) edges. So if `len(connections) < n - 1`, return `-1`.

## Interview Deduction Process (20 minutes)

**Step 1: Abstraction (5 min)**  
We want one connected component. To connect \(n\) nodes we need at least \(n - 1\) edges. So if there are fewer than \(n - 1\) cables, it’s impossible → return `-1`.

**Step 2: Count components (7 min)**  
If we have enough edges, extra edges can be “moved” to connect different components. So the answer is: **(number of connected components) − 1**. Each move connects two components; we need components − 1 moves to merge them all.

**Step 3: DSU (8 min)**  
Start with \(n\) components (each node alone). For each connection, unite the two endpoints. Each successful union decreases the component count by one. Final answer: `components - 1`. No need to build an adjacency list; DSU is enough.

## Solution Approach

**Necessary condition:** If `len(connections) < n - 1`, we don’t have enough cables to span all nodes → return `-1`.

**DSU:** Start with `components = n`. For each edge `(a, b)`, call `unite(a, b)`; if they were in different components, `unite` returns `True` and we do `components -= 1`. After processing all edges, we have the final number of connected components. The minimum number of cable moves to make the graph connected is **components − 1** (we need to connect the components using that many relocated cables).

### Key Insights

1. **Need at least n − 1 edges** — A connected graph on \(n\) nodes has at least \(n - 1\) edges. So `connections.size() < n - 1` → impossible.
2. **Answer = components − 1** — Each operation connects two components; to go from \(c\) components to 1 we need \(c - 1\) operations.
3. **DSU fits naturally** — Each connection merges two computers; union-find counts components without building an explicit graph.

## Python Solution

### DSU (O(n + E·α(n)) time)

```python
from typing import List


class DSU:
    def __init__(self, n: int) -> None:
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # path compression
        return self.parent[x]

    def unite(self, x: int, y: int) -> bool:
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        self.rank[px] += self.rank[py]
        return True


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1
        dsu = DSU(n)
        components = n
        for x, y in connections:
            if dsu.unite(x, y):
                components -= 1
        return components - 1
```

## Algorithm Explanation

We need at least \(n - 1\) edges to connect \(n\) nodes, so if there are fewer edges we return `-1`. Otherwise we use a DSU: initially every node is its own component, so `components = n`. For each cable `(x, y)`, we unite the two endpoints; if they were in different components, `unite` returns `True` and we decrement `components`. After processing all connections, `components` is the number of connected components. The minimum number of cable moves to make the network connected is `components - 1` (one move connects two components).

## Complexity Analysis

- **Time**: O(n + E·α(n)) — E = len(connections); each unite/find is effectively O(α(n)).
- **Space**: O(n) for the DSU.

## Edge Cases

- **Not enough edges** — `len(connections) < n - 1` → return `-1`.
- **Already connected** — One component → return `0`.
- **n == 1** — Zero edges needed; `connections` may be empty; we need 0 moves. DSU gives 1 component → return 0. And `len(connections) >= 0 >= n - 1` for n=1, so we don’t return -1. Good.

## Common Mistakes

- **Skipping the n - 1 check** — Without it, when edges are insufficient we might return a non-negative number; the problem requires -1 when impossible.
- **Returning components instead of components - 1** — We need the number of *moves*, which is one less than the number of components (to merge c components we need c - 1 connections between them).

## Related Problems

- [LC 1202: Smallest String With Swaps](/2026/03/09/medium-1202-smallest-string-with-swaps/) — DSU to group indices.
- [LC 1584: Min Cost to Connect All Points](/2026/03/08/medium-1584-min-cost-to-connect-all-points/) — MST with DSU (Kruskal).
- [LC 684: Redundant Connection](https://leetcode.com/problems/redundant-connection/) — Find an edge that creates a cycle (DSU).
- [LC 323: Number of Connected Components in an Undirected Graph](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/) — Count components (same idea, no “moves”).
