---
layout: post
title: "Algorithm Templates: Array & Matrix"
date: 2025-11-24 00:00:00 -0700
categories: leetcode templates array matrix
permalink: /posts/2025-11-24-leetcode-templates-array-matrix/
tags: [leetcode, templates, array, matrix]
---

{% raw %}
Welcome to the Array & Matrix template collection! These are ready-to-use C++ snippets for the most common array patterns: two pointers, sliding window, prefix sum, binary search, and matrix operations. Each template is minimal enough to memorize yet complete enough to paste into a solution and adapt. See also [Arrays & Strings](/posts/2025-10-29-leetcode-templates-arrays-strings/) and [Search](/posts/2026-01-20-leetcode-templates-search/).

> **Arrays are the most common data structure in interviews.** Most problems start with an array or can be reduced to one. Learning these patterns well — two pointers, sliding window, prefix sum, and binary search — covers roughly 40% of all LeetCode problems.

## Contents

- [Two Pointers](#two-pointers)
- [Sliding Window](#sliding-window)
- [Prefix Sum](#prefix-sum)
- [Binary Search](#binary-search)
- [Matrix Operations](#matrix-operations)
- [Array Manipulation](#array-manipulation)

## Two Pointers

**When to use:** The problem says "sorted array", asks for a "pair with target sum", mentions "container with most water", or requires comparing elements from both ends.

### Two Sum on Sorted Array

```python
def two_sum_sorted(a: list[int], target: int) -> bool:
    l, r = 0, len(a) - 1
    while l < r:
        s = a[l] + a[r]
        if s == target:
            return True
        if s < target:
            l += 1
        else:
            r -= 1
    return False

```

### Three Sum / Four Sum

```python
def three_sum(nums: list[int]) -> list[list[int]]:
    nums.sort()
    n = len(nums)
    result: list[list[int]] = []
    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left, right = i + 1, n - 1
        while left < right:
            s = nums[i] + nums[left] + nums[right]
            if s == 0:
                result.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif s < 0:
                left += 1
            else:
                right -= 1
    return result

```

| ID | Title | Link | Solution |
|---|---|---|---|
| 15 | 3Sum | [Link](https://leetcode.com/problems/3sum/) | - |
| 18 | 4Sum | [Link](https://leetcode.com/problems/4sum/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2025/11/04/medium-18-4sum/) |
| 11 | Container With Most Water | [Link](https://leetcode.com/problems/container-with-most-water/) | - |
| 75 | Sort Colors | [Link](https://leetcode.com/problems/sort-colors/) | [Solution](https://robinali34.github.io/blog_leetcode_python/posts/2025-12-02-medium-75-sort-colors/) |
| 360 | Sort Transformed Array | [Link](https://leetcode.com/problems/sort-transformed-array/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2025/12/31/medium-360-sort-transformed-array/) |
| 344 | Reverse String | [Link](https://leetcode.com/problems/reverse-string/) | [Solution](https://robinali34.github.io/blog_leetcode_python/posts/2025-10-29-easy-344-reverse-string/) |
| 844 | Backspace String Compare | [Link](https://leetcode.com/problems/backspace-string-compare/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2026/01/12/easy-844-backspace-string-compare/) |
| 1868 | Product of Two Run-Length Encoded Arrays | [Link](https://leetcode.com/problems/product-of-two-run-length-encoded-arrays/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2025/10/20/medium-1868-product-of-two-run-length-encoded-arrays/) |

## Sliding Window

**When to use:** The problem asks for a "subarray of size k", "longest/shortest subarray with property X", or any contiguous subarray optimization.

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 170" style="max-width:520px;width:100%">
  <style>
    text { font-family: ui-monospace, monospace; fill: #5A5752; }
    .label { font-size: 13px; }
    .idx { font-size: 11px; }
    .arrow-label { font-size: 11px; font-style: italic; }
  </style>
  <!-- array boxes -->
  <g transform="translate(30,50)">
    <rect x="0"   y="0" width="50" height="40" rx="4" fill="#D4D8D0" stroke="#B8B5B0" stroke-width="1.5"/>
    <text x="25"  y="26" text-anchor="middle" class="label">3</text>
    <text x="25"  y="55" text-anchor="middle" class="idx">0</text>
    <rect x="60"  y="0" width="50" height="40" rx="4" fill="#D4D8D0" stroke="#B8B5B0" stroke-width="1.5"/>
    <text x="85"  y="26" text-anchor="middle" class="label">1</text>
    <text x="85"  y="55" text-anchor="middle" class="idx">1</text>
    <rect x="120" y="0" width="50" height="40" rx="4" fill="#E8D5D0" stroke="#B8B5B0" stroke-width="1.5"/>
    <text x="145" y="26" text-anchor="middle" class="label">7</text>
    <text x="145" y="55" text-anchor="middle" class="idx">2</text>
    <rect x="180" y="0" width="50" height="40" rx="4" fill="#E8D5D0" stroke="#B8B5B0" stroke-width="1.5"/>
    <text x="205" y="26" text-anchor="middle" class="label">2</text>
    <text x="205" y="55" text-anchor="middle" class="idx">3</text>
    <rect x="240" y="0" width="50" height="40" rx="4" fill="#E8D5D0" stroke="#B8B5B0" stroke-width="1.5"/>
    <text x="265" y="26" text-anchor="middle" class="label">5</text>
    <text x="265" y="55" text-anchor="middle" class="idx">4</text>
    <rect x="300" y="0" width="50" height="40" rx="4" fill="#D4D8D0" stroke="#B8B5B0" stroke-width="1.5"/>
    <text x="325" y="26" text-anchor="middle" class="label">9</text>
    <text x="325" y="55" text-anchor="middle" class="idx">5</text>
    <rect x="360" y="0" width="50" height="40" rx="4" fill="#D4D8D0" stroke="#B8B5B0" stroke-width="1.5"/>
    <text x="385" y="26" text-anchor="middle" class="label">4</text>
    <text x="385" y="55" text-anchor="middle" class="idx">6</text>
    <rect x="420" y="0" width="50" height="40" rx="4" fill="#D4D8D0" stroke="#B8B5B0" stroke-width="1.5"/>
    <text x="445" y="26" text-anchor="middle" class="label">8</text>
    <text x="445" y="55" text-anchor="middle" class="idx">7</text>
  </g>
  <!-- window bracket -->
  <rect x="148" y="42" width="194" height="52" rx="6" fill="none" stroke="#D4D8E0" stroke-width="2.5" stroke-dasharray="6,3"/>
  <!-- left pointer -->
  <line x1="175" y1="38" x2="175" y2="18" stroke="#B8B5B0" stroke-width="1.5" marker-end="url(#arrowUp)"/>
  <text x="175" y="12" text-anchor="middle" class="arrow-label" fill="#5A5752">left</text>
  <!-- right pointer -->
  <line x1="325" y1="38" x2="325" y2="18" stroke="#B8B5B0" stroke-width="1.5" marker-end="url(#arrowUp)"/>
  <text x="325" y="12" text-anchor="middle" class="arrow-label" fill="#5A5752">right</text>
  <!-- shrink-left arrow -->
  <line x1="165" y1="130" x2="210" y2="130" stroke="#B8B5B0" stroke-width="1.5" marker-end="url(#arrowRight)"/>
  <text x="188" y="148" text-anchor="middle" class="arrow-label">shrink left</text>
  <!-- expand-right arrow -->
  <line x1="380" y1="130" x2="335" y2="130" stroke="#B8B5B0" stroke-width="1.5" marker-end="url(#arrowLeft)"/>
  <text x="358" y="148" text-anchor="middle" class="arrow-label">expand right</text>
  <!-- window label -->
  <text x="245" y="130" text-anchor="middle" class="label" fill="#5A5752">window [left, right]</text>
  <defs>
    <marker id="arrowUp" markerWidth="8" markerHeight="6" refX="4" refY="6" orient="auto"><path d="M0,6 L4,0 L8,6" fill="none" stroke="#B8B5B0" stroke-width="1.2"/></marker>
    <marker id="arrowRight" markerWidth="8" markerHeight="6" refX="8" refY="3" orient="auto"><path d="M0,0 L8,3 L0,6" fill="none" stroke="#B8B5B0" stroke-width="1.2"/></marker>
    <marker id="arrowLeft" markerWidth="8" markerHeight="6" refX="0" refY="3" orient="auto"><path d="M8,0 L0,3 L8,6" fill="none" stroke="#B8B5B0" stroke-width="1.2"/></marker>
  </defs>
</svg>

### Fixed Size Window

```python
# Maximum sum of subarray of size k
def max_sum_subarray(nums: list[int], k: int) -> int:
    window = sum(nums[:k])
    best = window
    for i in range(k, len(nums)):
        window += nums[i] - nums[i - k]
        best = max(best, window)
    return best

```

### Variable Size Window

```python
# Longest subarray with sum <= k
def longest_subarray(nums: list[int], k: int) -> int:
    left = 0
    total = 0
    max_len = 0
    for right in range(len(nums)):
        total += nums[right]
        while total > k:
            total -= nums[left]
            left += 1
        max_len = max(max_len, right - left + 1)
    return max_len

```

| ID | Title | Link | Solution |
|---|---|---|---|
| 3 | Longest Substring Without Repeating Characters | [Link](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2025/10/10/medium-3-longest-substring-without-repeating-characters/) |
| 209 | Minimum Size Subarray Sum | [Link](https://leetcode.com/problems/minimum-size-subarray-sum/) | - |
| 239 | Sliding Window Maximum | [Link](https://leetcode.com/problems/sliding-window-maximum/) | [Solution](https://robinali34.github.io/blog_leetcode_python/posts/2025-11-04-hard-239-sliding-window-maximum/) |
| 480 | Sliding Window Median | [Link](https://leetcode.com/problems/sliding-window-median/) | [Solution](https://robinali34.github.io/blog_leetcode_python/posts/2025-11-04-hard-480-sliding-window-median/) |
| 2799 | Count Complete Subarrays in an Array | [Link](https://leetcode.com/problems/count-complete-subarrays-in-an-array/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2025/10/17/medium-2799-count-complete-subarrays-in-an-array/) |
| 346 | Moving Average from Data Stream | [Link](https://leetcode.com/problems/moving-average-from-data-stream/) | [Solution](https://robinali34.github.io/blog_leetcode_python/posts/2025-12-14-easy-346-moving-average-from-data-stream/) |
| 713 | Subarray Product Less Than K | [Link](https://leetcode.com/problems/subarray-product-less-than-k/) | - |

## Prefix Sum

**When to use:** The problem involves "range sum queries", "subarray sum equals k", or asks you to compute cumulative totals over a range efficiently.

### Basic Prefix Sum

```python
def prefix_sum(a: list[int]) -> list[int]:
    ps = [0] * (len(a) + 1)
    for i in range(len(a)):
        ps[i + 1] = ps[i] + a[i]
    return ps


def range_sum(prefix: list[int], l: int, r: int) -> int:
    return prefix[r + 1] - prefix[l]

```

### Difference Array

```python
# Range addition
def get_modified_array(length: int, updates: list[list[int]]) -> list[int]:
    diff = [0] * (length + 1)
    for start, end, inc in updates:
        diff[start] += inc
        diff[end + 1] -= inc
    result = [0] * length
    cur = 0
    for i in range(length):
        cur += diff[i]
        result[i] = cur
    return result

```

| ID | Title | Link | Solution |
|---|---|---|---|
| 303 | Range Sum Query - Immutable | [Link](https://leetcode.com/problems/range-sum-query-immutable/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2026/01/01/easy-303-range-sum-query-immutable/) |
| 307 | Range Sum Query - Mutable | [Link](https://leetcode.com/problems/range-sum-query-mutable/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2026/01/16/medium-307-range-sum-query-mutable/) |
| 560 | Subarray Sum Equals K | [Link](https://leetcode.com/problems/subarray-sum-equals-k/) | - |
| 525 | Contiguous Array | [Link](https://leetcode.com/problems/contiguous-array/) | [Solution](https://robinali34.github.io/blog_leetcode_python/posts/2025-11-04-medium-525-contiguous-array/) |
| 1124 | Longest Well-Performing Interval | [Link](https://leetcode.com/problems/longest-well-performing-interval/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2025/10/16/medium-1124-longest-well-performing-interval/) |
| 327 | Count of Range Sum | [Link](https://leetcode.com/problems/count-of-range-sum/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2026/01/20/hard-327-count-of-range-sum/) |
| 370 | Range Addition | [Link](https://leetcode.com/problems/range-addition/) | - |
| 1094 | Car Pooling | [Link](https://leetcode.com/problems/car-pooling/) | [Solution](https://robinali34.github.io/blog_leetcode_python/posts/2025-10-22-medium-1094-car-pooling/) |

## Binary Search

**When to use:** The input is sorted, the problem says "find position", "search", or you need to minimize/maximize a value where the answer is monotonic.

### Search in Sorted Array

```python
def binary_search(nums: list[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

```

### Search in Rotated Sorted Array

```python
def search_rotated(nums: list[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1

```

| ID | Title | Link | Solution |
|---|---|---|---|
| 33 | Search in Rotated Sorted Array | [Link](https://leetcode.com/problems/search-in-rotated-sorted-array/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2025/09/23/medium-33-search-in-rotated-sorted-array/) |
| 34 | Find First and Last Position | [Link](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/) | - |
| 240 | Search a 2D Matrix II | [Link](https://leetcode.com/problems/search-a-2d-matrix-ii/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2025/10/07/medium-240-search-a-2d-matrix-ii/) |

## Matrix Operations

**When to use:** The problem says "rotate image", "spiral order", "transpose matrix", or involves traversing a 2D grid in a specific pattern.

### Rotate Matrix

```python
# Rotate 90 degrees clockwise
def rotate_matrix(matrix: list[list[int]]) -> None:
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for row in matrix:
        row.reverse()

```

### Spiral Matrix

```python
def spiral_order(matrix: list[list[int]]) -> list[int]:
    if not matrix:
        return []
    m, n = len(matrix), len(matrix[0])
    top, bottom, left, right = 0, m - 1, 0, n - 1
    result: list[int] = []
    while top <= bottom and left <= right:
        for j in range(left, right + 1):
            result.append(matrix[top][j])
        top += 1
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1
        if top <= bottom:
            for j in range(right, left - 1, -1):
                result.append(matrix[bottom][j])
            bottom -= 1
        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1
    return result

```

| ID | Title | Link | Solution |
|---|---|---|---|
| 48 | Rotate Image | [Link](https://leetcode.com/problems/rotate-image/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2025/09/24/medium-48-rotate-image/) |
| 54 | Spiral Matrix | [Link](https://leetcode.com/problems/spiral-matrix/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2025/09/25/medium-54-spiral-matrix/) |
| 59 | Spiral Matrix II | [Link](https://leetcode.com/problems/spiral-matrix-ii/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2026/02/18/medium-59-spiral-matrix-ii/) |
| 498 | Diagonal Traverse | [Link](https://leetcode.com/problems/diagonal-traverse/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2026/01/20/medium-498-diagonal-traverse/) |
| 189 | Rotate Array | [Link](https://leetcode.com/problems/rotate-array/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2026/01/20/medium-189-rotate-array/) |
| 419 | Battleships in a Board | [Link](https://leetcode.com/problems/battleships-in-a-board/) | [Solution](https://robinali34.github.io/blog_leetcode_python/posts/2025-10-21-medium-419-battleships-in-a-board/) |
| 661 | Image Smoother | [Link](https://leetcode.com/problems/image-smoother/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2025/12/30/easy-661-image-smoother/) |
| 73 | Set Matrix Zeroes | [Link](https://leetcode.com/problems/set-matrix-zeroes/) | [Solution](https://robinali34.github.io/blog_leetcode_python/2026/04/02/medium-73-set-matrix-zeroes/) |

## Array Manipulation

**When to use:** The problem involves "merge intervals", "jump game", "overlapping ranges", or requires rearranging array elements in-place.

### Merge Intervals

```python
def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    intervals.sort(key=lambda x: x[0])
    merged: list[list[int]] = []
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])
    return merged

```

### Jump Game

```python
# Jump Game II - Minimum jumps
def jump_game_ii(nums: list[int]) -> int:
    n = len(nums)
    jumps = cur_end = cur_far = 0
    for i in range(n - 1):
        cur_far = max(cur_far, i + nums[i])
        if i == cur_end:
            jumps += 1
            cur_end = cur_far
    return jumps

```

| ID | Title | Link | Solution |
|---|---|---|---|
| 56 | Merge Intervals | [Link](https://leetcode.com/problems/merge-intervals/) | [Solution](https://robinali34.github.io/blog_leetcode_python/posts/2025-11-24-medium-56-merge-intervals/) |
| 45 | Jump Game II | [Link](https://leetcode.com/problems/jump-game-ii/) | [Solution](https://robinali34.github.io/blog_leetcode_python/posts/2025-11-18-medium-45-jump-game-ii/) |
| 969 | Pancake Sorting | [Link](https://leetcode.com/problems/pancake-sorting/) | [Solution](https://robinali34.github.io/blog_leetcode_python/posts/2025-11-18-medium-969-pancake-sorting/) |

## Summary

| Pattern | Signal Phrases | Key Idea |
|---|---|---|
| Two Pointers | "sorted array", "pair sum", "container" | Start/end pointers moving inward |
| Sliding Window | "substring", "subarray of size k" | Expand right, shrink left |
| Prefix Sum | "range sum", "subarray sum equals k" | Precompute cumulative sums |
| Binary Search | "sorted", "find position" | Halve search space |
| Matrix | "rotate", "spiral", "transpose" | Index mapping |

## More templates

- **Beginner's Guide:** [LeetCode Beginner's Guide](/2026/06/25/leetcode-beginners-guide/)
- **Arrays & Strings, Search:** [Arrays & Strings](/posts/2025-10-29-leetcode-templates-arrays-strings/), [Search](/posts/2026-01-20-leetcode-templates-search/)
- **Data structures, Graph:** [Data Structures & Core Algorithms](/posts/2025-10-29-leetcode-templates-data-structures/), [Graph](/posts/2025-10-29-leetcode-templates-graph/)
- **Master index:** [Categories & Templates](/posts/2025-10-29-leetcode-categories-and-templates/)
{% endraw %}

