---
layout: post
title: "310. Minimum Height Trees"
date: 2026-01-14 00:00:00 -0700
categories: [leetcode, medium, graph, tree, topological-sort, bfs]
permalink: /2026/01/14/medium-310-minimum-height-trees/
tags: [leetcode, medium, graph, tree, topological-sort, bfs, peeling-leaves]
---

# 310. Minimum Height Trees

## Problem Statement

A tree is an undirected graph in which any two vertices are connected by **exactly** one path. In other words, any connected graph without simple cycles is a tree.

You are given a tree of `n` nodes labelled from `0` to `n - 1`. The tree is represented as an array `edges` where `edges[i] = [ai, bi]` indicates that there is an undirected edge between nodes `ai` and `bi` in the tree.

Return *the labels of all nodes that are the roots of **minimum height trees (MHTs)***. You can return the answer in **any order**.

A **minimum height tree** is a tree rooted at a node such that the tree has the smallest possible height among all possible rooted trees.

## Examples

**Example 1:**
```
Input: n = 4, edges = [[1,0],[1,2],[1,3]]
Output: [1]
Explanation: As shown, the height of the tree when rooted at node 1 is 1, which is the minimum possible.
```

**Example 2:**
```
Input: n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
Output: [3,4]
```

## Constraints

- `1 <= n <= 2 * 10^4`
- `edges.length == n - 1`
- `0 <= ai, bi < n`
- `ai != bi`
- All the pairs `(ai, bi)` are distinct.
- The given input is **guaranteed** to be a tree and there will be **no repeated** edges.

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Tree structure**: Is the graph guaranteed to be a tree? (Assumption: Yes - per constraints, input is guaranteed to be a tree with n-1 edges)

2. **Height definition**: How is tree height defined? (Assumption: Height is the number of edges in the longest path from root to any leaf)

3. **Root selection**: Can we choose any node as root? (Assumption: Yes - we want to find which node(s) as root give minimum height)

4. **Multiple centers**: Can there be multiple minimum height trees? (Assumption: Yes - there can be 1 or 2 center nodes that give minimum height)

5. **Return format**: Should we return all possible roots or just one? (Assumption: Return all nodes that can serve as root for minimum height trees)

## Interview Deduction Process (20 minutes)

**Step 1: Brute-Force Approach (5 minutes)**

For each node, calculate the height of the tree when that node is the root (using BFS or DFS). Return the node(s) with minimum height. This approach requires O(n) time per node to calculate height, giving O(n²) overall complexity, which is too slow for large trees.

**Step 2: Semi-Optimized Approach (7 minutes)**

Use the fact that minimum height trees have roots at the "center" of the tree. Find the diameter of the tree (longest path), and the center nodes of the diameter are the roots. However, finding the diameter requires two BFS passes, and identifying center nodes requires additional processing. This approach works but can be complex to implement correctly.

**Step 3: Optimized Solution (8 minutes)**

Use topological sort (leaf removal): repeatedly remove leaf nodes (nodes with degree 1) until 1 or 2 nodes remain. These remaining nodes are the roots of minimum height trees. The key insight is that leaves contribute to tree height, so removing them iteratively reveals the center. This achieves O(n) time complexity. Alternatively, use two BFS passes to find diameter endpoints, then find the center of the diameter. The topological approach is simpler and more intuitive: keep removing leaves until the "core" remains, which naturally identifies the optimal roots.

## Solution Approach

This problem requires finding the center(s) of a tree. The key insight is that **minimum height trees have their roots at the center(s) of the longest path (diameter) in the tree**.

### Key Insights:

1. **Tree Centers**: A tree has at most 2 centers (nodes at the middle of the longest path)
2. **Peeling Leaves**: Repeatedly remove leaves (nodes with degree 1) until 1 or 2 nodes remain
3. **Topological Sort**: Similar to Kahn's algorithm, process nodes with indegree 1
4. **Remaining Nodes**: The 1 or 2 nodes remaining after peeling are the centers (MHT roots)

### Algorithm:

1. **Build Graph**: Create adjacency list and calculate degrees
2. **Find Leaves**: Initialize queue with all nodes having degree 1
3. **Peel Leaves Iteratively**:
   - Process all leaves at current level
   - Remove leaves and update degrees of neighbors
   - Add new leaves (degree becomes 1) to queue
   - Continue until ≤ 2 nodes remain
4. **Return Centers**: Remaining nodes are the MHT roots

## Solution

### **Solution: Peeling Leaves (Topological Sort)**

```python
from collections import defaultdict, deque

class Solution:
    def findMinHeightTrees(self, n, edges):
        if n == 0:
            return []
        if n == 1:
            return [0]

        # build graph
        adj = defaultdict(list)
        degree = [0] * n

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            degree[u] += 1
            degree[v] += 1

        # init leaves
        leaves = deque()
        for i in range(n):
            if degree[i] == 1:
                leaves.append(i)

        remaining = n

        # trim leaves level by level
        while remaining > 2:
            size = len(leaves)
            remaining -= size

            for _ in range(size):
                leaf = leaves.popleft()

                for nei in adj[leaf]:
                    degree[nei] -= 1
                    if degree[nei] == 1:
                        leaves.append(nei)

        # remaining nodes are roots of MHT
        return list(leaves)
```

