---
layout: post
title: "Algorithm Templates: Data Structure Design"
date: 2025-11-24 00:00:00 -0700
categories: leetcode templates design
permalink: /posts/2025-11-24-leetcode-templates-data-structure-design/
tags: [leetcode, templates, design, data-structures]
---

{% raw %}
Data structure design problems are among the most popular interview questions at top tech companies. This page provides complete, tested C++ implementations for LRU/LFU cache, Trie, time-based key-value store, and other classic design patterns. The key insight for most of these problems is combining two or more simple structures to achieve the required time complexity.

> **Design problems test your ability to compose data structures.** The trick is almost always combining a hash map with another structure (linked list, heap, array) to get O(1) for multiple operations.

<svg viewBox="0 0 720 200" xmlns="http://www.w3.org/2000/svg" style="max-width: 100%; height: auto; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;">
  <text x="360" y="18" font-size="12" fill="#5A5752" font-weight="700" text-anchor="middle">LRU Cache — hash map + doubly linked list</text>
  <rect x="30" y="40" width="200" height="120" rx="8" fill="#FAF8F5" stroke="#D4D1CC"/>
  <text x="130" y="58" font-size="11" fill="#5A5752" font-weight="600" text-anchor="middle">Hash Map</text>
  <text x="50" y="80" font-size="10" fill="#5A5752">key=1 → node₁</text>
  <text x="50" y="98" font-size="10" fill="#5A5752">key=2 → node₂</text>
  <text x="50" y="116" font-size="10" fill="#5A5752">key=3 → node₃</text>
  <text x="130" y="145" font-size="9" fill="#9A9792" text-anchor="middle">O(1) lookup by key</text>
  <text x="400" y="35" font-size="10" fill="#9A9792">head (oldest)</text>
  <rect x="280" y="45" width="70" height="32" rx="4" fill="#F0EBE6" stroke="#B8B5B0"/><text x="315" y="64" font-size="12" fill="#9A9792" text-anchor="middle">1</text>
  <line x1="350" y1="61" x2="380" y2="61" stroke="#B8B5B0" marker-end="url(#lru-arr)"/>
  <rect x="380" y="45" width="70" height="32" rx="4" fill="#D4D8D0" stroke="#6B8B6B" stroke-width="2"/><text x="415" y="64" font-size="12" fill="#5A5752" font-weight="700" text-anchor="middle">2</text>
  <line x1="450" y1="61" x2="480" y2="61" stroke="#B8B5B0"/>
  <rect x="480" y="45" width="70" height="32" rx="4" fill="#E8D5D0" stroke="#C08070" stroke-width="2"/><text x="515" y="64" font-size="12" fill="#5A5752" font-weight="700" text-anchor="middle">3</text>
  <text x="560" y="35" font-size="10" fill="#C08070" font-weight="600">tail (recent)</text>
  <defs><marker id="lru-arr" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto"><polygon points="0 0, 8 3, 0 6" fill="#B8B5B0"/></marker></defs>
  <text x="400" y="100" font-size="10" fill="#5A5752" text-anchor="middle">Doubly linked list — O(1) insert/remove at any position</text>
  <text x="400" y="130" font-size="10" fill="#5A5752" text-anchor="middle">get(3): map lookup → splice node to tail (mark recent)</text>
  <text x="400" y="152" font-size="10" fill="#5A5752" text-anchor="middle">put(4): if full → evict head (oldest), insert at tail</text>
  <text x="400" y="180" font-size="10" fill="#3A6B3A" font-weight="600" text-anchor="middle">Both get and put are O(1)</text>
</svg>

- **Beginner's Guide:** [LeetCode Beginner's Guide](/2026/06/25/leetcode-beginners-guide/)

## Contents

