---
layout: post
title: "[Hard] 218. The Skyline Problem"
date: 2025-10-05 00:00:00 -0000
categories: python sweep-line priority-queue data-structures union-find problem-solving
---

# [Hard] 218. The Skyline Problem

A city's skyline is the outer contour of the silhouette formed by all the buildings in that city when viewed from a distance. Given the locations and heights of all the buildings, return the skyline formed by these buildings collectively.

The geometric information of each building is given in the array `buildings` where `buildings[i] = [lefti, righti, heighti]`:

- `lefti` is the x coordinate of the left edge of the ith building.
- `righti` is the x coordinate of the right edge of the ith building.
- `heighti` is the height of the ith building.

You may assume all buildings are perfect rectangles grounded on an absolutely flat surface at height 0.

The skyline should be represented as a list of "key points" sorted by their x-coordinate in the form `[[x1,y1],[x2,y2],...]`. Each key point is the left endpoint of some horizontal segment in the skyline except the last point in the list, which always has a y-coordinate 0 and is used to mark the skyline's termination where the rightmost building ends. Any ground between the leftmost and rightmost buildings should be part of the skyline contour.

Note: There must be no consecutive horizontal lines of equal height in the output skyline. For instance, `[...[2 3],[4 5],[7 5],[11 5],[12 7]...]` is not acceptable; the three lines of height 5 should be merged into one: `[...[2 3],[4 5],[12 7]...]`

## Examples

**Example 1:**
```
Input: buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
Output: [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
Explanation:
Figure A shows the buildings of the input.
Figure B shows the skyline formed by those buildings. The red points in figure B represent the key points in the output list.
```

**Example 2:**
```
Input: buildings = [[0,2,3],[2,5,3]]
Output: [[0,3],[5,0]]
```

## Constraints

- `1 <= buildings.length <= 10^4`
- `0 <= lefti < righti <= 2^31 - 1`
- `1 <= heighti <= 2^31 - 1`
- `buildings` is sorted by `lefti` in non-decreasing order.

## Approach

This is a classic sweep line algorithm problem. The key insight is to process all building edges (start and end points) in sorted order and maintain the current maximum height at each position.

There are several approaches to solve this problem:

1. **Coordinate Compression + Brute Force**: Compress coordinates and update heights for each building
2. **Sweep Line with Map**: Use events and maintain height counts
3. **Sweep Line with Priority Queue**: Use priority queue to track active buildings
4. **Sweep Line with Two Priority Queues**: Separate queues for active and past heights
5. **Union Find Optimization**: Use Union Find to optimize the coordinate compression approach

## Solution 1: Coordinate Compression + Brute Force

```python
class Solution:
    def getSkyline(self, buildings: list[list[int]]) -> list[list[int]]:
        edgeSet = set()
        for building in buildings:
            left, right = building[0], building[1]
            edgeSet.add(left)
            edgeSet.add(right)
        edges = sorted(list(edgeSet))
        edgeIdxMap = {edge: i for i, edge in enumerate(edges)}
        heights = [0] * len(edges)
        for building in buildings:
            left, right, height = building[0], building[1], building[2]
            leftIdx, rightIdx = edgeIdxMap[left], edgeIdxMap[right]
            for idx in range(leftIdx, rightIdx):
                heights[idx] = max(heights[idx], height)
        result = []
        for i in range(len(heights)):
            curHeight, curPos = heights[i], edges[i]
            if i == 0 or curHeight != heights[i - 1]:
                result.append([curPos, curHeight])
        return result
```

**Time Complexity:** O(n²) - For each building, we update all positions it covers
**Space Complexity:** O(n) - Edge set and height array

### How it works:
1. **Collect all unique x-coordinates** (building edges)
2. **Create mapping** from coordinate to index
3. **For each building**, update heights in the range [left, right)
4. **Generate skyline** by checking height changes

## Solution 2: Sweep Line with Map

```python
from sortedcontainers import SortedDict

class Solution:
    def getSkyline(self, buildings: list[list[int]]) -> list[list[int]]:
        pairs = []
        for b in buildings:
            left, right, height = b[0], b[1], b[2]
            pairs.append((left, -height))
            pairs.append((right, height))
        
        pairs.sort(key=lambda x: (x[0], x[1]))
        
        result = []
        height_map = SortedDict({0: 1})
        pre = 0
        
        for x, h in pairs:
            if h < 0:
                height_map[-h] = height_map.get(-h, 0) + 1
            else:
                height_map[h] = height_map.get(h, 0) - 1
                if height_map[h] == 0:
                    del height_map[h]
            
            cur = height_map.keys()[-1]  # Get max key
            if cur != pre:
                result.append([x, cur])
                pre = cur
        
        return result
```

