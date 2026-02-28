---
layout: post
title: "Algorithm Templates: Queue"
date: 2025-11-24 00:00:00 -0700
categories: leetcode templates queue
permalink: /posts/2025-11-24-leetcode-templates-queue/
tags: [leetcode, templates, queue, data-structures]
---

{% raw %}
Minimal, copy-paste C++ for BFS queue, monotonic queue, priority queue, circular queue, and deque. See also [Graph](/posts/2025-10-29-leetcode-templates-graph/) and [Data Structures](/posts/2025-10-29-leetcode-templates-data-structures/) (monotonic queue).

## Contents

- [Basic Queue Operations](#basic-queue-operations)
- [BFS with Queue](#bfs-with-queue)
- [Monotonic Queue](#monotonic-queue)
- [Priority Queue](#priority-queue)
- [Circular Queue](#circular-queue)
- [Double-ended Queue (Deque)](#double-ended-queue-deque)

## Basic Queue Operations

```python
#include <queue>
# Standard queue operations
deque[int> q
q.push(1)        # Enqueue
q[0]        # Peek front
q[-1]         # Peek back
q.pop()          # Dequeue
not q        # Check if empty
len(q)         # Get size

```

### Implement Queue using Stacks

```python
class MyQueue:
list[int> input, output
def push(self, x):
    input.push(x)
def pop(self):
    peek()
    val = output.top()
    output.pop()
    return val
def peek(self):
    if not output:
        while not not input:
            output.push(input.top())
            input.pop()
    return output.top()
def empty(self):
    return not input  and  not output

```

| ID | Title | Link | Solution |
|---|---|---|---|
| 232 | Implement Queue using Stacks | [Link](https://leetcode.com/problems/implement-queue-using-stacks/) | - |

## BFS with Queue

Queue is essential for Breadth-First Search (level-order traversal).

```python
# BFS on graph
def bfs(self, graph, start):
    deque[int> q
    list[bool> visited(len(graph), False)
    q.push(start)
    visited[start] = True
    while not not q:
        node = q[0]
        q.pop()
        # Process node
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                q.push(neighbor)
# Level-order traversal (BFS on tree)
def levelOrder(self, root):
    list[list[int>> result
    if (not root) return result
    deque[TreeNode> q
    q.push(root)
    while not not q:
        size = len(q)
        list[int> level
        for (i = 0 i < size i += 1) :
        TreeNode node = q[0]
        q.pop()
        level.append(node.val)
        if node.left) q.push(node.left:
        if node.right) q.push(node.right:
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
# Monotonic decreasing queue (for sliding window maximum)
class MonotonicQueue:
deque<int> dq
def push(self, val):
    # Remove elements smaller than val
    while not not dq  and  dq[-1] < val:
        dq.pop()
    dq.append(val)
def pop(self, val):
    if not not dq  and  dq[0] == val:
        dq.pop_front()
def max(self):
    return dq[0]
# Sliding Window Maximum
def maxSlidingWindow(self, nums, k):
    MonotonicQueue mq
    list[int> result
    for (i = 0 i < len(nums) i += 1) :
    if i < k - 1:
        mq.push(nums[i])
         else :
        mq.push(nums[i])
        result.append(mq.max())
        mq.pop(nums[i - k + 1])
return result

```

| ID | Title | Link | Solution |
|---|---|---|---|
| 239 | Sliding Window Maximum | [Link](https://leetcode.com/problems/sliding-window-maximum/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-11-04-hard-239-sliding-window-maximum/) |
| 1438 | Longest Continuous Subarray With Absolute Diff <= Limit | [Link](https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/) | - |

## Priority Queue

Priority queue (heap) for maintaining order.

```python
#include <queue>
#include <vector>
# Max heap (default)
heapq[int> maxHeap
# Min heap
heapq[int, list[int>, greater<int>> minHeap
# Custom comparator using struct
struct Compare :
def operator(self, )(pair<int, a, pair<int, b):
    return a.second > b.second # Min heap by second element
heapq[pair<int, int>, list[pair<int, int>>, Compare> pq
# Custom comparator using lambda operator
cmp = [](pair<int, int> a, pair<int, int> b) :
return a.second > b.second # Min heap by second element
heapq[pair<int, int>, list[pair<int, int>>, decltype(cmp)> pq(cmp)
# Lambda example: Min heap by distance (for Dijkstra's algorithm)
distCmp = [](pair<int, int> a, pair<int, int> b) :
return a.first > b.first # :distance, node - min heap by distance
heapq[pair<int, int>, list[pair<int, int>>, decltype(distCmp)> pq(distCmp)

```

### K-way Merge

```python
# Merge k sorted lists using priority queue
def mergeKLists(self, lists):
    cmp = [](ListNode a, ListNode b) : return a.val > b.val
heapq[ListNode, list[ListNode>, decltype(cmp)> pq(cmp)
for list in lists:
    if list) pq.push(list:
ListNode dummy = ListNode(0)
ListNode cur = dummy
while not not pq:
    ListNode node = pq.top()
    pq.pop()
    cur.next = node
    cur = cur.next
    if node.next) pq.push(node.next:
return dummy.next

```

### Top K Elements

```python
# Find top k frequent elements
def topKFrequent(self, nums, k):
    dict[int, int> freq
    for (num : nums) freq[num]++
    heapq[pair<int, int>, list[pair<int, int>>, greater<pair<int, int>>> pq
    for ([num, count] : freq) :
    pq.push(:count, num)
    if len(pq) > k) pq.pop(:
list[int> result
while not not pq:
    result.append(pq.top().second)
    pq.pop()
return result

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
list[int> data
head, tail, size, capacity
MyCircularQueue(k) : data(k), head(0), tail(0), size(0), capacity(k) :
def enQueue(self, value):
    if (isFull()) return False
    data[tail] = value
    tail = (tail + 1) % capacity
    size += 1
    return True
def deQueue(self):
    if (isEmpty()) return False
    head = (head + 1) % capacity
    size -= 1
    return True
def Front(self):
    (-1 if         return isEmpty()  else data[head])
def Rear(self):
    (-1 if         return isEmpty()  else data[(tail - 1 + capacity) % capacity])
def isEmpty(self):
    return size == 0
def isFull(self):
    return size == capacity

```

| ID | Title | Link | Solution |
|---|---|---|---|
| 622 | Design Circular Queue | [Link](https://leetcode.com/problems/design-circular-queue/) | - |

## Double-ended Queue (Deque)

```python
#include <deque>
deque<int> dq
dq.push_front(1)  # Add to front
dq.append(2)   # Add to back
dq.pop_front()     # Remove from front
dq.pop()      # Remove from back
dq[0]         # Access front
dq[-1]          # Access back


```

### Sliding Window with Deque

```python
# Sliding window maximum using deque
def maxSlidingWindow(self, nums, k):
    deque<int> dq
    list[int> result
    for (i = 0 i < len(nums) i += 1) :
    # Remove indices outside window
    while not not dq  and  dq[0] <= i - k:
        dq.pop_front()
    # Remove indices with smaller values
    while not not dq  and  nums[dq[-1]] <= nums[i]:
        dq.pop()
    dq.append(i)
    if i >= k - 1:
        result.append(nums[dq[0]])
return result

```

### Two Deques Pattern (Middle Element Access)

Use two deques to efficiently access middle elements in a queue.

```python
# Front Middle Back Queue: Two deques with rebalancing
class FrontMiddleBackQueue:
deque<int> front_cache, back_cache
def rebalance(self):
    # Maintain: len(front_cache) <= len(back_cache) <= len(front_cache) + 1
    while len(front_cache) > len(back_cache):
        back_cache.push_front(front_cache[-1])
        front_cache.pop()
    while len(back_cache) > len(front_cache) + 1:
        front_cache.append(back_cache[0])
        back_cache.pop_front()
def pushMiddle(self, val):
    front_cache.append(val)
    rebalance()
def popMiddle(self):
    if(not front_cache  and  not back_cache) return -1
    if len(front_cache) == len(back_cache):
        val = front_cache[-1]
        front_cache.pop()
        return val
         else :
        val = back_cache[0]
        back_cache.pop_front()
        return val

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

