---
layout: post
title: "LC 545: Boundary of Binary Tree"
date: 2025-10-21 16:30:00 -0700
categories: leetcode medium tree dfs
permalink: /posts/2025-10-21-medium-545-boundary-of-binary-tree/
tags: [leetcode, medium, tree, dfs, binary-tree, boundary-traversal]
---

# LC 545: Boundary of Binary Tree

**Difficulty:** Medium  
**Category:** Tree, DFS, Binary Tree  
**Companies:** Amazon, Google, Facebook, Microsoft

## Problem Statement

Given a binary tree, return the values of its boundary in **anti-clockwise direction** starting from root. Boundary includes left boundary, leaves, and right boundary in order without duplicate nodes.

**Left boundary** is defined as the path from root to the left-most node. If the root doesn't have a left subtree, then the left boundary is empty.

**Right boundary** is defined as the path from root to the right-most node. If the root doesn't have a right subtree, then the right boundary is empty.

**Left-most node** is the leaf node you reach when you always travel to the left subtree if it exists. If not, travel to the right subtree. Stop when you reach a leaf node.

**Right-most node** is the leaf node you reach when you always travel to the right subtree if it exists. If not, travel to the left subtree. Stop when you reach a leaf node.

**Leaf nodes** are nodes that don't have any children.

### Examples

**Example 1:**
```
Input: root = [1,null,2,3,4]
Output: [1,3,4,2]
Explanation:
- The left boundary is empty because the root doesn't have a left child.
- The right boundary follows the path 1 -> 2 -> 4.
- The leaves from left to right are 3, 4.
- The anti-clockwise boundary is [1,3,4,2].
```

**Example 2:**
```
Input: root = [1,2,3,4,5,6,null,null,null,7,8,9,10]
Output: [1,2,4,7,8,9,10,6,3]
Explanation:
- The left boundary follows the path 1 -> 2 -> 4.
- The right boundary follows the path 1 -> 3 -> 6.
- The leaves from left to right are 4, 7, 8, 9, 10.
- The anti-clockwise boundary is [1,2,4,7,8,9,10,6,3].
```

### Constraints

- The number of nodes in the tree is in the range `[0, 10^4]`
- `-1000 <= Node.val <= 1000`

## Solution Approach

### Key Insight

The boundary traversal consists of three parts in order:
1. **Left boundary**: Root → leftmost node (excluding leaves)
2. **Leaves**: All leaf nodes from left to right
3. **Right boundary**: Rightmost node → root (excluding leaves, in reverse order)

### Approach: Three-Step Boundary Traversal

**Algorithm:**
1. Add root to result (if not a leaf)
2. Traverse left boundary (excluding leaves)
3. Traverse all leaves from left to right
4. Traverse right boundary (excluding leaves, in reverse order)

**Time Complexity:** O(n)  
**Space Complexity:** O(h) where h is height of tree

```python
class Solution:

    def boundaryOfBinaryTree(self, root: TreeNode) -> list[int]:
        if not root:
            return []
        result = []
        result.append(root.val)
        self.getleft(root.left, result)
        self.getleaf(root.left, result)
        self.getleaf(root.right, result)
        self.getright(root.right, result)
        return result
    
    def getleft(self, node: TreeNode, result: list[int]) -> None:
        if not node or (not node.left and not node.right):
            return
        result.append(node.val)
        if not node.left:
            self.getleft(node.right, result)
        else:
            self.getleft(node.left, result)
    
    def getleaf(self, node: TreeNode, result: list[int]) -> None:
        if not node:
            return
        self.getleaf(node.left, result)
        if not node.left and not node.right:
            result.append(node.val)
        self.getleaf(node.right, result)
    
    def getright(self, node: TreeNode, result: list[int]) -> None:
        if not node or (not node.left and not node.right):
            return
        if not node.right:
            self.getright(node.left, result)
        else:
            self.getright(node.right, result)
        result.append(node.val)
```

### Alternative Approach: Single Pass with Flags

**Algorithm:**
1. Use flags to track if a node is on left boundary, right boundary, or is a leaf
2. Traverse the tree once and collect nodes based on flags
3. Handle special cases for root and single-node trees

```python
class Solution:

    def boundaryOfBinaryTree(self, root: TreeNode) -> list[int]:
        result = []
        if not root:
            return result
        
        result.append(root.val)
        
        # Get left boundary (excluding root and leaves)
        self.getLeftBoundary(root.left, result)
        
        # Get all leaves
        self.getLeaves(root, result)
        
        # Get right boundary (excluding root and leaves)
        self.getRightBoundary(root.right, result)
        
        return result
    
    def getLeftBoundary(self, node: TreeNode, result: list[int]) -> None:
        if not node or (not node.left and not node.right):
            return
        
        result.append(node.val)
        
        if node.left:
            self.getLeftBoundary(node.left, result)
        else:
            self.getLeftBoundary(node.right, result)
    
    def getLeaves(self, node: TreeNode, result: list[int]) -> None:
        if not node:
            return
        
        if not node.left and not node.right:
            result.append(node.val)
            return
        
        self.getLeaves(node.left, result)
        self.getLeaves(node.right, result)
    
    def getRightBoundary(self, node: TreeNode, result: list[int]) -> None:
        if not node or (not node.left and not node.right):
            return
        
        if node.right:
            self.getRightBoundary(node.right, result)
        else:
            self.getRightBoundary(node.left, result)
        
        result.append(node.val)
```

## Detailed Algorithm Breakdown

### 1. Left Boundary Traversal
- Start from root's left child
- Always prefer left child if exists, otherwise go right
- Stop when reaching a leaf node
- Add nodes to result during traversal

### 2. Leaf Traversal
- Perform inorder traversal to get leaves from left to right
- Add only leaf nodes (nodes with no children)
- Skip non-leaf nodes

### 3. Right Boundary Traversal
- Start from root's right child
- Always prefer right child if exists, otherwise go left
- Stop when reaching a leaf node
- Add nodes to result **after** recursive calls (reverse order)

## Edge Cases Handling

1. **Empty Tree**: Return empty vector
2. **Single Node**: Return [root->val]
3. **Root is Leaf**: Only add root once
4. **No Left/Right Subtree**: Handle gracefully in boundary functions

## Complexity Analysis

| Aspect | Complexity | Explanation |
|--------|------------|-------------|
| Time | O(n) | Visit each node exactly once |
| Space | O(h) | Recursion stack depth equals tree height |

## Key Implementation Details

1. **Leaf Check**: `!node->left && !node->right`
2. **Boundary Logic**: Prefer left/right child, fallback to other child
3. **Order Matters**: Left boundary → Leaves → Right boundary (reversed)
4. **Duplicate Prevention**: Each node appears exactly once in result

## Follow-up Questions

- What if we need the boundary in clockwise direction?
- How would you handle duplicate values in the tree?
- What if we need to find the boundary of a general tree (not binary)?

## Related Problems

- [LC 199: Binary Tree Right Side View](https://leetcode.com/problems/binary-tree-right-side-view/)
- [LC 257: Binary Tree Paths](https://leetcode.com/problems/binary-tree-paths/)
- [LC 113: Path Sum II](https://leetcode.com/problems/path-sum-ii/)

## Implementation Notes

1. **Recursive Approach**: Clean and intuitive implementation
2. **Boundary Detection**: Use child existence to determine boundary
3. **Order Preservation**: Maintain anti-clockwise order throughout
4. **Memory Efficiency**: O(h) space complexity for balanced trees

---

*This problem demonstrates tree traversal techniques and the importance of understanding boundary conditions in tree problems.*
