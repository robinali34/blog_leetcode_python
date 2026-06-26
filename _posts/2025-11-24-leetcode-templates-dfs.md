---
layout: post
title: "Algorithm Templates: DFS"
date: 2025-11-24 00:00:00 -0700
categories: leetcode templates dfs graph
permalink: /posts/2025-11-24-leetcode-templates-dfs/
tags: [leetcode, templates, dfs, graph, traversal]
---

{% raw %}
**Depth-First Search (DFS)** is one of the most fundamental graph traversal algorithms. It works by starting at a node and exploring as far down each branch as possible before backtracking — making it ideal for problems involving reachability, connected components, paths, and tree structure. This page collects ready-to-use C++ templates for the most common DFS patterns you'll encounter on LeetCode. See also [Graph](/posts/2025-10-29-leetcode-templates-graph/) and [Backtracking](/posts/2025-11-24-leetcode-templates-backtracking/).

> **New to DFS?** DFS explores as deep as possible before backtracking. Think of it like exploring a maze — go straight until you hit a dead end, then back up and try the next turn.

<div style="text-align:center; margin: 1.5em 0;">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 310" width="520" height="310" style="max-width:100%;">
  <style>
    .node{fill:#D4D8D0;stroke:#B8B5B0;stroke-width:2}
    .visited{fill:#E8D5D0;stroke:#B8B5B0;stroke-width:2}
    .current{fill:#D4D8E0;stroke:#B8B5B0;stroke-width:2.5}
    .edge{stroke:#B8B5B0;stroke-width:2;fill:none}
    .label{font:bold 14px sans-serif;fill:#3A3530;text-anchor:middle;dominant-baseline:central}
    .order{font:11px sans-serif;fill:#5A5752;text-anchor:middle}
    .title{font:bold 13px sans-serif;fill:#5A5752;text-anchor:middle}
    .stk{fill:#D4D8E0;stroke:#B8B5B0;stroke-width:1.5}
    .stklbl{font:12px monospace;fill:#3A3530;text-anchor:middle;dominant-baseline:central}
  </style>
  <!-- Title -->
  <text x="180" y="18" class="title">DFS Traversal Order</text>
  <!-- Edges -->
  <line x1="180" y1="55" x2="110" y2="115" class="edge"/>
  <line x1="180" y1="55" x2="250" y2="115" class="edge"/>
  <line x1="110" y1="135" x2="65" y2="195" class="edge"/>
  <line x1="110" y1="135" x2="155" y2="195" class="edge"/>
  <line x1="250" y1="135" x2="250" y2="195" class="edge"/>
  <!-- Nodes: visited=E8D5D0, current=D4D8E0 -->
  <circle cx="180" cy="45" r="20" class="visited"/>
  <text x="180" y="45" class="label">1</text>
  <text x="180" y="75" class="order">①</text>
  <circle cx="110" cy="125" r="20" class="visited"/>
  <text x="110" y="125" class="label">2</text>
  <text x="110" y="155" class="order">②</text>
  <circle cx="250" cy="125" r="20" class="node"/>
  <text x="250" y="125" class="label">3</text>
  <text x="250" y="155" class="order">⑤</text>
  <circle cx="65" cy="205" r="20" class="visited"/>
  <text x="65" y="205" class="label">4</text>
  <text x="65" y="235" class="order">③</text>
  <circle cx="155" cy="205" r="20" class="current"/>
  <text x="155" y="205" class="label">5</text>
  <text x="155" y="235" class="order">④</text>
  <circle cx="250" cy="205" r="20" class="node"/>
  <text x="250" y="205" class="label">6</text>
  <text x="250" y="235" class="order">⑥</text>
  <!-- Stack visualization -->
  <text x="420" y="18" class="title">Stack</text>
  <rect x="390" y="28" width="60" height="28" rx="4" class="stk"/>
  <text x="420" y="42" class="stklbl">3</text>
  <rect x="390" y="60" width="60" height="28" rx="4" class="stk"/>
  <text x="420" y="74" class="stklbl">5 ←</text>
  <text x="420" y="108" class="order">top of stack</text>
  <!-- Legend -->
  <rect x="360" y="145" width="16" height="16" rx="3" class="visited"/>
  <text x="385" y="155" style="font:12px sans-serif;fill:#5A5752" dominant-baseline="central">Visited</text>
  <rect x="360" y="170" width="16" height="16" rx="3" class="current"/>
  <text x="385" y="180" style="font:12px sans-serif;fill:#5A5752" dominant-baseline="central">Processing</text>
  <rect x="360" y="195" width="16" height="16" rx="3" class="node"/>
  <text x="385" y="205" style="font:12px sans-serif;fill:#5A5752" dominant-baseline="central">Unvisited</text>
  <!-- Arrow showing the "go deep" path -->
  <text x="420" y="260" class="order">DFS goes deep</text>
  <text x="420" y="278" class="order">before going wide</text>
</svg>
</div>

## Contents

- [Basic DFS](#basic-dfs)
- [DFS on Grid](#dfs-on-grid)
- [DFS on Tree](#dfs-on-tree)
- [DFS with Memoization](#dfs-with-memoization)
- [Iterative DFS](#iterative-dfs)

## Basic DFS

Depth-First Search explores as far as possible before backtracking.

**When to use:** Checking reachability between nodes, finding connected components, or exploring all paths in a general graph.

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

| ID | Title | Link | Solution |
|---|---|---|---|
| 841 | Keys and Rooms | [Link](https://leetcode.com/problems/keys-and-rooms/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2026/03/12/medium-841-keys-and-rooms/) |

## DFS on Grid

DFS for 2D grid problems (connected components, paths).

**When to use:** Flood-fill problems, island counting, or any task where you explore connected cells in a 2D matrix.

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
| 200 | Number of Islands | [Link](https://leetcode.com/problems/number-of-islands/) | [Solution](https://robinali34.github.io/blog_leetcode_python/posts/2025-11-20-medium-200-number-of-islands/) |
| 79 | Word Search | [Link](https://leetcode.com/problems/word-search/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2026/01/12/medium-79-word-search/) |
| 695 | Max Area of Island | [Link](https://leetcode.com/problems/max-area-of-island/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2025/10/20/medium-695-max-area-of-island/) |
| 133 | Clone Graph | [Link](https://leetcode.com/problems/clone-graph/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2025/10/20/medium-133-clone-graph/) |
| 417 | Pacific Atlantic Water Flow | [Link](https://leetcode.com/problems/pacific-atlantic-water-flow/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2025/10/19/medium-417-pacific-atlantic-water-flow/) |
| 323 | Number of Connected Components | [Link](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2026/01/07/medium-323-number-of-connected-components-in-an-undirected-graph/) |
| 547 | Number of Provinces | [Link](https://leetcode.com/problems/number-of-provinces/) | [Solution](https://robinali34.github.io/blog_leetcode_python/posts/2025-12-18-medium-547-number-of-provinces/) |

## DFS on Tree

DFS for tree problems (preorder, inorder, postorder).

**When to use:** Tree traversals, path-sum problems, computing tree height/diameter, or any recursive tree decomposition.

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
| 100 | Same Tree | [Link](https://leetcode.com/problems/same-tree/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2026/01/19/easy-100-same-tree/) |
| 101 | Symmetric Tree | [Link](https://leetcode.com/problems/symmetric-tree/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2026/01/19/easy-101-symmetric-tree/) |
| 104 | Maximum Depth of Binary Tree | [Link](https://leetcode.com/problems/maximum-depth-of-binary-tree/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2026/01/19/easy-104-maximum-depth-of-binary-tree/) |
| 111 | Minimum Depth of Binary Tree | [Link](https://leetcode.com/problems/minimum-depth-of-binary-tree/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2026/01/19/easy-111-minimum-depth-of-binary-tree/) |
| 112 | Path Sum | [Link](https://leetcode.com/problems/path-sum/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2026/01/19/easy-112-path-sum/) |
| 129 | Sum Root to Leaf Numbers | [Link](https://leetcode.com/problems/sum-root-to-leaf-numbers/) | [Solution](https://robinali34.github.io/blog_leetcode_python/posts/2025-11-24-medium-129-sum-root-to-leaf-numbers/) |
| 226 | Invert Binary Tree | [Link](https://leetcode.com/problems/invert-binary-tree/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2026/01/19/easy-226-invert-binary-tree/) |
| 236 | Lowest Common Ancestor | [Link](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2026/01/19/medium-236-lowest-common-ancestor-of-a-binary-tree/) |
| 437 | Path Sum III | [Link](https://leetcode.com/problems/path-sum-iii/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2025/10/19/medium-437-path-sum-iii/) |
| 690 | Employee Importance | [Link](https://leetcode.com/problems/employee-importance/) | [Solution](https://robinali34.github.io/blog_leetcode_python/posts/2025-12-16-medium-690-employee-importance/) |

## DFS with Memoization

DFS with caching to avoid recomputation.

**When to use:** Problems with overlapping subproblems on graphs or grids, such as longest increasing path or counting distinct paths.

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
| 329 | Longest Increasing Path in a Matrix | [Link](https://leetcode.com/problems/longest-increasing-path-in-a-matrix/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2026/04/18/hard-329-longest-increasing-path-in-a-matrix/) |

## Iterative DFS

DFS using stack instead of recursion.

**When to use:** When the recursion depth might cause a stack overflow, or when you need explicit control over the traversal order.

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

## Pattern Comparison

| Pattern | When to Use | Time | Space |
|---|---|---|---|
| Basic DFS | Reachability, connected components | O(V+E) | O(V) |
| Grid DFS | Flood fill, island counting | O(M×N) | O(M×N) |
| Tree DFS | All tree traversals, path problems | O(N) | O(H) |
| DFS + Memo | Overlapping subproblems on graphs/grids | O(States) | O(States) |
| Iterative | When recursion stack overflows | O(V+E) | O(V) |

## DFS vs BFS

> **When should you pick DFS over BFS (or vice versa)?**
>
> - **Use DFS** when you need to explore all paths, check connectivity, detect cycles, or solve problems that decompose recursively (e.g., tree shape, backtracking). DFS is also more memory-efficient on narrow/deep structures.
> - **Use BFS** when you need the **shortest path in an unweighted graph**, want to process nodes level by level, or need the minimum number of steps to reach a target.
> - **Rule of thumb:** If the problem says "shortest" or "minimum steps," reach for BFS. If it says "all paths," "connected," or "exists," DFS is usually the natural fit.

## More templates

- **Graph, Backtracking:** [Graph](/posts/2025-10-29-leetcode-templates-graph/), [Backtracking](/posts/2025-11-24-leetcode-templates-backtracking/)
- **Data structures, Search:** [Data Structures & Core Algorithms](/posts/2025-10-29-leetcode-templates-data-structures/), [Search](/posts/2026-01-20-leetcode-templates-search/)
- **Beginner's Guide:** [LeetCode Beginner's Guide](/2026/06/25/leetcode-beginners-guide/)
- **Master index:** [Categories & Templates](/posts/2025-10-29-leetcode-categories-and-templates/)
{% endraw %}

