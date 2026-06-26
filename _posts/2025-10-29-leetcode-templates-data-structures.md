---
layout: post
title: "Algorithm Templates: Data Structures & Core Algorithms"
date: 2025-10-29 00:00:00 -0700
categories: leetcode templates data-structures algorithms
permalink: /posts/2025-10-29-leetcode-templates-data-structures/
tags: [leetcode, templates, data-structures, algorithms]
---

{% raw %}
This page is your toolbox of essential data structures for LeetCode. Each template is self-contained C++ you can copy directly into your solution. They range from beginner-friendly (binary search, prefix sum) to advanced (segment tree, sparse table) — start with what you need and come back for more as you level up.

> **This is the foundation.** These data structures are the building blocks that other templates (DFS, BFS, DP) build on. Master binary search and prefix sums first, then work outward — you'll see them appear inside graph, tree, and dynamic programming solutions.

<svg viewBox="0 0 740 200" xmlns="http://www.w3.org/2000/svg" style="max-width: 100%; height: auto; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;">
  <text x="370" y="22" font-size="13" fill="#5A5752" font-weight="700" text-anchor="middle">Which Data Structure Do I Need?</text>
  <rect x="30" y="40" width="150" height="44" rx="8" fill="#D4D8E0" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="105" y="58" font-size="11" fill="#5A5752" font-weight="600" text-anchor="middle">Sorted + search?</text>
  <text x="105" y="76" font-size="10" fill="#7A7772" text-anchor="middle">→ Binary Search</text>
  <rect x="200" y="40" width="150" height="44" rx="8" fill="#D4D8D0" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="275" y="58" font-size="11" fill="#5A5752" font-weight="600" text-anchor="middle">Range sums?</text>
  <text x="275" y="76" font-size="10" fill="#7A7772" text-anchor="middle">→ Prefix Sum / BIT</text>
  <rect x="370" y="40" width="150" height="44" rx="8" fill="#E8D5D0" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="445" y="58" font-size="11" fill="#5A5752" font-weight="600" text-anchor="middle">Next greater/smaller?</text>
  <text x="445" y="76" font-size="10" fill="#7A7772" text-anchor="middle">→ Monotonic Stack</text>
  <rect x="500" y="40" width="150" height="44" rx="8" fill="#E8E3D8" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="575" y="58" font-size="11" fill="#5A5752" font-weight="600" text-anchor="middle">Top-K / min cost?</text>
  <text x="575" y="76" font-size="10" fill="#7A7772" text-anchor="middle">→ Heap</text>
  <rect x="30" y="110" width="150" height="44" rx="8" fill="#D4D8E0" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="105" y="128" font-size="11" fill="#5A5752" font-weight="600" text-anchor="middle">Connected groups?</text>
  <text x="105" y="146" font-size="10" fill="#7A7772" text-anchor="middle">→ Union-Find (DSU)</text>
  <rect x="200" y="110" width="150" height="44" rx="8" fill="#D4D8D0" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="275" y="128" font-size="11" fill="#5A5752" font-weight="600" text-anchor="middle">Prefix of strings?</text>
  <text x="275" y="146" font-size="10" fill="#7A7772" text-anchor="middle">→ Trie</text>
  <rect x="370" y="110" width="150" height="44" rx="8" fill="#E8D5D0" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="445" y="128" font-size="11" fill="#5A5752" font-weight="600" text-anchor="middle">Range query + update?</text>
  <text x="445" y="146" font-size="10" fill="#7A7772" text-anchor="middle">→ Segment Tree</text>
  <rect x="500" y="110" width="150" height="44" rx="8" fill="#E8E3D8" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="575" y="128" font-size="11" fill="#5A5752" font-weight="600" text-anchor="middle">Static range min/max?</text>
  <text x="575" y="146" font-size="10" fill="#7A7772" text-anchor="middle">→ Sparse Table</text>
  <text x="370" y="185" font-size="10" fill="#9A9792" text-anchor="middle">Start with binary search + prefix sum — they appear inside most other patterns</text>
</svg>

## Contents

