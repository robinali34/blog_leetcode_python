---
layout: post
title: "Algorithm Templates: Math & Bit Manipulation"
date: 2025-11-24 00:00:00 -0700
categories: leetcode templates math bit-manipulation
permalink: /posts/2025-11-24-leetcode-templates-math-bit-manipulation/
tags: [leetcode, templates, math, bit-manipulation]
---

{% raw %}
Minimal, copy-paste Python for bit operations, fast exponentiation, GCD/LCM, primes, and number theory. See also [Math & Geometry](/posts/2025-10-29-leetcode-templates-math-geometry/).

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
# Set bit at position i
def set_bit(num: int, i: int) -> int:
    return num | (1 << i)


def clear_bit(num: int, i: int) -> int:
    return num & ~(1 << i)


def toggle_bit(num: int, i: int) -> int:
    return num ^ (1 << i)


def is_bit_set(num: int, i: int) -> int:
    return (num >> i) & 1


def count_set_bits(num: int) -> int:
    count = 0
    while num:
        count += num & 1
        num >>= 1
    return count


def count_set_bits_kernighan(num: int) -> int:
    count = 0
    while num:
        num &= num - 1
        count += 1
    return count

```

### Common Bit Tricks

```python
def lowest_set_bit(num: int) -> int:
    return num & (-num)


def clear_lowest_set_bit(num: int) -> int:
    return num & (num - 1)


def is_power_of_two(num: int) -> bool:
    return num > 0 and (num & (num - 1)) == 0


def next_power_of_two(num: int) -> int:
    num -= 1
    num |= num >> 1
    num |= num >> 2
    num |= num >> 4
    num |= num >> 8
    num |= num >> 16
    num |= num >> 32
    return num + 1


def xor_swap(a: int, b: int) -> tuple[int, int]:
    a ^= b
    b ^= a
    a ^= b
    return a, b

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
# Single Number (all appear twice except one)
def single_number(nums: list[int]) -> int:
    result = 0
    for num in nums:
        result ^= num
    return result


# Single Number II (all appear three times except one)
def single_number_ii(nums: list[int]) -> int:
    ones, twos = 0, 0
    for num in nums:
        ones = (ones ^ num) & ~twos
        twos = (twos ^ num) & ~ones
    return ones

```

### Gray Code

```python
def gray_code(n: int) -> list[int]:
    return [i ^ (i >> 1) for i in range(1 << n)]

```

| ID | Title | Link | Solution |
|---|---|---|---|
| 136 | Single Number | [Link](https://leetcode.com/problems/single-number/) | - |
| 137 | Single Number II | [Link](https://leetcode.com/problems/single-number-ii/) | - |
| 89 | Gray Code | [Link](https://leetcode.com/problems/gray-code/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/09/25/medium-89-gray-code/) |

## Fast Exponentiation

### Power Function

```python
# Fast exponentiation: x^n
def my_pow(x: float, n: int) -> float:
    N = n
    if N < 0:
        x = 1 / x
        N = -N
    result = 1.0
    current = x
    while N > 0:
        if N % 2 == 1:
            result *= current
        current *= current
        N //= 2
    return result

```

| ID | Title | Link | Solution |
|---|---|---|---|
| 50 | Pow(x, n) | [Link](https://leetcode.com/problems/powx-n/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/09/25/medium-50-pow-x-n/) |

## GCD and LCM

```python
def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a


def gcd_recursive(a: int, b: int) -> int:
    return a if b == 0 else gcd_recursive(b, a % b)


def lcm(a: int, b: int) -> int:
    return a // gcd(a, b) * b

```

## Prime Numbers

### Check Prime

```python
def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

```

### Sieve of Eratosthenes

```python
def sieve_of_eratosthenes(n: int) -> list[bool]:
    is_p = [True] * (n + 1)
    is_p[0] = is_p[1] = False
    for i in range(2, int(n**0.5) + 1):
        if is_p[i]:
            for j in range(i * i, n + 1, i):
                is_p[j] = False
    return is_p

```

## Number Theory

### Factorial Trailing Zeroes

```python
def trailing_zeroes(n: int) -> int:
    count = 0
    while n > 0:
        n //= 5
        count += n
    return count

```

### Reverse Integer

```python
def reverse_int(x: int) -> int:
    sign = -1 if x < 0 else 1
    x_abs = abs(x)
    r = 0
    while x_abs:
        r = r * 10 + x_abs % 10
        x_abs //= 10
    r *= sign
    if r < -(2**31) or r > 2**31 - 1:
        return 0
    return r

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

