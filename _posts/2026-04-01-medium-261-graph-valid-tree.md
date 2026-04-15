---
layout: post
title: "[Medium] 261. Graph Valid Tree"
date: 2026-04-01 00:00:00 -0700
categories: [leetcode, medium, graph, union-find, dfs]
tags: [leetcode, medium, graph, union-find, dfs, tree]
permalink: /2026/04/01/medium-261-graph-valid-tree/
---

# [Medium] 261. Graph Valid Tree

## Problem Statement

Given `n` nodes labeled `0` to `n - 1` and a list of undirected edges, determine whether these edges form a **valid tree**.

A valid tree on `n` nodes must be:

1. **Connected** — every node reachable from any other  
2. **Acyclic** — exactly `n - 1` edges and no cycles (equivalently: connected + `n - 1` edges)

## Examples

**Example 1:**

```python
Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
Output: True
```

**Example 2:**

```python
Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
Output: False  # cycle
```

## Constraints

- `1 <= n <= 2000`
- `0 <= edges.length <= 5000`
- `edges[i].length == 2`
- `0 <= ai, bi < n`
- No self-loops or duplicate edges in typical statements

## Clarification Questions

1. **Undirected?** Yes — treat each edge as bidirectional.
2. **Why `len(edges) == n - 1` first?** A tree on `n` nodes has exactly `n - 1` edges; fewer ⇒ disconnected, more ⇒ must contain a cycle (for simple graphs).

## Analysis Process

**Characterization:** For an undirected simple graph on `n` nodes, “connected + acyclic” ⇔ “connected + `n - 1` edges” ⇔ “acyclic + `n - 1` edges”.

So after enforcing `len(edges) == n - 1`, you only need **either**:

- detect a **cycle** while merging components (union-find), or  
- verify **one connected component** via DFS/BFS from a start node.

## Solution Option 1: Union-Find

```python
from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        parent = list(range(n))

        def find(x: int) -> int:
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        for u, v in edges:
            pu, pv = find(u), find(v)
            if pu == pv:
                return False
            parent[pu] = pv
        return True
```

With exactly `n - 1` edges and **no** cycle, the graph is a single tree (hence connected).

## Solution Option 2: DFS (adjacency list)

```python
from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()

        def dfs(node: int, par: int) -> bool:
            visited.add(node)
            for nei in graph[node]:
                if nei == par:
                    continue
                if nei in visited or not dfs(nei, node):
                    return False
            return True

        return dfs(0, -1) and len(visited) == n
```

Start from `0`; skip the edge back to `parent` to avoid false “cycle” on the undirected back-link. After DFS, all `n` nodes must be visited (connected).

## Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|--------|
| Union-find | O(n α(n)) ≈ O(n) | O(n) | Great when you only care about cycles / components |
| DFS | O(n + \|E\|) = O(n) here | O(n + \|E\|) | Explicit connectivity check; builds graph |

## Complexity

With `|E| = n - 1`:

- **Union-find:** time O(n α(n)), space O(n)  
- **DFS:** time O(n), space O(n) for graph + recursion stack

## Common Mistakes

- Skipping `len(edges) != n - 1` — then “no cycle” from union-find does **not** imply connected (forest with multiple trees).
- In DFS, forgetting to ignore `parent` → false cycle detection on the tree edge.
- Using directed graph logic on an undirected problem.

## Related Problems

- [LC 684: Redundant Connection](https://leetcode.com/problems/redundant-connection/)
- [LC 685: Redundant Connection II](https://leetcode.com/problems/redundant-connection-ii/)
- [LC 323: Number of Connected Components in an Undirected Graph](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/)
