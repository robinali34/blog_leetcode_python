---
layout: post
title: "523. Continuous Subarray Sum"
date: 2026-03-04 00:00:00 -0700
categories: [leetcode, medium, array, prefix-sum, hash-map]
tags: [leetcode, medium, array, prefix-sum, hash-map, math]
permalink: /2026/03/04/medium-523-continuous-subarray-sum/
---

# 523. Continuous Subarray Sum

## Problem Statement

Given an integer array `nums` and an integer `k`, return `True` if `nums` has a **continuous subarray** of length at least **2** whose elements sum up to a multiple of `k`, or `False` otherwise.

Formally, find `i < j` such that:

```text
sum(nums[i..j]) % k == 0
```

with `(j - i + 1) >= 2`.

If `k == 0`, then we are looking for a continuous subarray of length at least 2 whose sum is exactly 0.

## Examples

**Example 1:**

```python
Input: nums = [23, 2, 4, 6, 7], k = 6
Output: True
Explanation: [2, 4] has sum 6, which is a multiple of 6.
```

**Example 2:**

```python
Input: nums = [23, 2, 6, 4, 7], k = 6
Output: True
Explanation: [23, 2, 6, 4, 7] has sum 42, which is a multiple of 6.
```

**Example 3:**

```python
Input: nums = [23, 2, 6, 4, 7], k = 13
Output: False
```

## Constraints

- `1 <= nums.length <= 10^5`
- `0 <= nums[i] <= 10^9`
- `-10^9 <= k <= 10^9`

## Clarification Questions

1. **Length requirement**: Subarray must have length **at least 2**, correct?  
   **Assumption**: Yes — single-element subarrays do not count.
2. **k can be zero or negative**: Do we need to handle `k == 0` and negative `k`?  
   **Assumption**: Yes — treat `k == 0` as a special case; for negative `k`, only the absolute value matters in modulo.
3. **Empty subarray**: Are empty subarrays allowed?  
   **Assumption**: No — we only consider non-empty continuous subarrays.

## Interview Deduction Process (20 minutes)

**Step 1: Brute force idea (5 min)**  
Check all subarrays of length ≥ 2, compute sums, and check if divisible by `k`.  
Time complexity: \(O(n^2)\) — too slow for \(n = 10^5\).

**Step 2: Prefix sums & mod (7 min)**  
Let `prefix[i]` be the sum of the first `i` elements.  
For subarray `nums[i..j]`:

```text
sum(nums[i..j]) = prefix[j + 1] - prefix[i]
```

We want:

```text
(prefix[j + 1] - prefix[i]) % k == 0
⇒ prefix[j + 1] % k == prefix[i] % k
```

So we just need to find **two prefix sums** with the **same mod** value, and the distance between their indices must be at least 2 (since subarray length ≥ 2).

**Step 3: One-pass tracking (8 min)**  
Instead of storing all prefix sums, we track:
- A set (or map) of **previous modulo values**.
- The modulo at each step and the previous modulo from the last position.

This variant (using a set and `previous_mod`) ensures:
- We only add a modulo to the set **after** moving at least one step ahead, ensuring subarray length ≥ 2.

## Solution Approach

We maintain:

- `running_sum` — prefix sum as we iterate.
- `hash_set` — set of prefix-sum modulo `k` values we have seen **at least one index before the current**.
- `previous_mod` — modulo of the prefix sum up to the previous element.

Algorithm:

1. Handle `k == 0` separately: look for two consecutive zeros, because sum must be exactly 0 and length ≥ 2.
2. Normalize `k` as positive (e.g., `k = abs(k)`).
3. Initialize:
   - `hash_set = set()`
   - `running_sum = 0`
   - `previous_mod = 0`
4. For each `num` in `nums`:
   - Update `running_sum += num`.
   - Compute `mod = running_sum % k`.
   - If `mod` is already in `hash_set`, we have a previous prefix with same model value at least 2 indices apart → return `True`.
   - Add `previous_mod` to the set (so next step can use it).
   - Set `previous_mod = mod`.
5. If we finish loop without finding such a pair, return `False`.

### Key Insights

1. **Equal prefix-sum mod means subarray sum is multiple of k**  
   If `prefix[a] % k == prefix[b] % k`, then the subarray sum between them is divisible by `k`.

2. **Length ≥ 2 via delayed insert**  
   By adding `previous_mod` to the set only **after** processing the current element, we ensure any match corresponds to a subarray of length at least 2.

3. **Special case `k == 0`**  
   We cannot take modulo 0, so we directly look for any pair of consecutive zeros.

## Python Solution

```python
from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)

        # Special case for k == 0: look for at least two consecutive zeros
        if k == 0:
            for i in range(n - 1):
                if nums[i] == 0 and nums[i + 1] == 0:
                    return True
            return False

        k = abs(k)
        hash_set = set()
        running_sum = 0
        previous_mod = 0

        for num in nums:
            running_sum += num
            mod = running_sum % k

            if mod in hash_set:
                return True

            hash_set.add(previous_mod)
            previous_mod = mod

        return False
```

## Algorithm Explanation

- `running_sum` accumulates the total from the start.
- `mod = running_sum % k` is the current prefix sum modulo `k`.
- If we have seen this `mod` value before (in `hash_set`), then there exists an earlier prefix with the same modulo:

  ```text
  prefix[i] % k == prefix[j] % k  ⇒  sum(nums[i..j-1]) is multiple of k
  ```

- The use of `previous_mod` ensures we only add the modulo from the **previous** index into the set, enforcing that the subarray length is at least 2.

For `k == 0`, a subarray sum must be exactly 0. The simplest way for non-negative `nums` is to look for two consecutive zeros, which ensures a length-2 subarray with sum 0.

## Complexity Analysis

- **Time Complexity**: \(O(n)\), where \(n = \text{len}(nums)\) — single pass through the array.
- **Space Complexity**: \(O(\min(n, |k|))\) in worst case for the set of mod values, practically \(O(n)\).

## Edge Cases

- `k == 0` and no two consecutive zeros → must return `False`.
- All numbers are multiples of `k` — many valid subarrays exist.
- Very large `k` (larger than sum of all numbers) — only subarray sum 0 (from zeros) can work.
- Negative `k` — `abs(k)` works because divisibility does not depend on the sign.

## Common Mistakes

- Modulo by zero when `k == 0` — must handle this case specially.
- Forgetting the **length ≥ 2** requirement (e.g., treating a single element that is multiple of `k` as valid).
- Using a set of all `mod`s seen so far **before** enforcing distance, which can accidentally count subarrays of length 1.
- Not normalizing negative `k`, which can lead to confusing modulo behavior.

## Related Problems

- [LC 560: Subarray Sum Equals K](/2026/02/01/medium-560-subarray-sum-equals-k/) — Similar prefix-sum + hash-map pattern without modulo.
- [LC 974: Subarray Sums Divisible by K](https://leetcode.com/problems/subarray-sums-divisible-by-k/) — Count number of subarrays (any length) whose sum is divisible by `k` using prefix-sum modulo and counts map.

