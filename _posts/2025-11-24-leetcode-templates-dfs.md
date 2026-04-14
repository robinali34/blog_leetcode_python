---
layout: post
title: "Algorithm Templates: DFS"
date: 2025-11-24 00:00:00 -0700
categories: leetcode templates dfs graph
permalink: /posts/2025-11-24-leetcode-templates-dfs/
tags: [leetcode, templates, dfs, graph, traversal]
---

{% raw %}
Minimal, copy-paste Python for graph DFS, grid DFS, tree DFS, memoization, and iterative DFS. See also [Graph](/posts/2025-10-29-leetcode-templates-graph/) and [Backtracking](/posts/2025-11-24-leetcode-templates-backtracking/).

## Contents

- [Basic DFS](#basic-dfs)
- [DFS on Grid](#dfs-on-grid)
- [DFS on Tree](#dfs-on-tree)
- [DFS with Memoization](#dfs-with-memoization)
- [Iterative DFS](#iterative-dfs)

## Basic DFS

Depth-First Search explores as far as possible before backtracking.

```python
# DFS on graph (adjacency list)
def dfs_graph(graph: list[list[int]], node: int, visited: list[bool]) -> None:
    visited[node] = True
    # process node
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs_graph(graph, neighbor, visited)


def dfs_find_target(
    graph: list[list[int]], node: int, target: int, visited: list[bool]
) -> bool:
    if node == target:
        return True
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor] and dfs_find_target(graph, neighbor, target, visited):
            return True
    return False

```

## DFS on Grid

DFS for 2D grid problems (connected components, paths).

```python
# DFS on 2D grid (4-directional)
DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def dfs_grid(grid: list[list[str]], i: int, j: int) -> None:
    m, n = len(grid), len(grid[0])
    if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != "1":
        return
    grid[i][j] = "0"
    for di, dj in DIRS:
        dfs_grid(grid, i + di, j + dj)


def num_islands(grid: list[list[str]]) -> int:
    m, n = len(grid), len(grid[0])
    count = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == "1":
                count += 1
                dfs_grid(grid, i, j)
    return count


def dfs_word_search(board: list[list[str]], i: int, j: int, word: str, idx: int) -> bool:
    if idx == len(word):
        return True
    if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
        return False
    if board[i][j] != word[idx]:
        return False
    temp = board[i][j]
    board[i][j] = "#"
    for di, dj in DIRS:
        if dfs_word_search(board, i + di, j + dj, word, idx + 1):
            board[i][j] = temp
            return True
    board[i][j] = temp
    return False

```

| ID | Title | Link | Solution |
|---|---|---|---|
| 200 | Number of Islands | [Link](https://leetcode.com/problems/number-of-islands/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-11-20-medium-200-number-of-islands/) |
| 79 | Word Search | [Link](https://leetcode.com/problems/word-search/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/01/12/medium-79-word-search/) |
| 695 | Max Area of Island | [Link](https://leetcode.com/problems/max-area-of-island/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/10/20/medium-695-max-area-of-island/) |
| 133 | Clone Graph | [Link](https://leetcode.com/problems/clone-graph/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/10/20/medium-133-clone-graph/) |
| 417 | Pacific Atlantic Water Flow | [Link](https://leetcode.com/problems/pacific-atlantic-water-flow/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/10/19/medium-417-pacific-atlantic-water-flow/) |
| 323 | Number of Connected Components | [Link](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/01/07/medium-323-number-of-connected-components-in-an-undirected-graph/) |
| 547 | Number of Provinces | [Link](https://leetcode.com/problems/number-of-provinces/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-12-18-medium-547-number-of-provinces/) |

## DFS on Tree

DFS for tree problems (preorder, inorder, postorder).

```python
class TreeNode:
    def __init__(self, val: int = 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preorder(root: TreeNode | None, result: list[int]) -> None:
    if not root:
        return
    result.append(root.val)
    preorder(root.left, result)
    preorder(root.right, result)


def inorder(root: TreeNode | None, result: list[int]) -> None:
    if not root:
        return
    inorder(root.left, result)
    result.append(root.val)
    inorder(root.right, result)


def postorder(root: TreeNode | None, result: list[int]) -> None:
    if not root:
        return
    postorder(root.left, result)
    postorder(root.right, result)
    result.append(root.val)


def has_path_sum(root: TreeNode | None, target_sum: int) -> bool:
    if not root:
        return False
    if not root.left and not root.right:
        return root.val == target_sum
    return has_path_sum(root.left, target_sum - root.val) or has_path_sum(
        root.right, target_sum - root.val
    )


def sum_numbers(root: TreeNode | None, cur: int = 0) -> int:
    if not root:
        return 0
    cur = cur * 10 + root.val
    if not root.left and not root.right:
        return cur
    return sum_numbers(root.left, cur) + sum_numbers(root.right, cur)

```

| ID | Title | Link | Solution |
|---|---|---|---|
| 100 | Same Tree | [Link](https://leetcode.com/problems/same-tree/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/01/19/easy-100-same-tree/) |
| 101 | Symmetric Tree | [Link](https://leetcode.com/problems/symmetric-tree/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/01/19/easy-101-symmetric-tree/) |
| 104 | Maximum Depth of Binary Tree | [Link](https://leetcode.com/problems/maximum-depth-of-binary-tree/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/01/19/easy-104-maximum-depth-of-binary-tree/) |
| 111 | Minimum Depth of Binary Tree | [Link](https://leetcode.com/problems/minimum-depth-of-binary-tree/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/01/19/easy-111-minimum-depth-of-binary-tree/) |
| 112 | Path Sum | [Link](https://leetcode.com/problems/path-sum/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/01/19/easy-112-path-sum/) |
| 129 | Sum Root to Leaf Numbers | [Link](https://leetcode.com/problems/sum-root-to-leaf-numbers/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-11-24-medium-129-sum-root-to-leaf-numbers/) |
| 226 | Invert Binary Tree | [Link](https://leetcode.com/problems/invert-binary-tree/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/01/19/easy-226-invert-binary-tree/) |
| 236 | Lowest Common Ancestor | [Link](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/01/19/medium-236-lowest-common-ancestor-of-a-binary-tree/) |
| 437 | Path Sum III | [Link](https://leetcode.com/problems/path-sum-iii/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/10/19/medium-437-path-sum-iii/) |
| 690 | Employee Importance | [Link](https://leetcode.com/problems/employee-importance/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-12-16-medium-690-employee-importance/) |

## DFS with Memoization

DFS with caching to avoid recomputation.

```python
DIRS4 = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def dfs_with_memo(
    matrix: list[list[int]], i: int, j: int, memo: list[list[int]], prev: int
) -> int:
    m, n = len(matrix), len(matrix[0])
    if i < 0 or i >= m or j < 0 or j >= n or matrix[i][j] <= prev:
        return 0
    if memo[i][j] != -1:
        return memo[i][j]
    best = 1
    for di, dj in DIRS4:
        best = max(best, 1 + dfs_with_memo(matrix, i + di, j + dj, memo, matrix[i][j]))
    memo[i][j] = best
    return best

```

| ID | Title | Link | Solution |
|---|---|---|---|
| 329 | Longest Increasing Path in a Matrix | [Link](https://leetcode.com/problems/longest-increasing-path-in-a-matrix/) | - |

## Iterative DFS

DFS using stack instead of recursion.

```python
class TreeNode:
    def __init__(self, val: int = 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def dfs_iterative(graph: list[list[int]], start: int) -> None:
    st: list[int] = [start]
    visited = [False] * len(graph)
    while st:
        node = st.pop()
        if visited[node]:
            continue
        visited[node] = True
        for nei in reversed(graph[node]):
            if not visited[nei]:
                st.append(nei)


def preorder_iterative(root: TreeNode | None) -> list[int]:
    if not root:
        return []
    result: list[int] = []
    st: list[TreeNode] = [root]
    while st:
        node = st.pop()
        result.append(node.val)
        if node.right:
            st.append(node.right)
        if node.left:
            st.append(node.left)
    return result

```

| ID | Title | Link | Solution |
|---|---|---|---|
| 144 | Binary Tree Preorder Traversal | [Link](https://leetcode.com/problems/binary-tree-preorder-traversal/) | - |
| 94 | Binary Tree Inorder Traversal | [Link](https://leetcode.com/problems/binary-tree-inorder-traversal/) | - |

## More templates

- **Graph, Backtracking:** [Graph](/posts/2025-10-29-leetcode-templates-graph/), [Backtracking](/posts/2025-11-24-leetcode-templates-backtracking/)
- **Data structures, Search:** [Data Structures & Core Algorithms](/posts/2025-10-29-leetcode-templates-data-structures/), [Search](/posts/2026-01-20-leetcode-templates-search/)
- **Master index:** [Categories & Templates](/posts/2025-10-29-leetcode-categories-and-templates/)
{% endraw %}

