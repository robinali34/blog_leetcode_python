---
layout: post
title: "[Easy] 876. Middle of the Linked List"
date: 2026-03-10 00:00:00 -0700
categories: [leetcode, easy, linked-list, two-pointers]
tags: [leetcode, easy, linked-list, fast-slow]
permalink: /2026/03/10/easy-876-middle-of-the-linked-list/
---

# [Easy] 876. Middle of the Linked List

## Problem Statement

Given the `head` of a singly linked list, return the **middle node** of the linked list.

If there are **two middle nodes** (even length), return the **second** middle node.

## Examples

**Example 1:**

```python
Input: head = [1,2,3,4,5]
Output: [3,4,5]
# Middle node is 3 (odd length).
```

**Example 2:**

```python
Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
# Two middles: 3 and 4; return the second one (4).
```

## Constraints

- The number of nodes in the list is in the range `[1, 100]`.
- `1 <= Node.val <= 100`

## Clarification Questions

1. **Two middles**: For even length, return the second of the two middle nodes?  
   **Assumption**: Yes — e.g. for 6 nodes, return the 4th (index 3).
2. **Single node**: Return that node.  
   **Assumption**: Yes.
3. **Modify list**: Should we leave the list unchanged?  
   **Assumption**: Yes — just return a pointer to the middle node.

## Interview Deduction Process (20 minutes)

**Step 1: Naive (5 min)**  
Count nodes in one pass, then traverse to the (n // 2)-th node (0-based). Two passes, O(n) time, O(1) space.

**Step 2: Fast and slow (10 min)**  
Use two pointers: `slow` and `fast` both start at `head`. Each step: `fast = fast.next.next`, `slow = slow.next`. Stop when `fast` is `None` or `fast.next` is `None`. Then `slow` is at the middle. One pass, O(1) space. For even length, stopping when `fast` is at the last node (fast.next is None) leaves `slow` at the second middle — which matches the problem.

**Step 3: Loop condition (5 min)**  
`while fast and fast.next:` ensures we don’t dereference None. After the loop, return `slow`.

## Solution Approach

**Fast and slow pointers:** Move `slow` one step and `fast` two steps at a time. When `fast` reaches the end (`fast` is None or `fast.next` is None), `slow` is at the middle. This yields the first middle for odd length and the second middle for even length (standard formulation).

**Alternatives:** (1) Count length then traverse to index `n // 2`. (2) Store nodes in an array and return `arr[len(arr)//2]` — O(n) space.

### Key Insights

1. **One pass** — Fast/slow avoids counting length first; when fast has moved 2x, slow has moved x, so slow is at the middle when fast is at the end.
2. **Stopping condition** — `while fast and fast.next` keeps fast from going past the last node; when we stop, slow is correct for both odd and even (second middle for even).
3. **O(1) space** — No array, no recursion; just two pointers.

## Python Solution

### Fast and slow pointers (O(n) time, O(1) space)

```python
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow
```

## Algorithm Explanation

We maintain `slow` and `fast` starting at `head`. In each iteration, `fast` advances two steps and `slow` one step. The loop runs while `fast` and `fast.next` are not None (so we never call `next` on None). When the loop ends, `fast` is either None (odd length: fast moved past the last node) or at the last node (even length: fast.next is None). In both cases, `slow` is at the desired middle: for odd length at the unique middle, for even length at the second of the two middle nodes. Return `slow`.

## Complexity Analysis

- **Time**: O(n) — one pass; slow traverses about n/2 nodes.
- **Space**: O(1) — two pointers only.

## Edge Cases

- **Single node** — fast is head, fast.next is None; we don’t enter the loop; return head. Correct.
- **Two nodes** — One step: fast = head.next.next = None; slow = head.next. We return the second node (second middle). Correct.
- **Odd length** — slow ends at the unique middle. Correct.

## Common Mistakes

- **Wrong loop condition** — Using only `while fast:` can lead to fast being at the last node and then fast = fast.next.next assigning None (ok) but we might have advanced slow one extra time if we’re not careful. The standard `while fast and fast.next` is safe and gives the “second middle” for even length.
- **Starting slow at head.next** — Some variants start fast one step ahead; then the “middle” might be the first middle for even length. Stick to both at head with the standard loop for the problem’s definition.

## Related Problems

- [LC 234: Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/) — Find middle then reverse second half.
- [LC 141: Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) — Fast/slow to detect cycle.
- [LC 19: Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) — Two pointers / one pass from end.
- [LC 206: Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) — Classic linked list.
