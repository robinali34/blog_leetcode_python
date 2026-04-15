---
layout: post
title: "[Easy] 893. Groups of Special-Equivalent Strings"
date: 2026-02-15 00:00:00 -0700
categories: [leetcode, easy, string, hash]
tags: [leetcode, easy, string, hash, canonical-form]
permalink: /2026/02/15/easy-893-groups-of-special-equivalent-strings/
---

# [Easy] 893. Groups of Special-Equivalent Strings

## Problem Statement

Two strings are **special-equivalent** if you can swap characters at even indices among themselves and swap characters at odd indices among themselves, any number of times. Return the number of groups of special-equivalent strings.

## Examples

**Example 1:**

```
Input: words = ["abcd","cdab","cbad","xyzz","zzxy","zzyx"]
Output: 3
Explanation: Groups are ["abcd","cdab","cbad"], ["xyzz","zzxy"], ["zzyx"].
```

**Example 2:**

```
Input: words = ["abc","acb","bac","bca","cab","cba"]
Output: 3
```

## Constraints

- `1 <= words.length <= 1000`
- `1 <= words[i].length <= 20`
- `words[i]` consist of lowercase English letters
- All `words[i]` have the same length

## Clarification Questions

1. **Same length**: All words same length? (Assumption: Yes per constraints.)
2. **Group definition**: Two strings in same group iff they are special-equivalent? (Assumption: Yes.)
3. **Output**: Number of distinct groups? (Assumption: Yes.)
4. **Even/odd**: 0-based indexing for even/odd? (Assumption: Yes.)

## Interview Deduction Process (20 minutes)

**Step 1: Brute-force (5 min)** — For each pair, check if special-equivalent by trying swaps. Too slow — O(n²) pairs and expensive equivalence check.

**Step 2: Canonical form (7 min)** — Two strings are special-equivalent iff they have the same sorted even-index characters and same sorted odd-index characters. So canonical form = (sorted(even), sorted(odd)); group by this. O(n * L log L) where L is word length.

**Step 3: Optimized (8 min)** — Same idea; use tuple of sorted even chars and sorted odd chars as key. Count distinct keys. Handle length 1 (even and odd sets).

## Solution Approach

### Key Insights

Swapping within even positions and within odd positions means:

- **Order inside even positions doesn't matter**
- **Order inside odd positions doesn't matter**

So what actually matters is:
- The **multiset** of even-index characters
- The **multiset** of odd-index characters

Two strings are equivalent if and only if:

```
sorted(even chars) == sorted(even chars)
AND
sorted(odd chars) == sorted(odd chars)
```

### Canonical Form

For each word, build a **signature**:
1. Extract even-index characters
2. Extract odd-index characters
3. Sort both
4. Concatenate with a separator

Example: `"abcd"` -- even: `ac`, odd: `bd` -- signature: `"ac|bd"`

All strings with the same signature belong to one group. The answer is the number of distinct signatures.

### Formal View

Each string defines a pair `(E_multiset, O_multiset)`. Swaps only permute within E and within O. So equivalence class = identical pair of multisets. This is a classic **"group by canonical representation under allowed transformations"** pattern, similar to Group Anagrams (LC 49).

## Approach 1: Sort-Based Signature -- $O(nk \log k)$

For each word, sort even-index and odd-index characters separately, concatenate into a key, and insert into a set.

{% raw %}
```python
class Solution:
    def numSpecialEquivGroups(self, words):
        groups = set()
        
        for w in words:
            even = []
            odd = []
            
            for i in range(len(w)):
                if i % 2 == 0:
                    even.append(w[i])
                else:
                    odd.append(w[i])
            
            even.sort()
            odd.sort()
            
            key = "".join(even) + "|" + "".join(odd)
            groups.add(key)
        
        return len(groups)class Solution:
    def numSpecialEquivGroups(self, words):
        groups = set()
        
        for w in words:
            even = []
            odd = []
            
            for i in range(len(w)):
                if i % 2 == 0:
                    even.append(w[i])
                else:
                    odd.append(w[i])
            
            even.sort()
            odd.sort()
            
            key = "".join(even) + "|" + "".join(odd)
            groups.add(key)
        
        return len(groups)

```
{% endraw %}

**Time**: $O(nk \log k)$ -- sorting twice per word
**Space**: $O(nk)$

## Approach 2: Frequency Count -- $O(nk)$

Since characters are lowercase letters (only 26), we can avoid sorting by counting character frequencies instead.

{% raw %}
```python
class Solution:
    def numSpecialEquivGroups(self, words):
        groups = set()
        
        for w in words:
            even = [0] * 26
            odd = [0] * 26
            
            for i in range(len(w)):
                if i % 2 == 0:
                    even[ord(w[i]) - ord('a')] += 1
                else:
                    odd[ord(w[i]) - ord('a')] += 1
            
            key = []
            for i in range(26):
                key.append(str(even[i]))
                key.append("#")
            
            for i in range(26):
                key.append(str(odd[i]))
                key.append("#")
            
            groups.add("".join(key))
        
        return len(groups)
```
{% endraw %}

**Time**: $O(nk)$
**Space**: $O(nk)$

## Common Mistakes

- Only sorting the whole string (ignores even/odd split)
- Forgetting the parity split entirely
- Not using a separator in the key (causes hash collisions, e.g., counts `12` vs `1` + `2`)
- Using `vector<int>` as key without a custom hash

## Key Takeaways

This problem tests:
- **Canonical representation** -- reduce equivalence to a signature
- **Parity-based partitioning** -- even vs odd index awareness
- **Frequency counting** as an alternative to sorting for small alphabets

## Related Problems

- [49. Group Anagrams](https://leetcode.com/problems/group-anagrams/) -- group by sorted canonical form
- [205. Isomorphic Strings](https://leetcode.com/problems/isomorphic-strings/) -- transformation invariant

## Template Reference

- [Arrays & Strings](/blog_leetcode/posts/2025-10-29-leetcode-templates-arrays-strings/)
