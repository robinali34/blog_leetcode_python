---
layout: post
title: "LC 344: Reverse String"
date: 2025-10-29 00:00:00 -0700
categories: leetcode easy two-pointers string
permalink: /posts/2025-10-29-easy-344-reverse-string/
tags: [leetcode, easy, two-pointers, string]
---

# LC 344: Reverse String

Reverse the array of characters in-place using O(1) extra memory.

## Approach

Two pointers at the ends swap characters and converge toward the center.
- Initialize `left=0`, `right=n-1`
- While `left < right`, swap `s[left]` with `s[right]`, then move inward

## Python Solution

```python
class Solution:
    def reverseString(self, s: list[str]) -> None:
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
```

## Complexity

- Time: O(n)
- Space: O(1)
