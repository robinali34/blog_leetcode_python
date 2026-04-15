---
layout: post
title: "[Medium] 621. Task Scheduler"
date: 2026-03-02 00:00:00 -0700
categories: [leetcode, medium, greedy, counting]
tags: [leetcode, medium, array, greedy, counting, scheduling]
permalink: /2026/03/02/medium-621-task-scheduler/
---

# [Medium] 621. Task Scheduler

## Problem Statement

You are given a list of tasks represented by capital letters `A`–`Z`. Each task takes **1 unit of time** to execute. There is a **cooling interval** `n` such that the **same task** must be separated by at least `n` units of time.

You may insert **idle slots** to respect the cooling interval. Return the **minimum number of time units** the CPU will take to finish all the tasks.

## Examples

**Example 1:**

```python
Input:  tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation:
One optimal schedule is: A B idle A B idle A B
Total time units = 8.
```

**Example 2:**

```python
Input:  tasks = ["A","C","A","B","D","B"], n = 1
Output: 6
Explanation:
We can schedule without idle: A B A B C D (or similar).
```

## Constraints

- `1 <= tasks.length <= 10^4`
- `tasks[i]` is an uppercase English letter `'A'` to `'Z'`
- `0 <= n <= 100`

## Clarification Questions

1. **Task duration**: Each task always takes exactly 1 unit time? (Assumption: Yes.)  
2. **Reordering**: Can we execute tasks in any order as long as the cooling rule is respected? (Assumption: Yes.)  
3. **Idle slots**: Are idle slots allowed and do they count as 1 unit of time? (Assumption: Yes.)  
4. **Cooling constraint**: Cooling interval applies **only between identical tasks**, not between different tasks? (Assumption: Yes.)  
5. **Objective**: We want the **minimum total time** units, not the actual schedule? (Assumption: Yes.)  

## Interview Deduction Process (20 minutes)

**Step 1: Naive simulation (5 min)**  
Try to simulate with a max-heap: always pick the most frequent remaining task that is not in cooldown. This works but is more complex and slower to reason about.

**Step 2: Frequency viewpoint (7 min)**  
The schedule is dominated by the **most frequent tasks**. Think in terms of:
- `maxFreq`: the highest frequency of any task
- `countMax`: how many tasks have this frequency

Instead of simulating, build a **frame** using the most frequent tasks and then see how other tasks fill the gaps.

**Step 3: Derive a formula (8 min)**  
Arrange the most frequent tasks in rows:

```text
AAAA...A   (maxFreq times)
```

Turn this into blocks:

- Number of blocks between them: `maxFreq - 1`
- Each block length: `n + 1` (task + n cooldown slots)

This yields a required frame length:

```text
(maxFreq - 1) * (n + 1) + countMax
```

Finally, the true answer is:

```text
max(len(tasks), (maxFreq - 1) * (n + 1) + countMax)
```

Because we can never do better than just executing each task once (no idle), but we may be forced to insert idle time to respect cooling.

## Solution Approach

We **count how many times each task appears**, then plug into the formula.

1. Use `Counter(tasks)` to get frequencies.  
2. Compute:
   - `maxFreq = max(freq.values())`
   - `countMax = number of tasks whose frequency is maxFreq`
3. Compute:
   - `frame = (maxFreq - 1) * (n + 1) + countMax`
4. Answer is `max(len(tasks), frame)`.

### Key Insights

1. **Most frequent task dominates**  
   If a task appears very often, it forces gaps around its occurrences. This gives a natural block structure.

2. **Block structure**  
   We create `maxFreq - 1` full blocks of length `n + 1` (task + `n` cooldown), and then place the last set of max-frequency tasks at the end.

3. **Multiple max-frequency tasks**  
   If there are `countMax` tasks that all have `maxFreq` occurrences, they share the last block, so we add `countMax` at the end instead of just 1.

4. **No-idle scenario**  
   If other tasks are numerous enough to fill all gaps, the schedule length is simply `len(tasks)`; hence the `max(...)` in the final formula.

## Python Solution

```python
from collections import Counter
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)

        maxFreq = max(freq.values())
        countMax = list(freq.values()).count(maxFreq)

        frame = (maxFreq - 1) * (n + 1) + countMax
        return max(len(tasks), frame)
```

## Algorithm Explanation

- Count how many times each letter appears.  
- Consider the letter(s) with maximum count:
  - There are `maxFreq` occurrences of such tasks.
  - We separate them into `maxFreq - 1` groups; between each pair we must have at least `n` other slots to respect cooldown.
- Each group contributes `(n + 1)` to the frame (task + `n` cooldown).
- The final group adds `countMax` tasks (all tasks with that highest frequency).
- If other tasks do **not** fully fill the gaps, we need idle slots and the frame length dominates.
- If other tasks are enough, the schedule collapses to just `len(tasks)` time units.

## Example Walkthrough

Given:

```python
tasks = ["A","A","A","B","B","B"]
n = 2
```

- Frequencies: `A: 3`, `B: 3`  
  `maxFreq = 3`, `countMax = 2`
- Frame:

```text
(maxFreq - 1) * (n + 1) + countMax
= (3 - 1) * (2 + 1) + 2
= 2 * 3 + 2
= 8
```

`len(tasks) = 6`, so answer is `max(6, 8) = 8`.

A valid schedule:

```text
A B idle A B idle A B
```

## Complexity Analysis

- **Time Complexity**: \(O(N)\), where \(N = \text{len}(tasks)\), since we count frequencies and scan the map.
- **Space Complexity**: \(O(1)\) extra, because there are at most 26 distinct tasks.

## Edge Cases

- `n = 0` — no cooling: answer is simply `len(tasks)`; the formula still works.
- All tasks are unique (e.g. `["A","B","C"]`) — no cooling conflicts; answer `= len(tasks)`.
- Only one type of task (e.g. `["A","A","A"]`, `n > 0`) — we must insert idle slots between every pair.
- Large `n` with few task types — large gaps, frame often dominates.

## Common Mistakes

- **Simulating with a priority queue** when a counting + formula approach is simpler and faster.
- Forgetting that **multiple tasks** can share the same maximum frequency (`countMax`).
- Off-by-one errors in `(maxFreq - 1)` or `(n + 1)` when building the frame.
- Forgetting to take the final `max(len(tasks), frame)` and returning only the frame length.

## Related Problems

- [LC 358: Rearrange String k Distance Apart](https://leetcode.com/problems/rearrange-string-k-distance-apart/) — Similar spacing constraint, often implemented with a heap.
- [LC 767: Reorganize String](https://leetcode.com/problems/reorganize-string/) — Rearranging to avoid adjacent equal characters.

