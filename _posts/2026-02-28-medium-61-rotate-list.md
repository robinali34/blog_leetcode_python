---
layout: post
title: "61. Rotate List"
date: 2026-02-28 00:00:00 -0700
categories: [leetcode, medium, linked-list, python]
permalink: /2026/02/28/medium-61-rotate-list/
tags: [leetcode, medium, linked-list, two-pointers]
---

# 61. Rotate List

## Problem Statement

Given the head of a singly linked list, rotate the list to the right by `k` places. That is, the last `k` nodes (or fewer if the list is short) are moved to the front. The list is modified in place; you return the new head.

**Example:** `1 → 2 → 3 → 4 → 5` with `k = 2` becomes `4 → 5 → 1 → 2 → 3`.

## Examples

**Example 1:**
```
Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]
Explanation: Rotate right by 2: last two nodes (4, 5) move to the front.
```

**Example 2:**
```
Input: head = [0,1,2], k = 4
Output: [2,0,1]
Explanation: k = 4 with n = 3 is equivalent to k = 1 (rotate right once).
```

**Example 3:**
```
Input: head = [1,2], k = 1
Output: [2,1]
```

## Constraints

- The number of nodes in the list is in the range `[0, 500]`.
- `-100 <= Node.val <= 100`
- `0 <= k <= 2 * 10^9`

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Rotation direction**: Rotate “right” means the last nodes move to the front? (Assumption: Yes — last `k` nodes become the new head segment.)

2. **Empty or single node**: What if `head` is null or there is only one node? (Assumption: Return `head` as-is; no rotation needed.)

3. **k larger than length**: If `k >= n`, how do we interpret? (Assumption: Effective rotation is `k % n`; rotating by `n` leaves the list unchanged.)

4. **In-place**: Must we do it in O(1) extra space? (Assumption: Prefer O(1) space; no copying nodes into an array.)

5. **Singly linked list**: Do we have only `next` pointers? (Assumption: Yes — singly linked; we need to find the tail and new tail in one or two passes.)

## Interview Deduction Process (20 minutes)

**Step 1: Brute-Force Approach (5 minutes)**

Rotate one step at a time: repeatedly take the last node, detach it, and put it at the front; do this `k` times. This is O(n) per step, so O(nk) total. When `k` can be up to 2×10^9, this is too slow. We need to use the fact that rotating by `n` leaves the list unchanged, so effective rotation is `k % n`.

**Step 2: Semi-Optimized Approach (7 minutes)**

Compute length `n`, then set `k = k % n`. To avoid O(nk) work, we can find the new head position: the new head is the node that is `n - k` steps from the start (0-indexed: position `n - k`). So we need a pointer at the tail and a pointer `n - k - 1` steps from the head; the node after that is the new head. We can do one pass to get length and tail, then a second pass to find the node at index `n - k - 1`, then break the list and reconnect. This is O(n) time, O(1) space.

**Step 3: Optimized Solution (8 minutes)**

Make the list circular: after getting length and tail, set `tail.next = head`. Then the new tail is exactly `n - k - 1` steps from the current head. Walk that many steps, set `new_head = new_tail.next`, then `new_tail.next = None`. One length pass, one pass to find the new tail — O(n) time, O(1) space. The circular trick avoids special cases for “finding the (n-k)-th node” and keeps the code clean.

## Solution Approach

This is a **linked list** problem that becomes easy once we use **modulo** (`k % n`) and the **circular list** idea. The key insight is that rotating right by `k` is the same as cutting the list at position `n - k` (0-based) and reconnecting the tail to the old head.

### Key Insights:

1. **Effective k**: Only `k % n` matters; rotating by `n` leaves the list unchanged.
2. **New head position**: The new head is the node at index `n - k` (0-based), i.e. the node after the one at index `n - k - 1`.
3. **Circular list**: If we set `tail.next = head`, then walking `n - k - 1` steps from `head` lands on the new tail; the next node is the new head.
4. **Edge cases**: Empty list, single node, or `k % n == 0` → return `head` unchanged.

