---
layout: post
title: "[Medium] 2539. Count the Number of Good Subsequences"
date: 2026-04-19 00:00:00 -0700
categories: [leetcode, medium, string, combinatorics, math, hash-map]
permalink: /2026/04/19/medium-2539-count-the-number-of-good-subsequences/
tags: [leetcode, medium, string, combinatorics, frequency, modular-arithmetic, hash-map]
---

# [Medium] 2539. Count the Number of Good Subsequences

Given a string `s`, count how many **non-empty** subsequences are **good**.

A subsequence is good if **every character that appears in it appears the same number of times**.

Examples:

- `"aabb"` — good counts include patterns where each present letter appears twice (e.g. two `a`s and two `b`s).
- `"aab"` — not good if both `a` and `b` appear but with different frequencies (e.g. two `a`s and one `b`).

Return the answer modulo `10^9 + 7`.

## Problem summary

Brute force over subsequences is hopeless. The trick is to **count combinatorially using character frequencies**.

## Key insight

Instead of generating subsequences, **fix a target frequency `k`**, and count subsequences where **every chosen character appears exactly `k` times** (and you may omit any letter entirely).

## Step-by-step

1. **Frequency map:** `freq[c] =` number of occurrences of `c` in `s`.

2. **For a fixed `k`:** For each character with `freq[c] ≥ k`, you may either **skip** that letter or **take exactly `k` copies** of it. The number of ways to choose those `k` copies from `freq[c]` positions is `C(freq[c], k)`.

   Independently across letters, the contribution for that letter is `(1 + C(freq[c], k))`: the `1` is “do not include this letter,” and `C(freq[c], k)` is “include it exactly `k` times.”

3. **Multiply and subtract empty:** The product over all letters gives all combinations including “choose nothing from everyone.” Subtract `1` to remove the empty subsequence:

   `ways(k) = ∏_{c : freq[c] ≥ k} (1 + C(freq[c], k)) - 1`

4. **Sum over `k`:** Let `max_f = max(freq.values())`. The answer is:

   `answer = Σ_{k=1}^{max_f} ways(k)` (all modulo `MOD`).

### Group characters by frequency (same formula, less redundancy)

Letters that share the same total count `f` behave identically for a fixed `k`. Let `freqCount[f]` be how many distinct characters have frequency `f` in `s` (i.e. `Counter(freq.values())`).

Then the product over characters becomes a product over distinct frequencies:

`ways(k) = ∏_{f ≥ k} (1 + C(f, k))^{freqCount[f]} - 1`

The inner loop runs over **distinct frequency values** (at most the alphabet size) and uses modular exponentiation instead of repeating the same factor once per letter.

## Complexity (all correct variants)

- **Time:** `O(n)` to scan the string and build counters; plus preprocessing for binomials; plus roughly **`O(max_f × 26)`** for the double loop over `k` and letters (or over distinct frequencies — still bounded by a constant alphabet).
- **Space:** dominated by how you store **`C(n, k)`**: **`Θ(max_f²)`** for a full Pascal table vs **`Θ(max_f)`** for factorial / inverse factorial arrays.

## Approaches and trade-offs

Two independent choices:

1. **How you compute `C(n, k) mod MOD`** — Pascal row/column DP vs factorials + modular inverse.
2. **How you multiply letter contributions** — one factor per **character** vs one factor per **distinct frequency** (with an exponent when several letters share the same count).

| Approach | Precompute `C` | Inner loop (per `k`) | Space | Notes |
| -------- | ---------------- | ---------------------- | ----- | ----- |
| Pascal triangle | `O(max_f²)` time, `O(max_f²)` space | `O(26)` chars | **Huge** if `max_f ≈ 10⁴` | Easy to write; **impractical** here. |
| Factorial + inverse | `O(max_f)` time, `O(max_f)` space | `O(26)` over `freq` | **Linear in `max_f`** | Standard for prime modulus. |
| Factorial + `freq_count` + `pow` | same as above | `O(F)` distinct freqs, `F ≤ 26` | same | Same math; **cleaner** when many letters share one frequency. |

### 1) Pascal’s triangle (simple, wrong scale for large `max_f`)