**Time Complexity:** O(n log n) - Sorting + map operations
**Space Complexity:** O(n) - Map and pairs vector

### How it works:
1. **Create events**: Start events with negative height, end events with positive height
2. **Sort events** by x-coordinate, then by height (negative heights first)
3. **Process events**: Add/remove heights from map
4. **Track maximum height** and add skyline points when it changes

## Solution 3: Sweep Line with Priority Queue

```python
import heapq

class Solution:
    def getSkyline(self, buildings: list[list[int]]) -> list[list[int]]:
        edges = []
        for i, building in enumerate(buildings):
            edges.append([building[0], i])
            edges.append([building[1], i])
        
        edges.sort()
        live = []  # Max heap: (-height, right)
        result = []
        idx = 0
        
        while idx < len(edges):
            cur = edges[idx][0]
            while idx < len(edges) and edges[idx][0] == cur:
                b = edges[idx][1]
                if buildings[b][0] == cur:
                    right = buildings[b][1]
                    height = buildings[b][2]
                    heapq.heappush(live, (-height, right))
                idx += 1
            
            while live and live[0][1] <= cur:
                heapq.heappop(live)
            
            curHeight = -live[0][0] if live else 0
            if not result or result[-1][1] != curHeight:
                result.append([cur, curHeight])
        
        return result
```

**Time Complexity:** O(n log n) - Sorting + priority queue operations
**Space Complexity:** O(n) - Priority queue and edges vector

### How it works:
1. **Create edge events** with building indices
2. **Sort edges** by x-coordinate
3. **Process events**: Add buildings to priority queue when they start
4. **Remove expired buildings** from priority queue
5. **Track maximum height** from active buildings

## Solution 4: Sweep Line with Two Priority Queues

```python
import heapq

class Solution:
    def getSkyline(self, buildings: list[list[int]]) -> list[list[int]]:
        edges = []
        for b in buildings:
            edges.append([b[0], b[2]])
            edges.append([b[1], -b[2]])
        
        edges.sort(key=lambda x: (x[0], -x[1]))
        
        live = []  # Max heap: (-height, height)
        past = []  # Max heap: (-height, height)
        result = []
        idx = 0
        
        while idx < len(edges):
            cur = edges[idx][0]
            while idx < len(edges) and edges[idx][0] == cur:
                height = edges[idx][1]
                if height > 0:
                    heapq.heappush(live, (-height, height))
                else:
                    heapq.heappush(past, (height, -height))
                idx += 1
            
            while live and past and live[0][1] == past[0][1]:
                heapq.heappop(live)
                heapq.heappop(past)
            
            curHeight = -live[0][0] if live else 0
            if not result or result[-1][1] != curHeight:
                result.append([cur, curHeight])
        
        return result
```
<｜tool▁calls▁begin｜><｜tool▁call▁begin｜>
grep

**Time Complexity:** O(n log n) - Sorting + priority queue operations
**Space Complexity:** O(n) - Two priority queues

### How it works:
1. **Create events**: Start with positive height, end with negative height
2. **Sort events** by x-coordinate, then by height (descending)
3. **Use two priority queues**: One for active heights, one for past heights
4. **Remove matching heights** from both queues
5. **Track maximum active height**

## Solution 5: Union Find Optimization

```python
class UnionFind:
    def __init__(self, n: int):
        self.root = list(range(n))
    
    def find(self, x: int) -> int:
        if self.root[x] != x:
            return self.find(self.root[x])
        return self.root[x]
    
    def merge(self, x: int, y: int) -> None:
        self.root[self.find(x)] = self.find(y)

class Solution:
    def getSkyline(self, buildings: list[list[int]]) -> list[list[int]]:
        buildings.sort(key=lambda x: x[2], reverse=True)
        edgeSet = set()
        for b in buildings:
            edgeSet.add(b[0])
            edgeSet.add(b[1])
        edges = sorted(list(edgeSet))
        edgeIdxMap = {edge: i for i, edge in enumerate(edges)}
        uf = UnionFind(len(edges))
        heights = [0] * len(edges)
        for b in buildings:
            left, right, height = b[0], b[1], b[2]
            leftIdx = uf.find(edgeIdxMap[left])
            rightIdx = edgeIdxMap[right]
            while leftIdx < rightIdx:
                heights[leftIdx] = height
                uf.merge(leftIdx, rightIdx)
                leftIdx += 1
                leftIdx = uf.find(leftIdx)
        result = []
        for i in range(len(edges)):
            if i == 0 or heights[i] != heights[i - 1]:
                result.append([edges[i], heights[i]])
        return result
```
<｜tool▁calls▁begin｜><｜tool▁call▁begin｜>
read_file

