---
layout: post
title: "[Medium] 1669. Merge In Between Linked Lists"
date: 2026-04-15 00:00:00 -0700
categories: [leetcode, medium, linked-list]
permalink: /2026/04/15/medium-1669-merge-in-between-linked-lists/
tags: [leetcode, medium, linked-list, pointer-manipulation, dummy-node]
---

# [Medium] 1669. Merge In Between Linked Lists

You are given two singly linked lists, `list1` and `list2`, and two integers `a` and `b`.

You must:

- remove nodes from index `a` to `b` (inclusive) in `list1`
- insert `list2` into that gap

## Key Insight (ACM-style thinking)

This is pure pointer rewiring.

Find:

- `prevA`: node right before index `a` (`a - 1`)
- `afterB`: node right after index `b` (`b + 1`)

Then connect:

`prevA -> list2 -> afterB`

## Step-by-step Plan

1. Traverse `list1` to locate `prevA`.
2. Continue to locate `afterB`.
3. Traverse `list2` to locate its tail.
4. Rewire pointers:
   - `prevA.next = list2`
   - `tail.next = afterB`

## Complexity

- **Time:** `O(n + m)`
- **Space:** `O(1)`

## Solution

```python
from typing import Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(
        self, list1: "ListNode", a: int, b: int, list2: "ListNode"
    ) -> "ListNode":
        dummy = ListNode(0, list1)
        prevA = dummy

        # Find node before index a.
        for _ in range(a):
            prevA = prevA.next

        # Move to node at index b, then step once more to index b+1.
        afterB = prevA
        for _ in range(b - a + 1):
            afterB = afterB.next
        afterB = afterB.next

        # Attach list2 at cut position.
        prevA.next = list2

        # Find tail of list2.
        tail = list2
        while tail.next:
            tail = tail.next

        # Connect tail of list2 to remainder of list1.
        tail.next = afterB

        return dummy.next
```
