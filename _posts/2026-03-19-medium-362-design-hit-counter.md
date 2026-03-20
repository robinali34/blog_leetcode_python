---
layout: post
title: "362. Design Hit Counter"
date: 2026-03-19 00:00:00 -0700
categories: [leetcode, medium, design, queue, sliding-window]
tags: [leetcode, medium, design, deque, sliding-window]
permalink: /2026/03/19/medium-362-design-hit-counter/
---

# 362. Design Hit Counter

## Problem Statement

Design a hit counter that counts the number of hits received in the past **5 minutes** (i.e., the past 300 seconds).

Implement the `HitCounter` class:

- `HitCounter()` initializes the object.
- `void hit(int timestamp)` records a hit at `timestamp` (in seconds).
- `int getHits(int timestamp)` returns the number of hits in the past 5 minutes from `timestamp`.

Assume calls are made in **non-decreasing timestamp order**.

## Examples

**Example 1:**

```python
Input:
["HitCounter","hit","hit","hit","getHits","hit","getHits","getHits"]
[[],[1],[2],[3],[4],[300],[300],[301]]

Output:
[null,null,null,null,3,null,4,3]
```

## Constraints

- `1 <= timestamp <= 2 * 10^9`
- At most `300` calls to `hit` and `getHits` in total (LeetCode follow-up asks about much higher scale)
- Calls are made in non-decreasing timestamp order.

## Clarification Questions

1. **Window definition**: “Past 5 minutes” means hits with `timestamp - hit_time < 300` (inclusive of current second)?  
   **Assumption**: Yes — remove hits where `hit_time <= timestamp - 300`.
2. **Order guarantee**: Are timestamps non-decreasing across calls?  
   **Assumption**: Yes (given by problem).
3. **Scale follow-up**: What if hits are huge (many per second)?  
   **Assumption**: We should discuss a bucketed O(1)-space approach too.

## Interview Deduction Process (20 minutes)

**Step 1: Direct idea (5 min)**  
Store every hit timestamp. To answer `getHits(t)`, count timestamps in `(t-300, t]`.

**Step 2: Use monotonic order (7 min)**  
Since timestamps are non-decreasing, old hits are always at the front. A queue/deque naturally supports:

- append new hit at right
- pop expired hits from left

So each timestamp is added once and removed once.

**Step 3: Follow-up optimization (8 min)**  
If traffic is huge, storing every hit may be large. Because window size is fixed (300 seconds), use 300 buckets:

- `times[i]`: second currently stored in bucket `i`
- `hits[i]`: number of hits at that second

Index is `timestamp % 300`. Reset bucket if stale second.

## Solution Approach 1 — Deque sliding window (your approach)

Store each hit timestamp in a deque.  
On each `hit` or `getHits`, remove expired timestamps from the front.

### Python

```python
from collections import deque


class HitCounter:
    def __init__(self):
        self.hit_tracker = deque()

    def hit(self, timestamp: int) -> None:
        self.hit_tracker.append(timestamp)
        while self.hit_tracker and self.hit_tracker[0] + 300 <= self.hit_tracker[-1]:
            self.hit_tracker.popleft()

    def getHits(self, timestamp: int) -> int:
        while self.hit_tracker and self.hit_tracker[0] + 300 <= timestamp:
            self.hit_tracker.popleft()
        return len(self.hit_tracker)
```

**Complexity**
- `hit`: amortized O(1)
- `getHits`: amortized O(1)
- Space: O(k), where k = hits in the last 300 seconds

---

## Solution Approach 2 — Queue + binary search (prefix idea)

Keep all hit timestamps in a list (append-only). For `getHits(timestamp)`, find first index `> timestamp - 300` via `bisect_right`, then answer is `len(list) - idx`.

Useful when you rarely purge and want simple read logic.

### Python

```python
import bisect


class HitCounter:
    def __init__(self):
        self.hits = []

    def hit(self, timestamp: int) -> None:
        self.hits.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        left = bisect.bisect_right(self.hits, timestamp - 300)
        return len(self.hits) - left
```

**Complexity**
- `hit`: O(1)
- `getHits`: O(log n)
- Space: O(total hits ever) unless you additionally purge old hits

---

## Solution Approach 3 — Fixed 300 buckets (follow-up scalable)

Use constant-size arrays of length 300:

- `times[i]` stores which second this bucket currently represents.
- `hits[i]` stores hits count for that second.

For timestamp `t`, bucket index is `i = t % 300`:

- If `times[i] != t`, this bucket is stale → reset to this second.
- Else increment existing count.

For `getHits(t)`, sum `hits[i]` where `t - times[i] < 300`.

### Python

```python
class HitCounter:
    def __init__(self):
        self.times = [0] * 300
        self.hits = [0] * 300

    def hit(self, timestamp: int) -> None:
        i = timestamp % 300
        if self.times[i] != timestamp:
            self.times[i] = timestamp
            self.hits[i] = 1
        else:
            self.hits[i] += 1

    def getHits(self, timestamp: int) -> int:
        total = 0
        for i in range(300):
            if timestamp - self.times[i] < 300:
                total += self.hits[i]
        return total
```

**Complexity**
- `hit`: O(1)
- `getHits`: O(300) = O(1)
- Space: O(300) = O(1)

## Tradeoff Comparison

| Approach | hit | getHits | Space | Best for |
|---|---:|---:|---:|---|
| Deque sliding window | amortized O(1) | amortized O(1) | O(k) recent hits | Typical interviews / simple clean solution |
| List + binary search | O(1) | O(log n) | O(n) all hits | Append-heavy, read with binary search |
| 300-bucket circular | O(1) | O(1) | O(1) | Very high traffic follow-up |

## Edge Cases

- Multiple hits at same timestamp.
- `getHits` called with no hits.
- Large timestamps (up to 2e9) — all approaches handle this.

## Common Mistakes

- Expiry condition off-by-one: remove hits where `hit_time + 300 <= current_time`.
- Forgetting timestamp monotonic guarantee (deque approach relies on it).
- In bucket approach, forgetting to reset stale bucket before increment.

## Related Problems

- [LC 346: Moving Average from Data Stream](https://leetcode.com/problems/moving-average-from-data-stream/) — Sliding window stream design.
- [LC 933: Number of Recent Calls](https://leetcode.com/problems/number-of-recent-calls/) — Similar queue-based window counting.
- [LC 362: Design Hit Counter](https://leetcode.com/problems/design-hit-counter/) — This problem.

