---
layout: post
title: "Algorithm Templates: Linked List"
date: 2025-11-24 00:00:00 -0700
categories: leetcode templates linked-list
permalink: /posts/2025-11-24-leetcode-templates-linked-list/
tags: [leetcode, templates, linked-list]
---

{% raw %}
This page collects battle-tested C++ templates for every major linked-list pattern you'll see on LeetCode. Each section includes ready-to-use code, the signal phrases that tell you which pattern to reach for, and a quick explanation of the core idea. Bookmark it, copy what you need, and focus your energy on the actual problem logic.

> **New to Linked Lists?** A linked list is a chain of nodes where each node points to the next. Unlike arrays, you can't jump to index *i* — you must walk from the head. The tradeoff: O(1) insert/delete at known positions, but O(n) access.

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 220" style="max-width:680px;width:100%;height:auto;display:block;margin:1.5em auto">
  <style>
    .ll-node { fill: #A8B5A2; stroke: #6B7D65; stroke-width: 1.5; rx: 8; }
    .ll-dummy { fill: #C4A882; stroke: #9A7E5A; stroke-width: 1.5; rx: 8; }
    .ll-null { fill: #D4A5A5; stroke: #B07878; stroke-width: 1.5; rx: 8; }
    .ll-text { font-family: ui-monospace, SFMono-Regular, Menlo, monospace; font-size: 14px; fill: #3A3A3A; text-anchor: middle; dominant-baseline: central; }
    .ll-label { font-family: system-ui, -apple-system, sans-serif; font-size: 12px; fill: #6B6B6B; text-anchor: middle; }
    .ll-title { font-family: system-ui, -apple-system, sans-serif; font-size: 13px; fill: #555; font-weight: 600; }
    .ll-arrow { stroke: #7A7A7A; stroke-width: 1.5; fill: none; marker-end: url(#arrowhead); }
  </style>
  <defs>
    <marker id="arrowhead" markerWidth="8" markerHeight="6" refX="8" refY="3" orient="auto">
      <path d="M0,0 L8,3 L0,6 Z" fill="#7A7A7A"/>
    </marker>
  </defs>
  <!-- Row 1: Basic linked list -->
  <text x="30" y="18" class="ll-title">Basic linked list</text>
  <text x="55" y="45" class="ll-label">head</text>
  <line x1="55" y1="52" x2="55" y2="62" stroke="#999" stroke-width="1" marker-end="url(#arrowhead)"/>
  <rect x="20" y="65" width="70" height="35" class="ll-node"/>
  <text x="55" y="82" class="ll-text">1</text>
  <line x1="90" y1="82" x2="130" y2="82" class="ll-arrow"/>
  <rect x="130" y="65" width="70" height="35" class="ll-node"/>
  <text x="165" y="82" class="ll-text">2</text>
  <line x1="200" y1="82" x2="240" y2="82" class="ll-arrow"/>
  <rect x="240" y="65" width="70" height="35" class="ll-node"/>
  <text x="275" y="82" class="ll-text">3</text>
  <line x1="310" y1="82" x2="350" y2="82" class="ll-arrow"/>
  <rect x="350" y="65" width="70" height="35" class="ll-null"/>
  <text x="385" y="82" class="ll-text">null</text>
  <!-- Row 2: Dummy node pattern -->
  <text x="30" y="142" class="ll-title">Dummy node pattern</text>
  <text x="55" y="162" class="ll-label">dummy</text>
  <line x1="55" y1="169" x2="55" y2="177" stroke="#999" stroke-width="1" marker-end="url(#arrowhead)"/>
  <rect x="20" y="180" width="70" height="35" class="ll-dummy"/>
  <text x="55" y="197" class="ll-text">0</text>
  <line x1="90" y1="197" x2="130" y2="197" class="ll-arrow"/>
  <text x="165" y="162" class="ll-label">head</text>
  <line x1="165" y1="169" x2="165" y2="177" stroke="#999" stroke-width="1" marker-end="url(#arrowhead)"/>
  <rect x="130" y="180" width="70" height="35" class="ll-node"/>
  <text x="165" y="197" class="ll-text">1</text>
  <line x1="200" y1="197" x2="240" y2="197" class="ll-arrow"/>
  <rect x="240" y="180" width="70" height="35" class="ll-node"/>
  <text x="275" y="197" class="ll-text">2</text>
  <line x1="310" y1="197" x2="350" y2="197" class="ll-arrow"/>
  <rect x="350" y="180" width="70" height="35" class="ll-node"/>
  <text x="385" y="197" class="ll-text">3</text>
  <line x1="420" y1="197" x2="460" y2="197" class="ll-arrow"/>
  <rect x="460" y="180" width="70" height="35" class="ll-null"/>
  <text x="495" y="197" class="ll-text">null</text>
</svg>

## Contents

- [ListNode Definition](#listnode-definition)
- [Basic Operations](#basic-operations)
- [Two Pointers](#two-pointers)
- [Dummy Node Pattern](#dummy-node-pattern)
- [Reversal](#reversal)
- [Merge](#merge)
- [Cycle Detection](#cycle-detection)
- [Circular Linked List](#circular-linked-list)

## ListNode Definition

**When to use:** Every linked-list problem — this is the building block. Know the struct by heart so you never waste time on boilerplate.

### Standard Definition

```python
class ListNode:
    def __init__(self, val: int = 0, next=None):
        self.val = val
        self.next = next

```

### Alternative Definitions

```python
# Optional typing style
from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next

```

### Common Construction Methods

```python
class ListNode:
    def __init__(self, val: int = 0, next=None):
        self.val = val
        self.next = next


def create_list(values: list[int]) -> ListNode | None:
    if not values:
        return None
    head = ListNode(values[0])
    cur = head
    for x in values[1:]:
        cur.next = ListNode(x)
        cur = cur.next
    return head


def create_list_recursive(values: list[int], index: int = 0) -> ListNode | None:
    if index >= len(values):
        return None
    node = ListNode(values[index])
    node.next = create_list_recursive(values, index + 1)
    return node


def create_list_dummy(values: list[int]) -> ListNode | None:
    dummy = ListNode(0)
    cur = dummy
    for val in values:
        cur.next = ListNode(val)
        cur = cur.next
    return dummy.next

```

### Utility Functions

```python
class ListNode:
    def __init__(self, val: int = 0, next=None):
        self.val = val
        self.next = next


def print_list(head: ListNode | None) -> None:
    parts: list[str] = []
    cur = head
    while cur:
        parts.append(str(cur.val))
        cur = cur.next
    print(" -> ".join(parts))


def get_length(head: ListNode | None) -> int:
    n = 0
    cur = head
    while cur:
        n += 1
        cur = cur.next
    return n


def list_to_array(head: ListNode | None) -> list[int]:
    out: list[int] = []
    cur = head
    while cur:
        out.append(cur.val)
        cur = cur.next
    return out

```

### Example Usage

```python
class ListNode:
    def __init__(self, val: int = 0, next=None):
        self.val = val
        self.next = next


def create_list(values: list[int]) -> ListNode | None:
    if not values:
        return None
    h = ListNode(values[0])
    c = h
    for x in values[1:]:
        c.next = ListNode(x)
        c = c.next
    return h


head = create_list([1, 2, 3, 4, 5])
# print_list(head)  # 1 -> 2 -> 3 -> 4 -> 5
# get_length(head) == 5
# list_to_array(head) == [1, 2, 3, 4, 5]

```

## Basic Operations

**When to use:** You need to "visit every node", "count nodes", "find a value", or "collect values into an array". Also the foundation for insert/delete at arbitrary positions.

### Traversal

```python
class ListNode:
    def __init__(self, val: int = 0, next=None):
        self.val = val
        self.next = next


def traverse(head: ListNode | None) -> None:
    cur = head
    while cur:
        _ = cur.val
        cur = cur.next


def traverse_recursive(head: ListNode | None) -> None:
    if not head:
        return
    _ = head.val
    traverse_recursive(head.next)

```

### Insertion

```python
class ListNode:
    def __init__(self, val: int = 0, next=None):
        self.val = val
        self.next = next


def insert_at_head(head: ListNode | None, val: int) -> ListNode:
    node = ListNode(val, head)
    return node


def insert_after(node: ListNode, val: int) -> None:
    node.next = ListNode(val, node.next)

```

### Deletion

```python
class ListNode:
    def __init__(self, val: int = 0, next=None):
        self.val = val
        self.next = next


def delete_node_copy(node: ListNode) -> None:
    assert node.next
    node.val = node.next.val
    node.next = node.next.next


def delete_value(head: ListNode | None, val: int) -> ListNode | None:
    if not head:
        return None
    if head.val == val:
        return head.next
    cur = head
    while cur.next:
        if cur.next.val == val:
            cur.next = cur.next.next
            break
        cur = cur.next
    return head

```

| ID | Title | Link | Solution |
|---|---|---|---|
| 203 | Remove Linked List Elements | [Link](https://leetcode.com/problems/remove-linked-list-elements/) | [Solution](https://robinali34.github.io/blog_leetcode_python/posts/2025-11-18-easy-203-remove-linked-list-elements/) |
| 237 | Delete Node in a Linked List | [Link](https://leetcode.com/problems/delete-node-in-a-linked-list/) | - |

## Two Pointers

**When to use:** The problem says "middle of list", "kth from end", "intersection of two lists", or "split list into halves". Use fast/slow pointers to solve in one pass without knowing the length.

### Fast and Slow Pointers

```python
class ListNode:
    def __init__(self, val: int = 0, next=None):
        self.val = val
        self.next = next


def find_middle(head: ListNode | None) -> ListNode | None:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


def find_kth_from_end(head: ListNode | None, k: int) -> ListNode | None:
    fast = head
    for _ in range(k):
        if fast is None:
            return None
        fast = fast.next
    slow = head
    while fast:
        slow = slow.next
        fast = fast.next
    return slow

```

### Two Pointers for Partitioning

```python
class ListNode:
    def __init__(self, val: int = 0, next=None):
        self.val = val
        self.next = next


def partition(head: ListNode | None, x: int) -> ListNode | None:
    less = ListNode(0)
    greater = ListNode(0)
    less_cur, greater_cur = less, greater
    while head:
        if head.val < x:
            less_cur.next = head
            less_cur = less_cur.next
        else:
            greater_cur.next = head
            greater_cur = greater_cur.next
        head = head.next
    greater_cur.next = None
    less_cur.next = greater.next
    return less.next

```

| ID | Title | Link | Solution |
|---|---|---|---|
| 876 | Middle of the Linked List | [Link](https://leetcode.com/problems/middle-of-the-linked-list/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2026/03/10/easy-876-middle-of-the-linked-list/) |
| 19 | Remove Nth Node From End of List | [Link](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) | - |

## Dummy Node Pattern

**When to use:** The problem involves "delete head", "merge lists", "insert at front", or any operation where the head might change. A dummy node in front of head eliminates null-check edge cases.

```python
class ListNode:
    def __init__(self, val: int = 0, next=None):
        self.val = val
        self.next = next


def remove_elements(head: ListNode | None, val: int) -> ListNode | None:
    dummy = ListNode(0, head)
    cur = dummy
    while cur.next:
        if cur.next.val == val:
            cur.next = cur.next.next
        else:
            cur = cur.next
    return dummy.next

```

**Key Benefits:**
- Handles empty list case
- Simplifies head deletion
- Reduces special case handling

| ID | Title | Link | Solution |
|---|---|---|---|
| 203 | Remove Linked List Elements | [Link](https://leetcode.com/problems/remove-linked-list-elements/) | [Solution](https://robinali34.github.io/blog_leetcode_python/posts/2025-11-18-easy-203-remove-linked-list-elements/) |

## Reversal

**When to use:** The problem says "reverse linked list", "reverse between positions", "reverse in groups of k", or "palindrome linked list". The core trick is rewiring `next` pointers as you walk.

### Reverse Entire List

```python
class ListNode:
    def __init__(self, val: int = 0, next=None):
        self.val = val
        self.next = next


def reverse_list(head: ListNode | None) -> ListNode | None:
    prev, cur = None, head
    while cur:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt
    return prev


def reverse_list_recursive(head: ListNode | None) -> ListNode | None:
    if not head or not head.next:
        return head
    new_head = reverse_list_recursive(head.next)
    head.next.next = head
    head.next = None
    return new_head

```

### Reverse Between Positions

```python
class ListNode:
    def __init__(self, val: int = 0, next=None):
        self.val = val
        self.next = next


def reverse_between(head: ListNode | None, left: int, right: int) -> ListNode | None:
    dummy = ListNode(0, head)
    prev = dummy
    for _ in range(left - 1):
        prev = prev.next
    cur = prev.next
    for _ in range(right - left):
        nxt = cur.next
        cur.next = nxt.next
        nxt.next = prev.next
        prev.next = nxt
    return dummy.next

```

### Reverse in Groups

```python
class ListNode:
    def __init__(self, val: int = 0, next=None):
        self.val = val
        self.next = next


def reverse_k_group(head: ListNode | None, k: int) -> ListNode | None:
    cur = head
    for _ in range(k):
        if cur is None:
            return head
        cur = cur.next
    prev, cur = None, head
    for _ in range(k):
        nxt = cur.next
        cur.next = prev
        prev, cur = cur, nxt
    head.next = reverse_k_group(cur, k)
    return prev

```

| ID | Title | Link | Solution |
|---|---|---|---|
| 206 | Reverse Linked List | [Link](https://leetcode.com/problems/reverse-linked-list/) | [Solution](https://robinali34.github.io/blog_leetcode_python/posts/2025-11-16-easy-206-reverse-linked-list/) |
| 92 | Reverse Linked List II | [Link](https://leetcode.com/problems/reverse-linked-list-ii/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2026/04/16/medium-92-reverse-linked-list-ii/) |
| 25 | Reverse Nodes in k-Group | [Link](https://leetcode.com/problems/reverse-nodes-in-k-group/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2025/09/24/hard-25-reverse-nodes-in-k-group/) |
| 24 | Swap Nodes in Pairs | [Link](https://leetcode.com/problems/swap-nodes-in-pairs/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2025/09/24/medium-23-swap-nodes-in-pairs/) |

## Merge

**When to use:** The problem says "merge two sorted lists", "merge k sorted lists", or "add two numbers represented as lists". Compare heads, advance the smaller, and use a dummy node to collect the result.

### Merge Two Sorted Lists

```python
class ListNode:
    def __init__(self, val: int = 0, next=None):
        self.val = val
        self.next = next


def merge_two_lists(list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
    dummy = ListNode(0)
    cur = dummy
    while list1 and list2:
        if list1.val <= list2.val:
            cur.next = list1
            list1 = list1.next
        else:
            cur.next = list2
            list2 = list2.next
        cur = cur.next
    cur.next = list1 or list2
    return dummy.next

```

### Merge K Sorted Lists

```python
class ListNode:
    def __init__(self, val: int = 0, next=None):
        self.val = val
        self.next = next


def merge_two_lists(a: ListNode | None, b: ListNode | None) -> ListNode | None:
    dummy = ListNode(0)
    cur = dummy
    while a and b:
        if a.val <= b.val:
            cur.next, a = a, a.next
        else:
            cur.next, b = b, b.next
        cur = cur.next
    cur.next = a or b
    return dummy.next


def merge_k_lists(lists: list[ListNode | None]) -> ListNode | None:
    if not lists:
        return None

    def helper(lo: int, hi: int) -> ListNode | None:
        if lo == hi:
            return lists[lo]
        mid = (lo + hi) // 2
        return merge_two_lists(helper(lo, mid), helper(mid + 1, hi))

    return helper(0, len(lists) - 1)

```

| ID | Title | Link | Solution |
|---|---|---|---|
| 21 | Merge Two Sorted Lists | [Link](https://leetcode.com/problems/merge-two-sorted-lists/) | - |
| 23 | Merge k Sorted Lists | [Link](https://leetcode.com/problems/merge-k-sorted-lists/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2026/02/15/hard-23-merge-k-sorted-lists/) |
| 2 | Add Two Numbers | [Link](https://leetcode.com/problems/add-two-numbers/) | [Solution](https://robinali34.github.io/blog_leetcode_python/posts/2025-11-18-medium-2-add-two-numbers/) |
| 1669 | Merge In Between Linked Lists | [Link](https://leetcode.com/problems/merge-in-between-linked-lists/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2026/04/15/medium-1669-merge-in-between-linked-lists/) |

## Cycle Detection

**When to use:** The problem asks "has cycle", "find cycle start", or "find the duplicate number" (which reduces to cycle detection). Floyd's algorithm: if fast and slow meet, there's a cycle.

### Detect Cycle (Floyd's Algorithm)

```python
class ListNode:
    def __init__(self, val: int = 0, next=None):
        self.val = val
        self.next = next


def has_cycle(head: ListNode | None) -> bool:
    if not head or not head.next:
        return False
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False


def detect_cycle(head: ListNode | None) -> ListNode | None:
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            break
    else:
        return None
    slow = head
    while slow is not fast:
        slow = slow.next
        fast = fast.next
    return slow

```

| ID | Title | Link | Solution |
|---|---|---|---|
| 141 | Linked List Cycle | [Link](https://leetcode.com/problems/linked-list-cycle/) | - |
| 142 | Linked List Cycle II | [Link](https://leetcode.com/problems/linked-list-cycle-ii/) | - |

## Circular Linked List

**When to use:** The problem mentions "circular linked list", "sorted circular list", or "rotate list". The key difference from normal lists: the tail's `next` points back to the head instead of `nullptr`.

### Insert into Sorted Circular List

```python
class ListNode:
    def __init__(self, val: int = 0, next=None):
        self.val = val
        self.next = next


def insert_circular(head: ListNode | None, insert_val: int) -> ListNode:
    if not head:
        node = ListNode(insert_val)
        node.next = node
        return node
    prev, cur = head, head.next
    while cur is not head:
        if prev.val <= insert_val <= cur.val:
            break
        if prev.val > cur.val and (insert_val >= prev.val or insert_val <= cur.val):
            break
        prev, cur = cur, cur.next
    prev.next = ListNode(insert_val, cur)
    return head

```

| ID | Title | Link | Solution |
|---|---|---|---|
| 708 | Insert into a Sorted Circular Linked List | [Link](https://leetcode.com/problems/insert-into-a-sorted-circular-linked-list/) | [Solution](https://robinali34.github.io/blog_leetcode_python/posts/2025-10-27-medium-708-insert-into-a-sorted-circular-linked-list/) |
| 382 | Linked List Random Node | [Link](https://leetcode.com/problems/linked-list-random-node/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2026/04/08/medium-382-linked-list-random-node/) |

## Quick-Reference Summary

| Pattern | Signal Phrases | Key Idea |
|---|---|---|
| Two Pointers | "middle", "kth from end", "intersection" | Fast moves 2x, slow moves 1x |
| Dummy Node | "delete head", "merge", "insert at front" | Avoids null-check edge cases |
| Reversal | "reverse list", "reverse between" | Rewire next pointers |
| Merge | "merge sorted", "merge k lists" | Compare heads, advance smaller |
| Cycle Detection | "has cycle", "cycle start" | Floyd's: fast meets slow = cycle |

## More templates

- **Beginner's Guide:** [LeetCode Beginner's Guide](/2026/06/25/leetcode-beginners-guide/)
- **Data structures (pointers, recursion):** [Data Structures & Core Algorithms](/posts/2025-10-29-leetcode-templates-data-structures/)
- **Graph, Search:** [Graph](/posts/2025-10-29-leetcode-templates-graph/), [Search](/posts/2026-01-20-leetcode-templates-search/)
- **Master index:** [Categories & Templates](/posts/2025-10-29-leetcode-categories-and-templates/)
{% endraw %}

