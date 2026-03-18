---
layout: post
title: "1376. Time Needed to Inform All Employees"
date: 2026-03-17 00:00:00 -0700
categories: [leetcode, medium, tree, graph, dfs, bfs]
tags: [leetcode, medium, tree, graph, dfs, bfs]
permalink: /2026/03/17/medium-1376-time-needed-to-inform-all-employees/
---

# 1376. Time Needed to Inform All Employees

## Problem Statement

A company has `n` employees, numbered from `0` to `n - 1`. The **head** of the company has `id = headID`.

You are given two integer arrays:

- `manager[i]` — the direct manager of employee `i` (for the head, `manager[headID] == -1`).  
- `informTime[i]` — the time it takes for employee `i` to inform all of their **direct** subordinates.

The company structure forms a **tree** rooted at `headID` (directed edges from manager to subordinates).

It takes `informTime[i]` minutes to pass information from employee `i` to all of their direct subordinates **in parallel**. Each subordinate then repeats the process with their own subordinates, and so on.

Return the **number of minutes** needed to inform **all** employees about an urgent piece of news.

## Examples

**Example 1:**

```python
Input: n = 1, headID = 0, manager = [-1], informTime = [0]
Output: 0
```

**Example 2:**

```python
Input: 
n = 6, headID = 2
manager = [2,2,-1,2,2,2]
informTime = [0,0,1,0,0,0]

Output: 1
# Head 2 informs everyone in 1 minute (all its direct subordinates in parallel).
```

## Constraints

- `1 <= n <= 10^5`
- `0 <= headID < n`
- `manager.length == n`
- `informTime.length == n`
- `manager[headID] == -1`
- For all `i != headID`, `0 <= manager[i] < n`
- The structure is a **tree**.

## Clarification Questions

1. **Parallel informing**: When a manager informs their direct subordinates, does that happen in parallel?  
   **Assumption**: Yes — all direct subordinates receive the message after `informTime[manager]` minutes at the same time.
2. **Leaf inform time**: For employees with no subordinates, is `informTime[i]` always 0?  
   **Assumption**: Yes (no one to inform).
3. **Answer definition**: We want the maximum time taken for any employee to receive the news (i.e., the longest root-to-leaf time)?  
   **Assumption**: Yes.

## Interview Deduction Process (20 minutes)

**Step 1: Tree view (5 min)**  
The `manager` array defines a **rooted tree** with edges from manager to subordinate:

- Node = employee.  
- Edge = `manager[i] -> i`.  
- The time to go from a manager to its children is `informTime[manager]`.

We need the **longest time** from `headID` to any leaf (employee with no subordinates).

**Step 2: Naive baseline (5 min)**  
For each employee `i`:

- Walk up the chain: `i → manager[i] → manager[manager[i]] → ... → headID`,  
- Sum up the inform times along the path,  
- Track the maximum across all employees.

Worst case (a long chain): length `n`, and repeating this for each of `n` employees gives **O(n²)** time.

**Step 3: Optimization (10 min)**  
Instead of repeatedly walking up, we can:

1. Build an **adjacency list**: `manager -> list of subordinates`.  
2. Run one **DFS or BFS** from `headID`, accumulating the time along the path, and keep the maximum.

This visits each node once → **O(n)** time.

## Solution Approach

**Graph = tree rooted at headID:** Build `graph[m]` = list of employees that have `manager == m`. Then:

- **DFS approach:**  
  `time(node) = informTime[node] + max(time(child) for child in children)`.  
  The answer is `time(headID)`.

- **BFS approach:**  
  Level-order traversal from `headID`, carrying the time accumulated so far; track the maximum time when popping nodes.

### Key Insights

1. **Tree DP / longest path** — Time to a node is parent’s time plus `informTime[parent]`. We want the maximum over all leaves.  
2. **Single pass** — Each node is visited once; no recomputing chains.  
3. **Graph direction** — Edges go from manager to subordinate, not the other way around.

## Python Solution — DFS

```python
from collections import defaultdict
from typing import List


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph: dict[int, list[int]] = defaultdict(list)
        for i in range(n):
            if manager[i] != -1:
                graph[manager[i]].append(i)

        def dfs(node: int) -> int:
            max_time = 0
            for child in graph[node]:
                max_time = max(max_time, dfs(child))
            return informTime[node] + max_time

        return dfs(headID)
```

## Python Solution — BFS

```python
from collections import defaultdict, deque
from typing import List


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph: dict[int, list[int]] = defaultdict(list)
        for i in range(n):
            if manager[i] != -1:
                graph[manager[i]].append(i)

        queue = deque([(headID, 0)])  # (node, time_so_far)
        max_time = 0

        while queue:
            node, time = queue.popleft()
            max_time = max(max_time, time)
            for child in graph[node]:
                queue.append((child, time + informTime[node]))

        return max_time
```

## Algorithm Explanation

In the DFS version, `dfs(node)` returns the total time needed to inform everyone in the subtree rooted at `node`. For each child, we compute `dfs(child)` and take the maximum, since informing subtrees happens in parallel; the total for `node` is its own `informTime[node]` plus the longest child time.

In the BFS version, we propagate the accumulated time along edges: when we are at `(node, time)`, each child gets called with `time + informTime[node]`. The answer is the maximum `time` seen for any node.

## Complexity Analysis

- **Time**: O(n) — build adjacency list in O(n), then DFS or BFS visits each node once.  
- **Space**: O(n) for adjacency list and recursion stack or queue.

## Edge Cases

- `n = 1` and `informTime[headID] = 0` → answer is `0`.  
- A long chain (each employee manages exactly one subordinate) — DFS depth = n, BFS queue size up to n.  
- A star (head manages everyone) — answer is `informTime[headID]`.

## Common Mistakes

- **Adding `informTime[child]` instead of `informTime[node]`** during propagation — children’s time is added on the **edge into** them; we must use the manager’s `informTime`.  
- **Trying to walk up from each node** — leads to O(n²) re-traversal; better to build the tree and walk down once.  
- **Forgetting parallelism** — We should take the **maximum** child time, not sum of all child times.

## Related Problems

- [LC 104: Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/) — Longest root-to-leaf depth.  
- [LC 543: Diameter of Binary Tree](/2026/03/06/easy-543-diameter-of-binary-tree/) — Longest path in a tree.  
- [LC 1339: Maximum Product of Splitted Binary Tree](https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/) — Tree DP.  
- [LC 207: Course Schedule](https://leetcode.com/problems/course-schedule/) — Directed graph / reachability.

