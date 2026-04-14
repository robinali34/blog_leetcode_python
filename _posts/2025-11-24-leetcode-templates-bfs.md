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
# BFS on graph (adjacency list)
from collections import deque

def bfs(self, graph, start):
    q = deque()
    visited = [False] * len(graph)

    q.append(start)
    visited[start] = True

    while q:
        node = q.popleft()

        # Process node
        print(node, end=" ")

        # Explore neighbors
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                q.append(neighbor)
```

## BFS on Grid

BFS for 2D grid problems (4-directional or 8-directional).

```python
from collections import deque

# BFS on 2D grid (4-directional)
def bfsGrid(self, grid, start, target):
    m, n = len(grid), len(grid[0])

    q = deque([start])
    dist = [[-1] * n for _ in range(m)]

    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    dist[start[0]][start[1]] = 0

    while q:
        x, y = q.popleft()

        if (x, y) == target:
            return dist[x][y]

        for dx, dy in dirs:
            nx, ny = x + dx, y + dy

            if (0 <= nx < m and 0 <= ny < n and
                grid[nx][ny] != '#' and dist[nx][ny] == -1):

                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))

    return -1


# Count connected components (Number of Islands)
def numIslands(self, grid):
    m, n = len(grid), len(grid[0])
    count = 0

    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1':
                count += 1

                q = deque([(i, j)])
                grid[i][j] = '0'

                while q:
                    x, y = q.popleft()

                    for dx, dy in dirs:
                        nx, ny = x + dx, y + dy

                        if (0 <= nx < m and 0 <= ny < n and grid[nx][ny] == '1'):
                            grid[nx][ny] = '0'
                            q.append((nx, ny))

    return count
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 200 | Number of Islands | [Link](https://leetcode.com/problems/number-of-islands/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-11-20-medium-200-number-of-islands/) |
| 695 | Max Area of Island | [Link](https://leetcode.com/problems/max-area-of-island/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/10/20/medium-695-max-area-of-island/) |

## Multi-source BFS

Start BFS from multiple sources simultaneously.

```python
from collections import deque

# Multi-source BFS (e.g., 01 Matrix)
def updateMatrix(self, mat):
    m, n = len(mat), len(mat[0])

    q = deque()
    dist = [[-1] * n for _ in range(m)]

    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    # Add all zeros as starting points
    for i in range(m):
        for j in range(n):
            if mat[i][j] == 0:
                q.append((i, j))
                dist[i][j] = 0

    while q:
        x, y = q.popleft()

        for dx, dy in dirs:
            nx, ny = x + dx, y + dy

            if (0 <= nx < m and 0 <= ny < n and dist[nx][ny] == -1):
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))

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
# Shortest path in unweighted graph
from collections import deque

def shortestPath(self, graph, start, target):
    q = deque()
    dist = [-1] * len(graph)

    q.append(start)
    dist[start] = 0

    while q:
        node = q.popleft()

        if node == target:
            return dist[node]

        for neighbor in graph[node]:
            if dist[neighbor] == -1:
                dist[neighbor] = dist[node] + 1
                q.append(neighbor)
```

## Level-order Traversal

BFS for tree level-order traversal.

```python
# Binary Tree Level Order Traversal
from collections import deque

# Binary Tree Level Order Traversal
def levelOrder(self, root):
    result = []
    if not root:
        return result

    q = deque([root])

    while q:
        size = len(q)
        level = []

        for _ in range(size):
            node = q.popleft()
            level.append(node.val)

            if node.left:
                q.append(node.left)

            if node.right:
                q.append(node.right)

        result.append(level)

    return result


# Zigzag Level Order Traversal
def zigzagLevelOrder(self, root):
    result = []
    if not root:
        return result

    q = deque([root])
    leftToRight = True

    while q:
        size = len(q)
        level = [0] * size

        for i in range(size):
            node = q.popleft()

            index = i if leftToRight else (size - 1 - i)
            level[index] = node.val

            if node.left:
                q.append(node.left)

            if node.right:
                q.append(node.right)

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
# BFS with state (e.g., Shortest Path with Obstacle Elimination)
from collections import deque

def shortestPath(self, grid, k):
    m, n = len(grid), len(grid[0])

    visited = [[[False] * (k + 1) for _ in range(n)] for _ in range(m)]

    q = deque()
    # state: (x, y, obstacles_eliminated, steps)
    q.append((0, 0, 0, 0))

    visited[0][0][0] = True

    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while q:
        x, y, obstacles, steps = q.popleft()

        if x == m - 1 and y == n - 1:
            return steps

        for dx, dy in dirs:
            nx, ny = x + dx, y + dy

            if 0 <= nx < m and 0 <= ny < n:
                newObstacles = obstacles + grid[nx][ny]

                if newObstacles <= k and not visited[nx][ny][newObstacles]:
                    visited[nx][ny][newObstacles] = True
                    q.append((nx, ny, newObstacles, steps + 1))

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