## Solution

### **Solution 1: Make List Circular (O(n) time, O(1) space)**

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        # Compute length and find tail
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1

        k %= length
        if k == 0:
            return head

        # Make it circular
        tail.next = head

        # Find new tail (length - k - 1 steps from head)
        steps_to_new_tail = length - k - 1
        new_tail = head
        for _ in range(steps_to_new_tail):
            new_tail = new_tail.next

        new_head = new_tail.next
        new_tail.next = None
        return new_head
```

### **Algorithm Explanation:**

1. **Edge cases (Lines 15–16)**: If list is empty, has one node, or `k == 0`, return `head`.
2. **Length and tail (Lines 18–23)**: One pass to count nodes and keep a pointer to the last node.
3. **Effective k (Lines 25–27)**: Set `k = k % length`; if 0, return `head`.
4. **Make circular (Line 30)**: `tail.next = head` so we can traverse from head to the “previous” tail.
5. **Find new tail (Lines 33–36)**: Walk `length - k - 1` steps from `head`; that node is the new tail.
6. **Break and return (Lines 38–40)**: `new_head = new_tail.next`, then `new_tail.next = None`, return `new_head`.

### **Why This Works:**

- **Modulo**: `k % n` reduces any large `k` to a value in `[0, n-1]`, so we never do more than one full “rotation.”
- **Circular list**: Connecting tail to head lets us treat the list as a ring; the node at offset `n - k - 1` from the start is the new tail, and its successor is the new head.
- **Single pass for length**: We need `n` to compute `k % n` and the number of steps to the new tail; one traversal is enough.

### **Example Walkthrough:**

**For `head = [1,2,3,4,5]`, `k = 2`:**

```
Length n = 5, k % 5 = 2.
Make circular: 1 → 2 → 3 → 4 → 5 → 1 (cycle).

New tail index = n - k - 1 = 5 - 2 - 1 = 2 (0-based).
Walk 2 steps from head: 1 → 2 → 3. So new_tail = node 3.

new_head = new_tail.next = node 4.
new_tail.next = None → list is 4 → 5 → 1 → 2 → 3.

Return node 4.
```

### **Solution 2: Two Passes Without Making Circular**

Alternatively, get length and tail in one pass, then in a second pass find the node at index `n - k - 1` (new tail), break the list there, and reconnect the tail to the old head. Same O(n) time and O(1) space; the circular approach just avoids reconnecting pointers in a separate step.

### **Complexity Analysis:**

**Solution 1 (Circular):**
- **Time Complexity:** O(n) — one pass for length and tail, one pass to find the new tail.
- **Space Complexity:** O(1) — only a few pointers.

**Solution 2 (Two passes, no circle):**
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

### **Key Differences from LC 189 (Rotate Array):**

1. **Structure**: Linked list has no random access; we need to traverse to find the new tail. Array can use index arithmetic and reverse operations.
2. **In-place**: For a list, “in-place” means O(1) extra space by rewiring pointers; no extra array.

### **Edge Cases:**

1. **Empty list**: `head is None` → return `None`.
2. **Single node**: Return `head`; rotation has no effect.
3. **k == 0**: Return `head`.
4. **k >= n**: Use `k % n`; e.g. `n = 3`, `k = 4` → effective `k = 1`.

### **Common Mistakes:**

1. **Forgetting `k % n`**: When `k` is large, rotating one-by-one is too slow; always reduce to `k % length`.
2. **Off-by-one**: The new tail is at index `n - k - 1` (0-based), not `n - k`. The new head is the next node after the new tail.
3. **Not handling k % n == 0**: After reducing `k`, if `k == 0`, the list is unchanged; return `head` without making it circular.

### **Related Problems:**

- [LC 189: Rotate Array](https://leetcode.com/problems/rotate-array/) — Similar idea with an array
- [LC 21: Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/) — Linked list basics
- [LC 206: Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) — Pointer manipulation
