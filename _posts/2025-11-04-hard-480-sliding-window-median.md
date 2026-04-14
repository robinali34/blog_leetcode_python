---
layout: post
title: "[Hard] 480. Sliding Window Median"
date: 2025-11-04 21:55:29 -0800
categories: leetcode algorithm hard cpp arrays multiset sliding-window two-heaps problem-solving
permalink: /posts/2025-11-04-hard-480-sliding-window-median/
tags: [leetcode, hard, array, multiset, sliding-window, two-heaps, median]
---

# [Hard] 480. Sliding Window Median

The **median** is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle values.

- For example, for `arr = [2,3,4]`, the median is `3`.
- For example, for `arr = [2,3]`, the median is `(2 + 3) / 2 = 2.5`.

You are given an integer array `nums` and an integer `k`. There is a sliding window of size `k` which is moving from the very left of the array to the very right. You can only see the `k` numbers in the window. Each time the sliding window moves right by one position.

Return *the median array for each window in the original array*.

## Examples

**Example 1:**
```
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [1.00000,-1.00000,-1.00000,3.00000,5.00000,6.00000]
Explanation: 
Window position                Median
---------------                -----
[1  3  -1] -3  5  3  6  7        1
 1 [3  -1  -3] 5  3  6  7       -1
 1  3 [-1  -3  5] 3  6  7       -1
 1  3  -1 [-3  5  3] 6  7        3
 1  3  -1  -3 [5  3  6] 7        5
 1  3  -1  -3  5 [3  6  7]       6
```

**Example 2:**
```
Input: nums = [1,2,3,4,2,3,1,4,2], k = 3
Output: [2.00000,3.00000,3.00000,3.00000,2.00000,3.00000,2.00000]
```

## Constraints

- `1 <= k <= nums.length <= 10^5`
- `-2^31 <= nums[i] <= 2^31 - 1`

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Sliding window**: What is a sliding window? (Assumption: Contiguous subarray of size k that moves from left to right)

2. **Median calculation**: How is median calculated? (Assumption: For odd k, middle element; for even k, average of two middle elements)

3. **Return format**: What should we return? (Assumption: Array of medians - one for each window position)

4. **Window count**: How many windows are there? (Assumption: nums.length - k + 1 windows - from index 0 to nums.length - k)

5. **Time complexity**: What time complexity is expected? (Assumption: O(n log k) - maintain sorted window using balanced BST or heaps)

## Interview Deduction Process (30 minutes)

**Step 1: Brute-Force Approach (8 minutes)**

For each window position, extract the window, sort it, find the median, and add to result. This approach has O(n × k log k) time complexity: O(n) windows, each requiring O(k log k) to sort, which is too slow for large inputs.

**Step 2: Semi-Optimized Approach (10 minutes)**

Maintain a sorted data structure (like a multiset or balanced BST) for the current window. When sliding the window, remove the leftmost element and add the new rightmost element, then find the median. This reduces time to O(n log k) since each insertion/deletion takes O(log k). However, finding the median in a balanced BST requires tracking the size or using iterators, which adds complexity.

**Step 3: Optimized Solution (12 minutes)**

Use two multisets (two-heaps pattern): maintain a small multiset (for smaller half) and a large multiset (for larger half). Keep them balanced so the median is easily accessible. When sliding the window, remove the outgoing element and add the incoming element, rebalancing if needed. This achieves O(n log k) time: O(n) windows, each requiring O(log k) for insert/delete operations. The key insight is that maintaining two balanced heaps/multisets allows O(1) median access while supporting efficient insertions and deletions as the window slides.

## Solution 1: Two Multisets (Two-Heaps Pattern)

**Time Complexity:** O(n log k) - Each insertion/deletion is O(log k)  
**Space Complexity:** O(k) - Two multisets store window elements

Use a sorted window and `bisect` for insert/remove (same idea as two balanced multisets, implemented with sorted order).

```python
import bisect

class Solution:
    def medianSlidingWindow(self, nums: list[int], k: int) -> list[float]:
        window = sorted(nums[:k])

        def median() -> float:
            if k % 2 == 1:
                return float(window[k // 2])
            return (window[k // 2 - 1] + window[k // 2]) / 2.0

        res = [median()]
        for i in range(k, len(nums)):
            out = nums[i - k]
            window.pop(bisect.bisect_left(window, out))
            bisect.insort(window, nums[i])
            res.append(median())
        return res
```

