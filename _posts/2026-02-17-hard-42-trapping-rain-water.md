---
layout: post
title: "[Hard] 42. Trapping Rain Water"
date: 2026-02-17 00:00:00 -0700
categories: [leetcode, hard, two-pointers, stack, dp]
tags: [leetcode, hard, two-pointers, monotonic-stack, prefix-suffix, dp]
permalink: /2026/02/17/hard-42-trapping-rain-water/
---

# [Hard] 42. Trapping Rain Water

## Problem Statement

Given `n` non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

## Examples

**Example 1:**

```
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
```

**Example 2:**

```
Input: height = [4,2,0,3,2,5]
Output: 9
```

## Constraints

- `n == height.length`
- `1 <= n <= 2 * 10^4`
- `0 <= height[i] <= 10^5`

## Clarification Questions

1. **Bar width**: Is each bar width 1? (Assumption: Yes — standard problem.)
2. **Water units**: One unit of water per unit area between bars? (Assumption: Yes.)
3. **Edges**: Do the first and last bars trap water? (Assumption: They form boundaries; water is trapped between higher bars.)
4. **Empty array**: n >= 1? (Assumption: Yes per constraints.)
5. **Output**: Total water trapped as integer? (Assumption: Yes.)

## Interview Deduction Process (20 minutes)

**Step 1: Brute-Force (5 min)** — For each index i, find max height to the left and right; water at i = min(maxLeft, maxRight) - height[i]. O(n^2) — too slow.

**Step 2: Prefix/Suffix (7 min)** — Precompute leftMax[i] and rightMax[i] in two passes. Then one pass to sum water. O(n) time, O(n) space.

**Step 3: Two pointers (8 min)** — If leftMax < rightMax, water at left depends only on leftMax; move left pointer and update leftMax. Else symmetric for right. O(n) time, O(1) space.

## Solution Approach

### Mathematical Model

At index `i`, the water trapped is:

$$\text{water}[i] = \min(\text{maxLeft}[i],\ \text{maxRight}[i]) - \text{height}[i]$$

If negative, clamp to 0. Where:
- `maxLeft[i]` = maximum height from `0` to `i`
- `maxRight[i]` = maximum height from `i` to `n-1`

### From Brute Force to Optimal

**Brute force**: For each index, scan left and right to find the max. $O(n^2)$ -- too slow.

**Prefix/Suffix arrays**: Precompute `leftMax[]` and `rightMax[]` in two passes. $O(n)$ time, $O(n)$ space. Safe and clean.

**Two pointers**: Key insight -- if `leftMax < rightMax`, water depends **only** on `leftMax` because $\min(\text{leftMax}, \text{rightMax}) = \text{leftMax}$. The opposite side is guaranteed to be at least as tall. So we don't need full arrays; just move the smaller side inward. $O(n)$ time, $O(1)$ space.

### Comparison Table

| Approach | Time | Space | Notes |
|---|---|---|---|
| Brute Force | $O(n^2)$ | $O(1)$ | Too slow |
| Prefix/Suffix | $O(n)$ | $O(n)$ | Safe, easy |
| Two Pointers | $O(n)$ | $O(1)$ | Optimal |
| Monotonic Stack | $O(n)$ | $O(n)$ | Useful pattern |

## Approach 1: Brute Force -- $O(n^2)$

For each index, scan left and right to find the max height on each side.

{% raw %}
```python
class Solution:
    def trap(self, height):
        n = len(height)
        water = 0
        
        for i in range(n):
            leftMax = 0
            rightMax = 0
            
            # max to the left of i
            for l in range(i + 1):
                leftMax = max(leftMax, height[l])
            
            # max to the right of i
            for r in range(i, n):
                rightMax = max(rightMax, height[r])
            
            water += min(leftMax, rightMax) - height[i]
        
        return water

```
{% endraw %}

**Time**: $O(n^2)$
**Space**: $O(1)$

## Approach 2: Prefix & Suffix Arrays -- $O(n)$ time, $O(n)$ space

Precompute `leftMax[i]` and `rightMax[i]` in two linear passes, then compute water in a third pass.

