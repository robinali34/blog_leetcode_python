---
layout: post
title: "LeetCode Templates: Trees"
date: 2025-10-29 00:00:00 -0700
categories: leetcode templates trees
permalink: /posts/2025-10-29-leetcode-templates-trees/
tags: [leetcode, templates, trees]
---

## Contents

- [Traversals (iterative)](#traversals-iterative)
- [LCA (Binary Lifting)](#lca-binary-lifting)
- [HLD (Heavy-Light Decomposition)](#hld-heavy-light-decomposition-skeleton)

## Traversals (iterative)

```python
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
```

```python
from collections import deque

def level_order(root: Optional[TreeNode]) -> list[list[int]]:
    if not root:
        return []
    res = []
    q = deque([root])
    while q:
        sz = len(q)
        res.append([])
        for _ in range(sz):
            u = q.popleft()
            res[-1].append(u.val)
            if u.left:
                q.append(u.left)
            if u.right:
                q.append(u.right)
    return res
```

| ID | Title | Link |
|---|---|---|
| 94 | Binary Tree Inorder Traversal | [Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/) |
| 102 | Binary Tree Level Order Traversal | [Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/) |

## LCA (Binary Lifting)

```python
K = 17
depth = []
up = []  # up[u][k] = 2^k-th ancestor of u

def dfs_lift(u: int, p: int, g: list[list[int]]):
    up[u][0] = p
    for k in range(1, K + 1):
        up[u][k] = -1 if up[u][k-1] < 0 else up[up[u][k-1]][k-1]
    for v in g[u]:
        if v != p:
            depth[v] = depth[u] + 1
            dfs_lift(v, u, g)

def lift(u: int, k: int) -> int:
    for i in range(K + 1):
        if k & (1 << i):
            u = -1 if u < 0 else up[u][i]
    return u

def lca(a: int, b: int) -> int:
    if depth[a] < depth[b]:
        a, b = b, a
    a = lift(a, depth[a] - depth[b])
    if a == b:
        return a
    for i in range(K, -1, -1):
        if up[a][i] != up[b][i]:
            a = up[a][i]
            b = up[b][i]
    return up[a][0]
```

| ID | Title | Link |
|---|---|---|
| 236 | Lowest Common Ancestor of a Binary Tree | [Lowest Common Ancestor of a Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/) |
| 235 | Lowest Common Ancestor of a BST | [Lowest Common Ancestor of a BST](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/) |

## HLD (Heavy-Light Decomposition) skeleton

```python
N = 200000
g_h = [[] for _ in range(N)]
sz_h = [0] * N
par_h = [0] * N
dep_h = [0] * N
heavy_h = [-1] * N
head_h = [0] * N
in_h = [0] * N
cur_t = 0

def dfs1(u: int, p: int) -> int:
    global cur_t
    par_h[u] = p
    dep_h[u] = 0 if p == -1 else dep_h[p] + 1
    sz_h[u] = 1
    heavy_h[u] = -1
    best = 0
    for v in g_h[u]:
        if v != p:
            s = dfs1(v, u)
            sz_h[u] += s
            if s > best:
                best = s
                heavy_h[u] = v
    return sz_h[u]

def dfs2(u: int, h: int):
    global cur_t
    head_h[u] = h
    in_h[u] = cur_t
    cur_t += 1
    if heavy_h[u] != -1:
        dfs2(heavy_h[u], h)
        for v in g_h[u]:
            if v != par_h[u] and v != heavy_h[u]:
                dfs2(v, v)
```

> Note: HLD is rarely required on LeetCode.
