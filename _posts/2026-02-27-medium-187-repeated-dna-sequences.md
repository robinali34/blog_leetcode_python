---
layout: post
title: "187. Repeated DNA Sequences"
date: 2026-02-27 00:00:00 -0700
categories: [leetcode, medium, string, hashing, sliding-window, bit-manipulation]
permalink: /2026/02/27/medium-187-repeated-dna-sequences/
tags: [leetcode, medium, string, hashing, sliding-window, bit-manipulation]
---

# 187. Repeated DNA Sequences

## Problem Statement

The DNA sequence is composed of a series of nucleotides abbreviated as `'A'`, `'C'`, `'G'`, and `'T'`. Given a string `s` that represents a DNA sequence, return all the **10-letter-long sequences (substrings)** that occur more than once in a DNA molecule. You may return the answer in **any order**.

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

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Substring length**: Is the length always 10? (Assumption: Yes — we need 10-letter-long sequences only.)

2. **Character set**: What characters can appear in `s`? (Assumption: Only `'A'`, `'C'`, `'G'`, `'T'` — standard DNA nucleotides.)

3. **Output format**: Do we need a specific order? (Assumption: Any order; return as list/set of strings.)

4. **Overlap**: Can the same 10-letter sequence appear in multiple overlapping positions? (Assumption: Yes — count each distinct substring that appears at least twice.)

5. **Empty or short string**: What if `s` has fewer than 10 characters? (Assumption: Return empty list — no 10-letter substring exists.)

## Interview Deduction Process (20 minutes)

**Step 1: Brute-Force Approach (5 minutes)**

Slide a window of length 10 over the string; for each substring, check all other positions for a match. O(n²) or O(n × 10) per window — too slow for n up to 10^5. We need to detect duplicates in one pass or with O(1) comparison per window.

**Step 2: Semi-Optimized Approach (7 minutes)**

Use a hash set: for each starting index `i`, extract `s[i:i+10]` and add to a set; if already in the set, add to the result. O(n) time, O(n) space. This works but creates O(n) substrings of length 10. For large n we can avoid creating every substring by using a rolling hash or encoding.

**Step 3: Optimized Solution (8 minutes)**

Encode each of the 4 letters in 2 bits; a 10-letter window fits in 20 bits (one integer). Maintain a rolling hash: for each new character, shift left by 2, add the new 2 bits, mask to 20 bits. Compare integers in O(1); only build the substring when adding to the result. O(n) time, O(n) space with a smaller constant and no substring slicing in the hot loop.

## Solution Approach

This is a **fixed-length sliding window** problem with **substring deduplication**. The key insight is that with only 4 characters, we can encode a 10-character window in 20 bits and use a rolling update for O(1) per step.

### Key Insights:

1. **Fixed window**: There are `n - 9` possible 10-letter substrings; we need to find those that appear more than once.
2. **Small alphabet**: 4 symbols → 2 bits per character → 10 characters = 20 bits, fits in one integer.
3. **Rolling hash**: Update the integer in O(1) by shifting, OR-ing the new character’s bits, and masking to 20 bits.
4. **Duplicate detection**: Use a set of seen hashes; when we see a hash again, add the current window substring to the result.

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

### Algorithm Explanation:

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

### Algorithm Explanation:

1. Encode each character as 0, 1, 2, or 3 (2 bits). Initialize `hash_val = 0`, `mask = (1 << 20) - 1`.
2. For each index `i`, update: `hash_val = ((hash_val << 2) | mapping[s[i]]) & mask`.
3. Once `i >= 9`, the current window is `s[i-9 : i+1]`. If `hash_val` is already in `seen`, add that substring to `repeated`; otherwise add `hash_val` to `seen`.
4. Return `list(repeated)`.

### Why This Works:

- The mask keeps only the last 20 bits, so the integer uniquely represents the last 10 characters. Duplicate windows yield the same hash. We only build the substring when adding to `repeated`.

### Mask trick

- 10 characters × 2 bits = 20 bits.
- `mask = (1 << 20) - 1` keeps only the lowest 20 bits.
- After `(hash_val << 2) | new_bits`, the `& mask` drops the oldest character’s bits, so the integer always represents the last 10 characters.

## Key insights

1. **Fixed-length sliding window** over the string.
2. **Rolling hash / bit encoding** turns a 10-character window into a single integer for O(1) comparison.
3. **Small alphabet (4 symbols)** makes 2-bit encoding and a 20-bit integer feasible.
4. This pattern is useful for string matching, Rabin–Karp, and substring deduplication.

### Edge Cases:

1. **String shorter than 10**: Return empty list.
2. **No repeated sequence**: Return empty list.
3. **All same character (e.g. "AAAAAAAAAAAAA")**: One 10-letter substring repeated; return that one string in a list.

### Common Mistakes:

1. **Forgetting `i >= 9`**: The first valid 10-letter window starts when `i >= 9`.
2. **Using one set only**: We need to distinguish "seen once" vs "seen twice or more"; use one set for seen and one for repeated (or count frequencies).
3. **Wrong mask size**: For 10 characters × 2 bits = 20 bits; mask must be `(1 << 20) - 1`.

### Related Problems:

- [LC 3: Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) — Sliding window
- [LC 76: Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) — Variable window
- [LC 1044: Longest Duplicate Substring](https://leetcode.com/problems/longest-duplicate-substring/) — Binary search + rolling hash

### Follow-ups

- What if the substring length is `k` instead of 10?
- What if the alphabet is larger (e.g., full ASCII)?
- How would you solve it with Rabin–Karp (e.g., a prime-base hash)?
- Can you find repeated substrings of any length?
