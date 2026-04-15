---
layout: post
title: "[Medium] 2406. Divide Intervals Into Minimum Number of Groups"
date: 2026-03-16 00:00:00 -0700
categories: [leetcode, medium, interval, heap, sweep-line]
tags: [leetcode, medium, intervals, heap, sweep-line]
permalink: /2026/03/16/medium-2406-divide-intervals-into-minimum-number-of-groups/
---

# [Medium] 2406. Divide Intervals Into Minimum Number of Groups

## Problem Statement

You are given a 2D integer array `intervals`, where `intervals[i] = [start_i, end_i]` describes an interval on the number line **including** both endpoints.

You must divide the intervals into **one or more groups** such that in each group, **no two intervals intersect** (i.e., no two intervals in the same group share any point).

Return the **minimum number of groups** you need to partition all the intervals.

Two intervals `[a, b]` and `[c, d]` intersect if there exists `x` such that `x` is in both intervals. Because intervals are inclusive, they intersect if `max(a, c) <= min(b, d)`.

## Examples

**Example 1:**

```python
Input: intervals = [[5,10],[6,8],[1,5],[2,3],[1,10]]
Output: 3
```

**Example 2:**

```python
Input: intervals = [[1,3],[5,6],[8,10],[11,13]]
Output: 1
# All intervals are non-overlapping; one group is enough.
```

## Constraints

- `1 <= intervals.length <= 10^5`
- `intervals[i].length == 2`
- `1 <= start_i <= end_i <= 10^9`

## Clarification Questions

1. **Inclusive endpoints**: Are endpoints inclusive?  
   **Assumption**: Yes. So `[a, b]` and `[c, d]` are non-overlapping iff `b < c` or `d < a`.
2. **Touching intervals**: If `b < c`, they can be in the same group; if `b >= c`, they intersect and must be in different groups.
3. **Reordering allowed**: We can reorder intervals arbitrarily to group them?  
   **Assumption**: Yes — we just have to partition them into valid groups.

## Interview Deduction Process (20 minutes)

**Step 1: Relation to “maximum overlap” (7 min)**  
Think of all intervals on the number line. The minimum number of groups needed so that no group has overlapping intervals is equal to the **maximum number of intervals overlapping at any point**. Intuition: if at some time `t` there are `k` overlapping intervals, they must all be in different groups → need at least `k` groups. Conversely, if you have `G` groups and `G` is at least the maximum overlap, you can greedily place intervals into these groups so that no group’s active intervals overlap.

**Step 2: How to compute max overlap (7 min)**  
Two common ways:

1. **Min-heap of end times** (meeting rooms pattern).  
2. **Sweep line with events** (+1 at start, -1 after end).

Both give the peak number of overlapping intervals.

**Step 3: Details for inclusivity (6 min)**  
Here endpoints are inclusive. So `[start, end]` and `[next_start, next_end]` are non-overlapping in a group only if `end < next_start`. That affects:

- Heap solution: we can reuse a group (pop an end time) when `min_end < start` (strict).  
- Sweep line: we add a `+1` at `start` and a `-1` at `end + 1` so that intervals are considered active on `[start, end]`.

## Solution Approach 1 — Min-heap of end times (Meeting Rooms style)

**Idea:** Sort intervals by start time. Use a min-heap storing the **end times** of currently active intervals (one per group). For each new interval `[start, end]`:

- If the earliest finishing group’s end time is **strictly less than** `start`, that group is now free (no overlap), so we pop it and reuse that group.  
- Push `end` for the new interval into the heap (either a reused group or a new group).  
- The heap size at the end is the number of groups used.

### Python Solution — Heap

```python
import heapq
from typing import List


class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals.sort()  # sort by start time, then end
        heap: list[int] = []  # min-heap of end times

        for start, end in intervals:
            if heap and heap[0] < start:
                heapq.heappop(heap)
            heapq.heappush(heap, end)

        return len(heap)
```

### Explanation

We sort by start time so we process intervals in chronological order. The heap keeps track of the end times of the last interval in each group. For each new interval `[start, end]`:

- If the smallest end time `heap[0]` is `< start`, that group’s last interval ends before this one starts; they do **not** overlap, so we can reuse that group: pop it.
- Push `end` to represent assigning this interval to some group (possibly reused or new).  
- The heap size is the number of groups used at any time; after processing all intervals, that is the minimum number of groups.

Because intervals are inclusive, we require `heap[0] < start` (strict) to say “no overlap.” If `heap[0] == start`, they share the point `start` and must be different groups.

## Solution Approach 2 — Sweep Line (difference array / events)

**Idea:** Convert intervals into events:

- At `start`: active interval count `+1`.  
- At `end + 1`: active interval count `-1` (since they are active through `end`).

Sort all events by coordinate and run a prefix sum to track current overlap and maximum overlap.

