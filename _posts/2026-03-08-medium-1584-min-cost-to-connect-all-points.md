---
layout: post
title: "1584. Min Cost to Connect All Points"
date: 2026-03-08 00:00:00 -0700
categories: [leetcode, medium, graph, mst, union-find]
tags: [leetcode, medium, graph, kruskal, dsu, manhattan]
permalink: /2026/03/08/medium-1584-min-cost-to-connect-all-points/
---

# 1584. Min Cost to Connect All Points

## Problem Statement

You are given an array `points` representing integer coordinates of some points on a 2D plane, where `points[i] = [xi, yi]`.

The **cost of connecting** two points `[xi, yi]` and `[xj, yj]` is the **Manhattan distance**: `|xi - xj| + |yi - yj|`, where `|val|` denotes the absolute value of `val`.

Return the **minimum cost** to make all points connected. All points are connected if there is **exactly one simple path** between any two points.

## Examples

**Example 1:**

```python
Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
Output: 20
# One way: connect (0,0)-(2,2)=4, (0,0)-(3,10)=13, (0,0)-(5,2)=7, (0,0)-(7,0)=7
# Minimum total is achieved by an MST; e.g. 4+6+5+5=20 or similar.
```

**Example 2:**

```python
Input: points = [[3,12],[-2,5],[-4,1]]
Output: 18
```

## Constraints

- `1 <= points.length <= 1000`
- `-10^6 <= xi, yi <= 10^6`
- All pairs `(xi, yi)` are distinct.

## Clarification Questions

1. **Meaning of “connected”**: Exactly one simple path between every pair → the graph must be a **tree** spanning all points.  
   **Assumption**: Yes — we need a spanning tree.
2. **Edge cost**: Manhattan distance only?  
   **Assumption**: Yes — no other cost function.
3. **Multiple edges**: We can use any subset of the possible edges (any pair of points); we are not limited to a given edge list.  
   **Assumption**: Yes — we can connect any two points at cost = Manhattan distance.

## Interview Deduction Process (20 minutes)

**Step 1: Recognize MST (5 min)**  
We need a tree that spans all nodes and minimizes total edge weight. That is the **minimum spanning tree (MST)**. The graph is complete (every pair has an edge); weight = Manhattan distance.

**Step 2: Kruskal (10 min)**  
Generate all \(\binom{n}{2}\) edges with weights, sort by weight, then add edges in order using a DSU: if the two endpoints are in different components, unite them and add the weight. Stop after adding \(n - 1\) edges. Total cost is the sum of those edge weights.

**Step 3: DSU (5 min)**  
Use union-find with path compression and union by rank so each find/unite is effectively O(α(n)).

## Solution Approach

**Kruskal's algorithm:** Treat each point as a vertex. There is an edge between every pair of points with weight = Manhattan distance. Sort all edges by weight. Initialize a DSU of size \(n\). For each edge in sorted order, if the two endpoints are not in the same component, unite them and add the edge weight to the answer. After \(n - 1\) edges, we have an MST and return the total cost.

**DSU:** Path compression in `find` and union by rank in `unite` keep the structure efficient.

### Key Insights

1. **MST** — “Minimum cost to connect all points with exactly one path between any two” is the definition of a minimum spanning tree.
2. **Complete graph** — Every pair of points can be connected; edge weight = Manhattan distance. So we have O(n²) edges.
3. **Kruskal** — Sort edges, add in order without creating a cycle (DSU). Greedy choice is correct for MST.

## Python Solution

### Kruskal with DSU (O(n² log n) time, O(n²) space for edges)

```python
from typing import List


class DSU:
    def __init__(self, n: int) -> None:
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x: int) -> int:
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])  # path compression
        return self.parent[x]

    def unite(self, x: int, y: int) -> bool:
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        return True


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        all_edges: List[tuple[int, int, int]] = []

        for i in range(n):
            for j in range(i + 1, n):
                w = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                all_edges.append((w, i, j))

        all_edges.sort()

        dsu = DSU(n)
        mst_cost = 0
        edges_used = 0

        for weight, u, v in all_edges:
            if edges_used == n - 1:
                break
            if dsu.unite(u, v):
                mst_cost += weight
                edges_used += 1
        return mst_cost
```

## Algorithm Explanation

We build the complete graph: for each pair of points \((i, j)\) with \(i < j\), we add an edge with weight \(|x_i - x_j| + |y_i - y_j|\). We sort these edges by weight. We then run Kruskal: start with each point in its own component (DSU); for each edge in increasing order, if the two endpoints are in different components we unite them and add the edge weight to the answer. After \(n - 1\) such edges we have an MST and return the total cost. The DSU uses path compression in `find` and union by rank in `unite` (only increment rank when the two roots have equal rank) so operations are effectively O(α(n)).

## Complexity Analysis

- **Time**: O(n² log n) — we have O(n²) edges, sort them in O(n² log n), then process each with DSU operations O(α(n)) ≈ O(1).
- **Space**: O(n²) for the list of edges; O(n) for the DSU.

## Edge Cases

- **n == 1** — No edges needed; return 0.
- **n == 2** — One edge; cost = Manhattan distance between the two points.
- **Collinear or grid points** — Algorithm is the same; many edges may have equal weight.

## Common Mistakes

- **DSU rank update** — In union by rank, only increase the root’s rank by 1 when the two roots have the **same** rank. Adding `rank[py]` to `rank[px]` breaks the rank invariant and can make the tree deeper than intended.
- **Stopping condition** — We need exactly \(n - 1\) edges; we can break once `edges_used == n - 1`.
- **Manhattan distance** — Use `|x1-x2| + |y1-y2|`, not Euclidean.

## Related Problems

- [LC 1135: Connecting Cities With Minimum Cost](https://leetcode.com/problems/connecting-cities-with-minimum-cost/) — MST with given edge list.
- [LC 1168: Optimize Water Distribution in a Village](https://leetcode.com/problems/optimize-water-distribution-in-a-village/) — MST with virtual node.
- [LC 684: Redundant Connection](https://leetcode.com/problems/redundant-connection/) — Detect cycle with DSU.
- [LC 1319: Number of Operations to Make Network Connected](https://leetcode.com/problems/number-of-operations-to-make-network-connected/) — Count components; use DSU or DFS.
