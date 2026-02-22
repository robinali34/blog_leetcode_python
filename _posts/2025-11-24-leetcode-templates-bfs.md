---
layout: post
title: "Algorithm Templates: BFS"
date: 2025-11-24 00:00:00 -0700
categories: leetcode templates bfs graph
permalink: /posts/2025-11-24-leetcode-templates-bfs/
tags: [leetcode, templates, bfs, graph, traversal]
---

{% raw %}
Minimal, copy-paste C++ for graph and grid BFS, multi-source BFS, shortest path, and level-order traversal. See also [Graph](/posts/2025-10-29-leetcode-templates-graph/) for Dijkstra and 0-1 BFS.

## Contents

- [Basic BFS](#basic-bfs)
- [BFS on Grid](#bfs-on-grid)
- [Multi-source BFS](#multi-source-bfs)
- [BFS for Shortest Path](#bfs-for-shortest-path)
- [Level-order Traversal](#level-order-traversal)
- [BFS with State](#bfs-with-state)

## Basic BFS

Breadth-First Search explores nodes level by level using a queue.

```python
// BFS on graph (adjacency list)
def bfs(self, graph, start):
    deque[int> q
    list[bool> visited(len(graph), False)
    q.push(start)
    visited[start] = True
    while not not q:
        node = q[0]
        q.pop()
        // Process node
        cout << node << " "
        // Explore neighbors
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                q.push(neighbor)
```

## BFS on Grid

BFS for 2D grid problems (4-directional or 8-directional).

```python
// BFS on 2D grid (4-directional)
def bfsGrid(self, grid, pair<int, start, pair<int, target):
    m = len(grid), n = grid[0].__len__()
    deque[pair<int, int>> q
    list[list[int>> dist(m, list[int>(n, -1))
    list[pair<int, int>> dirs = \:\:0,1\, \:0,-1\, \:1,0\, \:-1,0\\
q.push(start)
dist[start.first][start.second] = 0
while not not q:
    [x, y] = q[0]
    q.pop()
    if make_pair(x, y) == target:
        return dist[x][y]
    for ([dx, dy] : dirs) :
    nx = x + dx, ny = y + dy
    if (nx >= 0  and  nx < m  and  ny >= 0  and  ny < n  and
    grid[nx][ny] != '#'  and  dist[nx][ny] == -1) :
    dist[nx][ny] = dist[x][y] + 1
    q.push(:nx, ny)
return -1
// Count connected components (Number of Islands)
def numIslands(self, grid):
    m = len(grid), n = grid[0].__len__()
    count = 0
    list[pair<int, int>> dirs = \:\:0,1\, \:0,-1\, \:1,0\, \:-1,0\\
for (i = 0 i < m i += 1) :
for (j = 0 j < n j += 1) :
if grid[i][j] == '1':
    count += 1
    deque[pair<int, int>> q
    q.push(:i, j)
    grid[i][j] = '0'
    while not not q:
        [x, y] = q[0]
        q.pop()
        for ([dx, dy] : dirs) :
        nx = x + dx, ny = y + dy
        if (nx >= 0  and  nx < m  and  ny >= 0  and  ny < n  and
        grid[nx][ny] == '1') :
        grid[nx][ny] = '0'
        q.push(:nx, ny)
return count
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 200 | Number of Islands | [Link](https://leetcode.com/problems/number-of-islands/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-11-20-medium-200-number-of-islands/) |
| 695 | Max Area of Island | [Link](https://leetcode.com/problems/max-area-of-island/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/10/20/medium-695-max-area-of-island/) |

## Multi-source BFS

Start BFS from multiple sources simultaneously.

```python
// Multi-source BFS (e.g., 01 Matrix)
def updateMatrix(self, mat):
    m = len(mat), n = mat[0].__len__()
    deque[pair<int, int>> q
    list[list[int>> dist(m, list[int>(n, -1))
    list[pair<int, int>> dirs = \:\:0,1\, \:0,-1\, \:1,0\, \:-1,0\\
// Add all zeros as starting points
for (i = 0 i < m i += 1) :
for (j = 0 j < n j += 1) :
if mat[i][j] == 0:
    q.push(:i, j)
    dist[i][j] = 0
while not not q:
    [x, y] = q[0]
    q.pop()
    for ([dx, dy] : dirs) :
    nx = x + dx, ny = y + dy
    if nx >= 0  and  nx < m  and  ny >= 0  and  ny < n  and  dist[nx][ny] == -1:
        dist[nx][ny] = dist[x][y] + 1
        q.push(:nx, ny)
return dist
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 286 | Walls and Gates | [Link](https://leetcode.com/problems/walls-and-gates/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-12-14-medium-286-walls-and-gates/) |
| 542 | 01 Matrix | [Link](https://leetcode.com/problems/01-matrix/) | - |
| 317 | Shortest Distance from All Buildings | [Link](https://leetcode.com/problems/shortest-distance-from-all-buildings/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/09/24/hard-317-shortest-distance-from-all-buildings/) |
| 994 | Rotting Oranges | [Link](https://leetcode.com/problems/rotting-oranges/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-12-13-medium-994-rotting-oranges/) |

## BFS for Shortest Path

BFS finds shortest path in unweighted graphs.

```python
// Shortest path in unweighted graph
def shortestPath(self, graph, start, target):
    deque[int> q
    list[int> dist(len(graph), -1)
    q.push(start)
    dist[start] = 0
    while not not q:
        node = q[0]
        q.pop()
        if node == target:
            return dist[node]
        for neighbor in graph[node]:
            if dist[neighbor] == -1:
                dist[neighbor] = dist[node] + 1
                q.push(neighbor)
    return -1
```

## Level-order Traversal

BFS for tree level-order traversal.

```python
// Binary Tree Level Order Traversal
def levelOrder(self, root):
    list[list[int>> result
    if (not root) return result
    deque[TreeNode> q
    q.push(root)
    while not not q:
        size = len(q)
        list[int> level
        for (i = 0 i < size i += 1) :
        TreeNode node = q[0]
        q.pop()
        level.append(node.val)
        if node.left) q.push(node.left:
        if node.right) q.push(node.right:
    result.append(level)
return result
// Zigzag Level Order Traversal
def zigzagLevelOrder(self, root):
    list[list[int>> result
    if (not root) return result
    deque[TreeNode> q
    q.push(root)
    bool leftToRight = True
    while not not q:
        size = len(q)
        list[int> level(size)
        for (i = 0 i < size i += 1) :
        TreeNode node = q[0]
        q.pop()
        (i if             index = leftToRight  else size - 1 - i)
        level[index] = node.val
        if node.left) q.push(node.left:
        if node.right) q.push(node.right:
    result.append(level)
    leftToRight = not leftToRight
return result
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 102 | Binary Tree Level Order Traversal | [Link](https://leetcode.com/problems/binary-tree-level-order-traversal/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/01/07/medium-102-binary-tree-level-order-traversal/) |
| 103 | Binary Tree Zigzag Level Order Traversal | [Link](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/01/06/medium-103-binary-tree-zigzag-level-order-traversal/) |
| 314 | Binary Tree Vertical Order Traversal | [Link](https://leetcode.com/problems/binary-tree-vertical-order-traversal/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/10/20/medium-314-binary-tree-vertical-order-traversal/) |
| 429 | N-ary Tree Level Order Traversal | [Link](https://leetcode.com/problems/n-ary-tree-level-order-traversal/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/01/07/medium-429-n-ary-tree-level-order-traversal/) |
| 993 | Cousins in Binary Tree | [Link](https://leetcode.com/problems/cousins-in-binary-tree/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/01/07/easy-993-cousins-in-binary-tree/) |
| 863 | All Nodes Distance K in Binary Tree | [Link](https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-10-25-medium-863-all-nodes-distance-k-in-binary-tree/) |

## BFS with State

BFS when state includes more than just position.

```python
// BFS with state (e.g., Shortest Path with Obstacle Elimination)
def shortestPath(self, grid, k):
    m = len(grid), n = grid[0].__len__()
    list[list[list[bool>>> visited(m, list[list[bool>>(n, list[bool>(k + 1, False)))
    deque[list[int>> q // :x, y, obstacles_eliminated, steps
q.push(:0, 0, 0, 0)
visited[0][0][0] = True
list[pair<int, int>> dirs = \:\:0,1\, \:0,-1\, \:1,0\, \:-1,0\\
while not not q:
    state = q[0]
    q.pop()
    x = state[0], y = state[1], obstacles = state[2], steps = state[3]
    if x == m - 1  and  y == n - 1:
        return steps
    for ([dx, dy] : dirs) :
    nx = x + dx, ny = y + dy
    if nx >= 0  and  nx < m  and  ny >= 0  and  ny < n:
        newObstacles = obstacles + grid[nx][ny]
        if newObstacles <= k  and  not visited[nx][ny][newObstacles]:
            visited[nx][ny][newObstacles] = True
            q.push(:nx, ny, newObstacles, steps + 1)
return -1
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 1293 | Shortest Path in a Grid with Obstacles Elimination | [Link](https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/) | - |
| 847 | Shortest Path Visiting All Nodes | [Link](https://leetcode.com/problems/shortest-path-visiting-all-nodes/) | - |

## More templates

- **Graph (Dijkstra, 0-1 BFS, topo):** [Graph](/posts/2025-10-29-leetcode-templates-graph/)
- **Data structures, Search:** [Data Structures & Core Algorithms](/posts/2025-10-29-leetcode-templates-data-structures/), [Search](/posts/2026-01-20-leetcode-templates-search/)
- **Master index:** [Categories & Templates](/posts/2025-10-29-leetcode-categories-and-templates/)
{% endraw %}

