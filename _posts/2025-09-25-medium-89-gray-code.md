---
layout: post
title: "[Medium] 89. Gray Code"
categories: python gray-code problem-solving
---

# [Medium] 89. Gray Code

An n-bit gray code sequence is a sequence of 2^n integers where:

- Every integer is between 0 and 2^n - 1 (inclusive)
- The first integer is 0
- An integer appears at most once in the sequence
- The binary representation of every pair of adjacent integers differs by exactly one bit
- The binary representation of the first and last integers differs by exactly one bit

Given an integer n, return any valid n-bit gray code sequence.

## Examples

**Example 1:**
```
Input: n = 2
Output: [0,1,3,2]
Explanation:
The binary representation of the gray code sequence is [00, 01, 11, 10].
- 00 and 01 differ by one bit
- 01 and 11 differ by one bit  
- 11 and 10 differ by one bit
- 10 and 00 differ by one bit
[0,2,3,1] is also a valid gray code sequence, whose binary representation is [00, 10, 11, 01].
```

**Example 2:**
```
Input: n = 1
Output: [0,1]
```

## Constraints

- 1 <= n <= 16

## Approach

There are several approaches to generate Gray codes:

1. **Backtracking**: Try all possible sequences and backtrack when invalid
2. **Recursive Construction**: Build Gray code recursively by mirroring previous sequence
3. **Iterative Construction**: Build Gray code iteratively using the same mirroring principle
4. **Mathematical Formula**: Use the formula `i ^ (i >> 1)` for each number

## Solution 1: Backtracking Approach

```python
class Solution:
    def grayCode(self, n: int) -> list[int]:
        result = [0]
        isPresent = {0}
        self.getGreyCode(result, n, isPresent)
        return result
    
    def getGreyCode(self, result: list[int], n: int, isPresent: set) -> bool:
        if len(result) == (1 << n):
            return True
        current = result[-1]
        for i in range(n):
            next_num = current ^ (1 << i)
            if next_num not in isPresent:
                isPresent.add(next_num)
                result.append(next_num)
                if self.getGreyCode(result, n, isPresent):
                    return True
                isPresent.remove(next_num)
                result.pop()
        return False
```

**Time Complexity:** O(2^n) - Exponential time due to backtracking
**Space Complexity:** O(2^n) - For the result vector and visited set

## Solution 2: Recursive Mirror Construction

```python
class Solution:
    def grayCode(self, n: int) -> list[int]:
        result = []
        self.getGreyCode(result, n)
        return result
    
    def getGreyCode(self, result: list[int], n: int) -> None:
        if n == 0:
            result.append(0)
            return
        self.getGreyCode(result, n - 1)
        cur = len(result)
        mask = 1 << (n - 1)
        for i in range(cur - 1, -1, -1):
            result.append(result[i] | mask)
```

**Time Complexity:** O(2^n) - Each recursive call doubles the sequence
**Space Complexity:** O(2^n) - For the result vector

## Solution 3: Iterative Mirror Construction

```python
class Solution:
    def grayCode(self, n: int) -> list[int]:
        result = [0]
        for i in range(1, n + 1):
            pre = len(result)
            mask = 1 << (i - 1)
            for j in range(pre - 1, -1, -1):
                result.append(mask | result[j])
        return result
```

**Time Complexity:** O(2^n) - Builds sequence iteratively
**Space Complexity:** O(2^n) - For the result vector

## Solution 4: Mathematical Formula Approach

```python
class Solution:
    def grayCode(self, n: int) -> list[int]:
        result = []
        for i in range(1 << n):
            result.append(i ^ (i >> 1))
        return result
```

**Time Complexity:** O(2^n) - Generate each Gray code number
**Space Complexity:** O(2^n) - For the result vector

## Solution 5: Alternative Recursive with Global Variable

```python
class Solution:
    def __init__(self):
        self.nextNum = 0
    
    def grayCode(self, n: int) -> list[int]:
        result = []
        self.nextNum = 0
        self.getGreyCode(result, n)
        return result
    
    def getGreyCode(self, result: list[int], n: int) -> None:
        if n == 0:
            result.append(self.nextNum)
            return
        self.getGreyCode(result, n - 1)
        self.nextNum = self.nextNum ^ (1 << (n - 1))
        self.getGreyCode(result, n - 1)
```

**Time Complexity:** O(2^n) - Recursive construction
**Space Complexity:** O(2^n) - For the result vector

## Step-by-Step Example (Solution 3)

For n = 3:

1. Start with [0]
2. i = 1: mirror and add 1-bit mask
   - [0] → [0, 1]
3. i = 2: mirror and add 2-bit mask  
   - [0, 1] → [0, 1, 3, 2]
4. i = 3: mirror and add 3-bit mask
   - [0, 1, 3, 2] → [0, 1, 3, 2, 6, 7, 5, 4]

Final result: [0, 1, 3, 2, 6, 7, 5, 4]

## Key Insights

1. **Mirror Property**: Gray codes can be constructed by mirroring the previous sequence and adding a high-order bit
2. **Bit Manipulation**: Use XOR (`^`) to flip bits and OR (`|`) to set bits
3. **Mathematical Formula**: `i ^ (i >> 1)` directly computes the i-th Gray code
4. **Recursive Structure**: Gray codes have a natural recursive structure

## Solution Comparison

- **Backtracking**: Most intuitive but inefficient for large n
- **Recursive Mirror**: Clean recursive approach, moderate efficiency
- **Iterative Mirror**: Most efficient iterative approach
- **Mathematical Formula**: Most concise and efficient
- **Alternative Recursive**: Uses global state, less clean

## Common Mistakes

1. **Off-by-one errors** in bit shifting (`1 << (n-1)` vs `1 << n`)
2. **Forgetting to reverse** the mirrored sequence
3. **Incorrect bit manipulation** operations
4. **Not handling edge case** n = 0 properly

## Related Problems

- [1238. Circular Permutation in Binary Representation](https://leetcode.com/problems/circular-permutation-in-binary-representation/)
- [89. Gray Code](https://leetcode.com/problems/gray-code/) (this problem)
