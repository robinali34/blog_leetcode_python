---
layout: post
title: "1188. Design Bounded Blocking Queue"
date: 2026-03-29 00:00:00 -0700
categories: [leetcode, medium, concurrency, design]
tags: [leetcode, medium, threading, semaphore, queue]
permalink: /2026/03/29/medium-1188-design-bounded-blocking-queue/
---

# 1188. Design Bounded Blocking Queue

## Problem Statement

Implement a thread-safe bounded blocking queue with:

- `BoundedBlockingQueue(capacity)` — fixed capacity
- `enqueue(element)` — block until there is space, then add
- `dequeue()` — block until non-empty, then remove and return front
- `size()` — current number of elements (LeetCode tests often call this from a single inspector thread; see notes below)

## Clarification Questions

1. **What should `enqueue` do when the queue is full?** Block until `dequeue` frees a slot.
2. **What should `dequeue` do when empty?** Block until something is enqueued.
3. **Fairness?** Not required; any valid interleaving that respects blocking is fine.

## Analysis Process

Treat capacity as **two counts**:

- **Empty slots:** start at `capacity`; `enqueue` must take one before storing.
- **Filled slots:** start at `0`; `dequeue` must take one before removing.

`threading.Semaphore` gives exactly that: `acquire()` blocks at `0`, `release()` increments.

Pair with a `collections.deque` for FIFO storage.

## Python Solution (Semaphores + deque)

```python
from collections import deque
from threading import Semaphore


class BoundedBlockingQueue:
    def __init__(self, capacity: int):
        self.emptySlots = Semaphore(capacity)
        self.filledSlots = Semaphore(0)
        self.queue = deque()

    def enqueue(self, element: int) -> None:
        self.emptySlots.acquire()
        self.queue.append(element)
        self.filledSlots.release()

    def dequeue(self) -> int:
        self.filledSlots.acquire()
        val = self.queue.popleft()
        self.emptySlots.release()
        return val

    def size(self) -> int:
        return len(self.queue)
```

Order of operations matters: **acquire empty slot before mutating**, **release filled after append**; symmetrically for dequeue.

## Option: Add a `Lock` around the deque

On LeetCode, semaphore-only solutions often pass. For extra clarity in real systems, guard `append` / `popleft` with `threading.Lock` so no queue operation runs concurrently with another (optional here if you keep critical sections minimal).

## Comparison (high level)

| Idea | Blocking | Storage |
|------|----------|---------|
| Two semaphores | `emptySlots` / `filledSlots` | deque (FIFO) |
| `queue.Queue(maxsize=…)` | built-in | Standard library (interview shortcut if allowed) |

## Complexity

Let `n` be capacity.

- **Per successful `enqueue` / `dequeue`:** O(1) amortized for deque ops; blocking time is unbounded (depends on other thread).
- **Extra space:** O(n) for stored elements plus O(1) semaphore state.

## Common Mistakes

- Releasing semaphores in the wrong order (deadlock or capacity violation).
- Forgetting `from collections import deque`.
- Calling `size()` from many threads expecting a strict snapshot — without a lock, `len(self.queue)` can be stale relative to concurrent `enqueue`/`dequeue`; LeetCode often avoids racing on `size()`.

## Related Problems

- [LC 1115: Print FooBar Alternately](/2026/03/28/medium-1115-print-foobar-alternately/)
- [LC 1242: Web Crawler Multithreaded](https://leetcode.com/problems/web-crawler-multithreaded/)
