---
layout: post
title: "Algorithm Templates: DFS"
date: 2025-11-24 00:00:00 -0700
categories: leetcode templates dfs graph
permalink: /posts/2025-11-24-leetcode-templates-dfs/
tags: [leetcode, templates, dfs, graph, traversal]
---

{% raw %}
Minimal, copy-paste C++ for graph DFS, grid DFS, tree DFS, memoization, and iterative DFS. See also [Graph](/posts/2025-10-29-leetcode-templates-graph/) and [Backtracking](/posts/2025-11-24-leetcode-templates-backtracking/).

## Contents

- [Basic DFS](#basic-dfs)
- [DFS on Grid](#dfs-on-grid)
- [DFS on Tree](#dfs-on-tree)
- [DFS with Memoization](#dfs-with-memoization)
- [Iterative DFS](#iterative-dfs)

## Basic DFS

Depth-First Search explores as far as possible before backtracking.

```python
// DFS on graph (adjacency list)
def dfs(self, graph, node, visited):
    visited[node] = True
    // Process node
    cout << node << " "
    // Explore neighbors
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited)
// DFS with return value
def dfs(self, graph, node, target, visited):
    if (node == target) return True
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]  and  dfs(graph, neighbor, target, visited):
            return True
    return False
```

## DFS on Grid

DFS for 2D grid problems (connected components, paths).

```python
// DFS on 2D grid (4-directional)
def dfsGrid(self, grid, i, j):
    m = len(grid), n = grid[0].__len__()
    if i < 0  or  i >= m  or  j < 0  or  j >= n  or  grid[i][j] != '1':
        return
    grid[i][j] = '0' // Mark as visited
    // Explore 4 directions
    dfsGrid(grid, i + 1, j)
    dfsGrid(grid, i - 1, j)
    dfsGrid(grid, i, j + 1)
    dfsGrid(grid, i, j - 1)
// Number of Islands using DFS
def numIslands(self, grid):
    m = len(grid), n = grid[0].__len__()
    count = 0
    for (i = 0 i < m i += 1) :
    for (j = 0 j < n j += 1) :
    if grid[i][j] == '1':
        count += 1
        dfsGrid(grid, i, j)
return count
// Word Search
def dfsWordSearch(self, board, i, j, word, idx):
    if (idx == len(word)) return True
    if (i < 0  or  i >= len(board)  or  j < 0  or  j >= board[0].__len__()) return False
    if (board[i][j] != word[idx]) return False
    char temp = board[i][j]
    board[i][j] = '#' // Mark as visited
    list[pair<int, int>> dirs = \:\:0,1\, \:0,-1\, \:1,0\, \:-1,0\\
for ([dx, dy] : dirs) :
if dfsWordSearch(board, i + dx, j + dy, word, idx + 1):
    return True
board[i][j] = temp // Backtrack
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
// Preorder DFS
def preorder(self, root, result):
    if (not root) return
    result.append(root.val)
    preorder(root.left, result)
    preorder(root.right, result)
// Inorder DFS
def inorder(self, root, result):
    if (not root) return
    inorder(root.left, result)
    result.append(root.val)
    inorder(root.right, result)
// Postorder DFS
def postorder(self, root, result):
    if (not root) return
    postorder(root.left, result)
    postorder(root.right, result)
    result.append(root.val)
// Path Sum
def hasPathSum(self, root, targetSum):
    if (not root) return False
    if not root.left  and  not root.right:
        return root.val == targetSum
    return hasPathSum(root.left, targetSum - root.val)  or
    hasPathSum(root.right, targetSum - root.val)
// Sum Root to Leaf Numbers
def sumNumbers(self, root, 0):
    if (not root) return 0
    sum = sum  10 + root.val
    if (not root.left  and  not root.right) return sum
    return sumNumbers(root.left, sum) + sumNumbers(root.right, sum)
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
// DFS with memoization (e.g., Longest Increasing Path)
dfsWithMemo(list[list[int>> matrix, i, j,
list[list[int>> memo, prev) :
m = len(matrix), n = matrix[0].__len__()
if i < 0  or  i >= m  or  j < 0  or  j >= n  or  matrix[i][j] <= prev:
    return 0
if memo[i][j] != -1:
    return memo[i][j]
result = 1
list[pair<int, int>> dirs = \:\:0,1\, \:0,-1\, \:1,0\, \:-1,0\\
for ([dx, dy] : dirs) :
result = max(result, 1 + dfsWithMemo(matrix, i + dx, j + dy,
memo, matrix[i][j]))
memo[i][j] = result
return result
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 329 | Longest Increasing Path in a Matrix | [Link](https://leetcode.com/problems/longest-increasing-path-in-a-matrix/) | - |

## Iterative DFS

DFS using stack instead of recursion.

```python
// Iterative DFS on graph
def dfsIterative(self, graph, start):
    list[int> st
    list[bool> visited(len(graph), False)
    st.push(start)
    while not not st:
        node = st.top()
        st.pop()
        if (visited[node]) continue
        visited[node] = True
        // Process node
        cout << node << " "
        // Push neighbors in reverse order to maintain order
        for (i = graph[node].__len__() - 1 i >= 0 i -= 1) :
        if not visited[graph[node][i]]:
            st.push(graph[node][i])
// Iterative DFS on tree
def preorderIterative(self, root):
    list[int> result
    if (not root) return result
    list[TreeNode> st
    st.push(root)
    while not not st:
        TreeNode node = st.top()
        st.pop()
        result.append(node.val)
        if node.right) st.push(node.right:
        if node.left) st.push(node.left:
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

