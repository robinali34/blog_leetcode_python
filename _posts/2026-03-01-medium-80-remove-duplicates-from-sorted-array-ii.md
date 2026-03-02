---
layout: post
title: "80. Remove Duplicates from Sorted Array II"
date: 2026-03-01 00:00:00 -0700
categories: [leetcode, medium, array, two-pointers]
tags: [leetcode, medium, array, two-pointers, in-place]
permalink: /2026/03/01/medium-80-remove-duplicates-from-sorted-array-ii/
---

# 80. Remove Duplicates from Sorted Array II

## Problem Statement

Given a sorted integer array `nums`, remove duplicates **in-place** such that each element appears **at most twice**, and return the **new length**.

You must do this with:
- \(O(n)\) time complexity
- \(O(1)\) extra space

The relative order of the kept elements should be maintained.

## Examples

**Example 1:**

```python
Input:  nums = [1,1,1,2,2,3]
Output: 5
Array becomes: [1,1,2,2,3,_]
```

**Example 2:**

```python
Input:  nums = [0,0,1,1,1,1,2,3,3]
Output: 7
Array becomes: [0,0,1,1,2,3,3,_,_]
```

## Constraints

- `1 <= nums.length <= 3 * 10^4`
- `-10^4 <= nums[i] <= 10^4`
- `nums` is sorted in **non-decreasing** order

## Clarification Questions

1. **In-place**: We can overwrite elements in `nums`, but cannot use another array?  
2. **Return value**: We return the **new length** `k`, and LeetCode checks the first `k` elements only?  
3. **Order**: The order of the remaining elements must be kept the same as in the original array?  
4. **Sorted property**: The array is always sorted in non-decreasing order (no need to re-sort)?  
5. **Maximum duplicates**: Exactly “at most 2” occurrences are allowed for each value (not 1, not 3)?  

## Interview Deduction Process (20 minutes)

**Step 1: Brute-force idea (5 min)**  
Use a frequency map, then rebuild the array with at most 2 copies of each number.  
Problem: uses extra space and is not truly in-place in the intended sense.

**Step 2: Two-pointers intuition (7 min)**  
Because `nums` is **sorted**, all duplicates are consecutive.  
We can maintain a **write pointer** `k` and iterate through the array with a **read pointer**.  
We only write a number if adding it would **not** violate the “at most two copies” rule.

**Step 3: Optimized rule (8 min)**  
Key trick: instead of counting explicitly, rely on the already-written part of the array.  
When deciding whether to write the current number `num`:
- If `k < 2`, always keep (we haven’t even written 2 elements yet).
- Otherwise, compare `num` with `nums[k - 2]`.  
  - If `num == nums[k - 2]`, we already have at least 2 copies — **skip**.  
  - Otherwise, it is safe to **write**.

## Solution Approach

We use a **single pass** with a **write pointer**:

- Let `k` be the index where we **write** the next valid element.
- Iterate through each `num` in `nums`:
  - If `k < 2`, we always keep the element.
  - If `k >= 2`, we only keep `num` if it is **different** from `nums[k - 2]`.
- After the loop, `k` is the new length, and the first `k` positions of `nums` hold the answer.

### Key Insights

1. **Sorted array ⇒ local comparison is enough**  
   Since equal elements are consecutive, to know whether we already kept two copies, we only need to look **two positions back**.

2. **No explicit counting**  
   We don’t maintain a frequency counter. The already-written prefix of `nums` implicitly encodes how many times we have kept each value.

3. **General pattern**  
   If we want to allow at most `m` duplicates, the general condition becomes:  
   `if k < m or nums[k - m] != num: keep it`.

## Python Solution

### Implementation

```python
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0

        for num in nums:
            # Keep if we have written fewer than 2 elements so far,
            # or if this num is different from the element at k - 2
            if k < 2 or nums[k - 2] != num:
                nums[k] = num
                k += 1

        return k
```

### Alternative Index-Based Version

Same idea, but using indices explicitly:

```python
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n

        idx = 2  # index to write the next allowed element

        for i in range(2, n):
            if nums[i] != nums[idx - 2]:
                nums[idx] = nums[i]
                idx += 1

        return idx
```

## Algorithm Explanation

We maintain a **prefix** `nums[:k]` that always satisfies the rule:  
> Every value appears at most twice.

For each new `num`:
- If `k < 2`, the prefix is too short to break the rule, so we write it.
- If `k >= 2`, then:
  - If `num == nums[k - 2]`, we would end up with three identical numbers at indices `k - 2`, `k - 1`, `k`. We must **skip**.
  - If `num != nums[k - 2]`, we can safely write it at `nums[k]`.

Because the array is sorted, if we see the same value again, it must appear right after the previous occurrences, so this local check is sufficient.

## Example Walkthrough

Take `nums = [1,1,1,2,2,3]`.

| Step | num | k (before) | nums[k-2] (if k>=2) | Keep? | nums (prefix shown) |
|------|-----|-----------:|---------------------|-------|----------------------|
| 1    | 1   | 0          | -                   | yes   | [1]                  |
| 2    | 1   | 1          | -                   | yes   | [1,1]                |
| 3    | 1   | 2          | 1                   | no    | [1,1]                |
| 4    | 2   | 2          | 1                   | yes   | [1,1,2]              |
| 5    | 2   | 3          | 1                   | yes   | [1,1,2,2]            |
| 6    | 3   | 4          | 2                   | yes   | [1,1,2,2,3]          |

Final `k = 5`, and the array is `[1,1,2,2,3, _]`.

## Complexity Analysis

- **Time Complexity**: \(O(n)\), where \(n\) is the length of `nums`, since we scan the array once.
- **Space Complexity**: \(O(1)\), as we only use a few integer variables and mutate the array in-place.

## Edge Cases

- Arrays of length `0`, `1`, or `2` — already valid, just return `len(nums)`.
- All elements identical, e.g. `[1,1,1,1]` ⇒ `[1,1,_,_]`, return `2`.
- No duplicates at all, e.g. `[1,2,3,4]` ⇒ unchanged, return `4`.
- Negative values (still sorted), e.g. `[-1,-1,-1,0,0,1]`.

## Common Mistakes

- **Counting occurrences explicitly** for each value and doing extra passes instead of a single-pass two-pointer solution.
- **Comparing only with the previous element** (index `k - 1`) rather than `k - 2`, which fails to enforce “at most two” properly.
- **Using extra arrays or data structures**, which breaks the intended in-place constraint.
- Forgetting to handle small arrays (length `< 2`) cleanly.

## Related Problems

- [LC 26: Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) — Allow at most 1 occurrence.
- [LC 27: Remove Element](https://leetcode.com/problems/remove-element/) — Remove all occurrences of a given value in-place.
- [LC 283: Move Zeroes](https://leetcode.com/problems/move-zeroes/) — Another in-place two-pointer array rewrite.

