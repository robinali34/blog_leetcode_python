---
layout: post
title: "[Hard] 850. Rectangle Area II"
date: 2025-12-16 00:00:00 -0800
categories: leetcode algorithm hard cpp geometry sweep-line segment-tree problem-solving
---

{% raw %}
You are given a 2D array of axis-aligned `rectangles`. For each `rectangle[i] = [xi1, yi1, xi2, yi2]`, where `(xi1, yi1)` is the bottom-left corner and `(xi2, yi2)` is the top-right corner of the `ith` rectangle.

Calculate the **total area** covered by all `rectangles` in the plane. Any area covered by two or more rectangles should only be counted **once**.

Return the total area. Since the answer may be too large, return it **modulo** `10^9 + 7`.

## Examples

**Example 1:**
```
Input: rectangles = [[0,0,2,2],[1,0,2,3],[1,0,3,1]]
Output: 6
Explanation: A total area of 6 is covered by all three rectangles, as illustrated in the picture.
From (1,1) to (2,2), the green and red rectangles overlap.
```

**Example 2:**
```
Input: rectangles = [[0,0,1000000000,1000000000]]
Output: 49
Explanation: The answer is 10^18 modulo (10^9 + 7), which is 49.
```

## Constraints

- `1 <= rectangles.length <= 200`
- `rectangles[i].length == 4`
- `0 <= xi1, yi1, xi2, yi2 <= 10^9`
- `xi1 <= xi2`
- `yi1 <= yi2`

## Thinking Process

1. **Sweep line**: Convert 2D problem to 1D by sweeping along one axis

- Identify the pattern from constraints (sorted? graph? optimal substructure?).
- Write brute force first mentally, then optimize the bottleneck.
- Verify edge cases: empty input, single element, duplicates.

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 230 110" style="max-width:100%;height:auto;display:block;margin:1.5em auto;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif">
<text x="50%" y="18" text-anchor="middle" font-size="13" font-weight="600" fill="#5A5752">Array + hash map</text>

  <rect x="30" y="45" width="28" height="28" rx="3" fill="#E8E3D8" stroke="#B8B5B0"/><text x="44" y="61" text-anchor="middle" font-size="10">2</text>
  <rect x="62" y="45" width="28" height="28" rx="3" fill="#E0D8E4" stroke="#A098A8"/><text x="76" y="61" text-anchor="middle" font-size="10">7</text>
  <rect x="106" y="45" width="28" height="28" rx="3" fill="#E8E3D8" stroke="#B8B5B0"/><text x="120" y="61" text-anchor="middle" font-size="10">11</text>
  <rect x="150" y="40" width="60" height="38" rx="4" fill="#FAF8F5" stroke="#D4D1CC"/>
  <text x="180" y="61" text-anchor="middle" font-size="10" fill="#6B6560">map</text>
  <text x="110" y="100" text-anchor="middle" font-size="11" fill="#6B6560">hash map for O(1) lookups</text>

</svg>

## Common Approaches

Typical techniques for this pattern:

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| **Brute force** *(this problem)* | Often O(n^2) or O(2^n) | O(n) | Baseline; clarifies the optimization target |
| Sort + scan | O(n log n) | O(1) | Pairs, intervals, greedy ordering |
| Hash map / set | O(n) | O(n) | Frequency, membership, two-sum style |
| Single-pass linear | O(n) | O(1) | Two pointers, sliding window, Kadane |

## Solution

**Time Complexity:** O(n² log n) - Sorting events + O(n) per event for coverage calculation  
**Space Complexity:** O(n) - For events and coordinate arrays

This solution uses a sweep line algorithm with coordinate compression to handle large coordinate values efficiently.

```python
class Solution:
    def rectangleArea(self, rectangles):
        MOD = 10**9 + 7

        OPEN, CLOSE = 1, -1

        xCoords = []
        events = []  # (y, type, x1, x2)

        for x1, y1, x2, y2 in rectangles:
            xCoords.append(x1)
            xCoords.append(x2)

            events.append((y1, OPEN, x1, x2))
            events.append((y2, CLOSE, x1, x2))

        # coordinate compression
        xCoords = sorted(set(xCoords))

        xIdx = {x: i for i, x in enumerate(xCoords)}

        # sort events by y, OPEN before CLOSE if same y
        events.sort(key=lambda x: (x[0], -x[1]))

        n = len(xCoords)
        count = [0] * n

        def calc_covered():
            covered = 0
            for i in range(n - 1):
                if count[i] > 0:
                    covered += xCoords[i + 1] - xCoords[i]
            return covered

        res = 0
        prevY = events[0][0]

        for y, typ, x1, x2 in events:
            res += calc_covered() * (y - prevY)
            res %= MOD

            i1, i2 = xIdx[x1], xIdx[x2]

            for i in range(i1, i2):
                count[i] += typ

            prevY = y

        return res % MOD
```

### Solution Explanation

**Approach:** Brute force (this problem)

**Key idea:** 1. **Sweep line**: Convert 2D problem to 1D by sweeping along one axis

**How the code works:**
1. **Sweep line**: Convert 2D problem to 1D by sweeping along one axis
- Identify the pattern from constraints (sorted? graph? optimal substructure?).
- Write brute force first mentally, then optimize the bottleneck.
- Verify edge cases: empty input, single element, duplicates.

**Walkthrough** — input `rectangles = [[0,0,2,2],[1,0,2,3],[1,0,3,1]]`, expected output `6`:

A total area of 6 is covered by all three rectangles, as illustrated in the picture.
From (1,1) to (2,2), the green and red rectangles overlap.

