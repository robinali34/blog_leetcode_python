---
layout: post
title: "797. All Paths From Source to Target"
date: 2026-03-12 00:00:00 -0700
categories: [leetcode, medium, graph, dfs, backtracking]
tags: [leetcode, medium, graph, dfs, backtracking]
permalink: /2026/03/12/medium-797-all-paths-from-source-to-target/
---

# 797. All Paths From Source to Target

## Problem Statement

Given a directed acyclic graph (DAG) of `n` nodes labeled from `0` to `n - 1`, find all possible paths from node `0` to node `n - 1` and return them in **any order**.

The graph is given as follows: `graph[i]` is a list of all nodes you can visit from node `i` (i.e., there is a directed edge from node `i` to node `graph[i][j]`).

## Examples

**Example 1:**

```python
Input: graph = [[1,2],[3],[3],[]]
Output: [[0,1,3],[0,2,3]]
# Paths: 0 → 1 → 3  and  0 → 2 → 3
```

**Example 2:**

```python
Input: graph = [[4,3,1],[3,2,4],[3],[4],[]]
Output: [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
```

## Constraints

- `n == graph.length`
- `2 <= n <= 15`
- `0 <= graph[i][j] < n`
- `graph[i][j] != i` (no self-loops)
- No duplicate edges
- The graph is **guaranteed to be a DAG** (no cycles)

## Clarification Questions

1. **DAG**: So we never need to worry about cycles or visited set for “already on path”?  
   **Assumption**: Yes — no cycles; we still use a path list and backtrack so we don’t reuse the same path list incorrectly, but we won’t revisit the same node in a single path in a DAG from 0 to n-1 in standard traversal.
2. **All paths**: Return every distinct path from 0 to n-1?  
   **Assumption**: Yes.
3. **Order**: Any order of paths and any order of nodes within a path is fine?  
   **Assumption**: Yes — problem says “any order.”

## Interview Deduction Process (20 minutes)

**Step 1: Abstraction (5 min)**  
We have a DAG; we need to enumerate all simple paths from source 0 to target n−1. This is “all paths” enumeration, not shortest path — so we need to explore all branches.

**Step 2: DFS + backtracking (10 min)**  
Start at node 0 with a path list `[0]`. From current node u, for each neighbor v in `graph[u]`, append v to the path, recurse from v, then pop v (backtrack). When current node is n−1, we have a valid path — append a **copy** of the path to the result. No need for a separate “visited” set because the graph is a DAG and we’re building a path; we don’t revisit a node in the same path.

**Step 3: Implementation (5 min)**  
Use a single mutable path list; when we reach n−1, `result.append(list(path))`. Recurse on each neighbor, then pop. Base case: when node == n−1, record path and return (or don’t recurse further).

## Solution Approach

**DFS with backtracking:** Maintain a single list for the current path. Start at 0. When the current node is n−1, append a copy of the path to the result. For each neighbor in `graph[node]`, append the neighbor to the path, recurse, then pop (backtrack). This enumerates all paths from 0 to n−1. Because the graph is a DAG, we won’t cycle; each path is simple.

### Key Insights

1. **DAG** — No cycles, so we don’t need a global visited set to avoid infinite recursion; backtracking with one path list is enough.
2. **Append a copy** — When we find a path (current node == n−1), store `list(path)` so later backtracking doesn’t mutate stored paths.
3. **Backtrack** — After recursing on a neighbor, pop that neighbor so the same path list can be used for the next branch.

## Python Solution

### DFS with backtracking (O(2^n) in worst case, O(n) space for path)

```python
from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        result: List[List[int]] = []
        path: List[int] = []

        def dfs(node: int) -> None:
            path.append(node)
            if node == n - 1:
                result.append(list(path))
            else:
                for neighbor in graph[node]:
                    dfs(neighbor)
            path.pop()

        dfs(0)
        return result
```

## Algorithm Explanation

We start at node 0 and maintain a single `path` list. In `dfs(node)` we append `node` to `path`. If `node == n - 1`, we have a complete path and append a copy of `path` to `result`. Otherwise we recurse on each neighbor in `graph[node]`. After processing all neighbors we pop the current node from `path` (backtrack) so the parent can try other branches. The graph is a DAG so we never revisit a node in the same path; no extra visited set is needed.

## Complexity Analysis

- **Time**: In the worst case the graph can be nearly complete and we enumerate many paths; upper bound is O(2^n) paths each of length O(n). More precisely, proportional to the number of paths from 0 to n−1 plus the work to build them.
- **Space**: O(n) for the recursion stack and the single path list; O(output) for the result.

## Edge Cases

- **Two nodes**: graph = [[1], []] → one path [0, 1].
- **Linear chain**: graph = [[1],[2],[3],[]] → one path [0,1,2,3].
- **Multiple paths**: As in examples; all are enumerated.

## Common Mistakes

- **Forgetting to backtrack** — We must pop after recursing so the same path list is correct for siblings.
- **Appending the same list** — Use `result.append(list(path))`; if we appended `path`, later pops would change stored paths.
- **Using a visited set** — In a DAG from 0 to n−1, a simple path won’t repeat nodes; the path list itself prevents reuse within one branch. A global “visited” would block valid alternate paths that revisit no node, so don’t use it for this problem.

## Related Problems

- [LC 841: Keys and Rooms](/2026/03/12/medium-841-keys-and-rooms/) — Reachability from one node (single path not needed).
- [LC 113: Path Sum II](/2026/03/06/medium-113-path-sum-ii/) — All root-to-leaf paths in a tree (backtracking).
- [LC 207: Course Schedule](https://leetcode.com/problems/course-schedule/) — DAG cycle detection.
- [LC 129: Sum Root to Leaf Numbers](https://leetcode.com/problems/sum-root-to-leaf-numbers/) — Enumerate paths in a tree.
