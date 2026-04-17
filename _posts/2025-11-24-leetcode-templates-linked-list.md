---
layout: post
title: "Algorithm Templates: Linked List"
date: 2025-11-24 00:00:00 -0700
categories: leetcode templates linked-list
permalink: /posts/2025-11-24-leetcode-templates-linked-list/
tags: [leetcode, templates, linked-list]
---

{% raw %}
Minimal, copy-paste Python for traversal, two pointers, dummy node, reversal, merge, cycle detection, and circular list.

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
| 203 | Remove Linked List Elements | [Link](https://leetcode.com/problems/remove-linked-list-elements/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-11-18-easy-203-remove-linked-list-elements/) |
| 237 | Delete Node in a Linked List | [Link](https://leetcode.com/problems/delete-node-in-a-linked-list/) | - |

## Two Pointers

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
| 143 | Reorder List | [Link](https://leetcode.com/problems/reorder-list/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2026/04/14/medium-143-reorder-list/) |
| 1669 | Merge In Between Linked Lists | [Link](https://leetcode.com/problems/merge-in-between-linked-lists/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2026/04/15/medium-1669-merge-in-between-linked-lists/) |
| 92 | Reverse Linked List II | [Link](https://leetcode.com/problems/reverse-linked-list-ii/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2026/04/16/medium-92-reverse-linked-list-ii/) |
| 19 | Remove Nth Node From End of List | [Link](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) | - |

## Dummy Node Pattern

Use dummy node to simplify edge cases (empty list, head deletion).

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
| 203 | Remove Linked List Elements | [Link](https://leetcode.com/problems/remove-linked-list-elements/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-11-18-easy-203-remove-linked-list-elements/) |

## Reversal

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
| 206 | Reverse Linked List | [Link](https://leetcode.com/problems/reverse-linked-list/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-11-16-easy-206-reverse-linked-list/) |
| 92 | Reverse Linked List II | [Link](https://leetcode.com/problems/reverse-linked-list-ii/) | - |
| 25 | Reverse Nodes in k-Group | [Link](https://leetcode.com/problems/reverse-nodes-in-k-group/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/09/24/hard-25-reverse-nodes-in-k-group/) |
| 24 | Swap Nodes in Pairs | [Link](https://leetcode.com/problems/swap-nodes-in-pairs/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/09/24/medium-23-swap-nodes-in-pairs/) |

## Merge

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
| 23 | Merge k Sorted Lists | [Link](https://leetcode.com/problems/merge-k-sorted-lists/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/02/15/hard-23-merge-k-sorted-lists/) |
| 2 | Add Two Numbers | [Link](https://leetcode.com/problems/add-two-numbers/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-11-18-medium-2-add-two-numbers/) |

## Cycle Detection

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
| 708 | Insert into a Sorted Circular Linked List | [Link](https://leetcode.com/problems/insert-into-a-sorted-circular-linked-list/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-10-27-medium-708-insert-into-a-sorted-circular-linked-list/) |

## More templates

- **Data structures (pointers, recursion):** [Data Structures & Core Algorithms](/posts/2025-10-29-leetcode-templates-data-structures/)
- **Graph, Search:** [Graph](/posts/2025-10-29-leetcode-templates-graph/), [Search](/posts/2026-01-20-leetcode-templates-search/)
- **Master index:** [Categories & Templates](/posts/2025-10-29-leetcode-categories-and-templates/)
{% endraw %}

