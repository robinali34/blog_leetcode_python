---
layout: post
title: "[Medium] 341. Flatten Nested List Iterator"
date: 2026-03-24 00:00:00 -0700
categories: [leetcode, medium, stack, iterator, design]
tags: [leetcode, medium, stack, iterator, nested-list]
permalink: /2026/03/24/medium-341-flatten-nested-list-iterator/
---

# [Medium] 341. Flatten Nested List Iterator

## Problem Statement

You are given a nested list of integers `nestedList`. Each element is either:

- a single integer, or
- a nested list of integers

Implement an iterator with the following methods:

- `next()`: returns the next integer in the flattened order
- `hasNext()`: returns `True` if there is at least one more integer to return

The flattened order is the left-to-right order of integers when fully expanded.

## Examples

**Example 1:**

```python
Input: nestedList = [[1,1],2,[1,1]]
Output: [1,1,2,1,1]
```

**Example 2:**

```python
Input: nestedList = [[],[3],[]]
Output: [3]
```

## Constraints

- The nested list is valid and consists of `NestedInteger` objects.
- `next()` is called only when `hasNext()` returns `True`.

## Clarification Questions

1. **How are integers vs lists distinguished?**  
   Use `NestedInteger.isInteger()`; if `True` then `getInteger()` returns the value.
2. **How do we expand a nested list?**  
   Use `NestedInteger.getList()` to get its children.
3. **Can `hasNext()` be called multiple times before `next()`?**  
   Yes; the iterator must not “skip” elements.
4. **Do we need to flatten eagerly?**  
   Not required; in fact, lazy evaluation is the typical solution.

## Analysis Process

### 1) Naive approach (eager flatten)

Flatten the entire nested structure into a plain list of integers in `__init__`, then iterate by index.

This is simple but uses extra space proportional to the total number of integers.

### 2) Lazy approach

We avoid expanding everything up front.

Maintain a stack of `NestedInteger` objects that represents what’s left to process.  

In `hasNext()`:

- Look at the top.
- If it’s an integer, `hasNext()` can return `True`.
- Otherwise it’s a list: pop it and push its children back onto the stack (in reverse so left-to-right order is preserved).

Each nested list node gets expanded at most once, giving **amortized** efficiency.

## Solution Options

### Option 1: Lazy Stack (Amortized O(1) per operation)

This is your solution: expand only when needed inside `hasNext()`.

```python
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#     def isInteger(self) -> bool:
#         return True if this NestedInteger holds a single integer
#     def getInteger(self) -> int:
#         return the single integer if it holds an integer
#     def getList(self) -> [NestedInteger]:
#         return the nested list if it holds a list

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stk = nestedList[::-1]
    
    def next(self) -> int:
        return self.stk.pop().getInteger()
    
    def hasNext(self) -> bool:
        while self.stk:
            top = self.stk[-1]
            if top.isInteger():
                return True
            self.stk.pop()
            self.stk.extend(top.getList()[::-1])
        return False
```

Key idea: pushing `top.getList()[::-1]` keeps the leftmost child on top of the stack.

### Option 2: Eager Flatten + Index Pointer

Precompute all integers in `__init__` with DFS, store them in an array, then iterate with a pointer.

```python
# class NestedInteger: ...

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.data = []
        self._flatten(nestedList)
        self.i = 0
    
    def _flatten(self, nestedList: [NestedInteger]) -> None:
        for x in nestedList:
            if x.isInteger():
                self.data.append(x.getInteger())
            else:
                self._flatten(x.getList())

    def next(self) -> int:
        v = self.data[self.i]
        self.i += 1
        return v
    
    def hasNext(self) -> bool:
        return self.i < len(self.data)
```

### Option 3: Stack-Based DFS Iterator Simulation (Same as Option 1, but phrased iteratively)

Option 1 already represents the standard iterative DFS simulation.  
So in interviews, it’s usually enough to present Option 1 and optionally mention Option 2 as a space trade-off.

## Comparison

| Option | Evaluation | `hasNext()` / `next()` | Extra Space | Notes |
|---|---|---|---|---|
| Lazy Stack | On-demand expansion | amortized O(1) | O(nested depth) to O(total nodes) worst-case | Best balance for iterator problems |
| Eager Flatten | Fully flatten in `__init__` | O(1) | O(#integers) | Simpler but uses more memory |

## Complexity Analysis

For Option 1 (lazy stack):

- **Time:** amortized `O(total nested items)` across all calls (each node/list is expanded once)
- **Space:** up to `O(total nested items)` in the worst case, typically closer to nesting depth

## Related Problems

- [LC 385: Mini Parser](https://leetcode.com/problems/mini-parser/)
- [LC 78: Subsets](https://leetcode.com/problems/subsets/)
