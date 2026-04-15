---
layout: post
title: "[Medium] 249. Group Shifted Strings"
date: 2026-03-07 00:00:00 -0700
categories: [leetcode, medium, string, hash-table]
tags: [leetcode, medium, string, grouping, shift]
permalink: /2026/03/07/medium-249-group-shifted-strings/
---

# [Medium] 249. Group Shifted Strings

## Problem Statement

Given a list of strings made of only lowercase letters, group all strings that belong to the same **shifting sequence**.

Two strings are in the same shifting sequence if we can shift one to the other by adding the same constant (mod 26) to every character. Shifting wraps around: `'z' + 1` → `'a'`, `'a' - 1` → `'z'`.

Return the groups in any order.

## Examples

**Example 1:**

```python
Input: strings = ["abc","bcd","acef","xyz","az","ba","a","z"]
Output: [["abc","bcd","xyz"],["az","ba"],["acef"],["a","z"]]
# "abc" → shift by 1 → "bcd"; diff pattern 1,1. "xyz" has diffs 1,1 (x→y, y→z) so same group.
# "az" and "ba" both have single diff 25 (or -1 mod 26) = 25.
# "acef": diffs 2,2,3. "a" and "z": no diffs (length 0 or 1) → same key.
```

**Example 2:**

```python
Input: strings = ["a"]
Output: [["a"]]
```

## Constraints

- `1 <= strings.length <= 200`
- `1 <= strings[i].length <= 50`
- `strings[i]` consists of lowercase English letters.

## Clarification Questions

1. **Shift meaning**: Each character is shifted by the same amount (mod 26)?  
   **Assumption**: Yes — so the sequence of **differences** between consecutive characters is invariant under shifting.
2. **Empty string / single char**: Single-character strings (and empty) all have the same “pattern” (no consecutive pairs), so they group together.  
   **Assumption**: Group them in one group.

## Interview Deduction Process (20 minutes)

**Step 1: When are two strings equivalent? (5 min)**  
If we shift every character by the same amount, the **difference** between consecutive characters (mod 26) stays the same. So "abc" has diffs (1, 1), "bcd" has (1, 1), "xyz" has (1, 1). So we can use the tuple of consecutive differences (mod 26) as a canonical key.

**Step 2: Build the key (10 min)**  
For each string, compute `(ord(s[i]) - ord(s[i-1]) + 26) % 26` for `i in 1..len(s)-1`. Encode this sequence as a string (e.g. comma-separated) so it’s hashable. Group strings in a dict by this key.

**Step 3: Edge cases (5 min)**  
Length 0 or 1: no consecutive pairs, so key is empty; all such strings share the same group.

## Solution Approach

**Hash by difference sequence:** Two strings are in the same shifting sequence iff their sequences of consecutive character differences (mod 26) are equal. So for each string build the list of `(ord(s[i]) - ord(s[i-1]) + 26) % 26` for `i >= 1`, turn it into a hashable key (e.g. comma-separated string or tuple), and group in a dict. Return the dict’s values.

### Key Insights

1. **Invariant under shift** — Shifting every character by `d` doesn’t change the difference between consecutive characters (mod 26).
2. **Key = tuple of diffs** — Encode as a string or tuple so it’s hashable; comma-separated is simple.
3. **Normalize negative diffs** — Use `(diff + 26) % 26` so wraparound (e.g. `'a' - 'b'`) is a positive number in `[0, 25]`.

## Python Solution

### Hash by consecutive differences (O(L) time, O(L) space)

```python
from collections import defaultdict
from typing import List


class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        hm: dict[str, list[str]] = defaultdict(list)
        for s in strings:
            key = []
            for i in range(1, len(s)):
                diff = (ord(s[i]) - ord(s[i - 1]) + 26) % 26
                key.append(str(diff))
            key_str = ",".join(key)
            hm[key_str].append(s)
        return list(hm.values())
```

## Algorithm Explanation

For each string we compute the sequence of “steps” between consecutive characters: `(ord(s[i]) - ord(s[i-1]) + 26) % 26`. This is in `[0, 25]` and is the same for all strings that are shifts of each other (e.g. "abc", "bcd", "xyz" all give `[1, 1]`). We turn the list into a string key (e.g. `"1,1"`) so we can use it as a dict key, append the string to `hm[key_str]`, and finally return all groups as `list(hm.values())`. Strings of length 0 or 1 produce an empty key and are grouped together.

## Complexity Analysis

- **Time**: O(L), where L is the total length of all strings — we do one pass per string and build the key in linear time in the string length.
- **Space**: O(L) for the hash map and the returned list.

## Edge Cases

- **Single character or empty** — Key is the empty string; all such strings go into one group.
- **One group** — All strings in the input might be in the same shifting sequence.
- **All different** — Each string might have a unique difference pattern (e.g. different lengths or patterns).

## Common Mistakes

- **Forgetting to normalize mod 26** — `ord('a') - ord('z')` is negative; use `(diff + 26) % 26` so the key is consistent (e.g. "az" and "ba" should group).
- **Using a list as key** — In Python, lists aren’t hashable; use a tuple or a string (e.g. `",".join(...)`).
- **Off-by-one in the loop** — The key has length `len(s) - 1` (one diff per adjacent pair).

## Related Problems

- [LC 49: Group Anagrams](https://leetcode.com/problems/group-anagrams/) — Group by anagram (same multiset of characters).
- [LC 242: Valid Anagram](/2026/03/07/easy-242-valid-anagram/) — Check if two strings are anagrams.
- [LC 205: Isomorphic Strings](https://leetcode.com/problems/isomorphic-strings/) — Character mapping / structure.
