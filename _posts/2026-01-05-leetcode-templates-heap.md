---
layout: post
title: "Algorithm Templates: Heap"
date: 2026-01-05 00:00:00 -0700
categories: leetcode templates heap priority-queue
permalink: /posts/2026-01-05-leetcode-templates-heap/
tags: [leetcode, templates, heap, priority-queue, data-structures]
---

{% raw %}
Minimal, copy-paste C++ for min/max heap, K-way merge, top K, and two heaps. See also [Data Structures](/posts/2025-10-29-leetcode-templates-data-structures/) for heap patterns.

## Contents

- [Heap Overview](#heap-overview)
- [Min Heap](#min-heap)
- [Max Heap](#max-heap)
- [Custom Comparators](#custom-comparators)
- [Common Patterns](#common-patterns)
- [K-way Merge](#k-way-merge)
- [Top K Elements](#top-k-elements)
- [Two Heaps](#two-heaps)
- [Dijkstra's Algorithm](#dijkstras-algorithm)

## Heap Overview

A **heap** (priority queue) is a complete binary tree that satisfies the heap property:
- **Min Heap**: Parent node is always less than or equal to its children
- **Max Heap**: Parent node is always greater than or equal to its children

**Key Operations:**
- `push(x)`: Insert element - O(log n)
- `pop()`: Remove top element - O(log n)
- `top()`: Access top element - O(1)
- `empty()`: Check if empty - O(1)
- `size()`: Get size - O(1)

**Use Cases:**
- Finding K largest/smallest elements
- Merging K sorted sequences
- Maintaining running median
- Shortest path algorithms (Dijkstra's)
- Scheduling problems

## Min Heap

Min heap keeps the smallest element at the top.

```python
import heapq

# Min heap in Python (heapq is min-heap by default)
min_heap = []
heapq.heappush(min_heap, 5)
heapq.heappush(min_heap, 2)
heapq.heappush(min_heap, 8)
heapq.heappush(min_heap, 1)

smallest = min_heap[0]         # 1
removed = heapq.heappop(min_heap)  # removes 1
next_smallest = min_heap[0]    # 2

```

### Example: Find K Smallest Elements

```python
import heapq

class Solution:
    def findKSmallest(self, nums, k):
        minHeap = []

        for num in nums:
            heapq.heappush(minHeap, num)

        result = []

        for i in range(k):
            if minHeap:
                result.append(heapq.heappop(minHeap))

        return result
```

## Max Heap

Max heap keeps the largest element at the top (default in C++).

```python
import heapq

# Max heap via negation
max_heap = []
heapq.heappush(max_heap, -5)
heapq.heappush(max_heap, -2)
heapq.heappush(max_heap, -8)
heapq.heappush(max_heap, -1)

largest = -max_heap[0]         # 8
removed = -heapq.heappop(max_heap)  # removes 8
next_largest = -max_heap[0]    # 5

```

### Example: Find K Largest Elements

```python
import heapq

class Solution:
    def findKLargest(self, nums, k):
        maxHeap = []

        for num in nums:
            heapq.heappush(maxHeap, -num)  # simulate max heap

        result = []

        for i in range(k):
            if maxHeap:
                result.append(-heapq.heappop(maxHeap))

        return result

```

## Custom Comparators

### Using Struct

```python
import heapq

# Custom comparator for pairs: min heap by second element
# (Python uses tuple ordering instead of struct comparator)
pq = []

# Example: :value, frequency - keep element with smallest frequency on top
heapq.heappush(pq, (5, 1))
heapq.heappush(pq, (3, 2))
heapq.heappush(pq, (7, 3))

print(pq[0])  # (3, 2)

```

```python
import heapq

# Custom struct with comparator: min heap by cost
class Node:
    def __init__(self, cost, node_id):
        self.cost = cost
        self.node_id = node_id

    def __lt__(self, other):
        return self.cost < other.cost  # Min heap by cost

pq = []

# Example usage
heapq.heappush(pq, Node(10, 1))  # cost 10, id 1
heapq.heappush(pq, Node(5, 2))   # cost 5, id 2
heapq.heappush(pq, Node(15, 3))  # cost 15, id 3

print(pq[0].cost)  # 5
```

### Custom Object Comparator

```python
import heapq

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist2(self):
        return self.x * self.x + self.y * self.y

    def __lt__(self, other):
        return self.dist2() < other.dist2()  # min heap by squared distance

pq = []
heapq.heappush(pq, Point(3, 4))  # dist2 = 25
heapq.heappush(pq, Point(1, 1))  # dist2 = 2
closest = heapq.heappop(pq)

```

## Common Patterns

### Pattern 1: Maintain K Elements

Keep only K elements in heap, remove smallest/largest when size exceeds K.

```python
# Keep K largest elements
import heapq

min_heap = []  # min heap to keep K largest
for num in nums:
    heapq.heappush(min_heap, num)
    if len(min_heap) > k:
        heapq.heappop(min_heap)  # remove smallest
# now min_heap contains K largest elements

```

### Pattern 2: Frequency-Based

Use heap with frequency counts.

```python
# Top K frequent elements
import heapq
from collections import Counter

freq = Counter(nums)
min_heap = []  # (frequency, element)
for num, count in freq.items():
    heapq.heappush(min_heap, (count, num))
    if len(min_heap) > k:
        heapq.heappop(min_heap)

```

## K-way Merge

Merge K sorted lists/arrays using a min heap.

```python
# Merge K sorted lists
import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_k_lists(lists):
    heap = []  # (value, list_index, node)

    for i, node in enumerate(lists):
        if node is not None:
            heapq.heappush(heap, (node.val, i, node))

    dummy = ListNode()
    cur = dummy
    while heap:
        _, i, node = heapq.heappop(heap)
        cur.next = node
        cur = cur.next
        if node.next is not None:
            heapq.heappush(heap, (node.next.val, i, node.next))

    return dummy.next

```

### K-way Merge for Arrays

```python
# Merge K sorted arrays
import heapq

def merge_k_sorted_arrays(arrays):
    heap = []  # (value, array_index, position)
    for i, arr in enumerate(arrays):
        if arr:
            heapq.heappush(heap, (arr[0], i, 0))

    result = []
    while heap:
        val, arr_idx, pos = heapq.heappop(heap)
        result.append(val)
        nxt = pos + 1
        if nxt < len(arrays[arr_idx]):
            heapq.heappush(heap, (arrays[arr_idx][nxt], arr_idx, nxt))
    return result

```

## Top K Elements

### Top K Frequent Elements

```python
def topKFrequent(self, nums, k):
    import heapq
    from collections import Counter

    freq = Counter(nums)
    min_heap = []  # (count, num)

    for num, count in freq.items():
        heapq.heappush(min_heap, (count, num))
        if len(min_heap) > k:
            heapq.heappop(min_heap)

    return [num for count, num in min_heap]

```

### K Closest Points to Origin

```python
def kClosest(self, points, k):
    import heapq

    max_heap = []  # (-dist2, x, y)
    for x, y in points:
        dist2 = x * x + y * y
        heapq.heappush(max_heap, (-dist2, x, y))
        if len(max_heap) > k:
            heapq.heappop(max_heap)

    return [[x, y] for _, x, y in max_heap]

```

### Kth Largest Element in an Array (LC 215)

**Solution 1: Min Heap (O(n log k))**

Keep a min heap of size k. The top element will be the kth largest.

```python
class Solution:
    def findKthLargest(self, nums, k):
        import heapq

        min_heap = []
        for num in nums:
            heapq.heappush(min_heap, num)
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        return min_heap[0]

```

**Solution 2: QuickSelect (O(n) average, O(n²) worst case)**

Use partition-based selection algorithm.

```python
class Solution:
    def findKthLargest(self, nums, k):
        target = len(nums) - k
        left, right = 0, len(nums) - 1

        while True:
            pivot_index = self.partition(nums, left, right)
            if pivot_index == target:
                return nums[pivot_index]
            if pivot_index < target:
                left = pivot_index + 1
            else:
                right = pivot_index - 1

    def partition(self, nums, left, right):
        pivot = nums[right]
        i = left
        for j in range(left, right):
            if nums[j] <= pivot:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        nums[i], nums[right] = nums[right], nums[i]
        return i

```

**Comparison:**
- **Heap**: O(n log k) time, O(k) space - Simple and efficient for small k
- **QuickSelect**: O(n) average time, O(n²) worst case, O(1) space - Better for large k

## Two Heaps

Maintain two heaps to find median or balance elements.

### Find Median from Data Stream

```python
class MedianFinder:
    def __init__(self):
        import heapq
        self._heapq = heapq
        self.max_heap = []  # lower half as negative values
        self.min_heap = []  # upper half

    def addNum(self, num):
        self._heapq.heappush(self.max_heap, -num)
        self._heapq.heappush(self.min_heap, -self._heapq.heappop(self.max_heap))
        if len(self.max_heap) < len(self.min_heap):
            self._heapq.heappush(self.max_heap, -self._heapq.heappop(self.min_heap))

    def findMedian(self):
        if len(self.max_heap) > len(self.min_heap):
            return float(-self.max_heap[0])
        return (-self.max_heap[0] + self.min_heap[0]) / 2.0

```

### Sliding Window Median

```python
def medianSlidingWindow(self, nums, k):
    # Reference implementation using sorted window (O(n * k))
    import bisect

    window = sorted(nums[:k])
    medians = []

    for i in range(k, len(nums) + 1):
        if k % 2 == 1:
            medians.append(float(window[k // 2]))
        else:
            medians.append((window[k // 2 - 1] + window[k // 2]) / 2.0)

        if i == len(nums):
            break

        out_num = nums[i - k]
        in_num = nums[i]
        window.pop(bisect.bisect_left(window, out_num))
        bisect.insort(window, in_num)

    return medians

```

## Dijkstra's Algorithm

Use min heap for shortest path finding.

```python
# Shortest path from source to all nodes
import heapq

def dijkstra(graph, start):
    # graph[u] = [(v, weight), ...]
    n = len(graph)
    dist = [float("inf")] * n
    dist[start] = 0

    pq = [(0, start)]  # (distance, node)
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, weight in graph[u]:
            new_dist = d + weight
            if new_dist < dist[v]:
                dist[v] = new_dist
                heapq.heappush(pq, (new_dist, v))
    return dist

```

## Easy Problems

| ID | Title | Link | Solution |
|---|---|---|---|
| 703 | Kth Largest Element in a Stream | [Link](https://leetcode.com/problems/kth-largest-element-in-a-stream/) | - |
| 1046 | Last Stone Weight | [Link](https://leetcode.com/problems/last-stone-weight/) | - |
| 1167 | Minimum Cost to Connect Sticks | [Link](https://leetcode.com/problems/minimum-cost-to-connect-sticks/) | - |

## Medium Problems

| ID | Title | Link | Solution |
|---|---|---|---|
| 23 | Merge k Sorted Lists | [Link](https://leetcode.com/problems/merge-k-sorted-lists/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/02/15/hard-23-merge-k-sorted-lists/) |
| 215 | Kth Largest Element in an Array | [Link](https://leetcode.com/problems/kth-largest-element-in-an-array/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/01/05/medium-215-kth-largest-element-in-an-array/) |
| 253 | Meeting Rooms II | [Link](https://leetcode.com/problems/meeting-rooms-ii/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-12-11-medium-253-meeting-rooms-ii/) |
| 295 | Find Median from Data Stream | [Link](https://leetcode.com/problems/find-median-from-data-stream/) | - |
| 347 | Top K Frequent Elements | [Link](https://leetcode.com/problems/top-k-frequent-elements/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-10-21-medium-347-top-k-frequent-elements/) |
| 378 | Kth Smallest Element in a Sorted Matrix | [Link](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/) | - |
| 692 | Top K Frequent Words | [Link](https://leetcode.com/problems/top-k-frequent-words/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/01/08/medium-692-top-k-frequent-words/) |
| 621 | Task Scheduler | [Link](https://leetcode.com/problems/task-scheduler/) | - |
| 767 | Reorganize String | [Link](https://leetcode.com/problems/reorganize-string/) | - |
| 973 | K Closest Points to Origin | [Link](https://leetcode.com/problems/k-closest-points-to-origin/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-10-21-medium-973-k-closest-points-to-origin/) |
| 1976 | Number of Ways to Arrive at Destination | [Link](https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/12/28/medium-1976-number-of-ways-to-arrive-at-destination/) |

## Hard Problems

| ID | Title | Link | Solution |
|---|---|---|---|
| 239 | Sliding Window Maximum | [Link](https://leetcode.com/problems/sliding-window-maximum/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-11-04-hard-239-sliding-window-maximum/) |
| 480 | Sliding Window Median | [Link](https://leetcode.com/problems/sliding-window-median/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-11-04-hard-480-sliding-window-median/) |
| 743 | Network Delay Time | [Link](https://leetcode.com/problems/network-delay-time/) | - |
| 787 | Cheapest Flights Within K Stops | [Link](https://leetcode.com/problems/cheapest-flights-within-k-stops/) | - |
| 871 | Minimum Number of Refueling Stops | [Link](https://leetcode.com/problems/minimum-number-of-refueling-stops/) | - |

## Common Heap Patterns

### Pattern 1: K Largest/Smallest
- Use min heap to keep K largest (remove smallest when size > K)
- Use max heap to keep K smallest (remove largest when size > K)

### Pattern 2: Frequency-Based
- Count frequencies, use heap to find top K by frequency

### Pattern 3: K-way Merge
- Push first element of each sequence into min heap
- Pop smallest, push next element from same sequence

### Pattern 4: Two Heaps
- Maintain two balanced heaps for median finding
- One heap for lower half, one for upper half

### Pattern 5: Shortest Path
- Use min heap in Dijkstra's algorithm
- Store {distance, node} pairs

## Key Insights

1. **Min Heap for K Largest**: Keep K largest by removing smallest
2. **Max Heap for K Smallest**: Keep K smallest by removing largest
3. **Custom Comparators**: Use lambda or struct for complex ordering
4. **Two Heaps**: Balance two heaps for median problems
5. **Efficiency**: Heap operations are O(log n), making it efficient for dynamic problems

## Time Complexity

| Operation | Time Complexity |
|-----------|----------------|
| `push()` | O(log n) |
| `pop()` | O(log n) |
| `top()` | O(1) |
| `empty()` | O(1) |
| `size()` | O(1) |

## Space Complexity

- **Heap Storage**: O(n) where n is number of elements
- **Auxiliary Space**: O(1) for operations (excluding storage)

## When to Use Heap

1. **K Largest/Smallest**: Finding top K elements
2. **K-way Merge**: Merging K sorted sequences
3. **Scheduling**: Meeting rooms, task scheduling
4. **Shortest Path**: Dijkstra's algorithm
5. **Median Finding**: Two heaps pattern
6. **Frequency Problems**: Top K frequent elements

## Common Mistakes

1. **Wrong Comparator**: Using `>` instead of `<` (or vice versa) for min/max heap
2. **Not Handling Empty**: Accessing `top()` without checking `empty()`
3. **Wrong Heap Type**: Using max heap when min heap is needed
4. **Not Maintaining Size**: Forgetting to pop when size exceeds K
5. **Custom Comparator Logic**: Reversing the comparison logic incorrectly

## Related Data Structures

- **Set/Multiset**: For maintaining sorted order with duplicates
- **Map**: For frequency counting before heap operations
- **Deque**: For sliding window problems (alternative to heap)

## More templates

- **Data structures (heap, monotonic queue):** [Data Structures & Core Algorithms](/posts/2025-10-29-leetcode-templates-data-structures/)
- **Graph (Dijkstra):** [Graph](/posts/2025-10-29-leetcode-templates-graph/)
- **Master index:** [Categories & Templates](/posts/2025-10-29-leetcode-categories-and-templates/)

{% endraw %}

