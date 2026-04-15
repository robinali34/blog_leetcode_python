---
layout: post
title: "[Medium] 29. Divide Two Integers"
date: 2026-02-14 00:00:00 -0700
categories: [leetcode, medium, math, bit-manipulation]
tags: [leetcode, medium, bit-manipulation, math]
permalink: /2026/02/14/medium-29-divide-two-integers/
---

# [Medium] 29. Divide Two Integers

## Problem Statement

Given two integers `dividend` and `divisor`, divide two integers **without** using multiplication, division, and mod operator. Return the quotient after dividing `dividend` by `divisor`. The integer division should truncate toward zero.

## Examples

**Example 1:**

```
Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = 3.33333.. which is truncated to 3.
```

**Example 2:**

```
Input: dividend = 7, divisor = -3
Output: -2
Explanation: 7/-3 = -2.33333.. which is truncated to -2.
```

## Constraints

- `-2^31 <= dividend, divisor <= 2^31 - 1`
- `divisor != 0`
- Cannot use `*`, `/`, or `%`
- Must truncate toward zero
- Return `2^31 - 1` if overflow occurs
- Range: signed 32-bit integer

## Clarification Questions

1. **Operators**: Can we use multiplication, division, or mod? (Assumption: No — only addition, subtraction, bit shifts.)
2. **Truncation**: Truncate toward zero or floor? (Assumption: Toward zero — e.g. -7/3 = -2.)
3. **Overflow**: What if quotient exceeds 32-bit range? (Assumption: Return 2^31 - 1.)
4. **Divisor zero**: Guaranteed non-zero? (Assumption: Yes per constraints.)
5. **Negative numbers**: Can both be negative? (Assumption: Yes; work with absolute values then fix sign.)

## Interview Deduction Process (20 minutes)

**Step 1: Brute-Force (5 min)** — Repeatedly subtract divisor from dividend until dividend < divisor. Count subtractions. O(dividend/divisor) which can be 2^31 — TLE.

**Step 2: Power-of-two multiples (7 min)** — Subtract the largest multiple of divisor that is a power of two (divisor << k). Greedily subtract divisor*(2^k) and add 2^k to quotient. Reduces to O(log quotient) steps.

**Step 3: Optimized (8 min)** — Use longs to avoid overflow when handling INT_MIN. Convert to positive, then apply bit-shift subtraction. Handle sign at the end. Edge: INT_MIN / -1 overflows → return INT_MAX.

## Solution Approach

Focus on: time complexity, overflow safety, bit manipulation tricks, edge case coverage, mathematical transformation.

### Repeated subtraction is too slow

Naive approach:

```
while dividend >= divisor:
    dividend -= divisor
    count++
```

Worst case: $O(2^{31})$ -- TLE. We need $O(\log n)$.

### Think in Binary (Core Insight)

Division is repeated subtraction. Instead of subtracting `divisor` once at a time, subtract the **largest multiple** of `divisor` each time. That multiple can be found using bit shifts:

```
divisor * (2^k) == divisor << k
```

So we greedily subtract the largest shifted divisor. This makes it **logarithmic**.

> Division = Binary decomposition of quotient.

## Approach (Bitwise Greedy)

### Step 1: Handle edge cases

- `divisor == 0` (if allowed)
- Overflow case: `dividend == INT_MIN` and `divisor == -1`

### Step 2: Convert to absolute values

Why use `long`? Because:

```
INT_MIN = -2^31
INT_MAX =  2^31 - 1
```

The absolute value of `INT_MIN` overflows a 32-bit int. Using `long long` avoids this.

Use XOR to detect result sign:

```python
negative = (dividend > 0) ^ (divisor > 0)




```

### Step 3: Main Loop

For `i` from 31 down to 0:
- Check: `if ((dividend >> i) >= divisor)`
- If yes: `dividend -= divisor << i`, `result += 1 << i`

Each bit of the quotient is determined from most significant to least significant, exactly like binary long division.

### Complexity

| Metric | Value |
|--------|-------|
| Time | $O(\log n)$ -- 32 iterations for 32-bit int |
| Space | $O(1)$ |

## Edge Cases

**Case 1:** `dividend = INT_MIN, divisor = -1` -- Answer = `INT_MAX` (overflow guard)

**Case 2:** `dividend = 0` -- Answer = `0`

**Case 3:** `divisor = INT_MIN` -- Only returns `1` if `dividend == INT_MIN`, else `0`

**Case 4:** Mixed signs `(+,+)`, `(-,-)`, `(+,-)`, `(-,+)` -- handled by XOR sign detection

## Solution

{% raw %}
```python
class Solution:
    def divide(self, dividend, divisor):
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        # overflow case
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX
        
        negative = (dividend < 0) ^ (divisor < 0)
        
        dvd = abs(dividend)
        dvs = abs(divisor)
        
        result = 0
        
        for i in range(31, -1, -1):
            if (dvd >> i) >= dvs:
                result += (1 << i)
                dvd -= (dvs << i)
        
        return -result if negative else result
```
{% endraw %}

### Why This Solution Works Well

- Logarithmic time
- No illegal operators
- Overflow-safe
- Bitwise optimized
- Clean edge-case handling

## Alternative: Exponential Doubling

Instead of iterating over all 32 bits, repeatedly double `divisor` until it exceeds `dividend`, then subtract:

{% raw %}
```python
class Solution:
    def divide(self, dividend, divisor):
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX
        
        negative = (dividend < 0) ^ (divisor < 0)
        
        a = abs(dividend)
        b = abs(divisor)
        
        result = 0
        
        while a >= b:
            temp = b
            multiple = 1
            
            while a >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            
            a -= temp
            result += multiple
        
        return -result if negative else resultclass Solution:
    def divide(self, dividend, divisor):
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX
        
        negative = (dividend < 0) ^ (divisor < 0)
        
        a = abs(dividend)
        b = abs(divisor)
        
        result = 0
        
        while a >= b:
            temp = b
            multiple = 1
            
            while a >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            
            a -= temp
            result += multiple
        
        return -result if negative else result
```
{% endraw %}

Also $O(\log n)$.

## Key Takeaways

This problem tests:
- **Bit manipulation mastery** -- shifting as multiplication
- **Integer overflow handling** -- `INT_MIN` absolute value trap
- **Signed range awareness** -- asymmetric 32-bit range
- **Greedy binary decomposition** -- the core algorithmic insight

## Template Reference

- [Math & Bit Manipulation](/blog_leetcode/posts/2025-11-24-leetcode-templates-math-bit-manipulation/)
