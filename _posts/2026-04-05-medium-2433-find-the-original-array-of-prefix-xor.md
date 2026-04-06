---
layout: post
title: "2433. Find The Original Array of Prefix Xor"
date: 2026-04-05 00:00:00 -0700
categories: [leetcode, medium, array, bit-manipulation]
tags: [leetcode, medium, xor, prefix]
permalink: /2026/04/05/medium-2433-find-the-original-array-of-prefix-xor/
---

# 2433. Find The Original Array of Prefix Xor

## Problem Statement

You are given an integer array `pref` of size `n`. Find and return the array `arr` of size `n` such that:

`pref[i] = arr[0] ^ arr[1] ^ … ^ arr[i]`

for all `0 <= i < n`.

It is guaranteed that the answer exists and is unique.

## Examples

**Example 1:**

```python
Input: pref = [5,2,0,3,1]
Output: [5,7,2,3,2]
```

**Example 2:**

```python
Input: pref = [13]
Output: [13]
```

## Constraints

- `1 <= pref.length <= 10^5`
- `0 <= pref[i] <= 10^6`

## Analysis

Prefix XOR:

- `pref[i] = pref[i-1] ^ arr[i]` for `i >= 1`

Since XOR is its own inverse (`x ^ x = 0`):

`arr[i] = pref[i] ^ pref[i-1]` for `i >= 1`, and `arr[0] = pref[0]`.

In-place variant: walk **backwards** and set `pref[i] ^= pref[i-1]` so `pref[i]` becomes `arr[i]`.

## Solution Option 1: New array

```python
from typing import List


class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        n = len(pref)
        arr = [pref[0]]
        for i in range(1, n):
            arr.append(pref[i] ^ pref[i - 1])
        return arr
```

## Solution Option 2: In-place on `pref`

```python
from typing import List


class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        n = len(pref)
        for i in range(n - 1, 0, -1):
            pref[i] ^= pref[i - 1]
        return pref
```

After the loop, `pref[0]` is unchanged and equals `arr[0]`; each `pref[i]` for `i > 0` has been XORed with the previous prefix value to yield `arr[i]`.

## Complexity

- **Time:** O(n)
- **Space:** O(n) for Option 1; O(1) extra for Option 2 (modifies input)

## Related Problems

- [LC 1310: XOR Queries of a Subarray](https://leetcode.com/problems/xor-queries-of-a-subarray/)
- [LC 1486: XOR Operation in an Array](https://leetcode.com/problems/xor-operation-in-an-array/)
