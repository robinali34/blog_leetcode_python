---
layout: post
title: "[Medium] 1115. Print FooBar Alternately"
date: 2026-03-28 00:00:00 -0700
categories: [leetcode, medium, concurrency, threading]
tags: [leetcode, medium, threading, semaphore, condition-variable]
permalink: /2026/03/28/medium-1115-print-foobar-alternately/
---

# [Medium] 1115. Print FooBar Alternately

## Problem Statement

Two threads are given:

- one calls `foo()` repeatedly
- one calls `bar()` repeatedly

The same `FooBar` instance will be passed to both threads. For a given integer `n`, each method is called `n` times. You must synchronize them so the output is `n` repetitions of `"foobar"` in order (interleaved as `foo` then `bar` each time).

## Examples

Conceptually, for `n = 2` the print order is: `foo`, `bar`, `foo`, `bar`.

## Constraints

- `1 <= n <= 1000`

## Clarification Questions

1. **Can `foo` and `bar` run on different threads?** Yes — assume concurrent calls; you must enforce ordering.
2. **How many times does each method run?** Exactly `n` times each.
3. **First print?** `foo` must happen before the first `bar`.

## Analysis Process

You need a **handshake**: after each `foo`, allow one `bar`; after each `bar`, allow the next `foo`.

Common patterns:

- **Two semaphores:** one “permission” for `foo`, one for `bar`; initial counts encode who starts.
- **Condition + boolean turn:** threads wait until it is their turn, then flip turn and `notify_all()`.

Both are standard for strict alternation.

## Solution Options

### Option 1: Two semaphores

`foo` starts with permission (`foo_sem = 1`), `bar` blocks until `foo` releases `bar_sem`.

```python
import threading
from typing import Callable


class FooBar:
    def __init__(self, n: int):
        self.n = n
        self.foo_sem = threading.Semaphore(1)
        self.bar_sem = threading.Semaphore(0)

    def foo(self, printFoo: Callable[[], None]) -> None:
        for _ in range(self.n):
            self.foo_sem.acquire()
            printFoo()
            self.bar_sem.release()

    def bar(self, printBar: Callable[[], None]) -> None:
        for _ in range(self.n):
            self.bar_sem.acquire()
            printBar()
            self.foo_sem.release()
```

### Option 2: `threading.Condition` + turn flag

```python
import threading
from typing import Callable


class FooBar:
    def __init__(self, n: int):
        self.n = n
        self.cv = threading.Condition()
        self.foo_turn = True

    def foo(self, printFoo: Callable[[], None]) -> None:
        for _ in range(self.n):
            with self.cv:
                while not self.foo_turn:
                    self.cv.wait()
                printFoo()
                self.foo_turn = False
                self.cv.notify_all()

    def bar(self, printBar: Callable[[], None]) -> None:
        for _ in range(self.n):
            with self.cv:
                while self.foo_turn:
                    self.cv.wait()
                printBar()
                self.foo_turn = True
                self.cv.notify_all()
```

## Comparison

| Approach | Mechanism | Pros | Cons |
|----------|------------|------|------|
| Semaphores | explicit permits per phase | Very small code, clear “who may go” | Must get initial counts right |
| Condition + flag | wait on shared boolean | Familiar mutex/cond pattern | Easy to get `wait` condition wrong |

## Complexity

Per printed pair: **O(1)** synchronization work; overall **O(n)** calls each to `foo`/`bar`. Extra space is **O(1)** for semaphores/condition state.

## Common Mistakes

- Wrong initial semaphore values (who is allowed to run first).
- Using `if` instead of `while` around `wait()` (must recheck after wakeup).
- Forgetting `notify_all()` (or `notify()`) after flipping state so the other thread can proceed.
- Deadlock from acquiring the same lock twice on the same thread (not an issue with semaphores as written; with `Lock` + `Condition`, only hold `Condition`’s lock inside `with self.cv`).

## Related Problems

- [LC 1114: Print in Order](https://leetcode.com/problems/print-in-order/)
- [LC 1195: Fizz Buzz Multithreaded](https://leetcode.com/problems/fizz-buzz-multithreaded/)