### Python Solution — Sweep Line

```python
from typing import List


class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        events: list[tuple[int, int]] = []
        for start, end in intervals:
            events.append((start, 1))
            events.append((end + 1, -1))

        events.sort()  # sort by coordinate

        curr_overlap = 0
        max_overlap = 0
        for _, delta in events:
            curr_overlap += delta
            if curr_overlap > max_overlap:
                max_overlap = curr_overlap

        return max_overlap
```

### Explanation

We process the line from left to right:

- When we see a `+1` event at `start`, an interval becomes active.  
- When we see a `-1` event at `end + 1`, that interval stops being active after `end`.

The prefix sum `curr_overlap` is the number of intervals active at the current coordinate. The maximum value of `curr_overlap` over all coordinates is the maximum number of overlapping intervals, which equals the minimum number of groups needed.

## Complexity Analysis

For both approaches:

- **Time**: O(n log n) for sorting (`n = len(intervals)`); heap operations add O(n log n) in the first solution; sweep line’s event sort is also O(n log n).  
- **Space**: O(n) for heap or events.

## Edge Cases

- Single interval → 1 group.  
- Non-overlapping chain of intervals → 1 group.  
- All intervals overlapping at a point → number of groups = number of intervals.  
- Large coordinates (up to 1e9) → sweep line uses sparse events, not an array; fine.

## Common Mistakes

- **Using `<=` instead of `<`** in the heap condition — With inclusive intervals, `[a,b]` and `[b,c]` intersect at `b`, so we can only reuse a group when `end < next_start` (strict).
- **Subtracting at `end` instead of `end + 1`** in sweep line — That would treat intervals as half-open and undercount overlaps at endpoints; use `end + 1` to honor inclusivity.

## Related Problems

