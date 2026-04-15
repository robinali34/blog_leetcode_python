---
layout: post
title: "[Easy] 110. Balanced Binary Tree"
date: 2026-03-06 00:00:00 -0700
categories: [leetcode, easy, tree, dfs]
tags: [leetcode, easy, tree, height, balance]
permalink: /2026/03/06/easy-110-balanced-binary-tree/
---

# [Easy] 110. Balanced Binary Tree

## Problem Statement

Given a binary tree, determine if it is **height-balanced**.

A height-balanced binary tree is one in which the **left and right subtrees of every node** differ in height by no more than 1.

## Examples

**Example 1:**

```python
Input: root = [3,9,20,null,null,15,7]
Output: True
# Tree:    3
#         / \
#        9  20
#           /  \
#          15   7
# Heights at root: left=1, right=2 → diff=1 ✓
```

**Example 2:**

```python
Input: root = [1,2,2,3,3,null,null,4,4]
Output: False
# Tree:       1
#            / \
#           2   2
#          / \
#         3   3
#        / \
#       4   4
# At node 2: left height 2, right height 1 → diff=1 ✓
# At node 3: left height 1, right height 0 → diff=1 ✓
# At node 1: left height 3, right height 1 → diff=2 ✗
```

**Example 3:**

```python
Input: root = []
Output: True
```

## Constraints

- The number of nodes in the tree is in the range `[0, 5000]`.
- `-10^4 <= Node.val <= 10^4`

## Clarification Questions

1. **Empty tree**: Is an empty tree considered balanced?  
   **Assumption**: Yes — return `True`.
2. **Definition**: Must **every** node satisfy the balance condition, or only the root?  
   **Assumption**: Every node — the condition applies to all subtrees.
3. **Height**: Is height the number of edges or the number of nodes on the longest path?  
   **Assumption**: Typically “edges” (leaf has height 0). Empty tree height is often -1 or 0; we use 0 for empty so a single node has height 1 for “number of nodes” style, or we use -1 for empty so single node has height 0. LeetCode-style: empty = 0 height (single node = 1) or -1 for empty (single node = 0). The important part is that we compare left and right consistently; the code below uses “node count” style (empty → 0, leaf → 1).

## Interview Deduction Process (20 minutes)

**Step 1: Definition (5 min)**  
Balance at a node: `|height(left) - height(right)| <= 1`, and both left and right subtrees must be balanced. Base case: `node is None` → balanced, height 0 (or -1 depending on convention).

**Step 2: Naive approach (5 min)**  
At each node, compute left height, right height, check balance, and recurse to check left and right are balanced. Computing height is O(n) per node → O(n²) total for a skew tree.

**Step 3: Optimal approach (10 min)**  
Single DFS that returns both “height” and “is balanced.” If we use a sentinel (e.g. -1) for “imbalanced,” we can return one value: height if balanced, -1 if not. Then `abs(left_h - right_h) <= 1` and both non-negative for current node to be balanced. One pass → O(n).

## Solution Approach

**Naive (O(n²)):** For each node, compute height of left and right (separate recursive calls), check `|left_h - right_h| <= 1`, and recursively check that left and right subtrees are balanced. Recomputes heights repeatedly.

**Optimal (O(n)):** One DFS helper that returns the height of the subtree, or a sentinel (e.g. -1) if the subtree is not balanced. If either child returns -1 or `abs(left_h - right_h) > 1`, return -1; otherwise return `1 + max(left_h, right_h)`. Final result: tree is balanced iff the helper returns a non-negative value.

### Key Insights

1. **Every node** — Balance must hold at the root and at every internal node; checking only the root is wrong.
2. **Height once** — Avoid computing height separately for each node; combine “compute height” and “check balance” in one DFS.
3. **Sentinel** — Using -1 (or any invalid height) to mean “imbalanced” lets us use a single return value and propagate failure up.

## Python Solution

### Naive (O(n²)) — check balance at each node, height computed separately

```python
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        def height(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0
            return 1 + max(height(node.left), height(node.right))

        left_h = height(root.left)
        right_h = height(root.right)
        if abs(left_h - right_h) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
```

### Optimal (O(n)) — single DFS, height with -1 sentinel for imbalanced

```python
from typing import Optional


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height_if_balanced(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0
            left_h = height_if_balanced(node.left)
            right_h = height_if_balanced(node.right)
            if left_h == -1 or right_h == -1 or abs(left_h - right_h) > 1:
                return -1
            return 1 + max(left_h, right_h)

        return height_if_balanced(root) != -1
```

## Algorithm Explanation

**Naive:**  
Base: empty tree is balanced. Otherwise compute left and right heights (each call visits the whole subtree), check `|left_h - right_h| <= 1`, and recursively ensure both left and right are balanced. Same height computation is repeated for nodes in deeper calls.

**Optimal:**  
Helper returns the height of the subtree if it is balanced, and -1 if it is not. Base: `None` → 0. Recurse on left and right. If either returns -1 or `abs(left_h - right_h) > 1`, return -1. Otherwise return `1 + max(left_h, right_h)`. The tree is balanced iff the final return is not -1.

## Complexity Analysis

- **Naive**
  - **Time**: O(n²) in the worst case (e.g. skewed tree): at each node we compute height of its subtree, and heights are computed repeatedly for overlapping subtrees.
  - **Space**: O(h) for recursion stack, h = height.

- **Optimal**
  - **Time**: O(n) — each node is visited once.
  - **Space**: O(h) for recursion stack.

## Edge Cases

- `root is None` → return `True`.
- Single node → balanced (left and right heights 0).
- Only one child at root → check |1 - 0| = 1 → balanced.
- Deep imbalance in a subtree → -1 propagates to root.

## Common Mistakes

- **Checking only the root** — You must ensure every node’s left and right heights differ by at most 1; a tree can be unbalanced at an internal node even if the root looks fine.
- **O(n²) when O(n) is possible** — Computing height in a separate pass per node leads to repeated work; combine height and balance in one DFS.
- **Wrong height convention** — Be consistent (e.g. empty = 0, then height = 1 + max(left, right)); the inequality `abs(left - right) <= 1` is what matters.

## Related Problems

- [LC 104: Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/) — Height of tree.
- [LC 543: Diameter of Binary Tree](/2026/03/06/easy-543-diameter-of-binary-tree/) — Similar “return depth, update global max” DFS.
- [LC 124: Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/) — DFS returning a value and using a global/side result.
- [LC 114: Flatten Binary Tree to Linked List](https://leetcode.com/problems/flatten-binary-tree-to-linked-list/) — Tree manipulation.
