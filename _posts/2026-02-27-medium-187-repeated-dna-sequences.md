---
layout: post
title: "[Medium] 187. Repeated DNA Sequences"
date: 2026-02-27 00:00:00 -0700
categories: leetcode algorithm medium python string hashing sliding-window bit-manipulation
---

# [Medium] 187. Repeated DNA Sequences

The DNA sequence is composed of a series of nucleotides abbreviated as `'A'`, `'C'`, `'G'`, and `'T'`. Given a string `s` that represents a DNA sequence, return all the **10-letter-long sequences (substrings)** that occur more than once in a DNA molecule. You may return the answer in **any order**.

## Problem Summary

Given a DNA string `s` (characters only `'A'`, `'C'`, `'G'`, and `'T'`), return all 10-letter-long sequences that occur more than once.

## Examples

**Example 1:**
```
Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC", "CCCCCAAAAA"]
```

**Example 2:**
```
Input: s = "AAAAAAAAAAAAA"
Output: ["AAAAAAAAAA"]
```

## Constraints

- `1 <= s.length <= 10^5`
- `s[i]` is either `'A'`, `'C'`, `'G'`, or `'T'`.

## Analysis

1. **Constraints thinking**
   - DNA has only 4 character types → good for encoding (e.g., 2 bits per character).
   - Fixed substring length = 10.
   - If `n` is the length of the string, there are `n - 9` possible 10-letter substrings.
   - We need to detect duplicates efficiently.

## Solution 1: Hash Set (Baseline)

**Idea:** Slide a window of length 10, store each substring in a set; if seen again, add to the result set.

**Time Complexity:** O(n)  
**Space Complexity:** O(n)

Each substring copy is O(10), so this is simple but does more string work than necessary.

```python
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        if len(s) < 10:
            return []
        seen = set()
        repeated = set()
        for i in range(len(s) - 9):
            sub = s[i : i + 10]
            if sub in seen:
                repeated.add(sub)
            else:
                seen.add(sub)
        return list(repeated)

```

### How it works

1. Iterate over every starting index `i` for a 10-character window.
2. Extract substring `s[i : i + 10]`.
3. If it’s already in `seen`, add it to `repeated`; otherwise add it to `seen`.
4. Return `repeated` as a list.

---

## Solution 2: Rolling Hash with Bit Encoding (Optimal)

**Idea:** With only 4 letters, we can encode each character in 2 bits. So 10 characters use 20 bits and fit in a 32-bit integer. We can use a rolling window: update the integer in O(1) by shifting, adding the new character’s bits, and masking out the oldest.

**Encoding:**

| Char | Binary |
|------|--------|
| A    | 00     |
| C    | 01     |
| G    | 10     |
| T    | 11     |

**Rolling update:** For a window of 10 characters (20 bits), use a mask `(1 << 20) - 1`. After shifting left by 2 and adding the new character’s 2 bits, apply the mask so only the last 20 bits are kept.

**Time Complexity:** O(n)  
**Space Complexity:** O(n)

Each step is O(1); no substring creation in the hot path. We only form the substring when adding to the result (when a duplicate is found).

```python
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        if len(s) < 10:
            return []

        mapping = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
        seen = set()
        repeated = set()

        hash_val = 0
        mask = (1 << 20) - 1

        for i in range(len(s)):
            hash_val = ((hash_val << 2) | mapping[s[i]]) & mask

            if i >= 9:
                if hash_val in seen:
                    repeated.add(s[i - 9 : i + 1])
                else:
                    seen.add(hash_val)

        return list(repeated)

```

### How it works

1. Encode each character as 0, 1, 2, or 3 (2 bits).
2. For each index `i`, update: `hash_val = ((hash_val << 2) | mapping[s[i]]) & mask`.
3. Once `i >= 9`, the current window is `s[i-9 : i+1]`. If `hash_val` is already in `seen`, add that substring to `repeated`; otherwise add `hash_val` to `seen`.
4. Return `repeated` as a list.

### Mask trick

- 10 characters × 2 bits = 20 bits.
- `mask = (1 << 20) - 1` keeps only the lowest 20 bits.
- After `(hash_val << 2) | new_bits`, the `& mask` drops the oldest character’s bits, so the integer always represents the last 10 characters.

## Key insights

1. **Fixed-length sliding window** over the string.
2. **Rolling hash / bit encoding** turns a 10-character window into a single integer for O(1) comparison.
3. **Small alphabet (4 symbols)** makes 2-bit encoding and a 20-bit integer feasible.
4. This pattern is useful for string matching, Rabin–Karp, and substring deduplication.

## Follow-ups

- What if the substring length is `k` instead of 10?
- What if the alphabet is larger (e.g., full ASCII)?
- How would you solve it with Rabin–Karp (e.g., a prime-base hash)?
- Can you find repeated substrings of any length?
