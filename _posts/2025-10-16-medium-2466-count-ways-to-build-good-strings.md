---
layout: post
title: "[Medium] 2466. Count Ways To Build Good Strings"
date: 2025-10-16 20:01:57 -0700
categories: python dynamic-programming dp problem-solving
---

# [Medium] 2466. Count Ways To Build Good Strings

Given the integers `zero`, `one`, `low`, and `high`, we can construct a string by starting with an empty string, and then at each step perform either of the following:

- Append the character `'0'` `zero` times.
- Append the character `'1'` `one` times.

This can be performed any number of times.

A **good string** is a string constructed by the above process having a **length** between `low` and `high` (inclusive).

Return the number of different **good strings** you can construct satisfying these properties. Since the answer can be large, return it **modulo** `10^9 + 7`.

## Examples

**Example 1:**
```
Input: low = 3, high = 3, zero = 1, one = 1
Output: 8
Explanation: 
One possible valid good string is "011".
It can be constructed as follows: "" -> "0" -> "01" -> "011". 
All binary strings from "000" to "111" are good strings in this example.
```

**Example 2:**
```
Input: low = 2, high = 3, zero = 1, one = 2
Output: 5
Explanation: The good strings are "00", "11", "000", "110", and "011".
```

## Constraints

- `1 <= low <= high <= 10^5`
- `1 <= zero, one <= high`

## Solution 1: Bottom-Up Dynamic Programming

**Time Complexity:** O(high)  
**Space Complexity:** O(high)

Use bottom-up DP to calculate the number of ways to build strings of each length.

```python
class Solution:
private:
    list[int] dp;
    int MOD = 1e9 + 7;
    

    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD = 10**9 + 7
        dp = [0] * (high + 1)
        dp[0] = 1  # Base case: empty string
        
        for i in range(1, high + 1):
            if i - zero >= 0:
                dp[i] = (dp[i] + dp[i - zero]) % MOD
            if i - one >= 0:
                dp[i] = (dp[i] + dp[i - one]) % MOD
        
        result = 0
        for i in range(low, high + 1):
            result = (result + dp[i]) % MOD
        
        return result
```

## Solution 2: Top-Down Dynamic Programming (Memoization)

**Time Complexity:** O(high)  
**Space Complexity:** O(high)

Use top-down DP with memoization to calculate the number of ways recursively.

```python
class Solution:
    def __init__(self):
        self.MOD = 10**9 + 7
    
    def dfs(self, dp: list[int], zero: int, one: int, end: int) -> int:
        if dp[end] != -1:
            return dp[end]
        
        cnt = 0
        if end >= one:
            cnt = (cnt + self.dfs(dp, zero, one, end - one)) % self.MOD
        if end >= zero:
            cnt = (cnt + self.dfs(dp, zero, one, end - zero)) % self.MOD
        
        dp[end] = cnt
        return dp[end]
    
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dp = [-1] * (high + 1)
        dp[0] = 1  # Base case: empty string
        
        result = 0
        for length in range(low, high + 1):
            result = (result + self.dfs(dp, zero, one, length)) % self.MOD
        
        return result
```

## How the Algorithm Works

### Key Insight: Dynamic Programming

The problem can be solved using dynamic programming where `dp[i]` represents the number of ways to build a string of length `i`.

**Recurrence Relation:**
- `dp[i] = dp[i - zero] + dp[i - one]` (if both are valid)
- Base case: `dp[0] = 1` (empty string)

### Step-by-Step Example: `low = 2, high = 3, zero = 1, one = 2`

**Bottom-Up Approach:**

| Length | Ways to Build | Explanation |
|--------|---------------|-------------|
| 0 | 1 | Empty string (base case) |
| 1 | 1 | "0" (from length 0 + zero=1) |
| 2 | 2 | "00" (from length 1 + zero=1), "1" (from length 0 + one=2) |
| 3 | 3 | "000" (from length 2 + zero=1), "01" (from length 1 + one=2) |

**DP Table:**
```
dp = [1, 1, 2, 3]
```

**Answer:** Sum from length 2 to 3 = `dp[2] + dp[3] = 2 + 3 = 5`

### Visual Representation

```
Length 0: "" (1 way)
Length 1: "0" (1 way)
Length 2: "00", "1" (2 ways)
Length 3: "000", "01", "10" (3 ways)

Good strings (length 2-3): "00", "1", "000", "01", "10" = 5 ways
```

## Algorithm Breakdown

### Solution 1: Bottom-Up DP

```python
MOD = 10**9 + 7
dp = [0] * (high + 1)
dp[0] = 1  # Base case

for i in range(1, high + 1):
    if i - zero >= 0:
        dp[i] = (dp[i] + dp[i - zero]) % MOD
    if i - one >= 0:
        dp[i] = (dp[i] + dp[i - one]) % MOD
```

**Process:**
1. Initialize DP array with size `high + 1`
2. Set base case: `dp[0] = 1`
3. For each length `i`, add ways from `i - zero` and `i - one`
4. Sum all valid lengths from `low` to `high`

### Solution 2: Top-Down DP (Memoization)

