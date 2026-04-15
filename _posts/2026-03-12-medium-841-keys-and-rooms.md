---
layout: post
title: "[Medium] 841. Keys and Rooms"
date: 2026-03-12 00:00:00 -0700
categories: [leetcode, medium, graph, dfs, bfs]
tags: [leetcode, medium, graph, reachability, stack, queue]
permalink: /2026/03/12/medium-841-keys-and-rooms/
---

# [Medium] 841. Keys and Rooms

## Problem Statement

There are `n` rooms labeled from `0` to `n - 1`. You start in room `0`.  

Each room `i` contains a list of keys `rooms[i]`, where **each key is labeled with a room number**.

All rooms are initially locked except room `0`.  
You can enter a room only if you have its key.

You can take all the keys in any room you enter.

Return `True` if you can visit **all the rooms**, or `False` otherwise.

## Examples

**Example 1:**

```python
Input: rooms = [[1],[2],[3],[]]
Output: True
# Start in 0, get key for 1.
# From 1, get key for 2.
# From 2, get key for 3.
# All rooms are reachable.
```

**Example 2:**

```python
Input: rooms = [[1,3],[3,0,1],[2],[0]]
Output: False
# Room 2 is never reachable; we never get key 2.
```

## Constraints

- `n == len(rooms)`
- `1 <= n <= 1000`
- `0 <= rooms[i].length <= 1000`
- `1 <= sum(len(rooms[i])) <= 3000`
- `0 <= rooms[i][j] < n`
- There are no duplicate keys in `rooms[i]`.

## Clarification Questions

1. **Key reuse**: Once we have a key for a room, can we use it multiple times?  
   **Assumption**: Yes — having the key means the room is effectively unlocked; we only need to visit it once.
2. **Duplicate keys**: Can a room contain duplicate keys or its own key?  
   **Assumption**: The constraints say no duplicates per room, but even if they existed, they do not change reachability (extra edges to the same node).
3. **Goal**: We just need to know if we can **reach all rooms** starting from room `0`?  
   **Assumption**: Yes — this is a graph reachability question.

## Abstraction

Treat this as a **graph problem**:

- Each room is a **node**.  
- Each key in `rooms[i]` is a **directed edge** from room `i` to `key`.  
- We begin at node `0` and want to know if we can **reach every node**.

So the problem is equivalent to:

> Starting from node 0 in a directed graph, can we visit all nodes?

## Baseline (Naive) — Why it’s suboptimal

A naive idea:

- For each room `i`, scan all previously visited rooms to see if any contains key `i`.  
- If yes, mark room `i` as reachable. Repeat until no new rooms are discovered.

This leads to repeatedly scanning previous rooms and keys:

- Potentially **O(n²)** or worse in practice due to repeated work.  
- Harder to reason about correctness and stopping conditions.

## Optimized Approach — DFS / BFS

We only need **reachability** from room `0`. The natural approach:

- Perform a **DFS or BFS** starting from room `0`.  
- Maintain a `visited` set (rooms we have entered).  
- Whenever we see a key `k` in the current room, if `k` is not visited, we add it to `visited` and push it onto the stack/queue.

At the end, if `len(visited) == n`, then **all rooms are reachable**.

### Complexity

- Let `V = n` (rooms), `E = total number of keys` (sum of `len(rooms[i])`).  
- **Time**: O(V + E) — we visit each room at most once and traverse each key once.  
- **Space**: O(V) for the `visited` set and stack/queue.

### Key Insights

1. **Graph reachability** — This is simply “can we reach all nodes from node 0?”  
2. **DFS or BFS both work** — Either traversal explores the reachable subgraph; only the order differs.  
3. **Visited set** — Prevents re-processing rooms, bounds time to O(V + E).

## Python Solution (DFS with stack)

```python
from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = set([0])
        stack = [0]

        while stack:
            room = stack.pop()
            for key in rooms[room]:
                if key not in visited:
                    visited.add(key)
                    stack.append(key)

        return len(visited) == n
```

## Python Solution (BFS with queue)

```python
from typing import List
from collections import deque


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = set([0])
        queue = deque([0])

        while queue:
            room = queue.popleft()
            for key in rooms[room]:
                if key not in visited:
                    visited.add(key)
                    queue.append(key)

        return len(visited) == n
```

## Algorithm Explanation

We model rooms as graph nodes and keys as directed edges. Starting from room `0`, we:

1. Initialize `visited = {0}` and a stack/queue containing just `0`.  
2. While there are rooms to process:
   - Pop a room `r`.  
   - For each `key` in `rooms[r]`:
     - If `key` has not been visited, add it to `visited` and push it to stack/queue.  
3. At the end, if `len(visited) == n`, we have reached all rooms and return `True`; otherwise `False`.

Because each room is processed at most once and each key is examined at most once, the time complexity is linear in the size of the graph (`V + E`).

## Complexity Analysis

- **Time**: O(V + E), where `V = n` (rooms), `E = sum(len(rooms[i]))` (total keys).  
- **Space**: O(V) for the `visited` set and stack/queue.

## Edge Cases

- `n = 1` and `rooms = [[]]` → already in room 0, so return `True`.  
- Some rooms have no keys (empty lists) — fine; they might still be reachable from others.  
- A room may contain a key to itself or duplicate keys — harmless; `visited` prevents re-processing.

## Common Mistakes

- **Re-scanning rooms** — Repeatedly scanning all previously visited rooms for keys leads to O(n²) behavior; use DFS/BFS instead.  
- **No visited set** — Without `visited`, you can loop indefinitely or process rooms many times.  
- **Assuming undirected edges** — Keys give directed edges; but for this problem, whether edges are considered directed or undirected doesn’t change the answer because you only ever travel along available keys.

## Related Problems

- [LC 200: Number of Islands](https://leetcode.com/problems/number-of-islands/) — DFS/BFS for connected components in a grid.  
- [LC 207: Course Schedule](https://leetcode.com/problems/course-schedule/) — Graph reachability and cycle detection.  
- [LC 133: Clone Graph](https://leetcode.com/problems/clone-graph/) — DFS/BFS graph traversal and cloning.  
- [LC 323: Number of Connected Components in an Undirected Graph](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/) — Count components by DFS/BFS.

