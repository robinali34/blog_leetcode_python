---
layout: post
title: "[Medium] 223. Rectangle Area"
date: 2026-04-09 00:00:00 -0700
categories: [leetcode, medium, math, geometry]
tags: [leetcode, medium, math, geometry]
permalink: /2026/04/09/medium-223-rectangle-area/
---

# [Medium] 223. Rectangle Area

## Problem Statement

Given the coordinates of two axis-aligned rectangles in the plane, return the **total area** covered by both rectangles.

Each rectangle is given as `(x1, y1, x2, y2)` with `(x1, y1)` bottom-left and `(x2, y2)` top-right.

## Examples

**Example 1:**

```python
Input: ax1=-3, ay1=0, ax2=3, ay2=4, bx1=0, by1=-1, bx2=9, by2=2
Output: 45
```

**Example 2:**

```python
Input: ax1=-2, ay1=-2, ax2=2, ay2=2, bx1=-2, by1=-2, bx2=2, by2=2
Output: 16
# Same rectangle — overlap counted once
```

## Constraints

- `-10^4 <= ax1, ay1, ax2, ay2, bx1, by1, bx2, by2 <= 10^4`

## Analysis

- Area of rectangle A: `(ax2 - ax1) * (ay2 - ay1)` (same for B).
- Intersection is also axis-aligned: horizontal overlap width = `max(0, min(ax2, bx2) - max(ax1, bx1))`, vertical height = `max(0, min(ay2, by2) - max(ay1, by1))`.
- **Inclusion–exclusion:** `area(A) + area(B) - area(intersection)`.

## Python Solution

```python
class Solution:
    def computeArea(
        self,
        ax1: int,
        ay1: int,
        ax2: int,
        ay2: int,
        bx1: int,
        by1: int,
        bx2: int,
        by2: int,
    ) -> int:
        area_of_a = (ay2 - ay1) * (ax2 - ax1)
        area_of_b = (by2 - by1) * (bx2 - bx1)

        left = max(ax1, bx1)
        right = min(ax2, bx2)
        x_overlap = right - left

        top = min(ay2, by2)
        bottom = max(ay1, by1)
        y_overlap = top - bottom

        area_of_overlap = 0
        if x_overlap > 0 and y_overlap > 0:
            area_of_overlap = x_overlap * y_overlap
        total_area = area_of_a + area_of_b - area_of_overlap

        return total_area
```

## Complexity

- **Time:** O(1)
- **Space:** O(1)

## Common Mistakes

- Using `max(0, overlap)` only on the product instead of checking both dimensions (your `if` handles non-overlap cleanly).
- Confusing which corner is min/max for y (bottom vs top).

## Related Problems

- [LC 836: Rectangle Overlap](https://leetcode.com/problems/rectangle-overlap/)
- [LC 391: Perfect Rectangle](https://leetcode.com/problems/perfect-rectangle/)
