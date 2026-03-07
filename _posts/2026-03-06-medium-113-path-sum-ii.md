---
layout: post
title: "113. Path Sum II"
date: 2026-03-06 00:00:00 -0700
categories: [leetcode, medium, tree, dfs]
tags: [leetcode, medium, tree, path-sum, backtracking]
permalink: /2026/03/06/medium-113-path-sum-ii/
---

# 113. Path Sum II

## Problem Statement

Given the `root` of a binary tree and an integer `targetSum`, return **all root-to-leaf paths** where the sum of the node values in the path equals `targetSum`. Each path should be returned as a list of node values.

A **leaf** is a node with no children.

## Examples

**Example 1:**

```python
Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: [[5,4,11,2],[5,8,4,5]]
# Paths: 5+4+11+2 = 22 and 5+8+4+5 = 22.
# (Example tree may have 5 on right of 4; both paths shown.)
```

**Example 2:**

```python
Input: root = [1,2,3], targetSum = 5
Output: []
# Paths 1→2 sum 3, 1→3 sum 4. None sum to 5.
```

**Example 3:**

```python
Input: root = [1,2], targetSum = 0
Output: []
```

## Constraints

- The number of nodes in the tree is in the range `[0, 5000]`.
- `-1000 <= Node.val <= 1000`
- `-1000 <= targetSum <= 1000`

## Clarification Questions

1. **Empty tree**: Return empty list when `root is None`?  
   **Assumption**: Yes.
2. **Root-to-leaf only**: Only paths that end at a leaf count?  
   **Assumption**: Yes — same as LC 112.
3. **Order**: Any order of paths and any order of left/right in the tree is acceptable; we use left-to-right recursion for consistent path order.

## Interview Deduction Process (20 minutes)

**Step 1: Same as 112, but collect paths (5 min)**  
We still use “remaining” sum and only count root-to-leaf paths. When we find a leaf with remaining equal to the node’s value (after subtracting it), we have a valid path — we must record the **list of values** on the current path.

**Step 2: Backtracking (10 min)**  
Maintain a single mutable list “path”: at each node append `node.val`, recurse on left and right (if not a leaf), then **pop** to backtrack. When we find a valid leaf, append a **copy** of path to the result (e.g. `rtn.append(list(path))`).

**Step 3: Base case (5 min)**  
`node is None` → return without doing anything. Otherwise subtract `node.val` from remaining, append to path, check leaf + remaining == 0, recurse on children, pop.

## Solution Approach

**DFS with backtracking:** Use a shared list to build the current path. At each node: append `node.val`, subtract from remaining. If the node is a leaf and remaining is 0, append a **copy** of the path to the result. Recurse on left and right (order optional). Before returning, **pop** the current node from the path so the parent’s path is restored. This way we only use one list and O(h) space for the path plus result storage.

### Key Insights

1. **Backtrack with one list** — Push (append) before recursing, pop after; avoid building a new list per path.
2. **Append a copy** — When we find a valid path, do `rtn.append(list(pathNodes))` so later pops don’t mutate the stored path.
3. **Root-to-leaf** — Only add to result when the current node is a leaf and the sum matches.

## Python Solution

### DFS with backtracking

```python
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        rtn: List[List[int]] = []
        path_nodes: List[int] = []

        def traverse_paths(node: Optional[TreeNode], remaining_sum: int) -> None:
            if not node:
                return
            remaining_sum -= node.val
            path_nodes.append(node.val)

            if not node.left and not node.right and remaining_sum == 0:
                rtn.append(list(path_nodes))
            else:
                traverse_paths(node.left, remaining_sum)
                traverse_paths(node.right, remaining_sum)
            path_nodes.pop()

        traverse_paths(root, targetSum)
        return rtn
```

## Algorithm Explanation

We traverse from the root, maintaining `path_nodes` (current path) and `remaining_sum` (targetSum minus the sum of values so far). For each non-null node we subtract `node.val` from remaining and append it to `path_nodes`. If the node is a leaf and `remaining_sum == 0`, we append a **copy** of `path_nodes` to `rtn`. We then recurse on left and right. After both calls we pop the current node from `path_nodes` so the same list can be reused for other branches. Empty tree is handled by returning `[]` at the start.

## Complexity Analysis

- **Time**: O(n) — we visit each node once. Copying a path when we find a valid leaf is O(h) per path; in the worst case there can be O(n) such paths of length O(h), so worst case O(n·h). For a balanced tree that is O(n log n); often stated as O(n) when focusing on node visits.
- **Space**: O(h) for the recursion stack and the single `path_nodes` list; plus O(output) for the result list of paths.

## Edge Cases

- `root is None` → return `[]`.
- Single node: valid path iff `root.val == targetSum` → `[[root.val]]` or `[]`.
- No path sums to target → `[]`.
- Multiple paths can sum to target (e.g. Example 1).

## Common Mistakes

- **Forgetting to pop** — We must pop after recursing so the same list is correct for the parent’s other child.
- **Appending the same list** — Use `rtn.append(list(path_nodes))`; if we appended `path_nodes` itself, later pops would change the stored path.
- **Counting internal nodes** — Only add to result when the node is a leaf and remaining is 0.

## Related Problems

- [LC 112: Path Sum](/2026/03/06/easy-112-path-sum/) — Decide if any root-to-leaf path sums to target (boolean).
- [LC 437: Path Sum III](https://leetcode.com/problems/path-sum-iii/) — Count paths that sum to target (path can start/end at any node).
- [LC 129: Sum Root to Leaf Numbers](https://leetcode.com/problems/sum-root-to-leaf-numbers/) — Sum numbers formed by root-to-leaf paths.
- [LC 257: Binary Tree Paths](https://leetcode.com/problems/binary-tree-paths/) — Return all root-to-leaf paths (no sum condition).
<｜tool▁calls▁begin｜><｜tool▁call▁begin｜>
StrReplace