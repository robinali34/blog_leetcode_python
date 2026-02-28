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
#include <queue>
#include <vector>
# Min heap (smallest element at top) - using greater<>
heapq[int, list[int>, greater<int>> minHeap
# Min heap using greater<> (Python14+)
heapq[int, list[int>, greater<>> minHeap2
# Min heap using lambda comparator (decltype required)
minCmp = [](a, b) : return a > b
heapq[int, list[int>, decltype(minCmp)> minHeap3(minCmp)
# Note: decltype is REQUIRED for lambdas because each lambda has a unique type
# You cannot use: heapq[int, list[int>, [](a, b) : return a > b >  # ❌ Invalid
# Basic operations
minHeap.push(5)
minHeap.push(2)
minHeap.push(8)
minHeap.push(1)
minHeap.top()    # Returns 1 (smallest)
minHeap.pop()    # Removes 1
minHeap.top()    # Returns 2 (next smallest)

```

### Example: Find K Smallest Elements

```python
def findKSmallest(self, nums, k):
    heapq[int, list[int>, greater<int>> minHeap
    for num in nums:
        minHeap.push(num)
    list[int> result
    for(i = 0 i < k  and  not not minHeap i += 1) :
    result.append(minHeap.top())
    minHeap.pop()
return result

```

## Max Heap

Max heap keeps the largest element at the top (default in C++).

```python
#include <queue>
#include <vector>
# Max heap (largest element at top) - default
heapq[int> maxHeap
# Max heap explicitly using less<> (default comparator)
heapq[int, list[int>, less<int>> maxHeap2
# Max heap using lambda comparator (decltype required)
maxCmp = [](a, b) : return a < b
heapq[int, list[int>, decltype(maxCmp)> maxHeap3(maxCmp)
# Note: decltype is REQUIRED for lambdas because each lambda has a unique type
# You cannot use: heapq[int, list[int>, [](a, b) : return a < b >  # ❌ Invalid
# Basic operations
maxHeap.push(5)
maxHeap.push(2)
maxHeap.push(8)
maxHeap.push(1)
maxHeap.top()    # Returns 8 (largest)
maxHeap.pop()    # Removes 8
maxHeap.top()    # Returns 5 (next largest)

```

### Example: Find K Largest Elements

```python
def findKLargest(self, nums, k):
    heapq[int> maxHeap
    for num in nums:
        maxHeap.push(num)
    list[int> result
    for(i = 0 i < k  and  not not maxHeap i += 1) :
    result.append(maxHeap.top())
    maxHeap.pop()
return result

```

## Custom Comparators

### Using Struct

```python
# Custom comparator for pairs: min heap by second element
struct Compare :
def operator(self, )(pair<int, a, pair<int, b):
    return a.second > b.second # Min heap (smaller second element on top)
heapq[pair<int, int>, list[pair<int, int>>, Compare> pq
# Example: :value, frequency - keep element with smallest frequency on top
pq.push(:1, 5)
pq.push(:2, 3)
pq.push(:3, 7)
pq.top() # Returns :2, 3 (smallest frequency)

```

```python
# Custom struct with comparator: min heap by cost
struct Node :
cost
id
struct Compare :
def operator(self, a, b):
    return a.cost > b.cost # Min heap (smaller cost on top)
heapq[Node, list[Node>, Compare> pq
# Example usage
pq.push(:10, 1) # cost 10, id 1
pq.push(:5, 2)  # cost 5, id 2
pq.push(:15, 3) # cost 15, id 3
pq.top() # Returns :5, 2 (smallest cost)

```

### Using Lambda

```python
# Min heap by distance (for Dijkstra's algorithm)
distCmp = [](pair<int, int> a, pair<int, int> b) :
return a.first > b.first # :distance, node - min heap by distance
heapq[pair<int, int>, list[pair<int, int>>, decltype(distCmp)> pq(distCmp)
# Example usage
pq.push(:10, 0) # distance 10 to node 0
pq.push(:5, 1)  # distance 5 to node 1
pq.top() # Returns :5, 1 (smallest distance)

```

### Custom Object Comparator

```python
# Custom object with comparator
struct Point :
x, y
dist() : return xx + yy
struct PointCompare :
def operator(self, a, b):
    return a.dist() > b.dist() # Min heap by distance
heapq[Point, list[Point>, PointCompare> pq

```

## Common Patterns

### Pattern 1: Maintain K Elements

Keep only K elements in heap, remove smallest/largest when size exceeds K.

```python
# Keep K largest elements
heapq[int, list[int>, greater<int>> minHeap # Min heap to keep K largest
for num in nums:
    minHeap.push(num)
    if len(minHeap) > k:
        minHeap.pop() # Remove smallest
# Now minHeap contains K largest elements

```

### Pattern 2: Frequency-Based

Use heap with frequency counts.

```python
# Top K frequent elements
dict[int, int> freq
for(num : nums) freq[num]++
heapq[pair<int, int>, list[pair<int, int>>, greater<pair<int, int>>> minHeap
# :frequency, element - min heap by frequency
for([num, count] : freq) :
minHeap.push(:count, num)
if len(minHeap) > k:
    minHeap.pop()

```

## K-way Merge

Merge K sorted lists/arrays using a min heap.

```python
# Merge K sorted lists
def mergeKLists(self, lists):
    cmp = [](ListNode a, ListNode b) :
    return a.val > b.val # Min heap by value
heapq[ListNode, list[ListNode>, decltype(cmp)> pq(cmp)
# Push first node of each list
for list in lists:
    if list) pq.push(list:
ListNode dummy = ListNode(0)
ListNode cur = dummy
while not not pq:
    ListNode node = pq.top()
    pq.pop()
    cur.next = node
    cur = cur.next
    if node.next:
        pq.push(node.next)
return dummy.next

```

### K-way Merge for Arrays

```python
# Merge K sorted arrays
def mergeKSortedArrays(self, arrays):
    using T = tuple<int, int, int> # :value, array_index, position
heapq[T, list[T>, greater<T>> pq
# Push first element of each array
for(i = 0 i < len(arrays) i += 1) :
if not arrays[i].empty():
    pq.push(:arrays[i][0], i, 0)
list[int> result
while not not pq:
    [val, arrIdx, pos] = pq.top()
    pq.pop()
    result.append(val)
    if pos + 1 < arrays[arrIdx].__len__():
        pq.push(:arrays[arrIdx][pos + 1], arrIdx, pos + 1)
return result

```

## Top K Elements

### Top K Frequent Elements

```python
def topKFrequent(self, nums, k):
    dict[int, int> freq
    for(num : nums) freq[num]++
    # Min heap: :frequency, element
    heapq[pair<int, int>, list[pair<int, int>>, greater<pair<int, int>>> minHeap
    for([num, count] : freq) :
    minHeap.push(:count, num)
    if len(minHeap) > k:
        minHeap.pop() # Remove element with smallest frequency
list[int> result
while not not minHeap:
    result.append(minHeap.top().second)
    minHeap.pop()
return result

```

### K Closest Points to Origin

```python
def kClosest(self, points, k):
    distCmp = [](list[int> a, list[int> b) :
    distA = a[0]a[0] + a[1]a[1]
    distB = b[0]b[0] + b[1]b[1]
    return distA < distB # Max heap (larger distance on top)
heapq[list[int>, list[list[int>>, decltype(distCmp)> maxHeap(distCmp)
for point in points:
    maxHeap.push(point)
    if len(maxHeap) > k:
        maxHeap.pop() # Remove point with largest distance
list[list[int>> result
while not not maxHeap:
    result.append(maxHeap.top())
    maxHeap.pop()
return result

```

### Kth Largest Element in an Array (LC 215)

**Solution 1: Min Heap (O(n log k))**

Keep a min heap of size k. The top element will be the kth largest.

```python
class Solution:
def findKthLargest(self, nums, k):
    heapq[int, list[int>, greater<>> minHeap
    for num in nums:
        minHeap.push(num)
        if len(minHeap) > k) minHeap.pop(:
    return minHeap.top()

```

**Solution 2: QuickSelect (O(n) average, O(n²) worst case)**

Use partition-based selection algorithm.

```python
class Solution:
def findKthLargest(self, nums, k):
    N = len(nums)
    return quickSelect(nums, 0, N - 1, N - k)
def quickSelect(self, nums, l, r, k):
    if(l == r) return nums[k]
    pivot = nums[l], i = l - 1, j = r + 1
    while i < j:
        do i += 1 while(nums[i] < pivot)
        do j -= 1 while(nums[j] > pivot)
        if i < j:
        swap(nums[i], nums[j])
    if k <= j) return quickSelect(nums, l, j, k:
    else return quickSelect(nums, j + 1, r, k)

```

**Comparison:**
- **Heap**: O(n log k) time, O(k) space - Simple and efficient for small k
- **QuickSelect**: O(n) average time, O(n²) worst case, O(1) space - Better for large k

## Two Heaps

Maintain two heaps to find median or balance elements.

### Find Median from Data Stream

```python
class MedianFinder:
heapq[int> maxHeap # Lower half (max heap)
heapq[int, list[int>, greater<int>> minHeap # Upper half (min heap)
def addNum(self, num):
    maxHeap.push(num)
    minHeap.push(maxHeap.top())
    maxHeap.pop()
    if len(maxHeap) < len(minHeap):
        maxHeap.push(minHeap.top())
        minHeap.pop()
def findMedian(self):
    if len(maxHeap) > len(minHeap):
        return maxHeap.top()
    return (maxHeap.top() + minHeap.top()) / 2.0

```

### Sliding Window Median

```python
def medianSlidingWindow(self, nums, k):
    multiset<int> window(nums.begin(), nums.begin() + k)
    mid = next(window.begin(), k / 2)
    list[double> medians
    for(i = k i <= len(nums) i += 1) :
    medians.append((double(mid) + prev(mid, 1 - k % 2)) / 2.0)
    if(i == len(nums)) break
    window.insert(nums[i])
    if(nums[i] < mid) mid -= 1
    if(nums[i - k] <= mid) mid += 1
    window.erase(window.lower_bound(nums[i - k]))
return medians

```

## Dijkstra's Algorithm

Use min heap for shortest path finding.

```python
# Shortest path from source to all nodes
def dijkstra(self, list[list[pair<int, graph, start):
    n = len(graph)
    list[int> dist(n, INT_MAX)
    dist[start] = 0
    # Min heap: :distance, node
    cmp = [](pair<int, int> a, pair<int, int> b) :
    return a.first > b.first # Min heap by distance
heapq[pair<int, int>, list[pair<int, int>>, decltype(cmp)> pq(cmp)
pq.push(:0, start)
while not not pq:
    [d, u] = pq.top()
    pq.pop()
    if(d > dist[u]) continue # Already processed with better distance
    for([v, weight] : graph[u]) :
    newDist = dist[u] + weight
    if newDist < dist[v]:
        dist[v] = newDist
        pq.push(:newDist, v)
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

