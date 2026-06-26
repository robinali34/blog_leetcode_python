---
layout: post
title: "Algorithm Templates: Trees"
date: 2025-10-29 00:00:00 -0700
categories: leetcode templates trees
permalink: /posts/2025-10-29-leetcode-templates-trees/
tags: [leetcode, templates, trees]
---

{% raw %}
Trees are one of the most frequently tested data structures in coding interviews. This page collects ready-to-use C++ templates for every major tree pattern — from basic traversals to advanced structures like segment trees and heavy-light decomposition. Each section includes the core template, guidance on when to reach for it, and curated practice problems.

> **New to Trees?** A tree is a connected graph with no cycles. Binary trees (each node has at most 2 children) are the most common in interviews. The key insight: most tree problems are solved with recursion — process the current node, then recurse on left and right.

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 340" style="max-width:520px;margin:1em auto;display:block">
  <style>
    .nd{fill:#C9B1BD;stroke:#8E9AAF;stroke-width:2}
    .eg{stroke:#8E9AAF;stroke-width:2}
    .vl{font:bold 16px sans-serif;fill:#3D3535;text-anchor:middle;dominant-baseline:central}
    .lb{font:13px sans-serif;fill:#6B5B6B;text-anchor:middle}
    .tv{font:12px monospace;fill:#3D3535}
    .tl{font:bold 12px sans-serif;fill:#8E7E6E}
  </style>
  <line class="eg" x1="260" y1="50" x2="140" y2="130"/>
  <line class="eg" x1="260" y1="50" x2="380" y2="130"/>
  <line class="eg" x1="140" y1="130" x2="80" y2="210"/>
  <line class="eg" x1="380" y1="130" x2="440" y2="210"/>
  <circle class="nd" cx="260" cy="50" r="24"/>
  <text class="vl" x="260" y="50">1</text>
  <circle class="nd" cx="140" cy="130" r="24"/>
  <text class="vl" x="140" y="130">2</text>
  <circle class="nd" cx="380" cy="130" r="24"/>
  <text class="vl" x="380" y="130">3</text>
  <circle class="nd" cx="80" cy="210" r="24" style="fill:#A8B5A2"/>
  <text class="vl" x="80" y="210">4</text>
  <circle class="nd" cx="440" cy="210" r="24" style="fill:#A8B5A2"/>
  <text class="vl" x="440" y="210">5</text>
  <text class="lb" x="260" y="16" style="fill:#C4956A;font-weight:bold">root</text>
  <text class="lb" x="88" y="128">left child</text>
  <text class="lb" x="440" y="105">right child</text>
  <text class="lb" x="80" y="246">leaf</text>
  <text class="lb" x="440" y="246">leaf</text>
  <text class="tl" x="40" y="280">Preorder:</text>
  <text class="tv" x="120" y="280">1 → 2 → 4 → 3 → 5  (root, left, right)</text>
  <text class="tl" x="40" y="300">Inorder:</text>
  <text class="tv" x="120" y="300">4 → 2 → 1 → 3 → 5  (left, root, right)</text>
  <text class="tl" x="40" y="320">Postorder:</text>
  <text class="tv" x="120" y="320">4 → 2 → 5 → 3 → 1  (left, right, root)</text>
</svg>

## Contents

- [Traversals (iterative)](#traversals-iterative)
- [Tree DFS Patterns](#tree-dfs-patterns)
  - [Pattern 1: Basic Tree Traversal (DFS)](#pattern-1-basic-tree-traversal-dfs)
  - [Pattern 2: DFS with Return Value (Bottom-Up)](#pattern-2-dfs-with-return-value-bottom-up)
  - [Pattern 3: DFS with Global Result](#pattern-3-dfs-with-global-result)
  - [Pattern 4: Root-to-Leaf Path Tracking](#pattern-4-root-to-leaf-path-tracking)
  - [Pattern 5: BFS / Level Order Traversal](#pattern-5-bfs--level-order-traversal)
  - [Pattern 6: Lowest Common Ancestor (LCA)](#pattern-6-lowest-common-ancestor-lca)
  - [Pattern 7: Binary Search Tree (BST) Pattern](#pattern-7-binary-search-tree-bst-pattern)
  - [Practice Roadmap](#practice-roadmap)
- [LCA (Binary Lifting)](#lca-binary-lifting)
- [Segment Tree](#segment-tree)
- [Binary Search on Segment Tree (Tree Walking)](#binary-search-on-segment-tree-tree-walking)
- [Fenwick Tree (Binary Indexed Tree)](#fenwick-tree-binary-indexed-tree)
- [HLD (Heavy-Light Decomposition)](#hld-heavy-light-decomposition-skeleton)

## Traversals (iterative)

**When to use:** You need to visit every node in a specific order — inorder for sorted BST output, level-order for layer-by-layer processing.

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

| ID | Title | Link | Solution |
|---|---|---|---|
| 94 | Binary Tree Inorder Traversal | [Link](https://leetcode.com/problems/binary-tree-inorder-traversal/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2026/03/06/easy-94-binary-tree-inorder-traversal/) |
| 144 | Binary Tree Preorder Traversal | [Link](https://leetcode.com/problems/binary-tree-preorder-traversal/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2026/03/06/easy-144-binary-tree-preorder-traversal/) |
| 145 | Binary Tree Postorder Traversal | [Link](https://leetcode.com/problems/binary-tree-postorder-traversal/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2026/03/06/easy-145-binary-tree-postorder-traversal/) |
| 102 | Binary Tree Level Order Traversal | [Link](https://leetcode.com/problems/binary-tree-level-order-traversal/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2026/01/07/medium-102-binary-tree-level-order-traversal/) |
| 103 | Binary Tree Zigzag Level Order Traversal | [Link](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2026/01/06/medium-103-binary-tree-zigzag-level-order-traversal/) |
| 429 | N-ary Tree Level Order Traversal | [Link](https://leetcode.com/problems/n-ary-tree-level-order-traversal/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2026/01/07/medium-429-n-ary-tree-level-order-traversal/) |
| 314 | Binary Tree Vertical Order Traversal | [Link](https://leetcode.com/problems/binary-tree-vertical-order-traversal/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2025/10/20/medium-314-binary-tree-vertical-order-traversal/) |

## Tree DFS Patterns

Recognizing the right tree pattern quickly is key. Below are the 7 core patterns that cover nearly all tree DFS problems.

---

### Pattern 1: Basic Tree Traversal (DFS)

**When to use:** Simple traversal, count nodes, check a property on every node.

Traverse the tree using DFS. Most problems reduce to choosing **when** to process the node.

```
Preorder  : root → left → right
Inorder   : left → root → right
Postorder : left → right → root
```

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

| ID | Title | Link | Solution |
|---|---|---|---|
| 144 | Binary Tree Preorder Traversal | [Link](https://leetcode.com/problems/binary-tree-preorder-traversal/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2026/03/06/easy-144-binary-tree-preorder-traversal/) |
| 94 | Binary Tree Inorder Traversal | [Link](https://leetcode.com/problems/binary-tree-inorder-traversal/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2026/03/06/easy-94-binary-tree-inorder-traversal/) |
| 145 | Binary Tree Postorder Traversal | [Link](https://leetcode.com/problems/binary-tree-postorder-traversal/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2026/03/06/easy-145-binary-tree-postorder-traversal/) |
| 104 | Maximum Depth of Binary Tree | [Link](https://leetcode.com/problems/maximum-depth-of-binary-tree/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2026/01/19/easy-104-maximum-depth-of-binary-tree/) |

---

### Pattern 2: DFS with Return Value (Bottom-Up)

**When to use:** Height, diameter, balanced check — any problem where the answer depends on information from both subtrees.

Each recursive call returns information about its subtree. Process children first, then combine results and return upward. Used for: height, balance, diameter, subtree properties.

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 270" style="max-width: 100%; height: auto; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;">
  <text x="340" y="16" text-anchor="middle" fill="#5A5752" font-size="13" font-weight="bold">Computing Max Depth — values return upward</text>
  <!-- tree edges -->
  <line x1="340" y1="50" x2="190" y2="130" stroke="#B8B5B0" stroke-width="2"/>
  <line x1="340" y1="50" x2="490" y2="130" stroke="#B8B5B0" stroke-width="2"/>
  <line x1="190" y1="130" x2="110" y2="210" stroke="#B8B5B0" stroke-width="2"/>
  <line x1="190" y1="130" x2="270" y2="210" stroke="#B8B5B0" stroke-width="2"/>
  <!-- return value pills on edges (child → parent) -->
  <rect x="133" y="160" width="36" height="18" rx="9" fill="#F0EBE6" stroke="#B8B5B0" stroke-width="1"/>
  <text x="151" y="173" text-anchor="middle" fill="#5A5752" font-size="10" font-weight="bold">↑ 0</text>
  <rect x="213" y="160" width="36" height="18" rx="9" fill="#F0EBE6" stroke="#B8B5B0" stroke-width="1"/>
  <text x="231" y="173" text-anchor="middle" fill="#5A5752" font-size="10" font-weight="bold">↑ 0</text>
  <rect x="243" y="78" width="36" height="18" rx="9" fill="#E8E3D8" stroke="#B8B5B0" stroke-width="1"/>
  <text x="261" y="91" text-anchor="middle" fill="#3A3530" font-size="10" font-weight="bold">↑ 1</text>
  <rect x="398" y="78" width="36" height="18" rx="9" fill="#F0EBE6" stroke="#B8B5B0" stroke-width="1"/>
  <text x="416" y="91" text-anchor="middle" fill="#5A5752" font-size="10" font-weight="bold">↑ 0</text>
  <!-- nodes -->
  <circle cx="340" cy="50" r="22" fill="#E8D5D0" stroke="#8B8680" stroke-width="2"/>
  <text x="340" y="51" text-anchor="middle" dominant-baseline="central" fill="#3A3530" font-size="15" font-weight="bold">1</text>
  <circle cx="190" cy="130" r="22" fill="#D4D8E0" stroke="#B8B5B0" stroke-width="2"/>
  <text x="190" y="131" text-anchor="middle" dominant-baseline="central" fill="#3A3530" font-size="15" font-weight="bold">2</text>
  <circle cx="490" cy="130" r="22" fill="#D4D8D0" stroke="#B8B5B0" stroke-width="2"/>
  <text x="490" y="131" text-anchor="middle" dominant-baseline="central" fill="#3A3530" font-size="15" font-weight="bold">3</text>
  <circle cx="110" cy="210" r="22" fill="#E8E3D8" stroke="#B8B5B0" stroke-width="2"/>
  <text x="110" y="211" text-anchor="middle" dominant-baseline="central" fill="#3A3530" font-size="15" font-weight="bold">4</text>
  <circle cx="270" cy="210" r="22" fill="#E8E3D8" stroke="#B8B5B0" stroke-width="2"/>
  <text x="270" y="211" text-anchor="middle" dominant-baseline="central" fill="#3A3530" font-size="15" font-weight="bold">5</text>
  <!-- computation annotations -->
  <text x="340" y="28" text-anchor="middle" fill="#3A3530" font-size="11" font-weight="bold">1 + max(1, 0) = 2</text>
  <text x="190" y="164" text-anchor="middle" fill="#5A5752" font-size="10">1+max(0,0) = 1</text>
  <text x="490" y="160" text-anchor="middle" fill="#7A7772" font-size="10">leaf → 0</text>
  <text x="110" y="242" text-anchor="middle" fill="#7A7772" font-size="10">leaf → 0</text>
  <text x="270" y="242" text-anchor="middle" fill="#7A7772" font-size="10">leaf → 0</text>
  <!-- legend -->
  <rect x="530" y="200" width="140" height="50" rx="6" fill="#FAF8F5" stroke="#B8B5B0" stroke-width="1"/>
  <text x="600" y="219" text-anchor="middle" fill="#3A3530" font-size="12" font-weight="bold">Result: depth = 2</text>
  <rect x="545" y="228" width="28" height="14" rx="7" fill="#F0EBE6" stroke="#B8B5B0" stroke-width="1"/>
  <text x="559" y="239" text-anchor="middle" fill="#5A5752" font-size="8" font-weight="bold">↑ n</text>
  <text x="578" y="239" fill="#7A7772" font-size="10">return value</text>
</svg>

```python
def dfs(node):
    if not node:
        return 0
    left = dfs(node.left)
    right = dfs(node.right)
    return combine(left, right, node)
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 104 | Maximum Depth of Binary Tree | [Link](https://leetcode.com/problems/maximum-depth-of-binary-tree/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2026/01/19/easy-104-maximum-depth-of-binary-tree/) |
| 110 | Balanced Binary Tree | [Link](https://leetcode.com/problems/balanced-binary-tree/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2026/03/06/easy-110-balanced-binary-tree/) |
| 543 | Diameter of Binary Tree | [Link](https://leetcode.com/problems/diameter-of-binary-tree/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2026/03/06/easy-543-diameter-of-binary-tree/) |
| 124 | Binary Tree Maximum Path Sum | [Link](https://leetcode.com/problems/binary-tree-maximum-path-sum/) | - |
| 1376 | Time Needed to Inform All Employees | [Link](https://leetcode.com/problems/time-needed-to-inform-all-employees/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2026/03/17/medium-1376-time-needed-to-inform-all-employees/) |

---

### Pattern 3: DFS with Global Result

**When to use:** Max path sum, longest path — the optimal answer may span across left and right subtrees, but each recursive call can only return one branch upward.

While traversing, update a **global variable** tracking the best result. The recursive function returns a per-node value, but the answer lives outside the recursion.

```python
result = float("-inf")


def dfs(node):
    global result
    if not node:
        return 0
    left = max(0, dfs(node.left))
    right = max(0, dfs(node.right))
    result = max(result, left + right + node.val)
    return node.val + max(left, right)
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 543 | Diameter of Binary Tree | [Link](https://leetcode.com/problems/diameter-of-binary-tree/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2026/03/06/easy-543-diameter-of-binary-tree/) |
| 124 | Binary Tree Maximum Path Sum | [Link](https://leetcode.com/problems/binary-tree-maximum-path-sum/) | - |
| 1448 | Count Good Nodes in Binary Tree | [Link](https://leetcode.com/problems/count-good-nodes-in-binary-tree/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2026/03/18/medium-1448-count-good-nodes-in-binary-tree/) |

---

### Pattern 4: Root-to-Leaf Path Tracking

**When to use:** Root-to-leaf paths, path sum collection — any problem that needs the full path from root to the current node.

Maintain a path from root to the current node. **Push → recurse → pop** (backtracking). Used for returning paths, validating sequences, and path sum collection.

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 265" style="max-width: 100%; height: auto; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;">
  <text x="350" y="16" text-anchor="middle" fill="#5A5752" font-size="13" font-weight="bold">Path Tracking — collecting root-to-leaf path [1→2→4]</text>
  <!-- tree edges (highlighted path in darker stroke) -->
  <line x1="190" y1="50" x2="110" y2="130" stroke="#8B8680" stroke-width="3"/>
  <line x1="110" y1="130" x2="60" y2="210" stroke="#8B8680" stroke-width="3"/>
  <line x1="190" y1="50" x2="270" y2="130" stroke="#B8B5B0" stroke-width="1.5"/>
  <line x1="110" y1="130" x2="160" y2="210" stroke="#B8B5B0" stroke-width="1.5"/>
  <!-- nodes (highlighted path = warm fill, others = neutral) -->
  <circle cx="190" cy="50" r="22" fill="#E8D5D0" stroke="#8B8680" stroke-width="2"/>
  <text x="190" y="51" text-anchor="middle" dominant-baseline="central" fill="#3A3530" font-size="15" font-weight="bold">1</text>
  <circle cx="110" cy="130" r="22" fill="#E8D5D0" stroke="#8B8680" stroke-width="2"/>
  <text x="110" y="131" text-anchor="middle" dominant-baseline="central" fill="#3A3530" font-size="15" font-weight="bold">2</text>
  <circle cx="270" cy="130" r="22" fill="#D4D8E0" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="270" y="131" text-anchor="middle" dominant-baseline="central" fill="#3A3530" font-size="15" font-weight="bold">3</text>
  <circle cx="60" cy="210" r="22" fill="#E8D5D0" stroke="#8B8680" stroke-width="2"/>
  <text x="60" y="211" text-anchor="middle" dominant-baseline="central" fill="#3A3530" font-size="15" font-weight="bold">4</text>
  <text x="60" y="242" text-anchor="middle" fill="#5A5752" font-size="10" font-weight="bold">✓ leaf</text>
  <circle cx="160" cy="210" r="22" fill="#D4D8E0" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="160" y="211" text-anchor="middle" dominant-baseline="central" fill="#3A3530" font-size="15" font-weight="bold">5</text>
  <!-- side panel: path tracking steps -->
  <rect x="360" y="30" width="310" height="220" rx="8" fill="#FAF8F5" stroke="#B8B5B0" stroke-width="1"/>
  <text x="515" y="52" text-anchor="middle" fill="#5A5752" font-size="12" font-weight="bold">push → recurse → pop</text>
  <line x1="375" y1="60" x2="655" y2="60" stroke="#B8B5B0" stroke-width="0.5"/>
  <text x="380" y="82" fill="#3A3530" font-size="11" font-weight="bold">push(1)</text>
  <rect x="470" y="68" width="110" height="20" rx="4" fill="#E8D5D0" stroke="#B8B5B0" stroke-width="1"/>
  <text x="525" y="82" text-anchor="middle" fill="#3A3530" font-size="11">path = [1]</text>
  <text x="380" y="110" fill="#3A3530" font-size="11" font-weight="bold">push(2)</text>
  <rect x="470" y="96" width="110" height="20" rx="4" fill="#E8D5D0" stroke="#B8B5B0" stroke-width="1"/>
  <text x="525" y="110" text-anchor="middle" fill="#3A3530" font-size="11">path = [1, 2]</text>
  <text x="380" y="138" fill="#3A3530" font-size="11" font-weight="bold">push(4)</text>
  <rect x="470" y="124" width="110" height="20" rx="4" fill="#E8D5D0" stroke="#B8B5B0" stroke-width="1"/>
  <text x="525" y="138" text-anchor="middle" fill="#3A3530" font-size="11">path = [1, 2, 4]</text>
  <text x="595" y="138" fill="#5A5752" font-size="10" font-weight="bold">✓</text>
  <text x="515" y="162" text-anchor="middle" fill="#5A5752" font-size="11">leaf → result.add([1, 2, 4])</text>
  <line x1="375" y1="172" x2="655" y2="172" stroke="#B8B5B0" stroke-width="0.5"/>
  <text x="380" y="192" fill="#9A9792" font-size="11">pop(4)  →  path = [1, 2]</text>
  <text x="380" y="212" fill="#9A9792" font-size="11">pop(2)  →  path = [1]</text>
  <text x="380" y="232" fill="#7A7772" font-size="10" font-style="italic">backtracking restores path state</text>
</svg>

```python
def dfs(node, path, result):
    if not node:
        return
    path.append(node.val)

    if not node.left and not node.right:
        result.append(path[:])

    dfs(node.left, path, result)
    dfs(node.right, path, result)
    path.pop()
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 112 | Path Sum | [Link](https://leetcode.com/problems/path-sum/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2026/03/06/easy-112-path-sum/) |
| 113 | Path Sum II | [Link](https://leetcode.com/problems/path-sum-ii/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2026/03/06/medium-113-path-sum-ii/) |
| 257 | Binary Tree Paths | [Link](https://leetcode.com/problems/binary-tree-paths/) | - |

---

### Pattern 5: BFS / Level Order Traversal

**When to use:** Level-order, right-side view, zigzag traversal — any problem that processes nodes layer by layer.

Traverse the tree **level by level** using a queue. Used for level processing, shortest depth, and breadth exploration.

```python
from collections import deque


def levelOrder(root):
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
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 102 | Binary Tree Level Order Traversal | [Link](https://leetcode.com/problems/binary-tree-level-order-traversal/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2026/01/07/medium-102-binary-tree-level-order-traversal/) |
| 107 | Binary Tree Level Order Traversal II | [Link](https://leetcode.com/problems/binary-tree-level-order-traversal-ii/) | - |
| 111 | Minimum Depth of Binary Tree | [Link](https://leetcode.com/problems/minimum-depth-of-binary-tree/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2026/01/19/easy-111-minimum-depth-of-binary-tree/) |

---

### Pattern 6: Lowest Common Ancestor (LCA)

**When to use:** Lowest common ancestor — find the deepest node that is an ancestor of both target nodes.

Postorder DFS: if both subtrees contain a target, the current node is the LCA.

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 280" style="max-width: 100%; height: auto; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;">
  <text x="350" y="16" text-anchor="middle" fill="#5A5752" font-size="13" font-weight="bold">Lowest Common Ancestor — p=5, q=1</text>
  <!-- tree edges -->
  <line x1="350" y1="55" x2="200" y2="135" stroke="#B8B5B0" stroke-width="2"/>
  <line x1="350" y1="55" x2="500" y2="135" stroke="#B8B5B0" stroke-width="2"/>
  <line x1="200" y1="135" x2="130" y2="215" stroke="#B8B5B0" stroke-width="1.5"/>
  <line x1="200" y1="135" x2="270" y2="215" stroke="#B8B5B0" stroke-width="1.5"/>
  <line x1="500" y1="135" x2="430" y2="215" stroke="#B8B5B0" stroke-width="1.5"/>
  <line x1="500" y1="135" x2="570" y2="215" stroke="#B8B5B0" stroke-width="1.5"/>
  <!-- LCA node (3) — warm highlight with stronger border -->
  <circle cx="350" cy="55" r="24" fill="#E8D5D0" stroke="#8B8680" stroke-width="2.5"/>
  <text x="350" y="56" text-anchor="middle" dominant-baseline="central" fill="#3A3530" font-size="16" font-weight="bold">3</text>
  <text x="350" y="24" text-anchor="middle" fill="#3A3530" font-size="12" font-weight="bold">★ LCA</text>
  <!-- p node (5) — blue-grey highlight -->
  <circle cx="200" cy="135" r="22" fill="#D4D8E0" stroke="#8B8680" stroke-width="2.5"/>
  <text x="200" y="136" text-anchor="middle" dominant-baseline="central" fill="#3A3530" font-size="15" font-weight="bold">5</text>
  <rect x="217" y="117" width="18" height="16" rx="3" fill="#D4D8E0" stroke="#8B8680" stroke-width="1"/>
  <text x="226" y="129" text-anchor="middle" fill="#3A3530" font-size="10" font-weight="bold">p</text>
  <!-- q node (1) — blue-grey highlight -->
  <circle cx="500" cy="135" r="22" fill="#D4D8E0" stroke="#8B8680" stroke-width="2.5"/>
  <text x="500" y="136" text-anchor="middle" dominant-baseline="central" fill="#3A3530" font-size="15" font-weight="bold">1</text>
  <rect x="517" y="117" width="18" height="16" rx="3" fill="#D4D8E0" stroke="#8B8680" stroke-width="1"/>
  <text x="526" y="129" text-anchor="middle" fill="#3A3530" font-size="10" font-weight="bold">q</text>
  <!-- other nodes — neutral -->
  <circle cx="130" cy="215" r="20" fill="#F0EBE6" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="130" y="216" text-anchor="middle" dominant-baseline="central" fill="#5A5752" font-size="14">6</text>
  <circle cx="270" cy="215" r="20" fill="#F0EBE6" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="270" y="216" text-anchor="middle" dominant-baseline="central" fill="#5A5752" font-size="14">2</text>
  <circle cx="430" cy="215" r="20" fill="#F0EBE6" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="430" y="216" text-anchor="middle" dominant-baseline="central" fill="#5A5752" font-size="14">0</text>
  <circle cx="570" cy="215" r="20" fill="#F0EBE6" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="570" y="216" text-anchor="middle" dominant-baseline="central" fill="#5A5752" font-size="14">8</text>
  <!-- annotations showing how left/right results meet -->
  <rect x="118" y="247" width="116" height="18" rx="4" fill="#E8E3D8" stroke="#B8B5B0" stroke-width="0.5"/>
  <text x="176" y="260" text-anchor="middle" fill="#5A5752" font-size="10">left = found p ✓</text>
  <rect x="440" y="247" width="120" height="18" rx="4" fill="#E8E3D8" stroke="#B8B5B0" stroke-width="0.5"/>
  <text x="500" y="260" text-anchor="middle" fill="#5A5752" font-size="10">right = found q ✓</text>
  <text x="350" y="278" text-anchor="middle" fill="#3A3530" font-size="11" font-weight="bold">left &amp;&amp; right → return root (node 3 is LCA)</text>
</svg>

```python
def lca(root, p, q):
    if not root or root is p or root is q:
        return root
    left = lca(root.left, p, q)
    right = lca(root.right, p, q)
    if left and right:
        return root
    return left if left else right
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 236 | Lowest Common Ancestor of a Binary Tree | [Link](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2026/01/19/medium-236-lowest-common-ancestor-of-a-binary-tree/) |
| 235 | Lowest Common Ancestor of a BST | [Link](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/) | - |

---

### Pattern 7: Binary Search Tree (BST) Pattern

**When to use:** Validate BST, search, insert, delete — any problem that leverages the BST property (`left < root < right`) for pruning or ordered processing.

BST property: `left < root < right`. Inorder traversal produces sorted order. This enables pruning and ordered processing.

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 300" style="max-width: 100%; height: auto; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;">
  <text x="350" y="16" text-anchor="middle" fill="#5A5752" font-size="13" font-weight="bold">Binary Search Tree — left &lt; root &lt; right</text>
  <!-- tree edges -->
  <line x1="350" y1="55" x2="200" y2="135" stroke="#B8B5B0" stroke-width="2"/>
  <line x1="350" y1="55" x2="500" y2="135" stroke="#B8B5B0" stroke-width="2"/>
  <line x1="200" y1="135" x2="120" y2="215" stroke="#B8B5B0" stroke-width="2"/>
  <line x1="200" y1="135" x2="280" y2="215" stroke="#B8B5B0" stroke-width="2"/>
  <line x1="500" y1="135" x2="580" y2="215" stroke="#B8B5B0" stroke-width="2"/>
  <!-- ordering labels on edges -->
  <text x="258" y="86" text-anchor="middle" fill="#9A9792" font-size="13" font-weight="bold">&lt;</text>
  <text x="440" y="86" text-anchor="middle" fill="#9A9792" font-size="13" font-weight="bold">&gt;</text>
  <text x="148" y="170" text-anchor="middle" fill="#9A9792" font-size="13" font-weight="bold">&lt;</text>
  <text x="252" y="170" text-anchor="middle" fill="#9A9792" font-size="13" font-weight="bold">&gt;</text>
  <text x="552" y="170" text-anchor="middle" fill="#9A9792" font-size="13" font-weight="bold">&gt;</text>
  <!-- nodes -->
  <circle cx="350" cy="55" r="24" fill="#D4D8D0" stroke="#8B8680" stroke-width="2"/>
  <text x="350" y="56" text-anchor="middle" dominant-baseline="central" fill="#3A3530" font-size="16" font-weight="bold">8</text>
  <circle cx="200" cy="135" r="22" fill="#D4D8D0" stroke="#B8B5B0" stroke-width="2"/>
  <text x="200" y="136" text-anchor="middle" dominant-baseline="central" fill="#3A3530" font-size="15" font-weight="bold">3</text>
  <circle cx="500" cy="135" r="22" fill="#D4D8D0" stroke="#B8B5B0" stroke-width="2"/>
  <text x="500" y="136" text-anchor="middle" dominant-baseline="central" fill="#3A3530" font-size="15" font-weight="bold">10</text>
  <circle cx="120" cy="215" r="22" fill="#E8E3D8" stroke="#B8B5B0" stroke-width="2"/>
  <text x="120" y="216" text-anchor="middle" dominant-baseline="central" fill="#3A3530" font-size="15" font-weight="bold">1</text>
  <circle cx="280" cy="215" r="22" fill="#E8E3D8" stroke="#B8B5B0" stroke-width="2"/>
  <text x="280" y="216" text-anchor="middle" dominant-baseline="central" fill="#3A3530" font-size="15" font-weight="bold">6</text>
  <circle cx="580" cy="215" r="22" fill="#E8E3D8" stroke="#B8B5B0" stroke-width="2"/>
  <text x="580" y="216" text-anchor="middle" dominant-baseline="central" fill="#3A3530" font-size="15" font-weight="bold">14</text>
  <!-- inorder traversal (sorted output) -->
  <rect x="80" y="260" width="540" height="30" rx="6" fill="#FAF8F5" stroke="#B8B5B0" stroke-width="1"/>
  <text x="100" y="279" fill="#5A5752" font-size="11" font-weight="bold">Inorder:</text>
  <text x="160" y="280" fill="#3A3530" font-size="13" font-weight="bold">1</text>
  <text x="182" y="280" fill="#9A9792" font-size="12">→</text>
  <text x="205" y="280" fill="#3A3530" font-size="13" font-weight="bold">3</text>
  <text x="227" y="280" fill="#9A9792" font-size="12">→</text>
  <text x="250" y="280" fill="#3A3530" font-size="13" font-weight="bold">6</text>
  <text x="272" y="280" fill="#9A9792" font-size="12">→</text>
  <text x="295" y="280" fill="#3A3530" font-size="13" font-weight="bold">8</text>
  <text x="317" y="280" fill="#9A9792" font-size="12">→</text>
  <text x="345" y="280" fill="#3A3530" font-size="13" font-weight="bold">10</text>
  <text x="372" y="280" fill="#9A9792" font-size="12">→</text>
  <text x="400" y="280" fill="#3A3530" font-size="13" font-weight="bold">14</text>
  <text x="445" y="280" fill="#5A5752" font-size="11" font-style="italic">(sorted!)</text>
</svg>

```python
def inorder(node):
    if not node:
        return
    inorder(node.left)
    process(node)
    inorder(node.right)
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 98 | Validate Binary Search Tree | [Link](https://leetcode.com/problems/validate-binary-search-tree/) | - |
| 230 | Kth Smallest Element in a BST | [Link](https://leetcode.com/problems/kth-smallest-element-in-a-bst/) | - |
| 235 | Lowest Common Ancestor of a BST | [Link](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/) | - |
| 894 | All Possible Full Binary Trees | [Link](https://leetcode.com/problems/all-possible-full-binary-trees/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2026/04/12/medium-894-all-possible-full-binary-trees/) |

---

### Practice Roadmap

| Day | Focus | Problems |
|---|---|---|
| 1 | Basics | LC 104 Maximum Depth, LC 102 Level Order, LC 257 Binary Tree Paths |
| 2 | Intermediate | LC 110 Balanced Binary Tree, LC 543 Diameter, LC 236 LCA |
| 3 | Advanced | LC 98 Validate BST, LC 230 Kth Smallest in BST, LC 124 Max Path Sum |

### Quick Pattern Recognition

If the problem mentions **height, diameter, path sum, ancestor, subtree, depth** → think **DFS on tree**.

If the problem mentions **levels, shortest depth, layer traversal** → think **BFS with queue**.

Most tree interview problems are medium difficulty, DFS recursion, postorder reasoning. If you can confidently solve LC 543, LC 236, and LC 124, you are well-prepared for senior-level tree questions.

---

## LCA (Binary Lifting)

**When to use:** Multiple LCA queries on a static tree, or when you also need to find the k-th ancestor of a node. Preprocess in O(N log N), answer each query in O(log N).

```python
K = 17
depth: list[int] = []
up: list[list[int]] = []


def dfsLift(u: int, p: int, g: list[list[int]]) -> None:
    up[u][0] = p
    for k in range(1, K + 1):
        up[u][k] = -1 if up[u][k - 1] < 0 else up[up[u][k - 1]][k - 1]
    for v in g[u]:
        if v != p:
            depth[v] = depth[u] + 1
            dfsLift(v, u, g)


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

| ID | Title | Link | Solution |
|---|---|---|---|
| 236 | Lowest Common Ancestor of a Binary Tree | [Link](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2026/01/19/medium-236-lowest-common-ancestor-of-a-binary-tree/) |
| 235 | Lowest Common Ancestor of a BST | [Link](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/) | - |
| 1650 | Lowest Common Ancestor of a Binary Tree III | [Link](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iii/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2025/10/20/medium-1650-lowest-common-ancestor-of-a-binary-tree-iii/) |
| 270 | Closest Binary Search Tree Value | [Link](https://leetcode.com/problems/closest-binary-search-tree-value/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2025/12/30/easy-270-closest-binary-search-tree-value/) |
| 285 | Inorder Successor in BST | [Link](https://leetcode.com/problems/inorder-successor-in-bst/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2025/12/30/medium-285-inorder-successor-in-bst/) |
| 426 | Convert Binary Search Tree to Sorted Doubly Linked List | [Link](https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/) | [Solution](https://robinali34.github.io/blog_leetcode_python/posts/2025-10-22-medium-426-convert-binary-search-tree-to-sorted-doubly-linked-list/) |
| 938 | Range Sum of BST | [Link](https://leetcode.com/problems/range-sum-of-bst/) | [Solution](https://robinali34.github.io/blog_leetcode_python/posts/2025-11-24-easy-938-range-sum-of-bst/) |
| 100 | Same Tree | [Link](https://leetcode.com/problems/same-tree/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2026/01/19/easy-100-same-tree/) |
| 101 | Symmetric Tree | [Link](https://leetcode.com/problems/symmetric-tree/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2026/01/19/easy-101-symmetric-tree/) |
| 104 | Maximum Depth of Binary Tree | [Link](https://leetcode.com/problems/maximum-depth-of-binary-tree/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2026/01/19/easy-104-maximum-depth-of-binary-tree/) |
| 110 | Balanced Binary Tree | [Link](https://leetcode.com/problems/balanced-binary-tree/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2026/03/06/easy-110-balanced-binary-tree/) |
| 111 | Minimum Depth of Binary Tree | [Link](https://leetcode.com/problems/minimum-depth-of-binary-tree/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2026/01/19/easy-111-minimum-depth-of-binary-tree/) |
| 112 | Path Sum | [Link](https://leetcode.com/problems/path-sum/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2026/03/06/easy-112-path-sum/) |
| 113 | Path Sum II | [Link](https://leetcode.com/problems/path-sum-ii/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2026/03/06/medium-113-path-sum-ii/) |
| 226 | Invert Binary Tree | [Link](https://leetcode.com/problems/invert-binary-tree/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2026/01/19/easy-226-invert-binary-tree/) |
| 543 | Diameter of Binary Tree | [Link](https://leetcode.com/problems/diameter-of-binary-tree/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2026/03/06/easy-543-diameter-of-binary-tree/) |
| 437 | Path Sum III | [Link](https://leetcode.com/problems/path-sum-iii/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2025/10/19/medium-437-path-sum-iii/) |
| 129 | Sum Root to Leaf Numbers | [Link](https://leetcode.com/problems/sum-root-to-leaf-numbers/) | [Solution](https://robinali34.github.io/blog_leetcode_python/posts/2025-11-24-medium-129-sum-root-to-leaf-numbers/) |
| 863 | All Nodes Distance K in Binary Tree | [Link](https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/) | [Solution](https://robinali34.github.io/blog_leetcode_python/posts/2025-10-25-medium-863-all-nodes-distance-k-in-binary-tree/) |
| 545 | Boundary of Binary Tree | [Link](https://leetcode.com/problems/boundary-of-binary-tree/) | [Solution](https://robinali34.github.io/blog_leetcode_python/posts/2025-10-21-medium-545-boundary-of-binary-tree/) |
| 993 | Cousins in Binary Tree | [Link](https://leetcode.com/problems/cousins-in-binary-tree/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2026/01/07/easy-993-cousins-in-binary-tree/) |
| 1443 | Minimum Time to Collect All Apples in a Tree | [Link](https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2025/10/20/medium-1443-minimum-time-to-collect-all-apples-in-a-tree/) |

## Segment Tree

**When to use:** Range queries (sum, min, max) with interleaved point or range updates — whenever a prefix-sum array would be too slow because of frequent modifications.

Segment Tree is a data structure that allows efficient range queries and range updates on an array. It's particularly useful for problems involving range sum, range minimum/maximum, and range updates.

**Reference:** [A Recursive Approach to Segment Trees, Range Sum Queries, and Lazy Propagation](https://leetcode.com/articles/a-recursive-approach-to-segment-trees-range-sum-queries-lazy-propagation/)

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 740 335" style="max-width: 100%; height: auto; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;">
  <text x="370" y="16" text-anchor="middle" fill="#5A5752" font-size="13" font-weight="bold">Segment Tree — Range Sum for array [1, 3, 5, 7, 2, 4]</text>
  <!-- edges: level 0 → level 1 -->
  <line x1="387" y1="55" x2="285" y2="90" stroke="#B8B5B0" stroke-width="1.5"/>
  <line x1="387" y1="55" x2="489" y2="90" stroke="#B8B5B0" stroke-width="1.5"/>
  <!-- edges: level 1 → level 2 -->
  <line x1="285" y1="120" x2="234" y2="155" stroke="#B8B5B0" stroke-width="1.5"/>
  <line x1="285" y1="120" x2="336" y2="155" stroke="#B8B5B0" stroke-width="1.5"/>
  <line x1="489" y1="120" x2="438" y2="155" stroke="#B8B5B0" stroke-width="1.5"/>
  <line x1="489" y1="120" x2="540" y2="155" stroke="#B8B5B0" stroke-width="1.5"/>
  <!-- edges: level 2 → level 3 -->
  <line x1="234" y1="185" x2="200" y2="220" stroke="#B8B5B0" stroke-width="1.5"/>
  <line x1="234" y1="185" x2="268" y2="220" stroke="#B8B5B0" stroke-width="1.5"/>
  <line x1="438" y1="185" x2="404" y2="220" stroke="#B8B5B0" stroke-width="1.5"/>
  <line x1="438" y1="185" x2="472" y2="220" stroke="#B8B5B0" stroke-width="1.5"/>
  <!-- dotted lines: leaves → array cells -->
  <line x1="200" y1="250" x2="200" y2="278" stroke="#B8B5B0" stroke-width="1" stroke-dasharray="3,3"/>
  <line x1="268" y1="250" x2="268" y2="278" stroke="#B8B5B0" stroke-width="1" stroke-dasharray="3,3"/>
  <line x1="336" y1="185" x2="336" y2="278" stroke="#B8B5B0" stroke-width="1" stroke-dasharray="3,3"/>
  <line x1="404" y1="250" x2="404" y2="278" stroke="#B8B5B0" stroke-width="1" stroke-dasharray="3,3"/>
  <line x1="472" y1="250" x2="472" y2="278" stroke="#B8B5B0" stroke-width="1" stroke-dasharray="3,3"/>
  <line x1="540" y1="185" x2="540" y2="278" stroke="#B8B5B0" stroke-width="1" stroke-dasharray="3,3"/>
  <!-- level 0: root node -->
  <rect x="361" y="30" width="52" height="34" rx="6" fill="#E8D5D0" stroke="#8B8680" stroke-width="1.5"/>
  <text x="387" y="44" text-anchor="middle" fill="#3A3530" font-size="14" font-weight="bold">22</text>
  <text x="387" y="58" text-anchor="middle" fill="#7A7772" font-size="9">[0–5]</text>
  <!-- level 1 -->
  <rect x="259" y="88" width="52" height="34" rx="6" fill="#D4D8E0" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="285" y="102" text-anchor="middle" fill="#3A3530" font-size="14" font-weight="bold">9</text>
  <text x="285" y="116" text-anchor="middle" fill="#7A7772" font-size="9">[0–2]</text>
  <rect x="463" y="88" width="52" height="34" rx="6" fill="#D4D8E0" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="489" y="102" text-anchor="middle" fill="#3A3530" font-size="14" font-weight="bold">13</text>
  <text x="489" y="116" text-anchor="middle" fill="#7A7772" font-size="9">[3–5]</text>
  <!-- level 2 -->
  <rect x="208" y="153" width="52" height="34" rx="6" fill="#D4D8D0" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="234" y="167" text-anchor="middle" fill="#3A3530" font-size="13" font-weight="bold">4</text>
  <text x="234" y="181" text-anchor="middle" fill="#7A7772" font-size="9">[0–1]</text>
  <rect x="310" y="153" width="52" height="34" rx="6" fill="#D4D8D0" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="336" y="167" text-anchor="middle" fill="#3A3530" font-size="13" font-weight="bold">5</text>
  <text x="336" y="181" text-anchor="middle" fill="#7A7772" font-size="9">[2]</text>
  <rect x="412" y="153" width="52" height="34" rx="6" fill="#D4D8D0" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="438" y="167" text-anchor="middle" fill="#3A3530" font-size="13" font-weight="bold">9</text>
  <text x="438" y="181" text-anchor="middle" fill="#7A7772" font-size="9">[3–4]</text>
  <rect x="514" y="153" width="52" height="34" rx="6" fill="#D4D8D0" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="540" y="167" text-anchor="middle" fill="#3A3530" font-size="13" font-weight="bold">4</text>
  <text x="540" y="181" text-anchor="middle" fill="#7A7772" font-size="9">[5]</text>
  <!-- level 3 (leaf nodes of the tree) -->
  <rect x="174" y="218" width="52" height="34" rx="6" fill="#E8E3D8" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="200" y="232" text-anchor="middle" fill="#3A3530" font-size="13" font-weight="bold">1</text>
  <text x="200" y="246" text-anchor="middle" fill="#7A7772" font-size="9">[0]</text>
  <rect x="242" y="218" width="52" height="34" rx="6" fill="#E8E3D8" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="268" y="232" text-anchor="middle" fill="#3A3530" font-size="13" font-weight="bold">3</text>
  <text x="268" y="246" text-anchor="middle" fill="#7A7772" font-size="9">[1]</text>
  <rect x="378" y="218" width="52" height="34" rx="6" fill="#E8E3D8" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="404" y="232" text-anchor="middle" fill="#3A3530" font-size="13" font-weight="bold">7</text>
  <text x="404" y="246" text-anchor="middle" fill="#7A7772" font-size="9">[3]</text>
  <rect x="446" y="218" width="52" height="34" rx="6" fill="#E8E3D8" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="472" y="232" text-anchor="middle" fill="#3A3530" font-size="13" font-weight="bold">2</text>
  <text x="472" y="246" text-anchor="middle" fill="#7A7772" font-size="9">[4]</text>
  <!-- array cells at bottom -->
  <text x="105" y="296" fill="#5A5752" font-size="11" font-weight="bold">array:</text>
  <rect x="170" y="278" width="60" height="26" rx="4" fill="#FAF8F5" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="200" y="295" text-anchor="middle" fill="#3A3530" font-size="13" font-weight="bold">1</text>
  <rect x="238" y="278" width="60" height="26" rx="4" fill="#FAF8F5" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="268" y="295" text-anchor="middle" fill="#3A3530" font-size="13" font-weight="bold">3</text>
  <rect x="306" y="278" width="60" height="26" rx="4" fill="#FAF8F5" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="336" y="295" text-anchor="middle" fill="#3A3530" font-size="13" font-weight="bold">5</text>
  <rect x="374" y="278" width="60" height="26" rx="4" fill="#FAF8F5" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="404" y="295" text-anchor="middle" fill="#3A3530" font-size="13" font-weight="bold">7</text>
  <rect x="442" y="278" width="60" height="26" rx="4" fill="#FAF8F5" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="472" y="295" text-anchor="middle" fill="#3A3530" font-size="13" font-weight="bold">2</text>
  <rect x="510" y="278" width="60" height="26" rx="4" fill="#FAF8F5" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="540" y="295" text-anchor="middle" fill="#3A3530" font-size="13" font-weight="bold">4</text>
  <!-- index labels -->
  <text x="105" y="322" fill="#9A9792" font-size="10">index:</text>
  <text x="200" y="322" text-anchor="middle" fill="#9A9792" font-size="10">0</text>
  <text x="268" y="322" text-anchor="middle" fill="#9A9792" font-size="10">1</text>
  <text x="336" y="322" text-anchor="middle" fill="#9A9792" font-size="10">2</text>
  <text x="404" y="322" text-anchor="middle" fill="#9A9792" font-size="10">3</text>
  <text x="472" y="322" text-anchor="middle" fill="#9A9792" font-size="10">4</text>
  <text x="540" y="322" text-anchor="middle" fill="#9A9792" font-size="10">5</text>
</svg>

### Basic Segment Tree (Range Sum Query)

```python
class SegmentTree:
    def __init__(self, nums: list[int]):
        self.n = len(nums)
        self.tree = [0] * (4 * self.n)
        self._build(nums, 1, 0, self.n - 1)

    def update(self, index: int, val: int) -> None:
        self._update(1, 0, self.n - 1, index, val)

    def query(self, left: int, right: int) -> int:
        return self._query(1, 0, self.n - 1, left, right)

    def _build(self, node: int, l: int, r: int, nums: list[int]) -> None:
        if l == r:
            self.tree[node] = nums[l]
        else:
            mid = (l + r) // 2
            self._build(node * 2, l, mid, nums)
            self._build(node * 2 + 1, mid + 1, r, nums)
            self.tree[node] = self.tree[node * 2] + self.tree[node * 2 + 1]

    def _update(self, node: int, l: int, r: int, idx: int, val: int) -> None:
        if l == r:
            self.tree[node] = val
        else:
            mid = (l + r) // 2
            if idx <= mid:
                self._update(node * 2, l, mid, idx, val)
            else:
                self._update(node * 2 + 1, mid + 1, r, idx, val)
            self.tree[node] = self.tree[node * 2] + self.tree[node * 2 + 1]

    def _query(self, node: int, l: int, r: int, ql: int, qr: int) -> int:
        if qr < l or ql > r:
            return 0
        if ql <= l and r <= qr:
            return self.tree[node]
        mid = (l + r) // 2
        return self._query(node * 2, l, mid, ql, qr) + self._query(
            node * 2 + 1, mid + 1, r, ql, qr
        )
```

### Segment Tree with Lazy Propagation (Range Update)

```python
class SegmentTreeLazy:
    def __init__(self, nums: list[int]):
        self.n = len(nums)
        self.tree = [0] * (4 * self.n)
        self.lazy = [0] * (4 * self.n)
        self._build(nums, 1, 0, self.n - 1)

    def updateRange(self, left: int, right: int, val: int) -> None:
        self._updateRange(1, 0, self.n - 1, left, right, val)

    def query(self, left: int, right: int) -> int:
        return self._query(1, 0, self.n - 1, left, right)

    def _build(self, node: int, l: int, r: int, nums: list[int]) -> None:
        if l == r:
            self.tree[node] = nums[l]
        else:
            mid = (l + r) // 2
            self._build(node * 2, l, mid, nums)
            self._build(node * 2 + 1, mid + 1, r, nums)
            self.tree[node] = self.tree[node * 2] + self.tree[node * 2 + 1]

    def _push(self, node: int, l: int, r: int) -> None:
        if self.lazy[node] != 0:
            self.tree[node] += self.lazy[node] * (r - l + 1)
            if l != r:
                self.lazy[node * 2] += self.lazy[node]
                self.lazy[node * 2 + 1] += self.lazy[node]
            self.lazy[node] = 0

    def _updateRange(
        self, node: int, l: int, r: int, ql: int, qr: int, val: int
    ) -> None:
        self._push(node, l, r)
        if qr < l or ql > r:
            return
        if ql <= l and r <= qr:
            self.lazy[node] += val
            self._push(node, l, r)
            return
        mid = (l + r) // 2
        self._updateRange(node * 2, l, mid, ql, qr, val)
        self._updateRange(node * 2 + 1, mid + 1, r, ql, qr, val)
        self._push(node * 2, l, mid)
        self._push(node * 2 + 1, mid + 1, r)
        self.tree[node] = self.tree[node * 2] + self.tree[node * 2 + 1]

    def _query(self, node: int, l: int, r: int, ql: int, qr: int) -> int:
        self._push(node, l, r)
        if qr < l or ql > r:
            return 0
        if ql <= l and r <= qr:
            return self.tree[node]
        mid = (l + r) // 2
        return self._query(node * 2, l, mid, ql, qr) + self._query(
            node * 2 + 1, mid + 1, r, ql, qr
        )
```

### Generic Segment Tree Template

```python
from typing import Callable, TypeVar

T = TypeVar("T")


class SegmentTreeGeneric:
    def __init__(
        self,
        arr: list[T],
        identity: T,
        merge: Callable[[T, T], T],
    ):
        self.n = len(arr)
        self.tree = [identity] * (4 * self.n)
        self.identity = identity
        self.merge = merge
        self._build(arr, 1, 0, self.n - 1)

    def update(self, index: int, val: T) -> None:
        self._update(1, 0, self.n - 1, index, val)

    def query(self, left: int, right: int) -> T:
        return self._query(1, 0, self.n - 1, left, right)

    def _build(self, arr: list[T], node: int, l: int, r: int) -> None:
        if l == r:
            self.tree[node] = arr[l]
        else:
            mid = (l + r) // 2
            self._build(arr, node * 2, l, mid)
            self._build(arr, node * 2 + 1, mid + 1, r)
            self.tree[node] = self.merge(self.tree[node * 2], self.tree[node * 2 + 1])

    def _update(self, node: int, l: int, r: int, idx: int, val: T) -> None:
        if l == r:
            self.tree[node] = val
        else:
            mid = (l + r) // 2
            if idx <= mid:
                self._update(node * 2, l, mid, idx, val)
            else:
                self._update(node * 2 + 1, mid + 1, r, idx, val)
            self.tree[node] = self.merge(self.tree[node * 2], self.tree[node * 2 + 1])

    def _query(self, node: int, l: int, r: int, ql: int, qr: int) -> T:
        if qr < l or ql > r:
            return self.identity
        if ql <= l and r <= qr:
            return self.tree[node]
        mid = (l + r) // 2
        return self.merge(
            self._query(node * 2, l, mid, ql, qr),
            self._query(node * 2 + 1, mid + 1, r, ql, qr),
        )


# Usage examples:
# Range Sum: SegmentTreeGeneric(arr, 0, lambda a, b: a + b)
# Range Min: SegmentTreeGeneric(arr, float("inf"), min)
# Range Max: SegmentTreeGeneric(arr, float("-inf"), max)
```

### Binary Search on Segment Tree (Tree Walking)

Instead of doing a binary search over an index and then a segment tree query (O(log^2 N)), we descend the segment tree directly to find the first element satisfying a condition in O(log N).

#### Template: Find First Index >= X

```python
def findFirst(node, l: int, r: int, x: int) -> int:
    if node.maxVal < x:
        return -1
    if l == r:
        return l

    mid = l + (r - l) // 2
    res = findFirst(node.left, l, mid, x)
    if res == -1:
        res = findFirst(node.right, mid + 1, r, x)
    return res
```

### Key Concepts

1. **Tree Structure**: Binary tree where each node represents a range `[l, r]`
2. **Build**: O(n) - Construct tree from array
3. **Point Update**: O(log n) - Update single element
4. **Range Query**: O(log n) - Query sum/min/max over range
5. **Lazy Propagation**: O(log n) - Defer range updates for efficiency
6. **Space Complexity**: O(4n) - Array-based representation

### When to Use

- **Range Queries**: Sum, min, max, gcd over ranges
- **Range Updates**: Add/subtract value to all elements in range
- **Frequent Updates**: When updates and queries are interleaved
- **Large Arrays**: When brute force is too slow

### Easy

| ID | Title | Link | Solution |
|---|---|---|---|
| 303 | Range Sum Query - Immutable | [Link](https://leetcode.com/problems/range-sum-query-immutable/) | - |
| 307 | Range Sum Query - Mutable | [Link](https://leetcode.com/problems/range-sum-query-mutable/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2026/01/16/medium-307-range-sum-query-mutable/) |

### Medium

| ID | Title | Link | Solution |
|---|---|---|---|
| 307 | Range Sum Query - Mutable | [Link](https://leetcode.com/problems/range-sum-query-mutable/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2026/01/16/medium-307-range-sum-query-mutable/) |
| 308 | Range Sum Query 2D - Mutable | [Link](https://leetcode.com/problems/range-sum-query-2d-mutable/) | - |
| 715 | Range Module | [Link](https://leetcode.com/problems/range-module/) | - |
| 729 | My Calendar I | [Link](https://leetcode.com/problems/my-calendar-i/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2026/01/17/medium-729-my-calendar-i/) |
| 731 | My Calendar II | [Link](https://leetcode.com/problems/my-calendar-ii/) | - |
| 1177 | Can Make Palindrome from Substring | [Link](https://leetcode.com/problems/can-make-palindrome-from-substring/) | - |
| 1505 | Minimum Possible Integer After at Most K Swaps | [Link](https://leetcode.com/problems/minimum-possible-integer-after-at-most-k-adjacent-swaps-on-digits/) | - |
| 1649 | Create Sorted Array through Instructions | [Link](https://leetcode.com/problems/create-sorted-array-through-instructions/) | - |
| 3477 | Number of Unplaced Fruits | [Link](https://leetcode.com/problems/number-of-unplaced-fruits/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2026/01/16/medium-3477-number-of-unplaced-fruits/) |

### Hard

| ID | Title | Link | Solution |
|---|---|---|---|
| 218 | The Skyline Problem | [Link](https://leetcode.com/problems/the-skyline-problem/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2025/10/05/hard-218-skyline-problem/) |
| 699 | Falling Squares | [Link](https://leetcode.com/problems/falling-squares/) | - |
| 715 | Range Module | [Link](https://leetcode.com/problems/range-module/) | - |
| 732 | My Calendar III | [Link](https://leetcode.com/problems/my-calendar-iii/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2026/01/18/hard-732-my-calendar-iii/) |
| 850 | Rectangle Area II | [Link](https://leetcode.com/problems/rectangle-area-ii/) | [Solution](https://robinali34.github.io/blog_leetcode_python/posts/2025-12-16-hard-850-rectangle-area-ii/) |
| 1157 | Online Majority Element In Subarray | [Link](https://leetcode.com/problems/online-majority-element-in-subarray/) | - |
| 2407 | Longest Increasing Subsequence II | [Link](https://leetcode.com/problems/longest-increasing-subsequence-ii/) | - |

### References

- [LeetCode: A Recursive Approach to Segment Trees, Range Sum Queries, and Lazy Propagation](https://leetcode.com/articles/a-recursive-approach-to-segment-trees-range-sum-queries-lazy-propagation/) - Comprehensive guide to segment trees with examples

## Fenwick Tree (Binary Indexed Tree)

**When to use:** Prefix sums with point updates, especially when you want simpler code and lower memory than a segment tree. Not suitable for min/max queries or range updates.

Fenwick Tree (also known as Binary Indexed Tree or BIT) is a data structure that provides efficient methods for calculating prefix sums and updating array elements. It's more space-efficient than Segment Tree but less flexible.

### Basic Fenwick Tree (1-Indexed)

```python
class FenwickTree:
    def __init__(self, size: int):
        self.n = size
        self.BIT = [0] * (size + 1)

    # Add delta to element at index i (0-indexed)
    def add(self, i: int, delta: int) -> None:
        i += 1  # Convert to 1-indexed
        while i <= self.n:
            self.BIT[i] += delta
            i += i & -i  # Move to next node

    # Get prefix sum from [0, i] (0-indexed)
    def prefixSum(self, i: int) -> int:
        s = 0
        i += 1  # Convert to 1-indexed
        while i > 0:
            s += self.BIT[i]
            i -= i & -i  # Move to parent
        return s

    # Get range sum from [l, r] (0-indexed)
    def rangeSum(self, l: int, r: int) -> int:
        return self.prefixSum(r) - (self.prefixSum(l - 1) if l > 0 else 0)
```

### Fenwick Tree for Range Sum Query

```python
class NumArray:
    def __init__(self, nums: list[int]):
        self.nums = nums
        self.n = len(nums)
        self.BIT = [0] * (self.n + 1)
        for i in range(self.n):
            self._add(i, nums[i])

    def _add(self, i: int, delta: int) -> None:
        i += 1
        while i <= self.n:
            self.BIT[i] += delta
            i += i & -i

    def _prefixSum(self, i: int) -> int:
        s = 0
        i += 1
        while i > 0:
            s += self.BIT[i]
            i -= i & -i
        return s

    def update(self, index: int, val: int) -> None:
        delta = val - self.nums[index]
        self.nums[index] = val
        self._add(index, delta)

    def sumRange(self, left: int, right: int) -> int:
        return self._prefixSum(right) - (self._prefixSum(left - 1) if left > 0 else 0)
```

### 2D Fenwick Tree

```python
class FenwickTree2D:
    def __init__(self, rows: int, cols: int):
        self.m = rows
        self.n = cols
        self.BIT = [[0] * (cols + 1) for _ in range(rows + 1)]

    def add(self, row: int, col: int, delta: int) -> None:
        row += 1
        col += 1
        i = row
        while i <= self.m:
            j = col
            while j <= self.n:
                self.BIT[i][j] += delta
                j += j & -j
            i += i & -i

    def prefixSum(self, row: int, col: int) -> int:
        s = 0
        row += 1
        col += 1
        i = row
        while i > 0:
            j = col
            while j > 0:
                s += self.BIT[i][j]
                j -= j & -j
            i -= i & -i
        return s

    def rangeSum(self, r1: int, c1: int, r2: int, c2: int) -> int:
        return (
            self.prefixSum(r2, c2)
            - self.prefixSum(r1 - 1, c2)
            - self.prefixSum(r2, c1 - 1)
            + self.prefixSum(r1 - 1, c1 - 1)
        )
```

### Key Concepts

1. **1-Indexed Array**: BIT uses 1-indexed array internally (index 0 is unused)
2. **Lowest Set Bit**: `i & -i` extracts the lowest set bit
3. **Update**: Add delta to node and all ancestors: `i += (i & -i)`
4. **Query**: Sum from node to root: `i -= (i & -i)`
5. **Space Complexity**: O(n) - More efficient than Segment Tree's O(4n)
6. **Time Complexity**: O(log n) for both update and query

### How It Works

- **Tree Structure**: Each node stores sum of a range ending at that index
- **Update Path**: When updating index `i`, update all nodes that include `i`
- **Query Path**: When querying prefix sum up to `i`, sum all nodes on path to root
- **Range Query**: `rangeSum(l, r) = prefixSum(r) - prefixSum(l-1)`

### When to Use

- **Prefix Sum Queries**: Efficient prefix sum calculations
- **Point Updates**: Single element updates
- **Space Constraint**: When O(n) space is preferred over O(4n)
- **Range Sum**: When only range sum is needed (not min/max)
- **Not Suitable For**: Range updates, min/max queries, complex range operations

### Comparison: Segment Tree vs Fenwick Tree

| Aspect | Segment Tree | Fenwick Tree |
|--------|-------------|--------------|
| **Space** | O(4n) | O(n) |
| **Build Time** | O(n) | O(n log n) |
| **Update** | O(log n) | O(log n) |
| **Range Query** | O(log n) | O(log n) |
| **Range Update** | O(log n) with lazy | Not directly supported |
| **Min/Max Query** | Supported | Not directly supported |
| **Code Complexity** | More verbose | Simpler |
| **Flexibility** | High | Limited to prefix/range sum |

### Example Problems

| ID | Title | Link | Solution |
|---|---|---|---|
| 307 | Range Sum Query - Mutable | [Link](https://leetcode.com/problems/range-sum-query-mutable/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2026/01/16/medium-307-range-sum-query-mutable/) |
| 308 | Range Sum Query 2D - Mutable | [Link](https://leetcode.com/problems/range-sum-query-2d-mutable/) | - |
| 315 | Count of Smaller Numbers After Self | [Link](https://leetcode.com/problems/count-of-smaller-numbers-after-self/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2026/01/17/hard-315-count-of-smaller-numbers-after-self/) |
| 327 | Count of Range Sum | [Link](https://leetcode.com/problems/count-of-range-sum/) | - |
| 493 | Reverse Pairs | [Link](https://leetcode.com/problems/reverse-pairs/) | - |
| 1649 | Create Sorted Array through Instructions | [Link](https://leetcode.com/problems/create-sorted-array-through-instructions/) | - |

### References

- [TopCoder: Binary Indexed Trees](https://www.topcoder.com/thrive/articles/Binary%20Indexed%20Trees) - Comprehensive tutorial on Fenwick Trees
- [GeeksforGeeks: Binary Indexed Tree](https://www.geeksforgeeks.org/binary-indexed-tree-or-fenwick-tree-2/) - Implementation and examples

## HLD (Heavy-Light Decomposition) skeleton

**When to use:** Path queries or path updates on a tree (e.g., sum/max along a path between two nodes). Decomposes the tree into chains so you can use a segment tree on each chain. Rarely needed on LeetCode, but essential for competitive programming.

```python
N = 200000
gH: list[list[int]] = [[] for _ in range(N)]
szH = [0] * N
parH = [0] * N
depH = [0] * N
heavyH = [-1] * N
headH = [0] * N
inH = [0] * N
curT = 0


def dfs1(u: int, p: int) -> int:
    parH[u] = p
    depH[u] = 0 if p == -1 else depH[p] + 1
    szH[u] = 1
    heavyH[u] = -1
    best = 0
    for v in gH[u]:
        if v != p:
            s = dfs1(v, u)
            szH[u] += s
            if s > best:
                best = s
                heavyH[u] = v
    return szH[u]


def dfs2(u: int, h: int) -> None:
    global curT
    headH[u] = h
    inH[u] = curT
    curT += 1
    if heavyH[u] != -1:
        dfs2(heavyH[u], h)
    for v in gH[u]:
        if v != parH[u] and v != heavyH[u]:
            dfs2(v, v)
```

> Note: HLD is rarely required on LeetCode.

## Pattern Summary

| Pattern | Signal Phrases | Approach |
|---|---|---|
| Inorder Traversal | "sorted order of BST" | Left → Root → Right |
| Bottom-Up DFS | "height", "diameter", "balanced" | Return value from children |
| Global Result | "max path sum" | Track global max during DFS |
| Path Tracking | "root-to-leaf", "path sum" | Pass path down recursively |
| Level-order BFS | "level by level", "right side view" | Queue, process by level |
| LCA | "lowest common ancestor" | Recursive or binary lifting |
| BST | "validate", "search", "insert" | Use BST property (left < root < right) |

## More templates

- **Beginner's Guide:** [LeetCode Beginner's Guide](/2026/06/25/leetcode-beginners-guide/)
- **Data structures (segment tree, Fenwick, DSU):** [Data Structures & Core Algorithms](/posts/2025-10-29-leetcode-templates-data-structures/)
- **Graph (BFS, Dijkstra, topo):** [Graph](/posts/2025-10-29-leetcode-templates-graph/)
- **Search (binary search, 2D):** [Search](/posts/2026-01-20-leetcode-templates-search/)
- **Master index:** [Categories & Templates](/posts/2025-10-29-leetcode-categories-and-templates/)
{% endraw %}
