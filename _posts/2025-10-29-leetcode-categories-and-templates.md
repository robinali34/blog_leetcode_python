---
layout: post
title: "LeetCode Categories and Solution Templates"
date: 2025-10-29 00:00:00 -0700
categories: leetcode algorithm problem-solving templates
permalink: /posts/2025-10-29-leetcode-categories-and-templates/
tags: [leetcode, templates, patterns, dp, graph, sliding-window, two-pointers, binary-search]
---

{% raw %}
# LeetCode Categories and Solution Templates

A quick reference to the most common LeetCode categories and battle‑tested Python templates to speed up implementation.

> This guide is now split into category posts:
> - Arrays & Strings: [/posts/2025-10-29-leetcode-templates-arrays-strings/](/posts/2025-10-29-leetcode-templates-arrays-strings/)
> - Data Structures: [/posts/2025-10-29-leetcode-templates-data-structures/](/posts/2025-10-29-leetcode-templates-data-structures/)
> - Graph: [/posts/2025-10-29-leetcode-templates-graph/](/posts/2025-10-29-leetcode-templates-graph/)
> - Trees: [/posts/2025-10-29-leetcode-templates-trees/](/posts/2025-10-29-leetcode-templates-trees/)
> - Dynamic Programming: [/posts/2025-10-29-leetcode-templates-dp/](/posts/2025-10-29-leetcode-templates-dp/)
> - Math & Geometry: [/posts/2025-10-29-leetcode-templates-math-geometry/](/posts/2025-10-29-leetcode-templates-math-geometry/)
> - Advanced Techniques: [/posts/2025-10-29-leetcode-templates-advanced/](/posts/2025-10-29-leetcode-templates-advanced/)

## Contents

