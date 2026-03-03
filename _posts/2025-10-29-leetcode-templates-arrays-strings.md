---
layout: post
title: "LeetCode Templates: Arrays & Strings"
date: 2025-10-29 00:00:00 -0700
categories: [leetcode, templates, arrays, strings]
permalink: /posts/2025-10-29-leetcode-templates-arrays-strings/
tags: [leetcode, templates, arrays, strings]
---

## Contents

- [How to Analyze Arrays & Strings](#how-to-analyze-arrays--strings)
- [Sliding Window (fixed/variable)](#sliding-window-fixedvariable)
- [Two Pointers (sorted arrays/strings)](#two-pointers-sorted-arraysstrings)
- [Binary Search on Answer](#binary-search-on-answer-monotonic-predicate)
- [Prefix Sum / Difference Array](#prefix-sum--difference-array)
- [Hash Map Frequencies](#hash-map-frequencies)
- [KMP (Substring Search)](#kmp-substring-search)
- [Manacher](#manacher-longest-palindromic-substring-on)
- [Z-Algorithm](#z-algorithm-pattern-occurrences)
- [String Rolling Hash](#string-rolling-hash-rabin-karp)

## How to Analyze Arrays & Strings

Use this checklist before coding:

1. **What kind of interval logic?**
   - contiguous segment -> sliding window / prefix sum
   - pair/triple relation -> two pointers / sort + scan

2. **Is there monotonic feasibility?**
   - if answer can be binary-searched (min/max feasible value), use binary search on answer

3. **Need exact substring matching?**
   - many text-pattern checks -> KMP / Z / rolling hash

4. **Target complexity**
   - most interview-quality solutions should land in `O(n)` or `O(n log n)`

## Sliding Window (fixed/variable)

```python
def longest_no_repeat(s: str) -> int:
    cnt = [0] * 256
    best = 0
    l = 0

    for r, ch in enumerate(s):
        idx = ord(ch)
        cnt[idx] += 1
        while cnt[idx] > 1:
            cnt[ord(s[l])] -= 1
            l += 1
        best = max(best, r - l + 1)
    return best
```

| ID | Title | Link |
|---|---|---|
| 3 | [Longest Substring Without Repeating Characters](/2025/10/09/medium-3-longest-substring-without-repeating-characters/) | [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) |
| 76 | Minimum Window Substring | [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) |
| 424 | Longest Repeating Character Replacement | [Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/) |

## Two Pointers (sorted arrays/strings)

```python
def two_sum_sorted(a: list[int], target: int) -> bool:
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

| ID | Title | Link |
|---|---|---|
| 15 | 3Sum | [3Sum](https://leetcode.com/problems/3sum/) |
| 11 | Container With Most Water | [Container With Most Water](https://leetcode.com/problems/container-with-most-water/) |
| 125 | Valid Palindrome | [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) |

## Binary Search on Answer (monotonic predicate)

```python
def first_good(lo: int, hi: int, good) -> int:
    # Finds smallest x in [lo, hi] with good(x) == True.
    while lo < hi:
        mid = (lo + hi) // 2
        if good(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo
```

| ID | Title | Link |
|---|---|---|
| 875 | Koko Eating Bananas | [Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/) |
| 1011 | Capacity To Ship Packages Within D Days | [Capacity To Ship Packages Within D Days](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/) |
| 410 | Split Array Largest Sum | [Split Array Largest Sum](https://leetcode.com/problems/split-array-largest-sum/) |

## Prefix Sum / Difference Array

```python
def prefix_sum(nums: list[int]) -> list[int]:
    ps = [0] * (len(nums) + 1)
    for i, x in enumerate(nums):
        ps[i + 1] = ps[i] + x
    return ps


def range_sum(ps: list[int], l: int, r: int) -> int:
    # inclusive range [l, r]
    return ps[r + 1] - ps[l]
```

| ID | Title | Link |
|---|---|---|
| 560 | [Subarray Sum Equals K](/2026/02/01/medium-560-subarray-sum-equals-k/) | [Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/) |
| 238 | [Product of Array Except Self](/2026/01/27/medium-238-product-of-array-except-self/) | [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/) |
| 370 | Range Addition | [Range Addition](https://leetcode.com/problems/range-addition/) |

## Hash Map Frequencies

```python
from collections import Counter


def freq_map(nums: list[int]) -> dict[int, int]:
    return dict(Counter(nums))


def freq_map_manual(nums: list[int]) -> dict[int, int]:
    freq = {}
    for x in nums:
        freq[x] = freq.get(x, 0) + 1
    return freq
```

| ID | Title | Link |
|---|---|---|
| 1 | Two Sum | [Two Sum](https://leetcode.com/problems/two-sum/) |
| 49 | [Group Anagrams](/posts/2025-11-18-medium-49-group-anagrams/) | [Group Anagrams](https://leetcode.com/problems/group-anagrams/) |
| 359 | Logger Rate Limiter | [Logger Rate Limiter](https://leetcode.com/problems/logger-rate-limiter/) |

## KMP (Substring Search)

```python
def kmp_pi(s: str) -> list[int]:
    n = len(s)
    pi = [0] * n
    for i in range(1, n):
        j = pi[i - 1]
        while j > 0 and s[i] != s[j]:
            j = pi[j - 1]
        if s[i] == s[j]:
            j += 1
        pi[i] = j
    return pi


def kmp_find_all(text: str, pattern: str) -> list[int]:
    if not pattern:
        return list(range(len(text) + 1))

    pi = kmp_pi(pattern)
    out = []
    j = 0
    for i, ch in enumerate(text):
        while j > 0 and ch != pattern[j]:
            j = pi[j - 1]
        if ch == pattern[j]:
            j += 1
        if j == len(pattern):
            out.append(i - len(pattern) + 1)
            j = pi[j - 1]
    return out
```

| ID | Title | Link |
|---|---|---|
| 28 | Find the Index of the First Occurrence in a String | [Find the Index of the First Occurrence in a String](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/) |
| 214 | Shortest Palindrome | [Shortest Palindrome](https://leetcode.com/problems/shortest-palindrome/) |

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
            center, right = i, i + p[i]
        if p[i] > best_len:
            best_len, best_center = p[i], i

    start = (best_center - best_len) // 2
    return s[start : start + best_len]
```

| ID | Title | Link |
|---|---|---|
| 5 | [Longest Palindromic Substring](/2026/01/08/medium-5-longest-palindromic-substring/) | [Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/) |

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

## String Rolling Hash (Rabin-Karp)

```python
class RH:
    B = 911382323
    M = 1_000_000_007

    def __init__(self, s: str):
        n = len(s)
        self.p = [1] * (n + 1)
        self.h = [0] * (n + 1)
        for i, ch in enumerate(s):
            self.p[i + 1] = (self.p[i] * self.B) % self.M
            self.h[i + 1] = (self.h[i] * self.B + ord(ch)) % self.M

    def get(self, l: int, r: int) -> int:
        # substring hash for s[l:r]
        return (self.h[r] - self.h[l] * self.p[r - l]) % self.M
```

| ID | Title | Link |
|---|---|---|
| 187 | [Repeated DNA Sequences](/2026/02/27/medium-187-repeated-dna-sequences/) | [Repeated DNA Sequences](https://leetcode.com/problems/repeated-dna-sequences/) |
| 1044 | Longest Duplicate Substring | [Longest Duplicate Substring](https://leetcode.com/problems/longest-duplicate-substring/) |

