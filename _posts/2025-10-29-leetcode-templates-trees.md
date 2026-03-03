---
layout: post
title: "LeetCode Templates: Trees"
date: 2025-10-29 00:00:00 -0700
categories: [leetcode, templates, trees]
permalink: /posts/2025-10-29-leetcode-templates-trees/
tags: [leetcode, templates, trees]
---

## Contents

- [How to Analyze Tree Problems](#how-to-analyze-tree-problems)
- [Traversals (iterative)](#traversals-iterative)
- [LCA (Binary Lifting)](#lca-binary-lifting)
- [HLD (Heavy-Light Decomposition)](#hld-heavy-light-decomposition-skeleton)

## How to Analyze Tree Problems

1. **Rooting and parent relation**
   - Most algorithms become easier after fixing a root and parent array.

2. **Query type**
   - single traversal output -> DFS/BFS
   - ancestor queries -> LCA
   - path queries with updates -> HLD + segment tree/Fenwick

3. **Constraints**
   - one query vs many queries changes preferred preprocessing.

4. **Complexity planning**
   - traversal `O(n)`
   - binary lifting preprocess `O(n log n)`, query `O(log n)`
   - HLD path decomposition `O(log^2 n)` with segment tree

## Traversals (iterative)

```python
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorder(root: Optional[TreeNode]) -> list[int]:
    ans = []
    st = []
    cur = root
    while cur or st:
        while cur:
            st.append(cur)
            cur = cur.left
        cur = st.pop()
        ans.append(cur.val)
        cur = cur.right
    return ans


def level_order(root: Optional[TreeNode]) -> list[list[int]]:
    if not root:
        return []
    res = []
    q = deque([root])
    while q:
        sz = len(q)
        level = []
        for _ in range(sz):
            u = q.popleft()
            level.append(u.val)
            if u.left:
                q.append(u.left)
            if u.right:
                q.append(u.right)
        res.append(level)
    return res
```

| ID | Title | Link |
|---|---|---|
| 94 | Binary Tree Inorder Traversal | [Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/) |
| 102 | Binary Tree Level Order Traversal | [Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/) |

## LCA (Binary Lifting)

```python
def build_lca(g: list[list[int]], root: int = 0):
    n = len(g)
    LOG = (n - 1).bit_length()
    up = [[-1] * LOG for _ in range(n)]
    depth = [0] * n

    def dfs(u: int, p: int) -> None:
        up[u][0] = p
        for k in range(1, LOG):
            prev = up[u][k - 1]
            up[u][k] = -1 if prev == -1 else up[prev][k - 1]
        for v in g[u]:
            if v == p:
                continue
            depth[v] = depth[u] + 1
            dfs(v, u)

    dfs(root, -1)

    def lift(u: int, d: int) -> int:
        for k in range(LOG):
            if (d >> k) & 1:
                u = up[u][k]
                if u == -1:
                    break
        return u

    def lca(a: int, b: int) -> int:
        if depth[a] < depth[b]:
            a, b = b, a
        a = lift(a, depth[a] - depth[b])
        if a == b:
            return a
        for k in range(LOG - 1, -1, -1):
            if up[a][k] != up[b][k]:
                a = up[a][k]
                b = up[b][k]
        return up[a][0]

    return lca, depth, up
```

| ID | Title | Link |
|---|---|---|
| 236 | Lowest Common Ancestor of a Binary Tree | [Lowest Common Ancestor of a Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/) |
| 235 | Lowest Common Ancestor of a BST | [Lowest Common Ancestor of a BST](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/) |

## HLD (Heavy-Light Decomposition) skeleton

```python
def hld_build(g: list[list[int]], root: int = 0):
    n = len(g)
    parent = [-1] * n
    depth = [0] * n
    size = [0] * n
    heavy = [-1] * n
    head = [0] * n
    pos = [0] * n
    cur = 0

    def dfs1(u: int, p: int) -> int:
        parent[u] = p
        size[u] = 1
        best = 0
        for v in g[u]:
            if v == p:
                continue
            depth[v] = depth[u] + 1
            s = dfs1(v, u)
            size[u] += s
            if s > best:
                best = s
                heavy[u] = v
        return size[u]

    def dfs2(u: int, h: int) -> None:
        nonlocal cur
        head[u] = h
        pos[u] = cur
        cur += 1
        if heavy[u] != -1:
            dfs2(heavy[u], h)
        for v in g[u]:
            if v != parent[u] and v != heavy[u]:
                dfs2(v, v)

    dfs1(root, -1)
    dfs2(root, root)
    return parent, depth, size, heavy, head, pos
```

> Note: HLD appears less often in LeetCode, but the decomposition pattern is useful for advanced tree path queries.

