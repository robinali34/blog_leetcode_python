---
layout: post
title: "144. Binary Tree Preorder Traversal"
date: 2026-03-06 00:00:00 -0700
categories: [leetcode, easy, tree, dfs]
tags: [leetcode, easy, tree, preorder, stack]
permalink: /2026/03/06/easy-144-binary-tree-preorder-traversal/
---

# 144. Binary Tree Preorder Traversal

## Problem Statement

Given the `root` of a binary tree, return the **preorder traversal** of its nodes' values.

Preorder: **root → left → right**.

## Examples

**Example 1:**

```python
Input: root = [1,null,2,3]
Output: [1,2,3]
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
2. **Order**: Strict root → left → right?  
   **Assumption**: Yes — classic preorder.
3. **Space**: Recursion stack counts toward space?  
   **Assumption**: Yes — iterative stack solution avoids recursion stack.

## Interview Deduction Process (20 minutes)

**Step 1: Recursive definition (5 min)**  
Preorder = process root, then preorder(left), then preorder(right). Base case: `node is None` → return.

**Step 2: Recursive implementation (7 min)**  
Use a helper that appends `node.val`, then recurses on left and right. Collect results in a list (closure or passed list).

**Step 3: Iterative with stack (8 min)**  
Simulate the call stack: push root, then while stack not empty, pop, append value, then push **right** then **left** (so left is processed first when we pop).

## Solution Approach

**Recursive:** Visit root, recurse left, recurse right. Use a shared list or pass it as argument.

**Iterative:** Use a stack. Push root. Loop: pop node, append `node.val`, push `node.right` (if any), then push `node.left` (if any). This yields root → left → right order.

**Morris (O(1) space):** Use the tree's right pointers to build a temporary link from the rightmost node of the current node's left subtree back to the current node. Visit the node when creating the link (preorder), then traverse left; when the link is found, remove it and go right.

### Key Insights

1. **Preorder = root first** — Process the current node before its children.
2. **Stack order** — Push right before left so that when we pop, we process left first (LIFO).
3. **Null checks** — Skip pushing `None` to avoid extra checks in the loop.
4. **Morris** — In-order predecessor's right pointer is reused to return from the left subtree without a stack; visit node when we create the link (preorder).

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
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        rtn: List[int] = []

        def preorder_dfs(node: Optional[TreeNode]) -> None:
            if not node:
                return
            rtn.append(node.val)
            preorder_dfs(node.left)
            preorder_dfs(node.right)

        preorder_dfs(root)
        return rtn
```

### Iterative (Stack)

```python
from typing import List, Optional


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        rtn: List[int] = []
        if root is None:
            return rtn

        stk: List[TreeNode] = [root]
        while stk:
            node = stk.pop()
            rtn.append(node.val)
            if node.right:
                stk.append(node.right)
            if node.left:
                stk.append(node.left)
        return rtn
```

### Morris Preorder (O(1) space)

```python
from typing import List, Optional


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output: List[int] = []
        node = root

        while node:
            if not node.left:
                output.append(node.val)
                node = node.right
            else:
                # Find inorder predecessor of node (rightmost in left subtree)
                predecessor = node.left
                while predecessor.right and predecessor.right is not node:
                    predecessor = predecessor.right

                if not predecessor.right:
                    # First time: visit node (preorder), thread back to node, go left
                    output.append(node.val)
                    predecessor.right = node
                    node = node.left
                else:
                    # Second time: we've returned from left subtree, unthread, go right
                    predecessor.right = None
                    node = node.right

        return output
```

## Algorithm Explanation

**Recursive:**  
If node is null, return. Otherwise append `node.val`, then call preorder on left subtree, then on right subtree. The closure `rtn` collects values in preorder.

**Iterative:**  
We simulate the same order with a stack. After popping a node we visit it (append), then we push its right child and then its left child so that the next pop is the left child (preorder: root, then left subtree, then right subtree).

**Morris:**  
We use the right pointer of the **inorder predecessor** of the current node (rightmost node in its left subtree) as a temporary link back to the current node. When there is no left child, we visit the node and go right. When there is a left child: if the predecessor's right is null, we visit the node (preorder), set `predecessor.right = node`, and go left; when we later reach the same node via the thread, we clear the thread and go right. Each edge is traversed at most twice, so time is still \(O(n)\), and we use only \(O(1)\) extra space (no stack).

## Complexity Analysis

- **Time Complexity**: \(O(n)\), where \(n\) is the number of nodes — each node is visited once (recursive/iterative); in Morris each edge is traversed at most twice, so still \(O(n)\).
- **Space Complexity**:  
  - Recursive: \(O(h)\) for the call stack, where \(h\) is the height (worst \(O(n)\) for a skew tree).  
  - Iterative: \(O(h)\) for the stack (same worst case).  
  - Morris: \(O(1)\) extra space (only a few pointers; tree structure is restored after traversal).

## Edge Cases

- `root is None` → return `[]`.
- Single node → return `[root.val]`.
- Skewed tree (e.g. all left) → recursion/stack depth is \(O(n)\).

## Common Mistakes

- **Recursive:** Passing `rtn` into the helper when it's captured by closure — call should be `preorder_dfs(root)` with no second argument.
- **Iterative:** Pushing left before right (would still be valid preorder but then you must pop left first — pushing right then left keeps standard preorder with a single pop loop).
- Forgetting to check for `None` before pushing children to avoid pushing `None` onto the stack.
- **Morris:** Forgetting to set `predecessor.right = None` when unwinding the thread, which would leave the tree modified; or visiting the node at the wrong time (in preorder we visit when we create the link, not when we follow it back).

## Related Problems

- [LC 94: Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/) — Inorder (left → root → right).
- [LC 145: Binary Tree Postorder Traversal](/2026/03/06/easy-145-binary-tree-postorder-traversal/) — Postorder (left → right → root).
- [LC 102: Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/) — BFS by level.
