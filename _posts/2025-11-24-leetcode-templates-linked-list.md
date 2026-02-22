---
layout: post
title: "Algorithm Templates: Linked List"
date: 2025-11-24 00:00:00 -0700
categories: leetcode templates linked-list
permalink: /posts/2025-11-24-leetcode-templates-linked-list/
tags: [leetcode, templates, linked-list]
---

{% raw %}
Minimal, copy-paste C++ for traversal, two pointers, dummy node, reversal, merge, cycle detection, and circular list.

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
// Standard ListNode definition used in LeetCode
struct ListNode :
val
ListNode next
ListNode() : val(0), next(None) :
ListNode(x) : val(x), next(None) :
ListNode(x, ListNode next) : val(x), next(next) :
```

### Alternative Definitions

```python
// Without default constructor
struct ListNode :
val
ListNode next
ListNode(x) : val(x), next(None) :
// With pointer initialization
struct ListNode :
val
ListNode next
ListNode(x = 0) : val(x), next(None) :
```

### Common Construction Methods

```python
// Method 1: Manual construction
def createList(self, values):
    if (not values) return None
    ListNode head = ListNode(values[0])
    ListNode cur = head
    for (i = 1 i < len(values) i += 1) :
    cur.next = ListNode(values[i])
    cur = cur.next
return head
// Method 2: Recursive construction
def createListRecursive(self, values, index):
    if (index >= len(values)) return None
    ListNode node = ListNode(values[index])
    node.next = createListRecursive(values, index + 1)
    return node
// Method 3: Using dummy node
def createListWithDummy(self, values):
    ListNode dummy = ListNode(0)
    ListNode cur = dummy
    for val in values:
        cur.next = ListNode(val)
        cur = cur.next
    return dummy.next
// Method 4: Create list from array
def createListFromArray(self, arr[], n):
    if (n == 0) return None
    ListNode head = ListNode(arr[0])
    ListNode cur = head
    for (i = 1 i < n i += 1) :
    cur.next = ListNode(arr[i])
    cur = cur.next
return head
```

### Utility Functions

```python
// Print linked list (for debugging)
def printList(self, head):
    ListNode cur = head
    while cur != None:
        cout << cur.val
        if (cur.next != None) cout << " . "
        cur = cur.next
    cout << endl
// Get length of linked list
def getLength(self, head):
    length = 0
    ListNode cur = head
    while cur != None:
        length += 1
        cur = cur.next
    return length
