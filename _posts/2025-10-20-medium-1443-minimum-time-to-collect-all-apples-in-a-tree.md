---
layout: post
title: "1443. Minimum Time to Collect All Apples in a Tree"
date: 2025-10-20 13:45:00 -0700
categories: leetcode algorithm medium tree dfs bfs graph
permalink: /2025/10/20/medium-1443-minimum-time-to-collect-all-apples-in-a-tree/
---

# 1443. Minimum Time to Collect All Apples in a Tree

**Difficulty:** Medium  
**Category:** Tree, DFS, BFS, Graph

## Problem Statement

Given an undirected tree consisting of `n` vertices numbered from `0` to `n-1`, which has some apples in their vertices. You spend 1 second to walk over one edge of the tree. Return the minimum time in seconds you have to spend to collect all apples in the tree, starting at vertex 0 and coming back to this vertex.

The edges of the undirected tree are given in the array `edges`, where `edges[i] = [ai, bi]` means that exists an edge connecting the vertices `ai` and `bi`. Additionally, there is a boolean array `hasApple`, where `hasApple[i] = true` means that vertex `i` has an apple; otherwise, vertex `i` does not have any apple.

## Examples

### Example 1:
```
Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [false,false,true,false,true,true,false]
Output: 8
Explanation: The figure above represents the given tree where red vertices have an apple. One optimal path to collect all apples is shown by the green arrows.
```

### Example 2:
```
Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [false,false,true,false,false,true,false]
Output: 6
Explanation: The figure above represents the given tree where red vertices have an apple. One optimal path to collect all apples is shown by the green arrows.
```

### Example 3:
```
Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [false,false,false,false,false,false,false]
Output: 0
```

## Constraints

- `1 <= n <= 10^5`
- `edges.length == n - 1`
- `edges[i].length == 2`
- `0 <= ai < bi < n`
- `fromi < toi`
- `hasApple.length == n`

## Approach

This problem can be solved using either **DFS** or **BFS** approaches. The key insight is that we only need to visit subtrees that contain apples or lead to apples.

### DFS Approach (Optimal):
1. **Build adjacency list** from edges
2. **DFS from root (0)** with parent tracking to avoid cycles
3. **For each subtree**, calculate time needed if it contains apples
4. **Return total time** including 2 seconds per edge (going and coming back)

### BFS Approach:
1. **Build adjacency list** and **parent mapping** using BFS
2. **For each apple node**, trace path back to root
3. **Count edges** in the path, avoiding duplicates
4. **Return total time** (2 seconds per unique edge)

## Solution

### Approach 1: DFS (Optimal)

```python
class Solution:
    def dfs(self, adj: list[list[int]], hasApple: list[bool], node: int, parent: int) -> int:
        totalTime = 0
        for child in adj[node]:
            if child == parent:
                continue
            childTime = self.dfs(adj, hasApple, child, node)
            if childTime > 0 or hasApple[child]:
                totalTime += childTime + 2
        return totalTime

    def minTime(self, n: int, edges: list[list[int]], hasApple: list[bool]) -> int:
        adj = [[] for _ in range(n)]
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        return self.dfs(adj, hasApple, 0, -1)
```

### Approach 2: BFS with Path Tracing

```python
class Solution:

    def minTime(self, n: int, edges: list[list[int]], hasApple: list[bool]) -> int:
        from collections import deque
        
        adj = [[] for _ in range(n)]
        for e in edges:
            adj[e[0]].append(e[1])
            adj[e[1]].append(e[0])
        
        parent = [-1] * n
        q = deque([0])
        visited = [False] * n
        visited[0] = True
        
        while q:
            node = q.popleft()
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    parent[neighbor] = node
                    q.append(neighbor)
        
        visitedNodes = set()
        time = 0
        for i in range(n):
            if not hasApple[i]:
                continue
            curr = i
            while curr != 0 and curr not in visitedNodes:
                visitedNodes.add(curr)
                time += 2
                curr = parent[curr]
        return time
```

## Explanation

### DFS Approach (Recommended):

**Step-by-Step Process:**
1. **Build adjacency list** from edges (undirected graph)
2. **DFS from root (0)** with parent parameter to avoid cycles
3. **For each child subtree:**
   - Calculate time needed for that subtree
   - If subtree has apples OR contains apples, add `childTime + 2`
   - The `+2` accounts for going to subtree and coming back
4. **Return total time** for current subtree

**Key Insight:** We only visit edges that lead to apples or are on the path to apples.

### BFS Approach:

**Step-by-Step Process:**
1. **Build adjacency list** and **parent mapping** using BFS
2. **For each apple node**, trace path back to root
3. **Count unique edges** in the path (avoid duplicates)
4. **Return total time** (2 seconds per unique edge)

**Key Insight:** We trace paths from each apple back to root and count unique edges.

### Example Walkthrough (DFS):
For `n=7, edges=[[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple=[false,false,true,false,true,true,false]`:

- **DFS(0):** Check children 1, 2
- **DFS(1):** Check children 4, 5
  - **DFS(4):** hasApple[4]=true, return 0+2=2
  - **DFS(5):** hasApple[5]=true, return 0+2=2
  - **DFS(1):** return 2+2+2=6
- **DFS(2):** Check children 3, 6
  - **DFS(3):** hasApple[3]=false, return 0
  - **DFS(6):** hasApple[6]=false, return 0
  - **DFS(2):** return 0
- **DFS(0):** return 6+0=6, but hasApple[2]=true, so return 6+2=8

## Complexity Analysis

### DFS Approach:
- **Time Complexity:** O(n) - each node visited once
- **Space Complexity:** O(n) - adjacency list + recursion stack

### BFS Approach:
- **Time Complexity:** O(n) - BFS + path tracing
- **Space Complexity:** O(n) - adjacency list + parent array + visited set

## Which Approach is More Optimal?

**DFS Approach is more optimal** for the following reasons:

1. **Single Pass:** DFS solves the problem in one traversal
2. **No Extra Data Structures:** Doesn't need parent array or visited set
3. **Cleaner Logic:** Directly calculates time during traversal
4. **Better Space Usage:** Only uses recursion stack vs multiple arrays
5. **More Intuitive:** Naturally handles the tree structure

**BFS Approach Trade-offs:**
- **Two Passes:** Requires BFS + path tracing
- **More Memory:** Uses parent array and visited set
- **Complex Logic:** More complex path tracing logic

## Key Insights

1. **Tree Structure:** Undirected tree with n-1 edges
2. **Edge Cost:** Each edge costs 2 seconds (going + coming back)
3. **Optimal Path:** Only visit edges that lead to apples
4. **DFS Advantage:** Natural fit for tree traversal problems
5. **Parent Tracking:** Essential to avoid cycles in undirected graph

## Alternative Approaches

### Iterative DFS:
```python
def minTime(self, n: int, edges: list[list[int]], hasApple: list[bool]) -> int:
    adj = [[] for _ in range(n)]
    for edge in edges:
        adj[edge[0]].append(edge[1])
        adj[edge[1]].append(edge[0])
    
    stk = [(0, -1)]  # (node, parent)
    subtreeTime = [0] * n
    
    while stk:
        node, parent = stk.pop()
        
        # Process children
        for child in adj[node]:
            if child != parent:
                stk.append((child, node))
    
    return subtreeTime[0]
```

The **DFS approach is the most optimal** solution for this problem, providing the best balance of time complexity, space efficiency, and code clarity.
