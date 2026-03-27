---
layout: post
title: "1087. Brace Expansion"
date: 2026-03-26 00:00:00 -0700
categories: [leetcode, medium, backtracking, string]
tags: [leetcode, medium, backtracking, dfs, string-parsing]
permalink: /2026/03/26/medium-1087-brace-expansion/
---

# 1087. Brace Expansion

## Problem Statement

A string `s` represents a list of words where each letter can be fixed or selected from a brace group.

Examples:

- `"a{b,c}d"` -> `["abd", "acd"]`
- `"{a,b}c{d,e}f"` -> `["acdf", "acef", "bcdf", "bcef"]`

Return all words in **lexicographical order**.

## Examples

**Example 1:**

```python
Input: s = "{a,b}c{d,e}f"
Output: ["acdf","acef","bcdf","bcef"]
```

**Example 2:**

```python
Input: s = "abcd"
Output: ["abcd"]
```

## Constraints

- `1 <= len(s) <= 50`
- `s` consists of lowercase letters, `{`, `}`, and `,`
- Input is valid and brace groups are well-formed

## Clarification Questions

1. **Are brace options single characters only?**  
   For this problem, yes (e.g. `{a,b,c}`).
2. **Do we need sorted output?**  
   Yes, lexicographical order is required.
3. **Can there be nested braces?**  
   No, this version has no nested brace expressions.

## Analysis Process

### 1) Parse into groups

Convert string into a list of character groups:

- fixed character -> one-element group (e.g. `['x']`)
- brace group -> sorted choice group (e.g. `{b,a,c}` -> `['a','b','c']`)

Example:

`"{a,b}c{d,e}"` -> `[['a','b'], ['c'], ['d','e']]`

### 2) Generate combinations with DFS

Do backtracking over group index:

- at position `pos`, try each character in `groups[pos]`
- append to current path
- recurse to `pos + 1`
- pop to backtrack

When `pos == len(groups)`, one full expanded word is built.

Because each group is sorted and DFS visits in that order, output is naturally lexicographical.

## Solution Options

### Option 1: Parse + DFS Backtracking (Recommended)

```python
from typing import List


class Solution:
    def expand(self, s: str) -> List[str]:
        groups = []
        i = 0
        while i < len(s):
            if s[i] == '{':
                i += 1
                choices = []

                while s[i] != '}':
                    if s[i].isalpha():
                        choices.append(s[i])
                    i += 1
                groups.append(sorted(choices))
                i += 1
            else:
                groups.append([s[i]])
                i += 1
        rtn = []

        def dfs(pos: int, path: list[str]) -> None:
            if pos == len(groups):
                rtn.append(''.join(path))
                return
            for ch in groups[pos]:
                path.append(ch)
                dfs(pos + 1, path)
                path.pop()

        dfs(0, [])
        return rtn
```

### Option 2: Iterative Product Build

Build results progressively:

- start with `[""]`
- for each group, create new list by appending every choice to each existing prefix

This avoids recursion but follows the same Cartesian-product idea.

## Comparison

| Option | Time | Extra Space | Pros | Cons |
|---|---:|---:|---|---|
| Parse + DFS | O(total output size) | O(depth + output) | Clean recursion, interview-friendly | Recursion stack |
| Iterative product | O(total output size) | O(output) | No recursion | Less intuitive for some |

## Complexity Analysis

Let:

- `k` = number of groups
- `m_i` = number of choices in group `i`
- `W = product(m_i)` = number of output words

Then:

- **Time:** `O(W * k)` (must generate all output strings)
- **Space:** `O(k)` recursion depth (excluding output), plus output storage

## Common Mistakes

- Forgetting to sort choices inside braces, causing non-lexicographic result.
- Including commas as choices during parsing.
- Not backtracking (`path.pop()`), which corrupts subsequent paths.

## Related Problems

- [LC 17: Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)
- [LC 784: Letter Case Permutation](https://leetcode.com/problems/letter-case-permutation/)
- [LC 1096: Brace Expansion II](https://leetcode.com/problems/brace-expansion-ii/)
