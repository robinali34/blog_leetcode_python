---
layout: post
title: "[Easy] 1768. Merge Strings Alternately"
date: 2026-03-27 00:00:00 -0700
categories: [leetcode, easy, string, two-pointers]
tags: [leetcode, easy, string, two-pointers]
permalink: /2026/03/27/easy-1768-merge-strings-alternately/
---

# [Easy] 1768. Merge Strings Alternately

## Problem Statement

You are given two strings `word1` and `word2`. Merge them by adding letters in alternating order, starting with `word1`. If a string is longer than the other, append the additional letters onto the end of the merged string.

## Examples

**Example 1:**

```python
Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
```

**Example 2:**

```python
Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
```

**Example 3:**

```python
Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
```

## Constraints

- `1 <= word1.length, word2.length <= 100`
- `word1` and `word2` consist of lowercase English letters

## Clarification Questions

1. **Order when lengths differ?** After alternating while both have characters, append the remainder of the longer string in order.
2. **Empty string?** Constraints say length ≥ 1, so both are non-empty.
3. **Case sensitivity?** Lowercase only per constraints.

## Analysis Process

Use two indices `i`, `j`. Each iteration: if `i < m`, take `word1[i]` and advance `i`; if `j < n`, take `word2[j]` and advance `j`. Stop when both are exhausted. This naturally alternates while both strings have characters, then drains the longer one.

## Python Solution

```python
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m, n = len(word1), len(word2)
        i, j = 0, 0
        rtn = list()
        while i < m or j < n:
            if i < m:
                rtn.append(word1[i])
                i += 1
            if j < n:
                rtn.append(word2[j])
                j += 1
        return "".join(rtn)
```

### Variant: single loop with `max(m, n)`

You can also iterate `k` from `0` to `max(m, n) - 1` and append `word1[k]` / `word2[k]` when in range; same complexity.

## Complexity Analysis

- **Time:** O(m + n)
- **Space:** O(m + n) for the output list (output length is always m + n)

## Common Mistakes

- Using one `while i < m and j < n` only, then forgetting to append the tail of the longer string.
- Building with repeated string concatenation in a loop (slow in some languages); list + `join` is fine in Python.

## Related Problems

- [LC 281: Zigzag Iterator](https://leetcode.com/problems/zigzag-iterator/)
- [LC 392: Is Subsequence](https://leetcode.com/problems/is-subsequence/)
