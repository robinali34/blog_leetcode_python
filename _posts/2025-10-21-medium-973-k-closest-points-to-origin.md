---
layout: post
title: "LC 973: K Closest Points to Origin"
date: 2025-10-21 15:30:00 -0700
categories: leetcode medium array sorting
permalink: /posts/2025-10-21-medium-973-k-closest-points-to-origin/
tags: [leetcode, medium, array, sorting, heap, quickselect]
---

# LC 973: K Closest Points to Origin

**Difficulty:** Medium  
**Category:** Array, Sorting, Heap, Quickselect  
**Companies:** Amazon, Google, Facebook, Microsoft

## Problem Statement

Given an array of `points` where `points[i] = [xi, yi]` represents a point on the X-Y plane and an integer `k`, return the `k` closest points to the origin `(0, 0)`.

The distance between two points on the X-Y plane is the Euclidean distance (i.e., `√((x1 - x2)² + (y1 - y2)²)`).

You may return the answer in **any order**. The answer is **guaranteed** to be **unique** (except for the order that it is in).

### Examples

**Example 1:**
```
Input: points = [[1,1],[2,2],[3,3]], k = 1
Output: [[1,1]]
Explanation:
The distance between (1, 1) and the origin is sqrt(2).
The distance between (2, 2) and the origin is sqrt(8).
The distance between (3, 3) and the origin is sqrt(18).
Since sqrt(2) < sqrt(8) < sqrt(18), we return [[1,1]].
```

**Example 2:**
```
Input: points = [[3,3],[5,-1],[-2,4]], k = 2
Output: [[3,3],[-2,4]]
Explanation: The answer [[-2,4],[3,3]] would also be accepted.
```

### Constraints

- `1 <= k <= points.length <= 10^4`
- `-10^4 <= xi, yi <= 10^4`

## Solution Approach

### Key Insight

Since we're finding the distance to the origin `(0, 0)`, we can simplify the distance calculation:
- **Euclidean distance**: `√(x² + y²)`
- **For comparison**: We can use `x² + y²` instead of `√(x² + y²)` since square root is monotonically increasing
- **Manhattan distance approximation**: `|x| + |y|` (not exact but useful for some optimizations)

### Approach 1: Sorting (Recommended)

**Algorithm:**
1. Sort all points by their squared distance to origin
2. Return the first `k` points

**Time Complexity:** O(n log n)  
**Space Complexity:** O(1) (excluding output)

```python
class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        points.sort(key=lambda p: p[0] * p[0] + p[1] * p[1])
        return points[:k]
```

### Approach 2: Max Heap

**Algorithm:**
1. Use a max heap to maintain the `k` closest points
2. For each point, if heap size < k, add it
3. If heap size = k and current point is closer than farthest in heap, replace it

**Time Complexity:** O(n log k)  
**Space Complexity:** O(k)

```python
import heapq

class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        # Use negative distance for max heap (Python has min heap)
        maxHeap = []
        
        for point in points:
            dist = point[0] * point[0] + point[1] * point[1]
            if len(maxHeap) < k:
                heapq.heappush(maxHeap, (-dist, point))
            elif dist < -maxHeap[0][0]:
                heapq.heappop(maxHeap)
                heapq.heappush(maxHeap, (-dist, point))
        
        result = [point for _, point in maxHeap]
        return result
```

### Approach 3: Quickselect (Optimal for Large k)

**Algorithm:**
1. Use quickselect to find the k-th smallest distance
2. Partition points around this distance
3. Return first k points

**Time Complexity:** O(n) average, O(n²) worst case  
**Space Complexity:** O(1)

```python
class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        left, right = 0, len(points) - 1
        
        while left <= right:
            pivotIndex = self.partition(points, left, right)
            if pivotIndex == k:
                break
            elif pivotIndex < k:
                left = pivotIndex + 1
            else:
                right = pivotIndex - 1
        
        return points[:k]
    
    def partition(self, points: list[list[int]], left: int, right: int) -> int:
        def getDistance(point):
            return point[0] * point[0] + point[1] * point[1]
        
        pivotDist = getDistance(points[right])
        i = left
        
        for j in range(left, right):
            if getDistance(points[j]) <= pivotDist:
                points[i], points[j] = points[j], points[i]
                i += 1
        points[i], points[right] = points[right], points[i]
        return i
```

## Complexity Analysis

| Approach | Time Complexity | Space Complexity | Best When |
|----------|-----------------|------------------|-----------|
| Sorting | O(n log n) | O(1) | General purpose, simple |
| Max Heap | O(n log k) | O(k) | k << n, memory constrained |
| Quickselect | O(n) avg | O(1) | Large datasets, k ≈ n |

## Key Insights

1. **Distance Simplification**: Use squared distance `x² + y²` instead of `√(x² + y²)` for comparison
2. **Sorting Trade-offs**: Simple but sorts all elements even when we only need k
3. **Heap Optimization**: Better when k is much smaller than n
4. **Quickselect Advantage**: Optimal average case but more complex implementation

## Follow-up Questions

- What if we need to handle dynamic updates (add/remove points)?
- How would you optimize for very large datasets that don't fit in memory?
- What if we need the k-th closest point in sorted order?

## Related Problems

- [LC 215: Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/)
- [LC 347: Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/)
- [LC 692: Top K Frequent Words](https://leetcode.com/problems/top-k-frequent-words/)

---

*This problem demonstrates the importance of choosing the right data structure and algorithm based on the constraints and requirements.*