### **Algorithm Explanation:**

1. **Edge Cases (Lines 5-7)**:
   - If `n == 0`, return empty
   - If `n == 1`, return `[0]` (single node is the center)

2. **Build Graph (Lines 9-19)**:
   - Create adjacency list `adj` for undirected graph
   - Calculate `inDegree` (degree) for each node
   - For each edge `[u, v]`, add both directions and increment degrees

3. **Initialize Leaves (Lines 21-26)**:
   - Find all nodes with `degree == 1` (leaves)
   - Add them to queue for processing

4. **Peel Leaves Iteratively (Lines 28-42)**:
   - **While `remainingNodes > 2`**:
     - Process all leaves at current level (batch processing)
     - For each leaf:
       - Remove it (decrement `remainingNodes`)
       - For each neighbor:
         - Decrement neighbor's degree
         - If neighbor's degree becomes 1, add to queue (new leaf)
   - Continue until ≤ 2 nodes remain

5. **Return Centers (Lines 44-48)**:
   - Remaining nodes in queue are the centers (MHT roots)
   - Return them as result

### **Why This Works:**

- **Tree Centers**: The center(s) of a tree are at the middle of the longest path
- **Peeling Leaves**: Removing leaves doesn't change the center(s) of the tree
- **Convergence**: After peeling, 1 or 2 nodes remain (the centers)
- **MHT Roots**: Centers minimize the maximum distance to any leaf

### **Example Walkthrough:**

**Input:** `n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]`

```
Tree structure:
    0
    |
    3
   /|\
  1 2 4
        \
         5

Step 1: Build Graph
  adj[0] = [3]
  adj[1] = [3]
  adj[2] = [3]
  adj[3] = [0,1,2,4]
  adj[4] = [3,5]
  adj[5] = [4]

  inDegree = [1, 1, 1, 4, 2, 1]

Step 2: Initialize Leaves
  Leaves: [0, 1, 2, 5] (degree = 1)

Step 3: First Iteration (remainingNodes = 6 > 2)
  Process leaves: [0, 1, 2, 5]
  
  Process 0:
    Neighbor: 3
    inDegree[3] = 4 - 1 = 3
    remainingNodes = 6 - 1 = 5
  
  Process 1:
    Neighbor: 3
    inDegree[3] = 3 - 1 = 2
    remainingNodes = 5 - 1 = 4
  
  Process 2:
    Neighbor: 3
    inDegree[3] = 2 - 1 = 1
    remainingNodes = 4 - 1 = 3
  
  Process 5:
    Neighbor: 4
    inDegree[4] = 2 - 1 = 1
    remainingNodes = 3 - 1 = 2
  
  New leaves: [3, 4] (both have degree 1 now)
  Leaves queue: [3, 4]

Step 4: Check Condition
  remainingNodes = 2 ≤ 2 → Stop

Step 5: Return Centers
  Result: [3, 4]
```

**Visual Representation:**
```
Initial:         After 1st iteration:
    0                 
    |                 
    3                 3
   /|\               / \
  1 2 4             4
        \             
         5           

Centers: 3 and 4 (both are valid MHT roots)
```

### **Complexity Analysis:**

- **Time Complexity:** O(n)
  - Building graph: O(n)
  - Peeling leaves: O(n) - each node processed once
  - Overall: O(n)
- **Space Complexity:** O(n)
  - Adjacency list: O(n)
  - Degree array: O(n)
  - Queue: O(n)

## Key Insights

1. **Tree Centers**: At most 2 centers exist (middle of longest path)
2. **Peeling Leaves**: Repeatedly remove leaves until centers remain
3. **Batch Processing**: Process all leaves at same level together
4. **Convergence**: Always converges to 1 or 2 nodes
5. **MHT Roots**: Centers minimize maximum distance to any leaf

## Edge Cases

1. **Single node**: `n = 1` → return `[0]`
2. **Two nodes**: `n = 2, edges = [[0,1]]` → return `[0,1]` (both are centers)
3. **Linear tree**: `n = 4, edges = [[0,1],[1,2],[2,3]]` → return `[1,2]` (middle nodes)
4. **Star tree**: `n = 4, edges = [[0,1],[0,2],[0,3]]` → return `[0]` (center)
5. **Balanced tree**: Returns 1 or 2 centers depending on structure

## Common Mistakes

1. **Not handling single node**: Forgetting edge case `n == 1`
2. **Wrong stopping condition**: Should stop when `remainingNodes <= 2`, not `== 0`
3. **Not batch processing**: Processing leaves one at a time instead of by level
4. **Wrong degree update**: Not updating degrees correctly when removing leaves
5. **Not tracking remaining nodes**: Forgetting to decrement `remainingNodes`

## Alternative Approaches

### **Approach 2: Two-Pass BFS (Find Diameter)**

Find the longest path (diameter) in the tree, then return the middle node(s).

