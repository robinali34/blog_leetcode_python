---
layout: post
title: "[Easy] 94. Binary Tree Inorder Traversal"
date: 2026-03-06 00:00:00 -0700
categories: [leetcode, easy, tree, dfs]
tags: [leetcode, easy, tree, inorder, stack]
permalink: /2026/03/06/easy-94-binary-tree-inorder-traversal/
---

# [Easy] 94. Binary Tree Inorder Traversal

## Problem Statement

Given the `root` of a binary tree, return the **inorder traversal** of its nodes' values.

Inorder: **left → root → right**.

## Examples

**Example 1:**

```python
Input: root = [1,null,2,3]
Output: [1,3,2]
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
2. **Order**: Strict left → root → right?  
   **Assumption**: Yes — classic inorder (e.g. BST gives sorted order).
3. **Space**: Recursion stack counts toward space?  
   **Assumption**: Yes — iterative stack or Morris avoids/minimizes it.

## Interview Deduction Process (20 minutes)

**Step 1: Recursive definition (5 min)**  
Inorder = inorder(left), then process root, then inorder(right). Base case: `node is None` → return.

**Step 2: Recursive implementation (7 min)**  
Use a helper that recurses on left, appends `node.val`, then recurses on right. Collect results in a list (closure or passed list).

**Step 3: Iterative with stack (8 min)**  
Simulate the call stack: go left to the bottom (pushing nodes), then pop (visit), then go right. Repeat until stack is empty and current node is None.

## Solution Approach

**Recursive:** Recurse left, append root, recurse right. Use a shared list or pass it as argument.

**Iterative:** Use a stack. While current node is not None or stack is not empty: if node is not None, push and go left; else pop, append value, set node to right. This yields left → root → right.

**Morris (O(1) space):** Use the right pointer of the inorder predecessor (rightmost in left subtree) as a temporary link back to the current node. When we follow the link back, we visit (inorder) and go right. No stack.

### Key Insights

1. **Inorder = root in the middle** — Process left subtree, then root, then right subtree.
2. **Iterative stack** — “Go left to the bottom, then pop (visit), then go right” captures the same order.
3. **Morris** — Thread from inorder predecessor’s right back to current node; visit when we return via the thread (inorder).

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
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        rtn: List[int] = []

        def inorder_dfs(node: Optional[TreeNode]) -> None:
            if not node:
                return
            inorder_dfs(node.left)
            rtn.append(node.val)
            inorder_dfs(node.right)

        inorder_dfs(root)
        return rtn
```

### Iterative (Stack)

```python
from typing import List, Optional


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        rtn: List[int] = []
        stk: List[TreeNode] = []
        node = root

        while node or stk:
            while node:
                stk.append(node)
                node = node.left
            node = stk.pop()
            rtn.append(node.val)
            node = node.right

        return rtn
```

### Morris Inorder (O(1) space)

```python
from typing import List, Optional


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        rtn: List[int] = []
        node = root

        while node:
            if not node.left:
                rtn.append(node.val)
                node = node.right
            else:
                predecessor = node.left
                while predecessor.right and predecessor.right is not node:
                    predecessor = predecessor.right

                if not predecessor.right:
                    predecessor.right = node
                    node = node.left
                else:
                    predecessor.right = None
                    rtn.append(node.val)  # visit when we return via thread
                    node = node.right

        return rtn
```

## Algorithm Explanation

**Recursive:**  
If node is null, return. Otherwise recurse on left subtree, append `node.val`, then recurse on right subtree. The closure collects values in inorder.

**Iterative:**  
We simulate the same order with a stack. “Go left until null” (pushing nodes), then pop (visit), then go right. Repeat. This processes left subtree first, then root, then right subtree.

**Morris:**  
We reuse the right pointer of the **inorder predecessor** (rightmost in left subtree). When there is no left child, we visit the node and go right. When there is a left child: if the predecessor’s right is null, we set `predecessor.right = node` and go left; when we later return via this thread, we visit the node (inorder), clear the thread, and go right. Each edge is traversed at most twice; no stack.

## Complexity Analysis

- **Time Complexity**: \(O(n)\), where \(n\) is the number of nodes — each node is visited once (recursive/iterative); in Morris each edge is traversed at most twice, so still \(O(n)\).
- **Space Complexity**:  
  - Recursive: \(O(h)\) for the call stack (\(h\) = height, worst \(O(n)\)).  
  - Iterative: \(O(h)\) for the stack.  
  - Morris: \(O(1)\) extra space (tree is restored after traversal).

## Edge Cases

- `root is None` → return `[]`.
- Single node → return `[root.val]`.
- Skewed tree → recursion/stack depth \(O(n)\).

## Common Mistakes

- **Recursive:** Appending before recursing left (would be preorder, not inorder).
- **Iterative:** Visiting before going left, or wrong loop condition (must continue while `node or stk`).
- **Morris:** Visiting when creating the thread instead of when following it back (that would be preorder); or forgetting to clear `predecessor.right`.

## Related Problems

- [LC 144: Binary Tree Preorder Traversal](/2026/03/06/easy-144-binary-tree-preorder-traversal/) — Preorder (root → left → right).
- [LC 145: Binary Tree Postorder Traversal](/2026/03/06/easy-145-binary-tree-postorder-traversal/) — Postorder (left → right → root).
- [LC 102: Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/) — BFS by level.
- [LC 230: Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/) — Inorder on BST gives sorted order; stop at k-th.