```python
def dfs(self, int zero, int one, int end) -> int:
    if(dp[end] != -1) return dp[end];  // Memoization check
    
    cnt = 0
    if(end >= one) cnt = (cnt + dfs(zero, one, end - one)) % MOD;
    if(end >= zero) cnt = (cnt + dfs(zero, one, end - zero)) % MOD;
    
    dp[end] = cnt;  // Store result
    return dp[end];
}
```

**Process:**
1. Initialize DP array with `-1` (unvisited)
2. Set base case: `dp[0] = 1`
3. For each length, recursively calculate using memoization
4. Sum all valid lengths from `low` to `high`

## Complexity Analysis

| Approach | Time Complexity | Space Complexity |
|----------|----------------|------------------|
| Bottom-Up DP | O(high) | O(high) |
| Top-Down DP | O(high) | O(high) |

## Edge Cases

1. **Single length range:** `low = high = 1` → Check if `zero = 1` or `one = 1`
2. **Large values:** `high = 10^5` → Use modulo arithmetic
3. **Equal zero and one:** `zero = one = 1` → Standard binary strings
4. **Different zero and one:** `zero = 1, one = 2` → Mixed length increments

## Key Insights

1. **DP State:** `dp[i]` = number of ways to build string of length `i`
2. **Recurrence:** Add ways from previous valid lengths
3. **Base Case:** Empty string has 1 way
4. **Modulo:** Handle large numbers with `10^9 + 7`

## Common Mistakes

1. **Missing base case:** Forgetting `dp[0] = 1`
2. **Wrong recurrence:** Not checking bounds `i - zero >= 0`
3. **Modulo errors:** Not applying modulo consistently
4. **Index bounds:** Accessing `dp[i]` without checking bounds

## Detailed Example Walkthrough

### Example: `low = 2, high = 3, zero = 1, one = 2`

**Bottom-Up DP:**

```
Step 1: Initialize
dp = [1, 0, 0, 0]

Step 2: Calculate dp[1]
i = 1, zero = 1, one = 2
- i - zero = 0 >= 0 → dp[1] += dp[0] = 1
- i - one = -1 < 0 → skip
dp = [1, 1, 0, 0]

Step 3: Calculate dp[2]
i = 2, zero = 1, one = 2
- i - zero = 1 >= 0 → dp[2] += dp[1] = 1
- i - one = 0 >= 0 → dp[2] += dp[0] = 1
dp = [1, 1, 2, 0]

Step 4: Calculate dp[3]
i = 3, zero = 1, one = 2
- i - zero = 2 >= 0 → dp[3] += dp[2] = 2
- i - one = 1 >= 0 → dp[3] += dp[1] = 1
dp = [1, 1, 2, 3]

Step 5: Sum from low to high
Sum = dp[2] + dp[3] = 2 + 3 = 5
```

**Top-Down DP:**

```
dfs(1, 2, 2):
- dp[2] = -1, calculate
- dfs(1, 2, 1) + dfs(1, 2, 0) = 1 + 1 = 2
- dp[2] = 2

dfs(1, 2, 3):
- dp[3] = -1, calculate  
- dfs(1, 2, 2) + dfs(1, 2, 1) = 2 + 1 = 3
- dp[3] = 3

Sum = dp[2] + dp[3] = 2 + 3 = 5
```

## Alternative Approaches

### Approach 1: Brute Force (DFS)
```python
class Solution:

    def countGoodStrings(self, int low, int high, int zero, int one) -> int:
        return dfs(0, low, high, zero, one);
    }
    
    def dfs(self, length: int, low: int, high: int, zero: int, one: int) -> int:
        MOD = 10**9 + 7
        if length > high:
            return 0
        count = 1 if length >= low else 0
        count = (count + self.dfs(length + zero, low, high, zero, one)) % MOD
        count = (count + self.dfs(length + one, low, high, zero, one)) % MOD
        return count
```

**Time Complexity:** O(2^high)  
**Space Complexity:** O(high)

### Approach 2: Mathematical Formula
```python
class Solution:

    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD = 10**9 + 7
        dp = [0] * (high + 1)
        dp[0] = 1
        
        for i in range(1, high + 1):
            if i >= zero:
                dp[i] = (dp[i] + dp[i - zero]) % MOD
            if i >= one:
                dp[i] = (dp[i] + dp[i - one]) % MOD
        
        result = 0
        for i in range(low, high + 1):
            result = (result + dp[i]) % MOD
        
        return result
```

## Related Problems

- [70. Climbing Stairs](https://leetcode.com/problems/climbing-stairs/)
- [322. Coin Change](https://leetcode.com/problems/coin-change/)
- [377. Combination Sum IV](https://leetcode.com/problems/combination-sum-iv/)
- [139. Word Break](https://leetcode.com/problems/word-break/)

## Why These Solutions are Optimal

1. **Optimal Time Complexity:** O(high) is the best possible
2. **Space Efficient:** O(high) space usage
3. **Mathematical Insight:** Converts problem to counting paths
4. **Modulo Handling:** Properly handles large numbers
5. **Two Approaches:** Both bottom-up and top-down are valid