{% raw %}
```python
class Solution:
    def trap(self, height):
        n = len(height)
        if n == 0:
            return 0
        
        leftMax = [0] * n
        rightMax = [0] * n
        
        water = 0
        
        # build leftMax
        leftMax[0] = height[0]
        for i in range(1, n):
            leftMax[i] = max(leftMax[i - 1], height[i])
        
        # build rightMax
        rightMax[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            rightMax[i] = max(rightMax[i + 1], height[i])
        
        # calculate water
        for i in range(n):
            water += min(leftMax[i], rightMax[i]) - height[i]
        
        return waterclass Solution:
    def trap(self, height):
        n = len(height)
        if n == 0:
            return 0
        
        leftMax = [0] * n
        rightMax = [0] * n
        
        water = 0
        
        # build leftMax
        leftMax[0] = height[0]
        for i in range(1, n):
            leftMax[i] = max(leftMax[i - 1], height[i])
        
        # build rightMax
        rightMax[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            rightMax[i] = max(rightMax[i + 1], height[i])
        
        # calculate water
        for i in range(n):
            water += min(leftMax[i], rightMax[i]) - height[i]
        
        return water

```
{% endraw %}

**Time**: $O(n)$
**Space**: $O(n)$

## Approach 3: Two Pointers -- $O(n)$ time, $O(1)$ space (Optimal)

The smaller side always determines the bottleneck. Move the pointer on the smaller side inward, accumulating water as you go.

**Invariant**: At each step, the smaller of `leftMax` and `rightMax` determines trapped water. Since the opposite side is guaranteed $\geq$ the smaller side, the water calculation is always safe.

{% raw %}
```python
class Solution:
    def trap(self, height):
        n = len(height)
        if n == 0:
            return 0
        
        l, r = 0, n - 1
        leftMax, rightMax = 0, 0
        water = 0
        
        while l < r:
            if height[l] < height[r]:
                if height[l] >= leftMax:
                    leftMax = height[l]
                else:
                    water += leftMax - height[l]
                l += 1
            else:
                if height[r] >= rightMax:
                    rightMax = height[r]
                else:
                    water += rightMax - height[r]
                r -= 1
        
        return waterclass Solution:
    def trap(self, height):
        n = len(height)
        if n == 0:
            return 0
        
        l, r = 0, n - 1
        leftMax, rightMax = 0, 0
        water = 0
        
        while l < r:
            if height[l] < height[r]:
                if height[l] >= leftMax:
                    leftMax = height[l]
                else:
                    water += leftMax - height[l]
                l += 1
            else:
                if height[r] >= rightMax:
                    rightMax = height[r]
                else:
                    water += rightMax - height[r]
                r -= 1
        
        return water
```
{% endraw %}

**Time**: $O(n)$
**Space**: $O(1)$

## Approach 4: Monotonic Stack -- $O(n)$ time, $O(n)$ space

Process bars left to right. When a taller bar is found, pop shorter bars from the stack and compute the water trapped in the "valley" between the current bar and the new stack top.

{% raw %}
```python
class Solution:
    def trap(self, height):
        n = len(height)
        water = 0
        st = []  # stack to store indices
        
        for i in range(n):
            while st and height[i] > height[st[-1]]:
                top = st.pop()
                
                if not st:
                    break
                
                distance = i - st[-1] - 1
                boundedHeight = min(height[i], height[st[-1]]) - height[top]
                water += distance * boundedHeight
            
            st.append(i)
        
        return waterclass Solution:
    def trap(self, height):
        n = len(height)
        water = 0
        st = []  # stack to store indices
        
        for i in range(n):
            while st and height[i] > height[st[-1]]:
                top = st.pop()
                
                if not st:
                    break
                
                distance = i - st[-1] - 1
                boundedHeight = min(height[i], height[st[-1]]) - height[top]
                water += distance * boundedHeight
            
            st.append(i)
        
        return water

```
{% endraw %}

**Time**: $O(n)$ -- each index is pushed and popped at most once
**Space**: $O(n)$ for the stack

## Pattern Recognition

When you see "for each position, need left info + right info," immediately consider:
- **Prefix/suffix arrays** -- safe and straightforward
- **Two pointers** -- optimal when one side dominates
- **Monotonic stack** -- when the problem involves bounded areas between bars

## Key Takeaways

- The formula $\min(\text{maxLeft}, \text{maxRight}) - \text{height}$ is the foundation -- all four approaches implement it differently
- Two pointers eliminates extra space by observing that the smaller side is the only bottleneck
- Monotonic stack computes water layer by layer (horizontally) rather than column by column (vertically)
- Master both two-pointer and monotonic-stack versions -- they appear in many related problems

### Related Problems:

- [LC 11: Container With Most Water](https://leetcode.com/problems/container-with-most-water/) — Two-pointer on water area
- [LC 84: Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/) — Monotonic stack classic
- [LC 407: Trapping Rain Water II](https://leetcode.com/problems/trapping-rain-water-ii/) — 3D version with BFS + heap

## Template Reference

- [Stack](/blog_leetcode/posts/2025-11-13-leetcode-templates-stack/)
- [Data Structures](/blog_leetcode/posts/2025-10-29-leetcode-templates-data-structures/)
