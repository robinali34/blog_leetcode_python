---
layout: post
title: "[Medium] 92. Reverse Linked List II"
date: 2026-04-16 00:00:00 -0700
categories: [leetcode, medium, linked-list]
permalink: /2026/04/16/medium-92-reverse-linked-list-ii/
tags: [leetcode, medium, linked-list, in-place, head-insertion, pointer-manipulation]
---

# [Medium] 92. Reverse Linked List II

Given a singly linked list and two positions `left` and `right` (1-indexed),
reverse only the nodes between positions `[left, right]` in-place.

## Understand the Task Precisely

You only reverse a sublist, not the entire list.
Everything outside `[left, right]` must stay in original order.

## Break It Into Subproblems

1. Traverse to node before `left` (`prev`).
2. Reverse the sublist from `left` to `right`.
3. Reconnect:
   - `prev -> new head of reversed sublist`
   - `tail of reversed sublist -> right + 1`

## Key Observation (the trick)

Use the **head insertion** technique inside the sublist:

- keep `curr` at the start of the sublist
- repeatedly take `curr.next` and insert it right after `prev`

This keeps the solution in one pass after positioning pointers and avoids extra traversals.

## Edge Cases

- `left == 1` (head changes) -> use a dummy node
- `left == right` -> no-op
- very small lists

## Core Idea Visualization

Initial:

`dummy -> prev -> a -> b -> c -> d -> next`

Move `b` to the front of sublist:

`prev -> b -> a -> c -> d`

Move `c` to the front of sublist:

`prev -> c -> b -> a -> d`

## Complexity

- **Time:** `O(n)`
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
    def reverseBetween(
        self, head: Optional["ListNode"], left: int, right: int
    ) -> Optional["ListNode"]:
        if not head or left == right:
            return head

        dummy = ListNode(0, head)
        prev = dummy

        # Move prev to node before 'left'.
        for _ in range(left - 1):
            prev = prev.next

        # Reverse sublist using head insertion.
        curr = prev.next
        for _ in range(right - left):
            nxt = curr.next
            curr.next = nxt.next
            nxt.next = prev.next
            prev.next = nxt

        return dummy.next
```
