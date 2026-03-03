---
layout: post
title: "LeetCode Templates: Data Structures"
date: 2025-10-29 00:00:00 -0700
categories: [leetcode, templates, data-structures]
permalink: /posts/2025-10-29-leetcode-templates-data-structures/
tags: [leetcode, templates, data-structures]
---

## Contents

- [How to Analyze Data Structures](#how-to-analyze-data-structures)
- [Quick Selection Checklist](#quick-selection-checklist)
- [Monotonic Stack](#monotonic-stack-next-greater--histogram)
- [Monotonic Queue](#monotonic-queue-sliding-window-extrema)
- [Heap / K-way Merge](#heap--k-way-merge)
- [Union-Find (DSU)](#union-find-disjoint-set-union)
- [Trie (Prefix Tree)](#trie-prefix-tree)
- [Segment Tree](#segment-tree-range-query--point-update)
- [Fenwick Tree](#fenwick-tree-binary-indexed-tree)

## How to Analyze Data Structures

When choosing a structure in interviews, use this decision frame:

1. **Operation profile**
   - What operations are needed? (insert, delete, query, min/max, prefix/range, connectivity)
   - Which operation dominates total runtime?

2. **Complexity targets**
   - Required time per operation: `O(1)`, `O(log n)`, or `O(n)`?
   - Can preprocessing be expensive if queries are cheap afterward?

3. **Data properties**
   - Sorted vs unsorted, static vs dynamic, unique vs duplicate-heavy
   - Local window constraints vs global graph constraints

4. **Invariant design**
   - Define the exact invariant your structure maintains
   - Example: "Deque indices are decreasing by value" or "Parent pointers form disjoint components"

5. **Memory and constants**
   - Same asymptotic complexity can have very different constants
   - Python-specific overhead matters for large `n`

6. **Failure modes**
   - Off-by-one index bugs
   - Incorrect stale-element removal in window structures
   - Incorrect path compression / union logic in DSU

### Operation Matrix

| Structure | Typical Use | Update | Query |
|---|---|---:|---:|
| Monotonic Stack | next greater, histogram | `O(1)` amortized | `O(1)` amortized per element |
| Monotonic Queue | sliding window max/min | `O(1)` amortized | `O(1)` per window |
| Heap | top-k, k-way merge | `O(log n)` | `O(1)` top, `O(log n)` pop |
| DSU | connectivity under unions | almost `O(1)` amortized | almost `O(1)` amortized |
| Trie | prefix/word dictionary | `O(L)` | `O(L)` |
| Segment Tree | dynamic range query | `O(log n)` | `O(log n)` |
| Fenwick Tree | prefix sum / point update | `O(log n)` | `O(log n)` |

## Quick Selection Checklist

- Need **next greater / nearest constraint** on each element -> monotonic stack
- Need **sliding window max/min** -> monotonic queue
- Need repeated **top-k or global min/max with updates** -> heap
- Need **dynamic connectivity** -> DSU
- Need **prefix dictionary** or string lookup by prefix -> trie
- Need **range query + point update** on arrays -> segment tree or Fenwick
- Need just **prefix/range sums** with point updates -> Fenwick is simpler

## Monotonic Stack (next greater / histogram)

Use when each element should be processed once and you need nearest larger/smaller relationships.

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
|---|---|---|
| 739 | Daily Temperatures | [Daily Temperatures](https://leetcode.com/problems/daily-temperatures/) |
| 84 | Largest Rectangle in Histogram | [Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/) |
| 503 | Next Greater Element II | [Next Greater Element II](https://leetcode.com/problems/next-greater-element-ii/) |

## Monotonic Queue (sliding window extrema)

Use when you need min/max over every fixed-size window in linear time.

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
|---|---|---|
| 239 | Sliding Window Maximum | [Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/) |
| 1438 | Longest Continuous Subarray With Absolute Diff <= Limit | [Longest Continuous Subarray With Absolute Diff <= Limit](https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/) |

## Heap / K-way Merge

Use for "always extract smallest/largest next" workflows.

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
|---|---|---|
| 23 | Merge k Sorted Lists | [Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/) |
| 295 | Find Median from Data Stream | [Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/) |

## Union-Find (Disjoint Set Union)

Use for incremental connectivity queries in undirected graphs.

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
|---|---|---|
| 684 | Redundant Connection | [Redundant Connection](https://leetcode.com/problems/redundant-connection/) |
| 721 | Accounts Merge | [Accounts Merge](https://leetcode.com/problems/accounts-merge/) |
| 1319 | Number of Operations to Make Network Connected | [Number of Operations to Make Network Connected](https://leetcode.com/problems/number-of-operations-to-make-network-connected/) |

## Trie (Prefix Tree)

Use for fast prefix-based word operations.

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
|---|---|---|
| 208 | Implement Trie | [Implement Trie](https://leetcode.com/problems/implement-trie-prefix-tree/) |
| 211 | Add and Search Word | [Add and Search Word](https://leetcode.com/problems/design-add-and-search-words-data-structure/) |
| 212 | Word Search II | [Word Search II](https://leetcode.com/problems/word-search-ii/) |

## Segment Tree (range query / point update)

Use when you need many dynamic range queries beyond simple prefix sums.

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
|---|---|---|
| 307 | Range Sum Query - Mutable | [Range Sum Query - Mutable](https://leetcode.com/problems/range-sum-query-mutable/) |
| 732 | My Calendar III | [My Calendar III](https://leetcode.com/problems/my-calendar-iii/) |

## Fenwick Tree (Binary Indexed Tree)

Use when operations are point update + prefix/range sum, with lower implementation overhead than segment tree.

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
|---|---|---|
| 315 | Count of Smaller Numbers After Self | [Count of Smaller Numbers After Self](https://leetcode.com/problems/count-of-smaller-numbers-after-self/) |
| 307 | Range Sum Query - Mutable | [Range Sum Query - Mutable](https://leetcode.com/problems/range-sum-query-mutable/) |
