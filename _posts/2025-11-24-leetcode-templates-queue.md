---
layout: post
title: "Algorithm Templates: Queue"
date: 2025-11-24 00:00:00 -0700
categories: leetcode templates queue
permalink: /posts/2025-11-24-leetcode-templates-queue/
tags: [leetcode, templates, queue, data-structures]
---

{% raw %}
Minimal, copy-paste Python for BFS queue, monotonic queue, priority queue, circular queue, and deque. See also [Graph](/posts/2025-10-29-leetcode-templates-graph/) and [Data Structures](/posts/2025-10-29-leetcode-templates-data-structures/) (monotonic queue).

## Contents

- [Basic Queue Operations](#basic-queue-operations)
- [BFS with Queue](#bfs-with-queue)
- [Monotonic Queue](#monotonic-queue)
- [Priority Queue](#priority-queue)
- [Circular Queue](#circular-queue)
- [Double-ended Queue (Deque)](#double-ended-queue-deque)

## Basic Queue Operations

```python
from collections import deque

# Standard deque as FIFO queue
q: deque[int] = deque()
q.append(1)  # enqueue (back)
q[0]  # peek front
q[-1]  # peek back
q.popleft()  # dequeue from front
not q  # empty check
len(q)

```

### Implement Queue using Stacks

```python
class MyQueue:
    def __init__(self) -> None:
        self._in: list[int] = []
        self._out: list[int] = []

    def push(self, x: int) -> None:
        self._in.append(x)

    def pop(self) -> int:
        self.peek()
        return self._out.pop()

    def peek(self) -> int:
        if not self._out:
            while self._in:
                self._out.append(self._in.pop())
        return self._out[-1]

    def empty(self) -> bool:
        return not self._in and not self._out

```

| ID | Title | Link | Solution |
|---|---|---|---|
| 232 | Implement Queue using Stacks | [Link](https://leetcode.com/problems/implement-queue-using-stacks/) | - |

## BFS with Queue

Queue is essential for Breadth-First Search (level-order traversal).

```python
from collections import deque


class TreeNode:
    def __init__(self, val: int = 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def bfs_graph(graph: list[list[int]], start: int) -> None:
    q: deque[int] = deque([start])
    visited = [False] * len(graph)
    visited[start] = True
    while q:
        node = q.popleft()
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                q.append(neighbor)


def level_order(root: TreeNode | None) -> list[list[int]]:
    if not root:
        return []
    result: list[list[int]] = []
    q: deque[TreeNode] = deque([root])
    while q:
        level: list[int] = []
        for _ in range(len(q)):
            node = q.popleft()
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        result.append(level)
    return result

```

| ID | Title | Link | Solution |
|---|---|---|---|
| 102 | Binary Tree Level Order Traversal | [Link](https://leetcode.com/problems/binary-tree-level-order-traversal/) | - |
| 107 | Binary Tree Level Order Traversal II | [Link](https://leetcode.com/problems/binary-tree-level-order-traversal-ii/) | - |

## Monotonic Queue

Maintain queue with monotonic property (increasing or decreasing).

```python
from collections import deque


class MonotonicQueue:
    """Decreasing deque of values (max at left)."""

    def __init__(self) -> None:
        self.dq: deque[int] = deque()

    def push(self, val: int) -> None:
        while self.dq and self.dq[-1] < val:
            self.dq.pop()
        self.dq.append(val)

    def pop(self, val: int) -> None:
        if self.dq and self.dq[0] == val:
            self.dq.popleft()

    def max_val(self) -> int:
        return self.dq[0]


def max_sliding_window(nums: list[int], k: int) -> list[int]:
    mq = MonotonicQueue()
    out: list[int] = []
    for i, x in enumerate(nums):
        mq.push(x)
        if i >= k - 1:
            out.append(mq.max_val())
            mq.pop(nums[i - k + 1])
    return out

```

| ID | Title | Link | Solution |
|---|---|---|---|
| 239 | Sliding Window Maximum | [Link](https://leetcode.com/problems/sliding-window-maximum/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-11-04-hard-239-sliding-window-maximum/) |
| 1438 | Longest Continuous Subarray With Absolute Diff <= Limit | [Link](https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/) | - |

## Priority Queue

Priority queue (heap) for maintaining order.

```python
import heapq

# Min-heap (default): heapq is a min-heap on the first element of tuples
pq: list[tuple[int, int]] = []
heapq.heappush(pq, (dist, node_id))

# Max-heap trick: store negated keys
heapq.heappush(pq, (-priority, item))

# Custom order: push tuples; Python compares lexicographically
heapq.heappush(pq, (secondary_key, primary_key, payload))

```

### K-way Merge

```python
import heapq


class ListNode:
    def __init__(self, val: int = 0, next=None):
        self.val = val
        self.next = next


def merge_k_lists(lists: list[ListNode | None]) -> ListNode | None:
    heap: list[tuple[int, int, ListNode]] = []
    for i, h in enumerate(lists):
        if h:
            heapq.heappush(heap, (h.val, i, h))
    dummy = ListNode(0)
    cur = dummy
    while heap:
        _, i, node = heapq.heappop(heap)
        cur.next = node
        cur = cur.next
        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))
    return dummy.next

```

### Top K Elements

```python
import heapq
from collections import Counter


def top_k_frequent(nums: list[int], k: int) -> list[int]:
    freq = Counter(nums)
    heap: list[tuple[int, int]] = []
    for num, c in freq.items():
        heapq.heappush(heap, (c, num))
        if len(heap) > k:
            heapq.heappop(heap)
    return [num for _, num in heap]

```

| ID | Title | Link | Solution |
|---|---|---|---|
| 23 | Merge k Sorted Lists | [Link](https://leetcode.com/problems/merge-k-sorted-lists/) | - |
| 347 | Top K Frequent Elements | [Link](https://leetcode.com/problems/top-k-frequent-elements/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-10-21-medium-347-top-k-frequent-elements/) |
| 295 | Find Median from Data Stream | [Link](https://leetcode.com/problems/find-median-from-data-stream/) | - |
| 215 | Kth Largest Element in an Array | [Link](https://leetcode.com/problems/kth-largest-element-in-an-array/) | - |
| 973 | K Closest Points to Origin | [Link](https://leetcode.com/problems/k-closest-points-to-origin/) | - |
| 253 | Meeting Rooms II | [Link](https://leetcode.com/problems/meeting-rooms-ii/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-12-11-medium-253-meeting-rooms-ii/) |
| 378 | Kth Smallest Element in a Sorted Matrix | [Link](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/) | - |
| 703 | Kth Largest Element in a Stream | [Link](https://leetcode.com/problems/kth-largest-element-in-a-stream/) | - |
| 767 | Reorganize String | [Link](https://leetcode.com/problems/reorganize-string/) | - |
| 1046 | Last Stone Weight | [Link](https://leetcode.com/problems/last-stone-weight/) | - |
| 1167 | Minimum Cost to Connect Sticks | [Link](https://leetcode.com/problems/minimum-cost-to-connect-sticks/) | - |
| 621 | Task Scheduler | [Link](https://leetcode.com/problems/task-scheduler/) | - |
| 743 | Network Delay Time | [Link](https://leetcode.com/problems/network-delay-time/) | - |
| 787 | Cheapest Flights Within K Stops | [Link](https://leetcode.com/problems/cheapest-flights-within-k-stops/) | - |

## Circular Queue

```python
class MyCircularQueue:
    def __init__(self, k: int) -> None:
        self.data = [0] * k
        self.head = 0
        self.tail = 0
        self.size = 0
        self.capacity = k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.data[self.tail] = value
        self.tail = (self.tail + 1) % self.capacity
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return True

    def Front(self) -> int:
        return -1 if self.isEmpty() else self.data[self.head]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.data[(self.tail - 1 + self.capacity) % self.capacity]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity

```

| ID | Title | Link | Solution |
|---|---|---|---|
| 622 | Design Circular Queue | [Link](https://leetcode.com/problems/design-circular-queue/) | - |

## Double-ended Queue (Deque)

```python
from collections import deque

dq: deque[int] = deque()
dq.appendleft(1)  # add front
dq.append(2)  # add back
dq.popleft()  # remove front
dq.pop()  # remove back
dq[0]
dq[-1]

```

### Sliding Window with Deque

```python
from collections import deque


def max_sliding_window_deque(nums: list[int], k: int) -> list[int]:
    dq: deque[int] = deque()
    out: list[int] = []
    for i, x in enumerate(nums):
        while dq and dq[0] <= i - k:
            dq.popleft()
        while dq and nums[dq[-1]] <= x:
            dq.pop()
        dq.append(i)
        if i >= k - 1:
            out.append(nums[dq[0]])
    return out

```

### Two Deques Pattern (Middle Element Access)

Use two deques to efficiently access middle elements in a queue.

```python
from collections import deque


class FrontMiddleBackQueue:
    def __init__(self) -> None:
        self.front: deque[int] = deque()
        self.back: deque[int] = deque()

    def _rebalance(self) -> None:
        while len(self.front) > len(self.back):
            self.back.appendleft(self.front.pop())
        while len(self.back) > len(self.front) + 1:
            self.front.append(self.back.popleft())

    def pushMiddle(self, val: int) -> None:
        self.front.append(val)
        self._rebalance()

    def popMiddle(self) -> int:
        if not self.front and not self.back:
            return -1
        if len(self.front) == len(self.back):
            return self.front.pop()
        return self.back.popleft()

```

**Key points:**
- Split queue into two halves: `front_cache` and `back_cache`
- Maintain balance: `front_cache.size() <= back_cache.size() <= front_cache.size() + 1`
- Middle element is `front_cache.back()` (if sizes equal) or `back_cache.front()` (if back_cache larger)
- Rebalance after each modification

| ID | Title | Link | Solution |
|---|---|---|---|
| 239 | Sliding Window Maximum | [Link](https://leetcode.com/problems/sliding-window-maximum/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-11-04-hard-239-sliding-window-maximum/) |
| 1670 | Design Front Middle Back Queue | [Link](https://leetcode.com/problems/design-front-middle-back-queue/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/01/13/medium-1670-design-front-middle-back-queue/) |

## More templates

- **Data structures (monotonic queue):** [Data Structures & Core Algorithms](/posts/2025-10-29-leetcode-templates-data-structures/)
- **BFS, Graph:** [BFS](/posts/2025-11-24-leetcode-templates-bfs/), [Graph](/posts/2025-10-29-leetcode-templates-graph/)
- **Master index:** [Categories & Templates](/posts/2025-10-29-leetcode-categories-and-templates/)
{% endraw %}

