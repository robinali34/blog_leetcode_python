---
layout: post
title: "1328. Break a Palindrome"
date: 2026-03-07 00:00:00 -0700
categories: [leetcode, medium, string, greedy]
tags: [leetcode, medium, string, palindrome, greedy]
permalink: /2026/03/07/medium-1328-break-a-palindrome/
---

# 1328. Break a Palindrome

## Problem Statement

Given a palindromic string `palindrome` of lowercase English letters, replace **exactly one** character with any lowercase letter so that the result is **not** a palindrome and is the **lexicographically smallest** string possible.

Return the resulting string. If impossible, return the empty string `""`.

## Examples

**Example 1:**

```python
Input: palindrome = "abccba"
Output: "aaccba"
```

**Example 2:**

```python
Input: palindrome = "a"
Output: ""
```

## Constraints

- `1 <= palindrome.length <= 1000`
- `palindrome` consists of lowercase English letters

## Analysis

- If length is **1**, any single-character string is a palindrome → return `""`.
- To get the **smallest** lex order, scan the **first half** only (index `i < n // 2`): the mirror position `n - 1 - i` is fixed by palindrome symmetry.
- First position where `chars[i] != 'a'`, set it to `'a'` → strictly smaller and breaks palindrome (unless the whole first half was `'a'`).
- If every character in the first half is `'a'`, the only way to break the palindrome while staying as small as possible is to bump the **last** character from `'a'` to `'b'` (works for `n >= 2`).

## Python Solution

```python
class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)
        if n == 1:
            return ""
        chars = list(palindrome)
        for i in range(0, n // 2):
            if chars[i] != "a":
                chars[i] = "a"
                return "".join(chars)
        chars[n - 1] = "b"
        return "".join(chars)
```

## Complexity

- **Time:** O(n)
- **Space:** O(n) for the list of characters (output is length `n`)

## Common Mistakes

- Modifying the mirror in the second half without mirroring logic — only edit the first half for the greedy step.
- Forgetting the all-`'a'` case (need last char `'b'`).

## Related Problems

- [LC 125: Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)
- [LC 680: Valid Palindrome II](https://leetcode.com/problems/valid-palindrome-ii/)
