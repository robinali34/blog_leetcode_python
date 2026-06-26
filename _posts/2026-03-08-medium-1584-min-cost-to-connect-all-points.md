---
layout: post
title: "[Medium] 1584. Min Cost to Connect All Points"
date: 2026-03-08
categories: [leetcode, medium, graph, mst, dsu]
tags: [leetcode, medium, graph, mst, kruskal, dsu]
permalink: /2026/03/08/medium-1584-min-cost-to-connect-all-points/
---

{% raw %}
You are given an array `points` where `points[i] = [xi, yi]` represents a point on the 2D plane. The cost to connect two points is the **Manhattan distance**: `|xi - xj| + |yi - yj|`. Return the minimum cost to connect all points such that every pair of points has a path between them.

## Examples

**Example 1:**

```
Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
Output: 20
```

**Example 2:**

```
Input: points = [[3,12],[-2,5],[-4,1]]
Output: 18
```

## Constraints

- `1 <= points.length <= 1000`
- `-10^6 <= xi, yi <= 10^6`
- All pairs `(xi, yi)` are distinct

## Common Approaches

Typical techniques for this pattern:

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| **BFS / DFS traversal** *(this problem)* | O(V+E) | O(V) | Connectivity, flood fill |
| Dijkstra | O((V+E)log V) | O(V) | Non-negative edge weights |
| Union-Find (DSU) | O(α(n)) | O(n) | Dynamic connectivity |
| Topological sort | O(V+E) | O(V) | DAG ordering, cycle detection |

## Thinking Process

This is a **Minimum Spanning Tree (MST)** problem on a complete graph. Each point is a node, and the edge weight between any two points is their Manhattan distance.

### Kruskal's Algorithm

1. Generate all binom{n}{2} edges with their Manhattan distance weights
2. Sort edges by weight (ascending)
3. Greedily add edges using **DSU (Union-Find)** -- skip edges that would create a cycle
4. Stop after adding n - 1 edges (MST is complete)

### Why Kruskal?

For a complete graph with n nodes, there are O(n^2) edges. Kruskal's sorts them and processes greedily, giving O(n^2 log n) total. Prim's with a heap is also O(n^2 log n) here, but Kruskal + DSU is cleaner for complete graphs.

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

## Approach: Kruskal's MST + DSU -- O(n^2 log n)
```python
Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
Output: 20
# One way: connect (0,0)-(2,2)=4, (0,0)-(3,10)=13, (0,0)-(5,2)=7, (0,0)-(7,0)=7
# Minimum total is achieved by an MST; e.g. 4+6+5+5=20 or similar.
```

### Solution Explanation

**Approach:** BFS / DFS traversal (this problem)

**Key idea:** This is a **Minimum Spanning Tree (MST)** problem on a complete graph. Each point is a node, and the edge weight between any two points is their Manhattan distance.

**How the code works:**
1. Generate all binom{n}{2} edges with their Manhattan distance weights
2. Sort edges by weight (ascending)
3. Greedily add edges using **DSU (Union-Find)** -- skip edges that would create a cycle
4. Stop after adding n - 1 edges (MST is complete)

**Walkthrough** — input `points = [[0,0],[2,2],[3,10],[5,2],[7,0]]`, expected output `20`:

1. Initialize variables from the problem setup.
2. Apply the main loop / recursion until the condition is met.
3. Confirm the result matches the expected output.
## Walk-Through

```
Points: [0,0], [2,2], [3,10], [5,2], [7,0]

Edges sorted by weight (first few):
  (0,1) w=4, (1,3) w=3, (0,3) w=7, (0,4) w=7, (3,4) w=4, ...

Process:
  (1,3) w=3  → unite 1,3  → cost=3,  edges=1
  (0,1) w=4  → unite 0,1  → cost=7,  edges=2
  (3,4) w=4  → unite 3,4  → cost=11, edges=3
  (0,2) w=13 → unite 0,2  → cost=20, edges=4 = n-1 → done!

MST cost = 20 ✓
```

## DSU (Union-Find) Recap

- **Path compression** (`find`): flattens the tree so future finds are nearly O(1)
- **Union by rank**: always attach the smaller tree under the larger root
- Combined: amortized O(α(n)) per operation (practically constant)

## Common Mistakes

- Forgetting to stop after n - 1 edges (MST of n nodes always has exactly n - 1 edges)
- Generating duplicate edges (only iterate `j = i + 1` to `n`, not all pairs)
- Using edge weight for rank in DSU (rank tracks tree height/size, not edge weight)

## Key Takeaways

- **Complete graph MST** = generate all edges + Kruskal's. Simple and effective for n ≤ 1000
- **DSU** is the natural companion to Kruskal's -- it answers "are these connected?" in near-constant time
- For larger n, Prim's with adjacency list or geometric optimizations (e.g., only considering nearest neighbors) would be needed

## Related Problems

- [1135. Connecting Cities With Minimum Cost](https://www.leetcode.com/problems/connecting-cities-with-minimum-cost/) -- Kruskal on given edges
- [1168. Optimize Water Distribution in a Village](https://www.leetcode.com/problems/optimize-water-distribution-in-a-village/) -- MST with virtual node
- [261. Graph Valid Tree](https://www.leetcode.com/problems/graph-valid-tree/) -- DSU for connectivity check

## References

- [LC 1584: Min Cost to Connect All Points on LeetCode](https://www.leetcode.com/problems/min-cost-to-connect-all-points/)
- [LeetCode Discuss — LC 1584: Min Cost to Connect All Points](https://www.leetcode.com/problems/min-cost-to-connect-all-points/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/min-cost-to-connect-all-points/editorial/) *(may require premium)*

## Template Reference

- [Graph](/posts/2025-10-29-leetcode-templates-graph/)
- [Data Structures (DSU)](/posts/2025-10-29-leetcode-templates-data-structures/)

{% endraw %}
