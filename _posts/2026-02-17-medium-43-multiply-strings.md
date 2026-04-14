---
layout: post
title: "43. Multiply Strings"
date: 2026-02-17 00:00:00 -0700
categories: [leetcode, medium, string, math, simulation]
tags: [leetcode, medium, string, math, big-integer, simulation]
permalink: /2026/02/17/medium-43-multiply-strings/
---

# 43. Multiply Strings

## Problem Statement

Given two non-negative integers represented as strings `num1` and `num2`, return their product as a string. You **cannot** convert the inputs to integers directly (numbers can be very large).

## Examples

**Example 1:**

```
Input: num1 = "2", num2 = "3"
Output: "6"
```

**Example 2:**

```
Input: num1 = "123", num2 = "456"
Output: "56088"
```

## Constraints

- `1 <= num1.length, num2.length <= 200`
- `num1` and `num2` consist of digits only
- Neither contains leading zeros (except `"0"` itself)

## Clarification Questions

1. **Direct conversion**: Can we use int()? (Assumption: No — numbers can exceed int range.)
2. **Leading zeros**: Should output have leading zeros? (Assumption: No — return canonical form.)
3. **Zero product**: "0" × anything = "0"? (Assumption: Yes.)
4. **Digits only**: Only '0'-'9'? (Assumption: Yes.)

## Interview Deduction Process (20 minutes)

**Step 1: Grade-school multiplication (5 min)** — Multiply each digit of num1 by each digit of num2; add into result at the right position. Result length at most len(num1) + len(num2).

**Step 2: Index mapping (7 min)** — num1[i] * num2[j] contributes to result at index i + j and i + j + 1. Use an array of length n + m; accumulate then strip leading zeros.

**Step 3: Optimized (8 min)** — Single pass: for each (i, j), add digit product to res[i+j+1] and carry to res[i+j]. Then convert to string and strip leading zeros. Handle "0" explicitly.

## Solution Approach

This is **big integer multiplication** -- simulate digit-by-digit multiplication exactly like grade school arithmetic.

### Key Insights

If `num1` has length `n` and `num2` has length `m`:
- The product has **at most `n + m` digits**
- Allocate a result array of size `n + m`

### Index Formula

When multiplying `num1[i] * num2[j]`, the contribution goes to:

$$\text{result}[i + j + 1] \quad \text{(ones place)}$$
$$\text{result}[i + j] \quad \text{(carry)}$$

This is because position `i` from the end of `num1` and position `j` from the end of `num2` together shift the product by `(n-1-i) + (m-1-j)` places, which maps to index `i + j + 1` in the result array.

### Walk-Through: `123 × 45`

```
         1  2  3
       ×    4  5
      -----------
  positions: result[0..4]

  3×5 = 15 → result[4] += 15  → result[4]=5, carry 1 to result[3]
  2×5 = 10 → result[3] += 10+1 = 11 → result[3]=1, carry 1 to result[2]
  1×5 =  5 → result[2] += 5+1 = 6

  3×4 = 12 → result[3] += 12  → result[3]=3, carry 1 to result[2]
  2×4 =  8 → result[2] += 8+1 = 15 → result[2]=5, carry 1 to result[1]
  1×4 =  4 → result[1] += 4+1 = 5

  result = [0, 5, 5, 3, 5] → "05535" → skip leading zero → "5535"
```

Wait -- `123 × 45 = 5535`. Correct!

## Approach: Grade School Multiplication -- $O(nm)$

Multiply each digit pair, accumulate into a result array with carry propagation.

{% raw %}
```python
class Solution:
    def multiply(self, num1, num2):
        if num1 == "0" or num2 == "0":
            return "0"
        
        n, m = len(num1), len(num2)
        result = [0] * (n + m)
        
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                mul = int(num1[i]) * int(num2[j])
                total = mul + result[i + j + 1]
                
                result[i + j + 1] = total % 10
                result[i + j] += total // 10
        
        # build the result string (skip leading zeros)
        ans = ""
        for num in result:
            if not (ans == "" and num == 0):
                ans += str(num)
        
        return ans if ans else "0"
```
{% endraw %}

**Time**: $O(n \times m)$
**Space**: $O(n + m)$ for the result array

## Common Mistakes

- Forgetting the early return for `"0"` inputs (otherwise you get `"000..."`)
- Off-by-one on the index formula (`i + j` vs `i + j + 1`)
- Not handling leading zeros when converting the result array to a string

## Key Takeaways

- **Big integer multiplication** follows the same algorithm you learned in school
- The index formula `result[i + j + 1]` is the core insight -- memorize it
- Always allocate `n + m` digits for the result
- Faster algorithms exist (Karatsuba $O(n^{1.58})$, FFT $O(n \log n)$) but are overkill for interview constraints

## Related Problems

- [2. Add Two Numbers](https://leetcode.com/problems/add-two-numbers/) -- big integer addition on linked lists
- [67. Add Binary](https://leetcode.com/problems/add-binary/) -- string addition with carry
- [415. Add Strings](https://leetcode.com/problems/add-strings/) -- big integer addition on strings

## Template Reference

- [Math & Bit Manipulation](/blog_leetcode/posts/2025-11-24-leetcode-templates-math-bit-manipulation/)
- [String Processing](/blog_leetcode/posts/2025-11-24-leetcode-templates-string-processing/)
