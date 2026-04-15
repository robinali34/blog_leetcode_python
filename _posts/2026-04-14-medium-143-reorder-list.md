---
layout: post
title: "[Medium] 143. Reorder List"
date: 2026-04-14 00:00:00 -0700
categories: [leetcode, medium, linked-list, two-pointers]
permalink: /2026/04/14/medium-143-reorder-list/
tags: [leetcode, medium, linked-list, fast-slow-pointers, reverse, merge]
---

# [Medium] 143. Reorder List

Given a singly linked list:

`L0 → L1 → L2 → … → Ln-1 → Ln`

Reorder it to:

`L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → …`

## Constraints / Rules

- You **cannot** modify node values, only pointers.
- Must be done **in-place**.

## Key Observation (ACM mindset)

This is not a simple traversal — it’s a structural transformation:

first node, last node, second node, second last node, …

That pattern screams:

**Split + Reverse + Merge**

## Optimal Strategy (3 steps)

### Step 1: Find the middle

Use fast & slow pointers:

- `slow` moves 1 step
- `fast` moves 2 steps

When `fast` reaches the end, `slow` is at (or near) the middle.

### Step 2: Reverse the second half

Cut the list after `slow`, then reverse the second half.

Example:

`1 → 2 → 3 → 4 → 5`

Second half: `4 → 5`  
Reversed: `5 → 4`

### Step 3: Merge the two halves

Interleave nodes:

First:  `1 → 2 → 3`  
Second: `5 → 4`

Result:

`1 → 5 → 2 → 4 → 3`

## Dry Run

Input:

`1 → 2 → 3 → 4 → 5`

- **Step 1:** `slow = 3`
- **Step 2:** reverse `4 → 5` to `5 → 4`
- **Step 3:** merge → `1 → 5 → 2 → 4 → 3`

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
    def reorderList(self, head: Optional["ListNode"]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return

        # Step 1: Find middle (slow)
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse 2nd half (starting at slow.next), then cut
        prev, curr = None, slow.next
        slow.next = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # Step 3: Merge two halves (head) and (prev)
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2
```