- [LC 253: Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/) — Same heap idea for maximum overlapping meetings.  
- [LC 732: My Calendar III](https://leetcode.com/problems/my-calendar-iii/) — Sweep line / ordered map for maximum overlap.  
- [LC 56: Merge Intervals](https://leetcode.com/problems/merge-intervals/) — Sort and merge overlapping intervals.

---
layout: post
title: "2406. Divide Intervals Into Minimum Number of Groups"
date: 2026-03-16 00:00:00 -0700
categories: [leetcode, medium, interval, heap, sweep-line]
tags: [leetcode, medium, intervals, heap, sweep-line]
permalink: /2026/03/16/medium-2406-divide-intervals-into-minimum-number-of-groups/
---

# 2406. Divide Intervals Into Minimum Number of Groups

## Problem Statement

You are given a 2D integer array `intervals`, where `intervals[i] = [start_i, end_i]` describes an interval on the number line **including** both endpoints.

You must divide the intervals into **one or more groups** such that in each group, **no two intervals intersect** (i.e., no two intervals in the same group share any point).

Return the **minimum number of groups** you need to partition all the intervals.

Two intervals `[a, b]` and `[c, d]` intersect if there exists `x` such that `x` is in both intervals. Because intervals are inclusive, they intersect if `max(a, c) <= min(b, d)`.

## Examples

**Example 1:**

```python
Input: intervals = [[5,10],[6,8],[1,5],[2,3],[1,10]]
Output: 3
```

**Example 2:**

```python
Input: intervals = [[1,3],[5,6],[8,10],[11,13]]\nOutput: 1\n# All intervals are non-overlapping; one group is enough.\n```

## Constraints

- `1 <= intervals.length <= 10^5`
- `intervals[i].length == 2`
- `1 <= start_i <= end_i <= 10^9`

## Clarification Questions

1. **Inclusive endpoints**: Are endpoints inclusive?  \n   **Assumption**: Yes. So `[a, b]` and `[c, d]` are non-overlapping iff `b < c` or `d < a`.\n2. **Touching intervals**: If `b < c`, they can be in the same group; if `b >= c`, they intersect and must be in different groups.\n3. **Reordering allowed**: We can reorder intervals arbitrarily to group them?  \n   **Assumption**: Yes — we just have to partition them into valid groups.\n\n## Interview Deduction Process (20 minutes)\n\n**Step 1: Relation to “maximum overlap” (7 min)**  \nThink of all intervals on the number line. The minimum number of groups needed so that no group has overlapping intervals is equal to the **maximum number of intervals overlapping at any point**. Intuition: if at some time `t` there are `k` overlapping intervals, they must all be in different groups → need at least `k` groups. Conversely, if you have `G` groups and `G` is at least the maximum overlap, you can greedily place intervals into these groups so that no group’s active intervals overlap.\n\n**Step 2: How to compute max overlap (7 min)**  \nTwo common ways:\n\n1. **Min-heap of end times** (meeting rooms pattern).  \n2. **Sweep line with events** (+1 at start, -1 after end).\n\nBoth give the peak number of overlapping intervals.\n\n**Step 3: Details for inclusivity (6 min)**  \nHere endpoints are inclusive. So `[start, end]` and `[next_start, next_end]` are non-overlapping in a group only if `end < next_start`. That affects:\n\n- Heap solution: we can reuse a group (pop an end time) when `min_end < start` (strict).  \n- Sweep line: we add a `+1` at `start` and a `-1` at `end + 1` so that intervals are considered active on `[start, end]`.\n\n## Solution Approach 1 — Min-heap of end times (Meeting Rooms style)\n\n**Idea:** Sort intervals by start time. Use a min-heap storing the **end times** of currently active intervals (one per group). For each new interval `[start, end]`:\n\n- If the earliest finishing group’s end time is **strictly less than** `start`, that group is now free (no overlap), so we pop it and reuse that group.  \n- Push `end` for the new interval into the heap (either a reused group or a new group).  \n- The heap size at the end is the number of groups used.\n\n### Python Solution — Heap\n\n```python\nimport heapq\nfrom typing import List\n\n\nclass Solution:\n    def minGroups(self, intervals: List[List[int]]) -> int:\n        intervals.sort()  # sort by start time, then end\n        heap: list[int] = []  # min-heap of end times\n\n        for start, end in intervals:\n            if heap and heap[0] < start:\n                heapq.heappop(heap)\n            heapq.heappush(heap, end)\n\n        return len(heap)\n```\n\n### Explanation\n\nWe sort by start time so we process intervals in chronological order. The heap keeps track of the end times of the last interval in each group. For each new interval `[start, end]`:\n\n- If the smallest end time `heap[0]` is `< start`, that group’s last interval ends before this one starts; they do **not** overlap, so we can reuse that group: pop it.\n- Push `end` to represent assigning this interval to some group (possibly reused or new).  \n- The heap size is the number of groups used at any time; after processing all intervals, that is the minimum number of groups.\n\nBecause intervals are inclusive, we require `heap[0] < start` (strict) to say “no overlap.” If `heap[0] == start`, they share the point `start` and must be different groups.\n\n## Solution Approach 2 — Sweep Line (difference array / events)\n\n**Idea:** Convert intervals into events:\n\n- At `start`: active interval count `+1`.  \n- At `end + 1`: active interval count `-1` (since they are active through `end`).\n\nSort all events by coordinate and run a prefix sum to track current overlap and maximum overlap.\n\n### Python Solution — Sweep Line\n\n```python\nfrom typing import List\n\n\nclass Solution:\n    def minGroups(self, intervals: List[List[int]]) -> int:\n        events: list[tuple[int, int]] = []\n        for start, end in intervals:\n            events.append((start, 1))\n            events.append((end + 1, -1))\n\n        events.sort()  # sort by coordinate\n\n        curr_overlap = 0\n        max_overlap = 0\n        for _, delta in events:\n            curr_overlap += delta\n            if curr_overlap > max_overlap:\n                max_overlap = curr_overlap\n\n        return max_overlap\n```\n\n### Explanation\n\nWe process the line from left to right:\n\n- When we see a `+1` event at `start`, an interval becomes active.  \n- When we see a `-1` event at `end + 1`, that interval stops being active after `end`.\n\nThe prefix sum `curr_overlap` is the number of intervals active at the current coordinate. The maximum value of `curr_overlap` over all coordinates is the maximum number of overlapping intervals, which equals the minimum number of groups needed.\n\n## Complexity Analysis\n\nFor both approaches:\n\n- **Time**: O(n log n) for sorting (`n = len(intervals)`); heap operations add O(n log n) in the first solution; sweep line’s event sort is also O(n log n).  \n- **Space**: O(n) for heap or events.\n\n## Edge Cases\n\n- Single interval → 1 group.  \n- Non-overlapping chain of intervals → 1 group.  \n- All intervals overlapping at a point → number of groups = number of intervals.  \n- Large coordinates (up to 1e9) → sweep line uses sparse events, not an array; fine.\n\n## Common Mistakes\n\n- **Using `<=` instead of `<`** in the heap condition — With inclusive intervals, `[a,b]` and `[b,c]` intersect at `b`, so we can only reuse a group when `end < next_start` (strict).\n- **Subtracting at `end` instead of `end + 1`** in sweep line — That would treat intervals as half-open and undercount overlaps at endpoints; use `end + 1` to honor inclusivity.\n\n## Related Problems\n\n- [LC 253: Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/) — Same heap idea for maximum overlapping meetings.  \n- [LC 732: My Calendar III](https://leetcode.com/problems/my-calendar-iii/) — Sweep line / ordered map for maximum overlap.  \n- [LC 56: Merge Intervals](https://leetcode.com/problems/merge-intervals/) — Sort and merge overlapping intervals.\n+\n*** End Patch```}github -->
