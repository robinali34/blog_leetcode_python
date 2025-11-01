---
layout: post
title: "LC 863: All Nodes Distance K in Binary Tree"
date: 2025-10-25 13:00:00 -0700
categories: leetcode medium tree dfs bfs
permalink: /posts/2025-10-25-medium-863-all-nodes-distance-k-in-binary-tree/
tags: [leetcode, medium, tree, binary-tree, dfs, bfs, graph, recursion]
---

# LC 863: All Nodes Distance K in Binary Tree

**Difficulty:** Medium  
**Category:** Tree, DFS, BFS  
**Companies:** Amazon, Facebook, Google, Microsoft, Apple

## Problem Statement

Given the `root` of a binary tree, the value of a `target` node, and an integer `k`, return an array of the values of all nodes that have a distance `k` from the target node.

You can return the answer in any order.

### Examples

**Example 1:**
```
Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
Output: [7,4,1]
Explanation: The nodes that are a distance 2 from the target node (value 5) have values 7, 4, and 1.
```

**Example 2:**
```
Input: root = [1], target = 1, k = 3
Output: []
```

### Constraints

- The number of nodes in the tree is in the range `[1, 500]`.
- `0 <= Node.val <= 500`
- All the values `Node.val` are unique.
- `target` is the value of one of the nodes in the tree.
- `k >= 0`

## Solution Approaches

### Approach 1: Convert Tree to Graph with DFS

**Key Insight:** Convert the binary tree into an undirected graph, then perform BFS/DFS from the target node to find all nodes at distance k.

**Algorithm:**
1. Build adjacency list by traversing the tree
2. Store parent-child relationships bidirectionally
3. Perform DFS starting from target node
4. Track visited nodes to avoid cycles
5. Collect nodes at exact distance k

**Time Complexity:** O(n)  
**Space Complexity:** O(n)

```python
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     # val = 0
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

class Solution:
    def __init__(self):
        self.graph = {}
        self.result = []
        self.visited = set()
    
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> list[int]:
        self.buildGraph(root, None)
        self.visited.add(target.val)
        self.dfs(target.val, 0, k)
        return self.result
    
    def buildGraph(self, curr: TreeNode, parent: TreeNode) -> None:
        if curr and parent:
            if curr.val not in self.graph:
                self.graph[curr.val] = []
            if parent.val not in self.graph:
                self.graph[parent.val] = []
            self.graph[curr.val].append(parent.val)
            self.graph[parent.val].append(curr.val)
        if curr.left:
            self.buildGraph(curr.left, curr)
        if curr.right:
            self.buildGraph(curr.right, curr)
    
    def dfs(self, curr: int, dist: int, K: int) -> None:
        if dist == K:
            self.result.append(curr)
            return
        for neighbor in self.graph.get(curr, []):
            if neighbor not in self.visited:
                self.visited.add(neighbor)
                self.dfs(neighbor, dist + 1, K)
```

### Approach 2: Parent Pointer Map with DFS

**Key Insight:** Create a parent pointer map to traverse up the tree, then use DFS to explore all neighbors (left, right, parent).

**Algorithm:**
1. Traverse tree to build parent map
2. Start DFS from target node
3. For each node, explore left, right, and parent
4. Track visited nodes
5. Collect nodes at distance k

**Time Complexity:** O(n)  
**Space Complexity:** O(n)

```python
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     # val = 0
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

class Solution:
    def __init__(self):
        self.parent = {}
    
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> list[int]:
        self.addParent(root, None)
        result = []
        visited = set()
        self.dfs(target, k, result, visited)
        return result
    
    def addParent(self, curr: TreeNode, parent_node: TreeNode) -> None:
        if curr:
            self.parent[curr] = parent_node
            self.addParent(curr.left, curr)
            self.addParent(curr.right, curr)
    
    def dfs(self, curr: TreeNode, dist: int, rtn: list[int], visited: set) -> None:
        if not curr or curr in visited:
            return
        visited.add(curr)
        if dist == 0:
            rtn.append(curr.val)
            return
        if curr in self.parent:
            self.dfs(self.parent[curr], dist - 1, rtn, visited)
        self.dfs(curr.left, dist - 1, rtn, visited)
        self.dfs(curr.right, dist - 1, rtn, visited)
```

### Approach 3: BFS with Graph Representation

