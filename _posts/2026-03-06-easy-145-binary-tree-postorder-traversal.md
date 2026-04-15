---
layout: post
title: "[Easy] 145. Binary Tree Postorder Traversal"
date: 2026-03-06 00:00:00 -0700
categories: [leetcode, easy, tree, dfs]
tags: [leetcode, easy, tree, postorder, stack]
permalink: /2026/03/06/easy-145-binary-tree-postorder-traversal/
---

# [Easy] 145. Binary Tree Postorder Traversal

## Problem Statement

Given the `root` of a binary tree, return the **postorder traversal** of its nodes' values.

Postorder: **left → right → root**.

## Examples

**Example 1:**

```python
Input: root = [1,null,2,3]
Output: [3,2,1]
# Tree:  1
#         \
#          2
#         /
#        3
```

**Example 2:**

```python
Input: root = []
Output: []
```

**Example 3:**

```python
Input: root = [1]
Output: [1]
```

## Constraints

- The number of nodes in the tree is in the range `[0, 100]`.
- `-100 <= Node.val <= 100`

## Clarification Questions

1. **Empty tree**: Return empty list when `root` is `None`?  
   **Assumption**: Yes.
2. **Order**: Strict left → right → root?  
   **Assumption**: Yes — classic postorder (e.g. useful for freeing tree or postfix expressions).
3. **Space**: Recursion stack counts toward space?  
   **Assumption**: Yes — iterative stack avoids recursion stack.

## Interview Deduction Process (20 minutes)

**Step 1: Recursive definition (5 min)**  
Postorder = postorder(left), postorder(right), then process root. Base case: `node is None` → return.

**Step 2: Recursive implementation (7 min)**  
Use a helper that recurses on left, recurses on right, then appends `node.val`. Collect results in a list (closure or passed list).

**Step 3: Iterative with stack (8 min)**  
Postorder is the reverse of “preorder but visit root then right then left.” So run a modified preorder (push left first so we pop right first), collect values, then **reverse** the list to get left → right → root. Alternatively, use one stack with a “last visited” pointer to know when we’re returning from the right subtree.

## Solution Approach

**Recursive:** Recurse left, recurse right, append root. Use a shared list or pass it as argument.

**Iterative (reverse trick):** Do a “right-first preorder” (traverse root → right → left) using a stack: push root, then in a loop pop, append value, push left then right (so right is popped next). Reverse the collected list to get left → right → root.

**Iterative (one stack, last visited):** Use a stack and a `last_visited` node. Go left to the bottom. When we pop a node, we visit it only if it has no right child or its right child was just visited; otherwise push the node back and go right. This yields true postorder without reversing.

### Key Insights

1. **Postorder = root last** — Process left subtree, then right subtree, then root.
2. **Reverse of root-right-left** — Postorder (left → right → root) is the reverse of “root → right → left,” so we can reuse a preorder-style loop and reverse the result.
3. **One-stack with last visited** — Visit a node only when we’re “returning” from its right subtree (right is None or right was last visited).

## Python Solution

### Recursive (DFS)

```python
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        rtn: List[int] = []

        def postorder_dfs(node: Optional[TreeNode]) -> None:
            if not node:
                return
            postorder_dfs(node.left)
            postorder_dfs(node.right)
            rtn.append(node.val)

        postorder_dfs(root)
        return rtn
```

### Iterative (reverse of root → right → left)

```python
from typing import List, Optional


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        rtn: List[int] = []
        stk: List[TreeNode] = [root]

        while stk:
            node = stk.pop()
            rtn.append(node.val)
            if node.left:
                stk.append(node.left)
            if node.right:
                stk.append(node.right)

        return rtn[::-1]  # reverse to get left → right → root
```

### Iterative (one stack, last visited)

```python
from typing import List, Optional


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        rtn: List[int] = []
        stk: List[TreeNode] = []
        node = root
        last_visited: Optional[TreeNode] = None

        while node or stk:
            while node:
                stk.append(node)
                node = node.left
            peek = stk[-1]
            # Visit only if no right subtree or right subtree was just visited
            if not peek.right or peek.right is last_visited:
                last_visited = stk.pop()
                rtn.append(last_visited.val)
                node = None
            else:
                node = peek.right

        return rtn
```

## Algorithm Explanation

**Recursive:**  
If node is null, return. Otherwise recurse on left subtree, recurse on right subtree, then append `node.val`. The closure collects values in postorder.

**Iterative (reverse):**  
We traverse in “preorder but right before left”: pop, append, push left then right. That gives root → right → left. Reversing the list gives left → right → root (postorder).

**Iterative (last visited):**  
We go left to the bottom (pushing nodes). Then we look at the top of the stack. If it has no right child or its right child was the node we just visited, we pop and visit (we’re “returning” from the right subtree). Otherwise we go to the right child. This mimics the recursive order without reversing.

## Complexity Analysis

- **Time Complexity**: \(O(n)\), where \(n\) is the number of nodes — each node is pushed/popped and visited once.
- **Space Complexity**: \(O(h)\) for the stack, where \(h\) is the height (worst \(O(n)\) for a skew tree). The reverse approach uses an extra \(O(n)\) for the output list before reversing (same asymptotic as storing the result).

## Edge Cases

- `root is None` → return `[]`.
- Single node → return `[root.val]`.
- Skewed tree → stack depth \(O(n)\).

## Common Mistakes

- **Recursive:** Appending before recursing (would be preorder or inorder, not postorder).
- **Iterative (reverse):** Pushing right then left (would give root → left → right; reversing would give right → left → root, which is wrong).
- **Last-visited:** Forgetting to set `node = None` after visiting so we don’t re-descend left; or not checking `peek.right is last_visited` and visiting before the right subtree is done.

## Related Problems

- [LC 94: Binary Tree Inorder Traversal](/2026/03/06/easy-94-binary-tree-inorder-traversal/) — Inorder (left → root → right).
- [LC 144: Binary Tree Preorder Traversal](/2026/03/06/easy-144-binary-tree-preorder-traversal/) — Preorder (root → left → right).
- [LC 102: Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/) — BFS by level.
- [LC 590: N-ary Tree Postorder Traversal](https://leetcode.com/problems/n-ary-tree-postorder-traversal/) — Same idea on N-ary trees.
