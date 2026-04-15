---
layout: post
title: "[Medium] 134. Gas Station"
date: 2026-03-22 00:00:00 -0700
categories: [leetcode, medium, greedy, array]
tags: [leetcode, medium, greedy, prefix-sum]
permalink: /2026/03/22/medium-134-gas-station/
---

# [Medium] 134. Gas Station

## Problem Statement

There are `n` gas stations in a circle, where the amount of gas at station `i` is `gas[i]`.

You have a car with an unlimited gas tank and it costs `cost[i]` gas to travel from station `i` to station `i + 1` (wrapping around).

Return the starting gas station index if you can travel around the circuit once in the clockwise direction, otherwise return `-1`.

If a solution exists, it is guaranteed to be unique.

## Examples

**Example 1:**

```python
Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
Output: 3
```

**Example 2:**

```python
Input: gas = [2,3,4], cost = [3,4,3]
Output: -1
```

## Constraints

- `n == gas.length == cost.length`
- `1 <= n <= 10^5`
- `0 <= gas[i], cost[i] <= 10^4`

## Interview Deduction Process (Greedy)

Let `gain[i] = gas[i] - cost[i]`.

1. If total gain over all stations is negative, completing the circuit is impossible.
2. While scanning left to right, keep a running `curr_gain`.
3. If `curr_gain` drops below 0 at index `i`, then any start in the current segment cannot reach `i + 1`, so reset start to `i + 1` and reset `curr_gain = 0`.

This gives an O(n) greedy solution.

## Why Resetting Start Works

Suppose we started at `start` and first failed at `i` (`curr_gain < 0`).

Then for any `k` in `[start, i]`, starting at `k` is also impossible: from `start` to `k - 1`, we had non-negative partial sums before failure, so removing that prefix cannot turn failure into success by `i + 1`.

Therefore, we can safely jump to `i + 1`.

## Python Solution

```python
from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gain = 0
        curr_gain = 0
        rtn = 0
        for i in range(len(gas)):
            total_gain += gas[i] - cost[i]
            curr_gain += gas[i] - cost[i]

            if curr_gain < 0:
                curr_gain = 0
                rtn = i + 1
        return rtn if total_gain >= 0 else -1
```

## Complexity Analysis

- **Time:** O(n)
- **Space:** O(1)

## Edge Cases

- Single station:
  - `gas[0] >= cost[0]` -> `0`
  - otherwise `-1`
- Total gas equals total cost: still valid if a feasible start exists (unique by problem guarantee).
- Many zeros: handled naturally by gain accumulation.

## Common Mistakes

- Forgetting the global feasibility check (`total_gain >= 0`).
- Trying all starting indices (O(n^2)).
- Resetting start incorrectly (must be `i + 1` after failure at `i`).

## Related Problems

- [LC 55: Jump Game](https://leetcode.com/problems/jump-game/)
- [LC 45: Jump Game II](https://leetcode.com/problems/jump-game-ii/)
- [LC 621: Task Scheduler](https://leetcode.com/problems/task-scheduler/)
