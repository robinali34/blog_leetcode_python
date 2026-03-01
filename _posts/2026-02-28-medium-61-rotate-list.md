---
layout: post
title: "61. Rotate List"
date: 2026-02-28 00:00:00 -0700
categories: leetcode algorithm medium python linked-list
permalink: /2026/02/28/medium-61-rotate-list/
tags: [leetcode, medium, linked-list, two-pointers]
---

# 61. Rotate List

**LeetCode 61 – Rotate List (Whiteboard-Style Analysis)**

## Problem Summary

Given the head of a singly linked list, rotate the list to the right by `k` places.

**Example:**
```
1 → 2 → 3 → 4 → 5, k = 2
Output: 4 → 5 → 1 → 2 → 3
```

## Examples

**Example 1:**
```
Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]
```

**Example 2:**
```
Input: head = [0,1,2], k = 4
Output: [2,0,1]
```

## Constraints

- The number of nodes in the list is in the range `[0, 500]`.
- `-100 <= Node.val <= 100`
- `0 <= k <= 2 * 10^9`

**Interview considerations:**
- Must be O(n) time
- Prefer O(1) extra space
- If `k >= n`, rotation repeats → equivalent to rotating by `k % n`

## 1. Clarify Constraints (Whiteboard Thinking)

- List length `n` can be 0 or up to ~500.
- `k` can be very large (up to 2×10^9), so we must use `k % n` to get effective rotation.
- Single pass for length, then one more pass or in-place pointer moves → O(n) time, O(1) space.

## 2. Key Insight

Instead of shifting nodes one by one (which would be O(nk)):

1. Count length `n`.
2. Compute effective rotation: `k = k % n`.
3. Make the list circular: `tail.next = head`.
4. Find the new tail (at position `n - k - 1` from start).
5. Break the circle: `new_head = new_tail.next`, `new_tail.next = None`.

## 3. Whiteboard Step-by-Step

Example: `1 → 2 → 3 → 4 → 5`, `k = 2`

- Length `n = 5`.
- Effective rotation: `k = 2 % 5 = 2`.
- New head position: `n - k = 3` steps from start (0-indexed position 3 is node 4).
- New tail: node at position `n - k - 1 = 2` (node 3).
- So: new tail = node 3, new head = node 4; break after 3, connect 5 → 1.

## 4. Algorithm Plan

1. **Edge cases**
   - If `head` is `None` → return `None`.
   - If only one node → return `head`.
   - If `k == 0` → return `head`.

2. **Count length and get tail**
   - Traverse once: count nodes and keep a pointer to the last node.

3. **Make circular**
   - `tail.next = head`.

4. **Find new tail**
   - Move `n - k - 1` steps from `head` (after `k %= n` and handling `k == 0`).

5. **Break circle**
   - `new_head = new_tail.next`
   - `new_tail.next = None`
   - Return `new_head`.

## 5. Complexity Analysis

- **Time:** O(n) — one pass for length, one for finding the new tail.
- **Space:** O(1) — only a few pointers.

## 6. Python Implementation (Clean & Interview-Ready)

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

        # Step 1: compute length and find tail
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1

        # Step 2: effective rotations
        k %= length
        if k == 0:
            return head

        # Step 3: make it circular
        tail.next = head

        # Step 4: find new tail (length - k - 1 steps from head)
        steps_to_new_tail = length - k - 1
        new_tail = head
        for _ in range(steps_to_new_tail):
            new_tail = new_tail.next

        # Step 5: break the circle
        new_head = new_tail.next
        new_tail.next = None

        return new_head
```

## 7. Why the Circular Method Works Best

- **Naive approach:** Rotate one step at a time → O(nk), too slow for large `k`.
- **Better approach:** Use modulo and the list structure:
  - One length pass + make circular + break at `(n - k)` gives O(n) time and O(1) space.
- This shows good use of the linked-list structure and edge-case handling.

## 8. Follow-Up Questions (Interview Mode)

- **What if we rotate left?**  
  Rotate right by `n - k` (or implement left by cutting at `k` and reconnecting).

- **Can we solve with two pointers without making the list circular?**  
  Yes: advance one pointer `k % n` steps, then move both until the first reaches the tail; the second is at the new tail. The circular version keeps the logic simple.

- **What if it were a doubly linked list?**  
  Same idea; update `prev`/`next` when breaking and reconnecting.

## 9. Final Whiteboard Summary

- **Core idea:** Rotate right by `k` = cut at position `n - k`, reconnect tail to head, then break at the new tail.
- **Steps:** Get length → `k %= n` → make circular → find new tail (`n - k - 1` steps) → break and return new head.

## Related Problems

- [189. Rotate Array](https://leetcode.com/problems/rotate-array/) — Similar idea with an array
- [21. Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/) — Linked list basics
- [206. Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) — Pointer manipulation
