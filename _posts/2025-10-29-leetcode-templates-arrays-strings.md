---
layout: post
title: "LeetCode Templates: Arrays & Strings"
date: 2025-10-29 00:00:00 -0700
categories: leetcode templates arrays strings
permalink: /posts/2025-10-29-leetcode-templates-arrays-strings/
tags: [leetcode, templates, arrays, strings]
---

## Contents

- [Sliding Window (fixed/variable)](#sliding-window-fixedvariable)
- [Two Pointers (sorted arrays/strings)](#two-pointers-sorted-arraysstrings)
- [Binary Search on Answer](#binary-search-on-answer-monotonic-predicate)
- [Prefix Sum / Difference Array](#prefix-sum--difference-array)
- [Hash Map Frequencies](#hash-map-frequencies)
- [KMP (Substring Search)](#kmp-substring-search)
- [Manacher](#manacher-longest-palindromic-substring-on)
- [Z-Algorithm](#z-algorithm-pattern-occurrences)
- [String Rolling Hash](#string-rolling-hash-rabin–karp)

## Sliding Window (fixed/variable)

```python
# Variable-size window (e.g., longest substring without repeating)
def longest_no_repeat(s: str) -> int:
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

| ID | Title | Link |
|---|---|---|
| 3 | [Longest Substring Without Repeating Characters](https://robinali34.github.io/blog_leetcode_python/posts/2025-10-09-medium-3-longest-substring-without-repeating-characters/) | [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | /posts/2025-10-09-medium-3-longest-substring-without-repeating-characters/ |
| 76 | Minimum Window Substring | [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) | - |
| 424 | Longest Repeating Character Replacement | [Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/) | - |

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
def bin_search(lo: int, hi: int) -> int:  # [lo, hi]
    def good(x: int) -> bool:
        # check feasibility
        return True
    
    while lo < hi:
        mid = (lo + hi) >> 1
        if good(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo
```

| ID | Title | Link |
|---|---|---|
| 33 | Search in Rotated Sorted Array | [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) |
| 34 | Find First and Last Position of Element in Sorted Array | [Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/) |
| 162 | Find Peak Element | [Find Peak Element](https://leetcode.com/problems/find-peak-element/) |
| 875 | Koko Eating Bananas | [Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/) |

## Prefix Sum / Difference Array

```python
def prefix(a: list[int]) -> list[int]:
    ps = [0] * (len(a) + 1)
    for i in range(len(a)):
        ps[i + 1] = ps[i] + a[i]
    return ps
```

| ID | Title | Link |
|---|---|---|
| 560 | Subarray Sum Equals K | [Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/) |
| 238 | Product of Array Except Self | [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/) |
| 525 | Contiguous Array | [Contiguous Array](https://leetcode.com/problems/contiguous-array/) |
| 370 | Range Addition | [Range Addition](https://leetcode.com/problems/range-addition/) |

## Hash Map Frequencies

```python
from collections import Counter
freq = Counter(nums)
# or manually:
freq = {}
for x in nums:
    freq[x] = freq.get(x, 0) + 1
```

| ID | Title | Link |
|---|---|---|
| 1 | Two Sum | [Two Sum](https://leetcode.com/problems/two-sum/) |
| 49 | Group Anagrams | [Group Anagrams](https://leetcode.com/problems/group-anagrams/) |
| 981 | Time Based Key-Value Store | [Time Based Key-Value Store](https://leetcode.com/problems/time-based-key-value-store/) |
| 359 | Logger Rate Limiter | [Logger Rate Limiter](https://leetcode.com/problems/logger-rate-limiter/) |

## KMP (Substring Search)
KMP is a pattern matching algorithm that finds occurrences of a pattern string P within a text string T efficiently — without re-checking characters that are already known to match.

While a naive substring search checks character-by-character and backtracks when a mismatch occurs (worst case O(n * m)),
KMP preprocesses the pattern to know how far it can safely skip ahead when mismatches happen.

It does this using a “prefix function” (also called LPS — longest prefix which is also suffix).

### Steps

Preprocess the pattern to build the lps[] array.

lps[i] = the length of the longest proper prefix of the substring P[0..i] which is also a suffix of this substring.

Proper prefix = prefix ≠ the string itself.

Use the LPS array during the search

When mismatch occurs, instead of resetting j = 0,
we move j back to lps[j-1].

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
```

| ID | Title | Link |
|---|---|---|
| 28 | Find the Index of the First Occurrence in a String | [Find the Index of the First Occurrence in a String](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/) |
| 214 | Shortest Palindrome | [Shortest Palindrome](https://leetcode.com/problems/shortest-palindrome/) |

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

## String Rolling Hash (Rabin–Karp)

```python
class RH:
    B = 911382323
    M = 972663749  # example
    
    def __init__(self, s: str):
        n = len(s)
        self.p = [1] * (n + 1)
        self.h = [0] * (n + 1)
        for i in range(n):
            self.p[i + 1] = (self.p[i] * self.B) % self.M
            self.h[i + 1] = (self.h[i] * self.B + ord(s[i])) % self.M
    
    def get(self, l: int, r: int) -> int:  # [l, r)
        return (self.h[r] - self.h[l] * self.p[r - l]) % self.M
```

| ID | Title | Link |
|---|---|---|
| 187 | Repeated DNA Sequences | [Repeated DNA Sequences](https://leetcode.com/problems/repeated-dna-sequences/) |
| 1044 | Longest Duplicate Substring | [Longest Duplicate Substring](https://leetcode.com/problems/longest-duplicate-substring/) |
