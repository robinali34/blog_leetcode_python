---
layout: post
title: "[Medium] 365. Water and Jug Problem"
date: 2026-03-14 00:00:00 -0700
categories: [leetcode, medium, math, number-theory]
tags: [leetcode, medium, gcd, bezout]
permalink: /2026/03/14/medium-365-water-and-jug-problem/
---

# [Medium] 365. Water and Jug Problem

## Problem Statement

You are given two jugs with capacities `jug1Capacity` and `jug2Capacity` (in liters). You have an unlimited water supply.

Determine whether it is possible to measure exactly `targetCapacity` liters using these two jugs.

Operations allowed:

- **Fill** either jug completely.
- **Empty** either jug.
- **Pour** water from one jug into the other until the source is empty or the destination is full.

You may assume that both jugs are initially empty. The measured amount can be in either jug or in both jugs combined.

## Examples

**Example 1:**

```python
Input: jug1Capacity = 3, jug2Capacity = 5, targetCapacity = 4
Output: True
# Fill 5, pour into 3 → leaves 2 in 5. Empty 3, pour 2 into 3. Fill 5, pour 1 into 3 → 4 in 5.
```

**Example 2:**

```python
Input: jug1Capacity = 2, jug2Capacity = 6, targetCapacity = 5
Output: False
# We can only get amounts that are multiples of gcd(2,6)=2; 5 is not.
```

**Example 3:**

```python
Input: jug1Capacity = 1, jug2Capacity = 2, targetCapacity = 3
Output: True
# Fill both: 1 + 2 = 3.
```

## Constraints

- `1 <= jug1Capacity, jug2Capacity, targetCapacity <= 10^6`

## Clarification Questions

1. **Unlimited water**: We can fill from the tap any number of times?  
   **Assumption**: Yes.
2. **Target**: Can target be the sum of both jugs (e.g. 1+2=3)?  
   **Assumption**: Yes — “in either jug or in both jugs combined.”
3. **No partial marks**: We don’t have a separate measuring cup; we only use the two jugs?  
   **Assumption**: Yes.

## Interview Deduction Process (20 minutes)

**Step 1: What amounts can we get? (7 min)**  
At any time the total water in the two jugs is unchanged by pouring (we just move it). Filling adds the jug’s capacity; emptying subtracts. So the total amount we can ever have is a **linear combination** of the two capacities: \(a \cdot x + b \cdot y\) for integers \(a, b\). By Bézout’s identity, the set of such values is exactly the set of **multiples of \(\gcd(x, y)\)**.

**Step 2: Necessary and sufficient (8 min)**  
So we can measure \(z\) if and only if:
- \(z \le x + y\) (we cannot hold more than both jugs full),
- \(z \ge 0\),
- \(z\) is a multiple of \(\gcd(x, y)\) (i.e. \(z \bmod \gcd(x,y) = 0\)).

**Step 3: Edge cases (5 min)**  
If \(x = 0\) or \(y = 0\), treat separately: e.g. if both 0 then only \(z = 0\); if one is 0 then we can only get multiples of the non-zero capacity, and \(z\) must be between 0 and that capacity (or 0). The constraints say capacities \(\ge 1\), so we can assume \(x, y \ge 1\); still handle \(z = 0\) (always true).

## Solution Approach

**Number theory:** The key is that the total water we can measure is always of the form \(a \cdot x + b \cdot y\) for integers \(a, b\). So we can get \(z\) iff \(\gcd(x, y) \mid z\) and \(0 \le z \le x + y\). Use Euclidean algorithm to compute \(\gcd\); then check \(z \le x + y\) and \(z \% \gcd(x,y) == 0\) (and \(z \ge 0\)).

### Key Insights

1. **Bézout** — Any linear combination \(ax + by\) is a multiple of \(\gcd(x,y)\); and every multiple of \(\gcd(x,y)\) can be written as \(ax + by\). So measurable amounts = multiples of \(\gcd(x,y)\).
2. **Upper bound** — We can’t hold more than \(x + y\) total; so \(z \le x + y\).
3. **No BFS/DFS needed** — The problem has a closed-form condition; no need to simulate pours.

## Python Solution

### GCD check (O(log min(x,y)) time, O(1) space)

```python
class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        x, y, z = jug1Capacity, jug2Capacity, targetCapacity
        if z < 0 or z > x + y:
            return False
        if z == 0:
            return True
        g = self._gcd(x, y)
        return z % g == 0

    def _gcd(self, a: int, b: int) -> int:
        while b:
            a, b = b, a % b
        return a
```

## Algorithm Explanation

We can only ever have a total amount of water that is a linear combination of the two jug capacities; that set is the set of multiples of \(\gcd(x, y)\). So we need \(z \ge 0\), \(z \le x + y\), and \(\gcd(x, y) \mid z\). We compute \(\gcd\) with the Euclidean algorithm and check \(z \% g == 0\). If \(z == 0\), we can “measure” it by doing nothing (already true).

## Complexity Analysis

- **Time**: O(log min(x, y)) for the Euclidean algorithm.
- **Space**: O(1).

## Edge Cases

- **z == 0** — Always achievable (both jugs empty).
- **z == x + y** — Achievable (fill both jugs).
- **x or y zero** — Constraints say \(\ge 1\); if we allowed 0, then only multiples of the non-zero jug and \(z \le\) that capacity.
- **z > x + y** — Return False.

## Common Mistakes

- **Forgetting z <= x + y** — We can’t hold more than the sum of the two capacities.
- **Simulating with BFS/DFS** — Works but is overkill and can be slow for large capacities; the math solution is O(log) and sufficient.
- **z == 0** — Return True (we already have 0 liters).

## Related Problems

- [LC 780: Reaching Points](https://leetcode.com/problems/reaching-points/) — Number-theory / GCD-style reachability.
- [LC 254: Factor Combinations](https://leetcode.com/problems/factor-combinations/) — Factors and decomposition.
- [LC 858: Mirror Reflection](https://leetcode.com/problems/mirror-reflection/) — Another math/gcd-style problem.
