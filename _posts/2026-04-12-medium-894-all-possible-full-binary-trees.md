---
layout: post
title: "[Medium] 894. All Possible Full Binary Trees"
date: 2026-04-12 00:00:00 -0700
categories: [leetcode, medium, tree, dynamic-programming]
tags: [leetcode, medium, binary-tree, recursion, memoization]
permalink: /2026/04/12/medium-894-all-possible-full-binary-trees/
---

# [Medium] 894. All Possible Full Binary Trees

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

## Problem Summary

Generate **all** full binary trees with exactly `n` nodes.

A **full** binary tree means every node has **either 0 or 2** children (no node with exactly one child). Return every distinct tree structure.

## Key Observations

### 1. Valid `n` must be odd

In a full binary tree, every internal node has two children, so if there are `k` internal nodes then

`n = 2k + 1`

(all leaves are counted in `n`). Hence `n` is always odd. If `n` is even, no such tree exists → return an empty list.

### 2. Recursive structure (divide and conquer)

For `n > 1`, the root uses one node. If the left subtree has `i` nodes, the right subtree must have `n - 1 - i` nodes (subtract the root). **Both** subtrees must themselves be full binary trees, so `i` and `n - 1 - i` are odd. Try every odd split `i = 1, 3, 5, …, n - 2`.

### 3. Recurrence (Catalan-style growth)

Let `F(n)` be the list of all full binary trees with `n` nodes. Then

For each odd `i`, combine every tree in `F(i)` with every tree in `F(n - 1 - i)` under a new root (nested loops in code).

The **count** of trees grows like a **Catalan-type** sequence (not plain Catalan numbers, but the same “combine left and right enumerations” flavor).

### 4. Memoization

`dfs(i)` is recomputed for the same `i` in many branches. Cache `memo[n] = F(n)` so each subtree size is built once.

## Algorithm

1. If `n` is even → return `[]`.
2. Base case `n == 1` → return a single-node tree `[TreeNode(0)]`.
3. For each odd `i` from `1` to `n - 2`:
   - `left = dfs(i)`, `right = dfs(n - 1 - i)`.
   - For each pair `(l, r)`, attach under a new root and append to the result list.
4. Store and return `memo[n]`.

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

Let `T(n)` be the number of distinct full binary trees with `n` nodes (odd). The algorithm enumerates **all** of them, so time and space are driven by **output size**, which grows roughly with **Catalan-type** counts (exponential in `n` in the worst case).

- **Memoization** avoids recomputing the full list `F(i)` for the same `i` many times when combining subtrees, but you still pay for **building every tree** once.
- With `n <= 20`, this is feasible in practice.

That cost is **unavoidable** in the sense that the answer itself can be huge; you must materialize every returned tree.

## Common Mistakes

- Allowing even `n` (impossible for a non-empty full binary tree with that node count).
- Wrong split: left size `i`, right size `n - 1 - i`, not `n - i`.

## Related Problems

- [LC 95: Unique Binary Search Trees II](https://leetcode.com/problems/unique-binary-search-trees-ii/)
- [LC 96: Unique Binary Search Trees](https://leetcode.com/problems/unique-binary-search-trees/)