## How Solution 1 Works

### Key Insight: Two-Heaps Pattern

- **`lo`**: Multiset containing smaller half, maintained in increasing order
- **`hi`**: Multiset containing larger half, maintained in increasing order
- **Balance**: Keep `lo.size() == hi.size()` (even k) or `lo.size() == hi.size() + 1` (odd k)
- **Median**: 
  - Odd k: `*prev(lo.end())` (maximum of lo)
  - Even k: `(*prev(lo.end()) + *hi.begin()) / 2.0`

### Step-by-Step Example: `nums = [1,3,-1,-3,5,3,6,7], k = 3`

| Step | i | nums[i] | Insert | lo | hi | Remove | lo | hi | Window | Median |
|------|---|---------|--------|----|----|--------|----|----|--------|--------|
| 0 | 0 | 1 | 1→lo | {1} | {} | - | {1} | {} | [1] | - |
| 1 | 1 | 3 | 3→hi | {1} | {3} | - | {1} | {3} | [1,3] | - |
| 2 | 2 | -1 | -1→lo | {-1,1} | {3} | - | {-1,1} | {3} | [-1,1,3] | 1.0 |
| 3 | 3 | -3 | -3→lo | {-3,-1,1} | {3} | 1→out | {-3,-1} | {3} | [-1,-3,3] | -1.0 |
| 4 | 4 | 5 | 5→hi | {-3,-1} | {3,5} | -1→out | {-3} | {3,5} | [-3,3,5] | -1.0 |
| 5 | 5 | 3 | 3→lo | {-3,3} | {5} | -3→out | {3} | {5} | [3,5,3] | 3.0 |
| 6 | 6 | 6 | 6→hi | {3} | {5,6} | 3→out | {5} | {6} | [5,3,6] | 5.0 |
| 7 | 7 | 7 | 7→hi | {5} | {6,7} | 3→out | {6} | {7} | [3,6,7] | 6.0 |

**Final Answer:** `[1.0, -1.0, -1.0, 3.0, 5.0, 6.0]`

### Visual Representation

```
nums = [1, 3, -1, -3, 5, 3, 6, 7]
       0  1   2    3   4  5  6  7

Step 0-2: Window [1, 3, -1]
  lo = {-1, 1}  (smaller half)
  hi = {3}       (larger half)
  Median = max(lo) = 1 (k=3 is odd)

Step 3: Window [3, -1, -3]
  lo = {-3, -1}
  hi = {3}
  Median = (max(lo) + min(hi)) / 2 = (-1 + 3) / 2 = 1
  Wait, k=3 is odd, so median = max(lo) = -1

Step 4: Window [-1, -3, 5]
  lo = {-3, -1}
  hi = {5}
  Median = max(lo) = -1
```

## Solution 2: Single Multiset with Median Iterator

**Time Complexity:** O(n log k) - Insertion/deletion is O(log k), iterator movement is O(1) amortized  
**Space Complexity:** O(k) - Single multiset stores window elements

Maintain a single multiset and a pointer to the median element. When adding/removing elements, adjust the median pointer incrementally.

```python
class Solution:
    def medianSlidingWindow(self, nums, k):
        medians = []

        window = sorted(nums[:k])

        def get_mid():
            if k % 2 == 1:
                return window[k // 2]
            else:
                return (window[k // 2 - 1] + window[k // 2]) / 2.0

        medians.append(get_mid())

        for i in range(k, len(nums)):
            # remove outgoing element
            window.remove(nums[i - k])

            # insert incoming element
            window.append(nums[i])
            window.sort()

            medians.append(get_mid())

        return medians
```

## How Solution 2 Works

### Key Insight: Median Iterator Tracking

- **`window`**: Multiset containing all elements in current window
- **`mid`**: Iterator pointing to the median element(s)
  - Odd k: `mid` points to middle element
  - Even k: `mid` points to the right median (we average with `next(mid, -1)`)