| Solution | Time | Space | Notes |
|----------|------|-------|-------|
| Sweep Line + Array | O(n² log n) | O(n) | Simple, good for n ≤ 200 |
| Sweep Line + Segment Tree | O(n log n) | O(n) | Optimal for large n |

### How Solution 1 Works

1. **Event Generation**:
   - For each rectangle, create two events:
     - OPEN event at bottom edge (y1): Start covering x-range [x1, x2]
     - CLOSE event at top edge (y2): Stop covering x-range [x1, x2]

2. **Coordinate Compression**:
   - Collect all unique x-coordinates
   - Map them to indices for efficient segment tracking
   - This handles large coordinate values (up to 10^9)

3. **Sweep Line**:
   - Process events from bottom to top (sorted by y)
   - At each event, calculate the covered area since the last event
   - Area = coveredLength × (currentY - previousY)

4. **Coverage Tracking**:
   - `count[i]` tracks how many rectangles cover the segment [xCoords[i], xCoords[i+1]]
   - OPEN events increment count, CLOSE events decrement

### Key Insight

The sweep line moves vertically (along y-axis), and at each position, we calculate the horizontal coverage. By processing events in order, we can compute the total area incrementally.
## Example Walkthrough

**Input:** `rectangles = [[0,0,2,2],[1,0,2,3],[1,0,3,1]]`

### Coordinate Compression:
```
X-coordinates: [0, 1, 2, 3]
Indices:       [0, 1, 2, 3]
```

### Events (sorted by y):
```
y=0: OPEN  [0,2] (rect 0)
y=0: OPEN  [1,2] (rect 1)
y=0: OPEN  [1,3] (rect 2)
y=1: CLOSE [1,3] (rect 2)
y=2: CLOSE [0,2] (rect 0)
y=3: CLOSE [1,2] (rect 1)
```

### Processing:
```
y=0 to y=1:
  Coverage: [0,1]=1, [1,2]=3, [2,3]=1
  Length: (1-0) + (2-1) + (3-2) = 3
  Area: 3 × (1-0) = 3

y=1 to y=2:
  After CLOSE [1,3]: [0,1]=1, [1,2]=2, [2,3]=0
  Length: (1-0) + (2-1) = 2
  Area: 2 × (2-1) = 2

y=2 to y=3:
  After CLOSE [0,2]: [0,1]=0, [1,2]=1, [2,3]=0
  Length: (2-1) = 1
  Area: 1 × (3-2) = 1

Total: 3 + 2 + 1 = 6
```

### Complexity
| Solution | Time | Space | Notes |
|----------|------|-------|-------|
| Sweep Line + Array | O(n² log n) | O(n) | Simple, good for n ≤ 200 |
| Sweep Line + Segment Tree | O(n log n) | O(n) | Optimal for large n |

## Common Mistakes

1. **Single rectangle**: Just return its area modulo MOD
2. **Large coordinates**: Use coordinate compression
3. **Overlapping rectangles**: Coverage counting handles duplicates
4. **Adjacent rectangles**: Properly counted as separate areas
5. **Large area**: Result can exceed 10^18, must use modulo

1. **Integer overflow**: Use `long long` for intermediate calculations
2. **Modulo operations**: Apply modulo correctly to avoid overflow
3. **Event ordering**: Process OPEN before CLOSE at same y-coordinate
4. **Coordinate compression**: Don't forget to map back to actual lengths
5. **Segment tree indexing**: Be careful with 0-based vs 1-based indexing

## Optimization Tips

1. **Use segment tree**: For O(log n) updates instead of O(n)
2. **Sort events once**: Avoid repeated sorting
3. **Process same-y events together**: Can batch updates
4. **Use `set` for deduplication**: Automatically sorts and removes duplicates

## Related Problems

- [218. The Skyline Problem](https://www.leetcode.com/problems/the-skyline-problem/) - Similar sweep line approach
- [391. Perfect Rectangle](https://www.leetcode.com/problems/perfect-rectangle/) - Rectangle coverage
- [836. Rectangle Overlap](https://www.leetcode.com/problems/rectangle-overlap/) - Simpler overlap detection
- [223. Rectangle Area](https://www.leetcode.com/problems/rectangle-area/) - Two rectangles only

## Pattern Recognition

This problem demonstrates the **"Sweep Line with Segment Tree"** pattern:

```
1. Generate events (start/end of ranges)
2. Coordinate compress if needed
3. Sort events by sweep dimension
4. Use segment tree for efficient range updates
5. Calculate answer incrementally
```

Similar problems:
- Skyline Problem
- Interval Coverage
- Range Sum Queries with Updates

## Real-World Applications

1. **Computer Graphics**: Calculating visible areas
2. **GIS Systems**: Computing land coverage
3. **Collision Detection**: Finding overlapping regions
4. **Layout Algorithms**: Determining occupied space
5. **Map Rendering**: Tile coverage calculations
## References

- [LC 850: Rectangle Area II on LeetCode](https://www.leetcode.com/problems/rectangle-area-ii/)
- [LeetCode Discuss — LC 850: Rectangle Area II](https://www.leetcode.com/problems/rectangle-area-ii/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/rectangle-area-ii/editorial/) *(may require premium)*

## Key Takeaways

1. **Sweep line**: Convert 2D problem to 1D by sweeping along one axis
2. **Coordinate compression**: Handle large coordinates by mapping to indices
3. **Event-based processing**: Track when rectangles start/end coverage
4. **Coverage counting**: Count overlapping rectangles instead of boolean coverage
5. **Segment tree**: Efficient range updates and queries

{% endraw %}
