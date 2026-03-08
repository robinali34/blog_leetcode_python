---
layout: post
title: "242. Valid Anagram"
date: 2026-03-07 00:00:00 -0700
categories: [leetcode, easy, string, hash-table]
tags: [leetcode, easy, string, anagram, counting]
permalink: /2026/03/07/easy-242-valid-anagram/
---

# 242. Valid Anagram

## Problem Statement

Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.

An **anagram** is a word or phrase formed by rearranging the letters of another, using all the original letters exactly once.

## Examples

**Example 1:**

```python
Input: s = "anagram", t = "nagaram"
Output: True
```

**Example 2:**

```python
Input: s = "rat", t = "car"
Output: False
```

## Constraints

- `1 <= s.length, t.length <= 5 * 10^4`
- `s` and `t` consist of lowercase English letters.

## Clarification Questions

1. **Unicode vs lowercase**: Are we only given lowercase English letters?  
   **Assumption**: Yes per constraints — we can use a fixed-size array of size 26.
2. **Different lengths**: If `len(s) != len(t)`, return `False` immediately.  
   **Assumption**: Yes.

## Interview Deduction Process (20 minutes)

**Step 1: Definition (3 min)**  
Anagram means same multiset of characters: same count for each character. Different length → false.

**Step 2: Count and compare (10 min)**  
Count frequency of each character in `s` (e.g. array or `Counter`). For `t`, decrement counts (or a second count). If any count goes negative, or lengths differ, return false. Alternatively: count `s`, then iterate `t` and decrement; at the end all counts should be 0.

**Step 3: Alternative — sort (5 min)**  
Sort both strings and compare — O(n log n) time, O(n) or O(1) space depending on whether sort is in-place for the type.

## Solution Approach

**Counting:** If `len(s) != len(t)`, return `False`. Use a single array of 26 integers (or a dict) to count characters in `s` (increment), then in `t` (decrement). If any count goes negative, return `False`. If we finish without negative, return `True`. Alternatively: count both and compare the two frequency maps.

**Sort:** Sort `s` and `t` and return `s == t`. O(n log n), simple but slower than linear.

### Key Insights

1. **Same length** — Quick check: anagrams must have the same length.
2. **One array** — Increment for `s`, decrement for `t`; no need for two maps. If any bucket is negative, `t` has a character not in `s` or with higher count.
3. **O(1) extra space** for the counter when we use a fixed 26-sized array (assuming lowercase letters).

## Python Solution

### Counting (O(n) time, O(1) space for 26 letters)

```python
from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        cnt = [0] * 26
        base = ord("a")
        for c in s:
            cnt[ord(c) - base] += 1
        for c in t:
            idx = ord(c) - base
            cnt[idx] -= 1
            if cnt[idx] < 0:
                return False
        return True
```

### Using Counter (O(n) time, O(1) space for 26 letters)

```python
from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return len(s) == len(t) and Counter(s) == Counter(t)
```

## Algorithm Explanation

**Counting:** Build a frequency array for `s`. For each character in `t`, decrement the corresponding count. If any count becomes negative, `t` has more of that character than `s`, so they are not anagrams. Same length plus no negative counts implies the counts match.

**Counter:** `Counter(s) == Counter(t)` compares multisets; combined with the length check we get the same result.

## Complexity Analysis

- **Time**: O(n), where n is the length of the strings (we assume equal length after the check).
- **Space**: O(1) for the 26-element array; O(1) for Counter with a bounded alphabet.

## Edge Cases

- Different lengths → `False`.
- Empty strings → same length, equal counts → `True`.
- Single character, same → `True`; different → `False`.

## Common Mistakes

- **Forgetting length check** — Different-length strings cannot be anagrams; check first to avoid wrong logic.
- **Using two maps and comparing** — One array with increment/decrement is simpler and avoids extra comparison step.

## Related Problems

- [LC 383: Ransom Note](/2026/03/07/easy-383-ransom-note/) — Similar character counting; magazine must cover note.
- [LC 49: Group Anagrams](https://leetcode.com/problems/group-anagrams/) — Group strings by anagram equivalence.
- [LC 387: First Unique Character in a String](https://leetcode.com/problems/first-unique-character-in-a-string/) — Counting then scan.
