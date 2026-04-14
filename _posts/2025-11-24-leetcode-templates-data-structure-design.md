---
layout: post
title: "Algorithm Templates: Data Structure Design"
date: 2025-11-24 00:00:00 -0700
categories: leetcode templates design
permalink: /posts/2025-11-24-leetcode-templates-data-structure-design/
tags: [leetcode, templates, design, data-structures]
---

{% raw %}
Minimal, copy-paste Python for LRU/LFU cache, Trie, time-based key-value store, and common design patterns.

## Contents

- [Stack-based Design](#stack-based-design)
- [LRU Cache](#lru-cache)
- [LFU Cache](#lfu-cache)
- [Trie](#trie)
- [Time-based Key-Value Store](#time-based-key-value-store)
- [Hit counter (time window)](#hit-counter-time-window)
- [Design Patterns](#design-patterns)

## Stack-based Design

### Min Stack
Maintain a primary stack for data and an auxiliary stack to track the minimum value at each state.

```python
class MinStack:
    def __init__(self) -> None:
        self.stk: list[int] = []
        self.min_stk: list[int] = []

    def push(self, val: int) -> None:
        self.stk.append(val)
        if not self.min_stk:
            self.min_stk.append(val)
        else:
            self.min_stk.append(min(self.min_stk[-1], val))

    def pop(self) -> None:
        self.stk.pop()
        self.min_stk.pop()

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return self.min_stk[-1]

```

| ID | Title | Link | Solution |
|---|---|---|---|
| 155 | Min Stack | [Link](https://leetcode.com/problems/min-stack/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/02/11/medium-155-min-stack/) |

## LRU Cache

Least Recently Used cache using hash map + doubly linked list.

```python
from collections import OrderedDict


class LRUCache:
    """LRU via OrderedDict (move_to_end on access)."""

    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.cache: OrderedDict[int, int] = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

```

### Thread-Safe LRU Cache

Thread-safe version using mutex for concurrent access.

```python
import threading
from collections import OrderedDict


class ThreadSafeLRUCache:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.cache: OrderedDict[int, int] = OrderedDict()
        self._lock = threading.Lock()

    def get(self, key: int) -> int:
        with self._lock:
            if key not in self.cache:
                return -1
            self.cache.move_to_end(key)
            return self.cache[key]

    def put(self, key: int, value: int) -> None:
        with self._lock:
            if key in self.cache:
                self.cache[key] = value
                self.cache.move_to_end(key)
                return
            self.cache[key] = value
            if len(self.cache) > self.capacity:
                self.cache.popitem(last=False)

    def size(self) -> int:
        with self._lock:
            return len(self.cache)

```

| ID | Title | Link | Solution |
|---|---|---|---|
| 146 | LRU Cache | [Link](https://leetcode.com/problems/lru-cache/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-11-14-medium-146-lru-cache/) |

## LFU Cache

Least Frequently Used cache.

```python
from collections import defaultdict, OrderedDict


class LFUCache:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.min_freq = 0
        self.key_val: dict[int, int] = {}
        self.key_freq: dict[int, int] = {}
        self.freq_keys: dict[int, OrderedDict[int, None]] = defaultdict(OrderedDict)

    def _touch(self, key: int) -> None:
        f = self.key_freq[key]
        self.freq_keys[f].pop(key)
        if not self.freq_keys[f] and f == self.min_freq:
            self.min_freq += 1
        f += 1
        self.key_freq[key] = f
        self.freq_keys[f][key] = None

    def get(self, key: int) -> int:
        if key not in self.key_val:
            return -1
        self._touch(key)
        return self.key_val[key]

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        if key in self.key_val:
            self.key_val[key] = value
            self._touch(key)
            return
        if len(self.key_val) >= self.capacity:
            k, _ = self.freq_keys[self.min_freq].popitem(last=False)
            del self.key_val[k]
            del self.key_freq[k]
        self.key_val[key] = value
        self.key_freq[key] = 1
        self.freq_keys[1][key] = None
        self.min_freq = 1

```

| ID | Title | Link | Solution |
|---|---|---|---|
| 460 | LFU Cache | [Link](https://leetcode.com/problems/lfu-cache/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-11-14-hard-460-lfu-cache/) |

## Trie

Prefix tree for efficient string operations.

```python
class TrieNode:
    def __init__(self) -> None:
        self.children: dict[str, TrieNode] = {}
        self.is_end = False


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_end = True

    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        return node.is_end

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for c in prefix:
            if c not in node.children:
                return False
            node = node.children[c]
        return True

```

| ID | Title | Link | Solution |
|---|---|---|---|
| 208 | Implement Trie (Prefix Tree) | [Link](https://leetcode.com/problems/implement-trie-prefix-tree/) | - |
| 211 | Design Add and Search Words Data Structure | [Link](https://leetcode.com/problems/design-add-and-search-words-data-structure/) | - |

## Time-based Key-Value Store

```python
import bisect
from collections import defaultdict


class TimeMap:
    def __init__(self) -> None:
        self.store: dict[str, list[tuple[int, str]]] = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        pairs = self.store.get(key)
        if not pairs:
            return ""
        i = bisect.bisect_right(pairs, (timestamp, chr(0x10FFFF))) - 1
        if i < 0:
            return ""
        return pairs[i][1]

```

| ID | Title | Link | Solution |
|---|---|---|---|
| 981 | Time Based Key-Value Store | [Link](https://leetcode.com/problems/time-based-key-value-store/) | - |

## Hit counter (time window)

Rolling window of timestamps: deque of hits, binary search on sorted times, or bucket counts per second — see blog for tradeoffs.

| ID | Title | Link | Solution |
|---|---|---|---|
| 362 | Design Hit Counter | [Link](https://leetcode.com/problems/design-hit-counter/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2026/03/19/medium-362-design-hit-counter/) |

## Design Patterns

### Random Pick with Weight

```python
import bisect
import random


class Solution:
    def __init__(self, w: list[int]) -> None:
        self.prefix: list[int] = []
        s = 0
        for x in w:
            s += x
            self.prefix.append(s)

    def pickIndex(self) -> int:
        t = random.randint(1, self.prefix[-1])
        return bisect.bisect_left(self.prefix, t)

```

### Design Tic-Tac-Toe

```python
class TicTacToe:
    def __init__(self, n: int) -> None:
        self.n = n
        self.rows = [0] * n
        self.cols = [0] * n
        self.diag = 0
        self.anti = 0

    def move(self, row: int, col: int, player: int) -> int:
        add = 1 if player == 1 else -1
        self.rows[row] += add
        self.cols[col] += add
        if row == col:
            self.diag += add
        if row + col == self.n - 1:
            self.anti += add
        n = self.n
        if (
            abs(self.rows[row]) == n
            or abs(self.cols[col]) == n
            or abs(self.diag) == n
            or abs(self.anti) == n
        ):
            return player
        return 0

```

| ID | Title | Link | Solution |
|---|---|---|---|
| 528 | Random Pick with Weight | [Link](https://leetcode.com/problems/random-pick-with-weight/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-11-24-medium-528-random-pick-with-weight/) |
| 348 | Design Tic-Tac-Toe | [Link](https://leetcode.com/problems/design-tic-tac-toe/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-10-21-medium-348-design-tic-tac-toe/) |
| 398 | Random Pick Index | [Link](https://leetcode.com/problems/random-pick-index/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-11-24-medium-398-random-pick-index/) |
| 2043 | Simple Bank System | [Link](https://leetcode.com/problems/simple-bank-system/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/10/20/medium-2043-simple-bank-system/) |
| 281 | Zigzag Iterator | [Link](https://leetcode.com/problems/zigzag-iterator/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-12-10-medium-281-zigzag-iterator/) |
| 1206 | Design Skiplist | [Link](https://leetcode.com/problems/design-skiplist/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-12-03-hard-1206-design-skiplist/) |

## More templates

- **Data structures (Trie, segment tree):** [Data Structures & Core Algorithms](/posts/2025-10-29-leetcode-templates-data-structures/)
- **Master index:** [Categories & Templates](/posts/2025-10-29-leetcode-categories-and-templates/)
{% endraw %}

