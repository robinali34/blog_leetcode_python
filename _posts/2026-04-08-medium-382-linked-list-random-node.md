---
layout: post
title: "[Medium] 382. Linked List Random Node"
date: 2026-04-08 00:00:00 -0700
categories: [leetcode, medium, linked-list, reservoir-sampling]
tags: [leetcode, medium, linked-list, random, reservoir-sampling]
permalink: /2026/04/08/medium-382-linked-list-random-node/
---

# [Medium] 382. Linked List Random Node

## Problem Statement

Given a singly linked list, implement a class such that:

- `__init__(head)` stores the list (or enough state to sample).
- `getRandom()` returns the value of a **uniformly random** node.

Each node has the same probability of being chosen.

## Examples

Each call to `getRandom` should behave like a fair draw over all current list nodes (list length fixed after construction).

## Constraints

- The number of nodes is in the range `[1, 10^4]`
- `-10^4 <= Node.val <= 10^4`
- At most `10^4` calls will be made to `getRandom`

## Clarification Questions

1. **Is list length unknown until we scan?** For reservoir sampling, we only need a stream; no need to know `n` upfront.
2. **Calls to `getRandom`:** Can be many; array approach uses O(n) space but O(1) per query after one linear scan in `__init__`.

## Solution Option 1: Reservoir sampling (O(1) space)

Traverse the list on each `getRandom`; keep one candidate and update with probability `1/i` for the `i`-th node (1-based), `i >= 2`.

```python
import random
from typing import Optional

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        rtn = self.head.val
        curr = self.head.next
        i = 2
        while curr:
            if random.randrange(i) == 0:
                rtn = curr.val
            curr = curr.next
            i += 1
        return rtn
```

`random.randrange(i)` returns uniform `0 .. i-1`, so probability of `0` is `1/i`.

## Solution Option 2: Copy values to array (O(n) space, O(1) `getRandom`)

```python
import random
from typing import Optional

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def __init__(self, head: Optional[ListNode]):
        self.values = []
        while head:
            self.values.append(head.val)
            head = head.next

    def getRandom(self) -> int:
        return random.choice(self.values)
```

## Comparison

| Approach | `__init__` | `getRandom` | Extra space |
|----------|------------|-------------|-------------|
| Reservoir | O(1) | O(n) time, one scan | O(1) |
| Array | O(n) | O(1) | O(n) |

## Complexity

- **Option 1:** space O(1); each `getRandom` costs O(n) time.  
- **Option 2:** space O(n); `getRandom` O(1) time.

## Related Problems

- [LC 398: Random Pick Index](https://leetcode.com/problems/random-pick-index/)
- [LC 528: Random Pick with Weight](https://leetcode.com/problems/random-pick-with-weight/)
