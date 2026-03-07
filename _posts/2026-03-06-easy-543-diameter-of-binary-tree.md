---
layout: post
title: "543. Diameter of Binary Tree"
date: 2026-03-06 00:00:00 -0700
categories: [leetcode, easy, tree, dfs]
tags: [leetcode, easy, tree, diameter, height]
permalink: /2026/03/06/easy-543-diameter-of-binary-tree/
---

# 543. Diameter of Binary Tree

## Problem Statement

Given the `root` of a binary tree, return the **length of the diameter** of the tree.

The **diameter** is the longest path between any two nodes, measured by the **number of edges**. This path may or may not pass through the root.

## Examples

**Example 1:**

```python
Input: root = [1,2,3,4,5]
Output: 3
# Tree:    1
#         / \
#        2   3
#       / \
#      4   5
# Longest path: 4 → 2 → 1 → 3 (or 5 → 2 → 1 → 3), 3 edges.
```

**Example 2:**

```python
Input: root = [1,2]
Output: 1
# Tree:  1
#       /
#      2
# One edge between 1 and 2.
```

## Constraints

- The number of nodes in the tree is in the range `[1, 10^4]`.
- `-100 <= Node.val <= 100`

## Clarification Questions

1. **Empty tree**: Constraints say at least 1 node; no need to handle `root is None` for the problem, but we can return 0 for clarity.
2. **Length**: Diameter = number of **edges** on the longest path (not number of nodes).  
   **Assumption**: Yes.
3. **Path**: Path can be anywhere in the tree, not necessarily through the root.  
   **Assumption**: Yes — we must consider the best path through every node.

## Interview Deduction Process (20 minutes)

**Step 1: What is the diameter at a node? (5 min)**  
The longest path **through** a node is the longest path down its left subtree plus the longest path down its right subtree (in edges). So we need the “depth” of left and right (max edges from that child to a leaf), then candidate diameter = left_depth + right_depth (with the right depth convention).

**Step 2: Depth convention (5 min)**  
Define depth of a node = max number of edges from this node to a leaf. Empty: 0. Then depth(node) = 1 + max(depth(left), depth(right)). The path through node uses (depth(left)) edges on the left and (depth(right)) on the right, so diameter through node = depth(left) + depth(right). So we can use depth(None)=0 and depth = 1 + max(L,R); candidate = L + R.

**Step 3: Single DFS (10 min)**  
Recurse to get left and right depths. Update a global (or nonlocal) max with L + R. Return depth = 1 + max(L, R). O(n) time, O(h) space.

## Solution Approach

**DFS with depth return:** For each node, the diameter passing through it equals the sum of the maximum depths of its left and right subtrees (each “depth” = max edges to a leaf, with `None` → 0). So we run a DFS that returns this depth, and at each node we compute candidate diameter = left_depth + right_depth and update the answer. Return value for the parent is 1 + max(left_depth, right_depth).

### Key Insights

1. **Path through each node** — The longest path through a node is determined by the longest path down left + longest path down right (in edges).
2. **Depth once** — Return “depth” (max edges to a leaf) from the DFS so the parent can use it; no need to recompute.
3. **Global / nonlocal max** — The best path might not go through the root, so we update the maximum at every node and return only the depth for the recursion.

## Python Solution

### DFS (O(n) — single pass)

```python
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        best = 0

        def depth(node: Optional[TreeNode]) -> int:
            nonlocal best
            if node is None:
                return 0
            left_d = depth(node.left)
            right_d = depth(node.right)
            best = max(best, left_d + right_d)
            return 1 + max(left_d, right_d)

        depth(root)
        return best
```

## Algorithm Explanation

We define **depth** of a node as the maximum number of edges from that node to a leaf. Base case: `None` → 0. Recursive: depth = 1 + max(depth(left), depth(right)).

At each node, the longest path that **goes through** that node has length left_d + right_d (edges on the left chain plus edges on the right chain). We update a global maximum with this value. The return value is the depth so the parent can compute its own candidate diameter. The final answer is the maximum over all nodes.

## Complexity Analysis

- **Time**: O(n) — each node is visited once.
- **Space**: O(h) for the recursion stack, where h is the height of the tree (O(n) worst case for a skewed tree).

## Edge Cases

- Single node → depth 0, candidate 0; diameter = 0.
- Only one child (e.g. `[1,2]`) → left_d=1, right_d=0, candidate=1; diameter = 1.
- Diameter not through root — the DFS naturally considers every node, so the global max is correct.

## Common Mistakes

- **Only checking through root** — The max path might be entirely in one subtree; we must consider the candidate at every node.
- **Counting nodes instead of edges** — The problem asks for the number of edges; using “depth” as edges (depth(None)=0, depth = 1+max(L,R)) keeps candidate = L+R as the edge count.
- **Forgetting to update the max** — We must do `best = max(best, left_d + right_d)` at every node.

## Related Problems

- [LC 110: Balanced Binary Tree](/2026/03/06/easy-110-balanced-binary-tree/) — Also uses “return depth, combine left/right” DFS.
- [LC 124: Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/) — Similar “path through node” with a different aggregate (sum).
- [LC 687: Longest Univalue Path](https://leetcode.com/problems/longest-univalue-path/) — Longest path where all values are equal; same “through node” idea.
- [LC 104: Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/) — Depth definition used here.
