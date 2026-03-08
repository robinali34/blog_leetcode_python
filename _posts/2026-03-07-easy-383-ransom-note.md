---
layout: post
title: "383. Ransom Note"
date: 2026-03-07 00:00:00 -0700
categories: [leetcode, easy, string, hash-table]
tags: [leetcode, easy, string, counting]
permalink: /2026/03/07/easy-383-ransom-note/
---

# 383. Ransom Note

## Problem Statement

Given two strings `ransomNote` and `magazine`, return `true` if `ransomNote` can be constructed by using **only** the letters from `magazine` and `false` otherwise.

Each letter in `magazine` can only be used **once** in `ransomNote`.

## Examples

**Example 1:**

```python
Input: ransomNote = "a", magazine = "b"
Output: False
```

**Example 2:**

```python
Input: ransomNote = "aa", magazine = "ab"
Output: False
# Need two 'a's; magazine has only one.
```

**Example 3:**

```python
Input: ransomNote = "aa", magazine = "aab"
Output: True
```

## Constraints

- `1 <= ransomNote.length, magazine.length <= 10^5`
- `ransomNote` and `magazine` consist of lowercase English letters.

## Clarification Questions

1. **Case**: Lowercase only?  
   **Assumption**: Yes — we can use a 26-sized count array.
2. **Reuse**: Each character in `magazine` at most once?  
   **Assumption**: Yes.

## Interview Deduction Process (20 minutes)

**Step 1: Meaning (3 min)**  
We need every character in `ransomNote` to appear in `magazine` with at least the same frequency. So count available letters in `magazine`, then “spend” them for each character in `ransomNote`; if we ever need more than available, return false.

**Step 2: Count magazine (7 min)**  
Build a frequency map (array of 26 or `Counter`) for `magazine`. Iterate over `ransomNote`; for each character decrement its count. If any count goes negative, return `False`. Otherwise return `True`.

**Step 3: One pass (5 min)**  
We can count `magazine` first, then one pass over `ransomNote`; no need to count `ransomNote` separately.

## Solution Approach

**Counting:** Count character frequencies in `magazine`. For each character in `ransomNote`, decrement the corresponding count. If any count becomes negative, the note cannot be built. Otherwise it can.

### Key Insights

1. **Magazine supplies, note consumes** — Count what’s available, then “use” letters for the note.
2. **Decrement and check** — Decrement as we process the note; first negative means impossible.
3. **Same pattern as anagram** — Like LC 242 but one string is the “pool” and the other is the “demand”; no need for same length.

## Python Solution

### Counting (O(n + m) time, O(1) space)

```python
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        cnt = [0] * 26
        base = ord("a")
        for c in magazine:
            cnt[ord(c) - base] += 1
        for c in ransomNote:
            idx = ord(c) - base
            cnt[idx] -= 1
            if cnt[idx] < 0:
                return False
        return True
```

### Using Counter

```python
from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        return not (Counter(ransomNote) - Counter(magazine))
        # Counter subtraction leaves only positive counts; empty if note is covered.
```

## Algorithm Explanation

Count how many of each letter appear in `magazine`. Then for each letter in `ransomNote`, subtract one from that letter’s count. If we ever go below zero, the magazine doesn’t have enough of that letter, so return `False`. If we process the entire note without going negative, return `True`. Optional: if `len(ransomNote) > len(magazine)`, return `False` early.

## Complexity Analysis

- **Time**: O(n + m), where n = len(ransomNote), m = len(magazine).
- **Space**: O(1) for the 26-element count array.

## Edge Cases

- `ransomNote` longer than `magazine` → `False` (optional early exit).
- Empty `ransomNote` → `True`.
- Empty `magazine` with non-empty note → `False`.

## Common Mistakes

- **Using each magazine letter more than once** — Decrement when “using” a letter; don’t reuse.
- **Counting note then comparing** — Simpler to count magazine and then consume for note.

## Related Problems

- [LC 242: Valid Anagram](/2026/03/07/easy-242-valid-anagram/) — Same-character-count check; both strings must match.
- [LC 387: First Unique Character in a String](https://leetcode.com/problems/first-unique-character-in-a-string/) — Count then scan.
- [LC 49: Group Anagrams](https://leetcode.com/problems/group-anagrams/) — Group by character counts.