// Convert linked list to vector
def listToVector(self, head):
    list[int> result
    ListNode cur = head
    while cur != None:
        result.append(cur.val)
        cur = cur.next
    return result
// Delete entire linked list (free memory)
def deleteList(self, head):
    while head != None:
        ListNode temp = head
        head = head.next
        delete temp
```

### Example Usage

```python
// Example: Create list [1, 2, 3, 4, 5]
list[int> values = :1, 2, 3, 4, 5
ListNode head = createList(values)
// Print the list
printList(head)  // Output: 1 . 2 . 3 . 4 . 5
// Get length
len = getLength(head)  // len = 5
// Convert to vector
list[int> vec = listToVector(head)  // vec = [1, 2, 3, 4, 5]
// Clean up
deleteList(head)
```

## Basic Operations

### Traversal

```python
// Iterative traversal
def traverse(self, head):
    ListNode cur = head
    while cur != None:
        // Process cur.val
        cur = cur.next
// Recursive traversal
def traverseRecursive(self, head):
    if (head == None) return
    // Process head.val
    traverseRecursive(head.next)
```

### Insertion

```python
// Insert at head
def insertAtHead(self, head, val):
    ListNode newNode = ListNode(val)
    newNode.next = head
    return newNode
// Insert after node
def insertAfter(self, node, val):
    ListNode newNode = ListNode(val)
    newNode.next = node.next
    node.next = newNode
```

### Deletion

```python
// Delete node (given node to delete, not head)
def deleteNode(self, node):
    node.val = node.next.val
    node.next = node.next.next
// Delete node with value
def deleteNode(self, head, val):
    if (head == None) return None
    if (head.val == val) return head.next
    ListNode cur = head
    while cur.next != None:
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
// Find middle node
def findMiddle(self, head):
    ListNode slow = head
    ListNode fast = head
    while fast != None  and  fast.next != None:
        slow = slow.next
        fast = fast.next.next
    return slow
// Find kth node from end
def findKthFromEnd(self, head, k):
    ListNode fast = head
    for (i = 0 i < k i += 1) :
    if (fast == None) return None
    fast = fast.next
ListNode slow = head
while fast != None:
    slow = slow.next
    fast = fast.next
return slow
```

### Two Pointers for Partitioning

```python
// Partition list around value x
def partition(self, head, x):
    ListNode less = ListNode(0)
    ListNode greater = ListNode(0)
    ListNode lessCur = less
    ListNode greaterCur = greater
    while head != None:
        if head.val < x:
            lessCur.next = head
            lessCur = lessCur.next
             else :
            greaterCur.next = head
            greaterCur = greaterCur.next
        head = head.next
    greaterCur.next = None
    lessCur.next = greater.next
    return less.next
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 876 | Middle of the Linked List | [Link](https://leetcode.com/problems/middle-of-the-linked-list/) | - |
| 19 | Remove Nth Node From End of List | [Link](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) | - |

## Dummy Node Pattern

Use dummy node to simplify edge cases (empty list, head deletion).

```python
// Remove elements with dummy node
def removeElements(self, head, val):
    ListNode dummy = ListNode(0)
    dummy.next = head
    ListNode cur = dummy
    while cur.next != None:
        if cur.next.val == val:
            cur.next = cur.next.next
             else :
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
// Iterative reversal
def reverseList(self, head):
    ListNode prev = None
    ListNode cur = head
    while cur != None:
        ListNode next = cur.next
        cur.next = prev
        prev = cur
        cur = next
    return prev
// Recursive reversal
def reverseListRecursive(self, head):
    if (head == None  or  head.next == None) return head
    ListNode newHead = reverseListRecursive(head.next)
    head.next.next = head
    head.next = None
    return newHead
```

### Reverse Between Positions

```python
// Reverse nodes from position left to right
def reverseBetween(self, head, left, right):
    ListNode dummy = ListNode(0)
    dummy.next = head
    ListNode prev = dummy
    // Move to left position
    for (i = 1 i < left i += 1) :
    prev = prev.next
// Reverse
ListNode cur = prev.next
for (i = 0 i < right - left i += 1) :
ListNode next = cur.next
cur.next = next.next
next.next = prev.next
prev.next = next
return dummy.next
```

### Reverse in Groups

```python
// Reverse nodes in k-group
def reverseKGroup(self, head, k):
    ListNode cur = head
    count = 0
    while cur != None  and  count < k:
        cur = cur.next
        count += 1
    if count == k:
        cur = reverseKGroup(cur, k)
        while count -= 1 > 0:
            ListNode next = head.next
            head.next = cur
            cur = head
            head = next
        head = cur
    return head
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
// Merge two sorted lists
def mergeTwoLists(self, list1, list2):
    ListNode dummy = ListNode(0)
    ListNode cur = dummy
    while list1 != None  and  list2 != None:
        if list1.val <= list2.val:
            cur.next = list1
            list1 = list1.next
             else :
            cur.next = list2
            list2 = list2.next
        cur = cur.next
    (list1 if     cur.next = (list1 != None)  else list2)
    return dummy.next
```

### Merge K Sorted Lists

```python
// Merge k sorted lists using divide and conquer
def mergeKLists(self, lists):
    if (not lists) return None
    return mergeKListsHelper(lists, 0, len(lists) - 1)
def mergeKListsHelper(self, lists, left, right):
    if (left == right) return lists[left]
    mid = left + (right - left) / 2
    ListNode leftList = mergeKListsHelper(lists, left, mid)
    ListNode rightList = mergeKListsHelper(lists, mid + 1, right)
    return mergeTwoLists(leftList, rightList)
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 21 | Merge Two Sorted Lists | [Link](https://leetcode.com/problems/merge-two-sorted-lists/) | - |
| 23 | Merge k Sorted Lists | [Link](https://leetcode.com/problems/merge-k-sorted-lists/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/02/15/hard-23-merge-k-sorted-lists/) |
| 2 | Add Two Numbers | [Link](https://leetcode.com/problems/add-two-numbers/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-11-18-medium-2-add-two-numbers/) |

## Cycle Detection

### Detect Cycle (Floyd's Algorithm)

```python
// Detect cycle using Floyd's cycle detection
def hasCycle(self, head):
    if (head == None  or  head.next == None) return False
    ListNode slow = head
    ListNode fast = head
    while fast != None  and  fast.next != None:
        slow = slow.next
        fast = fast.next.next
        if (slow == fast) return True
    return False
// Find cycle start node
def detectCycle(self, head):
    ListNode slow = head
    ListNode fast = head
    // Find meeting point
    while fast != None  and  fast.next != None:
        slow = slow.next
        fast = fast.next.next
        if (slow == fast) break
    if (fast == None  or  fast.next == None) return None
    // Find cycle start
    slow = head
    while slow != fast:
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
// Insert into sorted circular linked list
def insert(self, head, insertVal):
    if head == None:
        ListNode newNode = ListNode(insertVal)
        newNode.next = newNode
        return newNode
    ListNode prev = head
    ListNode cur = head.next
    while cur != head:
        // Normal insertion point
        if prev.val <= insertVal  and  insertVal <= cur.val:
            break
        // At the boundary (largest to smallest)
        if prev.val > cur.val  and  (insertVal >= prev.val  or  insertVal <= cur.val):
            break
        prev = cur
        cur = cur.next
    prev.next = ListNode(insertVal)
    prev.next.next = cur
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