- [Stack-based Design](#stack-based-design)
- [LRU Cache](#lru-cache)
- [LFU Cache](#lfu-cache)
- [Trie](#trie)
- [Time-based Key-Value Store](#time-based-key-value-store)
- [Design Patterns](#design-patterns)

## Stack-based Design

**When to use:** "get min/max in O(1)", "design a stack with extra operations", or when you need to track additional state alongside the primary data.

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
| 155 | Min Stack | [Link](https://leetcode.com/problems/min-stack/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2026/02/11/medium-155-min-stack/) |

## LRU Cache

**When to use:** "least recently used", "design a cache with O(1) get and put", or any eviction policy based on access recency.

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
| 146 | LRU Cache | [Link](https://leetcode.com/problems/lru-cache/) | [Solution](https://robinali34.github.io/blog_leetcode_python/posts/2025-11-14-medium-146-lru-cache/) |

## LFU Cache

**When to use:** "least frequently used", "evict the element used fewest times", or cache designs where frequency matters more than recency.

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
| 460 | LFU Cache | [Link](https://leetcode.com/problems/lfu-cache/) | [Solution](https://robinali34.github.io/blog_leetcode_python/posts/2025-11-14-hard-460-lfu-cache/) |

## Trie

**When to use:** "prefix search", "autocomplete", "word dictionary with wildcards", or any problem requiring efficient prefix lookups over a set of strings.

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

**When to use:** "get value at timestamp", "versioned storage", or when you need to retrieve the most recent value at or before a given time.

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
| 362 | Design Hit Counter | [Link](https://leetcode.com/problems/design-hit-counter/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2026/03/18/medium-362-design-hit-counter/) |
| 1146 | Snapshot Array | [Link](https://leetcode.com/problems/snapshot-array/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2026/03/19/medium-1146-snapshot-array/) |

## Design Patterns

**When to use:** "random with weight", "design tic-tac-toe", "iterator", or other custom data structure problems that combine multiple techniques.

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
| 528 | Random Pick with Weight | [Link](https://leetcode.com/problems/random-pick-with-weight/) | [Solution](https://robinali34.github.io/blog_leetcode_python/posts/2025-11-24-medium-528-random-pick-with-weight/) |
| 348 | Design Tic-Tac-Toe | [Link](https://leetcode.com/problems/design-tic-tac-toe/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2026/03/04/medium-348-design-tic-tac-toe/) |
| 1275 | Find Winner on a Tic Tac Toe Game | [Link](https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2026/03/04/easy-1275-find-winner-on-a-tic-tac-toe-game/) |
| 398 | Random Pick Index | [Link](https://leetcode.com/problems/random-pick-index/) | [Solution](https://robinali34.github.io/blog_leetcode_python/posts/2025-11-24-medium-398-random-pick-index/) |
| 2043 | Simple Bank System | [Link](https://leetcode.com/problems/simple-bank-system/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2025/10/20/medium-2043-simple-bank-system/) |
| 281 | Zigzag Iterator | [Link](https://leetcode.com/problems/zigzag-iterator/) | [Solution](https://robinali34.github.io/blog_leetcode_python/posts/2025-12-10-medium-281-zigzag-iterator/) |
| 1206 | Design Skiplist | [Link](https://leetcode.com/problems/design-skiplist/) | [Solution](https://robinali34.github.io/blog_leetcode_python/posts/2025-12-03-hard-1206-design-skiplist/) |
| 341 | Flatten Nested List Iterator | [Link](https://leetcode.com/problems/flatten-nested-list-iterator/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2026/03/24/medium-341-flatten-nested-list-iterator/) |
| 1115 | Print FooBar Alternately | [Link](https://leetcode.com/problems/print-foobar-alternately/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2026/03/28/medium-1115-print-foobar-alternately/) |
| 1188 | Design Bounded Blocking Queue | [Link](https://leetcode.com/problems/design-bounded-blocking-queue/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2026/03/29/medium-1188-design-bounded-blocking-queue/) |

## Summary

| Pattern | Signal Phrases | Structures Used |
|---|---|---|
| Min Stack | "min in O(1)" | Two stacks |
| LRU Cache | "least recently used" | Hash map + doubly linked list |
| LFU Cache | "least frequently used" | Hash map + frequency buckets |
| Trie | "prefix search", "autocomplete" | Tree of character nodes |
| Time-based KV | "get value at timestamp" | Hash map + binary search |

## More templates

- **Data structures (Trie, segment tree):** [Data Structures & Core Algorithms](/posts/2025-10-29-leetcode-templates-data-structures/)
- **Master index:** [Categories & Templates](/posts/2025-10-29-leetcode-categories-and-templates/)
{% endraw %}