- [Arrays & Strings](#arrays--strings) – core array/string patterns
  - [Sliding Window](#sliding-window-fixedvariable) – subarray/substring constraints
  - [Two Pointers](#two-pointers-sorted-arraysstrings) – ends converge/partition/merge
  - [Binary Search on Answer](#binary-search-on-answer-monotonic-predicate) – monotonic feasibility
  - [Prefix Sum / Difference](#prefix-sum--difference-array) – range totals and updates
  - [Hash Map Frequencies](#hash-map-frequencies) – counting/indexing by value
- [Data Structures](#data-structures) – reusable structures for queries
  - [Monotonic Stack](#monotonic-stack-next-greater--histogram) – next greater/histogram
  - [Monotonic Queue](#monotonic-queue-sliding-window-max) – sliding window extrema
  - [Heap / K-way Merge](#heap--k-way-merge) – merging streams/medians
  - [Union-Find](#union-find-disjoint-set-union) – connectivity/components
  - [Trie](#trie-prefix-tree) – prefix lookup
  - [Segment Tree](#segment-tree-range-querypoint-update) – range queries/point updates
  - [Fenwick Tree](#fenwick-tree-binary-indexed-tree) – prefix sums/inversions
- [Graph](#graph) – traversal and shortest paths
  - [BFS / Shortest Path](#bfs--shortest-path-unweighted) – unweighted shortest paths
  - [Multi-source BFS](#multi-source-bfs-gridsgraphs) – simultaneous wavefronts
  - [BFS on Bitmask State](#bfs-on-bitmask-state-eg-visit-all-keys) – state-space BFS
  - [Topological Sort](#topological-sort-kahn--dfs) – DAG ordering/cycle detect
  - [Dijkstra](#dijkstra-shortest-path-with-weights--0) – nonnegative weights
  - [0-1 BFS](#0-1-bfs-edge-weights-0-or-1) – 0/1 weighted graphs
  - [Tarjan SCC](#tarjan-scc-strongly-connected-components) – strongly connected comps
  - [Bridges & Articulation](#bridges-and-articulation-points-tarjan) – critical edges/nodes
- [Trees](#trees) – hierarchical structures
  - [Traversals](#tree-traversals-iterative) – inorder/level-order
  - [LCA](#lca-binary-lifting) – ancestor queries
  - [HLD](#heavy-light-decomposition-hld-skeleton) – path queries
- [Dynamic Programming](#dynamic-programming) – optimal substructure
  - [1D DP](#1d-dp-knapsacklinear) – knapsack/linear transitions
  - [2D DP](#2d-dp-gridpath) – grid paths/obstacles
  - [Digit DP](#digit-dp-count-numbers-with-property) – per-digit states
  - [Bitmask DP](#bitmask-dp-tsp--subsets) – subsets/TSP
- [Math & Geometry](#math--geometry) – combinatorics and 2D ops
  - [Combinatorics](#math--combinatorics-nck-mod-p) – nCk, factorials, mod math
  - [Geometry Primitives](#geometry-primitives-2d) – cross/segments/areas
- [Advanced Techniques](#advanced-techniques) – specialized patterns
  - [Coordinate Compression](#coordinate-compression) – map values to ranks
  - [Meet-in-the-Middle](#meet-in-the-middle-subset-sums) – split/merge subsets
  - [Manacher](#manacher-longest-palindromic-substring-on) – palindromes in O(n)
  - [Z-Algorithm](#z-algorithm-pattern-occurrences) – pattern occurrences
  - [Bitwise Trie](#bitwise-trie-max-xor-pair) – max XOR pairs

## Arrays & Strings

## Sliding Window (fixed/variable)

Use for subarray/substring with constraints (distinct count, sum/k, length).

```python
# Variable-size window (e.g., longest substring without repeating)
def solve(self, s: str) -> int:
    cnt = [0] * 256
    dup = 0
    best = 0
    l = 0
    for r in range(len(s)):
        cnt[ord(s[r])] += 1
        if cnt[ord(s[r])] == 2:
            dup += 1
        while dup > 0:
            cnt[ord(s[l])] -= 1
            if cnt[ord(s[l])] == 1:
                dup -= 1
            l += 1
        best = max(best, r - l + 1)
    return best
```

Examples: 3 Longest Substring Without Repeating Characters; 76 Minimum Window Substring; 424 Longest Repeating Character Replacement.

| ID | Title | Link |
|---|---|---|
| 3 | Longest Substring Without Repeating Characters | https://leetcode.com/problems/longest-substring-without-repeating-characters/ |
| 76 | Minimum Window Substring | https://leetcode.com/problems/minimum-window-substring/ |
| 424 | Longest Repeating Character Replacement | https://leetcode.com/problems/longest-repeating-character-replacement/ |

## Two Pointers (sorted arrays/strings)

```python
# Classic: two-sum on sorted array, or merging
def twoSum(self, a: list[int], target: int) -> bool:
    l, r = 0, len(a) - 1
    while l < r:
        s = a[l] + a[r]
        if s == target:
            return True
        if s < target:
            l += 1
        else:
            r -= 1
    return False
```

Examples: 15 3Sum; 11 Container With Most Water; 125 Valid Palindrome.

| ID | Title | Link |
|---|---|---|
| 15 | 3Sum | https://leetcode.com/problems/3sum/ |
| 11 | Container With Most Water | https://leetcode.com/problems/container-with-most-water/ |
| 125 | Valid Palindrome | https://leetcode.com/problems/valid-palindrome/ |

## Binary Search on Answer (monotonic predicate)

```python
# find minimum x s.t. predicate(x) == True
def binsearch(self, lo: int, hi: int, good: callable) -> int:
    # [lo, hi] - find minimum x where good(x) is True
    while lo < hi:
        mid = (lo + hi) // 2
        if good(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo
```

Examples: 33 Search in Rotated Sorted Array; 34 First/Last Position; 162 Find Peak Element; 875 Koko Eating Bananas.

| ID | Title | Link |
|---|---|---|
| 33 | Search in Rotated Sorted Array | https://leetcode.com/problems/search-in-rotated-sorted-array/ |
| 34 | Find First and Last Position of Element in Sorted Array | https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/ |
| 162 | Find Peak Element | https://leetcode.com/problems/find-peak-element/ |
| 875 | Koko Eating Bananas | https://leetcode.com/problems/koko-eating-bananas/ |

## Prefix Sum / Difference Array

```python
# range sum queries
def prefix(a: list[int]) -> list[int]:
    ps = [0] * (len(a) + 1)
    for i in range(len(a)):
        ps[i + 1] = ps[i] + a[i]
    return ps
```

Examples: 560 Subarray Sum Equals K; 238 Product of Array Except Self; 525 Contiguous Array; 370 Range Addition.

| ID | Title | Link |
|---|---|---|
| 560 | Subarray Sum Equals K | https://leetcode.com/problems/subarray-sum-equals-k/ |
| 238 | Product of Array Except Self | https://leetcode.com/problems/product-of-array-except-self/ |
| 525 | Contiguous Array | https://leetcode.com/problems/contiguous-array/ |
| 370 | Range Addition | https://leetcode.com/problems/range-addition/ |

## Hash Map Frequencies

```python
# count frequencies and check uniqueness, etc.
from collections import defaultdict
freq = defaultdict(int)
for x in nums:
    freq[x] += 1
```

Examples: 1 Two Sum; 49 Group Anagrams; 981 Time Based Key-Value Store; 359 Logger Rate Limiter.

| ID | Title | Link |
|---|---|---|
| 1 | Two Sum | https://leetcode.com/problems/two-sum/ |
| 49 | Group Anagrams | https://leetcode.com/problems/group-anagrams/ |
| 981 | Time Based Key-Value Store | https://leetcode.com/problems/time-based-key-value-store/ |
| 359 | Logger Rate Limiter | https://leetcode.com/problems/logger-rate-limiter/ |

## Monotonic Stack (next greater / histogram)

```python
# Next Greater Element (circular if needed)
def nextGreater(a: list[int]) -> list[int]:
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

Examples: 739 Daily Temperatures; 84 Largest Rectangle in Histogram; 239 Sliding Window Maximum.

| ID | Title | Link |
|---|---|---|
| 739 | Daily Temperatures | https://leetcode.com/problems/daily-temperatures/ |
| 84 | Largest Rectangle in Histogram | https://leetcode.com/problems/largest-rectangle-in-histogram/ |
| 239 | Sliding Window Maximum | https://leetcode.com/problems/sliding-window-maximum/ |

## Monotonic Queue (Sliding Window Max)

| ID | Title | Link |
|---|---|---|
| 239 | Sliding Window Maximum | https://leetcode.com/problems/sliding-window-maximum/ |
| 1438 | Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit | https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/ |
| 862 | Shortest Subarray with Sum at Least K | https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/ |

## Graph

## BFS / Shortest Path (unweighted)

# Grid BFS template (4-direction)
```python
from collections import deque

def bfsGrid(self, g: list[str], s: tuple[int, int], t: tuple[int, int]) -> int:
    m, n = len(g), len(g[0])
    q = deque([s])
    dist = [[-1] * n for _ in range(m)]
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    dist[s[0]][s[1]] = 0
    
    while q:
        x, y = q.popleft()
        if (x, y) == t:
            return dist[x][y]
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and g[nx][ny] != '#' and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))
    return -1
```

| ID | Title | Link |
|---|---|---|
| 200 | Number of Islands | https://leetcode.com/problems/number-of-islands/ |
| 417 | Pacific Atlantic Water Flow | https://leetcode.com/problems/pacific-atlantic-water-flow/ |
| 542 | 01 Matrix | https://leetcode.com/problems/01-matrix/ |

## DFS / Backtracking

```python
# Subsets
def dfs(self, i: int, nums: list[int], cur: list[int], out: list[list[int]]) -> None:
    if i == len(nums):
        out.append(cur[:])
        return
    self.dfs(i + 1, nums, cur, out)  # skip
    cur.append(nums[i])
    self.dfs(i + 1, nums, cur, out)  # take
    cur.pop()
```

| ID | Title | Link |
|---|---|---|
| 78 | Subsets | https://leetcode.com/problems/subsets/ |
| 46 | Permutations | https://leetcode.com/problems/permutations/ |
| 39 | Combination Sum | https://leetcode.com/problems/combination-sum/ |
| 77 | Combinations | https://leetcode.com/problems/combinations/ |

## Trees

## Tree Traversals (iterative)

# Inorder (iterative)
```python
def inorder(self, root: TreeNode) -> list[int]:
    ans = []
    st = []
    cur = root
    while cur or st:
        while cur:
            st.append(cur)
            cur = cur.left
        cur = st.pop()
        ans.append(cur.val)
        cur = cur.right
    return ans
```

# Level-order (BFS)
```python
from collections import deque

def levelOrder(self, root: TreeNode) -> list[list[int]]:
    if not root:
        return []
    res = []
    q = deque([root])
    while q:
        sz = len(q)
        level = []
        for _ in range(sz):
            u = q.popleft()
            level.append(u.val)
            if u.left:
                q.append(u.left)
            if u.right:
                q.append(u.right)
        res.append(level)
    return res
```

## LCA (Binary Lifting)

```python
K = 17  # adjust for n (e.g., 17 for n<=1e5)
depth = []
up = []

class LCA:
    def __init__(self, n: int):
        self.K = K
        self.depth = [0] * n
        self.up = [[-1] * (K + 1) for _ in range(n)]
    
    def dfsLift(self, u: int, p: int, g: list[list[int]]) -> None:
        self.up[u][0] = p
        for k in range(1, self.K + 1):
            if self.up[u][k-1] < 0:
                self.up[u][k] = -1
            else:
                self.up[u][k] = self.up[self.up[u][k-1]][k-1]
        for v in g[u]:
            if v != p:
                self.depth[v] = self.depth[u] + 1
                self.dfsLift(v, u, g)
    
    def lift(self, u: int, k: int) -> int:
        for i in range(self.K + 1):
            if k & (1 << i):
                if u < 0:
                    return -1
                u = self.up[u][i]
        return u
    
    def lca(self, a: int, b: int) -> int:
        if self.depth[a] < self.depth[b]:
            a, b = b, a
        a = self.lift(a, self.depth[a] - self.depth[b])
        if a == b:
            return a
        for i in range(self.K, -1, -1):
            if self.up[a][i] != self.up[b][i]:
                a = self.up[a][i]
                b = self.up[b][i]
        return self.up[a][0]
```

| ID | Title | Link |
|---|---|---|
| 236 | Lowest Common Ancestor of a Binary Tree | https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/ |
| 235 | Lowest Common Ancestor of a BST | https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/ |

## HLD (Heavy-Light Decomposition) skeleton

```python
# Heavy-Light Decomposition for path queries on a tree
# Build: dfs1 (sizes, heavy child), dfs2 (head/in), then segtree over in[]
class HLD:
    def __init__(self, n: int, g: list[list[int]]):
        self.n = n
        self.g = g
        self.szH = [0] * n
        self.parH = [-1] * n
        self.depH = [0] * n
        self.heavyH = [-1] * n
        self.headH = [0] * n
        self.inH = [0] * n
        self.curT = 0
    
    def dfs1(self, u: int, p: int) -> int:
        self.parH[u] = p
        self.depH[u] = 0 if p == -1 else self.depH[p] + 1
        self.szH[u] = 1
        self.heavyH[u] = -1
        best = 0
        for v in self.g[u]:
            if v != p:
                s = self.dfs1(v, u)
                self.szH[u] += s
                if s > best:
                    best = s
                    self.heavyH[u] = v
        return self.szH[u]
    
    def dfs2(self, u: int, h: int) -> None:
        self.headH[u] = h
        self.inH[u] = self.curT
        self.curT += 1
        if self.heavyH[u] != -1:
            self.dfs2(self.heavyH[u], h)
            for v in self.g[u]:
                if v != self.parH[u] and v != self.heavyH[u]:
                    self.dfs2(v, v)

# Example segment tree over values on nodes (mapped by inH[])
class SegTree:
    def __init__(self, n: int):
        self.n = n
        self.st = [0] * (4 * n)
    
    def upd(self, p: int, v: int, i: int = 1, l: int = 0, r: int = None) -> None:
        if r is None:
            r = self.n - 1
        if l == r:
            self.st[i] = v
            return
        m = (l + r) // 2
        if p <= m:
            self.upd(p, v, 2 * i, l, m)
        else:
            self.upd(p, v, 2 * i + 1, m + 1, r)
        self.st[i] = self.st[2 * i] + self.st[2 * i + 1]
    
    def qry(self, ql: int, qr: int, i: int = 1, l: int = 0, r: int = None) -> int:
        if r is None:
            r = self.n - 1
        if qr < l or r < ql:
            return 0
        if ql <= l and r <= qr:
            return self.st[i]
        m = (l + r) // 2
        return self.qry(ql, qr, 2 * i, l, m) + self.qry(ql, qr, 2 * i + 1, m + 1, r)

def queryPath(self, a: int, b: int, seg: SegTree, hld: HLD) -> int:
    res = 0
    while hld.headH[a] != hld.headH[b]:
        if hld.depH[hld.headH[a]] < hld.depH[hld.headH[b]]:
            a, b = b, a
        res += seg.qry(hld.inH[hld.headH[a]], hld.inH[a], 1, 0, seg.n - 1)
        a = hld.parH[hld.headH[a]]
    if hld.depH[a] > hld.depH[b]:
        a, b = b, a
    res += seg.qry(hld.inH[a], hld.inH[b], 1, 0, seg.n - 1)
    return res
```

| ID | Title | Link |
|---|---|---|
| — | (Rare in LC; use for path queries if needed) | — |

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
| 684 | Redundant Connection | https://leetcode.com/problems/redundant-connection/ |
| 721 | Accounts Merge | https://leetcode.com/problems/accounts-merge/ |
| 1319 | Number of Operations to Make Network Connected | https://leetcode.com/problems/number-of-operations-to-make-network-connected/ |

## Heap / K-way Merge

```python
import heapq

def mergeK(lists: list[list[int]]) -> list[int]:
    # T = (val, list_idx, pos)
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
| 23 | Merge k Sorted Lists | https://leetcode.com/problems/merge-k-sorted-lists/ |
| 295 | Find Median from Data Stream | https://leetcode.com/problems/find-median-from-data-stream/ |

## Topological Sort (Kahn / DFS)

```python
from collections import deque

def topoKahn(n: int, g: list[list[int]]) -> list[int]:
    indeg = [0] * n
    for u in range(n):
        for v in g[u]:
            indeg[v] += 1
    q = deque()
    for i in range(n):
        if not indeg[i]:
            q.append(i)
    order = []
    while q:
        u = q.popleft()
        order.append(u)
        for v in g[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    if len(order) != n:
        order.clear()
    return order
```

| ID | Title | Link |
|---|---|---|
| 207 | Course Schedule | https://leetcode.com/problems/course-schedule/ |
| 210 | Course Schedule II | https://leetcode.com/problems/course-schedule-ii/ |
| 269 | Alien Dictionary | https://leetcode.com/problems/alien-dictionary/ |

## Dijkstra (Shortest Path with Weights ≥ 0)

```python
import heapq

def dijkstra(n: int, g: list[list[tuple[int, int]]], s: int) -> list[int]:
    INF = 1 << 60
    dist = [INF] * n
    dist[s] = 0
    pq = [(0, s)]
    while pq:
        d, u = heapq.heappop(pq)
        if d != dist[u]:
            continue
        for v, w in g[u]:
            if dist[v] > d + w:
                dist[v] = d + w
                heapq.heappush(pq, (dist[v], v))
    return dist
```

| ID | Title | Link |
|---|---|---|
| 743 | Network Delay Time | https://leetcode.com/problems/network-delay-time/ |
| 1631 | Path With Minimum Effort | https://leetcode.com/problems/path-with-minimum-effort/ |

## 0-1 BFS (Edge Weights 0 or 1)

| ID | Title | Link |
|---|---|---|
| 1293 | Shortest Path in a Grid with Obstacles Elimination | https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/ |
| 847 | Shortest Path Visiting All Nodes | https://leetcode.com/problems/shortest-path-visiting-all-nodes/ |

## Trie (Prefix Tree)

| ID | Title | Link |
|---|---|---|
| 208 | Implement Trie (Prefix Tree) | https://leetcode.com/problems/implement-trie-prefix-tree/ |
| 211 | Design Add and Search Words Data Structure | https://leetcode.com/problems/design-add-and-search-words-data-structure/ |
| 212 | Word Search II | https://leetcode.com/problems/word-search-ii/ |

## KMP (Substring Search)

| ID | Title | Link |
|---|---|---|
| 28 | Find the Index of the First Occurrence in a String | https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/ |
| 214 | Shortest Palindrome | https://leetcode.com/problems/shortest-palindrome/ |

## LIS (Patience Sorting, O(n log n))

| ID | Title | Link |
|---|---|---|
| 300 | Longest Increasing Subsequence | https://leetcode.com/problems/longest-increasing-subsequence/ |
| 354 | Russian Doll Envelopes | https://leetcode.com/problems/russian-doll-envelopes/ |

## Segment Tree (Range Query/Point Update)

| ID | Title | Link |
|---|---|---|
| 307 | Range Sum Query – Mutable | https://leetcode.com/problems/range-sum-query-mutable/ |
| 732 | My Calendar III | https://leetcode.com/problems/my-calendar-iii/ |

## Fenwick Tree (Binary Indexed Tree)

| ID | Title | Link |
|---|---|---|
| 315 | Count of Smaller Numbers After Self | https://leetcode.com/problems/count-of-smaller-numbers-after-self/ |
| 307 | Range Sum Query – Mutable | https://leetcode.com/problems/range-sum-query-mutable/ |

## Bitmask DP (TSP / subsets)

| ID | Title | Link |
|---|---|---|
| 847 | Shortest Path Visiting All Nodes | https://leetcode.com/problems/shortest-path-visiting-all-nodes/ |
| 698 | Partition to K Equal Sum Subsets | https://leetcode.com/problems/partition-to-k-equal-sum-subsets/ |

## Math & Geometry

## Math / Combinatorics (nCk mod P)

| ID | Title | Link |
|---|---|---|
| 62 | Unique Paths | https://leetcode.com/problems/unique-paths/ |
| 172 | Factorial Trailing Zeroes | https://leetcode.com/problems/factorial-trailing-zeroes/ |

## Geometry Primitives (2D)

| ID | Title | Link |
|---|---|---|
| 149 | Max Points on a Line | https://leetcode.com/problems/max-points-on-a-line/ |
| 223 | Rectangle Area | https://leetcode.com/problems/rectangle-area/ |

## Manacher (Longest Palindromic Substring, O(n))

| ID | Title | Link |
|---|---|---|
| 5 | Longest Palindromic Substring | https://leetcode.com/problems/longest-palindromic-substring/ |

## Z-Algorithm (Pattern occurrences)

| ID | Title | Link |
|---|---|---|
| 1392 | Longest Happy Prefix | https://leetcode.com/problems/longest-happy-prefix/ |

## Coordinate Compression

| ID | Title | Link |
|---|---|---|
| 315 | Count of Smaller Numbers After Self | https://leetcode.com/problems/count-of-smaller-numbers-after-self/ |
| 327 | Count of Range Sum | https://leetcode.com/problems/count-of-range-sum/ |

## Meet-in-the-Middle (subset sums)

| ID | Title | Link |
|---|---|---|
| 1755 | Closest Subsequence Sum | https://leetcode.com/problems/closest-subsequence-sum/ |
| 805 | Split Array With Same Average | https://leetcode.com/problems/split-array-with-same-average/ |

## Bitwise Trie (Max XOR Pair)

| ID | Title | Link |
|---|---|---|
| 421 | Maximum XOR of Two Numbers in an Array | https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/ |

## Advanced Techniques

## Tarjan SCC (Strongly Connected Components)

```python
# Tarjan's algorithm: O(N+M) to label each node with SCC id
class TarjanSCC:
    def __init__(self, n: int):
        self.n = n
        self.timer = 0
        self.compCnt = 0
        self.g = [[] for _ in range(n)]
        self.tin = [-1] * n
        self.low = [0] * n
        self.comp = [-1] * n
        self.st = []
        self.in_stack = [False] * n
    
    def addEdge(self, u: int, v: int) -> None:
        self.g[u].append(v)
    
    def dfs(self, u: int) -> None:
        self.tin[u] = self.low[u] = self.timer
        self.timer += 1
        self.st.append(u)
        self.in_stack[u] = True
        for v in self.g[u]:
            if self.tin[v] == -1:
                self.dfs(v)
                self.low[u] = min(self.low[u], self.low[v])
            elif self.in_stack[v]:
                self.low[u] = min(self.low[u], self.tin[v])
        if self.low[u] == self.tin[u]:
            while True:
                v = self.st.pop()
                self.in_stack[v] = False
                self.comp[v] = self.compCnt
                if v == u:
                    break
            self.compCnt += 1
    
    def run(self) -> int:
        for i in range(self.n):
            if self.tin[i] == -1:
                self.dfs(i)
        return self.compCnt
```

| ID | Title | Link |
|---|---|---|
| 1192 | Critical Connections in a Network | https://leetcode.com/problems/critical-connections-in-a-network/ |
| 802 | Find Eventual Safe States (SCC/topo variant) | https://leetcode.com/problems/find-eventual-safe-states/ |

## Sweep Line (Intervals)

| ID | Title | Link |
|---|---|---|
| 218 | The Skyline Problem | https://leetcode.com/problems/the-skyline-problem/ |
| 253 | Meeting Rooms II | https://leetcode.com/problems/meeting-rooms-ii/ |

## Greedy

| ID | Title | Link |
|---|---|---|
| 435 | Non-overlapping Intervals | https://leetcode.com/problems/non-overlapping-intervals/ |
| 56 | Merge Intervals | https://leetcode.com/problems/merge-intervals/ |
| 621 | Task Scheduler | https://leetcode.com/problems/task-scheduler/ |

```python
# Interval scheduling: select max non-overlapping
def schedule(self, iv: list[tuple[int, int]]) -> int:
    iv.sort(key=lambda x: x[1])
    cnt = 0
    end = -10**9
    for s, e in iv:
        if s >= end:
            cnt += 1
            end = e
    return cnt
```
{% endraw %}
