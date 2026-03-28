---
layout: post
title: "151. Reverse Words in a String"
date: 2026-03-29 00:00:00 -0700
categories: [leetcode, medium, string, two-pointers]
tags: [leetcode, medium, string, deque, two-pointers]
permalink: /2026/03/29/medium-151-reverse-words-in-a-string/
---

# 151. Reverse Words in a String

## Problem Statement

Given an input string `s`, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in `s` will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

**Note:** `s` may contain leading or trailing spaces or multiple spaces between two words.

## Examples

**Example 1:**

```python
Input: s = "the sky is blue"
Output: "blue is sky the"
```

**Example 2:**

```python
Input: s = "  hello world  "
Output: "world hello"
```

**Example 3:**

```python
Input: s = "a good   example"
Output: "example good a"
```

## Constraints

- `1 <= s.length <= 10^4`
- `s` contains English letters (upper-case and lower-case), digits, and spaces `' '`
- There is at least one word in `s`

## Clarification Questions

1. **Collapse internal spaces?** Yes — output must use exactly one space between words, no leading/trailing spaces.
2. **Preserve case?** Yes, only word order changes.
3. **Mutable string?** In Python, strings are immutable; “in-place” is usually simulated with a list of characters.

## Analysis Process

Scan left to right after trimming ends (or while scanning, skip duplicate spaces). Collect each word’s characters; on a space boundary after a non-empty word, push the word to the front of a structure so overall order is reversed. Finally join with a single space.

Your approach uses `deque.appendleft` so the first word ends up rightmost in the final join.

## Solution Options

### Option 1: Trim + scan + `deque` (your solution)

```python
from collections import deque


class Solution:
    def reverseWords(self, s: str) -> str:
        left, right = 0, len(s) - 1
        while left <= right and s[left] == " ":
            left += 1
        while left <= right and s[right] == " ":
            right -= 1
        d, word = deque(), []
        while left <= right:
            if s[left] == " " and word:
                d.appendleft("".join(word))
                word = []
            elif s[left] != " ":
                word.append(s[left])
            left += 1
        d.appendleft("".join(word))
        return " ".join(d)
```

`appendleft` builds reversed order without reversing a full word list at the end.

### Option 2: `split` + reverse + `join`

```python
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])
```

`str.split()` with no argument splits on any run of whitespace and strips leading/trailing spaces. Concise for interviews when library use is allowed.

### Option 3: Manual word boundaries + `reversed`

Same idea as scanning, but collect words in a list then `join(reversed(...))`:

```python
class Solution:
    def reverseWords(self, s: str) -> str:
        words = []
        i, n = 0, len(s)
        while i < n:
            while i < n and s[i] == " ":
                i += 1
            if i >= n:
                break
            j = i
            while j < n and s[j] != " ":
                j += 1
            words.append(s[i:j])
            i = j
        return " ".join(reversed(words))
```

For a true **mutable character buffer** (reverse whole string then reverse each word), see [LC 186](https://leetcode.com/problems/reverse-words-in-a-string-ii/).

## Comparison

| Option | Time | Extra space | Pros | Cons |
|--------|------|-------------|------|------|
| Deque + scan | O(n) | O(n) words | Single pass over trimmed range, clear control | More code than `split` |
| `split` + slice | O(n) | O(n) | Short and readable | Relies on `split` behavior |
| Manual boundaries + `reversed` | O(n) | O(n) | No `deque`; explicit trimming | Slightly more index logic |

## Complexity Analysis

For Option 1:

- **Time:** O(n) — each index visited once; each character copied into a word and deque.
- **Space:** O(n) for stored words and the result string.

## Common Mistakes

- Forgetting to `appendleft` the last word after the loop (your code handles this with a final `appendleft`).
- Including empty strings when splitting naively on `' '` only.
- Returning multiple spaces between words.

## Related Problems

- [LC 186: Reverse Words in a String II](https://leetcode.com/problems/reverse-words-in-a-string-ii/)
- [LC 557: Reverse Words in a String III](https://leetcode.com/problems/reverse-words-in-a-string-iii/)
