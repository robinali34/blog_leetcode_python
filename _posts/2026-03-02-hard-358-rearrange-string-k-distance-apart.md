---
layout: post
title: "[Hard] 358. Rearrange String k Distance Apart"
date: 2026-03-02 00:00:00 -0700
categories: [leetcode, hard, string, heap, greedy]
tags: [leetcode, hard, string, heap, greedy, scheduling]
permalink: /2026/03/02/hard-358-rearrange-string-k-distance-apart/
---

# [Hard] 358. Rearrange String k Distance Apart

## Problem Statement

Given a string `s` and an integer `k`, rearrange the string so that the **same characters are at least distance `k` apart**.

Return **any valid rearranged string**. If it is **not possible**, return the empty string `""`.

## Examples

**Example 1:**

```python
Input:  s = "aabbcc", k = 3
Output: "abcabc"   # or any valid answer
```

**Example 2:**

```python
Input:  s = "aaabc", k = 3
Output: ""
Explanation: No valid rearrangement exists.
```

**Example 3:**

```python
Input:  s = "aaadbbcc", k = 2
Output: "abacabcd"   # or any valid answer
```

## Constraints

- `1 <= s.length <= 3 * 10^4`
- `s` consists of lowercase English letters
- `0 <= k <= s.length`

## Clarification Questions

1. **Return any valid string**: Do we need the lexicographically smallest, or just any valid arrangement?  
   **Assumption**: Any valid rearrangement is acceptable.  
2. **When k <= 1**: Is the original string always valid?  
   **Assumption**: Yes — distance constraint is trivial, so we can just return `s`.  
3. **Character set**: Only lowercase English letters?  
   **Assumption**: Yes, as in typical problem statement.  
4. **Exact distance vs at least**: Do equal characters need to be exactly `k` apart, or at least `k` apart?  
   **Assumption**: At least `k` apart (distance >= k).  
5. **Impossibility**: If impossible, should we return empty string or some special marker?  
   **Assumption**: Return `""`.  

## Interview Deduction Process (20 minutes)

**Step 1: Compare to Task Scheduler (5 min)**  
This is similar to CPU task scheduling with cooldown (like `621. Task Scheduler`), but with two important differences:
- We must return the **actual rearranged string**, not just a count.
- We **cannot insert idle slots**; every position must be a character from `s`.

So the pure counting formula from `621` is not enough; we need to **construct** a valid sequence.

**Step 2: Greedy structure (7 min)**  
We want to place characters so that:
- At each step, we use a character that is **available** (cooldown satisfied).
- Among available characters, we prefer the one with the **highest remaining frequency** (to avoid getting stuck later).

This suggests:
- A **max heap** keyed by remaining frequency.
- A **cooldown queue** to remember when characters can be used again.

**Step 3: Simulation with heap + queue (8 min)**  
We simulate step-by-step:

- Maintain `time` as the current position index (or step count).
- At each step:
  1. Release any characters from the cooldown queue whose `available_time` == current time and push them back to the heap.
  2. If the heap is empty but there are still characters in cooldown, we cannot place any character → **impossible**.
  3. Otherwise, pop the character with highest remaining frequency from the heap and append it to the result.
  4. Decrease its frequency; if it is still > 0, push it into cooldown with `available_time = time + k`.

Continue until both the heap and cooldown are empty.

## Solution Approach

We use:

- `Counter` to count character frequencies.
- A **max heap** (simulated via Python `heapq` with negative counts): elements `(-freq, ch)`.
- A **queue** (`deque`) to hold entries currently cooling down: `(available_time, -freq, ch)`.

Algorithm:

1. If `k <= 1`, return `s` (no separation needed).  
2. Initialize the heap with `(-freq, ch)` for each distinct character.  
3. Initialize an empty deque `cooldown` and an empty list `result`.  
4. Let `time = 0`. While `heap` or `cooldown` is not empty:
   - Increment `time`.
   - If `cooldown` front has `available_time == time`, pop it and push its `(count, ch)` back to heap.
   - If heap is empty now → impossible, return `""`.
   - Pop `(count, ch)` from heap; append `ch` to result.
   - If `count + 1 < 0` (still remaining), push `(time + k, count + 1, ch)` into `cooldown`.
5. Join `result` into a string and return.

### Key Insights

1. **Greedy choice**: Always pick the most frequent **allowed** character to avoid leaving high-frequency characters for the end where they may violate the distance constraint.

2. **Cooldown window**: The queue enforces that once we use a character at time `t`, it cannot be used again until time `t + k`. This automatically ensures the distance constraint.

3. **Impossibility detection**: If at any time there are still characters in cooldown but the heap is empty, we have remaining characters that cannot be placed anywhere without breaking the distance rule.