- [Binary Search (Bounds)](#binary-search-bounds)
- [Prefix Sum & Difference Array](#prefix-sum--difference-array)
- [Monotonic Stack](#monotonic-stack)
- [Monotonic Queue](#monotonic-queue)
- [Heap / Priority Queue](#heap--priority-queue)
- [Union-Find (DSU)](#union-find-dsu)
- [Trie](#trie)
- [Segment Tree](#segment-tree)
- [Fenwick Tree (BIT)](#fenwick-tree-bit)
- [Sparse Table (Range Min/Max)](#sparse-table-range-minmax)

---

## Binary Search (Bounds)

**When to use:** The input is sorted (or the answer space is monotonic) and you need to find a boundary — first element ≥ x, last element ≤ x, or the minimum/maximum value satisfying a condition.

Half-open range `[lo, hi)`. Use when you need first ≥ x (lower_bound) or first > x (upper_bound).

<svg viewBox="0 0 680 160" xmlns="http://www.w3.org/2000/svg" style="max-width: 100%; height: auto; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;">
  <text x="340" y="18" font-size="12" fill="#5A5752" font-weight="700" text-anchor="middle">Binary Search on [2, 5, 8, 12, 16, 23, 38] — target = 23</text>
  <rect x="80" y="30" width="50" height="32" rx="4" fill="#F0EBE6" stroke="#B8B5B0"/><text x="105" y="51" font-size="12" fill="#5A5752" text-anchor="middle">2</text>
  <rect x="130" y="30" width="50" height="32" rx="4" fill="#F0EBE6" stroke="#B8B5B0"/><text x="155" y="51" font-size="12" fill="#5A5752" text-anchor="middle">5</text>
  <rect x="180" y="30" width="50" height="32" rx="4" fill="#F0EBE6" stroke="#B8B5B0"/><text x="205" y="51" font-size="12" fill="#5A5752" text-anchor="middle">8</text>
  <rect x="230" y="30" width="50" height="32" rx="4" fill="#F0EBE6" stroke="#B8B5B0"/><text x="255" y="51" font-size="12" fill="#5A5752" text-anchor="middle">12</text>
  <rect x="280" y="30" width="50" height="32" rx="4" fill="#F0EBE6" stroke="#B8B5B0"/><text x="305" y="51" font-size="12" fill="#5A5752" text-anchor="middle">16</text>
  <rect x="330" y="30" width="50" height="32" rx="4" fill="#E8D5D0" stroke="#C08070" stroke-width="2"/><text x="355" y="51" font-size="12" fill="#5A5752" font-weight="700" text-anchor="middle">23</text>
  <rect x="380" y="30" width="50" height="32" rx="4" fill="#F0EBE6" stroke="#B8B5B0"/><text x="405" y="51" font-size="12" fill="#5A5752" text-anchor="middle">38</text>
  <text x="105" y="78" font-size="10" fill="#7080A0" font-weight="600">lo</text>
  <text x="355" y="78" font-size="10" fill="#C08070" font-weight="600">mid ✓</text>
  <text x="405" y="78" font-size="10" fill="#7080A0" font-weight="600">hi</text>
  <text x="340" y="110" font-size="10" fill="#5A5752" text-anchor="middle">Step 1: lo=0, hi=6, mid=3 → 12 &lt; 23 → lo=4</text>
  <text x="340" y="128" font-size="10" fill="#5A5752" text-anchor="middle">Step 2: lo=4, hi=6, mid=5 → 23 = target → found!</text>
  <text x="340" y="150" font-size="10" fill="#3A6B3A" font-weight="600" text-anchor="middle">Key: half-open range [lo, hi) — mid never equals hi</text>
</svg>

```python
from typing import List


def next_greater_circular(nums: List[int]) -> List[int]:
    n = len(nums)
    ans = [-1] * n
    st: List[int] = []  # stores indices; values are decreasing in stack

    for i in range(2 * n):
        idx = i % n
        while st and nums[st[-1]] < nums[idx]:
            ans[st.pop()] = nums[idx]
        if i < n:
            st.append(idx)
    return ans
```

| ID | Title | Link |
|----|--------|------|
| 34 | Find First and Last Position | [Link](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/) |
| 35 | Search Insert Position | [Link](https://leetcode.com/problems/search-insert-position/) |
| 875 | Koko Eating Bananas | [Link](https://leetcode.com/problems/koko-eating-bananas/) |

---

## Prefix Sum & Difference Array

**When to use:** You need to answer many "sum of subarray [l, r]" queries, or apply the same increment to many ranges efficiently.

Prefix sum: range sum in O(1). Difference array: range add in O(1), then one prefix sum to recover.

```python
from collections import deque
from typing import List


def max_sliding_window(nums: List[int], k: int) -> List[int]:
    dq = deque()  # stores indices; nums[dq] is decreasing
    out: List[int] = []

    for i, x in enumerate(nums):
        while dq and nums[dq[-1]] <= x:
            dq.pop()
        dq.append(i)

        # Remove indices outside current window [i-k+1, i]
        if dq[0] <= i - k:
            dq.popleft()

        if i >= k - 1:
            out.append(nums[dq[0]])
    return out
```

| ID | Title | Link |
|----|--------|------|
| 560 | Subarray Sum Equals K | [Link](https://leetcode.com/problems/subarray-sum-equals-k/) |
| 1109 | Corporate Flight Bookings | [Link](https://leetcode.com/problems/corporate-flight-bookings/) |
| 1094 | Car Pooling | [Link](https://leetcode.com/problems/car-pooling/) |

---

## Monotonic Stack

**When to use:** You need "next greater element", "next smaller element", "largest rectangle in histogram", or any problem where each element is compared to its neighbors in one direction.

Maintain indices with strictly increasing (or decreasing) values. Use for next greater/smaller, or histogram rectangle.

```python
import heapq
from typing import List


def merge_k_sorted_lists(lists: List[List[int]]) -> List[int]:
    # heap entry: (value, list_index, element_index)
    heap = []
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst[0], i, 0))

    out: List[int] = []
    while heap:
        v, li, ei = heapq.heappop(heap)
        out.append(v)
        ni = ei + 1
        if ni < len(lists[li]):
            heapq.heappush(heap, (lists[li][ni], li, ni))
    return out
```

| ID | Title | Link |
|----|--------|------|
| 739 | Daily Temperatures | [Link](https://leetcode.com/problems/daily-temperatures/) |
| 42 | Trapping Rain Water | [Link](https://leetcode.com/problems/trapping-rain-water/) |
| 84 | Largest Rectangle in Histogram | [Link](https://leetcode.com/problems/largest-rectangle-in-histogram/) |
| 503 | Next Greater Element II | [Link](https://leetcode.com/problems/next-greater-element-ii/) |
| 1944 | Visible People in Queue | [Link](https://leetcode.com/problems/number-of-visible-people-in-a-queue/) |

---

## Monotonic Queue

**When to use:** You need the maximum or minimum within a sliding window of fixed size, or need to maintain a monotonic property as elements enter and leave a window.

Deque of indices with values in monotonic order. Sliding window max/min.

```python
class DSU:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # path compression
        return self.parent[x]

    def union(self, a: int, b: int) -> bool:
        ra = self.find(a)
        rb = self.find(b)
        if ra == rb:
            return False

        # union by rank
        if self.rank[ra] < self.rank[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        if self.rank[ra] == self.rank[rb]:
            self.rank[ra] += 1
        return True
```

| ID | Title | Link |
|----|--------|------|
| 239 | Sliding Window Maximum | [Link](https://leetcode.com/problems/sliding-window-maximum/) |
| 1438 | Longest Continuous Subarray With Abs Diff ≤ Limit | [Link](https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/) |

---

## Heap / Priority Queue

**When to use:** You repeatedly need the smallest (or largest) element — merging k sorted lists, scheduling, median maintenance, or any "top K" problem.

Min-heap: `priority_queue<T, vector<T>, greater<T>>`. K-way merge: push heads, pop min, push next from same list.

```python
class TrieNode:
    def __init__(self):
        self.next = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.next:
                node.next[ch] = TrieNode()
            node = node.next[ch]
        node.is_end = True

    def search(self, word: str) -> bool:
        node = self.root
        for ch in word:
            if ch not in node.next:
                return False
            node = node.next[ch]
        return node.is_end

    def starts_with(self, prefix: str) -> bool:
        node = self.root
        for ch in prefix:
            if ch not in node.next:
                return False
            node = node.next[ch]
        return True
```

| ID | Title | Link |
|----|--------|------|
| 23 | Merge k Sorted Lists | [Link](https://leetcode.com/problems/merge-k-sorted-lists/) |
| 295 | Find Median from Data Stream | [Link](https://leetcode.com/problems/find-median-from-data-stream/) |

---

## Union-Find (DSU)

**When to use:** You need to track connected components, determine if two nodes are in the same group, or merge groups — common in graph connectivity, redundant edge detection, and "accounts merge" problems.

Path compression + rank merge. `find(x)`, `unite(a,b)`.

<svg viewBox="0 0 680 150" xmlns="http://www.w3.org/2000/svg" style="max-width: 100%; height: auto; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;">
  <text x="340" y="18" font-size="12" fill="#5A5752" font-weight="700" text-anchor="middle">Union-Find — unite(1,2), unite(3,4), unite(2,3)</text>
  <circle cx="120" cy="55" r="22" fill="#D4D8E0" stroke="#B8B5B0" stroke-width="2"/><text x="120" y="60" font-size="13" fill="#5A5752" font-weight="700" text-anchor="middle">0</text>
  <circle cx="220" cy="55" r="22" fill="#D4D8D0" stroke="#6B8B6B" stroke-width="2"/><text x="220" y="60" font-size="13" fill="#5A5752" font-weight="700" text-anchor="middle">1</text>
  <circle cx="320" cy="55" r="22" fill="#D4D8D0" stroke="#6B8B6B" stroke-width="2"/><text x="320" y="60" font-size="13" fill="#5A5752" font-weight="700" text-anchor="middle">2</text>
  <circle cx="480" cy="55" r="22" fill="#E8D5D0" stroke="#C08070" stroke-width="2"/><text x="480" y="60" font-size="13" fill="#5A5752" font-weight="700" text-anchor="middle">3</text>
  <circle cx="580" cy="55" r="22" fill="#E8D5D0" stroke="#C08070" stroke-width="2"/><text x="580" y="60" font-size="13" fill="#5A5752" font-weight="700" text-anchor="middle">4</text>
  <line x1="220" y1="55" x2="120" y2="55" stroke="#6B8B6B" stroke-width="2"/>
  <line x1="320" y1="55" x2="220" y2="55" stroke="#6B8B6B" stroke-width="2"/>
  <line x1="580" y1="55" x2="480" y2="55" stroke="#C08070" stroke-width="2"/>
  <text x="220" y="100" font-size="10" fill="#3A6B3A" text-anchor="middle">Group {0,1,2}</text>
  <text x="530" y="100" font-size="10" fill="#C08070" text-anchor="middle">Group {3,4}</text>
  <text x="340" y="130" font-size="10" fill="#5A5752" text-anchor="middle">find(x) returns root with path compression | unite merges two groups</text>
</svg>

```python
from typing import List


class SegmentTreeSum:
    def __init__(self, arr: List[int]):
        self.n = len(arr)
        self.st = [0] * (4 * self.n if self.n else 1)
        if self.n:
            self._build(1, 0, self.n - 1, arr)

    def _build(self, node: int, l: int, r: int, arr: List[int]) -> None:
        if l == r:
            self.st[node] = arr[l]
            return
        m = (l + r) // 2
        self._build(node * 2, l, m, arr)
        self._build(node * 2 + 1, m + 1, r, arr)
        self.st[node] = self.st[node * 2] + self.st[node * 2 + 1]

    def update(self, idx: int, val: int) -> None:
        def dfs(node: int, l: int, r: int) -> None:
            if l == r:
                self.st[node] = val
                return
            m = (l + r) // 2
            if idx <= m:
                dfs(node * 2, l, m)
            else:
                dfs(node * 2 + 1, m + 1, r)
            self.st[node] = self.st[node * 2] + self.st[node * 2 + 1]

        if self.n:
            dfs(1, 0, self.n - 1)

    def query(self, ql: int, qr: int) -> int:
        def dfs(node: int, l: int, r: int) -> int:
            if qr < l or r < ql:
                return 0
            if ql <= l and r <= qr:
                return self.st[node]
            m = (l + r) // 2
            return dfs(node * 2, l, m) + dfs(node * 2 + 1, m + 1, r)

        if not self.n:
            return 0
        return dfs(1, 0, self.n - 1)
```

| ID | Title | Link |
|----|--------|------|
| 684 | Redundant Connection | [Link](https://leetcode.com/problems/redundant-connection/) |
| 721 | Accounts Merge | [Link](https://leetcode.com/problems/accounts-merge/) |
| 1319 | Number of Operations to Make Network Connected | [Link](https://leetcode.com/problems/number-of-operations-to-make-network-connected/) |

---

## Trie

**When to use:** Problems involve prefix matching, autocomplete, word search in a dictionary, or "find all words with prefix X". Also useful for XOR-maximization with a bitwise trie.

Fixed alphabet (e.g. 26). Insert and search in O(|s|).

<svg viewBox="0 0 600 180" xmlns="http://www.w3.org/2000/svg" style="max-width: 100%; height: auto; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;">
  <text x="300" y="18" font-size="12" fill="#5A5752" font-weight="700" text-anchor="middle">Trie for words: "cat", "car", "dog"</text>
  <circle cx="300" cy="45" r="18" fill="#D4D8E0" stroke="#B8B5B0" stroke-width="2"/><text x="300" y="50" font-size="10" fill="#5A5752" text-anchor="middle">root</text>
  <line x1="280" y1="60" x2="200" y2="90" stroke="#B8B5B0"/><line x1="320" y1="60" x2="400" y2="90" stroke="#B8B5B0"/>
  <circle cx="200" cy="100" r="16" fill="#D4D8D0" stroke="#B8B5B0"/><text x="200" y="105" font-size="11" fill="#5A5752" text-anchor="middle">c</text>
  <circle cx="400" cy="100" r="16" fill="#E8D5D0" stroke="#B8B5B0"/><text x="400" y="105" font-size="11" fill="#5A5752" text-anchor="middle">d</text>
  <line x1="185" y1="115" x2="150" y2="140" stroke="#B8B5B0"/><line x1="215" y1="115" x2="250" y2="140" stroke="#B8B5B0"/>
  <circle cx="150" cy="150" r="14" fill="#E8E3D8" stroke="#B8B5B0"/><text x="150" y="155" font-size="10" fill="#5A5752" text-anchor="middle">a</text>
  <circle cx="250" cy="150" r="14" fill="#E8E3D8" stroke="#B8B5B0"/><text x="250" y="155" font-size="10" fill="#5A5752" text-anchor="middle">a</text>
  <line x1="140" y1="162" x2="120" y2="172" stroke="#B8B5B0"/><line x1="160" y1="162" x2="180" y2="172" stroke="#B8B5B0"/>
  <text x="120" y="176" font-size="9" fill="#3A6B3A" text-anchor="middle">t✓</text>
  <text x="180" y="176" font-size="9" fill="#3A6B3A" text-anchor="middle">r✓</text>
  <line x1="400" y1="115" x2="400" y2="150" stroke="#B8B5B0"/>
  <circle cx="400" cy="160" r="14" fill="#E8E3D8" stroke="#B8B5B0"/><text x="400" y="165" font-size="10" fill="#5A5752" text-anchor="middle">o</text>
  <line x1="400" y1="172" x2="400" y2="176" stroke="#B8B5B0"/><text x="400" y="176" font-size="9" fill="#3A6B3A" text-anchor="middle">g✓</text>
  <text x="300" y="176" font-size="9" fill="#9A9792" text-anchor="middle">Shared prefixes share nodes — "cat" and "car" share c→a</text>
</svg>

```python
class Fenwick:
    def __init__(self, n: int):
        self.n = n
        self.bit = [0] * (n + 1)  # 1-indexed

    def add(self, i: int, delta: int) -> None:
        # external i is 0-indexed
        i += 1
        while i <= self.n:
            self.bit[i] += delta
            i += i & -i

    def prefix_sum(self, i: int) -> int:
        # sum of nums[0..i], external i is 0-indexed
        i += 1
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s

    def range_sum(self, l: int, r: int) -> int:
        if l > r:
            return 0
        return self.prefix_sum(r) - (self.prefix_sum(l - 1) if l > 0 else 0)
```

| ID | Title | Link |
|----|--------|------|
| 208 | Implement Trie | [Link](https://leetcode.com/problems/implement-trie-prefix-tree/) |
| 211 | Design Add and Search Words | [Link](https://leetcode.com/problems/design-add-and-search-words-data-structure/) |
| 212 | Word Search II | [Link](https://leetcode.com/problems/word-search-ii/) |

---

## Segment Tree

**When to use:** You need both range queries (sum, min, max) AND point or range updates on the same array. More powerful than Fenwick tree when you need lazy propagation or non-commutative operations.

0-indexed range [0, n-1]. Point update, range sum (or min/max). Recursive implementation.

```python
class SegTree:
    def __init__(self, n: int):
        self.n = n
        self.st = [0] * (4 * n)

    def _upd(self, i: int, l: int, r: int, p: int, v: int) -> None:
        if l == r:
            self.st[i] = v
            return
        m = (l + r) // 2
        if p <= m:
            self._upd(2 * i, l, m, p, v)
        else:
            self._upd(2 * i + 1, m + 1, r, p, v)
        self.st[i] = self.st[2 * i] + self.st[2 * i + 1]

    def _qry(self, i: int, l: int, r: int, ql: int, qr: int) -> int:
        if qr < l or r < ql:
            return 0
        if ql <= l and r <= qr:
            return self.st[i]
        m = (l + r) // 2
        return self._qry(2 * i, l, m, ql, qr) + self._qry(
            2 * i + 1, m + 1, r, ql, qr
        )

    def upd(self, p: int, v: int) -> None:
        self._upd(1, 0, self.n - 1, p, v)

    def qry(self, ql: int, qr: int) -> int:
        return self._qry(1, 0, self.n - 1, ql, qr)
```

| ID | Title | Link |
|----|--------|------|
| 307 | Range Sum Query – Mutable | [Link](https://leetcode.com/problems/range-sum-query-mutable/) |
| 732 | My Calendar III | [Link](https://leetcode.com/problems/my-calendar-iii/) |

---

## Fenwick Tree (BIT)

**When to use:** You need prefix sums with point updates — simpler and faster constant than segment tree when you don't need lazy propagation. Great for counting inversions or "count of smaller numbers after self".

1-indexed. Point add, prefix sum. Range sum [l, r] = sum(r) - sum(l-1).

```python
class BIT:
    def __init__(self, n: int):
        self.n = n
        self.f = [0] * (n + 1)

    def add(self, i: int, v: int) -> None:
        i += 1  # convert 0-indexed to 1-indexed
        while i <= self.n:
            self.f[i] += v
            i += i & -i

    def sum(self, i: int) -> int:
        i += 1  # convert 0-indexed to 1-indexed
        s = 0
        while i > 0:
            s += self.f[i]
            i -= i & -i
        return s

    def range_sum(self, l: int, r: int) -> int:
        return self.sum(r) - self.sum(l - 1)
```

| ID | Title | Link |
|----|--------|------|
| 307 | Range Sum Query – Mutable | [Link](https://leetcode.com/problems/range-sum-query-mutable/) |
| 315 | Count of Smaller Numbers After Self | [Link](https://leetcode.com/problems/count-of-smaller-numbers-after-self/) |
| 308 | Range Sum Query 2D – Mutable | [Link](https://leetcode.com/problems/range-sum-query-2d-mutable/) |

---

## Sparse Table (Range Min/Max)

**When to use:** You need O(1) range min/max/gcd queries with NO updates. Perfect for static arrays where you precompute once and query many times.

O(n log n) build, O(1) range min/max. Idempotent only (min, max, gcd). 0-indexed.

```python
class SparseTable:
    def __init__(self, a: list[int]):
        n = len(a)
        self.lg = [0] * (n + 1)
        for i in range(2, n + 1):
            self.lg[i] = self.lg[i // 2] + 1
        k = self.lg[n] + 1
        self.st = [[0] * k for _ in range(n)]
        for i in range(n):
            self.st[i][0] = a[i]
        for j in range(1, k):
            step = 1 << j
            prev = 1 << (j - 1)
            for i in range(n - step + 1):
                self.st[i][j] = self.op(self.st[i][j - 1], self.st[i + prev][j - 1])

    def op(self, a: int, b: int) -> int:
        return min(a, b)  # or max

    def qry(self, l: int, r: int) -> int:
        j = self.lg[r - l + 1]
        return self.op(self.st[l][j], self.st[r - (1 << j) + 1][j])
```

| ID | Title | Link |
|----|--------|------|
| — | Range min/max, GCD (no update) | — |

---

---

## Quick Reference

| Structure | When to Use | Operations | Time |
|---|---|---|---|
| Binary Search | Sorted data, find boundary | lower/upper bound | O(log n) |
| Prefix Sum | Range sum queries | build + query | O(n) + O(1) |
| Monotonic Stack | Next greater/smaller | push/pop | O(n) |
| DSU | Connected components, union | find/union | O(α(n)) |
| Trie | Prefix search, autocomplete | insert/search | O(L) |
| Segment Tree | Range query + update | build/query/update | O(n) + O(log n) |
| Fenwick Tree | Prefix sums + point update | update/query | O(log n) |

## More Templates

- **Beginner's Guide:** [LeetCode Beginner's Guide](/2026/06/25/leetcode-beginners-guide/)
- **Graph (BFS, Dijkstra, Topo, DSU):** [Graph Templates](/posts/2025-10-29-leetcode-templates-graph/)
- **Binary search (rotated, 2D, answer space):** [Search Templates](/posts/2026-01-20-leetcode-templates-search/)
- **DP, Backtracking, Greedy, Stack:** [Categories & Templates](/posts/2025-10-29-leetcode-categories-and-templates/)
{% endraw %}
