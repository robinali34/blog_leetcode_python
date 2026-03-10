---
layout: post
title: "1202. Smallest String With Swaps"
date: 2026-03-09 00:00:00 -0700
categories: [leetcode, medium, string, union-find, graph]
tags: [leetcode, medium, string, dsu, connected-components]
permalink: /2026/03/09/medium-1202-smallest-string-with-swaps/
---

# 1202. Smallest String With Swaps

## Problem Statement

You are given a string `s` and an array of pairs of indices `pairs`, where `pairs[i] = [a, b]` indicates that you can swap the characters at indices `a` and `b` in the string.

You can swap the characters at any pair of indices in `pairs` **any number of times**.

Return the **lexicographically smallest** string that `s` can be changed to after any number of swaps.

## Examples

**Example 1:**

```python
Input: s = "dcab", pairs = [[0,3],[1,2]]
Output: "bacd"
# Swap s[0] and s[3]: "dcab" -> "bcad"
# Swap s[1] and s[2]: "bcad" -> "bacd"
# No further swaps yield a smaller string.
```

**Example 2:**

```python
Input: s = "dcab", pairs = [[0,3],[1,2],[0,2]]
Output: "abcd"
# Indices 0,1,2,3 are all connected; we can arrange them arbitrarily.
# Sorted chars: a,b,c,d at sorted indices 0,1,2,3 -> "abcd"
```

**Example 3:**

```python
Input: s = "cba", pairs = [[0,1],[1,2]]
Output: "abc"
# 0-1-2 connected; sort chars and place at 0,1,2.
```

## Constraints

- `1 <= s.length <= 10^5`
- `0 <= pairs.length <= 10^5`
- `0 <= pairs[i][0], pairs[i][1] < s.length`
- `s` contains only lowercase English letters.

## Clarification Questions

1. **Unlimited swaps**: We can use any pair in `pairs` any number of times?  
   **Assumption**: Yes — so indices in the same connected component can be rearranged arbitrarily.
2. **Transitive**: If we can swap (a,b) and (b,c), can we effectively swap (a,c)?  
   **Assumption**: Yes — connectivity is transitive.
3. **Lexicographically smallest**: Standard dictionary order.  
   **Assumption**: Yes.

## Interview Deduction Process (20 minutes)

**Step 1: Connectivity (5 min)**  
Indices that can be swapped (directly or transitively) form connected components. Within each component, we can achieve any permutation of the characters at those indices (by repeated swaps).

**Step 2: Greedy per component (10 min)**  
To get the lexicographically smallest string, we want the smallest character at the smallest index, etc. So for each component: collect the indices and the characters; sort them; place the smallest char at the smallest index, second smallest at second smallest index, etc.

**Step 3: DSU for components (5 min)**  
Use union-find to group indices by connectivity. For each index, find its root; group indices by root. Then for each group, sort indices and chars, and assign.

## Solution Approach

**DSU + greedy sort:** Treat pairs as edges; indices that are connected (same component) can be rearranged arbitrarily. For each component, collect the indices and their characters. Sort the indices and sort the characters in that component. Place the sorted characters at the sorted indices in order. This gives the lexicographically smallest arrangement for each component.

### Key Insights

1. **Connected components** — Indices in the same component can be permuted arbitrarily. DSU groups them.
2. **Greedy per component** — Lexicographically smallest: smallest char at smallest index. So sort indices and chars within each component, then map in order.
3. **No cross-component swaps** — Characters in different components stay in their index ranges; we optimize each component independently.

## Python Solution

### DSU + sort per component (O(n log n + E·α(n)) time)

```python
from collections import defaultdict
from typing import List


class DSU:
    def __init__(self, n: int) -> None:
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # path compression
        return self.parent[x]

    def unite(self, x: int, y: int) -> bool:
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        self.rank[px] += self.rank[py]
        return True


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        dsu = DSU(n)

        for x, y in pairs:
            dsu.unite(x, y)

        groups: dict[int, list[int]] = defaultdict(list)
        for i in range(n):
            groups[dsu.find(i)].append(i)

        res = list(s)
        for idxs in groups.values():
            chars = [s[i] for i in idxs]
            chars.sort()
            idxs.sort()
            for i in range(len(idxs)):
                res[idxs[i]] = chars[i]
        return "".join(res)
```

## Algorithm Explanation

We build a DSU from the index pairs: each pair connects two indices. After processing all pairs, indices in the same component can be swapped arbitrarily. We group indices by their root (find). For each group, we collect the indices and the characters at those indices. We sort both: indices in ascending order and characters in ascending order. We then place the smallest character at the smallest index, the second smallest at the second smallest index, etc. This gives the lexicographically smallest string possible for that component. The final string is built by concatenating the result array.

## Complexity Analysis

- **Time**: O(n log n + E·α(n)) — DSU operations: O(E·α(n)); grouping: O(n); per component: sort indices and chars, worst case O(n log n) total.
- **Space**: O(n) for the DSU, groups, and result.

## Edge Cases

- **No pairs** — Each index is its own component; no swaps possible; return `s` unchanged.
- **All indices connected** — One component; sort all chars and place at 0,1,...,n-1.
- **Empty string** — Constraints say length ≥ 1.

## Common Mistakes

- **Forgetting to sort indices** — We must place the smallest char at the smallest index, so we need both sorted and aligned.
- **Mutating `idxs`** — `idxs.sort()` sorts in place; we iterate over the same list. We assign to `res[idxs[i]]` so we need the sorted order; this is correct.
- **In-place mutation of `idxs`** — The loop `for idxs in groups.values()` gives us a list; we sort it. When we iterate `for i in range(len(idxs))`, we use the sorted indices. Correct.

## Related Problems

- [LC 684: Redundant Connection](https://leetcode.com/problems/redundant-connection/) — DSU to detect cycles.
- [LC 1584: Min Cost to Connect All Points](/2026/03/08/medium-1584-min-cost-to-connect-all-points/) — DSU for MST.
- [LC 1319: Number of Operations to Make Network Connected](https://leetcode.com/problems/number-of-operations-to-make-network-connected/) — Count components.
- [LC 721: Accounts Merge](https://leetcode.com/problems/accounts-merge/) — DSU to merge accounts by email.