```python
from collections import Counter

MOD = 10**9 + 7


class Solution:
    def countGoodSubsequences(self, s: str) -> int:
        freq = Counter(s)
        max_f = max(freq.values())

        n = max_f
        C = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            C[i][0] = 1
            for j in range(1, i + 1):
                C[i][j] = (C[i - 1][j - 1] + C[i - 1][j]) % MOD

        result = 0
        for k in range(1, max_f + 1):
            ways = 1
            for c in freq:
                if freq[c] >= k:
                    ways = ways * (1 + C[freq[c]][k]) % MOD
            ways = (ways - 1) % MOD
            result = (result + ways) % MOD
        return result
```

**Trade-off:** No modular inverses; very readable. But building **`(max_f + 1)²`** entries is **`O(max_f²)` memory** — with `max_f` up to `10⁴`, that is on the order of **10⁸ cells** (and similar time), which is **not acceptable** for this problem’s constraints.

### 2) Factorials + Fermat inverse (per character)

```python
from collections import Counter

MOD = 10**9 + 7


class Solution:
    def countGoodSubsequences(self, s: str) -> int:
        freq = Counter(s)
        max_f = max(freq.values())

        fact = [1] * (max_f + 1)
        invfact = [1] * (max_f + 1)
        for i in range(1, max_f + 1):
            fact[i] = fact[i - 1] * i % MOD

        invfact[max_f] = pow(fact[max_f], MOD - 2, MOD)
        for i in range(max_f - 1, -1, -1):
            invfact[i] = invfact[i + 1] * (i + 1) % MOD

        def comb(f: int, k: int) -> int:
            return fact[f] * invfact[k] % MOD * invfact[f - k] % MOD

        rtn = 0
        for k in range(1, max_f + 1):
            ways = 1
            for f in freq.values():
                if f >= k:
                    ways = ways * (1 + comb(f, k)) % MOD
            ways = (ways - 1) % MOD
            rtn = (rtn + ways) % MOD
        return rtn
```

**Trade-off:** **`O(max_f)`** extra space and **`O(max_f)`** preprocessing; each `comb` in **`O(1)`**. Requires **`MOD` prime** (here it is). Inner loop is one factor per **letter that appears** (at most `26`).

### 3) Same as (2), but group identical frequencies (`freq_count` + `pow`)

If you build `freq_count = Counter(freq.values())`, you must multiply **`(1 + C(f, k))` once per distinct frequency `f`**, raised to the number of letters with that frequency — not by iterating `freq.values()` again (that would repeat the same `f` many times and overcount).

```python
from collections import Counter

MOD = 10**9 + 7


class Solution:
    def countGoodSubsequences(self, s: str) -> int:
        freq = Counter(s)
        freq_count = Counter(freq.values())
        max_f = max(freq_count)

        fact = [1] * (max_f + 1)
        invfact = [1] * (max_f + 1)
        for i in range(1, max_f + 1):
            fact[i] = fact[i - 1] * i % MOD

        invfact[max_f] = pow(fact[max_f], MOD - 2, MOD)
        for i in range(max_f - 1, -1, -1):
            invfact[i] = invfact[i + 1] * (i + 1) % MOD

        def comb(f: int, k: int) -> int:
            return fact[f] * invfact[k] % MOD * invfact[f - k] % MOD

        rtn = 0
        for k in range(1, max_f + 1):
            ways = 1
            for f, cnt in freq_count.items():
                if f >= k:
                    ways = ways * pow(1 + comb(f, k), cnt, MOD) % MOD
            ways = (ways - 1) % MOD
            rtn = (rtn + ways) % MOD
        return rtn
```

**Trade-off:** Same asymptotic cost as (2) for this alphabet size; **clearer algebra** and fewer redundant multiplications when several characters share one frequency. **Prefer this version** for submissions: correct grouping, good constants, and **`O(max_f)`** precomputation.

## Takeaway

For **large `max_f`**, avoid a dense **`O(max_f²)`** Pascal table; use **factorials + inverse factorials** modulo a prime. Whether you loop **`freq.values()`** or **`freq_count` + `pow`** is the same big‑`O` here, but **`freq_count`** matches the grouped formula directly and stays tidy when many letters share one frequency.
