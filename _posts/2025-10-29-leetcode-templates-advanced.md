---
layout: post
title: "LeetCode Templates: Advanced Techniques"
date: 2025-10-29 00:00:00 -0700
categories: leetcode templates advanced
permalink: /posts/2025-10-29-leetcode-templates-advanced/
tags: [leetcode, templates, advanced]
---

## Contents

- [Coordinate Compression](#coordinate-compression)
- [Meet-in-the-Middle (subset sums)](#meet-in-the-middle-subset-sums)
- [Manacher (LPS O(n))](#manacher-longest-palindromic-substring-on)
- [Z-Algorithm](#z-algorithm-pattern-occurrences)
- [Bitwise Trie (Max XOR Pair)](#bitwise-trie-max-xor-pair)

## Coordinate Compression

```python
from bisect import bisect_left

class Compressor:
    def __init__(self):
        self.vals = []
    
    def add(self, items):
        self.vals.extend(items)
    
    def build(self):
        self.vals = sorted(set(self.vals))
    
    def get(self, x):
        return bisect_left(self.vals, x)
```

| ID | Title | Link |
|---|---|---|
| 315 | Count of Smaller Numbers After Self | [Count of Smaller Numbers After Self](https://leetcode.com/problems/count-of-smaller-numbers-after-self/) |
| 327 | Count of Range Sum | [Count of Range Sum](https://leetcode.com/problems/count-of-range-sum/) |

## Meet-in-the-Middle (subset sums)

```python
from bisect import bisect_left, bisect_right

def count_subsets(a: list[int], T: int) -> int:
    n = len(a)
    m = n // 2
    L, R = [], []
    
    def go(l: int, r: int, out: list):
        k = r - l
        for mask in range(1 << k):
            s = 0
            for i in range(k):
                if mask >> i & 1:
                    s += a[l + i]
            out.append(s)
    
    go(0, m, L)
    go(m, n, R)
    R.sort()
    ans = 0
    for x in L:
        left = bisect_left(R, T - x)
        right = bisect_right(R, T - x)
        ans += right - left
    return ans
```

| ID | Title | Link |
|---|---|---|
| 1755 | Closest Subsequence Sum | [Closest Subsequence Sum](https://leetcode.com/problems/closest-subsequence-sum/) |
| 805 | Split Array With Same Average | [Split Array With Same Average](https://leetcode.com/problems/split-array-with-same-average/) |

## Manacher (Longest Palindromic Substring, O(n))

```python
def manacher(s: str) -> str:
    t = "|" + "|".join(s) + "|"
    n = len(t)
    p = [0] * n
    c = r = best = center = 0
    for i in range(n):
        mir = 2 * c - i
        if i < r:
            p[i] = min(r - i, p[mir])
        while i - 1 - p[i] >= 0 and i + 1 + p[i] < n and t[i - 1 - p[i]] == t[i + 1 + p[i]]:
            p[i] += 1
        if i + p[i] > r:
            c = i
            r = i + p[i]
        if p[i] > best:
            best = p[i]
            center = i
    start = (center - best) // 2
    return s[start:start + best]
```

| ID | Title | Link |
|---|---|---|
| 5 | Longest Palindromic Substring | [Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/) |

## Z-Algorithm (Pattern occurrences)

```python
def z_func(s: str) -> list[int]:
    n = len(s)
    z = [0] * n
    l = r = 0
    for i in range(1, n):
        if i <= r:
            z[i] = min(r - i + 1, z[i - l])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] - 1 > r:
            l = i
            r = i + z[i] - 1
    return z
```

| ID | Title | Link |
|---|---|---|
| 1392 | Longest Happy Prefix | [Longest Happy Prefix](https://leetcode.com/problems/longest-happy-prefix/) |

## Bitwise Trie (Max XOR Pair)

```python
class BitTrie:
    class Node:
        def __init__(self):
            self.ch = [-1, -1]
    
    def __init__(self):
        self.t = [self.Node()]
    
    def insert(self, x: int):
        u = 0
        for b in range(31, -1, -1):
            bit = (x >> b) & 1
            if self.t[u].ch[bit] == -1:
                self.t[u].ch[bit] = len(self.t)
                self.t.append(self.Node())
            u = self.t[u].ch[bit]
    
    def max_xor(self, x: int) -> int:
        u = 0
        ans = 0
        for b in range(31, -1, -1):
            bit = (x >> b) & 1
            want = bit ^ 1
            if self.t[u].ch[want] != -1:
                ans |= 1 << b
                u = self.t[u].ch[want]
            else:
                u = self.t[u].ch[bit]
        return ans
```

| ID | Title | Link |
|---|---|---|
| 421 | Maximum XOR of Two Numbers in an Array | [Maximum XOR of Two Numbers in an Array](https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/) |