4. **Alphabet size is small**: At most 26 letters, so heap operations are cheap; the overall complexity is dominated by the number of positions \(N\).

## Python Solution (Heap + Cooldown Queue)

```python
import heapq
from collections import Counter, deque


class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        if k <= 1:
            # No distance constraint or trivial constraint
            return s

        freq = Counter(s)

        # Max heap on remaining count (store negative for heapq)
        max_heap: list[tuple[int, str]] = [(-cnt, ch) for ch, cnt in freq.items()]
        heapq.heapify(max_heap)

        # Queue of (available_time, -cnt, ch)
        cooldown = deque()

        res: list[str] = []
        time = 0

        while max_heap or cooldown:
            time += 1

            # Release any characters whose cooldown has expired
            if cooldown and cooldown[0][0] == time:
                _, neg_cnt, ch = cooldown.popleft()
                heapq.heappush(max_heap, (neg_cnt, ch))

            if not max_heap:
                # No available character to place, but we still have cooling ones
                return ""

            neg_cnt, ch = heapq.heappop(max_heap)
            res.append(ch)

            # Decrease count and put into cooldown if still remaining
            neg_cnt += 1  # since neg_cnt is negative, +1 moves it toward zero
            if neg_cnt < 0:
                cooldown.append((time + k, neg_cnt, ch))

        return "".join(res)
```

## Algorithm Explanation

We treat each position in the result as a **time step**.

- The heap always contains characters that are **currently allowed** to be used (cooldown satisfied).
- The queue contains characters that have been used recently and are waiting until they can be used again.
- At each step:
  - We first move any character from cooldown back to the heap if its `available_time` has arrived.
  - If we can pick something from the heap, we place it and send it back to cooldown with its next allowed time.

The `time + k` choice ensures that between two placements of the same character, there are at least `k - 1` different positions in between, so their indices differ by at least `k`.

## Example Walkthrough

Consider `s = "aaadbbcc", k = 2`.

Frequencies: `a:3, b:2, c:2, d:1`

- Step 1: `time=1`, heap has all letters. Pick `a` → `"a"`, push `a` into cooldown with `available_time=3`.
- Step 2: `time=2`, `a` still cooling. Heap has `b,c,d`. Pick `b` → `"ab"`, cooldown: `a@3,b@4`.
- Step 3: `time=3`, release `a` (available), heap: `a,c,d`. Pick `a` → `"aba"`, cooldown: `b@4,a@5`.
- Step 4: `time=4`, release `b`, heap: `b,c,d`. Pick `b` → `"abab"`, cooldown: `a@5,b@6`.
- Step 5: `time=5`, release `a`, heap: `a,c,d`. Pick `a` → `"ababa"`, cooldown: `b@6,a@7`.
- Step 6: `time=6`, release `b`, heap: `b,c,d`. Pick `c` → `"ababac"`, cooldown: `a@7,b@8,c@8`.
- Step 7: `time=7`, release `a`, heap: `a,c,d`. Pick `c` → `"ababacc"`, cooldown: `b@8,c@9`.
- Step 8: `time=8`, release `b`, heap: `b,d`. Pick `d` → `"ababaccd"`, cooldown: `c@9` (if still remaining).

Result string `"ababaccd"` (or similar) respects the distance ≥ 2 rule for all equal characters.

## Complexity Analysis

- **Time Complexity**:  
  \(O(N \log \Sigma)\) where \(N = |s|\) and \(\Sigma\) is alphabet size (≤ 26).  
  In practice this is effectively linear in \(N\).

- **Space Complexity**:  
  \(O(\Sigma)\) for frequencies, heap, and cooldown queue.

## Edge Cases

- `k == 0` or `k == 1`: Any arrangement is valid; we can just return `s`.
- All identical characters, e.g. `s = "aaaa", k = 3` → impossible, return `""`.
- Large `k` relative to `|s|`: Often impossible unless many different characters exist.

## Common Mistakes

- Only using a **heap** without a cooldown queue, which fails to enforce the distance constraint.
- Trying to adapt the **closed-form formula** from `621. Task Scheduler` directly without actually constructing a string.
- Forgetting to detect impossibility when the heap is empty but cooldown still contains characters.
- Incorrect handling of `k <= 1` edge case and returning an over-complicated answer when simple `s` is enough.

## Related Problems

- [LC 621: Task Scheduler](/2026/03/02/medium-621-task-scheduler/) — Similar cooldown idea but returns minimum time, not an explicit schedule.
- [LC 767: Reorganize String](https://leetcode.com/problems/reorganize-string/) — Distance constraint with \(k = 2\), can be solved with a similar heap pattern.

