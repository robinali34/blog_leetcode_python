---
layout: post
title: "894. All Possible Full Binary Trees"
date: 2026-04-12 00:00:00 -0700
categories: [leetcode, medium, tree, dynamic-programming]
tags: [leetcode, medium, binary-tree, recursion, memoization]
permalink: /2026/04/12/medium-894-all-possible-full-binary-trees/
---

# 894. All Possible Full Binary Trees

## Problem Statement

Given an integer `n`, return a list of **all possible** full binary trees with exactly `n` nodes. Each node has `val == 0`.

A **full binary tree** is a binary tree where every node has either `0` or `2` children.

Return the answer in **any order**.

## Examples

**Example 1:**

```python
Input: n = 7
Output: [ list of all distinct full binary trees with 7 nodes ]
```

**Example 2:**

```python
Input: n = 3
Output: [ one full tree: root with two leaves ]
```

## Constraints

- `1 <= n <= 20`

## Analysis

A full binary tree on `n` nodes exists **only if `n` is odd** (even `n` → return `[]`).

For `n > 1`, the root has two non-empty subtrees. If the left subtree has `i` nodes, the right has `n - 1 - i` nodes (subtract root). Both must be odd, so iterate `i = 1, 3, 5, …, n-2`.

Combine every left tree with every right tree under a new root. **Memoize** by `n` to avoid recomputing lists for the same subtree size.

## Python Solution

```python
from typing import List, Optional

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        memo = {}

        def dfs(n: int) -> List[Optional[TreeNode]]:
            if n % 2 == 0:
                return []
            if n == 1:
                return [TreeNode(0)]
            if n in memo:
                return memo[n]

            rtn = []
            for i in range(1, n, 2):
                left = dfs(i)
                right = dfs(n - 1 - i)
                for l in left:
                    for r in right:
                        root = TreeNode(0)
                        root.left = l
                        root.right = r
                        rtn.append(root)
            memo[n] = rtn
            return rtn

        return dfs(n)
```

## Complexity

Let `F(n)` be the number of full binary trees with `n` nodes (Catalan-type growth). Generating all trees is exponential in `n`; memoization avoids recomputing the list for each subtree size repeatedly.

- **Time / space:** dominated by output size (problem constraint `n <= 20` keeps it feasible).

## Common Mistakes

- Allowing even `n` (impossible for a non-empty full binary tree with that node count).
- Wrong split: left size `i`, right size `n - 1 - i`, not `n - i`.

## Related Problems

- [LC 95: Unique Binary Search Trees II](https://leetcode.com/problems/unique-binary-search-trees-ii/)
- [LC 96: Unique Binary Search Trees](https://leetcode.com/problems/unique-binary-search-trees/)
