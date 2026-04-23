---
layout: post
title: "[Medium] 1962. Remove Stones to Minimize the Total"
date: 2026-04-22 00:00:00 -0700
categories: [leetcode, medium, array, greedy, heap]
permalink: /2026/04/22/medium-1962-remove-stones-to-minimize-the-total/
tags: [leetcode, medium, greedy, max-heap, priority-queue, simulation]
---

# [Medium] 1962. Remove Stones to Minimize the Total

You are given an array `piles`, where `piles[i]` is the number of stones in pile `i`, and an integer `k`.

Repeat exactly `k` times:

- pick one pile,
- remove `floor(pile / 2)` stones from it.

Return the minimum possible total stones left.

## Problem essence

To minimize the final sum, each operation should remove as many stones as possible **right now**.  
Removing `floor(x / 2)` is larger for larger `x`, so the greedy move is:

- always operate on the **current largest pile**.

This is the classic pattern: **repeat k times + choose best candidate each step** -> use a max heap.

## Data structure

Python `heapq` is a min-heap, so use negatives to simulate a max-heap.

## Python (clean style)

```python
import heapq
from typing import List


class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = [-x for x in piles]  # max-heap via negatives
        heapq.heapify(heap)

        for _ in range(k):
            largest = -heapq.heappop(heap)
            reduced = largest - largest // 2
            heapq.heappush(heap, -reduced)

        return -sum(heap)
```

## Why greedy is optimal

- Reduction per move is `floor(pile / 2)`, which is monotonic in `pile`.
- Choosing a smaller pile can never remove more stones than choosing a larger pile at that step.
- So every step has a dominant best local choice: current maximum.

## Complexity

- Heap build: `O(n)`
- Each of `k` operations: pop + push = `O(log n)`
- Total: `O(n + k log n)`
- Space: `O(n)`

## Pattern recognition

Same bucket as:

- repeatedly take max/min and update,
- priority-queue greedy,
- scheduling / resource reduction with dynamic best choice.