- **Incremental Updates**: When adding/removing, adjust `mid` by at most 1 position

### Step-by-Step Example: `nums = [1,3,-1,-3,5,3,6,7], k = 3`

| Step | i | nums[i] | Insert | mid points to | Remove | mid points to | Window | Median |
|------|---|---------|--------|---------------|--------|---------------|--------|--------|
| 0 | - | - | - | - | - | - | {1,3,-1} | 1 |
| 1 | 3 | -3 | {-3} | 1→-1 | 1 | -1→-1 | {-3,-1,3} | -1 |
| 2 | 4 | 5 | {5} | -1→-1 | -1 | -1→3 | {-3,3,5} | -1 |
| 3 | 5 | 3 | {3} | 3→3 | -3 | 3→3 | {3,3,5} | 3 |
| 4 | 6 | 6 | {6} | 3→5 | 3 | 5→5 | {3,5,6} | 5 |
| 5 | 7 | 7 | {7} | 5→6 | 3 | 6→6 | {3,6,7} | 6 |

**Note:** After sorting: `{-3,-1,3}` → `mid` points to `-1` (index 1 in sorted array)

### Median Calculation Trick

```python
if k % 2 == 1:
    medians.append(float(window[k // 2]))
else:
    medians.append((window[k // 2 - 1] + window[k // 2]) / 2.0)
```

- **k is odd**: use the single middle element `window[k // 2]`.
- **k is even**: average the two middle elements `window[k // 2 - 1]` and `window[k // 2]`.

## Algorithm Breakdown

### Solution 1: Two Multisets

#### 1. Insert New Element
```python
import bisect

bisect.insort(window, nums[i])
```
- Keep `window` sorted after each insert (multiset behavior).

#### 2. Balance the Two Multisets
```python
# After each add/remove, rebalance lo/hi so sizes differ by at most 1
while len(lo) > len(hi) + 1:
    bisect.insort(hi, lo.pop())
while len(lo) < len(hi):
    bisect.insort(lo, hi.pop(0))
```
- Maintain: `len(lo) == len(hi)` (even k) or `len(lo) == len(hi) + 1` (odd k) when using two sorted halves.

#### 3. Remove Element Leaving Window
```python
if i >= k:
    out = nums[i - k]
    window.pop(bisect.bisect_left(window, out))
```
- Remove one occurrence of the value leaving the window (`bisect_left` + `pop`).

#### 4. Calculate Median
```python
if k % 2 == 0:
    median = (window[k // 2 - 1] + window[k // 2]) / 2.0
else:
    median = float(window[k // 2])
```

### Solution 2: Single Multiset with Iterator

#### 1. Initialize
```python
window = sorted(nums[:k])
# Median index: k // 2 (odd k) or k//2-1 and k//2 for even k
```
- Start with the first `k` elements sorted.

#### 2. Insert and Adjust
```python
bisect.insort(window, nums[i])
# If tracking an index into window, adjust when order changes
```
- Insert new element in sorted order.

#### 3. Remove and Adjust
```python
out = nums[i - k]
window.pop(bisect.bisect_left(window, out))
```
- Remove one occurrence of the outgoing value, then recompute median from `window`.

## Complexity Analysis

| Solution | Time | Space | Notes |
|----------|------|-------|-------|
| **Solution 1 (Two Multisets)** | O(n log k) | O(k) | Clear separation, easier to understand |
| **Solution 2 (Single Multiset)** | O(n log k) | O(k) | More compact, requires careful iterator management |

### Why O(n log k)?

- **Insertion**: O(log k) - Insert into multiset of size k
- **Deletion**: O(log k) - Erase from multiset of size k
- **Balance/Adjust**: O(log k) - Move elements between sets or adjust iterator
- **Total**: n operations × O(log k) = O(n log k)

## Comparison of Solutions

| Aspect | Solution 1 (Two Multisets) | Solution 2 (Single Multiset) |
|--------|----------------------------|------------------------------|
| **Clarity** | ✅ Clear separation of halves | ⚠️ Requires iterator management |
| **Correctness** | ✅ Easy to verify balance | ⚠️ Iterator adjustments can be tricky |
| **Duplicates** | ✅ Handles naturally | ⚠️ Need `lower_bound` for removal |
| **Median Calc** | ✅ Straightforward | ⚠️ Formula needs careful handling |
| **Maintainability** | ✅ Easier to debug | ⚠️ More complex logic |

