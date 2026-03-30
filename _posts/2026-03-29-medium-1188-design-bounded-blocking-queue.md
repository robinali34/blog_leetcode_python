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

Alternatively, use one **`threading.Condition`**: producers `wait` while full, consumers `wait` while empty, and `notify` / `notify_all` after changing length.

## Solution Option 1: Semaphores + deque

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

## Solution Option 2: `Condition` + `deque`

Same logic as your snippet, with two fixes:

1. **`size()` must not use `while self.cond:`** — a `Condition` is always truthy, so that loop is wrong and would not actually synchronize. Hold the condition’s lock and return `len(self.q)` (same lock as enqueue/dequeue).
2. **`deque`** still needs `from collections import deque`.

```python
import threading
from collections import deque


class BoundedBlockingQueue(object):
    def __init__(self, capacity: int):
        self.q = deque()
        self.capacity = capacity
        self.cond = threading.Condition()

    def enqueue(self, element: int) -> None:
        with self.cond:
            while len(self.q) == self.capacity:
                self.cond.wait()

            self.q.append(element)
            self.cond.notify()

    def dequeue(self) -> int:
        with self.cond:
            while len(self.q) == 0:
                self.cond.wait()

            val = self.q.popleft()
            self.cond.notify()
            return val

    def size(self) -> int:
        with self.cond:
            return len(self.q)
```

With a **single** condition for both “full” and “empty” waiters, some designs use **`notify_all()`** instead of **`notify()`** so every waiter re-checks `len(self.q)` (avoids edge cases where the wrong waiter stays asleep). LeetCode often accepts `notify()`.

## Option: Add a `Lock` around the deque

On LeetCode, semaphore-only solutions often pass. For extra clarity in real systems, guard `append` / `popleft` with `threading.Lock` so no queue operation runs concurrently with another (optional here if you keep critical sections minimal).

## Comparison (high level)

| Idea | Blocking | Storage |
|------|----------|---------|
| Two semaphores | `emptySlots` / `filledSlots` | deque (FIFO) |
| One `Condition` | `wait` while full / empty | deque under same lock |
| `queue.Queue(maxsize=…)` | built-in | Standard library (interview shortcut if allowed) |

## Complexity

Let `n` be capacity.

- **Per successful `enqueue` / `dequeue`:** O(1) amortized for deque ops; blocking time is unbounded (depends on other thread).
- **Extra space:** O(n) for stored elements plus O(1) semaphore state.

## Common Mistakes

- Releasing semaphores in the wrong order (deadlock or capacity violation).
- Forgetting `from collections import deque`.
- Writing `size()` as `while self.cond: return len(self.q)` — wrong control flow and no mutual exclusion; use **`with self.cond:`**.
- Using `if len(self.q) == …` instead of **`while`** after `wait()` — must recheck state after waking.
- Calling `size()` from many threads expecting a strict snapshot — without holding the same lock as `enqueue`/`dequeue`, reads can race; the condition-based `size()` above is consistent when all paths use `with self.cond`.

## Related Problems

- [LC 1115: Print FooBar Alternately](/2026/03/28/medium-1115-print-foobar-alternately/)
- [LC 1242: Web Crawler Multithreaded](https://leetcode.com/problems/web-crawler-multithreaded/)
