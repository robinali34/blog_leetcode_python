---
layout: post
title: "[Medium] 1448. Count Good Nodes in Binary Tree"
date: 2026-03-18 00:00:00 -0700
categories: [leetcode, medium, tree, dfs, bfs]
tags: [leetcode, medium, tree, dfs, bfs]
permalink: /2026/03/18/medium-1448-count-good-nodes-in-binary-tree/
---

# [Medium] 1448. Count Good Nodes in Binary Tree

## Problem Statement

Given a binary tree `root`, a node `X` in the tree is named **good** if in the path from `root` to `X` there are **no nodes with a value greater than `X`**.

Return the number of **good** nodes in the binary tree.

## Examples

**Example 1:**

```python
Input: root = [3,1,4,3,null,1,5]
Output: 4
# Good nodes: 3 (root), 3 (left-left), 4, 5
```

**Example 2:**

```python
Input: root = [3,3,null,4,2]
Output: 3
```

**Example 3:**

```python
Input: root = [1]
Output: 1
```

## Constraints

- The number of nodes in the binary tree is in the range `[1, 10^5]`.
- `-10^4 <= Node.val <= 10^4`

## Clarification Questions

1. **Path definition**: “Path from root to X” means the unique path following parent pointers down the tree, correct?  
   **Assumption**: Yes.
2. **Good condition**: Node is good iff `node.val >= max value seen so far on the path`?  
   **Assumption**: Yes.
3. **Empty tree**: Constraints say at least 1 node, but we’ll still handle `root is None` by returning 0.  
   **Assumption**: Safe guard.

## Interview Deduction Process (20 minutes)

**Step 1: Observing the invariant (6 min)**  
When traversing from root downwards, the only thing we need to know is the **maximum value seen so far** on the current path. A node is good if its value is >= that maximum.

**Step 2: DFS recursion (7 min)**  
Use DFS carrying `max_val` as state. At each node:

- If `node.val >= max_val`, it is good and we update `max_val`.
- Recurse to children with the updated max.

**Step 3: Iterative traversal (7 min)**  
Avoid recursion depth issues with `n` up to 1e5 by using an explicit stack (DFS) or queue (BFS), storing `(node, max_val)` for each pending state.

## Solution Approach

We traverse the tree and maintain the maximum value seen on the path from root to the current node.

- If `node.val >= max_val`, the node is good.
- Then we continue to children with `new_max = max(max_val, node.val)`.

This works with:

- **Recursive DFS**
- **Iterative DFS with stack**
- **BFS with queue**

### Key Insights

1. **State compression** — For each node, the only necessary path information is `max_so_far`.
2. **Local decision** — “Good” is decided locally using `node.val >= max_so_far`.
3. **Iterative is safer** — For very deep trees, iterative DFS/BFS avoids recursion depth issues in Python.

## Python Solution

### Recursive DFS (carry max-so-far)

```python
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        count = 0

        def dfs(node: Optional[TreeNode], max_val: int) -> None:
            nonlocal count
            if not node:
                return
            if node.val >= max_val:
                count += 1
                max_val = node.val
            dfs(node.left, max_val)
            dfs(node.right, max_val)

        dfs(root, root.val)
        return count
```

### Iterative DFS (stack)

```python
from typing import Optional, List, Tuple


class Solution:
    def goodNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        count = 0
        stack: List[Tuple[TreeNode, int]] = [(root, root.val)]

        while stack:
            node, max_val = stack.pop()
            if node.val >= max_val:
                count += 1
            new_max = max(max_val, node.val)
            if node.right:
                stack.append((node.right, new_max))
            if node.left:
                stack.append((node.left, new_max))

        return count
```

### BFS (queue)

```python
from collections import deque
from typing import Optional, Deque, Tuple


class Solution:
    def goodNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        count = 0
        queue: Deque[Tuple[TreeNode, int]] = deque([(root, root.val)])

        while queue:
            node, max_val = queue.popleft()
            if node.val >= max_val:
                count += 1
            new_max = max(max_val, node.val)
            if node.left:
                queue.append((node.left, new_max))
            if node.right:
                queue.append((node.right, new_max))

        return count
```

## Algorithm Explanation

We traverse nodes while carrying `max_val`, the maximum value seen on the path from the root to the current node.

- If `node.val >= max_val`, then no earlier node on the path is greater than `node.val`, so the node is **good**.
- Update `max_val` to `max(max_val, node.val)` and continue.

All three traversals (recursive DFS, iterative DFS, BFS) implement the same logic; they only differ in how they manage the traversal order and stack/queue.

## Complexity Analysis

- **Time**: O(n), where `n` is the number of nodes — each node is processed once.
- **Space**:
  - Recursive DFS: O(h) recursion stack, where `h` is tree height (worst-case O(n)).
  - Iterative DFS / BFS: O(h) or O(n) for explicit stack/queue in worst case.

## Edge Cases

- Single node → always good → 1.
- Strictly decreasing values down a path → only root is good.
- Strictly increasing values down a path → all nodes are good.

## Common Mistakes

- **Not updating `max_so_far` correctly** — Always pass `max(max_so_far, node.val)` to children.
- **Comparing with parent only** — “Good” compares to the maximum on the entire root-to-node path, not just parent.
- **Recursion depth in Python** — For deep trees, prefer iterative stack/queue.

## Related Problems

- [LC 124: Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/) — Tree path aggregates.
- [LC 543: Diameter of Binary Tree](/2026/03/06/easy-543-diameter-of-binary-tree/) — Tree DFS with path-related metric.
- [LC 102: Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/) — BFS traversal template.