## Edge Cases

1. **k = 1**: Each window has one element → return all elements as doubles
2. **k = nums.size()**: Single window → return single median
3. **All same elements**: `[3,3,3,3], k=3` → `[3.0, 3.0]`
4. **Duplicates**: `[1,2,2,3], k=3` → Need careful handling of duplicate removal
5. **Large numbers**: Use `long long` or handle overflow in median calculation

## Common Mistakes

### Solution 1
1. **Wrong balance condition**: Should be `lo.size() > hi.size() + 1` not `lo.size() > hi.size()`
2. **Wrong median calculation**: For even k, average max(lo) and min(hi)
3. **Duplicate removal**: Must use `lo.find(out)` not `lo.erase(out)` to remove only one occurrence

### Solution 2
1. **Iterator invalidation**: Adjust `mid` before erasing, not after
2. **Wrong median formula**: For odd k, need to handle differently
3. **Duplicate removal**: Must use `lower_bound` to remove correct element
4. **Iterator bounds**: Check `mid != window.begin()` before `prev(mid)`

## Fixed Solution 2 (Correct Median Calculation)

```python
class Solution:
    def medianSlidingWindow(self, nums, k):
        medians = []

        window = sorted(nums[:k])

        def get_median():
            if k % 2 == 1:
                return window[k // 2]
            else:
                return (window[k // 2 - 1] + window[k // 2]) / 2.0

        medians.append(get_median())

        for i in range(k, len(nums)):
            # remove outgoing element
            window.remove(nums[i - k])

            # insert incoming element
            window.append(nums[i])
            window.sort()

            medians.append(get_median())

        return medians
```

## Related Problems

- [295. Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/) - Two heaps pattern
- [239. Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/) - Similar sliding window
- [480. Sliding Window Median](https://leetcode.com/problems/sliding-window-median/) - This problem
- [1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit](https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/) - Use two deques

## Pattern Recognition

This problem demonstrates the **Two-Heaps/Multisets Pattern**:
- Maintain two balanced collections (heaps or multisets)
- One contains smaller half, other contains larger half
- Median is easily accessible from the boundaries
- Balance maintained after each insertion/deletion

**Key Insight:**
- For median in sliding window, we need to:
  1. Maintain sorted order
  2. Efficiently add/remove elements
  3. Quickly access middle element(s)

**Applications:**
- Finding median in data streams
- Sliding window statistics
- Order statistics in dynamic sets

## Optimization Tips

### Solution 1: Pre-allocate Result
```python
# Optional: reserve space for the output (length is known)
res: list[float] = [0.0] * (len(nums) - k + 1)
```

### Solution 2: Early Exit
```python
def median_sliding_window_early_k1(nums: list[int], k: int) -> list[float]:
    if k == 1:
        return [float(x) for x in nums]
    raise NotImplementedError

```

### Memory Optimization
Both solutions are already space-optimal. For very large k, consider using two priority queues instead of multisets (but then deletion becomes O(k) instead of O(log k)).

## Why Multiset Instead of Priority Queue?

**Priority Queue (Heap):**
- ✅ Fast insertion: O(log n)
- ❌ Slow deletion: O(n) - need to find and remove specific element
- ❌ Can't iterate - can't access arbitrary elements

**Multiset:**
- ✅ Fast insertion: O(log n)
- ✅ Fast deletion: O(log n) - can find and remove specific element
- ✅ Can iterate - can access any element via iterator
- ✅ Maintains sorted order

For sliding window median, we need to remove specific elements, so multiset is the right choice.

## Code Quality Notes

1. **Solution 1**: More readable and maintainable
2. **Solution 2**: More compact but requires careful iterator handling
3. **Error Handling**: Both handle edge cases properly
4. **Performance**: Both achieve optimal O(n log k) time complexity

---

*This problem extends the sliding window pattern to find median instead of maximum. The two-heaps pattern (implemented with multisets) is essential for efficiently maintaining order statistics in dynamic sets.*

