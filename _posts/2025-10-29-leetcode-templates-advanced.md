---
layout: post
title: "LeetCode Templates: Advanced Techniques"
date: 2025-10-29 00:00:00 -0700
categories: [leetcode, templates, advanced]
permalink: /posts/2025-10-29-leetcode-templates-advanced/
tags: [leetcode, templates, advanced]
---

## Contents

- [How to Analyze Advanced Techniques](#how-to-analyze-advanced-techniques)
- [Coordinate Compression](#coordinate-compression)
- [Meet-in-the-Middle (subset sums)](#meet-in-the-middle-subset-sums)
- [Manacher (LPS O(n))](#manacher-longest-palindromic-substring-on)
- [Z-Algorithm](#z-algorithm-pattern-occurrences)
- [Bitwise Trie (Max XOR Pair)](#bitwise-trie-max-xor-pair)

## How to Analyze Advanced Techniques

Use advanced techniques only when baseline patterns are close but still too slow.

1. **Identify the bottleneck**
   - `O(n^2)` from pairwise checks?
   - `O(2^n)` subset brute force?
   - repeated string comparisons?

2. **Match structure to pattern**
   - Huge values, small distinct coordinates -> coordinate compression
   - `n <= 40` subset sum variants -> meet-in-the-middle
   - many palindrome queries -> Manacher
   - prefix/suffix match logic -> Z-algorithm
   - maximum XOR objective -> bitwise trie

3. **Validate complexity**
   - Compression: `O(n log n)` preprocess, `O(log n)` map lookup
   - MITM: `O(2^(n/2) log 2^(n/2))`
   - Manacher/Z: `O(n)`
   - Bitwise trie: `O(B)` per insert/query (`B=31`)

## Coordinate Compression

```python
from bisect import bisect_left


class Compressor:
    def __init__(self):
        self.vals = []

    def add(self, items) -> None:
        self.vals.extend(items)

    def build(self) -> None:
        self.vals = sorted(set(self.vals))

    def get(self, x: int) -> int:
        return bisect_left(self.vals, x)
```

| ID | Title | Link |
|---|---|---|
| 315 | Count of Smaller Numbers After Self | [Count of Smaller Numbers After Self](https://leetcode.com/problems/count-of-smaller-numbers-after-self/) |
| 327 | Count of Range Sum | [Count of Range Sum](https://leetcode.com/problems/count-of-range-sum/) |

## Meet-in-the-Middle (subset sums)

```python
from bisect import bisect_left, bisect_right


def all_subset_sums(nums: list[int]) -> list[int]:
    n = len(nums)
    out = []
    for mask in range(1 << n):
        s = 0
        for i in range(n):
            if (mask >> i) & 1:
                s += nums[i]
        out.append(s)
    return out


def count_subsets_equal_target(nums: list[int], target: int) -> int:
    mid = len(nums) // 2
    left = all_subset_sums(nums[:mid])
    right = all_subset_sums(nums[mid:])
    right.sort()

    ans = 0
    for x in left:
        lo = bisect_left(right, target - x)
        hi = bisect_right(right, target - x)
        ans += hi - lo
    return ans
```

| ID | Title | Link |
|---|---|---|
| 1755 | Closest Subsequence Sum | [Closest Subsequence Sum](https://leetcode.com/problems/closest-subsequence-sum/) |
| 805 | Split Array With Same Average | [Split Array With Same Average](https://leetcode.com/problems/split-array-with-same-average/) |

## Manacher (Longest Palindromic Substring, O(n))

```python
def manacher(s: str) -> str:
    if not s:
        return ""

    t = "|" + "|".join(s) + "|"
    n = len(t)
    p = [0] * n
    center = right = 0
    best_len = best_center = 0

    for i in range(n):
        mirror = 2 * center - i
        if i < right:
            p[i] = min(right - i, p[mirror])

        while (
            i - 1 - p[i] >= 0
            and i + 1 + p[i] < n
            and t[i - 1 - p[i]] == t[i + 1 + p[i]]
        ):
            p[i] += 1

        if i + p[i] > right:
            center = i
            right = i + p[i]

        if p[i] > best_len:
            best_len = p[i]
            best_center = i

    start = (best_center - best_len) // 2
    return s[start : start + best_len]
```

| ID | Title | Link |
|---|---|---|
| 5 | Longest Palindromic Substring | [Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/) |

## Z-Algorithm (Pattern occurrences)

```python
def z_func(s: str) -> list[int]:
    n = len(s)
    if n == 0:
        return []

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

    def insert(self, x: int) -> None:
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
