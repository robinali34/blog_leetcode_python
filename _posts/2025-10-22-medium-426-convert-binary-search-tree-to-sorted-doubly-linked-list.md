---
layout: post
title: "LC 426: Convert Binary Search Tree to Sorted Doubly Linked List"
date: 2025-10-22 12:00:00 -0700
categories: leetcode medium tree linked-list
permalink: /posts/2025-10-22-medium-426-convert-binary-search-tree-to-sorted-doubly-linked-list/
tags: [leetcode, medium, tree, linked-list, bst, inorder-traversal, recursion]
---

# LC 426: Convert Binary Search Tree to Sorted Doubly Linked List

**Difficulty:** Medium  
**Category:** Tree, Linked List, DFS  
**Companies:** Amazon, Microsoft, Facebook

## Problem Statement

Convert a Binary Search Tree to a sorted Circular Doubly Linked List in-place.

Think of the left and right pointers as synonymous to the previous and next pointers in a doubly-linked list. For a circular doubly linked list, the predecessor of the first element is the last element, and the successor of the last element is the first element.

We want to do the transformation in-place. After the transformation, the left pointer of the tree node should point to its predecessor, and the right pointer should point to its successor. You should return the pointer to the smallest element of the linked list.

### Examples

**Example 1:**
```
Input: root = [4,2,5,1,3]
Output: [1,2,3,4,5]
Explanation: The figure below shows the transformed BST. The solid line indicates the successor relationship, while the dashed line means the predecessor relationship.
```

**Example 2:**
```
Input: root = [2,1,3]
Output: [1,2,3]
```

### Constraints

- `-1000 <= Node.val <= 1000`
- `Node.left.val < Node.val < Node.right.val` (BST property)
- `1 <= Number of Nodes <= 1000`

## Solution Approaches

### Approach 1: Inorder Traversal with Global Variables (Recommended)

**Key Insight:** Use inorder traversal to visit nodes in sorted order, maintaining first and last nodes to build the doubly linked list.

**Algorithm:**
1. Use inorder traversal to process nodes in sorted order
2. Maintain global `first` and `last` pointers
3. For each node, connect it to the previous node
4. After traversal, connect first and last to make it circular

**Time Complexity:** O(n)  
**Space Complexity:** O(h) where h is height of tree

```python
class Solution:
    def __init__(self):
        self.first = None
        self.last = None
    
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return None
        self.inorder(root)
        self.last.right = self.first
        self.first.left = self.last
        return self.first
    
    def inorder(self, node: 'Node') -> None:
        if node:
            self.inorder(node.left)
            if self.last:
                self.last.right = node
                node.left = self.last
            else:
                self.first = node
            self.last = node
            self.inorder(node.right)
```

### Approach 2: Inorder Traversal with Return Values

**Algorithm:**
1. Perform inorder traversal
2. Return the head and tail of the doubly linked list
3. Connect the head and tail to make it circular

**Time Complexity:** O(n)  
**Space Complexity:** O(h)

```python
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return None
        
        head = [None]
        tail = [None]
        self.inorder(root, head, tail)
        
        head[0].left = tail[0]
        tail[0].right = head[0]
        return head[0]
    
    def inorder(self, node: 'Node', head: list, tail: list) -> None:
        if not node:
            return
        
        self.inorder(node.left, head, tail)
        
        if not head[0]:
            head[0] = node
        else:
            tail[0].right = node
            node.left = tail[0]
        tail[0] = node
        
        self.inorder(node.right, head, tail)
```

### Approach 3: Iterative Inorder Traversal

**Algorithm:**
1. Use iterative inorder traversal with stack
2. Process nodes in sorted order
3. Build doubly linked list incrementally
4. Connect first and last nodes

**Time Complexity:** O(n)  
**Space Complexity:** O(h)

```python
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return None
        
        stk = []
        first = None
        last = None
        curr = root
        
        while curr or stk:
            while curr:
                stk.append(curr)
                curr = curr.left
            
            curr = stk.pop()
            
            if not first:
                first = curr
            else:
                last.right = curr
                curr.left = last
            last = curr
            
            curr = curr.right
        
        first.left = last
        last.right = first
        return first
```
<｜tool▁calls▁begin｜><｜tool▁call▁begin｜>
read_file

## Algorithm Analysis

### Approach Comparison

| Approach | Time | Space | Pros | Cons |
|----------|------|-------|------|------|
| Global Variables | O(n) | O(h) | Simple, clean | Uses global state |
| Return Values | O(n) | O(h) | No global variables | More complex |
| Iterative | O(n) | O(h) | No recursion | More code |

### Key Insights

1. **Inorder Traversal**: BST inorder gives sorted order
2. **Doubly Linked List**: Each node needs left and right pointers
3. **Circular Connection**: Connect first and last nodes
4. **In-place Transformation**: Modify existing tree structure

## Implementation Details

### Global Variables Approach
```python
class Solution:
    def __init__(self):
        self.first = None
        self.last = None
    
    def inorder(self, node: 'Node') -> None:
        if node:
            self.inorder(node.left)
            # Process current node
            if self.last:
                self.last.right = node
                node.left = self.last
            else:
                self.first = node  # First node in sorted order
            self.last = node
            self.inorder(node.right)
```

### Circular Connection
```python
# After inorder traversal
self.last.right = self.first  # Last points to first
self.first.left = self.last   # First points to last
return self.first             # Return smallest element
```

## Edge Cases

1. **Empty Tree**: `nullptr` → return `nullptr`
2. **Single Node**: `[1]` → circular list with one node
3. **Left Skewed**: `[1,null,2,null,3]` → sorted order
4. **Right Skewed**: `[1,2,null,3]` → sorted order

## Follow-up Questions

- What if the tree wasn't a BST?
- How would you handle duplicate values?
- What if you needed a non-circular doubly linked list?
- How would you optimize for very large trees?

## Related Problems

- [LC 114: Flatten Binary Tree to Linked List](https://leetcode.com/problems/flatten-binary-tree-to-linked-list/)
- [LC 897: Increasing Order Search Tree](https://leetcode.com/problems/increasing-order-search-tree/)
- [LC 98: Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/)

## Optimization Techniques

1. **Inorder Traversal**: Leverage BST property for sorted order
2. **Global Variables**: Simplify state management
3. **In-place Transformation**: No extra space for new nodes
4. **Circular Connection**: Efficient circular list creation

## Code Quality Notes

1. **Readability**: Global variables approach is most intuitive
2. **Performance**: All approaches have O(n) time complexity
3. **Space Efficiency**: O(h) space for recursion stack
4. **Robustness**: Handles all edge cases correctly

---

*This problem demonstrates the power of inorder traversal on BSTs and shows how tree structures can be transformed into linked list structures while maintaining sorted order.*
