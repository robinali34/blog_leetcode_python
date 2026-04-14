---
layout: post
title: "LC 347: Top K Frequent Elements"
date: 2025-10-21 16:00:00 -0700
categories: leetcode medium array hash-table heap
permalink: /posts/2025-10-21-medium-347-top-k-frequent-elements/
tags: [leetcode, medium, array, hash-table, heap, bucket-sort, quickselect]
---

# LC 347: Top K Frequent Elements

**Difficulty:** Medium  
**Category:** Array, Hash Table, Heap, Bucket Sort, Quickselect  
**Companies:** Amazon, Google, Facebook, Microsoft, Apple

## Problem Statement

Given an integer array `nums` and an integer `k`, return the `k` most frequent elements. You may return the answer in **any order**.

### Examples

**Example 1:**
```
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
```

**Example 2:**
```
Input: nums = [1], k = 1
Output: [1]
```

### Constraints

- `1 <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`
- `k` is in the range `[1, the number of unique elements in the array]`
- It is **guaranteed** that the answer is **unique**

## Solution Approaches

### Approach 1: Bucket Sort (Optimal)

**Algorithm:**
1. Count frequency of each element using hash map
2. Create buckets where index represents frequency
3. Iterate buckets from highest to lowest frequency
4. Collect elements until we have k elements

**Time Complexity:** O(n)  
**Space Complexity:** O(n)

```python
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq = {}

        # Step 1: count frequencies
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        n = len(nums)

        # Step 2: create buckets
        buckets = [[] for _ in range(n + 1)]
        for num, count in freq.items():
            buckets[count].append(num)

        # Step 3: collect top k frequent
        result = []
        for i in range(n, -1, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result

        return result
```

### Approach 2: Quickselect

**Algorithm:**
1. Count frequency of each element
2. Create array of unique elements
3. Use quickselect to find k-th largest frequency
4. Return elements with frequencies >= k-th largest

**Time Complexity:** O(n) average, O(n²) worst case  
**Space Complexity:** O(n)

```python
import random

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count_map = {}

        # Step 1: build frequency map
        for n in nums:
            count_map[n] = count_map.get(n, 0) + 1

        unique = list(count_map.keys())
        n = len(unique)

        # Step 2: quickselect
        self.quickselect(unique, count_map, 0, n - 1, n - k)

        # Step 3: return top k
        return unique[n - k:]

    def partition(self, arr, count_map, left, right, pivot_index):
        pivot_freq = count_map[arr[pivot_index]]

        # move pivot to end
        arr[pivot_index], arr[right] = arr[right], arr[pivot_index]

        store = left

        for i in range(left, right):
            if count_map[arr[i]] < pivot_freq:
                arr[store], arr[i] = arr[i], arr[store]
                store += 1

        # move pivot to correct place
        arr[store], arr[right] = arr[right], arr[store]
        return store

    def quickselect(self, arr, count_map, left, right, k_smallest):
        if left >= right:
            return

        pivot_index = left + random.randint(0, right - left)
        pivot_index = self.partition(arr, count_map, left, right, pivot_index)

        if k_smallest == pivot_index:
            return
        elif k_smallest < pivot_index:
            self.quickselect(arr, count_map, left, pivot_index - 1, k_smallest)
        else:
            self.quickselect(arr, count_map, pivot_index + 1, right, k_smallest)
```

### Approach 3: Min Heap

**Algorithm:**
1. Count frequency of each element
2. Use min heap of size k to maintain top k frequent elements
3. For each element, if heap size < k, add it
4. If heap size = k and current element has higher frequency than minimum in heap, replace it

**Time Complexity:** O(n log k)  
**Space Complexity:** O(n)

```python
import heapq

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq = {}

        # Step 1: build frequency map
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        # Step 2: maintain min heap of size k
        minHeap = []

        for num, count in freq.items():
            if len(minHeap) < k:
                heapq.heappush(minHeap, (count, num))
            elif count > minHeap[0][0]:
                heapq.heappop(minHeap)
                heapq.heappush(minHeap, (count, num))

        # Step 3: extract result
        result = []
        while minHeap:
            result.append(heapq.heappop(minHeap)[1])

        return result
```

### Approach 4: Max Heap

**Algorithm:**
1. Count frequency of each element
2. Use max heap to store all elements with their frequencies
3. Extract top k elements from heap

**Time Complexity:** O(n log n)  
**Space Complexity:** O(n)

```python
import heapq

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq = {}

        # Step 1: build frequency map
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        # Step 2: build max heap using negative counts
        maxHeap = []
        for num, count in freq.items():
            heapq.heappush(maxHeap, (-count, num))

        # Step 3: extract top k
        result = []
        for _ in range(k):
            result.append(heapq.heappop(maxHeap)[1])

        return result
```

## Complexity Analysis

| Approach | Time Complexity | Space Complexity | Best When |
|----------|-----------------|------------------|-----------|
| Bucket Sort | O(n) | O(n) | General purpose, optimal |
| Quickselect | O(n) avg, O(n²) worst | O(n) | Large datasets, k ≈ n |
| Min Heap | O(n log k) | O(n) | k << n, memory efficient |
| Max Heap | O(n log n) | O(n) | Simple implementation |

## Key Insights

1. **Bucket Sort Advantage**: Most efficient with O(n) time complexity
2. **Frequency Range**: Maximum frequency is at most n (array length)
3. **Heap Trade-offs**: Min heap better when k is small, max heap simpler but less efficient
4. **Quickselect Optimization**: Good average case but worst case can be O(n²)

## Algorithm Comparison

### Bucket Sort vs Heap Approaches

**Bucket Sort:**
- ✅ O(n) time complexity
- ✅ Simple implementation
- ❌ Uses O(n) extra space for buckets

**Min Heap:**
- ✅ O(n log k) time, good when k << n
- ✅ Memory efficient
- ❌ More complex implementation

**Max Heap:**
- ✅ Simple implementation
- ❌ O(n log n) time complexity
- ❌ Less efficient than min heap

## Follow-up Questions

- What if we need to handle dynamic updates (add/remove elements)?
- How would you optimize for very large datasets that don't fit in memory?
- What if we need the k most frequent elements in sorted order by frequency?

## Related Problems

- [LC 215: Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/)
- [LC 973: K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/)
- [LC 692: Top K Frequent Words](https://leetcode.com/problems/top-k-frequent-words/)

## Implementation Notes

1. **Bucket Sort**: Use `vector<vector<int>>` where index represents frequency
2. **Quickselect**: Random pivot selection for better average performance
3. **Heap**: Use `priority_queue` with custom comparator for min/max heap
4. **Hash Map**: `unordered_map` for O(1) frequency counting

---

*This problem demonstrates the importance of choosing the right algorithm based on constraints and requirements. Bucket sort provides optimal O(n) solution for this specific problem.*
