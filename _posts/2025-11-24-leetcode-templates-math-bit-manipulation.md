---
layout: post
title: "Algorithm Templates: Math & Bit Manipulation"
date: 2025-11-24 00:00:00 -0700
categories: leetcode templates math bit-manipulation
permalink: /posts/2025-11-24-leetcode-templates-math-bit-manipulation/
tags: [leetcode, templates, math, bit-manipulation]
---

{% raw %}
Minimal, copy-paste C++ for bit operations, fast exponentiation, GCD/LCM, primes, and number theory. See also [Math & Geometry](/posts/2025-10-29-leetcode-templates-math-geometry/).

## Contents

- [Bit Operations](#bit-operations)
- [Common Bit Tricks](#common-bit-tricks)
- [Fast Exponentiation](#fast-exponentiation)
- [GCD and LCM](#gcd-and-lcm)
- [Prime Numbers](#prime-numbers)
- [Number Theory](#number-theory)

## Bit Operations

### Basic Operations

```python
// Set bit at position i
def setBit(self, num, i):
    return num | (1 << i)
// Clear bit at position i
def clearBit(self, num, i):
    return num  ~(1 << i)
// Toggle bit at position i
def toggleBit(self, num, i):
    return num ^ (1 << i)
// Check if bit is set
def isBitSet(self, num, i):
    return (num >> i)  1
// Count set bits
def countSetBits(self, num):
    count = 0
    while num:
        count += num  1
        num >>= 1
    return count
// Count set bits (Brian Kernighan's algorithm)
def countSetBitsFast(self, num):
    count = 0
    while num:
        num = (num - 1)
        count += 1
    return count
```

### Common Bit Tricks

```python
// Get lowest set bit
def lowestSetBit(self, num):
    return num  (-num)
// Clear lowest set bit
def clearLowestSetBit(self, num):
    return num  (num - 1)
// Check if power of 2
def isPowerOfTwo(self, num):
    return num > 0  and  (num  (num - 1)) == 0
// Get next power of 2
def nextPowerOfTwo(self, num):
    num -= 1
    num |= num >> 1
    num |= num >> 2
    num |= num >> 4
    num |= num >> 8
    num |= num >> 16
    return num + 1
// Swap two numbers
def swap(self, a, b):
    a ^= b
    b ^= a
    a ^= b
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 29 | Divide Two Integers | [Link](https://leetcode.com/problems/divide-two-integers/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/02/14/medium-29-divide-two-integers/) |
| 36 | Valid Sudoku | [Link](https://leetcode.com/problems/valid-sudoku/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/02/14/medium-36-valid-sudoku/) |
| 67 | Add Binary | [Link](https://leetcode.com/problems/add-binary/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-12-11-easy-67-add-binary/) |
| 191 | Number of 1 Bits | [Link](https://leetcode.com/problems/number-of-1-bits/) | - |
| 231 | Power of Two | [Link](https://leetcode.com/problems/power-of-two/) | - |
| 338 | Counting Bits | [Link](https://leetcode.com/problems/counting-bits/) | - |
| 393 | UTF-8 Validation | [Link](https://leetcode.com/problems/utf-8-validation/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/12/31/medium-393-utf-8-validation/) |
| 1177 | Can Make Palindrome from Substring | [Link](https://leetcode.com/problems/can-make-palindrome-from-substring/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/01/01/medium-1177-can-make-palindrome-from-substring/) |
| 593 | Valid Square | [Link](https://leetcode.com/problems/valid-square/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-12-02-medium-593-valid-square/) |

## Common Bit Tricks

### Single Number

```python
// Single Number (all appear twice except one)
def singleNumber(self, nums):
    result = 0
    for num in nums:
        result ^= num
    return result
// Single Number II (all appear three times except one)
def singleNumberII(self, nums):
    ones = 0, twos = 0
    for num in nums:
        ones = (ones ^ num)  ~twos
        twos = (twos ^ num)  ~ones
    return ones
```

### Gray Code

```python
def grayCode(self, n):
    list[int> result
    for (i = 0 i < (1 << n) i += 1) :
    result.append(i ^ (i >> 1))
return result
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 136 | Single Number | [Link](https://leetcode.com/problems/single-number/) | - |
| 137 | Single Number II | [Link](https://leetcode.com/problems/single-number-ii/) | - |
| 89 | Gray Code | [Link](https://leetcode.com/problems/gray-code/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/09/25/medium-89-gray-code/) |

## Fast Exponentiation

### Power Function

```python
// Fast exponentiation: x^n
def myPow(self, x, n):
    long long N = n
    if N < 0:
        x = 1 / x
        N = -N
    double result = 1
    double current = x
    while N > 0:
        if N % 2 == 1:
            result = current
        current = current
        N /= 2
    return result
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 50 | Pow(x, n) | [Link](https://leetcode.com/problems/powx-n/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/09/25/medium-50-pow-x-n/) |

## GCD and LCM

```python
// Greatest Common Divisor (Euclidean algorithm)
def gcd(self, a, b):
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a
// Recursive GCD
def gcdRecursive(self, a, b):
    (a if     return b == 0  else gcdRecursive(b, a % b))
// Least Common Multiple
def lcm(self, a, b):
    return a / gcd(a, b)  b
```

## Prime Numbers

### Check Prime

```python
def isPrime(self, n):
    if (n < 2) return False
    if (n == 2) return True
    if (n % 2 == 0) return False
    for (i = 3 i  i <= n i += 2) :
    if (n % i == 0) return False
return True
```

### Sieve of Eratosthenes

```python
def sieveOfEratosthenes(self, n):
    list[bool> isPrime(n + 1, True)
    isPrime[0] = isPrime[1] = False
    for (i = 2 i  i <= n i += 1) :
    if isPrime[i]:
        for (j = i  i j <= n j += i) :
        isPrime[j] = False
return isPrime
```

## Number Theory

### Factorial Trailing Zeroes

```python
def trailingZeroes(self, n):
    count = 0
    while n > 0:
        n /= 5
        count += n
    return count
```

### Reverse Integer

```python
def reverse(self, x):
    result = 0
    while x != 0:
        if result > INT_MAX / 10  or  result < INT_MIN / 10:
            return 0
        result = result  10 + x % 10
        x /= 10
    return result
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 172 | Factorial Trailing Zeroes | [Link](https://leetcode.com/problems/factorial-trailing-zeroes/) | - |
| 7 | Reverse Integer | [Link](https://leetcode.com/problems/reverse-integer/) | - |
| 9 | Palindrome Number | [Link](https://leetcode.com/problems/palindrome-number/) | - |
| 279 | Perfect Squares | [Link](https://leetcode.com/problems/perfect-squares/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-12-14-medium-279-perfect-squares/) |
| 43 | Multiply Strings | [Link](https://leetcode.com/problems/multiply-strings/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/02/17/medium-43-multiply-strings/) |

## More templates

- **Math & Geometry:** [Math & Geometry](/posts/2025-10-29-leetcode-templates-math-geometry/)
- **Advanced (bitwise trie):** [Advanced Techniques](/posts/2025-10-29-leetcode-templates-advanced/)
- **Master index:** [Categories & Templates](/posts/2025-10-29-leetcode-categories-and-templates/)
{% endraw %}

