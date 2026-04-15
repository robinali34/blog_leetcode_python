---
layout: post
title: "[Medium] 2365. Task Scheduler II"
date: 2026-04-10 00:00:00 -0700
categories: [leetcode, medium, array, simulation, hash-table]
tags: [leetcode, medium, simulation, greedy]
permalink: /2026/04/10/medium-2365-task-scheduler-ii/
---

# [Medium] 2365. Task Scheduler II

## Problem Statement

You are given a **0-indexed** array `tasks` of positive integers representing task **types** you must complete **in order**. You also have an integer `space` such that after completing a task of type `x`, you must wait at least `space` full days before doing another task of type `x` (same type).

Each day you may complete **at most one** task. Return the **minimum** day number on which you finish the last task (days are numbered from `1`).

## Examples

**Example 1:**

```python
Input: tasks = [1,2,1,2,3,2], space = 3
Output: 9
```

**Example 2:**

```python
Input: tasks = [5,8,8,5], space = 2
Output: 6
```

## Constraints

- `1 <= tasks.length <= 10^5`
- `1 <= tasks[i] <= 10^9`
- `1 <= space <= 10^9`

## Analysis

Simulate the current day `day`. For each task in order:

- First time seeing a type → do it the next calendar step: `day += 1`.
- If seen before, the same type cannot be run until day `> last_seen[t] + space`.  
  If `day - last_seen[t] <= space`, jump to `last_seen[t] + space + 1`.  
  Otherwise `day += 1`.
- Record `last_seen[t] = day` when the task completes.

Return `day` after the last task.

## Python Solution

```python
from typing import List


class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        last_seen = {}
        day = 0
        for t in tasks:
            if t not in last_seen:
                day += 1
            else:
                if day - last_seen[t] <= space:
                    day = last_seen[t] + space + 1
                else:
                    day += 1
            last_seen[t] = day
        return day
```

## Complexity

- **Time:** O(n) for `n = len(tasks)`
- **Space:** O(u) where `u` is the number of distinct task types

## Common Mistakes

- Off-by-one on the gap: need **more than** `space` days between completions, i.e. next allowed day is `last + space + 1` when you must wait.
- Thinking you can reorder tasks (you cannot — follow `tasks` order).

## Related Problems

- [LC 621: Task Scheduler](https://leetcode.com/problems/task-scheduler/)
- [LC 309: Best Time to Buy and Sell Stock with Cooldown](/2026/03/20/medium-309-best-time-to-buy-and-sell-stock-with-cooldown/) — cooldown between actions
