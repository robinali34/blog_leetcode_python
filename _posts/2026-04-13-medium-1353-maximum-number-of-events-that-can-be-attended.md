---
layout: post
title: "[Medium] 1353. Maximum Number of Events That Can Be Attended"
date: 2026-04-13 00:00:00 -0700
categories: [leetcode, medium, greedy, heap, sorting, scheduling]
permalink: /2026/04/13/medium-1353-maximum-number-of-events-that-can-be-attended/
tags: [leetcode, medium, greedy, heap, priority-queue, interval-scheduling]
---

# [Medium] 1353. Maximum Number of Events That Can Be Attended

You are given an array of `events` where `events[i] = [startDay, endDay]`, meaning you may attend that event on **any** single day in the closed interval `[startDay, endDay]`.

You can attend **at most one event per day**. Return *the maximum number of events* you can attend.

## Examples

**Example 1:**
```
Input: events = [[1,2],[2,3],[3,4]]
Output: 3
Explanation: Attend all three on days 1, 2, and 3 (or 2, 3, 4).
```

**Example 2:**
```
Input: events = [[1,2],[2,3],[3,4],[1,2]]
Output: 4
```

**Example 3:**
```
Input: events = [[1,4],[4,4],[2,2],[3,4],[1,1]]
Output: 4
```

## Constraints

- `1 <= events.length <= 10^5`
- `events[i].length == 2`
- `1 <= startDay <= endDay <= 10^5`

## Clarification Questions

1. **Flexibility**: Can you pick any day in `[start, end]`? (Yes — one day per event, anywhere in the window.)
2. **Capacity**: How many events per day? (At most one.)
3. **Goal**: Maximize count of attended events, not duration or value.
4. **Overlaps**: Many events may overlap; you choose which to take each day.

## Why This Problem Is Different

### 1. Each event is flexible

You do **not** have to attend on `startDay`. Any day in `[start, end]` works.

So this is **scheduling on a time axis**: you assign each attended event to a concrete day, with at most one event per day.

### 2. Greedy insight

On any day when you are free to attend something, you should attend the **available** event whose window **ends the soonest** (smallest `end` among candidates).

**Why?** Events with an earlier deadline are the riskiest to postpone. Long windows can usually wait; tight windows cannot. Standard exchange argument: swapping a later-deadline event for an earlier-deadline one cannot reduce the number of events you can still fit.

### 3. Efficient simulation

We need to:

- Walk through time (or process events in start order).
- Know which events are **already available** (started) and **still valid** (not past `end`).
- Repeatedly pick the candidate with **minimum `end`**.

That leads naturally to a **min-heap (priority queue)** of end days.

## Final Algorithm

1. **Sort** `events` by `start` (and by `end` as a tie-breaker if you like).
2. Maintain a **min-heap** of **end days** for events that have started and might still be attended.
3. Maintain a **day** pointer (or jump `day` to the next event start when the heap is empty).
4. Each iteration:
   - **Push** all events with `start <= day` (advance the scan index `i`).
   - **Pop** from the heap while `heap[0] < day` (those windows closed before today).
   - If the heap is non-empty, **attend** one event: pop the smallest `end`, increment answer, move to `day + 1`.

Using the smallest `end` each time matches the greedy rule above.

## Solution

```python
import heapq
from typing import List


class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()
        heap: list[int] = []
        i = 0
        n = len(events)
        day = 0
        rtn = 0
        while i < n or heap:
            if not heap:
                day = events[i][0]
            while i < n and events[i][0] <= day:
                heapq.heappush(heap, events[i][1])
                i += 1
            while heap and heap[0] < day:
                heapq.heappop(heap)
            if heap:
                heapq.heappop(heap)
                rtn += 1
                day += 1
        return rtn
```

## Complexity

- **Time:** `O(n log n)` for sorting plus `O(n log n)` heap work over the simulation (each event pushed/popped a constant number of times in typical analyses).
- **Space:** `O(n)` for the heap in the worst case.

## Edge Cases

- Empty `events` after sort: loop exits immediately; return `0`.
- All events share the same day: heap picks by smallest `end` first; still correct.
- Very long `endDay`: algorithm only steps `day` forward when work is done; empty heap jumps `day` to the next `start`.

## Related Problems

- [630. Course Schedule III](https://leetcode.com/problems/course-schedule-iii/) — similar “pick by deadline” greedy with a heap
- [452. Minimum Number of Arrows to Burst Balloons](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/) — interval greedy on the line

---

*Flexible intervals plus one job per day make this a classic greedy scheduling pattern: always serve the task that becomes impossible soonest.*