**Algorithm:**
1. Build adjacency list representation
2. Use BFS with queue to find nodes at distance k
3. Track level/distance during traversal
4. Collect nodes exactly at distance k

**Time Complexity:** O(n)  
**Space Complexity:** O(n)

```python
class Solution:
    def __init__(self):
        self.graph = {}
    
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> list[int]:
        self.buildGraph(root, None)
        from collections import deque
        
        result = []
        q = deque([(target.val, 0)])
        visited = {target.val}
        
        while q:
            curr, dist = q.popleft()
            
            if dist == k:
                result.append(curr)
            elif dist < k:
                for neighbor in self.graph.get(curr, []):
                    if neighbor not in visited:
                        visited.add(neighbor)
                        q.append((neighbor, dist + 1))
        return result
    
    def buildGraph(self, curr: TreeNode, parent: TreeNode) -> None:
        if curr and parent:
            if curr.val not in self.graph:
                self.graph[curr.val] = []
            if parent.val not in self.graph:
                self.graph[parent.val] = []
            self.graph[curr.val].append(parent.val)
            self.graph[parent.val].append(curr.val)
        if curr.left:
            self.buildGraph(curr.left, curr)
        if curr.right:
            self.buildGraph(curr.right, curr)
```

## Algorithm Analysis

### Approach Comparison

| Approach | Time | Space | Pros | Cons |
|----------|------|-------|------|------|
| Graph + DFS | O(n) | O(n) | Simple, intuitive | Extra memory for graph |
| Parent Map + DFS | O(n) | O(n) | No extra graph structure | More complex traversal |
| Graph + BFS | O(n) | O(n) | Level-order traversal | Slightly more code |

### Key Insights

1. **Tree as Graph**: Binary trees are directed acyclic graphs; adding parent pointers makes them undirected
2. **Multi-directional Search**: Can traverse up (parent) and down (children) in tree
3. **Cycle Prevention**: Must track visited nodes to avoid infinite loops
4. **Distance Tracking**: Depth-first or breadth-first approaches both work

## Implementation Details

### Building Parent-Child Relationships
```python
# Store bidirectional edges
if curr and parent:
    graph[curr.val].append(parent.val)
    graph[parent.val].append(curr.val)
```

### DFS with Distance Control
```python
def dfs(self, curr: int, dist: int, K: int) -> None:
    if dist == K:
        result.append(curr)
        return
    # Recursively explore all neighbors
    for neighbor in graph.get(curr, []):
        if neighbor not in visited:
            visited.add(neighbor)
            self.dfs(neighbor, dist + 1, K)
```

### Three-Directional Search
```python
// Explore: parent, left child, right child
dfs(parent[curr], dist - 1, rtn, visited);
dfs(curr->left, dist - 1, rtn, visited);
dfs(curr->right, dist - 1, rtn, visited);
```

## Edge Cases

1. **Target is Root**: Still works, no parent path
2. **k = 0**: Returns only target node
3. **Single Node Tree**: Returns empty array if k > 0
4. **k Beyond Tree Depth**: Returns empty array
5. **Target at Leaf**: Must go up to parent then down

## Follow-up Questions

- What if the tree had more than 2 children per node?
- How would you modify for a directed graph?
- What if nodes could have duplicate values?
- How would you find nodes within distance k (not exactly k)?

## Related Problems

- [LC 314: Binary Tree Vertical Order Traversal](https://leetcode.com/problems/binary-tree-vertical-order-traversal/)
- [LC 863: All Nodes Distance K](https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/) *(This problem)*
- [LC 1161: Maximum Level Sum of a Binary Tree](https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/)
- [LC 742: Closest Leaf in a Binary Tree](https://leetcode.com/problems/closest-leaf-in-a-binary-tree/)

## Optimization Techniques

1. **Graph Conversion**: O(n) one-time preprocessing
2. **Visited Tracking**: O(1) lookup prevents redundant work
3. **Early Termination**: Stop at distance k exactly
4. **Bidirectional Edges**: Store parent-child relationships for undirected graph behavior

## Code Quality Notes

1. **Clarity**: Graph approach is most intuitive for new learners
2. **Modularity**: Separate graph building from search logic
3. **Memory**: Both approaches use O(n) space for n nodes
4. **Performance**: All solutions are optimal O(n) time

---

*This problem beautifully demonstrates how binary trees can be treated as graphs when we need multi-directional traversal capabilities.*

