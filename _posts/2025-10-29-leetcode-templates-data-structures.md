---
layout: post
title: "LeetCode Templates: Data Structures"
date: 2025-10-29 00:00:00 -0700
categories: leetcode templates data-structures
permalink: /posts/2025-10-29-leetcode-templates-data-structures/
tags: [leetcode, templates, data-structures]
---

## Contents

- [Monotonic Stack](#monotonic-stack-next-greater--histogram)
- [Monotonic Queue](#monotonic-queue-sliding-window-extrema)
- [Heap / K-way Merge](#heap--k-way-merge)
- [Union-Find (DSU)](#union-find-disjoint-set-union)
- [Trie (Prefix Tree)](#trie-prefix-tree)
- [Segment Tree](#segment-tree-range-query--point-update)
- [Fenwick Tree](#fenwick-tree-binary-indexed-tree)

## Monotonic Stack (next greater / histogram)

```python
def next_greater(a: list[int]) -> list[int]:
    n = len(a)
    ans = [-1] * n
    st = []
    for i in range(2 * n):
        idx = i % n
        while st and a[st[-1]] < a[idx]:
            ans[st[-1]] = a[idx]
            st.pop()
        if i < n:
            st.append(idx)
    return ans
```

| ID | Title | Link |
|---|---|---|
| 739 | Daily Temperatures | [Daily Temperatures](https://leetcode.com/problems/daily-temperatures/) |
| 84 | [Largest Rectangle in Histogram](https://robinali34.github.io/blog_leetcode/posts/2025-10-20-hard-84-largest-rectangle-in-histogram/) | [Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/) |
| 503 | Next Greater Element II | [Next Greater Element II](https://leetcode.com/problems/next-greater-element-ii/) |

## Monotonic Queue (sliding window extrema)

```python
from collections import deque

def max_window(a: list[int], k: int) -> list[int]:
    dq = deque()
    out = []
    for i in range(len(a)):
        while dq and a[dq[-1]] <= a[i]:
            dq.pop()
        dq.append(i)
        if dq[0] <= i - k:
            dq.popleft()
        if i >= k - 1:
            out.append(a[dq[0]])
    return out
```

| ID | Title | Link |
|---|---|---|
| 239 | Sliding Window Maximum | [Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/) |
| 1438 | Longest Continuous Subarray With Absolute Diff <= Limit | [Longest Continuous Subarray With Absolute Diff <= Limit](https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/) |

## Heap / K-way Merge

```python
import heapq

def merge_k(lists: list[list[int]]) -> list[int]:
    # pq: (val, list_idx, pos)
    pq = []
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(pq, (lst[0], i, 0))
    out = []
    while pq:
        v, i, j = heapq.heappop(pq)
        out.append(v)
        if j + 1 < len(lists[i]):
            heapq.heappush(pq, (lists[i][j + 1], i, j + 1))
    return out
```

| ID | Title | Link |
|---|---|---|
| 23 | Merge k Sorted Lists | [Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/) |
| 295 | Find Median from Data Stream | [Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/) |

## Union-Find (Disjoint Set Union)

```python
class DSU:
    def __init__(self, n: int):
        self.p = list(range(n))
        self.r = [0] * n
    
    def find(self, x: int) -> int:
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]
    
    def unite(self, a: int, b: int) -> bool:
        a = self.find(a)
        b = self.find(b)
        if a == b:
            return False
        if self.r[a] < self.r[b]:
            a, b = b, a
        self.p[b] = a
        if self.r[a] == self.r[b]:
            self.r[a] += 1
        return True
```

| ID | Title | Link |
|---|---|---|
| 684 | Redundant Connection | [Redundant Connection](https://leetcode.com/problems/redundant-connection/) |
| 721 | Accounts Merge | [Accounts Merge](https://leetcode.com/problems/accounts-merge/) |
| 1319 | Number of Operations to Make Network Connected | [Number of Operations to Make Network Connected](https://leetcode.com/problems/number-of-operations-to-make-network-connected/) |

## Trie (Prefix Tree)

```python
class Trie:
    def __init__(self):
        self.t = [{}]  # list of dicts: [{char -> next_idx}, ...]
        self.end = [False]  # end[i] = True if node i marks end of word
    
    def insert(self, s: str):
        u = 0
        for c in s:
            i = ord(c) - ord('a')
            if i not in self.t[u]:
                self.t[u][i] = len(self.t)
                self.t.append({})
                self.end.append(False)
            u = self.t[u][i]
        self.end[u] = True
    
    def search(self, s: str) -> bool:
        u = 0
        for c in s:
            i = ord(c) - ord('a')
            if i not in self.t[u]:
                return False
            u = self.t[u][i]
        return self.end[u]
```

| ID | Title | Link |
|---|---|---|
| 208 | Implement Trie | [Implement Trie](https://leetcode.com/problems/implement-trie-prefix-tree/) |
| 211 | Add and Search Word | [Add and Search Word](https://leetcode.com/problems/design-add-and-search-words-data-structure/) |
| 212 | Word Search II | [Word Search II](https://leetcode.com/problems/word-search-ii/) |

## Segment Tree (range query / point update)

```python
class SegTree:
    def __init__(self, n: int):
        self.n = n
        self.st = [0] * (4 * n)
    
    def update(self, p: int, v: int, i: int = 0, l: int = 0, r: int = None):
        if r is None:
            r = self.n - 1
        if l == r:
            self.st[i] = v
            return
        m = (l + r) // 2
        if p <= m:
            self.update(p, v, 2 * i + 1, l, m)
        else:
            self.update(p, v, 2 * i + 2, m + 1, r)
        self.st[i] = self.st[2 * i + 1] + self.st[2 * i + 2]
    
    def query(self, ql: int, qr: int, i: int = 0, l: int = 0, r: int = None) -> int:
        if r is None:
            r = self.n - 1
        if qr < l or r < ql:
            return 0
        if ql <= l and r <= qr:
            return self.st[i]
        m = (l + r) // 2
        return self.query(ql, qr, 2 * i + 1, l, m) + self.query(ql, qr, 2 * i + 2, m + 1, r)
```

| ID | Title | Link |
|---|---|---|
| 307 | Range Sum Query – Mutable | [Range Sum Query – Mutable](https://leetcode.com/problems/range-sum-query-mutable/) |
| 732 | My Calendar III | [My Calendar III](https://leetcode.com/problems/my-calendar-iii/) |

## Fenwick Tree (Binary Indexed Tree)

```python
class BIT:
    def __init__(self, n: int):
        self.n = n
        self.f = [0] * (n + 1)
    
    def add(self, i: int, v: int):
        while i <= self.n:
            self.f[i] += v
            i += i & -i
    
    def sum(self, i: int) -> int:
        s = 0
        while i > 0:
            s += self.f[i]
            i -= i & -i
        return s
```

| ID | Title | Link |
|---|---|---|
| 315 | Count of Smaller Numbers After Self | [Count of Smaller Numbers After Self](https://leetcode.com/problems/count-of-smaller-numbers-after-self/) |
| 307 | Range Sum Query – Mutable | [Range Sum Query – Mutable](https://leetcode.com/problems/range-sum-query-mutable/) |