```python
from collections import defaultdict, deque

class Solution:
    def findMinHeightTrees(self, n, edges):
        if n == 1:
            return [0]

        # build graph
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # BFS helper
        def bfs(start):
            q = deque([start])
            visited = [False] * n
            parent = [-1] * n

            visited[start] = True
            farthest = start

            while q:
                node = q.popleft()
                farthest = node

                for nei in adj[node]:
                    if not visited[nei]:
                        visited[nei] = True
                        parent[nei] = node
                        q.append(nei)

            return farthest, parent

        # 1st BFS: find one end of diameter
        u, _ = bfs(0)

        # 2nd BFS: find other end + parent pointers
        v, parent = bfs(u)

        # rebuild diameter path
        path = []
        cur = v
        while cur != -1:
            path.append(cur)
            cur = parent[cur]

        path.reverse()

        # find middle
        m = len(path)

        if m % 2 == 1:
            return [path[m // 2]]
        else:
            return [path[m // 2 - 1], path[m // 2]]
```

**Time Complexity:** O(n) - Two BFS passes  
**Space Complexity:** O(n)

### **Approach 3: Two-Pass DFS (Find Diameter)**

Similar to BFS approach but using DFS to find the diameter. Uses recursion to find farthest nodes.

```python
from collections import defaultdict

class Solution:
    def findMinHeightTrees(self, n, edges):
        if n == 1:
            return [0]

        # build graph
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # DFS helper
        def dfs(node, parent, dist):
            nonlocal farthestNode, maxDist

            if dist > maxDist:
                maxDist = dist
                farthestNode = node

            for nei in adj[node]:
                if nei == parent:
                    continue
                parent_map[nei] = node
                dfs(nei, node, dist + 1)

        # -------- First DFS --------
        farthestNode = 0
        maxDist = 0
        parent_map = [-1] * n

        dfs(0, -1, 0)
        u = farthestNode

        # -------- Second DFS --------
        farthestNode = u
        maxDist = 0
        parent_map = [-1] * n

        dfs(u, -1, 0)
        v = farthestNode

        # rebuild path u -> v
        path = []
        cur = v
        while cur != -1:
            path.append(cur)
            cur = parent_map[cur]

        path.reverse()

        # middle of diameter
        m = len(path)

        if m % 2 == 1:
            return [path[m // 2]]
        else:
            return [path[m // 2 - 1], path[m // 2]]
```

**Time Complexity:** O(n) - Two DFS passes  
**Space Complexity:** O(n) - Recursion stack

**Algorithm Explanation:**
1. **First DFS**: Start from any node (0), find the farthest node `u` by tracking distance
2. **Second DFS**: Start from `u`, find the farthest node `v` and build path using parent array
3. **Find Centers**: Middle node(s) of the path from `u` to `v` are the centers

**Key Points:**
- DFS recursively explores all paths from a starting node
- Tracks the farthest node and maximum distance encountered
- Parent array allows path reconstruction

### **Approach 4: DFS with Height Calculation**

Calculate height of tree when rooted at each node, return nodes with minimum height. This is less efficient but demonstrates the problem definition directly.

```python
from collections import defaultdict

class Solution:
    def findMinHeightTrees(self, n, edges):
        if n == 1:
            return [0]

        # build graph
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # DFS to compute height
        def dfs(node, parent):
            max_h = 0
            for nei in adj[node]:
                if nei == parent:
                    continue
                max_h = max(max_h, dfs(nei, node))
            return max_h + 1

        min_height = float('inf')
        result = []

        # try each node as root
        for root in range(n):
            height = dfs(root, -1)

            if height < min_height:
                min_height = height
                result = [root]
            elif height == min_height:
                result.append(root)

        return result
```

**Time Complexity:** O(n²) - For each node, DFS takes O(n)  
**Space Complexity:** O(n) - Recursion stack

**Note:** This approach is less efficient (O(n²)) compared to peeling leaves (O(n)), but it directly implements the problem definition.

**Comparison:**

| Approach | Time | Space | Complexity | Notes |
|----------|------|-------|------------|-------|
| **Peeling Leaves (BFS)** | O(n) | O(n) | Low | Most intuitive, recommended |
| **Two-Pass BFS** | O(n) | O(n) | Medium | Directly finds diameter |
| **Two-Pass DFS** | O(n) | O(n) | Medium | Similar to BFS, uses recursion |
| **DFS Height Calculation** | O(n²) | O(n) | Low | Direct implementation, less efficient |

## Related Problems

- [LC 207: Course Schedule](https://leetcode.com/problems/course-schedule/) - Topological sort
- [LC 210: Course Schedule II](https://leetcode.com/problems/course-schedule-ii/) - Topological sort ordering
- [LC 310: Minimum Height Trees](https://leetcode.com/problems/minimum-height-trees/) - This problem
- [LC 323: Number of Connected Components](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/) - Graph connectivity

---

*This problem demonstrates the **Peeling Leaves** pattern for finding tree centers. The key insight is that minimum height trees have their roots at the center(s) of the longest path, which can be found by repeatedly removing leaves until 1 or 2 nodes remain.*