**Time Complexity:** O(n²) in worst case, but optimized with Union Find
**Space Complexity:** O(n) - Union Find and height arrays

### How it works:
1. **Sort buildings** by height (descending)
2. **Process buildings** in height order
3. **Use Union Find** to skip already processed positions
4. **Update heights** only for unprocessed positions

## Step-by-Step Example (Solution 2)

Let's trace through `buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]`:

### Create Events:
```
(2, -10), (9, 10)   // Building 1: height 10
(3, -15), (7, 15)   // Building 2: height 15  
(5, -12), (12, 12)  // Building 3: height 12
(15, -10), (20, 10) // Building 4: height 10
(19, -8), (24, 8)   // Building 5: height 8
```

### Sort Events:
```
(2, -10), (3, -15), (5, -12), (7, 15), (9, 10), (12, 12), (15, -10), (19, -8), (20, 10), (24, 8)
```

### Process Events:
1. **x=2**: Add height 10 → max=10 → add [2,10]
2. **x=3**: Add height 15 → max=15 → add [3,15]
3. **x=5**: Add height 12 → max=15 → no change
4. **x=7**: Remove height 15 → max=12 → add [7,12]
5. **x=9**: Remove height 10 → max=12 → no change
6. **x=12**: Remove height 12 → max=0 → add [12,0]
7. **x=15**: Add height 10 → max=10 → add [15,10]
8. **x=19**: Add height 8 → max=10 → no change
9. **x=20**: Remove height 10 → max=8 → add [20,8]
10. **x=24**: Remove height 8 → max=0 → add [24,0]

### Result: `[[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]`

## Algorithm Analysis

### Solution Comparison:

| Solution | Time Complexity | Space Complexity | Approach | Pros | Cons |
|----------|----------------|-----------------|----------|------|------|
| Coordinate Compression | O(n²) | O(n) | Brute Force | Simple logic | Inefficient |
| Sweep Line + Map | O(n log n) | O(n) | Event Processing | Clean, efficient | Map overhead |
| Sweep Line + PQ | O(n log n) | O(n) | Priority Queue | Intuitive | PQ cleanup needed |
| Two Priority Queues | O(n log n) | O(n) | Dual PQ | Handles duplicates | More complex |
| Union Find | O(n²) worst | O(n) | Optimization | Skips processed | Complex implementation |

### Key Insights:

1. **Event Processing**: Convert buildings to start/end events
2. **Height Tracking**: Maintain current maximum height efficiently
3. **Change Detection**: Only add skyline points when height changes
4. **Coordinate Handling**: Process events in sorted order
5. **Data Structure Choice**: Map vs Priority Queue trade-offs

## Common Mistakes

1. **Not handling height changes correctly** - Only add points when height changes
2. **Incorrect event sorting** - Must handle ties properly
3. **Memory management** - Clean up expired buildings from priority queue
4. **Edge cases** - Handle empty buildings, single building scenarios
5. **Coordinate precision** - Handle large coordinate values

## Edge Cases

1. **Single building**: `[[1,2,3]]` → `[[1,3],[2,0]]`
2. **Overlapping buildings**: Same height buildings
3. **Adjacent buildings**: Buildings touching at edges
4. **Large coordinates**: Integer overflow considerations
5. **Empty input**: Return empty skyline

## Related Problems

- [253. Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/)
- [56. Merge Intervals](https://leetcode.com/problems/merge-intervals/)
- [57. Insert Interval](https://leetcode.com/problems/insert-interval/)
- [715. Range Module](https://leetcode.com/problems/range-module/)
- [850. Rectangle Area II](https://leetcode.com/problems/rectangle-area-ii/)

## Conclusion

The Skyline Problem is a classic sweep line algorithm that tests understanding of:

1. **Event Processing**: Converting 2D problems to 1D events
2. **Data Structures**: Choosing appropriate structures for height tracking
3. **Algorithm Design**: Efficiently processing sorted events
4. **Edge Case Handling**: Managing height changes and duplicates

**Recommended Solution**: Solution 2 (Sweep Line with Map) offers the best balance of efficiency, clarity, and correctness for most scenarios.

The key insight is recognizing that skyline changes only occur at building edges, and we need to efficiently track the maximum height at each position while processing events in order.
